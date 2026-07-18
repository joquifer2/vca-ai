"""Offline runtime for the AUC-001 post-closure cost-quality model.

This module contains deterministic transformations only. It does not acquire
evidence, call BigQuery, read historical outputs, or produce presentation
artifacts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, Iterable


COMMERCIAL_SIGNAL = "COMMERCIAL"
VALID_COVERAGE_STATUSES = {"matched", "lead_only", "spend_only", "UNKNOWN"}
PROHIBITED_METRIC_NAMES = {"CPL", "CPQL", "CPHQL", "cpl", "cpql", "cphql"}
MONETARY_TOLERANCE_EUR = Decimal("0.01")


@dataclass(frozen=True)
class ThresholdsConfig:
    descriptive_min_matched_leads: int = 1
    ranking_min_matched_leads: int = 10
    recommendation_min_matched_leads: int = 20
    recommendation_min_matched_ab_leads: int = 5


@dataclass
class ModelIssue:
    code: str
    severity: str
    message: str
    ad_id_norm: str | None = None


@dataclass
class LeadAggregate:
    ad_id_norm: str
    lead_count: int = 0
    ab_lead_count: int = 0
    tier_a_count: int = 0
    tier_b_count: int = 0
    raw_ad_ids: set[str] = field(default_factory=set)
    ad_names: set[str] = field(default_factory=set)


@dataclass
class SpendAggregate:
    ad_id_norm: str
    commercial_spend: Decimal = Decimal("0")
    spend_by_signal: dict[str, Decimal] = field(default_factory=dict)
    ad_names: set[str] = field(default_factory=set)


@dataclass
class CostQualityRow:
    ad_id_norm: str
    coverage_status: str
    leads: int = 0
    ab_leads: int = 0
    tier_a: int = 0
    tier_b: int = 0
    commercial_spend: Decimal = Decimal("0")
    cpl_commercial_matched: Decimal | None = None
    qualified_rate_ab_matched: Decimal | None = None
    cost_per_ab_commercial_matched: Decimal | None = None
    cost_per_tier_a_commercial_matched: Decimal | None = None
    sample_status: str = "not_applicable"
    labels: tuple[str, ...] = ()


@dataclass
class CostQualityModel:
    rows: list[CostQualityRow]
    issues: list[ModelIssue]
    aggregates: dict[str, Any]

    @property
    def has_blockers(self) -> bool:
        return any(issue.severity == "blocking" for issue in self.issues)


def normalize_lead_ad_id(ad_id: Any) -> str | None:
    """Normalize lead-side Meta ad ids by removing only an initial ag: prefix."""
    if ad_id is None:
        return None
    value = str(ad_id).strip()
    if not value:
        return None
    if value.startswith("ag:"):
        value = value[3:]
    return value or None


def normalize_spend_ad_id(ad_id: Any) -> str | None:
    if ad_id is None:
        return None
    value = str(ad_id).strip()
    return value or None


def decimal_value(value: Any) -> Decimal:
    if value is None or value == "":
        return Decimal("0")
    return Decimal(str(value))


def safe_divide(numerator: Decimal | int, denominator: int | Decimal) -> Decimal | None:
    denominator_decimal = Decimal(str(denominator))
    if denominator_decimal == 0:
        return None
    return Decimal(str(numerator)) / denominator_decimal


def prepare_lead_aggregates(records: Iterable[dict[str, Any]]) -> tuple[dict[str, LeadAggregate], list[ModelIssue]]:
    aggregates: dict[str, LeadAggregate] = {}
    issues: list[ModelIssue] = []

    for index, record in enumerate(records):
        ad_id_norm = normalize_lead_ad_id(record.get("ad_id"))
        if ad_id_norm is None:
            issues.append(ModelIssue("INVALID_LEAD_AD_ID", "blocking", f"Lead row {index} has null or empty ad_id"))
            continue

        aggregate = aggregates.setdefault(ad_id_norm, LeadAggregate(ad_id_norm=ad_id_norm))
        raw_ad_id = str(record.get("ad_id")).strip()
        aggregate.raw_ad_ids.add(raw_ad_id)

        ad_name = record.get("ad_name")
        if ad_name:
            aggregate.ad_names.add(str(ad_name))

        aggregate.lead_count += 1
        tier = str(record.get("lead_tier") or "").upper()
        if tier in {"A", "B"}:
            aggregate.ab_lead_count += 1
        if tier == "A":
            aggregate.tier_a_count += 1
        if tier == "B":
            aggregate.tier_b_count += 1

    for aggregate in aggregates.values():
        if len(aggregate.raw_ad_ids) > 1:
            issues.append(
                ModelIssue(
                    "AD_ID_NORM_COLLISION",
                    "blocking",
                    "Multiple raw lead ad_id values collapse into one ad_id_norm",
                    aggregate.ad_id_norm,
                )
            )
        if len(aggregate.ad_names) > 1:
            issues.append(
                ModelIssue(
                    "MULTIPLE_AD_NAMES",
                    "warning",
                    "Multiple ad_name labels exist for one ad_id_norm; labels cannot be used as keys",
                    aggregate.ad_id_norm,
                )
            )

    return aggregates, issues


def prepare_spend_aggregates(records: Iterable[dict[str, Any]]) -> tuple[dict[str, SpendAggregate], list[ModelIssue]]:
    aggregates: dict[str, SpendAggregate] = {}
    issues: list[ModelIssue] = []

    for index, record in enumerate(records):
        ad_id_norm = normalize_spend_ad_id(record.get("ad_id"))
        if ad_id_norm is None:
            issues.append(ModelIssue("INVALID_SPEND_AD_ID", "blocking", f"Spend row {index} has null or empty ad_id"))
            continue

        signal = str(record.get("campaign_signal") or "").upper()
        if not signal:
            issues.append(ModelIssue("INVALID_CAMPAIGN_SIGNAL", "blocking", f"Spend row {index} has empty signal", ad_id_norm))
            continue

        spend = decimal_value(record.get("spend_amount"))
        aggregate = aggregates.setdefault(ad_id_norm, SpendAggregate(ad_id_norm=ad_id_norm))
        aggregate.spend_by_signal[signal] = aggregate.spend_by_signal.get(signal, Decimal("0")) + spend
        if signal == COMMERCIAL_SIGNAL:
            aggregate.commercial_spend += spend

        ad_name = record.get("ad_name")
        if ad_name:
            aggregate.ad_names.add(str(ad_name))

    return aggregates, issues


def build_cost_quality_model(
    lead_records: Iterable[dict[str, Any]],
    spend_records: Iterable[dict[str, Any]],
    thresholds: ThresholdsConfig | None = None,
) -> CostQualityModel:
    thresholds = thresholds or ThresholdsConfig()
    leads, lead_issues = prepare_lead_aggregates(lead_records)
    spend, spend_issues = prepare_spend_aggregates(spend_records)
    issues = [*lead_issues, *spend_issues]

    rows: list[CostQualityRow] = []
    for ad_id_norm in sorted(set(leads) | set(spend)):
        lead = leads.get(ad_id_norm)
        spend_row = spend.get(ad_id_norm)
        lead_count = lead.lead_count if lead else 0
        ab_count = lead.ab_lead_count if lead else 0
        tier_a = lead.tier_a_count if lead else 0
        tier_b = lead.tier_b_count if lead else 0
        commercial_spend = spend_row.commercial_spend if spend_row else Decimal("0")

        if lead_count > 0 and commercial_spend > 0:
            coverage_status = "matched"
        elif lead_count > 0:
            coverage_status = "lead_only"
        elif commercial_spend > 0:
            coverage_status = "spend_only"
        else:
            coverage_status = "UNKNOWN"

        labels = sorted((lead.ad_names if lead else set()) | (spend_row.ad_names if spend_row else set()))
        row = CostQualityRow(
            ad_id_norm=ad_id_norm,
            coverage_status=coverage_status,
            leads=lead_count,
            ab_leads=ab_count,
            tier_a=tier_a,
            tier_b=tier_b,
            commercial_spend=commercial_spend,
            labels=tuple(labels),
            sample_status=classify_sample(lead_count, ab_count, coverage_status, thresholds),
        )

        if coverage_status == "matched":
            row.cpl_commercial_matched = safe_divide(commercial_spend, lead_count)
            row.qualified_rate_ab_matched = safe_divide(ab_count, lead_count)
            row.cost_per_ab_commercial_matched = safe_divide(commercial_spend, ab_count)
            row.cost_per_tier_a_commercial_matched = safe_divide(commercial_spend, tier_a)

        rows.append(row)

    aggregates = compute_aggregates(rows)
    issues.extend(validate_invariants(rows, aggregates))
    return CostQualityModel(rows=rows, issues=issues, aggregates=aggregates)


def classify_sample(
    matched_leads: int,
    matched_ab_leads: int,
    coverage_status: str,
    thresholds: ThresholdsConfig,
) -> str:
    if coverage_status != "matched":
        return "not_applicable"
    if (
        matched_leads >= thresholds.recommendation_min_matched_leads
        and matched_ab_leads >= thresholds.recommendation_min_matched_ab_leads
    ):
        return "recommendation_eligible"
    if matched_leads >= thresholds.ranking_min_matched_leads:
        return "ranking_eligible"
    if matched_leads >= thresholds.descriptive_min_matched_leads:
        return "descriptive_only"
    return "sample_insufficient"


def compute_aggregates(rows: Iterable[CostQualityRow]) -> dict[str, Any]:
    rows = list(rows)
    matched = [row for row in rows if row.coverage_status == "matched"]
    lead_only = [row for row in rows if row.coverage_status == "lead_only"]
    spend_only = [row for row in rows if row.coverage_status == "spend_only"]

    commercial_spend = sum((row.commercial_spend for row in rows), Decimal("0"))
    matched_spend = sum((row.commercial_spend for row in matched), Decimal("0"))
    spend_only_spend = sum((row.commercial_spend for row in spend_only), Decimal("0"))
    lead_total = sum(row.leads for row in rows)
    matched_leads = sum(row.leads for row in matched)
    lead_only_leads = sum(row.leads for row in lead_only)
    ab_total = sum(row.ab_leads for row in rows)
    matched_ab_leads = sum(row.ab_leads for row in matched)
    lead_only_ab_leads = sum(row.ab_leads for row in lead_only)

    return {
        "commercial_spend": commercial_spend,
        "matched_spend": matched_spend,
        "spend_only_spend": spend_only_spend,
        "lead_total": lead_total,
        "matched_leads": matched_leads,
        "lead_only_leads": lead_only_leads,
        "ab_total": ab_total,
        "matched_ab_leads": matched_ab_leads,
        "lead_only_ab_leads": lead_only_ab_leads,
        "tier_a_total": sum(row.tier_a for row in rows),
        "matched_tier_a": sum(row.tier_a for row in matched),
        "lead_only_tier_a": sum(row.tier_a for row in lead_only),
        "tier_b_total": sum(row.tier_b for row in rows),
        "matched_tier_b": sum(row.tier_b for row in matched),
        "lead_only_tier_b": sum(row.tier_b for row in lead_only),
        "prepared_ad_count": len(rows),
        "matched_ad_count": len(matched),
        "lead_only_ad_count": len(lead_only),
        "spend_only_ad_count": len(spend_only),
    }


def validate_invariants(rows: list[CostQualityRow], aggregates: dict[str, Any]) -> list[ModelIssue]:
    issues: list[ModelIssue] = []
    decimal_checks = [
        ("commercial_spend", aggregates["commercial_spend"], aggregates["matched_spend"] + aggregates["spend_only_spend"]),
    ]
    integer_checks = [
        ("lead_total", aggregates["lead_total"], aggregates["matched_leads"] + aggregates["lead_only_leads"]),
        ("ab_total", aggregates["ab_total"], aggregates["matched_ab_leads"] + aggregates["lead_only_ab_leads"]),
        ("tier_a_total", aggregates["tier_a_total"], aggregates["matched_tier_a"] + aggregates["lead_only_tier_a"]),
        ("tier_b_total", aggregates["tier_b_total"], aggregates["matched_tier_b"] + aggregates["lead_only_tier_b"]),
        (
            "prepared_ad_count",
            aggregates["prepared_ad_count"],
            aggregates["matched_ad_count"] + aggregates["lead_only_ad_count"] + aggregates["spend_only_ad_count"],
        ),
    ]

    for name, left, right in decimal_checks:
        if abs(left - right) > MONETARY_TOLERANCE_EUR:
            issues.append(ModelIssue("INVARIANT_FAILED", "blocking", f"{name}: {left} != {right}"))
    for name, left, right in integer_checks:
        if left != right:
            issues.append(ModelIssue("INVARIANT_FAILED", "blocking", f"{name}: {left} != {right}"))

    invalid_statuses = [row.coverage_status for row in rows if row.coverage_status not in VALID_COVERAGE_STATUSES]
    if invalid_statuses:
        issues.append(ModelIssue("INVALID_COVERAGE_STATUS", "blocking", ", ".join(invalid_statuses)))

    return issues


def validate_metric_name(metric_name: str) -> None:
    if metric_name in PROHIBITED_METRIC_NAMES:
        raise ValueError(f"Metric name must declare universe and coverage: {metric_name}")
