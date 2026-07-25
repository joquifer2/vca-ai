"""Offline runtime for the AUC-001 post-closure cost-quality model.

This module contains deterministic transformations only. It does not acquire
evidence, call BigQuery, read historical outputs, or produce presentation
artifacts.
"""

from __future__ import annotations

import copy
import json

from dataclasses import dataclass, field
from decimal import Decimal
from pathlib import Path
from typing import Any, Iterable


COMMERCIAL_SIGNAL = "COMMERCIAL"
PROFILE_RELATIVE_PATH = Path("analytical_use_cases") / "auc-001" / "faro-strategic-context-profile.json"
SCHEMA_FAMILY = "auc_001_reconciliation_output"
OUTPUT_SCHEMA_VERSION = "auc_001_reconciliation_output.v1"
MODEL_NAME = "auc_001_canonical_cost_quality_model"
SPECIFICATION_VERSIONS = ("SPEC-012", "SPEC-013")
SCHEMA_STATUS = "active"
DEPRECATED_ALIASES = {
    "matched_spend": "matched_commercial_spend",
    "spend_only_spend": "spend_only_commercial_spend",
}
PASS = "PASS"
FAIL = "FAIL"
VALID_COVERAGE_STATUSES = {"matched", "lead_only", "spend_only", "UNKNOWN", "unknown"}
PROHIBITED_METRIC_NAMES = {"CPL", "CPQL", "CPHQL", "cpl", "cpql", "cphql"}
ECONOMIC_METRIC_KEYWORDS = ("cpl", "cost_per")
MONETARY_TOLERANCE_EUR = Decimal("0.01")
RUNTIME_OUTPUT_RELATIVE_PATH = Path("execution") / "runtime-output.json"
PROTECTED_OUTPUT_NAMESPACES = (
    Path("outputs") / "auc-001" / "2026-06-30",
    Path("outputs") / "auc-001" / "pci-001" / "2026-06-30",
)


def profile_path(repo_root: str | Path | None = None) -> Path:
    base = Path(repo_root) if repo_root is not None else Path(__file__).resolve().parents[1]
    return base / PROFILE_RELATIVE_PATH


def load_strategic_context_profile(repo_root: str | Path | None = None) -> dict[str, Any]:
    path = profile_path(repo_root)
    return json.loads(path.read_text(encoding="utf-8"))


STRATEGIC_CONTEXT_CONSTRAINTS: dict[str, Any] = load_strategic_context_profile()

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
    spend_reconciliation: dict[str, Any] = field(default_factory=dict)
    coverage_reconciliation: dict[str, Any] = field(default_factory=dict)
    schema_family: str = SCHEMA_FAMILY
    output_schema_version: str = OUTPUT_SCHEMA_VERSION
    model_name: str = MODEL_NAME
    specification_versions: tuple[str, ...] = SPECIFICATION_VERSIONS
    schema_status: str = SCHEMA_STATUS
    deprecated_aliases: dict[str, str] = field(default_factory=lambda: dict(DEPRECATED_ALIASES))

    @property
    def has_blockers(self) -> bool:
        return any(issue.severity == "blocking" for issue in self.issues)

    @property
    def required_invariants(self) -> list[dict[str, Any]]:
        return [
            *self.spend_reconciliation.get("invariants", []),
            *self.coverage_reconciliation.get("invariants", []),
        ]

    @property
    def has_failed_required_invariants(self) -> bool:
        return any(invariant.get("result") == FAIL for invariant in self.required_invariants)

    @property
    def is_consumable(self) -> bool:
        return not self.has_blockers and not self.has_failed_required_invariants

    @property
    def structured_output(self) -> dict[str, Any]:
        return {
            "schema_family": self.schema_family,
            "output_schema_version": self.output_schema_version,
            "model_name": self.model_name,
            "specification_versions": list(self.specification_versions),
            "schema_status": self.schema_status,
            "deprecated_aliases": dict(self.deprecated_aliases),
            "is_consumable": self.is_consumable,
            "strategic_context_constraints": copy.deepcopy(STRATEGIC_CONTEXT_CONSTRAINTS),
            "spend_reconciliation": self.spend_reconciliation,
            "coverage_reconciliation": self.coverage_reconciliation,
        }


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


def contract_value(value: Any) -> Any:
    if isinstance(value, Decimal):
        return format(value, "f")
    return value


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

    commercial_spend_keys = {ad_id_norm for ad_id_norm, value in spend.items() if value.commercial_spend > 0}
    rows: list[CostQualityRow] = []
    for ad_id_norm in sorted(set(leads) | commercial_spend_keys):
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
    spend_reconciliation = build_spend_reconciliation(rows, spend)
    coverage_reconciliation = build_coverage_reconciliation(rows, aggregates)
    enrich_aggregates_with_structured_aliases(aggregates, spend_reconciliation)

    issues.extend(validate_invariants(rows, aggregates))
    issues.extend(validate_required_invariant_records([*spend_reconciliation["invariants"], *coverage_reconciliation["invariants"]]))
    return CostQualityModel(
        rows=rows,
        issues=issues,
        aggregates=aggregates,
        spend_reconciliation=spend_reconciliation,
        coverage_reconciliation=coverage_reconciliation,
    )


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
    unknown = [row for row in rows if row.coverage_status.lower() == "unknown"]

    commercial_spend = sum((row.commercial_spend for row in rows), Decimal("0"))
    matched_spend = sum((row.commercial_spend for row in matched), Decimal("0"))
    spend_only_spend = sum((row.commercial_spend for row in spend_only), Decimal("0"))
    unknown_spend = sum((row.commercial_spend for row in unknown), Decimal("0"))
    lead_total = sum(row.leads for row in rows)
    matched_leads = sum(row.leads for row in matched)
    lead_only_leads = sum(row.leads for row in lead_only)
    unknown_leads = sum(row.leads for row in unknown)
    ab_total = sum(row.ab_leads for row in rows)
    matched_ab_leads = sum(row.ab_leads for row in matched)
    lead_only_ab_leads = sum(row.ab_leads for row in lead_only)
    unknown_ab_leads = sum(row.ab_leads for row in unknown)

    return {
        "commercial_spend": commercial_spend,
        "matched_spend": matched_spend,
        "matched_commercial_spend": matched_spend,
        "spend_only_spend": spend_only_spend,
        "spend_only_commercial_spend": spend_only_spend,
        "unknown_commercial_spend": unknown_spend,
        "lead_total": lead_total,
        "matched_leads": matched_leads,
        "lead_only_leads": lead_only_leads,
        "unknown_leads": unknown_leads,
        "ab_total": ab_total,
        "matched_ab_leads": matched_ab_leads,
        "lead_only_ab_leads": lead_only_ab_leads,
        "unknown_ab_leads": unknown_ab_leads,
        "tier_a_total": sum(row.tier_a for row in rows),
        "matched_tier_a": sum(row.tier_a for row in matched),
        "lead_only_tier_a": sum(row.tier_a for row in lead_only),
        "unknown_tier_a": sum(row.tier_a for row in unknown),
        "tier_b_total": sum(row.tier_b for row in rows),
        "matched_tier_b": sum(row.tier_b for row in matched),
        "lead_only_tier_b": sum(row.tier_b for row in lead_only),
        "unknown_tier_b": sum(row.tier_b for row in unknown),
        "prepared_ad_count": len(rows),
        "matched_ad_count": len(matched),
        "lead_only_ad_count": len(lead_only),
        "spend_only_ad_count": len(spend_only),
        "unknown_ad_count": len(unknown),
    }


def enrich_aggregates_with_structured_aliases(
    aggregates: dict[str, Any],
    spend_reconciliation: dict[str, Any],
) -> None:
    aggregates["total_spend_all_signals"] = Decimal(spend_reconciliation["total_spend_all_signals"])
    aggregates["non_commercial_spend"] = Decimal(spend_reconciliation["non_commercial_spend"])
    aggregates["spend_by_signal"] = {
        signal: Decimal(value) for signal, value in spend_reconciliation["spend_by_signal"].items()
    }
    aggregates["non_commercial_spend_by_signal"] = {
        signal: Decimal(value) for signal, value in spend_reconciliation["non_commercial_spend_by_signal"].items()
    }


def build_spend_reconciliation(
    rows: list[CostQualityRow],
    spend: dict[str, SpendAggregate],
) -> dict[str, Any]:
    spend_by_signal: dict[str, Decimal] = {}
    for aggregate in spend.values():
        for signal, amount in aggregate.spend_by_signal.items():
            spend_by_signal[signal] = spend_by_signal.get(signal, Decimal("0")) + amount

    total_spend_all_signals = sum(spend_by_signal.values(), Decimal("0"))
    commercial_spend = spend_by_signal.get(COMMERCIAL_SIGNAL, Decimal("0"))
    matched_commercial_spend = sum(
        (row.commercial_spend for row in rows if row.coverage_status == "matched"),
        Decimal("0"),
    )
    spend_only_commercial_spend = sum(
        (row.commercial_spend for row in rows if row.coverage_status == "spend_only"),
        Decimal("0"),
    )
    non_commercial_spend_by_signal = {
        signal: amount for signal, amount in spend_by_signal.items() if signal != COMMERCIAL_SIGNAL
    }
    non_commercial_spend = sum(non_commercial_spend_by_signal.values(), Decimal("0"))

    invariants = [
        build_invariant(
            "total_spend_all_signals_identity",
            "total_spend_all_signals = commercial_spend + non_commercial_spend",
            total_spend_all_signals,
            commercial_spend + non_commercial_spend,
            MONETARY_TOLERANCE_EUR,
        ),
        build_invariant(
            "commercial_spend_identity",
            "commercial_spend = matched_commercial_spend + spend_only_commercial_spend",
            commercial_spend,
            matched_commercial_spend + spend_only_commercial_spend,
            MONETARY_TOLERANCE_EUR,
        ),
        build_invariant(
            "non_commercial_spend_by_signal_identity",
            "non_commercial_spend = sum(non_commercial_spend_by_signal)",
            non_commercial_spend,
            sum(non_commercial_spend_by_signal.values(), Decimal("0")),
            MONETARY_TOLERANCE_EUR,
        ),
        build_invariant(
            "total_spend_by_signal_identity",
            "total_spend_all_signals = sum(spend_by_signal)",
            total_spend_all_signals,
            sum(spend_by_signal.values(), Decimal("0")),
            MONETARY_TOLERANCE_EUR,
        ),
    ]

    return {
        "total_spend_all_signals": contract_value(total_spend_all_signals),
        "spend_by_signal": {signal: contract_value(amount) for signal, amount in sorted(spend_by_signal.items())},
        "commercial_spend": contract_value(commercial_spend),
        "matched_commercial_spend": contract_value(matched_commercial_spend),
        "spend_only_commercial_spend": contract_value(spend_only_commercial_spend),
        "matched_spend": contract_value(matched_commercial_spend),
        "spend_only_spend": contract_value(spend_only_commercial_spend),
        "non_commercial_spend": contract_value(non_commercial_spend),
        "non_commercial_spend_by_signal": {
            signal: contract_value(amount) for signal, amount in sorted(non_commercial_spend_by_signal.items())
        },
        "invariants": invariants,
    }


def build_coverage_reconciliation(
    rows: list[CostQualityRow],
    aggregates: dict[str, Any],
) -> dict[str, Any]:
    coverage = {
        "matched": build_coverage_bucket([row for row in rows if row.coverage_status == "matched"]),
        "lead_only": build_coverage_bucket([row for row in rows if row.coverage_status == "lead_only"]),
        "spend_only": build_coverage_bucket([row for row in rows if row.coverage_status == "spend_only"]),
        "unknown": build_coverage_bucket([row for row in rows if row.coverage_status.lower() == "unknown"]),
    }
    coverage["matched"]["matched_commercial_spend"] = coverage["matched"]["commercial_spend"]
    coverage["spend_only"]["spend_only_commercial_spend"] = coverage["spend_only"]["commercial_spend"]
    coverage["unknown"]["reason_codes"] = []
    invariants = [
        build_invariant(
            "lead_total_identity",
            "lead_total = matched.leads + lead_only.leads + unknown.leads",
            aggregates["lead_total"],
            coverage["matched"]["leads"] + coverage["lead_only"]["leads"] + coverage["unknown"]["leads"],
        ),
        build_invariant(
            "ab_total_identity",
            "ab_total = matched.ab_leads + lead_only.ab_leads + unknown.ab_leads",
            aggregates["ab_total"],
            coverage["matched"]["ab_leads"] + coverage["lead_only"]["ab_leads"] + coverage["unknown"]["ab_leads"],
        ),
        build_invariant(
            "tier_a_total_identity",
            "tier_a_total = matched.tier_a + lead_only.tier_a + unknown.tier_a",
            aggregates["tier_a_total"],
            coverage["matched"]["tier_a"] + coverage["lead_only"]["tier_a"] + coverage["unknown"]["tier_a"],
        ),
        build_invariant(
            "tier_b_total_identity",
            "tier_b_total = matched.tier_b + lead_only.tier_b + unknown.tier_b",
            aggregates["tier_b_total"],
            coverage["matched"]["tier_b"] + coverage["lead_only"]["tier_b"] + coverage["unknown"]["tier_b"],
        ),
        build_invariant(
            "commercial_spend_coverage_identity",
            "commercial_spend = matched.matched_commercial_spend + spend_only.spend_only_commercial_spend + unknown.commercial_spend",
            aggregates["commercial_spend"],
            Decimal(coverage["matched"]["matched_commercial_spend"])
            + Decimal(coverage["spend_only"]["spend_only_commercial_spend"])
            + Decimal(coverage["unknown"]["commercial_spend"]),
            MONETARY_TOLERANCE_EUR,
        ),
        build_invariant(
            "prepared_ad_count_identity",
            "prepared_ad_count = matched.ad_count + lead_only.ad_count + spend_only.ad_count + unknown.ad_count",
            aggregates["prepared_ad_count"],
            coverage["matched"]["ad_count"]
            + coverage["lead_only"]["ad_count"]
            + coverage["spend_only"]["ad_count"]
            + coverage["unknown"]["ad_count"],
        ),
    ]
    coverage["invariants"] = invariants
    return coverage


def build_coverage_bucket(rows: list[CostQualityRow]) -> dict[str, Any]:
    return {
        "ad_count": len(rows),
        "leads": sum(row.leads for row in rows),
        "ab_leads": sum(row.ab_leads for row in rows),
        "tier_a": sum(row.tier_a for row in rows),
        "tier_b": sum(row.tier_b for row in rows),
        "commercial_spend": contract_value(sum((row.commercial_spend for row in rows), Decimal("0"))),
    }


def build_invariant(
    name: str,
    expression: str,
    left_value: Decimal | int,
    right_value: Decimal | int,
    tolerance: Decimal | None = None,
) -> dict[str, Any]:
    if tolerance is None:
        result = PASS if left_value == right_value else FAIL
    else:
        result = PASS if abs(Decimal(left_value) - Decimal(right_value)) <= tolerance else FAIL
    return {
        "name": name,
        "expression": expression,
        "left_value": contract_value(left_value),
        "right_value": contract_value(right_value),
        "tolerance": contract_value(tolerance) if tolerance is not None else None,
        "result": result,
    }


def validate_invariants(rows: list[CostQualityRow], aggregates: dict[str, Any]) -> list[ModelIssue]:
    issues: list[ModelIssue] = []
    decimal_checks = [
        (
            "commercial_spend",
            aggregates["commercial_spend"],
            aggregates["matched_commercial_spend"] + aggregates["spend_only_commercial_spend"],
        ),
    ]
    integer_checks = [
        (
            "lead_total",
            aggregates["lead_total"],
            aggregates["matched_leads"] + aggregates["lead_only_leads"] + aggregates["unknown_leads"],
        ),
        (
            "ab_total",
            aggregates["ab_total"],
            aggregates["matched_ab_leads"] + aggregates["lead_only_ab_leads"] + aggregates["unknown_ab_leads"],
        ),
        (
            "tier_a_total",
            aggregates["tier_a_total"],
            aggregates["matched_tier_a"] + aggregates["lead_only_tier_a"] + aggregates["unknown_tier_a"],
        ),
        (
            "tier_b_total",
            aggregates["tier_b_total"],
            aggregates["matched_tier_b"] + aggregates["lead_only_tier_b"] + aggregates["unknown_tier_b"],
        ),
        (
            "prepared_ad_count",
            aggregates["prepared_ad_count"],
            aggregates["matched_ad_count"]
            + aggregates["lead_only_ad_count"]
            + aggregates["spend_only_ad_count"]
            + aggregates["unknown_ad_count"],
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


def validate_required_invariant_records(invariants: Iterable[dict[str, Any]]) -> list[ModelIssue]:
    issues: list[ModelIssue] = []
    for invariant in invariants:
        result = invariant.get("result")
        if result == FAIL:
            issues.append(
                ModelIssue(
                    "REQUIRED_INVARIANT_FAILED",
                    "blocking",
                    f"{invariant.get('name')}: {invariant.get('expression')}",
                )
            )
        elif result != PASS:
            issues.append(
                ModelIssue(
                    "INVALID_INVARIANT_RESULT",
                    "blocking",
                    f"{invariant.get('name')}: result must be PASS or FAIL",
                )
            )
    return issues


def validate_metric_name(metric_name: str) -> None:
    if metric_name in PROHIBITED_METRIC_NAMES:
        raise ValueError(f"Metric name must declare universe and coverage: {metric_name}")


def validate_structured_metric_request(
    metric_name: str,
    *,
    signal: str | None,
    coverage_status: str | None,
    universe: str | None,
    numerator_source: str | None = None,
    denominator_value: int | Decimal | None = None,
) -> None:
    """Validate the structured output metric universe without changing SPEC-012 policy."""
    validate_metric_name(metric_name)
    if not signal or not coverage_status or not universe:
        raise ValueError("Metric request must declare signal, coverage_status, and universe")
    if denominator_value is not None and Decimal(str(denominator_value)) == 0:
        raise ValueError("Metric denominator cannot be zero")

    normalized_metric_name = metric_name.lower()
    is_economic_metric = any(keyword in normalized_metric_name for keyword in ECONOMIC_METRIC_KEYWORDS)
    if is_economic_metric:
        if signal.upper() != COMMERCIAL_SIGNAL:
            raise ValueError("Economic metrics must use COMMERCIAL spend only")
        if coverage_status != "matched" or universe != "commercial_matched":
            raise ValueError("Economic metrics must use the commercial matched universe")
        if numerator_source == "total_spend_all_signals":
            raise ValueError("Economic metrics cannot use total_spend_all_signals as numerator")

def model_issue_to_dict(issue: ModelIssue) -> dict[str, Any]:
    return {
        "code": issue.code,
        "severity": issue.severity,
        "message": issue.message,
        "ad_id_norm": issue.ad_id_norm,
    }


def normalize_namespace_path(namespace_path: str | Path) -> Path:
    return Path(namespace_path).expanduser()


def is_protected_output_namespace(namespace_path: str | Path, repo_root: str | Path | None = None) -> bool:
    namespace = normalize_namespace_path(namespace_path)
    base = Path(repo_root).expanduser() if repo_root is not None else Path.cwd()
    try:
        relative_namespace = namespace.resolve().relative_to(base.resolve())
    except ValueError:
        relative_namespace = namespace

    normalized_parts = tuple(part.lower() for part in relative_namespace.parts)
    for protected in PROTECTED_OUTPUT_NAMESPACES:
        protected_parts = tuple(part.lower() for part in protected.parts)
        if normalized_parts == protected_parts:
            return True
    return False


def build_runtime_output_payload(
    model: CostQualityModel,
    *,
    execution_metadata: dict[str, Any],
    namespace_path: str | Path,
    runtime_output_path: str | Path | None = None,
) -> dict[str, Any]:
    """Build the physical runtime-output JSON payload from structured runtime output."""
    payload = dict(model.structured_output)
    runtime_path = Path(runtime_output_path) if runtime_output_path is not None else Path(namespace_path) / RUNTIME_OUTPUT_RELATIVE_PATH
    metadata = dict(execution_metadata)
    blockers = [model_issue_to_dict(issue) for issue in model.issues if issue.severity == "blocking"]

    payload.update(
        {
            "execution_id": metadata.get("execution_id"),
            "period_start": metadata.get("period_start"),
            "period_end": metadata.get("period_end"),
            "runtime": metadata.get("runtime", model.model_name),
            "data_provider": metadata.get("data_provider"),
            "source_tables": list(metadata.get("source_tables", [])),
            "input_hashes": dict(metadata.get("input_hashes", {})),
            "namespace": str(namespace_path).replace("\\", "/"),
            "runtime_output_path": str(runtime_path).replace("\\", "/"),
            "issues": [model_issue_to_dict(issue) for issue in model.issues],
            "package_status": {
                "is_complete": model.is_consumable,
                "is_consumable": model.is_consumable,
                "blockers": blockers,
            },
        }
    )
    return payload


def validate_runtime_output_payload(payload: dict[str, Any]) -> list[str]:
    missing = []
    required_fields = [
        "execution_id",
        "period_start",
        "period_end",
        "model_name",
        "schema_family",
        "output_schema_version",
        "specification_versions",
        "deprecated_aliases",
        "spend_reconciliation",
        "coverage_reconciliation",
        "is_consumable",
        "strategic_context_constraints",
        "runtime",
        "data_provider",
        "source_tables",
        "input_hashes",
        "namespace",
        "runtime_output_path",
        "issues",
        "package_status",
    ]
    for field_name in required_fields:
        if field_name not in payload or payload[field_name] is None:
            missing.append(field_name)
    return missing


def persist_runtime_output(
    model: CostQualityModel,
    namespace_path: str | Path,
    *,
    execution_metadata: dict[str, Any],
    repo_root: str | Path | None = None,
    allow_overwrite: bool = False,
) -> dict[str, Any]:
    """Persist SPEC-013 runtime output and return packaging status."""
    namespace = normalize_namespace_path(namespace_path)
    runtime_output_path = namespace / RUNTIME_OUTPUT_RELATIVE_PATH

    if is_protected_output_namespace(namespace, repo_root=repo_root):
        return {
            "write_status": "FAIL",
            "runtime_output_path": str(runtime_output_path).replace("\\", "/"),
            "is_consumable": model.is_consumable,
            "is_package_complete": False,
            "error": "PROTECTED_NAMESPACE",
            "issues": [
                {
                    "code": "PROTECTED_NAMESPACE",
                    "severity": "blocking",
                    "message": "Refusing to write runtime-output.json into a protected historical namespace",
                    "ad_id_norm": None,
                }
            ],
        }

    payload = build_runtime_output_payload(
        model,
        execution_metadata=execution_metadata,
        namespace_path=namespace,
        runtime_output_path=runtime_output_path,
    )
    missing_fields = validate_runtime_output_payload(payload)
    if missing_fields:
        return {
            "write_status": "FAIL",
            "runtime_output_path": str(runtime_output_path).replace("\\", "/"),
            "is_consumable": model.is_consumable,
            "is_package_complete": False,
            "error": "MISSING_RUNTIME_METADATA",
            "missing_fields": missing_fields,
            "payload": payload,
        }

    try:
        runtime_output_path.parent.mkdir(parents=True, exist_ok=True)
        if runtime_output_path.exists() and not allow_overwrite:
            raise FileExistsError(f"Runtime output already exists: {runtime_output_path}")
        runtime_output_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    except OSError as exc:
        return {
            "write_status": "FAIL",
            "runtime_output_path": str(runtime_output_path).replace("\\", "/"),
            "is_consumable": model.is_consumable,
            "is_package_complete": False,
            "error": "WRITE_FAILED",
            "message": str(exc),
            "payload": payload,
        }

    return {
        "write_status": "PASS",
        "runtime_output_path": str(runtime_output_path).replace("\\", "/"),
        "is_consumable": model.is_consumable,
        "is_package_complete": model.is_consumable,
        "error": None,
        "payload": payload,
    }