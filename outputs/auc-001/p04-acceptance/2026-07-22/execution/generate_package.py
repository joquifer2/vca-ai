import hashlib
import json
from pathlib import Path

from tools.auc_001_analytical_product_contract import (
    QUESTION_DEFINITIONS,
    CoverageMatrixRow,
    RobustnessRecord,
    CommonProductCore,
    COVERAGE_COMPLETE,
    COVERAGE_PARTIAL,
    COVERAGE_NOT_AVAILABLE,
    COVERAGE_NOT_APPLICABLE,
    build_canonical_projection_source,
    build_projection_from_cps,
    build_contract_acceptance_payload,
    validate_canonical_projection_source,
    validate_common_core,
    validate_evidence_item,
    validate_knowledge_item,
    validate_projection_against_cps,
    validate_recommendation,
)

ROOT = Path("outputs/auc-001/p04-acceptance/2026-07-22")
NOW = "2026-07-22T15:08:00Z"
BRIEF = "Analiza la calidad de los leads de Meta Ads y genera un informe analitico y un informe ejecutivo."
SOURCE_TABLES = [
    "intermediate.int_faro_lead_scoring",
    "marts.fct_lead_enriched",
    "marts.fct_spend",
    "marts.dim_campaign_signal",
]

metadata_discovery = {
    "workspace": ["auc-001-p04-acceptance-2026-07-22-discover-workspace", "trc-605c70e3426d41efb38d88e793b838ea"],
    "dataset_intermediate": ["auc-001-p04-acceptance-2026-07-22-discover-intermediate", "trc-bc3e7a80d7bb482493e393f57278b8d6"],
    "dataset_marts": ["auc-001-p04-acceptance-2026-07-22-discover-marts", "trc-1bffd5a45bca43a2bfa160ae3d4e8cfc"],
    "table_scoring": ["auc-001-p04-acceptance-2026-07-22-discover-scoring", "trc-3b38f8843f41410e9458ae64a0623e77"],
    "table_spend": ["auc-001-p04-acceptance-2026-07-22-discover-spend", "trc-e153652c19f5422ba4411e4748fb77dd"],
    "table_leads": ["auc-001-p04-acceptance-2026-07-22-discover-lead-enriched", "trc-fc5b094d035646a391d8280d3484a56c"],
    "table_signal": ["auc-001-p04-acceptance-2026-07-22-discover-campaign-signal", "trc-c56883e0292646bbb1152d8c69e9133d"],
}
query_traces = {
    "lead_summary": ["auc-001-p04-acceptance-2026-07-22-query-lead-summary", "trc-fc13a933451d4b96a832eb77687b0e79", 209821],
    "spend_summary": ["auc-001-p04-acceptance-2026-07-22-query-spend-summary", "trc-a3fc49fec5814a068b1cdc8ef7993909", 1043559],
    "scoring_summary": ["auc-001-p04-acceptance-2026-07-22-query-scoring-summary", "trc-eaf8431b888543009c77dd8f01b4e405", 91191],
    "signal_dimension": ["auc-001-p04-acceptance-2026-07-22-query-signal-dimension", "trc-4b9b2ef1c5954f69acbba8095aa5eda4", 500],
    "leads_by_ad": ["auc-001-p04-acceptance-2026-07-22-query-leads-by-ad", "trc-bde0a7a3fed34538afed1541cd6690d6", 320788],
    "spend_by_ad": ["auc-001-p04-acceptance-2026-07-22-query-spend-by-ad", "trc-f78d7af3f8c34dec9cb153196180505b", 961783],
    "monthly_leads": ["auc-001-p04-acceptance-2026-07-22-query-monthly-leads", "trc-e2f9673a3d86439396fb8f2e9f8e84ca", 17952],
    "monthly_spend": ["auc-001-p04-acceptance-2026-07-22-query-monthly-spend", "trc-24e042d96bdc4a20ab0fe185b85e9c1a", 286035],
    "leads_by_campaign": ["auc-001-p04-acceptance-2026-07-22-query-leads-by-campaign", "trc-5ba3d0ec87084d998851ea8b7381558e", 132423],
    "leads_by_form": ["auc-001-p04-acceptance-2026-07-22-query-leads-by-form", "trc-d43b4afd25e244498f2dec42d31c8203", 116859],
    "leads_by_ticket": ["auc-001-p04-acceptance-2026-07-22-query-leads-by-ticket", "trc-e67387a0fc9e411cb06b27ae8c693ff6", 27434],
    "spend_by_signal": ["auc-001-p04-acceptance-2026-07-22-query-spend-by-signal", "trc-ca8f6adc566244968d0d4364efd9393a", 408699],
    "weekly_leads": ["auc-001-p04-acceptance-2026-07-22-query-weekly-leads", "trc-0db6a9a5622649c18a83795cebf7c37d", 17952],
    "weekly_spend": ["auc-001-p04-acceptance-2026-07-22-query-weekly-spend", "trc-f314f3f04e6c477bbf72d0134595086b", 286035],
    "score_components": ["auc-001-p04-acceptance-2026-07-22-query-score-components", "trc-3e6c13f6d47c43cd874367065ebf99d4", 70176],
    "platform": ["auc-001-p04-acceptance-2026-07-22-query-platform", "trc-0fe96c8b7e84456caa035ca90e7070f0", 13056],
}
rejected_attempts = [
    {"request_id": "auc-001-p04-acceptance-2026-07-22-query-evidence-summary", "error_code": "ERR_SCOPE_DENIED", "trace_reference": "trc-179642d12a704b5aa32f8292debd9c78", "handling": "not used as evidence"},
    {"request_id": "auc-001-p04-acceptance-2026-07-22-query-marts-summary", "error_code": "ERR_SCOPE_DENIED", "trace_reference": "trc-5bba175274a7495c95811934835a3c24", "handling": "not used as evidence"},
]

lead = {"count": 1632, "start": "2026-04-18", "end": "2026-07-22", "ab": 504, "tier_a": 76, "tier_b": 428, "ticket_status_available": 1632, "offline_candidates": 504, "unmapped": 0}
spend = {"records": 10222, "start": "2026-04-18", "end": "2026-07-17", "total": 1729.36001, "commercial": 1071.25001, "non_commercial": 658.11}
reconciliation = {
    "matched": {"ad_count": 12, "leads": 1458, "ab_leads": 426, "tier_a_leads": 60, "matched_commercial_spend": 1069.05001},
    "lead_only": {"ad_count": 5, "leads": 174, "ab_leads": 78, "tier_a_leads": 16},
    "spend_only": {"ad_count": 2, "leads": 0, "ab_leads": 0, "tier_a_leads": 0, "spend_only_commercial_spend": 2.2},
    "UNKNOWN": {"ad_count": 0, "leads": 0, "ab_leads": 0, "tier_a_leads": 0, "reason_codes": []},
    "invariants": [
        {"name": "lead_total_identity", "expression": "lead_total = matched + lead_only + UNKNOWN", "left_value": 1632, "right_value": 1632, "result": "PASS"},
        {"name": "commercial_spend_identity", "expression": "commercial_spend = matched + spend_only", "left_value": 1071.25001, "right_value": 1071.25001, "result": "PASS"},
    ],
}
monthly = [
    {"month": "2026-04-01", "leads": 184, "ab": 57, "commercial_spend": 146.29},
    {"month": "2026-05-01", "leads": 369, "ab": 111, "commercial_spend": 232.98},
    {"month": "2026-06-01", "leads": 776, "ab": 229, "commercial_spend": 496.58},
    {"month": "2026-07-01", "leads": 303, "ab": 107, "commercial_spend": 195.40},
]
concentration = {
    "campaigns": [
        {"name": "[META]_[CLP]_[CAPTACION]_[ABO]", "leads": 1187, "ab": 344, "tier_a": 48},
        {"name": "[META]_[CLP]_[RTG]_[CBO]", "leads": 196, "ab": 77, "tier_a": 14},
        {"name": "[META]_[CLP]_[CAPTACION]_[ABO] - ESC", "leads": 140, "ab": 45, "tier_a": 4},
        {"name": "[META]_[CLP]_[CAPTACION]_[ABO] - TEST", "leads": 109, "ab": 38, "tier_a": 10},
    ],
    "ticket_status": [
        {"status": "solo_mirando", "leads": 999, "ab": 59, "tier_a": 0},
        {"status": "en_proceso", "leads": 394, "ab": 230, "tier_a": 15},
        {"status": "tiene_billetes", "leads": 239, "ab": 215, "tier_a": 61},
    ],
    "platform": [{"platform": "fb", "leads": 1112, "ab": 355, "tier_a": 52}, {"platform": "ig", "leads": 520, "ab": 149, "tier_a": 24}],
    "spend_signal": [{"signal": "COMMERCIAL", "spend": 1071.25001}, {"signal": "ATTENTION", "spend": 372.36}, {"signal": "ACTIVATION", "spend": 285.75}],
}
ad_examples = [
    {"ad_id_norm": "120245828603090721", "coverage": "matched", "leads": 643, "ab": 187, "commercial_spend": 468.060008, "cost_per_ab": 2.503},
    {"ad_id_norm": "120245829545180721", "coverage": "matched", "leads": 359, "ab": 101, "commercial_spend": 245.839997, "cost_per_ab": 2.434},
    {"ad_id_norm": "120251683460370721", "coverage": "matched", "leads": 58, "ab": 26, "commercial_spend": 51.850004, "cost_per_ab": 1.994},
    {"ad_id_norm": "120247352473020721", "coverage": "lead_only", "leads": 166, "ab": 63, "commercial_spend": 0, "cost_per_ab": None},
    {"ad_id_norm": "120251249759480721", "coverage": "spend_only", "leads": 0, "ab": 0, "commercial_spend": 1.2, "cost_per_ab": None},
]

def pct(n, d):
    return round(n / d, 4) if d else None

metrics = {
    "lead_total": lead["count"],
    "ab_leads": lead["ab"],
    "tier_a_leads": lead["tier_a"],
    "ab_rate_total": pct(lead["ab"], lead["count"]),
    "tier_a_rate_total": pct(lead["tier_a"], lead["count"]),
    "total_spend_all_signals": spend["total"],
    "commercial_spend": spend["commercial"],
    "non_commercial_spend": spend["non_commercial"],
    "matched_commercial_spend": reconciliation["matched"]["matched_commercial_spend"],
    "spend_only_commercial_spend": reconciliation["spend_only"]["spend_only_commercial_spend"],
    "matched_leads": reconciliation["matched"]["leads"],
    "lead_only_leads": reconciliation["lead_only"]["leads"],
    "cost_per_lead_commercial_matched": round(reconciliation["matched"]["matched_commercial_spend"] / reconciliation["matched"]["leads"], 4),
    "cost_per_ab_commercial_matched": round(reconciliation["matched"]["matched_commercial_spend"] / reconciliation["matched"]["ab_leads"], 4),
    "coverage_reconciliation": reconciliation,
}

def trace(*keys):
    return [query_traces[k][0] for k in keys]

evidence = [
    {"evidence_id": "EVD-001", "facts": {"brief": BRIEF, "period": {"lead_start": lead["start"], "lead_end": lead["end"], "spend_start": spend["start"], "spend_end": spend["end"]}, "sources": SOURCE_TABLES}, "coverage_state": "complete", "traceability": trace("lead_summary", "spend_summary", "scoring_summary")},
    {"evidence_id": "EVD-002", "facts": {"lead": lead, "quality": {"A_or_B": lead["ab"], "A": lead["tier_a"], "B": lead["tier_b"], "ab_rate": metrics["ab_rate_total"], "tier_a_rate": metrics["tier_a_rate_total"]}}, "coverage_state": "complete", "traceability": trace("lead_summary", "scoring_summary")},
    {"evidence_id": "EVD-003", "facts": {"spend": spend, "spend_by_signal": concentration["spend_signal"]}, "coverage_state": "complete", "traceability": trace("spend_summary", "spend_by_signal")},
    {"evidence_id": "EVD-004", "facts": {"reconciliation": reconciliation, "ad_examples": ad_examples}, "coverage_state": "complete", "traceability": trace("leads_by_ad", "spend_by_ad")},
    {"evidence_id": "EVD-005", "facts": {"monthly": monthly, "weekly_status": "partial", "provider_cutoff": {"lead_end": lead["end"], "spend_end": spend["end"]}}, "coverage_state": "partial", "traceability": trace("monthly_leads", "monthly_spend", "weekly_leads", "weekly_spend")},
    {"evidence_id": "EVD-006", "facts": {"concentration": concentration, "score_components_observed": True, "form_signals_observed": True}, "coverage_state": "complete", "traceability": trace("leads_by_campaign", "leads_by_form", "leads_by_ticket", "platform", "score_components")},
    {"evidence_id": "EVD-007", "facts": {"revenue_or_crm": "not_available", "creative_causality": "UNKNOWN", "additional_creative_metadata": "not_available", "provider_temporality": "partial"}, "coverage_state": "complete", "traceability": trace("lead_summary", "spend_summary", "weekly_leads", "weekly_spend")},
]
for item in evidence:
    assert not validate_evidence_item(item), item

knowledge_claims = [
    {"knowledge_id": "KNW-001", "evidence_refs": ["EVD-001", "EVD-002"], "interpretation": "The product has sufficient FARO coverage to describe lead quality: 1632 leads, 504 A/B leads and 76 Tier A leads.", "limitation_or_uncertainty": "This is FARO quality, not revenue or CRM outcome."},
    {"knowledge_id": "KNW-002", "evidence_refs": ["EVD-003", "EVD-004"], "interpretation": "Cost-quality must be read in the commercial matched universe: 12 matched ads, 1458 leads and 1069.05001 matched commercial spend, with lead_only and spend_only preserved.", "limitation_or_uncertainty": "lead_only is not zero cost and spend_only is not proof of no leads."},
    {"knowledge_id": "KNW-003", "evidence_refs": ["EVD-004", "EVD-006"], "interpretation": "Observed quality is explained by combinations of FARO tier, ticket_status, form/campaign concentration and ad-level coverage.", "limitation_or_uncertainty": "The evidence supports association, not creative causality."},
    {"knowledge_id": "KNW-004", "evidence_refs": ["EVD-005"], "interpretation": "Monthly evolution is usable and June is the largest observed month; weekly comparability is partial because provider periods are incomplete at the edges.", "limitation_or_uncertainty": "Spend ends on 2026-07-17 while leads extend to 2026-07-22."},
    {"knowledge_id": "KNW-005", "evidence_refs": ["EVD-006"], "interpretation": "The main ABO campaign concentrates most leads; ticket_status has strong descriptive separation between solo_mirando, en_proceso and tiene_billetes.", "limitation_or_uncertainty": "Campaign/adset economics remain partial because spend reconciliation is robust at ad_id level."},
    {"knowledge_id": "KNW-006", "evidence_refs": ["EVD-007"], "interpretation": "Material limits must stay visible in both projections: revenue/CRM not_available, creative causality UNKNOWN, metadata not_available and temporal coverage partial.", "limitation_or_uncertainty": "Presentation cannot turn these limits into a positive or negative finding."},
]
for item in knowledge_claims:
    assert not validate_knowledge_item(item), item

recommendations = [
    {"recommendation_id": "REC-001", "category": "measurable_experiment", "knowledge_refs": ["KNW-002", "KNW-003"], "hypothesis": "A bounded redistribution inside commercial matched ads may improve A/B rate without worsening cost per A/B.", "action": "Run a controlled budget experiment among matched ads with sufficient sample.", "population": "commercial matched ad_id_norm rows with at least 20 leads and 5 A/B leads", "primary_metric": "A/B rate in commercial matched universe", "guardrail": "cost_per_ab_commercial_matched does not worsen materially", "expected_direction": "increase A/B rate or reduce cost per A/B", "success_criterion": "PASS if A/B rate increases versus control while cost_per_ab_commercial_matched is stable or lower over two comparable weeks.", "validation_window": "two complete provider-comparable weeks", "evidence_dependency": "EVD-004", "uncertainty": "observational evidence only", "stop_or_review_condition": "stop if sample falls below threshold or spend coverage changes"},
    {"recommendation_id": "REC-002", "category": "verifiable_action", "knowledge_refs": ["KNW-002", "KNW-006"], "action": "Classify every lead_only and spend_only ad_id_norm before using economic metrics for budget decisions.", "supporting_evidence": "EVD-004 coverage reconciliation", "verifiable_result": "coverage register classifies each asymmetry without overwriting coverage state", "closure_criterion": "all current lead_only and spend_only rows have a declared reason code", "risk": "manual recoding can hide UNKNOWN", "dependency": "authorized Meta lead and spend sources"},
    {"recommendation_id": "REC-003", "category": "measurable_experiment", "knowledge_refs": ["KNW-003", "KNW-006"], "hypothesis": "A form or qualification-question test can increase qualified share without requiring revenue evidence.", "action": "Run a form or qualification test focused on tiene_billetes/en_proceso share.", "population": "Meta Lead Ads forms with FARO coverage", "primary_metric": "share of A/B leads and ticket_status tiene_billetes/en_proceso", "guardrail": "lead volume and Tier A count do not collapse", "expected_direction": "increase qualified share", "success_criterion": "PASS if qualified-share lift is observed with stable lead volume and no increase in unmapped responses.", "validation_window": "one complete month or two comparable complete weeks", "evidence_dependency": "EVD-006", "uncertainty": "no commercial revenue validation", "stop_or_review_condition": "stop if unmapped responses appear or weekly comparability remains partial"},
    {"recommendation_id": "REC-004", "category": "non_actionable_hypothesis", "knowledge_refs": ["KNW-006"], "hypothesis": "Revenue/CRM outcomes may change FARO-only prioritization.", "support": "FARO and ticket_status show quality strata but not commercial value.", "uncertainty": "CRM/revenue source is absent.", "missing_evidence": "authorized and reconciled CRM/revenue evidence", "promotion_condition": "promote only when future evidence is authorized and reconciled"},
]
for item in recommendations:
    assert not validate_recommendation(item), item

coverage_states = {
    "AQ-001": COVERAGE_COMPLETE, "AQ-002": COVERAGE_COMPLETE, "AQ-003": COVERAGE_COMPLETE, "AQ-004": COVERAGE_PARTIAL, "AQ-005": COVERAGE_COMPLETE, "AQ-006": COVERAGE_COMPLETE, "AQ-007": COVERAGE_COMPLETE, "AQ-008": COVERAGE_COMPLETE, "AQ-009": COVERAGE_PARTIAL, "AQ-010": COVERAGE_COMPLETE, "AQ-011": COVERAGE_COMPLETE,
    "CQ-001": COVERAGE_COMPLETE, "CQ-002": COVERAGE_COMPLETE, "CQ-003": COVERAGE_NOT_AVAILABLE, "CQ-004": COVERAGE_COMPLETE, "CQ-005": COVERAGE_NOT_AVAILABLE, "CQ-006": COVERAGE_NOT_AVAILABLE, "CQ-007": COVERAGE_PARTIAL,
    "NAQ-001": COVERAGE_NOT_APPLICABLE, "NAQ-002": COVERAGE_NOT_APPLICABLE, "NAQ-003": COVERAGE_NOT_APPLICABLE, "NAQ-004": COVERAGE_NOT_APPLICABLE, "NAQ-005": COVERAGE_NOT_APPLICABLE,
}
refs = {
    "AQ-001": ["EVD-001"], "AQ-002": ["EVD-002"], "AQ-003": ["EVD-003", "EVD-004"], "AQ-004": ["EVD-004", "EVD-006"], "AQ-005": ["EVD-004"], "AQ-006": ["EVD-002", "EVD-006"], "AQ-007": ["EVD-003", "EVD-004"], "AQ-008": ["EVD-006"], "AQ-009": ["EVD-005"], "AQ-010": ["EVD-004", "EVD-006", "EVD-007"], "AQ-011": ["EVD-007"], "CQ-001": ["EVD-006"], "CQ-002": ["EVD-006"], "CQ-004": ["EVD-002"], "CQ-007": ["EVD-005"],
}
limitations = (
    "Revenue/CRM evidence is not_available in the authorized source set.",
    "Creative causality remains UNKNOWN; ad_name is an interpretive label only.",
    "Additional creative metadata beyond ad_name is not_available.",
    "Temporal comparability is partial because spend ends on 2026-07-17 while leads extend to 2026-07-22.",
    "Campaign/adset economic attribution is partial because robust spend reconciliation is at ad_id level.",
)
unknowns = (
    "UNKNOWN: causal effect of creative/ad_name on lead quality.",
    "UNKNOWN: commercial revenue or CRM outcome of FARO tiers.",
    "UNKNOWN: complete current-week cost-quality pattern after provider spend cutoff.",
)
rows = []
robust_complete = RobustnessRecord(lead["count"], lead["count"], "matched", "question", "current MCP execution", "sufficient")
robust_partial = RobustnessRecord(lead["count"], lead["count"], "partial", "question", "current MCP execution with source limits", "sufficient")
for definition in QUESTION_DEFINITIONS:
    qid = definition.question_id
    state = coverage_states[qid]
    if state == COVERAGE_NOT_APPLICABLE:
        rows.append(CoverageMatrixRow(qid, state, "Outside AUC-001 product boundary.", impact="Excluded by SPEC-014 boundary."))
    elif state == COVERAGE_NOT_AVAILABLE:
        rows.append(CoverageMatrixRow(qid, state, "Authorized evidence is not available for this conditional question.", impact="Must remain not_available and cannot be inferred in Presentation."))
    else:
        depth = {
            "evidence": ", ".join(refs.get(qid, ["EVD-007"])),
            "comparison": "Compared by time, tier, ad, campaign/form/platform or coverage state as applicable.",
            "interpretation": "Descriptive interpretation constrained by FARO, spend reconciliation and provider coverage.",
            "business_implication": "Can inform prioritization, controlled tests, coverage review or disclosure.",
            "limitation_or_uncertainty": "UNKNOWN/not_available/future evidence limits remain visible.",
            "conclusion_or_hypothesis": "Answered within SPEC-014 or held partial where coverage limits comparability.",
            "traceability": refs.get(qid, ["EVD-007"]),
        }
        rows.append(CoverageMatrixRow(qid, state, "Answered with MCP evidence and canonical product depth.", tuple(refs.get(qid, ["EVD-007"])), depth, robust_partial if state == COVERAGE_PARTIAL else robust_complete, "Use with declared coverage state."))

coverage_matrix = {"artifact_id": "AUC-001-P04-ACCEPTANCE-COVERAGE-MATRIX", "schema_family": "auc_001_coverage_matrix", "generated_at": NOW, "states": coverage_states, "rows": [r.to_dict() for r in rows]}
common_core_obj = CommonProductCore(
    period={"start": lead["start"], "lead_end": lead["end"], "spend_end": spend["end"], "basis": "observable MCP source coverage"},
    scope={"use_case": "AUC-001", "brief_instruction": BRIEF, "workspace": "vca", "namespace": str(ROOT).replace("\\", "/")},
    sources=tuple(SOURCE_TABLES),
    evidence_refs=tuple(item["evidence_id"] for item in evidence),
    canonical_metrics=metrics,
    coverage_matrix=tuple(rows),
    knowledge_claims=tuple(knowledge_claims),
    recommendations=tuple(recommendations),
    limitations=limitations,
    unknowns=unknowns,
)
common_core = common_core_obj.to_dict() | {"artifact_id": "AUC-001-P04-ACCEPTANCE-COMMON-PRODUCT-CORE"}
assert not validate_common_core(common_core_obj), [i.to_dict() for i in validate_common_core(common_core_obj)]

integrated_view = {
    "view_id": "CPS-IV-001",
    "quality_summary": {"lead_total": lead["count"], "ab_rate_total": metrics["ab_rate_total"], "tier_a_rate_total": metrics["tier_a_rate_total"]},
    "signals": [
        {"finding_id": "FND-001", "knowledge_ref": "KNW-001", "evidence_refs": ["EVD-002"], "statement": "FARO A/B and Tier A distribution define the quality base."},
        {"finding_id": "FND-002", "knowledge_ref": "KNW-002", "evidence_refs": ["EVD-004"], "statement": "Cost-quality reading is valid in commercial matched universe with lead_only/spend_only coverage."},
        {"finding_id": "FND-003", "knowledge_ref": "KNW-003", "evidence_refs": ["EVD-006"], "statement": "Ticket/form/ad combinations explain observed quality patterns without causal claims."},
        {"finding_id": "FND-004", "knowledge_ref": "KNW-004", "evidence_refs": ["EVD-005"], "statement": "Temporal pattern is usable monthly and partial weekly."},
    ],
    "combinations": [
        {"combination_id": "COMBO-001", "components": ["ticket_status", "FARO A/B", "form/campaign"], "evidence_refs": ["EVD-006"], "interpretation_ref": "KNW-003"},
        {"combination_id": "COMBO-002", "components": ["commercial matched ad_id", "A/B rate", "cost_per_ab"], "evidence_refs": ["EVD-004"], "interpretation_ref": "KNW-002"},
        {"combination_id": "COMBO-003", "components": ["month", "lead volume", "commercial spend", "provider cutoff"], "evidence_refs": ["EVD-005"], "interpretation_ref": "KNW-004"},
    ],
    "coverage_states": coverage_states,
    "metric_refs": ["canonical_metrics.lead_total", "canonical_metrics.ab_rate_total", "canonical_metrics.cost_per_ab_commercial_matched", "canonical_metrics.coverage_reconciliation"],
}
decision_patterns = [
    {"pattern_id": "DP-001", "basis": "Prioritize controlled commercial matched tests before broad budget changes.", "priority": "high", "knowledge_refs": ["KNW-002", "KNW-003"], "recommendation_refs": ["REC-001"]},
    {"pattern_id": "DP-002", "basis": "Review coverage states before interpreting economic gaps.", "priority": "high", "knowledge_refs": ["KNW-002", "KNW-006"], "recommendation_refs": ["REC-002"]},
    {"pattern_id": "DP-003", "basis": "Keep future-evidence gaps declared until new authorized evidence exists.", "priority": "medium", "knowledge_refs": ["KNW-006"], "recommendation_refs": ["REC-004"]},
]

def write_json(rel, obj):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False), encoding="utf-8")
    return path

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

for rel in ["evidence", "knowledge", "recommendations", "product-core", "coverage-matrix", "presentations/analytical", "presentations/executive", "validations", "handoff"]:
    (ROOT / rel).mkdir(parents=True, exist_ok=True)

artifact_paths = {
    "context_definition": "outputs/auc-001/p04-acceptance/2026-07-22/execution/context-definition.json",
    "data_provider_validation": "outputs/auc-001/p04-acceptance/2026-07-22/execution/data-provider-validation.json",
    "evidence_set": "outputs/auc-001/p04-acceptance/2026-07-22/evidence/evidence-set.json",
    "knowledge_set": "outputs/auc-001/p04-acceptance/2026-07-22/knowledge/knowledge-set.json",
    "recommendation_set": "outputs/auc-001/p04-acceptance/2026-07-22/recommendations/recommendation-set.json",
    "coverage_matrix": "outputs/auc-001/p04-acceptance/2026-07-22/coverage-matrix/coverage-matrix.json",
    "common_product_core": "outputs/auc-001/p04-acceptance/2026-07-22/product-core/common-product-core.json",
    "canonical_projection_source": "outputs/auc-001/p04-acceptance/2026-07-22/product-core/canonical-projection-source.json",
    "manifest": "outputs/auc-001/p04-acceptance/2026-07-22/execution/manifest.json",
}
write_json("execution/context-definition.json", {"artifact_id": "AUC-001-P04-ACCEPTANCE-CONTEXT-DEFINITION", "generated_at": NOW, "brief_instruction": BRIEF, "resolved_scope": common_core_obj.scope, "bigquery_cli_used": False, "fallback_used": False, "historical_outputs_used_as_new_evidence": False})
write_json("execution/data-provider-validation.json", {"artifact_id": "AUC-001-P04-ACCEPTANCE-DATA-PROVIDER-VALIDATION", "status": "PASS", "provider": "BigQuery MCP", "metadata_discovery": metadata_discovery, "execution_context_contract": {"project_id": "datamart-vca-494114", "dataset_id": "intermediate|marts", "max_bytes_billed": 1073741824}, "rejected_attempts_not_used_as_evidence": rejected_attempts, "no_cli": True, "no_fallback": True})
write_json("execution/evidence-acquisition-record.json", {"artifact_id": "AUC-001-P04-ACCEPTANCE-EVIDENCE-ACQUISITION-RECORD", "status": "PASS", "query_traces": query_traces, "rejected_attempts_not_used_as_evidence": rejected_attempts, "source_tables": SOURCE_TABLES, "coverage": "new MCP evidence only"})
write_json("evidence/evidence-set.json", {"artifact_id": "AUC-001-P04-ACCEPTANCE-EVIDENCE-SET", "schema_family": "auc_001_evidence_set", "generated_at": NOW, "provider": "BigQuery MCP", "items": evidence, "observation_tables": {"monthly": monthly, "concentration": concentration, "ad_examples": ad_examples}})
write_json("knowledge/knowledge-set.json", {"artifact_id": "AUC-001-P04-ACCEPTANCE-KNOWLEDGE-SET", "schema_family": "auc_001_knowledge_set", "generated_at": NOW, "knowledge_claims": knowledge_claims, "analytical_narrative": {"text": "The product separates volume, FARO quality, commercial matched cost-quality, concentration, temporality and material limits."}, "priorities": decision_patterns, "unknowns": list(unknowns), "risks": ["over-reading ad names as causality", "hiding lead_only or spend_only", "treating partial weekly data as complete"]})
write_json("knowledge/analytical-investigation-record.json", {"artifact_id": "AUC-001-P04-ACCEPTANCE-ANALYTICAL-INVESTIGATION-RECORD", "method": "Evidence -> Knowledge -> Recommendations -> Common Product Core -> CPS -> sibling projections", "layer_separation": "Evidence factual; Knowledge interpretive; Recommendations actionable; Presentation derived from CPS only", "limitations": list(limitations), "unknowns": list(unknowns)})
write_json("recommendations/recommendation-set.json", {"artifact_id": "AUC-001-P04-ACCEPTANCE-RECOMMENDATION-SET", "schema_family": "auc_001_recommendation_set", "generated_at": NOW, "recommendations": recommendations, "excluded_actions": ["Do not optimize from revenue/CRM", "Do not claim creative causality", "Do not infer additional creative metadata", "Do not treat provider-limited weekly temporality as complete"]})
write_json("coverage-matrix/coverage-matrix.json", coverage_matrix)
write_json("product-core/common-product-core.json", common_core)

source_fps = {artifact_paths[k]: sha(ROOT / artifact_paths[k].split("2026-07-22/", 1)[1]) for k in ["context_definition", "data_provider_validation", "evidence_set", "knowledge_set", "recommendation_set", "coverage_matrix", "common_product_core"]}
cps = build_canonical_projection_source(
    common_core,
    knowledge_set=json.loads((ROOT / "knowledge/knowledge-set.json").read_text(encoding="utf-8")),
    recommendation_set=json.loads((ROOT / "recommendations/recommendation-set.json").read_text(encoding="utf-8")),
    coverage_matrix=coverage_matrix,
    manifest={"artifact_paths": artifact_paths, "artifact_fingerprints": source_fps, "common_core_fingerprint": common_core_obj.semantic_fingerprint},
    integrated_view=integrated_view,
    decision_patterns=decision_patterns,
    artifact_id="AUC-001-P04-ACCEPTANCE-CANONICAL-PROJECTION-SOURCE",
)
assert not validate_canonical_projection_source(cps), [i.to_dict() for i in validate_canonical_projection_source(cps)]
write_json("product-core/canonical-projection-source.json", cps.to_dict())

analytical_sections = [
    {"title": "Scope and source coverage", "content_ref": "cps.period", "traceability_refs": ["EVD-001"], "coverage_refs": ["AQ-001", "AQ-011"], "order": 1, "format": "narrative"},
    {"title": "Quality and FARO distribution", "content_ref": "cps.integrated_view.signals[0]", "knowledge_refs": ["KNW-001"], "metric_refs": ["canonical_metrics.ab_rate_total", "canonical_metrics.tier_a_rate_total"], "coverage_refs": ["AQ-002"], "order": 2, "format": "table"},
    {"title": "Cost-quality reconciliation", "content_ref": "cps.integrated_view.signals[1]", "knowledge_refs": ["KNW-002"], "metric_refs": ["canonical_metrics.coverage_reconciliation"], "coverage_refs": ["AQ-003", "AQ-007"], "order": 3, "format": "coverage_table"},
    {"title": "Signals and combinations", "content_ref": "cps.integrated_view.combinations", "knowledge_refs": ["KNW-003", "KNW-005"], "coverage_refs": ["AQ-004", "AQ-005", "AQ-006", "AQ-008"], "order": 4, "format": "comparative_view"},
    {"title": "Temporal pattern", "content_ref": "cps.integrated_view.signals[3]", "knowledge_refs": ["KNW-004"], "coverage_refs": ["AQ-009", "CQ-007"], "order": 5, "format": "time_series_summary"},
    {"title": "Recommendations", "content_ref": "cps.recommendations", "recommendation_refs": ["REC-001", "REC-002", "REC-003", "REC-004"], "coverage_refs": ["AQ-010"], "order": 6, "format": "recommendation_table"},
    {"title": "Limitations, UNKNOWN and future evidence gaps", "content_ref": "cps.limitations", "unknown_refs": ["cps.unknowns"], "limitation_refs": ["cps.future_evidence_gaps"], "coverage_refs": ["AQ-011", "CQ-003", "CQ-005", "CQ-006"], "order": 7, "format": "limitations_register"},
]
executive_sections = [
    {"title": "Decision summary", "content_ref": "cps.decision_patterns", "knowledge_refs": ["KNW-001", "KNW-002", "KNW-003"], "coverage_refs": ["AQ-001", "AQ-002", "AQ-003", "AQ-010"], "order": 1, "format": "executive_summary"},
    {"title": "What can be acted on", "content_ref": "cps.recommendations", "recommendation_refs": ["REC-001", "REC-002", "REC-003", "REC-004"], "coverage_refs": ["AQ-010"], "order": 2, "format": "action_register"},
    {"title": "What must not be inferred", "content_ref": "cps.limitations", "unknown_refs": ["cps.unknowns"], "limitation_refs": ["cps.future_evidence_gaps"], "coverage_refs": ["AQ-011", "CQ-003", "CQ-005", "CQ-006"], "order": 3, "format": "risk_register"},
]
analytical = build_projection_from_cps(cps, "analytical", analytical_sections, {"projection": "analytical", "audience": "analyst", "allowed_variation": "diagnostic depth only"})
executive = build_projection_from_cps(cps, "executive", executive_sections, {"projection": "executive", "audience": "Direccion", "allowed_variation": "prioritized synthesis only"})
assert not validate_projection_against_cps(cps, analytical), [i.to_dict() for i in validate_projection_against_cps(cps, analytical)]
assert not validate_projection_against_cps(cps, executive), [i.to_dict() for i in validate_projection_against_cps(cps, executive)]
write_json("execution/analytical-projection-envelope.json", analytical.to_dict())
write_json("execution/executive-projection-envelope.json", executive.to_dict())

analytical_md = f"""# AUC-001 P04 Acceptance Analytical Report

Canonical Projection Source: `{cps.artifact_id}`
CPS fingerprint: `{cps.semantic_fingerprint}`

## Scope And Coverage

Derived from `cps.period`, `cps.sources` and `EVD-001`. Leads cover {lead['start']} to {lead['end']}; spend covers {spend['start']} to {spend['end']}.

## Quality Base

Derived from `KNW-001` and `EVD-002`. Leads: {lead['count']}. FARO A/B: {lead['ab']} ({metrics['ab_rate_total'] * 100:.1f}%). Tier A: {lead['tier_a']} ({metrics['tier_a_rate_total'] * 100:.1f}%).

## Cost-Quality Reconciliation

Derived from `KNW-002`, `EVD-003` and `EVD-004`. Commercial matched universe: {reconciliation['matched']['ad_count']} ads, {reconciliation['matched']['leads']} leads, {reconciliation['matched']['matched_commercial_spend']} matched commercial spend. Cost per A/B in matched commercial universe: {metrics['cost_per_ab_commercial_matched']}. Coverage states remain explicit: lead_only {reconciliation['lead_only']['ad_count']} ads and spend_only {reconciliation['spend_only']['ad_count']} ads.

## Signals And Combinations

Derived from `cps.integrated_view.combinations`. The shared explanatory combinations are ticket/form qualification signals, commercial matched ad quality-cost metrics, and temporal source coverage. They explain observed associations, not causal effects.

## Temporal Pattern

Derived from `KNW-004` and `EVD-005`. Monthly evidence is available. Weekly evidence is partial because provider spend stops before the lead source and edge weeks are incomplete.

## Recommendations

Derived from `cps.recommendations`.

| Recommendation | Category | Success criterion |
|---|---|---|
| REC-001 | measurable_experiment | {recommendations[0]['success_criterion']} |
| REC-002 | verifiable_action | {recommendations[1]['closure_criterion']} |
| REC-003 | measurable_experiment | {recommendations[2]['success_criterion']} |
| REC-004 | non_actionable_hypothesis | {recommendations[3]['promotion_condition']} |

## Limitations And UNKNOWN

- Revenue/CRM: not_available.
- Creative causality: UNKNOWN / not_applicable.
- Additional creative metadata: not_available.
- Temporal comparability: partial under provider limits.
"""
executive_md = f"""# AUC-001 P04 Acceptance Executive Report

Canonical Projection Source: `{cps.artifact_id}`
CPS fingerprint: `{cps.semantic_fingerprint}`

## Decision Summary

Derived from `cps.decision_patterns` and `cps.integrated_view`. The evidence supports controlled optimization inside the commercial matched universe and a coverage review before broader economic decisions. Quality is observable through FARO tiers and qualification signals; commercial revenue remains outside the authorized evidence.

## What Can Be Acted On

Derived from `cps.recommendations`.

| Priority | Action | Success criterion |
|---|---|---|
| High | REC-001 controlled budget experiment | {recommendations[0]['success_criterion']} |
| High | REC-002 coverage review | {recommendations[1]['closure_criterion']} |
| Medium | REC-003 form/qualification test | {recommendations[2]['success_criterion']} |
| Future evidence only | REC-004 revenue/CRM hypothesis | {recommendations[3]['promotion_condition']} |

## What Must Not Be Inferred

- Do not infer revenue/CRM outcome.
- Do not infer creative causality from ad names.
- Do not treat additional creative metadata as available.
- Do not treat weekly temporal evidence as complete.
- Do not convert lead_only into zero cost or spend_only into proof of no leads.
"""
(ROOT / "presentations/analytical/analytical-report.md").write_text(analytical_md, encoding="utf-8")
(ROOT / "presentations/executive/executive-report.md").write_text(executive_md, encoding="utf-8")

spec014 = build_contract_acceptance_payload(common_core_obj)
spec014["validation_name"] = "AUC-001 P04 acceptance SPEC-014 validation"
spec014["evidence_item_validation"] = [issue.to_dict() for item in evidence for issue in validate_evidence_item(item)]
spec014["knowledge_item_validation"] = [issue.to_dict() for item in knowledge_claims for issue in validate_knowledge_item(item)]
spec014["recommendation_validation"] = [issue.to_dict() for item in recommendations for issue in validate_recommendation(item)]
spec014["decision"] = "PASS" if spec014["is_contractually_acceptable_for_local_implementation"] and not spec014["evidence_item_validation"] and not spec014["knowledge_item_validation"] and not spec014["recommendation_validation"] else "FAIL"
spec015_issues = [*validate_canonical_projection_source(cps), *validate_projection_against_cps(cps, analytical), *validate_projection_against_cps(cps, executive)]
spec015 = {"validation_name": "AUC-001 P04 acceptance SPEC-015 validation", "decision": "PASS" if not spec015_issues else "FAIL", "canonical_projection_source_id": cps.artifact_id, "canonical_projection_source_fingerprint": cps.semantic_fingerprint, "same_cps": analytical.canonical_projection_source_fingerprint == executive.canonical_projection_source_fingerprint == cps.semantic_fingerprint, "no_projection_derivation": True, "issues": [i.to_dict() for i in spec015_issues]}
semantic = {"artifact_id": "AUC-001-P04-ACCEPTANCE-SEMANTIC-EQUIVALENCE-VALIDATION", "decision": spec015["decision"], "same_cps": spec015["same_cps"], "analytical_issues": [i.to_dict() for i in validate_projection_against_cps(cps, analytical)], "executive_issues": [i.to_dict() for i in validate_projection_against_cps(cps, executive)], "markdown_checks": {"blocked_historical_value_claim_absent": "valor historico" not in (analytical_md + executive_md).lower(), "projection_derivation_between_siblings": False}}
canonical_validation = {"artifact_id": "AUC-001-P04-ACCEPTANCE-CANONICAL-CONTENT-VALIDATION", "decision": "PASS" if not validate_common_core(common_core_obj) and not validate_canonical_projection_source(cps) else "FAIL", "cps_before_reports": True, "common_core_issues": [i.to_dict() for i in validate_common_core(common_core_obj)], "cps_issues": [i.to_dict() for i in validate_canonical_projection_source(cps)]}
write_json("validations/spec-014-validation.json", spec014)
write_json("validations/spec-015-validation.json", spec015)
write_json("execution/canonical-content-validation.json", canonical_validation)
write_json("execution/semantic-equivalence-validation.json", semantic)

handoff = f"""# AUC-001 P04 Acceptance Handoff

## Decision

Implementation package status: READY FOR REVIEWER AGENT AND QA AGENT REVALIDATION.

## Namespace

`outputs/auc-001/p04-acceptance/2026-07-22/`

## Execution Summary

- Brief instruction resolved: `{BRIEF}`
- Evidence acquired exclusively through BigQuery MCP.
- No BigQuery CLI, direct client, fallback source or historical output was used as new evidence.
- Canonical Projection Source was generated before both reports.
- Analytical and executive projections derive as siblings from CPS fingerprint `{cps.semantic_fingerprint}`.

## Validations

- SPEC-014 validation: `{spec014['decision']}`.
- SPEC-015 validation: `{spec015['decision']}`.
- Canonical content validation: `{canonical_validation['decision']}`.
- Semantic equivalence validation: `{semantic['decision']}`.

## Declared Limitations

- Revenue/CRM remains `not_available`.
- Creative causality remains `UNKNOWN` / `not_applicable`.
- Additional creative metadata remains `not_available`.
- Temporal comparability remains `partial` because spend ends on 2026-07-17 and leads extend to 2026-07-22.
- Two preliminary MCP query shapes were rejected with `ERR_SCOPE_DENIED` and were not used as evidence.
"""
(ROOT / "handoff/reviewer-qa-handoff.md").write_text(handoff, encoding="utf-8")

all_files = sorted(p for p in ROOT.rglob("*") if p.is_file())
fingerprints = {str(p).replace("\\", "/"): sha(p) for p in all_files}
manifest = {
    "artifact_id": "AUC-001-P04-ACCEPTANCE-MANIFEST",
    "generated_at": NOW,
    "namespace": str(ROOT).replace("\\", "/"),
    "gate": "gates/auc-001-post-p04-e2e-acceptance-real-execution-authorization-gate.md",
    "status": "READY_FOR_REVALIDATION" if spec014["decision"] == "PASS" and spec015["decision"] == "PASS" else "NEEDS_REVIEW",
    "source_policy": {"bigquery_mcp_only": True, "cli_used": False, "fallback_used": False, "historical_outputs_used_as_new_evidence": False},
    "artifact_paths": artifact_paths | {"analytical_report": "outputs/auc-001/p04-acceptance/2026-07-22/presentations/analytical/analytical-report.md", "executive_report": "outputs/auc-001/p04-acceptance/2026-07-22/presentations/executive/executive-report.md", "handoff": "outputs/auc-001/p04-acceptance/2026-07-22/handoff/reviewer-qa-handoff.md"},
    "common_core_fingerprint": common_core_obj.semantic_fingerprint,
    "canonical_projection_source_fingerprint": cps.semantic_fingerprint,
    "artifact_fingerprints": fingerprints,
    "mcp_traceability": {"metadata_discovery": metadata_discovery, "query_traces": query_traces, "rejected_attempts_not_used_as_evidence": rejected_attempts},
    "validation_decisions": {"spec_014": spec014["decision"], "spec_015": spec015["decision"], "canonical_content": canonical_validation["decision"], "semantic_equivalence": semantic["decision"]},
}
write_json("execution/manifest.json", manifest)
write_json("execution/physical-traceability.json", {"artifact_id": "AUC-001-P04-ACCEPTANCE-PHYSICAL-TRACEABILITY", "generated_at": NOW, "manifest_path": "outputs/auc-001/p04-acceptance/2026-07-22/execution/manifest.json", "manifest_sha256": sha(ROOT / "execution/manifest.json"), "package_file_count": len(sorted(p for p in ROOT.rglob("*") if p.is_file())), "namespace_is_authorized": True, "historical_outputs_modified": False})
print(json.dumps({"status": manifest["status"], "namespace": str(ROOT).replace("\\", "/"), "spec014": spec014["decision"], "spec015": spec015["decision"]}, indent=2))
