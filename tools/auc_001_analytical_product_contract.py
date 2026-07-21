"""AUC-001 analytical product contract runtime helpers.

This module materializes SPEC-014 as deterministic local structures and
validators. It does not acquire evidence, call BigQuery, read historical
outputs, or write analytical products.
"""

from __future__ import annotations

import hashlib
import json

from dataclasses import dataclass, field
from typing import Any, Iterable, Mapping


CONTRACT_ID = "AUC-001-ANALYTICAL-PRODUCT-CONTRACT"
CONTRACT_VERSION = "spec-014.v1"
CONTRACT_SPECIFICATION = "SPEC-014"
PRODUCT_SCHEMA_FAMILY = "auc_001_analytical_product_contract"
PRODUCT_SCHEMA_VERSION = "auc_001_analytical_product_contract.v1"

COVERAGE_COMPLETE = "complete"
COVERAGE_PARTIAL = "partial"
COVERAGE_NOT_AVAILABLE = "not_available"
COVERAGE_NOT_APPLICABLE = "not_applicable"
COVERAGE_UNKNOWN = "UNKNOWN"
COVERAGE_BLOCKED = "blocked"

VALID_PRODUCT_COVERAGE_STATES = {
    COVERAGE_COMPLETE,
    COVERAGE_PARTIAL,
    COVERAGE_NOT_AVAILABLE,
    COVERAGE_NOT_APPLICABLE,
    COVERAGE_UNKNOWN,
    COVERAGE_BLOCKED,
}

RECOMMENDATION_MEASURABLE_EXPERIMENT = "measurable_experiment"
RECOMMENDATION_VERIFIABLE_ACTION = "verifiable_action"
RECOMMENDATION_NON_ACTIONABLE_HYPOTHESIS = "non_actionable_hypothesis"

VALID_RECOMMENDATION_CATEGORIES = {
    RECOMMENDATION_MEASURABLE_EXPERIMENT,
    RECOMMENDATION_VERIFIABLE_ACTION,
    RECOMMENDATION_NON_ACTIONABLE_HYPOTHESIS,
}

MANDATORY_DEPTH_FIELDS = (
    "evidence",
    "comparison",
    "interpretation",
    "business_implication",
    "limitation_or_uncertainty",
    "conclusion_or_hypothesis",
    "traceability",
)

ROBUSTNESS_FIELDS = (
    "denominator",
    "observed_volume",
    "coverage",
    "granularity",
    "comparator",
    "sample_sufficiency",
)

PROHIBITED_EVIDENCE_INTERPRETIVE_FIELDS = {
    "finding",
    "findings",
    "opportunity",
    "opportunities",
    "recommendation",
    "recommendations",
    "interpretation",
    "business_implication",
}

PROHIBITED_KNOWLEDGE_FIELDS = {
    "new_evidence",
    "sql_query",
    "bigquery_request_id",
    "recommendation",
    "recommendations",
}

PROHIBITED_PRESENTATION_FIELDS = {
    "new_evidence",
    "new_knowledge",
    "new_recommendation",
    "coverage_state_overrides",
}

PROHIBITED_PRESENTATION_SECTION_FIELDS = PROHIBITED_PRESENTATION_FIELDS | {
    "evidence",
    "knowledge",
    "recommendation",
    "recommendations",
    "coverage_states",
    "unknowns",
    "limitations",
}


@dataclass(frozen=True)
class AnalyticalQuestionDefinition:
    question_id: str
    taxonomy: str
    criticality: str
    required_view: str
    minimum_evidence: str
    minimum_interpretation: str
    recommendation_requirement: str
    valid_states: tuple[str, ...]
    applicability_condition: str | None = None

    @property
    def is_mandatory(self) -> bool:
        return self.taxonomy == "mandatory"

    @property
    def is_critical(self) -> bool:
        return self.criticality in {"high", "medium-high"}

    def to_dict(self) -> dict[str, Any]:
        return {
            "question_id": self.question_id,
            "taxonomy": self.taxonomy,
            "criticality": self.criticality,
            "required_view": self.required_view,
            "minimum_evidence": self.minimum_evidence,
            "minimum_interpretation": self.minimum_interpretation,
            "recommendation_requirement": self.recommendation_requirement,
            "valid_states": list(self.valid_states),
            "applicability_condition": self.applicability_condition,
        }


@dataclass(frozen=True)
class RobustnessRecord:
    denominator: Any
    observed_volume: Any
    coverage: str
    granularity: str
    comparator: str
    sample_sufficiency: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "denominator": self.denominator,
            "observed_volume": self.observed_volume,
            "coverage": self.coverage,
            "granularity": self.granularity,
            "comparator": self.comparator,
            "sample_sufficiency": self.sample_sufficiency,
        }


@dataclass(frozen=True)
class CoverageMatrixRow:
    question_id: str
    coverage_state: str
    justification: str
    evidence_refs: tuple[str, ...] = ()
    depth: Mapping[str, Any] = field(default_factory=dict)
    robustness: RobustnessRecord | None = None
    impact: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "question_id": self.question_id,
            "coverage_state": self.coverage_state,
            "justification": self.justification,
            "evidence_refs": list(self.evidence_refs),
            "depth": dict(self.depth),
            "robustness": self.robustness.to_dict() if self.robustness else None,
            "impact": self.impact,
        }


@dataclass(frozen=True)
class ProductContractIssue:
    code: str
    severity: str
    message: str
    question_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "severity": self.severity,
            "message": self.message,
            "question_id": self.question_id,
        }


@dataclass(frozen=True)
class CommonProductCore:
    period: Mapping[str, Any]
    scope: Mapping[str, Any]
    sources: tuple[str, ...]
    evidence_refs: tuple[str, ...]
    canonical_metrics: Mapping[str, Any]
    coverage_matrix: tuple[CoverageMatrixRow, ...]
    knowledge_claims: tuple[Mapping[str, Any], ...]
    recommendations: tuple[Mapping[str, Any], ...]
    limitations: tuple[str, ...]
    unknowns: tuple[str, ...]

    @property
    def semantic_fingerprint(self) -> str:
        payload = {
            "period": dict(self.period),
            "scope": dict(self.scope),
            "sources": list(self.sources),
            "evidence_refs": list(self.evidence_refs),
            "canonical_metrics": dict(self.canonical_metrics),
            "coverage_matrix": [row.to_dict() for row in self.coverage_matrix],
            "knowledge_claims": [dict(item) for item in self.knowledge_claims],
            "recommendations": [dict(item) for item in self.recommendations],
            "limitations": list(self.limitations),
            "unknowns": list(self.unknowns),
        }
        canonical = json.dumps(payload, sort_keys=True, default=str, separators=(",", ":"))
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    def to_dict(self) -> dict[str, Any]:
        return {
            "period": dict(self.period),
            "scope": dict(self.scope),
            "sources": list(self.sources),
            "evidence_refs": list(self.evidence_refs),
            "canonical_metrics": dict(self.canonical_metrics),
            "coverage_matrix": [row.to_dict() for row in self.coverage_matrix],
            "knowledge_claims": [dict(item) for item in self.knowledge_claims],
            "recommendations": [dict(item) for item in self.recommendations],
            "limitations": list(self.limitations),
            "unknowns": list(self.unknowns),
            "semantic_fingerprint": self.semantic_fingerprint,
        }


@dataclass(frozen=True)
class ProductProjection:
    projection_type: str
    common_core_fingerprint: str
    coverage_states: Mapping[str, str]
    unknowns: tuple[str, ...]
    limitations: tuple[str, ...]
    sections: tuple[Mapping[str, Any], ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "projection_type": self.projection_type,
            "common_core_fingerprint": self.common_core_fingerprint,
            "coverage_states": dict(self.coverage_states),
            "unknowns": list(self.unknowns),
            "limitations": list(self.limitations),
            "sections": [dict(section) for section in self.sections],
        }


@dataclass(frozen=True)
class AnalyticalProductContract:
    contract_id: str
    version: str
    schema_family: str
    schema_version: str
    specification: str
    coverage_matrix: tuple[AnalyticalQuestionDefinition, ...]
    required_views: tuple[str, ...]
    depth_fields: tuple[str, ...]
    robustness_fields: tuple[str, ...]
    coverage_states: tuple[str, ...]
    recommendation_categories: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "contract_id": self.contract_id,
            "version": self.version,
            "schema_family": self.schema_family,
            "schema_version": self.schema_version,
            "specification": self.specification,
            "coverage_matrix": [row.to_dict() for row in self.coverage_matrix],
            "required_views": list(self.required_views),
            "depth_fields": list(self.depth_fields),
            "robustness_fields": list(self.robustness_fields),
            "coverage_states": list(self.coverage_states),
            "recommendation_categories": list(self.recommendation_categories),
        }


QUESTION_DEFINITIONS: tuple[AnalyticalQuestionDefinition, ...] = (
    AnalyticalQuestionDefinition("AQ-001", "mandatory", "high", "volume_and_capture", "leads, period, temporal coverage", "capture rhythm and volume changes without absorbing quality evolution", "not_required_unless_actionable_change", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_UNKNOWN, COVERAGE_BLOCKED)),
    AnalyticalQuestionDefinition("AQ-002", "mandatory", "high", "faro_quality", "tier distribution, A/B, Tier A, denominators", "quality distribution and valuable segment weight", "not_required_unless_clear_opportunity", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_BLOCKED)),
    AnalyticalQuestionDefinition("AQ-003", "mandatory", "high", "reconciled_cost_quality", "spend, matched leads, coverage, SPEC-012 metrics", "economic efficiency with explicit universe", "required_if_economic_optimization", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_BLOCKED)),
    AnalyticalQuestionDefinition("AQ-004", "mandatory", "high", "campaign_adset", "volume, quality, cost when reconciled", "volume-quality-cost comparison and coverage bias", "required_if_campaign_prioritization", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_BLOCKED)),
    AnalyticalQuestionDefinition("AQ-005", "mandatory", "medium-high", "ad_creative", "ad_id_norm or equivalent technical id, ad metrics, ad_name if available", "value, waste or dependency without unvalidated creative causality", "required_if_creative_test", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_UNKNOWN, COVERAGE_NOT_AVAILABLE, COVERAGE_BLOCKED)),
    AnalyticalQuestionDefinition("AQ-006", "mandatory", "high", "explanatory_signals", "available FARO, form or qualification signals", "observed associations, not causality", "not_required_unless_testable_hypothesis", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_UNKNOWN, COVERAGE_NOT_AVAILABLE, COVERAGE_BLOCKED)),
    AnalyticalQuestionDefinition("AQ-007", "mandatory", "high", "tradeoff", "volume-quality-cost comparisons", "business tension and opportunity cost", "required_if_redistribution", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_BLOCKED)),
    AnalyticalQuestionDefinition("AQ-008", "mandatory", "medium-high", "concentration_dependency", "distribution by entity, segment or period", "dependency or concentration risk", "required_if_mitigation", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_UNKNOWN, COVERAGE_NOT_AVAILABLE, COVERAGE_BLOCKED)),
    AnalyticalQuestionDefinition("AQ-009", "mandatory", "high", "temporal", "monthly quality series and weekly series if comparable", "quality evolution, interpretable change, stability and partial-week limits", "required_if_temporal_action", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_UNKNOWN, COVERAGE_BLOCKED)),
    AnalyticalQuestionDefinition("AQ-010", "mandatory", "high", "opportunities_actions", "approved and traceable Knowledge Set", "priority, expected impact and uncertainty", "action_must_be_classified", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_UNKNOWN, COVERAGE_NOT_AVAILABLE, COVERAGE_BLOCKED)),
    AnalyticalQuestionDefinition("AQ-011", "mandatory", "high", "limits_coverage", "coverage, reconciliation, missingness, UNKNOWN and not_available", "impact of limits on reading and decision", "not_applicable", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_UNKNOWN, COVERAGE_BLOCKED)),
    AnalyticalQuestionDefinition("CQ-001", "conditional", "conditional", "platform_surface", "comparable dimension", "segmented differences and cautions", "only_if_segmented_action", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_NOT_AVAILABLE, COVERAGE_NOT_APPLICABLE), "dimension available and comparable"),
    AnalyticalQuestionDefinition("CQ-002", "conditional", "conditional", "post_lead_crm", "ticket_status or other authorized dimension", "quality FARO separated from commercial status", "only_if_sales_process_action", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_NOT_AVAILABLE, COVERAGE_NOT_APPLICABLE), "authorized post-lead source with sufficient coverage"),
    AnalyticalQuestionDefinition("CQ-003", "conditional", "conditional", "capi_events", "current authorized event evidence", "descriptive maturity or limitation", "only_if_tracking_experiment", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_NOT_AVAILABLE, COVERAGE_NOT_APPLICABLE), "authorized CAPI/event evidence exists"),
    AnalyticalQuestionDefinition("CQ-004", "conditional", "conditional", "high_quality", "Tier A or equivalent with sufficient volume", "robust reading or insufficiency declaration", "only_if_high_quality_action", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_UNKNOWN, COVERAGE_NOT_APPLICABLE), "denominator and volume allow comparability"),
    AnalyticalQuestionDefinition("CQ-005", "conditional", "conditional", "creative_metadata", "available and traceable metadata", "descriptive patterns without unauthorized visual inference", "only_if_creative_test", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_NOT_AVAILABLE, COVERAGE_NOT_APPLICABLE), "metadata beyond ad_name is available"),
    AnalyticalQuestionDefinition("CQ-006", "conditional", "conditional", "conversion_revenue", "reconciled commercial source", "business-quality relation with limits", "only_if_commercial_action", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_NOT_AVAILABLE, COVERAGE_NOT_APPLICABLE), "authorized and reconciled sales source exists"),
    AnalyticalQuestionDefinition("CQ-007", "conditional", "conditional", "complete_weekly", "complete weeks or explicit comparability rules", "weekly changes and partiality warning", "only_if_temporal_decision", (COVERAGE_COMPLETE, COVERAGE_PARTIAL, COVERAGE_NOT_AVAILABLE, COVERAGE_NOT_APPLICABLE), "complete weeks or partial-week rules exist"),
    AnalyticalQuestionDefinition("NAQ-001", "not_applicable", "out_of_boundary", "causal_creative_effect", "none", "causal effect requires experiment", "not_applicable", (COVERAGE_NOT_APPLICABLE,)),
    AnalyticalQuestionDefinition("NAQ-002", "not_applicable", "out_of_boundary", "automatic_meta_changes", "none", "belongs to later human or operational decision", "not_applicable", (COVERAGE_NOT_APPLICABLE,)),
    AnalyticalQuestionDefinition("NAQ-003", "not_applicable", "out_of_boundary", "pipeline_runtime_modification", "none", "belongs to implementation, not analytical product acceptance", "not_applicable", (COVERAGE_NOT_APPLICABLE,)),
    AnalyticalQuestionDefinition("NAQ-004", "not_applicable", "out_of_boundary", "historical_expected_values", "none", "historical outputs are not expected values", "not_applicable", (COVERAGE_NOT_APPLICABLE,)),
    AnalyticalQuestionDefinition("NAQ-005", "not_applicable", "out_of_boundary", "foundation_generalization", "none", "local contract cannot generalize to Foundation", "not_applicable", (COVERAGE_NOT_APPLICABLE,)),
)

QUESTION_INDEX = {definition.question_id: definition for definition in QUESTION_DEFINITIONS}

REQUIRED_VIEWS = tuple(dict.fromkeys(definition.required_view for definition in QUESTION_DEFINITIONS))


def build_analytical_product_contract() -> AnalyticalProductContract:
    return AnalyticalProductContract(
        contract_id=CONTRACT_ID,
        version=CONTRACT_VERSION,
        schema_family=PRODUCT_SCHEMA_FAMILY,
        schema_version=PRODUCT_SCHEMA_VERSION,
        specification=CONTRACT_SPECIFICATION,
        coverage_matrix=QUESTION_DEFINITIONS,
        required_views=REQUIRED_VIEWS,
        depth_fields=MANDATORY_DEPTH_FIELDS,
        robustness_fields=ROBUSTNESS_FIELDS,
        coverage_states=tuple(sorted(VALID_PRODUCT_COVERAGE_STATES)),
        recommendation_categories=tuple(sorted(VALID_RECOMMENDATION_CATEGORIES)),
    )


def normalize_truthy(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return True


def validate_coverage_row(row: CoverageMatrixRow | Mapping[str, Any]) -> list[ProductContractIssue]:
    data = row.to_dict() if isinstance(row, CoverageMatrixRow) else dict(row)
    question_id = data.get("question_id")
    state = data.get("coverage_state")
    issues: list[ProductContractIssue] = []
    definition = QUESTION_INDEX.get(str(question_id))

    if definition is None:
        return [ProductContractIssue("UNKNOWN_QUESTION", "blocking", "Coverage row references an unknown analytical question", str(question_id))]

    if state not in VALID_PRODUCT_COVERAGE_STATES:
        issues.append(ProductContractIssue("INVALID_COVERAGE_STATE", "blocking", "Coverage state is not recognized", question_id))
    elif state not in definition.valid_states:
        issues.append(ProductContractIssue("STATE_NOT_ALLOWED_FOR_QUESTION", "blocking", "Coverage state is not allowed for this question", question_id))

    if not normalize_truthy(data.get("justification")):
        issues.append(ProductContractIssue("MISSING_JUSTIFICATION", "blocking", "Every coverage row must justify its state", question_id))

    if state == COVERAGE_COMPLETE:
        issues.extend(validate_mandatory_depth(data.get("depth", {}), question_id=question_id))
        robustness = data.get("robustness")
        if robustness is None:
            issues.append(ProductContractIssue("MISSING_ROBUSTNESS", "blocking", "Complete rows must declare robustness", question_id))
        else:
            issues.extend(validate_robustness_record(robustness, question_id=question_id))
            robustness_data = robustness.to_dict() if isinstance(robustness, RobustnessRecord) else dict(robustness)
            if str(robustness_data.get("sample_sufficiency") or "") in {"low_sample", "insufficient", "not_evaluable"}:
                issues.append(ProductContractIssue("COMPLETE_WITH_INSUFFICIENT_SAMPLE", "blocking", "complete rows cannot have low, insufficient, or non-evaluable sample", question_id))
        if not data.get("evidence_refs"):
            issues.append(ProductContractIssue("MISSING_EVIDENCE_REFS", "blocking", "Complete rows must trace evidence references", question_id))

    if state == COVERAGE_NOT_AVAILABLE:
        if not normalize_truthy(data.get("impact")):
            issues.append(ProductContractIssue("MISSING_ABSENCE_IMPACT", "blocking", "not_available requires declared impact", question_id))

    if state == COVERAGE_UNKNOWN and not normalize_truthy(data.get("depth", {}).get("limitation_or_uncertainty")):
        issues.append(ProductContractIssue("UNKNOWN_WITHOUT_UNCERTAINTY", "blocking", "UNKNOWN must preserve the unresolved uncertainty", question_id))

    if definition.taxonomy == "not_applicable" and state != COVERAGE_NOT_APPLICABLE:
        issues.append(ProductContractIssue("NAQ_MUST_BE_NOT_APPLICABLE", "blocking", "Non-applicable questions must remain not_applicable", question_id))

    return issues


def validate_coverage_matrix(rows: Iterable[CoverageMatrixRow | Mapping[str, Any]]) -> list[ProductContractIssue]:
    rows = list(rows)
    issues: list[ProductContractIssue] = []
    seen: set[str] = set()
    for row in rows:
        data = row.to_dict() if isinstance(row, CoverageMatrixRow) else dict(row)
        question_id = str(data.get("question_id"))
        if question_id in seen:
            issues.append(ProductContractIssue("DUPLICATE_QUESTION_ROW", "blocking", "Coverage matrix has duplicate question row", question_id))
        seen.add(question_id)
        issues.extend(validate_coverage_row(row))

    expected = {definition.question_id for definition in QUESTION_DEFINITIONS}
    missing = sorted(expected - seen)
    for question_id in missing:
        issues.append(ProductContractIssue("MISSING_QUESTION_ROW", "blocking", "Coverage matrix is missing a contract question", question_id))
    return issues


def validate_mandatory_depth(depth: Mapping[str, Any], *, question_id: str | None = None) -> list[ProductContractIssue]:
    issues: list[ProductContractIssue] = []
    for field_name in MANDATORY_DEPTH_FIELDS:
        if not normalize_truthy(depth.get(field_name)):
            issues.append(ProductContractIssue("MISSING_DEPTH_FIELD", "blocking", f"Missing minimum depth field: {field_name}", question_id))
    return issues


def validate_robustness_record(record: RobustnessRecord | Mapping[str, Any], *, question_id: str | None = None) -> list[ProductContractIssue]:
    data = record.to_dict() if isinstance(record, RobustnessRecord) else dict(record)
    issues: list[ProductContractIssue] = []
    for field_name in ROBUSTNESS_FIELDS:
        if not normalize_truthy(data.get(field_name)) and data.get(field_name) != 0:
            issues.append(ProductContractIssue("MISSING_ROBUSTNESS_FIELD", "blocking", f"Missing robustness field: {field_name}", question_id))
    sufficiency = str(data.get("sample_sufficiency") or "")
    if sufficiency in {"low_sample", "insufficient", "not_evaluable"}:
        issues.append(ProductContractIssue("LOW_SAMPLE_REQUIRES_DEGRADATION", "warning", "Low or non-evaluable sample must degrade conclusions to partial or UNKNOWN", question_id))
    return issues


def validate_evidence_item(item: Mapping[str, Any]) -> list[ProductContractIssue]:
    fields = set(item)
    prohibited = sorted(fields & PROHIBITED_EVIDENCE_INTERPRETIVE_FIELDS)
    if prohibited:
        return [ProductContractIssue("EVIDENCE_CONTAINS_INTERPRETATION", "blocking", f"Evidence cannot contain interpretive fields: {', '.join(prohibited)}")]
    required = {"evidence_id", "facts", "coverage_state", "traceability"}
    missing = sorted(field for field in required if not normalize_truthy(item.get(field)))
    return [ProductContractIssue("EVIDENCE_MISSING_FIELD", "blocking", f"Evidence missing field: {field}") for field in missing]


def validate_knowledge_item(item: Mapping[str, Any]) -> list[ProductContractIssue]:
    fields = set(item)
    prohibited = sorted(fields & PROHIBITED_KNOWLEDGE_FIELDS)
    issues = [ProductContractIssue("KNOWLEDGE_FIELD_PROHIBITED", "blocking", f"Knowledge cannot contain field: {field}") for field in prohibited]
    for field_name in ("knowledge_id", "evidence_refs", "interpretation", "limitation_or_uncertainty"):
        if not normalize_truthy(item.get(field_name)):
            issues.append(ProductContractIssue("KNOWLEDGE_MISSING_FIELD", "blocking", f"Knowledge missing field: {field_name}"))
    return issues


def validate_recommendation(item: Mapping[str, Any]) -> list[ProductContractIssue]:
    category = item.get("category")
    issues: list[ProductContractIssue] = []
    if category not in VALID_RECOMMENDATION_CATEGORIES:
        return [ProductContractIssue("INVALID_RECOMMENDATION_CATEGORY", "blocking", "Recommendation category is not valid")]
    if not normalize_truthy(item.get("knowledge_refs")):
        issues.append(ProductContractIssue("RECOMMENDATION_WITHOUT_KNOWLEDGE", "blocking", "Recommendation must trace to Knowledge"))

    if category == RECOMMENDATION_MEASURABLE_EXPERIMENT:
        required = (
            "hypothesis",
            "action",
            "population",
            "primary_metric",
            "guardrail",
            "expected_direction",
            "success_criterion",
            "validation_window",
            "evidence_dependency",
            "uncertainty",
            "stop_or_review_condition",
        )
    elif category == RECOMMENDATION_VERIFIABLE_ACTION:
        required = ("action", "supporting_evidence", "verifiable_result", "closure_criterion", "risk", "dependency")
    else:
        required = ("hypothesis", "support", "uncertainty", "missing_evidence", "promotion_condition")

    for field_name in required:
        if not normalize_truthy(item.get(field_name)):
            issues.append(ProductContractIssue("RECOMMENDATION_MISSING_FIELD", "blocking", f"Recommendation missing field: {field_name}"))
    return issues


def validate_recommendations(items: Iterable[Mapping[str, Any]]) -> list[ProductContractIssue]:
    issues: list[ProductContractIssue] = []
    for item in items:
        issues.extend(validate_recommendation(item))
    return issues


def find_prohibited_nested_fields(value: Any, prohibited_fields: set[str], path: str = "root") -> list[str]:
    findings: list[str] = []
    if isinstance(value, Mapping):
        for key, nested_value in value.items():
            key_text = str(key)
            current_path = f"{path}.{key_text}"
            if key_text in prohibited_fields:
                findings.append(current_path)
            findings.extend(find_prohibited_nested_fields(nested_value, prohibited_fields, current_path))
    elif isinstance(value, (list, tuple)):
        for index, nested_value in enumerate(value):
            findings.extend(find_prohibited_nested_fields(nested_value, prohibited_fields, f"{path}[{index}]"))
    return findings


def validate_common_core(core: CommonProductCore) -> list[ProductContractIssue]:
    issues: list[ProductContractIssue] = []
    if not core.period:
        issues.append(ProductContractIssue("CORE_MISSING_PERIOD", "blocking", "Common core must declare period"))
    if not core.scope:
        issues.append(ProductContractIssue("CORE_MISSING_SCOPE", "blocking", "Common core must declare scope"))
    if not core.sources:
        issues.append(ProductContractIssue("CORE_MISSING_SOURCES", "blocking", "Common core must declare authorized sources"))
    if not core.evidence_refs:
        issues.append(ProductContractIssue("CORE_MISSING_EVIDENCE_REFS", "blocking", "Common core must declare evidence references"))
    issues.extend(validate_coverage_matrix(core.coverage_matrix))
    for knowledge_claim in core.knowledge_claims:
        issues.extend(validate_knowledge_item(knowledge_claim))
    issues.extend(validate_recommendations(core.recommendations))
    return issues


def build_projection(core: CommonProductCore, projection_type: str, sections: Iterable[Mapping[str, Any]] = ()) -> ProductProjection:
    if projection_type not in {"analytical", "executive"}:
        raise ValueError("projection_type must be analytical or executive")
    return ProductProjection(
        projection_type=projection_type,
        common_core_fingerprint=core.semantic_fingerprint,
        coverage_states={row.question_id: row.coverage_state for row in core.coverage_matrix},
        unknowns=core.unknowns,
        limitations=core.limitations,
        sections=tuple(dict(section) for section in sections),
    )


def validate_projection_equivalence(core: CommonProductCore, projection: ProductProjection | Mapping[str, Any]) -> list[ProductContractIssue]:
    data = projection.to_dict() if isinstance(projection, ProductProjection) else dict(projection)
    issues: list[ProductContractIssue] = []
    if data.get("common_core_fingerprint") != core.semantic_fingerprint:
        issues.append(ProductContractIssue("PROJECTION_CORE_DIVERGENCE", "blocking", "Projection does not reference the common core fingerprint"))
    if dict(data.get("coverage_states", {})) != {row.question_id: row.coverage_state for row in core.coverage_matrix}:
        issues.append(ProductContractIssue("PROJECTION_COVERAGE_DIVERGENCE", "blocking", "Projection changes coverage states"))
    if tuple(data.get("unknowns", ())) != core.unknowns:
        issues.append(ProductContractIssue("PROJECTION_UNKNOWN_DIVERGENCE", "blocking", "Projection changes UNKNOWNs"))
    if tuple(data.get("limitations", ())) != core.limitations:
        issues.append(ProductContractIssue("PROJECTION_LIMITATION_DIVERGENCE", "blocking", "Projection changes limitations"))
    for field_name in PROHIBITED_PRESENTATION_FIELDS:
        if field_name in data:
            issues.append(ProductContractIssue("PROJECTION_FIELD_PROHIBITED", "blocking", f"Projection cannot contain field: {field_name}"))
    prohibited_paths = find_prohibited_nested_fields(data.get("sections", ()), PROHIBITED_PRESENTATION_SECTION_FIELDS, "sections")
    for prohibited_path in prohibited_paths:
        issues.append(ProductContractIssue("PROJECTION_FIELD_PROHIBITED", "blocking", f"Projection section cannot contain canonical field: {prohibited_path}"))
    return issues


def assess_ad_name_applicability(*, has_ad_id_norm: bool, has_ad_metrics: bool, has_ad_name: bool) -> dict[str, Any]:
    if not has_ad_id_norm or not has_ad_metrics:
        return {
            "question_id": "AQ-005",
            "coverage_state": COVERAGE_BLOCKED,
            "reason": "ad creative granularity or traceable metrics are unavailable",
            "ad_name_is_blocking_by_itself": False,
        }
    if not has_ad_name:
        return {
            "question_id": "AQ-005",
            "coverage_state": COVERAGE_NOT_AVAILABLE,
            "reason": "ad_name label is unavailable but technical ad identity remains usable",
            "ad_name_is_blocking_by_itself": False,
        }
    return {
        "question_id": "AQ-005",
        "coverage_state": COVERAGE_COMPLETE,
        "reason": "ad_name label is available as an interpretive label only",
        "ad_name_is_blocking_by_itself": False,
    }


def assess_ticket_status_applicability(*, source_authorized: bool, coverage_sufficient: bool) -> dict[str, Any]:
    if not source_authorized:
        state = COVERAGE_NOT_AVAILABLE
        reason = "ticket_status source is not authorized for this execution"
    elif not coverage_sufficient:
        state = COVERAGE_PARTIAL
        reason = "ticket_status source is authorized but coverage is insufficient"
    else:
        state = COVERAGE_COMPLETE
        reason = "ticket_status source is authorized and sufficiently covered"
    return {
        "question_id": "CQ-002",
        "coverage_state": state,
        "reason": reason,
        "may_impute_from_faro": False,
    }


def assess_temporal_comparability(*, has_monthly_series: bool, has_complete_weeks: bool, has_partial_week_rule: bool) -> dict[str, Any]:
    if not has_monthly_series:
        return {
            "question_id": "AQ-009",
            "coverage_state": COVERAGE_BLOCKED,
            "minimum_temporal_basis": "monthly",
            "weekly_view_applicable": False,
            "reason": "mandatory monthly temporal basis is unavailable",
        }
    if has_complete_weeks or has_partial_week_rule:
        return {
            "question_id": "AQ-009",
            "coverage_state": COVERAGE_COMPLETE,
            "minimum_temporal_basis": "monthly",
            "weekly_view_applicable": True,
            "reason": "monthly basis exists and weekly comparability is supported",
        }
    return {
        "question_id": "AQ-009",
        "coverage_state": COVERAGE_PARTIAL,
        "minimum_temporal_basis": "monthly",
        "weekly_view_applicable": False,
        "reason": "monthly basis exists; weekly evolution is not comparable",
    }


def build_contract_acceptance_payload(core: CommonProductCore) -> dict[str, Any]:
    issues = validate_common_core(core)
    blocking = [issue for issue in issues if issue.severity == "blocking"]
    return {
        "schema_family": PRODUCT_SCHEMA_FAMILY,
        "schema_version": PRODUCT_SCHEMA_VERSION,
        "contract_id": CONTRACT_ID,
        "contract_version": CONTRACT_VERSION,
        "specification": CONTRACT_SPECIFICATION,
        "is_product_contract_acceptance_envelope": True,
        "is_complete_global_boolean": None,
        "completion_is_by_question_and_criticality": True,
        "common_core_fingerprint": core.semantic_fingerprint,
        "coverage_matrix": [row.to_dict() for row in core.coverage_matrix],
        "issues": [issue.to_dict() for issue in issues],
        "is_contractually_acceptable_for_local_implementation": not blocking,
    }