"""AUC-001 analytical product contract runtime helpers.

This module materializes SPEC-014 as deterministic local structures and
validators. It does not acquire evidence, call BigQuery, read historical
outputs, or write analytical products.
"""

from __future__ import annotations

import copy
import hashlib
import json

from dataclasses import dataclass, field
from typing import Any, Iterable, Mapping

from tools.auc_001_canonical_cost_quality_model import STRATEGIC_CONTEXT_CONSTRAINTS as DEFAULT_STRATEGIC_CONTEXT_CONSTRAINTS

CONTRACT_ID = "AUC-001-ANALYTICAL-PRODUCT-CONTRACT"
CONTRACT_VERSION = "spec-014.v1"
CONTRACT_SPECIFICATION = "SPEC-014"
PRODUCT_SCHEMA_FAMILY = "auc_001_analytical_product_contract"
PRODUCT_SCHEMA_VERSION = "auc_001_analytical_product_contract.v1"
CANONICAL_PROJECTION_SCHEMA_FAMILY = "auc_001_canonical_projection_source"
CANONICAL_PROJECTION_SCHEMA_VERSION = "auc_001_canonical_projection_source.v1"
CANONICAL_PROJECTION_CONTRACT_VERSION = "spec-015.v1"
CANONICAL_PROJECTION_SPECIFICATION = "SPEC-015"

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

COMPARISON_DESCRIPTIVE_CONTRAST = "descriptive_contrast"
COMPARISON_ECONOMIC_EFFICIENCY_CLAIM = "economic_efficiency_claim"
COMPARISON_STRATEGIC_HIERARCHY_CLAIM = "strategic_hierarchy_claim"
COMPARISON_CAUSAL_OR_OPTIMIZATION_CLAIM = "causal_or_optimization_claim"

VALID_COMPARISON_TYPES = {
    COMPARISON_DESCRIPTIVE_CONTRAST,
    COMPARISON_ECONOMIC_EFFICIENCY_CLAIM,
    COMPARISON_STRATEGIC_HIERARCHY_CLAIM,
    COMPARISON_CAUSAL_OR_OPTIMIZATION_CLAIM,
}

STRATEGIC_EQUIVALENCE_EQUIVALENT = "equivalent"
STRATEGIC_EQUIVALENCE_NON_EQUIVALENT = "non_equivalent"
STRATEGIC_EQUIVALENCE_UNKNOWN = "unknown"

VALID_STRATEGIC_EQUIVALENCE = {
    STRATEGIC_EQUIVALENCE_EQUIVALENT,
    STRATEGIC_EQUIVALENCE_NON_EQUIVALENT,
    STRATEGIC_EQUIVALENCE_UNKNOWN,
}

COMPARISON_GOVERNANCE_ALLOWED = "allowed"
COMPARISON_GOVERNANCE_ALLOWED_WITH_LIMITATION = "allowed_with_limitation"
COMPARISON_GOVERNANCE_PRESENTATION_RESTRICTED = "presentation_restricted"
COMPARISON_GOVERNANCE_BLOCKED = "blocked"

VALID_COMPARISON_GOVERNANCE_STATUSES = {
    COMPARISON_GOVERNANCE_ALLOWED,
    COMPARISON_GOVERNANCE_ALLOWED_WITH_LIMITATION,
    COMPARISON_GOVERNANCE_PRESENTATION_RESTRICTED,
    COMPARISON_GOVERNANCE_BLOCKED,
}

COMPARISON_GOVERNANCE_RANK = {
    COMPARISON_GOVERNANCE_ALLOWED: 0,
    COMPARISON_GOVERNANCE_ALLOWED_WITH_LIMITATION: 1,
    COMPARISON_GOVERNANCE_PRESENTATION_RESTRICTED: 2,
    COMPARISON_GOVERNANCE_BLOCKED: 3,
}

ANALYTICAL_COMPARISON_BEHAVIORS = {"preserve_full_context", "preserve_with_limitation", "suppress_claim"}
EXECUTIVE_COMPARISON_BEHAVIORS = {"simplify_with_limitation", "downgrade_to_descriptive", "suppress_claim"}

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

PRESENTATION_BLOCKED_PHRASES = (
    "conserva el valor del producto historico",
    "recupera el valor historico",
    "supera el valor historico",
    "creative causality is confirmed",
    "causalidad creativa confirmada",
    "creative winner",
    "ganador creativo",
    "lead_only means zero cost",
    "lead_only es coste cero",
    "spend_only means no leads",
    "spend_only es ausencia real de leads",
)

FUTURE_EVIDENCE_GAP_MARKERS = {
    "revenue_or_crm": ("revenue", "sales", "crm", "conversion comercial", "ventas"),
    "creative_causality": ("creative causal", "creative causality", "causalidad creativa"),
    "additional_creative_metadata": ("creative metadata", "metadata creativa", "visual asset"),
    "provider_limited_temporality": ("temporal", "weekly", "semanal", "cost-quality trend", "coste temporal"),
}

ALLOWED_PRESENTATION_SECTION_FIELDS = {
    "title",
    "content_ref",
    "content_refs",
    "cps_ref",
    "cps_refs",
    "traceability_refs",
    "knowledge_refs",
    "recommendation_refs",
    "comparison_refs",
    "comparison_classification_refs",
    "coverage_refs",
    "metric_refs",
    "limitation_refs",
    "unknown_refs",
    "display_role",
    "projection_role",
    "format",
    "order",
    "level",
    "emphasis",
    "visibility",
    "items",
    "ccd_constraint_refs",
    "strategic_context_constraint_refs",
}

VALID_CAMPAIGN_SIGNAL_LAYERS = set(DEFAULT_STRATEGIC_CONTEXT_CONSTRAINTS.get("layers", {}))
SIGNAL_INTERPRETATION_FIELDS = {
    "signal_layer",
    "campaign_signal",
    "kpi_family",
    "claim_type",
    "ccd_constraint_ref",
}
PROFILE_LAYERS = DEFAULT_STRATEGIC_CONTEXT_CONSTRAINTS.get("layers", {})
ATTENTION_FORBIDDEN_KPI_FAMILIES = set(PROFILE_LAYERS.get("ATTENTION", {}).get("forbidden_kpi_families", ()))
ACTIVATION_ALLOWED_INTERPRETATION_SCOPES = set(PROFILE_LAYERS.get("ACTIVATION", {}).get("allowed_interpretation_scopes", ()))
ACTIVATION_REQUIRED_COST_SEPARATION = set(PROFILE_LAYERS.get("ACTIVATION", {}).get("required_cost_separation", ()))
COMMERCIAL_ALLOWED_COST_QUALITY_UNIVERSE = PROFILE_LAYERS.get("COMMERCIAL", {}).get("allowed_cost_quality_universe")
COMMERCIAL_FORBIDDEN_PRIMARY_KPI_FAMILIES = set(PROFILE_LAYERS.get("COMMERCIAL", {}).get("forbidden_primary_kpi_families", ()))
PROFILE_METRIC_FAMILIES = DEFAULT_STRATEGIC_CONTEXT_CONSTRAINTS.get("metric_families", {})
COST_KPI_FAMILIES = set(PROFILE_METRIC_FAMILIES.get("cost_metric_families", ()))
UNIVERSAL_KPI_RANKING_CLAIM_TYPES = set(PROFILE_METRIC_FAMILIES.get("universal_kpi_ranking_claim_types", ()))
UNIVERSAL_KPI_RANKING_COMPARISON_SCOPES = set(PROFILE_METRIC_FAMILIES.get("universal_kpi_ranking_comparison_scopes", ()))

PRESENTATION_SECTION_REF_FIELDS = {
    "content_ref",
    "content_refs",
    "cps_ref",
    "cps_refs",
    "traceability_refs",
    "knowledge_refs",
    "recommendation_refs",
    "comparison_refs",
    "comparison_classification_refs",
    "coverage_refs",
    "metric_refs",
    "limitation_refs",
    "unknown_refs",
    "ccd_constraint_refs",
    "strategic_context_constraint_refs",
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
class ComparisonClassification:
    comparison_id: str
    source_artifact: str
    compared_universes: tuple[Mapping[str, Any], ...]
    comparison_type: tuple[str, ...]
    governance_status: str
    provisional_claim_ref: Mapping[str, Any] | None = None
    stabilized_claim_refs: Mapping[str, Any] = field(default_factory=dict)
    required_limitation_or_disclaimer_semantics: str | None = None
    allowed_projection_behavior: Mapping[str, str] = field(default_factory=dict)
    traceability: Mapping[str, Any] = field(default_factory=dict)
    qa_expected_check: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "comparison_id": self.comparison_id,
            "source_artifact": self.source_artifact,
            "provisional_claim_ref": dict(self.provisional_claim_ref) if self.provisional_claim_ref else None,
            "stabilized_claim_refs": dict(self.stabilized_claim_refs),
            "compared_universes": [dict(item) for item in self.compared_universes],
            "comparison_type": list(self.comparison_type),
            "governance_status": self.governance_status,
            "required_limitation_or_disclaimer_semantics": self.required_limitation_or_disclaimer_semantics,
            "allowed_projection_behavior": dict(self.allowed_projection_behavior),
            "traceability": dict(self.traceability),
            "qa_expected_check": self.qa_expected_check,
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
    comparison_classifications: tuple[Mapping[str, Any], ...] = ()
    strategic_context_constraints: Mapping[str, Any] = field(default_factory=lambda: copy.deepcopy(DEFAULT_STRATEGIC_CONTEXT_CONSTRAINTS))

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
            "comparison_classifications": [dict(item) for item in self.comparison_classifications],
            "strategic_context_constraints": dict(self.strategic_context_constraints),
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
            "comparison_classifications": [dict(item) for item in self.comparison_classifications],
            "strategic_context_constraints": dict(self.strategic_context_constraints),
            "semantic_fingerprint": self.semantic_fingerprint,
        }


@dataclass(frozen=True)
class ProductProjection:
    projection_type: str
    common_core_fingerprint: str
    coverage_states: Mapping[str, str]
    unknowns: tuple[str, ...]
    limitations: tuple[str, ...]
    comparison_classifications: tuple[Mapping[str, Any], ...] = ()
    sections: tuple[Mapping[str, Any], ...] = ()
    strategic_context_constraints: Mapping[str, Any] = field(default_factory=lambda: copy.deepcopy(DEFAULT_STRATEGIC_CONTEXT_CONSTRAINTS))

    def to_dict(self) -> dict[str, Any]:
        return {
            "projection_type": self.projection_type,
            "common_core_fingerprint": self.common_core_fingerprint,
            "coverage_states": dict(self.coverage_states),
            "unknowns": list(self.unknowns),
            "limitations": list(self.limitations),
            "comparison_classifications": [dict(item) for item in self.comparison_classifications],
            "sections": [dict(section) for section in self.sections],
            "strategic_context_constraints": dict(self.strategic_context_constraints),
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


def normalize_token(value: Any) -> str:
    return str(value or "").strip().lower().replace("-", "_").replace(" ", "_")


def strategic_constraints_payload(value: Mapping[str, Any] | None = None) -> dict[str, Any]:
    return copy.deepcopy(dict(value)) if isinstance(value, Mapping) and value else copy.deepcopy(DEFAULT_STRATEGIC_CONTEXT_CONSTRAINTS)


def validate_strategic_context_constraints(value: Mapping[str, Any] | None, *, artifact: str = "strategic_context_constraints") -> list[ProductContractIssue]:
    data = strategic_constraints_payload(value)
    issues: list[ProductContractIssue] = []
    if data.get("source_artifact") != "knowledge/client/ccd.md":
        issues.append(ProductContractIssue("STRATEGIC_CONTEXT_SOURCE_INVALID", "blocking", "Strategic constraints must reference knowledge/client/ccd.md", artifact))
    if not normalize_truthy(data.get("source_refs")):
        issues.append(ProductContractIssue("STRATEGIC_CONTEXT_REFS_MISSING", "blocking", "Strategic constraints must preserve CCD source references", artifact))
    layers = dict(data.get("layers") or {})
    for layer in sorted(VALID_CAMPAIGN_SIGNAL_LAYERS):
        if layer not in layers:
            issues.append(ProductContractIssue("STRATEGIC_CONTEXT_LAYER_MISSING", "blocking", f"Strategic constraints missing FARO layer: {layer}", artifact))
    global_rules = dict(data.get("global_rules") or {})
    if global_rules.get("forbidden_comparison") != "universal_kpi_ranking_across_layers":
        issues.append(ProductContractIssue("STRATEGIC_CONTEXT_UNIVERSAL_KPI_RULE_MISSING", "blocking", "Strategic constraints must block universal KPI ranking across FARO layers", artifact))
    if global_rules.get("required_traceability") != "ccd_constraint_ref":
        issues.append(ProductContractIssue("STRATEGIC_CONTEXT_TRACEABILITY_RULE_MISSING", "blocking", "Strategic constraints must require ccd_constraint_ref", artifact))
    return issues


def has_campaign_signal_semantics(item: Mapping[str, Any]) -> bool:
    return bool(set(item) & SIGNAL_INTERPRETATION_FIELDS)


def validate_campaign_signal_interpretation(item: Mapping[str, Any], *, artifact: str = "claim") -> list[ProductContractIssue]:
    if not has_campaign_signal_semantics(item):
        return []

    issues: list[ProductContractIssue] = []
    signal = str(item.get("signal_layer") or item.get("campaign_signal") or "").strip().upper()
    kpi_family = normalize_token(item.get("kpi_family"))
    claim_type = normalize_token(item.get("claim_type"))
    universe = normalize_token(item.get("universe"))
    interpretation_scope = normalize_token(item.get("interpretation_scope") or item.get("interpretation_type"))
    cost_scope = normalize_token(item.get("cost_scope"))
    cost_separation = {normalize_token(value) for value in item.get("cost_separation", [])} if isinstance(item.get("cost_separation"), (list, tuple, set)) else set()

    if signal not in VALID_CAMPAIGN_SIGNAL_LAYERS:
        issues.append(ProductContractIssue("CAMPAIGN_SIGNAL_LAYER_INVALID", "blocking", "campaign_signal interpretation must declare a layer published by the local profile", artifact))
        return issues
    if not normalize_truthy(item.get("ccd_constraint_ref")):
        issues.append(ProductContractIssue("CAMPAIGN_SIGNAL_CCD_REF_MISSING", "blocking", "campaign_signal interpretation must trace to CCD constraint", artifact))
    if not kpi_family:
        issues.append(ProductContractIssue("CAMPAIGN_SIGNAL_KPI_FAMILY_MISSING", "blocking", "campaign_signal interpretation must declare kpi_family", artifact))

    if claim_type in UNIVERSAL_KPI_RANKING_CLAIM_TYPES or normalize_token(item.get("comparison_scope")) in UNIVERSAL_KPI_RANKING_COMPARISON_SCOPES:
        issues.append(ProductContractIssue("FARO_UNIVERSAL_KPI_RANKING", "blocking", "Profile layers cannot be compared through one universal KPI", artifact))

    if signal == "ATTENTION" and kpi_family in ATTENTION_FORBIDDEN_KPI_FAMILIES:
        issues.append(ProductContractIssue("FARO_ATTENTION_FORBIDDEN_KPI", "blocking", "ATTENTION cannot be evaluated by direct leads, CPL, qualified CPL or direct commercial efficiency", artifact))

    if signal == "ACTIVATION":
        if interpretation_scope not in ACTIVATION_ALLOWED_INTERPRETATION_SCOPES:
            issues.append(ProductContractIssue("FARO_ACTIVATION_INTERPRETATION_REQUIRED", "blocking", "ACTIVATION must be interpreted as retargeting or prior-interest activation", artifact))
        if kpi_family in COST_KPI_FAMILIES or cost_scope:
            required = {"direct_cost", "complete_or_assisted_cost"}
            if not required <= cost_separation:
                issues.append(ProductContractIssue("FARO_ACTIVATION_COST_SEPARATION_REQUIRED", "blocking", "ACTIVATION cost reading must separate direct cost from complete or assisted cost", artifact))

    if signal == "COMMERCIAL":
        if kpi_family in COMMERCIAL_FORBIDDEN_PRIMARY_KPI_FAMILIES:
            issues.append(ProductContractIssue("FARO_COMMERCIAL_FORBIDDEN_PRIMARY_KPI", "blocking", "COMMERCIAL cannot be primarily evaluated by attention or video-consumption KPIs", artifact))
        if kpi_family in COST_KPI_FAMILIES and universe != COMMERCIAL_ALLOWED_COST_QUALITY_UNIVERSE:
            issues.append(ProductContractIssue("FARO_COMMERCIAL_UNIVERSE_REQUIRED", "blocking", "COMMERCIAL cost-quality must use the profile-declared universe", artifact))
    return issues


def validate_campaign_signal_collection(items: Iterable[Mapping[str, Any]], *, artifact: str) -> list[ProductContractIssue]:
    issues: list[ProductContractIssue] = []
    for index, item in enumerate(items):
        issues.extend(validate_campaign_signal_interpretation(item, artifact=f"{artifact}#{index}"))
    return issues


def comparison_classification_to_dict(item: ComparisonClassification | Mapping[str, Any]) -> dict[str, Any]:
    return item.to_dict() if isinstance(item, ComparisonClassification) else dict(item)


def comparison_governance_minimum_status(data: Mapping[str, Any]) -> str:
    comparison_types = set(data.get("comparison_type") or [])
    equivalence_values = {
        str(universe.get("strategic_equivalence"))
        for universe in data.get("compared_universes") or []
        if isinstance(universe, Mapping)
    }
    if COMPARISON_CAUSAL_OR_OPTIMIZATION_CLAIM in comparison_types and STRATEGIC_EQUIVALENCE_NON_EQUIVALENT in equivalence_values:
        return COMPARISON_GOVERNANCE_BLOCKED
    if comparison_types & {COMPARISON_ECONOMIC_EFFICIENCY_CLAIM, COMPARISON_STRATEGIC_HIERARCHY_CLAIM, COMPARISON_CAUSAL_OR_OPTIMIZATION_CLAIM}:
        if STRATEGIC_EQUIVALENCE_UNKNOWN in equivalence_values:
            return COMPARISON_GOVERNANCE_ALLOWED_WITH_LIMITATION
        if STRATEGIC_EQUIVALENCE_NON_EQUIVALENT in equivalence_values:
            return COMPARISON_GOVERNANCE_ALLOWED_WITH_LIMITATION
    return COMPARISON_GOVERNANCE_ALLOWED


def comparison_is_material(data: Mapping[str, Any]) -> bool:
    if "is_material" in data:
        return normalize_truthy(data.get("is_material"))
    if "material" in data:
        return normalize_truthy(data.get("material"))
    return True


def knowledge_ref_index(items: Iterable[Mapping[str, Any]]) -> set[str]:
    refs: set[str] = set()
    for item in items:
        if not isinstance(item, Mapping):
            continue
        value = item.get("knowledge_id") or item.get("id")
        if normalize_truthy(value):
            refs.add(str(value))
    return refs


def has_unknown_restrictive_comparison(classification: Mapping[str, Any]) -> bool:
    comparison_types = set(classification.get("comparison_type") or [])
    if not comparison_types & {COMPARISON_ECONOMIC_EFFICIENCY_CLAIM, COMPARISON_STRATEGIC_HIERARCHY_CLAIM, COMPARISON_CAUSAL_OR_OPTIMIZATION_CLAIM}:
        return False
    return any(
        isinstance(universe, Mapping) and universe.get("strategic_equivalence") == STRATEGIC_EQUIVALENCE_UNKNOWN
        for universe in classification.get("compared_universes") or []
    )


def recommendation_has_conclusive_unknown_decision(item: Mapping[str, Any]) -> bool:
    explicit_flags = {
        "economic_decision_conclusive",
        "optimization_action",
        "strategic_prioritization",
        "comparative_superiority_claim",
    }
    if any(normalize_truthy(item.get(flag)) for flag in explicit_flags):
        return True
    text = flatten_text(item).lower()
    blocked_markers = (
        "redistribuir inversion",
        "redistribuir inversión",
        "redistribuir presupuesto",
        "reallocate budget",
        "increase budget",
        "aumentar presupuesto",
        "reduce budget",
        "reducir presupuesto",
        "declares a winner",
        "declare a winner",
        "ganador",
        "winner",
        "priorizar estrategicamente",
        "priorizar estratégicamente",
        "strategically prioritize",
        "priorizar",
        "superioridad",
        "superiority",
        "mayor eficiencia economica",
        "mayor eficiencia económica",
        "mejor eficiencia",
        "eficiencia comparada",
        "economic efficiency is higher",
        "better efficiency",
        "more efficient",
        "optimize based on this comparison",
        "optimizar por esta comparacion",
        "optimizar por esta comparación",
    )
    return any(marker in text for marker in blocked_markers)


def recommendation_resolves_unknown_without_conclusive_decision(item: Mapping[str, Any]) -> bool:
    text = flatten_text(item).lower()
    resolution_markers = (
        "resolve",
        "resolver",
        "validate",
        "validar",
        "measure",
        "medir",
        "test",
        "experiment",
        "experimento",
        "reconcile",
        "reconciliar",
        "equivalence",
        "equivalencia",
        "uncertainty",
        "incertidumbre",
        "unknown",
        "desconocida",
        "evidence",
        "evidencia",
    )
    return any(marker in text for marker in resolution_markers)


def validate_comparison_classification(
    item: ComparisonClassification | Mapping[str, Any],
    *,
    artifact: str = "comparison_classification",
    knowledge_set_stabilized: bool = False,
    knowledge_items: Iterable[Mapping[str, Any]] = (),
) -> list[ProductContractIssue]:
    data = comparison_classification_to_dict(item)
    issues: list[ProductContractIssue] = []
    comparison_id = str(data.get("comparison_id") or "")
    if not normalize_truthy(comparison_id):
        issues.append(ProductContractIssue("COMPARISON_ID_MISSING", "blocking", "Comparison classification must preserve a stable identity", artifact))

    compared_universes = data.get("compared_universes") or []
    if not isinstance(compared_universes, (list, tuple)) or len(compared_universes) < 2:
        issues.append(ProductContractIssue("COMPARISON_UNIVERSE_MISSING", "blocking", "Comparison classification must declare at least two compared universes", comparison_id or artifact))
        compared_universes = []
    for index, universe in enumerate(compared_universes):
        if not isinstance(universe, Mapping):
            issues.append(ProductContractIssue("COMPARISON_UNIVERSE_INVALID", "blocking", "Compared universe must be a structured object", comparison_id or artifact))
            continue
        for field_name in ("universe_id", "universe_label", "strategic_equivalence"):
            if not normalize_truthy(universe.get(field_name)):
                issues.append(ProductContractIssue("COMPARISON_UNIVERSE_FIELD_MISSING", "blocking", f"Compared universe missing field: {field_name}", comparison_id or artifact))
        if universe.get("strategic_equivalence") not in VALID_STRATEGIC_EQUIVALENCE:
            issues.append(ProductContractIssue("COMPARISON_STRATEGIC_EQUIVALENCE_INVALID", "blocking", f"Compared universe {index} has invalid strategic equivalence", comparison_id or artifact))

    comparison_types = data.get("comparison_type") or []
    if isinstance(comparison_types, str):
        comparison_types = [comparison_types]
    if not comparison_types:
        issues.append(ProductContractIssue("COMPARISON_TYPE_MISSING", "blocking", "Comparison classification must declare at least one comparison type", comparison_id or artifact))
    invalid_types = sorted(set(str(item) for item in comparison_types) - VALID_COMPARISON_TYPES)
    for invalid_type in invalid_types:
        issues.append(ProductContractIssue("COMPARISON_TYPE_INVALID", "blocking", f"Comparison type is not valid: {invalid_type}", comparison_id or artifact))

    governance_status = str(data.get("governance_status") or "")
    if governance_status not in VALID_COMPARISON_GOVERNANCE_STATUSES:
        issues.append(ProductContractIssue("COMPARISON_GOVERNANCE_INVALID", "blocking", "Comparison governance status is not valid", comparison_id or artifact))
    elif not invalid_types:
        minimum_status = comparison_governance_minimum_status({**data, "comparison_type": comparison_types, "compared_universes": compared_universes})
        if COMPARISON_GOVERNANCE_RANK[governance_status] < COMPARISON_GOVERNANCE_RANK[minimum_status]:
            issues.append(ProductContractIssue("COMPARISON_GOVERNANCE_TOO_WEAK", "blocking", "Comparison governance status is weaker than the classified claim requires", comparison_id or artifact))

    if governance_status in {COMPARISON_GOVERNANCE_ALLOWED_WITH_LIMITATION, COMPARISON_GOVERNANCE_PRESENTATION_RESTRICTED}:
        if not normalize_truthy(data.get("required_limitation_or_disclaimer_semantics")):
            issues.append(ProductContractIssue("COMPARISON_LIMITATION_REQUIRED", "blocking", "Restricted comparison must declare limitation or disclaimer semantics", comparison_id or artifact))

    stabilized_claim_refs = as_mapping(data.get("stabilized_claim_refs"))
    reconciliation_status = str(stabilized_claim_refs.get("reconciliation_status") or "")
    if reconciliation_status == COMPARISON_GOVERNANCE_BLOCKED and governance_status != COMPARISON_GOVERNANCE_BLOCKED:
        issues.append(ProductContractIssue("COMPARISON_RECONCILIATION_BLOCKED", "blocking", "Blocked claim reconciliation must block the comparison", comparison_id or artifact))
    if knowledge_set_stabilized and comparison_is_material(data):
        knowledge_refs = stabilized_claim_refs.get("knowledge_refs") or []
        if isinstance(knowledge_refs, str):
            knowledge_refs = [knowledge_refs]
        invalid_reconciliation_statuses = {"", "not_applicable", "pending", "missing", "unresolved", "unknown"}
        if reconciliation_status in invalid_reconciliation_statuses:
            issues.append(ProductContractIssue("COMPARISON_RECONCILIATION_REQUIRED", "blocking", "Material comparison must be reconciled after Knowledge stabilization", comparison_id or artifact))
        if not normalize_truthy(knowledge_refs):
            issues.append(ProductContractIssue("COMPARISON_KNOWLEDGE_REFS_REQUIRED", "blocking", "Material comparison must resolve to stabilized Knowledge references", comparison_id or artifact))
        knowledge_refs_index = knowledge_ref_index(knowledge_items)
        missing_refs = sorted(str(ref) for ref in knowledge_refs if str(ref) not in knowledge_refs_index)
        for missing_ref in missing_refs:
            issues.append(ProductContractIssue("COMPARISON_KNOWLEDGE_REF_UNRESOLVED", "blocking", "Comparison knowledge reference does not resolve in stabilized Knowledge Set", missing_ref))

    allowed_behavior = as_mapping(data.get("allowed_projection_behavior"))
    analytical_behavior = allowed_behavior.get("analytical")
    executive_behavior = allowed_behavior.get("executive")
    if analytical_behavior not in ANALYTICAL_COMPARISON_BEHAVIORS:
        issues.append(ProductContractIssue("COMPARISON_ANALYTICAL_BEHAVIOR_INVALID", "blocking", "Analytical projection behavior is missing or invalid", comparison_id or artifact))
    if executive_behavior not in EXECUTIVE_COMPARISON_BEHAVIORS:
        issues.append(ProductContractIssue("COMPARISON_EXECUTIVE_BEHAVIOR_INVALID", "blocking", "Executive projection behavior is missing or invalid", comparison_id or artifact))
    if governance_status == COMPARISON_GOVERNANCE_BLOCKED and (analytical_behavior != "suppress_claim" or executive_behavior != "suppress_claim"):
        issues.append(ProductContractIssue("COMPARISON_BLOCKED_BEHAVIOR_INVALID", "blocking", "Blocked comparison must be suppressed in analytical and executive projections", comparison_id or artifact))

    return issues


def validate_comparison_classifications(
    items: Iterable[ComparisonClassification | Mapping[str, Any]],
    *,
    artifact: str = "comparison_classifications",
    knowledge_set_stabilized: bool = False,
    knowledge_items: Iterable[Mapping[str, Any]] = (),
) -> list[ProductContractIssue]:
    issues: list[ProductContractIssue] = []
    seen: set[str] = set()
    for index, item in enumerate(items):
        data = comparison_classification_to_dict(item)
        comparison_id = str(data.get("comparison_id") or "")
        if comparison_id in seen:
            issues.append(ProductContractIssue("COMPARISON_ID_DUPLICATED", "blocking", "Comparison classification identity is duplicated", comparison_id))
        if comparison_id:
            seen.add(comparison_id)
        issues.extend(
            validate_comparison_classification(
                data,
                artifact=f"{artifact}#{index}",
                knowledge_set_stabilized=knowledge_set_stabilized,
                knowledge_items=knowledge_items,
            )
        )
    return issues


def comparison_classification_index(items: Iterable[Mapping[str, Any]]) -> dict[str, Mapping[str, Any]]:
    return {
        str(item.get("comparison_id")): item
        for item in items
        if isinstance(item, Mapping) and normalize_truthy(item.get("comparison_id"))
    }


def validate_recommendation_comparison_refs(item: Mapping[str, Any], comparison_index: Mapping[str, Mapping[str, Any]]) -> list[ProductContractIssue]:
    issues: list[ProductContractIssue] = []
    refs = item.get("comparison_refs") or []
    if isinstance(refs, str):
        refs = [refs]
    for comparison_ref in refs:
        comparison_id = str(comparison_ref)
        classification = comparison_index.get(comparison_id)
        if classification is None:
            issues.append(ProductContractIssue("RECOMMENDATION_COMPARISON_REF_UNKNOWN", "blocking", "Recommendation references an unknown comparison classification", comparison_id))
            continue
        if classification.get("governance_status") == COMPARISON_GOVERNANCE_BLOCKED:
            issues.append(ProductContractIssue("RECOMMENDATION_BLOCKED_COMPARISON", "blocking", "Recommendation cannot depend on a blocked comparison", comparison_id))
            continue
        if has_unknown_restrictive_comparison(classification):
            category = item.get("category")
            if recommendation_has_conclusive_unknown_decision(item):
                issues.append(ProductContractIssue("RECOMMENDATION_UNKNOWN_COMPARISON_CONCLUSIVE", "blocking", "Recommendation cannot make a conclusive economic, hierarchy or optimization decision from an unknown-equivalence comparison", comparison_id))
                continue
            if category == RECOMMENDATION_MEASURABLE_EXPERIMENT and recommendation_resolves_unknown_without_conclusive_decision(item):
                continue
            if category == RECOMMENDATION_NON_ACTIONABLE_HYPOTHESIS and recommendation_resolves_unknown_without_conclusive_decision(item):
                continue
            if category == RECOMMENDATION_VERIFIABLE_ACTION and recommendation_resolves_unknown_without_conclusive_decision(item):
                continue
            issues.append(ProductContractIssue("RECOMMENDATION_UNKNOWN_COMPARISON_UNGOVERNED", "blocking", "Recommendation based on unknown-equivalence comparison must remain non-conclusive and explicitly resolve or preserve uncertainty", comparison_id))
    return issues


def find_blocked_comparison_refs(value: Any, blocked_ids: set[str], path: str = "sections") -> list[str]:
    findings: list[str] = []
    if isinstance(value, Mapping):
        for key, nested_value in value.items():
            key_text = str(key)
            current_path = f"{path}.{key_text}"
            if key_text in {"comparison_ref", "comparison_id"} and str(nested_value) in blocked_ids:
                findings.append(current_path)
            elif key_text in {"comparison_refs", "comparison_classification_refs"} and isinstance(nested_value, (list, tuple, set)):
                for comparison_ref in nested_value:
                    if str(comparison_ref) in blocked_ids:
                        findings.append(current_path)
            findings.extend(find_blocked_comparison_refs(nested_value, blocked_ids, current_path))
    elif isinstance(value, (list, tuple)):
        for index, nested_value in enumerate(value):
            findings.extend(find_blocked_comparison_refs(nested_value, blocked_ids, f"{path}[{index}]"))
    return findings

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
    issues.extend(validate_campaign_signal_interpretation(item, artifact="knowledge"))
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
    issues.extend(validate_campaign_signal_interpretation(item, artifact="recommendation"))
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
    issues.extend(validate_strategic_context_constraints(core.strategic_context_constraints, artifact="common_core.strategic_context_constraints"))
    for knowledge_claim in core.knowledge_claims:
        issues.extend(validate_knowledge_item(knowledge_claim))
    issues.extend(validate_recommendations(core.recommendations))
    comparison_items = tuple(dict(item) for item in core.comparison_classifications)
    issues.extend(
        validate_comparison_classifications(
            comparison_items,
            artifact="common_core.comparison_classifications",
            knowledge_set_stabilized=True,
            knowledge_items=core.knowledge_claims,
        )
    )
    comparison_index = comparison_classification_index(comparison_items)
    for recommendation in core.recommendations:
        issues.extend(validate_recommendation_comparison_refs(recommendation, comparison_index))
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
        comparison_classifications=tuple(dict(item) for item in core.comparison_classifications),
        sections=tuple(dict(section) for section in sections),
        strategic_context_constraints=core.strategic_context_constraints,
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
    if dict(data.get("strategic_context_constraints") or {}) != dict(core.strategic_context_constraints):
        issues.append(ProductContractIssue("PROJECTION_STRATEGIC_CONTEXT_DIVERGENCE", "blocking", "Projection changes strategic context constraints"))
    if list(data.get("comparison_classifications") or []) != [dict(item) for item in core.comparison_classifications]:
        issues.append(ProductContractIssue("PROJECTION_COMPARISON_CLASSIFICATION_DIVERGENCE", "blocking", "Projection changes comparison classifications"))
    for field_name in PROHIBITED_PRESENTATION_FIELDS:
        if field_name in data:
            issues.append(ProductContractIssue("PROJECTION_FIELD_PROHIBITED", "blocking", f"Projection cannot contain field: {field_name}"))
    prohibited_paths = find_prohibited_nested_fields(data.get("sections", ()), PROHIBITED_PRESENTATION_SECTION_FIELDS, "sections")
    for prohibited_path in prohibited_paths:
        issues.append(ProductContractIssue("PROJECTION_FIELD_PROHIBITED", "blocking", f"Projection section cannot contain canonical field: {prohibited_path}"))
    return issues



@dataclass(frozen=True)
class CanonicalProjectionSource:
    artifact_id: str
    status: str
    source_artifacts: Mapping[str, Any]
    product_contract: Mapping[str, Any]
    projection_contracts: Mapping[str, Any]
    period: Mapping[str, Any]
    scope: Mapping[str, Any]
    sources: tuple[str, ...]
    canonical_metrics: Mapping[str, Any]
    coverage_states: Mapping[str, str]
    knowledge_claims: tuple[Mapping[str, Any], ...]
    analytical_narrative: Mapping[str, Any]
    integrated_view: Mapping[str, Any]
    decision_patterns: tuple[Mapping[str, Any], ...]
    recommendations: tuple[Mapping[str, Any], ...]
    limitations: tuple[str, ...]
    unknowns: tuple[str, ...]
    future_evidence_gaps: Mapping[str, str]
    exclusions: tuple[str, ...]
    traceability: Mapping[str, Any]
    comparison_classifications: tuple[Mapping[str, Any], ...] = ()
    strategic_context_constraints: Mapping[str, Any] = field(default_factory=lambda: copy.deepcopy(DEFAULT_STRATEGIC_CONTEXT_CONSTRAINTS))
    schema_family: str = CANONICAL_PROJECTION_SCHEMA_FAMILY
    schema_version: str = CANONICAL_PROJECTION_SCHEMA_VERSION
    specification: str = CANONICAL_PROJECTION_SPECIFICATION
    contract_version: str = CANONICAL_PROJECTION_CONTRACT_VERSION

    @property
    def semantic_fingerprint(self) -> str:
        payload = self.to_dict(include_fingerprint=False)
        canonical = json.dumps(payload, sort_keys=True, default=str, separators=(",", ":"))
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    def to_dict(self, *, include_fingerprint: bool = True) -> dict[str, Any]:
        payload = {
            "artifact_id": self.artifact_id,
            "schema_family": self.schema_family,
            "schema_version": self.schema_version,
            "specification": self.specification,
            "contract_version": self.contract_version,
            "status": self.status,
            "source_artifacts": dict(self.source_artifacts),
            "product_contract": dict(self.product_contract),
            "projection_contracts": dict(self.projection_contracts),
            "period": dict(self.period),
            "scope": dict(self.scope),
            "sources": list(self.sources),
            "canonical_metrics": dict(self.canonical_metrics),
            "coverage_states": dict(self.coverage_states),
            "knowledge_claims": [dict(item) for item in self.knowledge_claims],
            "analytical_narrative": dict(self.analytical_narrative),
            "integrated_view": dict(self.integrated_view),
            "decision_patterns": [dict(item) for item in self.decision_patterns],
            "recommendations": [dict(item) for item in self.recommendations],
            "limitations": list(self.limitations),
            "unknowns": list(self.unknowns),
            "future_evidence_gaps": dict(self.future_evidence_gaps),
            "comparison_classifications": [dict(item) for item in self.comparison_classifications],
            "exclusions": list(self.exclusions),
            "traceability": dict(self.traceability),
            "strategic_context_constraints": dict(self.strategic_context_constraints),
        }
        if include_fingerprint:
            payload["semantic_fingerprint"] = self.semantic_fingerprint
        return payload


@dataclass(frozen=True)
class CanonicalProductProjection:
    projection_type: str
    canonical_projection_source_id: str
    canonical_projection_source_fingerprint: str
    coverage_states: Mapping[str, str]
    unknowns: tuple[str, ...]
    limitations: tuple[str, ...]
    future_evidence_gaps: Mapping[str, str]
    recommendation_refs: tuple[Mapping[str, Any], ...]
    knowledge_refs: tuple[str, ...]
    communication_context: Mapping[str, Any]
    comparison_classifications: tuple[Mapping[str, Any], ...] = ()
    sections: tuple[Mapping[str, Any], ...] = ()
    strategic_context_constraints: Mapping[str, Any] = field(default_factory=lambda: copy.deepcopy(DEFAULT_STRATEGIC_CONTEXT_CONSTRAINTS))

    def to_dict(self) -> dict[str, Any]:
        return {
            "projection_type": self.projection_type,
            "canonical_projection_source_id": self.canonical_projection_source_id,
            "canonical_projection_source_fingerprint": self.canonical_projection_source_fingerprint,
            "coverage_states": dict(self.coverage_states),
            "unknowns": list(self.unknowns),
            "limitations": list(self.limitations),
            "future_evidence_gaps": dict(self.future_evidence_gaps),
            "recommendation_refs": [dict(item) for item in self.recommendation_refs],
            "knowledge_refs": list(self.knowledge_refs),
            "communication_context": dict(self.communication_context),
            "comparison_classifications": [dict(item) for item in self.comparison_classifications],
            "sections": [dict(section) for section in self.sections],
            "strategic_context_constraints": dict(self.strategic_context_constraints),
        }


def as_mapping(value: Any) -> dict[str, Any]:
    return dict(value) if isinstance(value, Mapping) else {}


def as_tuple_of_mappings(value: Any) -> tuple[Mapping[str, Any], ...]:
    if not isinstance(value, (list, tuple)):
        return ()
    return tuple(dict(item) for item in value if isinstance(item, Mapping))


def stable_text_items(*values: Any) -> tuple[str, ...]:
    items: list[str] = []
    for value in values:
        if isinstance(value, str) and value.strip():
            items.append(value.strip())
        elif isinstance(value, Mapping):
            for nested in value.values():
                if isinstance(nested, str) and nested.strip():
                    items.append(nested.strip())
        elif isinstance(value, (list, tuple, set)):
            for nested in value:
                if isinstance(nested, str) and nested.strip():
                    items.append(nested.strip())
    return tuple(dict.fromkeys(items))


def extract_coverage_states(common_core: Mapping[str, Any], coverage_matrix: Mapping[str, Any] | None = None) -> dict[str, str]:
    coverage_source = dict(common_core.get("coverage_states") or {})
    matrix = as_mapping(coverage_matrix)
    coverage_source.update(dict(matrix.get("states") or {}))
    if not coverage_source and isinstance(matrix.get("rows"), list):
        coverage_source = {
            str(row.get("question_id")): str(row.get("coverage_state"))
            for row in matrix["rows"]
            if isinstance(row, Mapping) and row.get("question_id")
        }
    return coverage_source


def recommendation_identity(item: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "recommendation_id": item.get("recommendation_id") or item.get("id"),
        "category": item.get("category"),
        "priority": item.get("priority"),
        "knowledge_refs": list(item.get("knowledge_refs") or []),
        "primary_metric": item.get("primary_metric") or item.get("verifiable_result"),
        "guardrail": item.get("guardrail"),
        "success_criterion": item.get("success_criterion") or item.get("closure_criterion"),
        "review_condition": item.get("stop_or_review_condition") or item.get("promotion_condition"),
    }


def knowledge_identity(item: Mapping[str, Any]) -> str | None:
    value = item.get("knowledge_id") or item.get("id")
    return str(value) if value else None


def infer_future_evidence_gaps(
    limitations: Iterable[str],
    unknowns: Iterable[str],
    exclusions: Iterable[str],
    coverage_states: Mapping[str, str] | None = None,
) -> dict[str, str]:
    corpus = "\n".join([*limitations, *unknowns, *exclusions]).lower()
    gaps: dict[str, str] = {}
    for gap_id, markers in FUTURE_EVIDENCE_GAP_MARKERS.items():
        if any(marker in corpus for marker in markers):
            gaps[gap_id] = "declared_dependency_on_future_evidence"

    states = dict(coverage_states or {})
    if states.get("CQ-006") == COVERAGE_NOT_AVAILABLE:
        gaps["revenue_or_crm"] = "declared_dependency_on_future_evidence"
    if states.get("CQ-005") == COVERAGE_NOT_AVAILABLE:
        gaps["additional_creative_metadata"] = "declared_dependency_on_future_evidence"
    if states.get("AQ-005") in {COVERAGE_PARTIAL, COVERAGE_UNKNOWN, COVERAGE_NOT_AVAILABLE}:
        gaps["creative_causality"] = "declared_dependency_on_future_evidence"
    if states.get("AQ-009") == COVERAGE_PARTIAL or states.get("CQ-007") == COVERAGE_PARTIAL:
        gaps["provider_limited_temporality"] = "declared_dependency_on_future_evidence"
    return gaps


def build_default_integrated_view(
    knowledge_set: Mapping[str, Any],
    common_core: Mapping[str, Any],
    coverage_states: Mapping[str, str],
) -> dict[str, Any]:
    investigation = as_tuple_of_mappings(knowledge_set.get("analytical_investigation_record"))
    narrative = as_mapping(knowledge_set.get("analytical_narrative"))
    return {
        "status": "canonicalized_from_knowledge",
        "signals": [
            {
                "finding_id": item.get("finding_id"),
                "observation": item.get("observation"),
                "support": list(item.get("support") or []),
                "uncertainty": item.get("uncertainty"),
                "related_findings": list(item.get("related_findings") or []),
            }
            for item in investigation
        ],
        "analytical_narrative_ref": narrative.get("status"),
        "quality_explanation": narrative.get("text"),
        "coverage_states": dict(coverage_states),
        "canonical_metric_keys": sorted(str(key) for key in as_mapping(common_core.get("canonical_metrics")).keys()),
    }


def build_default_decision_patterns(knowledge_set: Mapping[str, Any]) -> tuple[Mapping[str, Any], ...]:
    priorities = as_tuple_of_mappings(knowledge_set.get("priorities"))
    narrative = as_mapping(knowledge_set.get("analytical_narrative"))
    patterns = [
        {
            "pattern_id": item.get("priority_id"),
            "basis": item.get("basis"),
            "priority": item.get("priority"),
            "knowledge_refs": list(item.get("knowledge_refs") or []),
        }
        for item in priorities
    ]
    if narrative:
        patterns.append(
            {
                "pattern_id": "analytical_narrative",
                "basis": narrative.get("text"),
                "priority": "contextual",
                "knowledge_refs": [
                    item.get("knowledge_id")
                    for item in as_tuple_of_mappings(knowledge_set.get("knowledge_claims"))
                    if item.get("knowledge_id")
                ],
            }
        )
    return tuple(patterns)


def build_canonical_projection_source(
    common_core: Mapping[str, Any],
    *,
    knowledge_set: Mapping[str, Any] | None = None,
    recommendation_set: Mapping[str, Any] | None = None,
    coverage_matrix: Mapping[str, Any] | None = None,
    manifest: Mapping[str, Any] | None = None,
    integrated_view: Mapping[str, Any] | None = None,
    decision_patterns: Iterable[Mapping[str, Any]] | None = None,
    artifact_id: str | None = None,
) -> CanonicalProjectionSource:
    common_core = dict(common_core)
    knowledge_set = as_mapping(knowledge_set)
    recommendation_set = as_mapping(recommendation_set)
    manifest = as_mapping(manifest)
    coverage_states = extract_coverage_states(common_core, coverage_matrix)
    knowledge_claims = as_tuple_of_mappings(knowledge_set.get("knowledge_claims")) or tuple(
        {"knowledge_id": str(index + 1), "claim": claim}
        for index, claim in enumerate(common_core.get("knowledge_claims") or [])
    )
    recommendations = as_tuple_of_mappings(recommendation_set.get("recommendations")) or tuple(
        {"recommendation_id": str(item)} for item in common_core.get("recommendations") or []
    )
    exclusions = stable_text_items(recommendation_set.get("excluded_actions"))
    comparison_classifications = as_tuple_of_mappings(common_core.get("comparison_classifications"))
    limitations = stable_text_items(common_core.get("limitations"), knowledge_set.get("risks"))
    unknowns = stable_text_items(common_core.get("unknowns"), knowledge_set.get("unknowns"))
    strategic_context_constraints = strategic_constraints_payload(common_core.get("strategic_context_constraints"))
    cps_integrated_view = dict(integrated_view) if integrated_view is not None else build_default_integrated_view(knowledge_set, common_core, coverage_states)
    cps_decision_patterns = tuple(dict(item) for item in decision_patterns) if decision_patterns is not None else build_default_decision_patterns(knowledge_set)
    source_artifacts = {
        "context_definition": manifest.get("artifact_paths", {}).get("context_definition"),
        "evidence_set": manifest.get("artifact_paths", {}).get("evidence_set") or common_core.get("evidence_refs"),
        "knowledge_set": manifest.get("artifact_paths", {}).get("knowledge_set") or knowledge_set.get("artifact_id"),
        "recommendation_set": manifest.get("artifact_paths", {}).get("recommendation_set") or recommendation_set.get("artifact_id"),
        "coverage_matrix": manifest.get("artifact_paths", {}).get("coverage_matrix"),
        "common_product_core": manifest.get("artifact_paths", {}).get("common_product_core") or common_core.get("artifact_id"),
        "manifest": manifest.get("artifact_paths", {}).get("manifest") or manifest.get("artifact_id"),
        "ccd": strategic_context_constraints.get("source_artifact"),
    }
    return CanonicalProjectionSource(
        artifact_id=artifact_id or f"{common_core.get('artifact_id', 'AUC-001')}-CANONICAL-PROJECTION-SOURCE",
        status="stabilized_for_presentation",
        source_artifacts=source_artifacts,
        product_contract={
            "id": "SPEC-014",
            "version": CONTRACT_VERSION,
            "schema_family": PRODUCT_SCHEMA_FAMILY,
            "schema_version": PRODUCT_SCHEMA_VERSION,
        },
        projection_contracts={
            "projection_selection": "SPEC-010",
            "communication_context_transformation": "SPEC-011",
            "canonical_projection_consolidation": "SPEC-015",
        },
        period=as_mapping(common_core.get("period")),
        scope=as_mapping(common_core.get("scope")),
        sources=tuple(common_core.get("sources") or []),
        canonical_metrics=as_mapping(common_core.get("canonical_metrics")),
        coverage_states=coverage_states,
        knowledge_claims=knowledge_claims,
        analytical_narrative=as_mapping(knowledge_set.get("analytical_narrative")),
        integrated_view=cps_integrated_view,
        decision_patterns=cps_decision_patterns,
        recommendations=recommendations,
        limitations=limitations,
        unknowns=unknowns,
        future_evidence_gaps=infer_future_evidence_gaps(limitations, unknowns, exclusions, coverage_states),
        exclusions=exclusions,
        comparison_classifications=comparison_classifications,
        traceability={
            "common_core_fingerprint": common_core.get("semantic_fingerprint") or manifest.get("common_core_fingerprint"),
            "artifact_fingerprints": manifest.get("artifact_fingerprints", {}),
            "coverage_matrix_states_source": "coverage_matrix" if coverage_matrix else "common_core",
            "presentation_must_not_consult_prompts_for_content": True,
            "strategic_context_source": strategic_context_constraints.get("source_artifact"),
            "strategic_context_refs": list(strategic_context_constraints.get("source_refs") or []),
        },
        strategic_context_constraints=strategic_context_constraints,
    )


def validate_canonical_projection_source(cps: CanonicalProjectionSource | Mapping[str, Any]) -> list[ProductContractIssue]:
    data = cps.to_dict() if isinstance(cps, CanonicalProjectionSource) else dict(cps)
    issues: list[ProductContractIssue] = []
    required = (
        "source_artifacts",
        "product_contract",
        "projection_contracts",
        "period",
        "scope",
        "sources",
        "canonical_metrics",
        "coverage_states",
        "knowledge_claims",
        "integrated_view",
        "recommendations",
        "limitations",
        "unknowns",
        "traceability",
        "strategic_context_constraints",
    )
    for field_name in required:
        if not normalize_truthy(data.get(field_name)):
            issues.append(ProductContractIssue("CPS_MISSING_BLOCK", "blocking", f"Canonical Projection Source missing block: {field_name}"))

    if data.get("schema_family") != CANONICAL_PROJECTION_SCHEMA_FAMILY:
        issues.append(ProductContractIssue("CPS_SCHEMA_FAMILY_INVALID", "blocking", "Canonical Projection Source schema family is invalid"))
    if data.get("specification") != CANONICAL_PROJECTION_SPECIFICATION:
        issues.append(ProductContractIssue("CPS_SPECIFICATION_INVALID", "blocking", "Canonical Projection Source must declare SPEC-015"))
    issues.extend(validate_strategic_context_constraints(data.get("strategic_context_constraints"), artifact="canonical_projection_source.strategic_context_constraints"))
    comparison_items = as_tuple_of_mappings(data.get("comparison_classifications"))
    issues.extend(
        validate_comparison_classifications(
            comparison_items,
            artifact="canonical_projection_source.comparison_classifications",
            knowledge_set_stabilized=True,
            knowledge_items=data.get("knowledge_claims") or (),
        )
    )

    coverage_states = dict(data.get("coverage_states") or {})
    for question_id, state in coverage_states.items():
        if state not in VALID_PRODUCT_COVERAGE_STATES:
            issues.append(ProductContractIssue("CPS_INVALID_COVERAGE_STATE", "blocking", "CPS contains invalid coverage state", str(question_id)))
    missing_questions = sorted({definition.question_id for definition in QUESTION_DEFINITIONS} - set(coverage_states))
    for question_id in missing_questions:
        issues.append(ProductContractIssue("CPS_MISSING_COVERAGE_STATE", "blocking", "CPS is missing coverage state", question_id))

    for item in data.get("knowledge_claims") or []:
        if isinstance(item, Mapping):
            if not normalize_truthy(item.get("knowledge_id")):
                issues.append(ProductContractIssue("CPS_KNOWLEDGE_WITHOUT_ID", "blocking", "CPS knowledge claim must preserve a stable identity"))
            issues.extend(validate_campaign_signal_interpretation(item, artifact="canonical_projection_source.knowledge_claim"))
    for item in data.get("recommendations") or []:
        if isinstance(item, Mapping):
            if not normalize_truthy(item.get("recommendation_id")):
                issues.append(ProductContractIssue("CPS_RECOMMENDATION_WITHOUT_ID", "blocking", "CPS recommendation must preserve a stable identity"))
            issues.extend(validate_campaign_signal_interpretation(item, artifact="canonical_projection_source.recommendation"))
    return issues


def build_projection_from_cps(
    cps: CanonicalProjectionSource,
    projection_type: str,
    sections: Iterable[Mapping[str, Any]] = (),
    communication_context: Mapping[str, Any] | None = None,
) -> CanonicalProductProjection:
    if projection_type not in {"analytical", "executive"}:
        raise ValueError("projection_type must be analytical or executive")
    return CanonicalProductProjection(
        projection_type=projection_type,
        canonical_projection_source_id=cps.artifact_id,
        canonical_projection_source_fingerprint=cps.semantic_fingerprint,
        coverage_states=cps.coverage_states,
        unknowns=cps.unknowns,
        limitations=cps.limitations,
        future_evidence_gaps=cps.future_evidence_gaps,
        recommendation_refs=tuple(recommendation_identity(item) for item in cps.recommendations),
        knowledge_refs=tuple(value for value in (knowledge_identity(item) for item in cps.knowledge_claims) if value),
        communication_context=dict(communication_context or {"projection": projection_type}),
        comparison_classifications=tuple(dict(item) for item in cps.comparison_classifications),
        sections=tuple(dict(section) for section in sections),
        strategic_context_constraints=cps.strategic_context_constraints,
    )


def flatten_text(value: Any) -> str:
    if isinstance(value, Mapping):
        return "\n".join(f"{key}: {flatten_text(nested)}" for key, nested in value.items())
    if isinstance(value, (list, tuple, set)):
        return "\n".join(flatten_text(item) for item in value)
    return str(value) if value is not None else ""


def has_section_reference(value: Any) -> bool:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if str(key) in PRESENTATION_SECTION_REF_FIELDS and normalize_truthy(nested):
                return True
            if has_section_reference(nested):
                return True
    elif isinstance(value, (list, tuple)):
        return any(has_section_reference(item) for item in value)
    return False


def find_unapproved_presentation_section_fields(value: Any, path: str = "sections") -> list[str]:
    findings: list[str] = []
    if isinstance(value, Mapping):
        for key, nested_value in value.items():
            key_text = str(key)
            current_path = f"{path}.{key_text}"
            if key_text not in ALLOWED_PRESENTATION_SECTION_FIELDS:
                findings.append(current_path)
            findings.extend(find_unapproved_presentation_section_fields(nested_value, current_path))
    elif isinstance(value, (list, tuple)):
        for index, nested_value in enumerate(value):
            findings.extend(find_unapproved_presentation_section_fields(nested_value, f"{path}[{index}]"))
    return findings


def validate_presentation_sections_are_cps_referenced(sections: Any) -> list[ProductContractIssue]:
    issues: list[ProductContractIssue] = []
    if not isinstance(sections, (list, tuple)):
        return issues
    for index, section in enumerate(sections):
        if not isinstance(section, Mapping):
            continue
        if not has_section_reference(section):
            issues.append(
                ProductContractIssue(
                    "PROJECTION_SECTION_UNTRACED",
                    "blocking",
                    f"Presentation section {index} must reference CPS content instead of carrying standalone narrative",
                )
            )
    return issues


def validate_presentation_items_are_structured_refs(sections: Any) -> list[ProductContractIssue]:
    issues: list[ProductContractIssue] = []
    if not isinstance(sections, (list, tuple)):
        return issues
    for section_index, section in enumerate(sections):
        if not isinstance(section, Mapping) or "items" not in section:
            continue
        items = section.get("items")
        if not isinstance(items, (list, tuple)):
            issues.append(
                ProductContractIssue(
                    "PROJECTION_ITEMS_INVALID",
                    "blocking",
                    f"Presentation section {section_index} items must be a list of CPS-referenced objects",
                )
            )
            continue
        for item_index, item in enumerate(items):
            if not isinstance(item, Mapping):
                issues.append(
                    ProductContractIssue(
                        "PROJECTION_ITEM_FREE_TEXT",
                        "blocking",
                        f"Presentation section {section_index} item {item_index} must be a CPS-referenced object, not free text",
                    )
                )
                continue
            if not has_section_reference(item):
                issues.append(
                    ProductContractIssue(
                        "PROJECTION_ITEM_UNTRACED",
                        "blocking",
                        f"Presentation section {section_index} item {item_index} must include its own CPS reference",
                    )
                )
    return issues


def validate_projection_against_cps(
    cps: CanonicalProjectionSource,
    projection: CanonicalProductProjection | Mapping[str, Any],
) -> list[ProductContractIssue]:
    data = projection.to_dict() if isinstance(projection, CanonicalProductProjection) else dict(projection)
    issues: list[ProductContractIssue] = []
    if data.get("canonical_projection_source_fingerprint") != cps.semantic_fingerprint:
        issues.append(ProductContractIssue("PROJECTION_CPS_DIVERGENCE", "blocking", "Projection does not reference the CPS fingerprint"))
    if data.get("canonical_projection_source_id") != cps.artifact_id:
        issues.append(ProductContractIssue("PROJECTION_CPS_ID_DIVERGENCE", "blocking", "Projection does not reference the CPS artifact id"))
    if dict(data.get("coverage_states") or {}) != dict(cps.coverage_states):
        issues.append(ProductContractIssue("PROJECTION_COVERAGE_DIVERGENCE", "blocking", "Projection changes coverage states"))
    if tuple(data.get("unknowns") or ()) != tuple(cps.unknowns):
        issues.append(ProductContractIssue("PROJECTION_UNKNOWN_DIVERGENCE", "blocking", "Projection changes UNKNOWNs"))
    if tuple(data.get("limitations") or ()) != tuple(cps.limitations):
        issues.append(ProductContractIssue("PROJECTION_LIMITATION_DIVERGENCE", "blocking", "Projection changes limitations"))
    if dict(data.get("future_evidence_gaps") or {}) != dict(cps.future_evidence_gaps):
        issues.append(ProductContractIssue("PROJECTION_GAP_DIVERGENCE", "blocking", "Projection changes future evidence gaps"))
    if dict(data.get("strategic_context_constraints") or {}) != dict(cps.strategic_context_constraints):
        issues.append(ProductContractIssue("PROJECTION_STRATEGIC_CONTEXT_DIVERGENCE", "blocking", "Projection changes strategic context constraints"))
    expected_comparisons = [dict(item) for item in cps.comparison_classifications]
    if list(data.get("comparison_classifications") or []) != expected_comparisons:
        issues.append(ProductContractIssue("PROJECTION_COMPARISON_CLASSIFICATION_DIVERGENCE", "blocking", "Projection changes comparison classifications"))
    if data.get("derived_from_projection"):
        issues.append(ProductContractIssue("PROJECTION_SIBLING_RULE_VIOLATION", "blocking", "Projection cannot derive from another projection"))

    expected_recommendations = [recommendation_identity(item) for item in cps.recommendations]
    if list(data.get("recommendation_refs") or []) != expected_recommendations:
        issues.append(ProductContractIssue("PROJECTION_RECOMMENDATION_DIVERGENCE", "blocking", "Projection changes recommendation identity, priority or success criteria"))

    sections = data.get("sections", ())
    blocked_comparison_ids = {
        str(item.get("comparison_id"))
        for item in cps.comparison_classifications
        if isinstance(item, Mapping) and item.get("governance_status") == COMPARISON_GOVERNANCE_BLOCKED
    }
    for blocked_path in find_blocked_comparison_refs(sections, blocked_comparison_ids):
        issues.append(ProductContractIssue("PROJECTION_BLOCKED_COMPARISON_PRESENTED", "blocking", f"Projection presents a blocked comparison: {blocked_path}"))
    prohibited_paths = find_prohibited_nested_fields(sections, PROHIBITED_PRESENTATION_SECTION_FIELDS, "sections")
    for prohibited_path in prohibited_paths:
        issues.append(ProductContractIssue("PROJECTION_FIELD_PROHIBITED", "blocking", f"Projection section cannot contain canonical field: {prohibited_path}"))
    unapproved_paths = find_unapproved_presentation_section_fields(sections, "sections")
    for unapproved_path in unapproved_paths:
        issues.append(ProductContractIssue("PROJECTION_UNAPPROVED_SECTION_FIELD", "blocking", f"Projection section field is not a CPS reference or presentation control: {unapproved_path}"))
    issues.extend(validate_presentation_sections_are_cps_referenced(sections))
    issues.extend(validate_presentation_items_are_structured_refs(sections))

    text = flatten_text(sections).lower()
    for phrase in PRESENTATION_BLOCKED_PHRASES:
        if phrase in text:
            issues.append(ProductContractIssue("PROJECTION_NEW_KNOWLEDGE_BLOCKED", "blocking", f"Projection contains blocked Presentation claim: {phrase}"))
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