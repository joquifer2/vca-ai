$ErrorActionPreference = "Stop"

function Invoke-PythonCheck {
    param([string]$Code)
    $Code | python -
    if ($LASTEXITCODE -ne 0) {
        throw "Python check failed with exit code $LASTEXITCODE"
    }
}

Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import (
    COMPARISON_ECONOMIC_EFFICIENCY_CLAIM,
    COMPARISON_DESCRIPTIVE_CONTRAST,
    COMPARISON_GOVERNANCE_ALLOWED,
    COMPARISON_GOVERNANCE_PRESENTATION_RESTRICTED,
    validate_comparison_classification,
)

claim = {
    "comparison_id": "CMP-UNKNOWN-ECONOMIC",
    "source_artifact": "analytical_reasoning",
    "compared_universes": [
        {"universe_id": "u1", "universe_label": "Meta spend universe", "strategic_equivalence": "unknown"},
        {"universe_id": "u2", "universe_label": "FARO quality universe", "strategic_equivalence": "equivalent"},
    ],
    "comparison_type": [COMPARISON_DESCRIPTIVE_CONTRAST, COMPARISON_ECONOMIC_EFFICIENCY_CLAIM],
    "governance_status": COMPARISON_GOVERNANCE_ALLOWED,
    "allowed_projection_behavior": {"analytical": "preserve_full_context", "executive": "downgrade_to_descriptive"},
}
issues = validate_comparison_classification(claim)
assert any(issue.code == "COMPARISON_GOVERNANCE_TOO_WEAK" for issue in issues), [issue.to_dict() for issue in issues]

claim["governance_status"] = COMPARISON_GOVERNANCE_PRESENTATION_RESTRICTED
claim["required_limitation_or_disclaimer_semantics"] = "Universe equivalence is unknown; presentation must not state economic superiority."
claim["allowed_projection_behavior"] = {"analytical": "preserve_with_limitation", "executive": "downgrade_to_descriptive"}
issues = validate_comparison_classification(claim)
assert not issues, [issue.to_dict() for issue in issues]
"@

Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import (
    COMPARISON_CAUSAL_OR_OPTIMIZATION_CLAIM,
    COMPARISON_GOVERNANCE_BLOCKED,
    validate_comparison_classification,
)

claim = {
    "comparison_id": "CMP-BLOCKED-CAUSAL",
    "source_artifact": "analytical_reasoning",
    "compared_universes": [
        {"universe_id": "lead_only", "universe_label": "Lead-only universe", "strategic_equivalence": "non_equivalent"},
        {"universe_id": "cost_quality", "universe_label": "Cost-quality universe", "strategic_equivalence": "equivalent"},
    ],
    "comparison_type": [COMPARISON_CAUSAL_OR_OPTIMIZATION_CLAIM],
    "governance_status": COMPARISON_GOVERNANCE_BLOCKED,
    "allowed_projection_behavior": {"analytical": "preserve_with_limitation", "executive": "suppress_claim"},
}
issues = validate_comparison_classification(claim)
assert any(issue.code == "COMPARISON_BLOCKED_BEHAVIOR_INVALID" for issue in issues), [issue.to_dict() for issue in issues]

claim["allowed_projection_behavior"] = {"analytical": "suppress_claim", "executive": "suppress_claim"}
issues = validate_comparison_classification(claim)
assert not issues, [issue.to_dict() for issue in issues]
"@

Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import validate_recommendation_comparison_refs

comparison_index = {
    "CMP-BLOCKED": {"comparison_id": "CMP-BLOCKED", "governance_status": "blocked"},
    "CMP-ALLOWED": {"comparison_id": "CMP-ALLOWED", "governance_status": "allowed_with_limitation"},
}
issues = validate_recommendation_comparison_refs({"recommendation_id": "REC-1", "comparison_refs": ["CMP-BLOCKED"]}, comparison_index)
assert any(issue.code == "RECOMMENDATION_BLOCKED_COMPARISON" for issue in issues), [issue.to_dict() for issue in issues]

issues = validate_recommendation_comparison_refs({"recommendation_id": "REC-2", "comparison_refs": ["CMP-ALLOWED"]}, comparison_index)
assert not issues, [issue.to_dict() for issue in issues]
"@

Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import (
    QUESTION_DEFINITIONS,
    build_canonical_projection_source,
    build_projection_from_cps,
    validate_projection_against_cps,
)

comparison = {
    "comparison_id": "CMP-TRANSPORT",
    "source_artifact": "analytical_reasoning",
    "compared_universes": [
        {"universe_id": "campaign_volume", "universe_label": "Campaign volume", "strategic_equivalence": "equivalent"},
        {"universe_id": "campaign_quality", "universe_label": "Campaign quality", "strategic_equivalence": "equivalent"},
    ],
    "comparison_type": ["descriptive_contrast"],
    "governance_status": "allowed",
    "allowed_projection_behavior": {"analytical": "preserve_full_context", "executive": "simplify_with_limitation"},
}
common_core = {
    "artifact_id": "AUC-001-EXP-CPC",
    "period": {"from": "2026-01-01", "to": "2026-01-31"},
    "scope": {"use_case": "AUC-001"},
    "sources": ["synthetic-fixture"],
    "evidence_refs": ["EVID-SYNTH"],
    "canonical_metrics": {"lead_count": 10},
    "coverage_states": {definition.question_id: "not_applicable" for definition in QUESTION_DEFINITIONS},
    "knowledge_claims": [],
    "recommendations": [],
    "limitations": ["synthetic fixture"],
    "unknowns": ["none for transport test"],
    "comparison_classifications": [comparison],
}
cps = build_canonical_projection_source(common_core, knowledge_set={"knowledge_claims": []}, recommendation_set={"recommendations": []})
assert cps.comparison_classifications == (comparison,)
projection = build_projection_from_cps(cps, "executive", sections=[{"title": "Comparison", "comparison_refs": ["CMP-TRANSPORT"], "display_role": "descriptive"}])
assert projection.comparison_classifications == (comparison,)
issues = validate_projection_against_cps(cps, projection)
assert not issues, [issue.to_dict() for issue in issues]

mutated = projection.to_dict()
mutated["comparison_classifications"] = []
issues = validate_projection_against_cps(cps, mutated)
assert any(issue.code == "PROJECTION_COMPARISON_CLASSIFICATION_DIVERGENCE" for issue in issues), [issue.to_dict() for issue in issues]
"@

Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import (
    QUESTION_DEFINITIONS,
    build_canonical_projection_source,
    build_projection_from_cps,
    validate_projection_against_cps,
)

blocked_comparison = {
    "comparison_id": "CMP-BLOCKED-PRESENTATION",
    "source_artifact": "analytical_reasoning",
    "compared_universes": [
        {"universe_id": "u1", "universe_label": "Universe 1", "strategic_equivalence": "non_equivalent"},
        {"universe_id": "u2", "universe_label": "Universe 2", "strategic_equivalence": "equivalent"},
    ],
    "comparison_type": ["causal_or_optimization_claim"],
    "governance_status": "blocked",
    "allowed_projection_behavior": {"analytical": "suppress_claim", "executive": "suppress_claim"},
}
common_core = {
    "artifact_id": "AUC-001-EXP-CPC",
    "period": {"from": "2026-01-01", "to": "2026-01-31"},
    "scope": {"use_case": "AUC-001"},
    "sources": ["synthetic-fixture"],
    "evidence_refs": ["EVID-SYNTH"],
    "canonical_metrics": {"lead_count": 10},
    "coverage_states": {definition.question_id: "not_applicable" for definition in QUESTION_DEFINITIONS},
    "knowledge_claims": [],
    "recommendations": [],
    "limitations": ["synthetic fixture"],
    "unknowns": ["none for blocked presentation test"],
    "comparison_classifications": [blocked_comparison],
}
cps = build_canonical_projection_source(common_core, knowledge_set={"knowledge_claims": []}, recommendation_set={"recommendations": []})
projection = build_projection_from_cps(cps, "analytical", sections=[{"title": "Blocked claim", "comparison_refs": ["CMP-BLOCKED-PRESENTATION"], "display_role": "claim"}])
issues = validate_projection_against_cps(cps, projection)
assert any(issue.code == "PROJECTION_BLOCKED_COMPARISON_PRESENTED" for issue in issues), [issue.to_dict() for issue in issues]
"@



Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import validate_comparison_classification

claim = {
    "comparison_id": "CMP-MATERIAL-NOT-RECONCILED",
    "source_artifact": "knowledge_set",
    "provisional_claim_ref": {"type": "textual_excerpt", "value": "provisional", "status": "provisional_until_knowledge_stabilization"},
    "stabilized_claim_refs": {"knowledge_refs": [], "recommendation_refs": [], "reconciliation_status": "not_applicable"},
    "compared_universes": [
        {"universe_id": "u1", "universe_label": "Universe 1", "strategic_equivalence": "equivalent"},
        {"universe_id": "u2", "universe_label": "Universe 2", "strategic_equivalence": "equivalent"},
    ],
    "comparison_type": ["descriptive_contrast"],
    "governance_status": "allowed",
    "allowed_projection_behavior": {"analytical": "preserve_full_context", "executive": "simplify_with_limitation"},
}
issues = validate_comparison_classification(claim, knowledge_set_stabilized=True, knowledge_items=[{"knowledge_id": "K-1"}])
assert any(issue.code == "COMPARISON_RECONCILIATION_REQUIRED" for issue in issues), [issue.to_dict() for issue in issues]
assert any(issue.code == "COMPARISON_KNOWLEDGE_REFS_REQUIRED" for issue in issues), [issue.to_dict() for issue in issues]
"@

Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import validate_comparison_classification

claim = {
    "comparison_id": "CMP-UNRESOLVED-KNOWLEDGE-REF",
    "source_artifact": "knowledge_set",
    "provisional_claim_ref": {"type": "textual_excerpt", "value": "provisional", "status": "provisional_until_knowledge_stabilization"},
    "stabilized_claim_refs": {"knowledge_refs": ["K-MISSING"], "recommendation_refs": [], "reconciliation_status": "reconciled"},
    "compared_universes": [
        {"universe_id": "u1", "universe_label": "Universe 1", "strategic_equivalence": "equivalent"},
        {"universe_id": "u2", "universe_label": "Universe 2", "strategic_equivalence": "equivalent"},
    ],
    "comparison_type": ["descriptive_contrast"],
    "governance_status": "allowed",
    "allowed_projection_behavior": {"analytical": "preserve_full_context", "executive": "simplify_with_limitation"},
}
issues = validate_comparison_classification(claim, knowledge_set_stabilized=True, knowledge_items=[{"knowledge_id": "K-1"}])
assert any(issue.code == "COMPARISON_KNOWLEDGE_REF_UNRESOLVED" for issue in issues), [issue.to_dict() for issue in issues]
"@

Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import validate_comparison_classification

claim = {
    "comparison_id": "CMP-STILL-PROVISIONAL",
    "source_artifact": "analytical_reasoning",
    "provisional_claim_ref": {"type": "textual_excerpt", "value": "provisional", "status": "provisional_until_knowledge_stabilization"},
    "stabilized_claim_refs": {"knowledge_refs": [], "recommendation_refs": [], "reconciliation_status": "pending"},
    "compared_universes": [
        {"universe_id": "u1", "universe_label": "Universe 1", "strategic_equivalence": "equivalent"},
        {"universe_id": "u2", "universe_label": "Universe 2", "strategic_equivalence": "equivalent"},
    ],
    "comparison_type": ["descriptive_contrast"],
    "governance_status": "allowed",
    "allowed_projection_behavior": {"analytical": "preserve_full_context", "executive": "simplify_with_limitation"},
}
issues = validate_comparison_classification(claim, knowledge_set_stabilized=False)
assert not issues, [issue.to_dict() for issue in issues]
"@

Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import validate_recommendation_comparison_refs

unknown_economic = {
    "comparison_id": "CMP-UNKNOWN-ECONOMIC-REC",
    "governance_status": "presentation_restricted",
    "comparison_type": ["economic_efficiency_claim"],
    "compared_universes": [
        {"universe_id": "u1", "universe_label": "Universe 1", "strategic_equivalence": "unknown"},
        {"universe_id": "u2", "universe_label": "Universe 2", "strategic_equivalence": "equivalent"},
    ],
}
recommendation = {
    "recommendation_id": "REC-UNKNOWN-BUDGET",
    "category": "verifiable_action",
    "comparison_refs": ["CMP-UNKNOWN-ECONOMIC-REC"],
    "action": "Increase budget because this universe shows mayor eficiencia economica",
}
issues = validate_recommendation_comparison_refs(recommendation, {"CMP-UNKNOWN-ECONOMIC-REC": unknown_economic})
assert any(issue.code == "RECOMMENDATION_UNKNOWN_COMPARISON_CONCLUSIVE" for issue in issues), [issue.to_dict() for issue in issues]
"@

Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import validate_recommendation_comparison_refs

unknown_hierarchy = {
    "comparison_id": "CMP-UNKNOWN-HIERARCHY-REC",
    "governance_status": "allowed_with_limitation",
    "comparison_type": ["strategic_hierarchy_claim"],
    "compared_universes": [
        {"universe_id": "u1", "universe_label": "Universe 1", "strategic_equivalence": "unknown"},
        {"universe_id": "u2", "universe_label": "Universe 2", "strategic_equivalence": "equivalent"},
    ],
}
recommendation = {
    "recommendation_id": "REC-UNKNOWN-PRIORITY",
    "category": "verifiable_action",
    "comparison_refs": ["CMP-UNKNOWN-HIERARCHY-REC"],
    "action": "Priorizar estrategicamente Universe 1 over Universe 2",
}
issues = validate_recommendation_comparison_refs(recommendation, {"CMP-UNKNOWN-HIERARCHY-REC": unknown_hierarchy})
assert any(issue.code == "RECOMMENDATION_UNKNOWN_COMPARISON_CONCLUSIVE" for issue in issues), [issue.to_dict() for issue in issues]
"@

Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import validate_recommendation_comparison_refs

unknown_economic = {
    "comparison_id": "CMP-UNKNOWN-HYPOTHESIS",
    "governance_status": "presentation_restricted",
    "comparison_type": ["economic_efficiency_claim"],
    "compared_universes": [
        {"universe_id": "u1", "universe_label": "Universe 1", "strategic_equivalence": "unknown"},
        {"universe_id": "u2", "universe_label": "Universe 2", "strategic_equivalence": "equivalent"},
    ],
}
recommendation = {
    "recommendation_id": "REC-NON-ACTIONABLE-UNKNOWN",
    "category": "non_actionable_hypothesis",
    "comparison_refs": ["CMP-UNKNOWN-HYPOTHESIS"],
    "hypothesis": "Hypothesis to resolve unknown equivalence before any economic decision",
    "uncertainty": "equivalence unknown",
}
issues = validate_recommendation_comparison_refs(recommendation, {"CMP-UNKNOWN-HYPOTHESIS": unknown_economic})
assert not issues, [issue.to_dict() for issue in issues]
"@

Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import validate_recommendation_comparison_refs

unknown_economic = {
    "comparison_id": "CMP-UNKNOWN-EXPERIMENT",
    "governance_status": "presentation_restricted",
    "comparison_type": ["economic_efficiency_claim"],
    "compared_universes": [
        {"universe_id": "u1", "universe_label": "Universe 1", "strategic_equivalence": "unknown"},
        {"universe_id": "u2", "universe_label": "Universe 2", "strategic_equivalence": "equivalent"},
    ],
}
recommendation = {
    "recommendation_id": "REC-MEASURABLE-UNKNOWN",
    "category": "measurable_experiment",
    "comparison_refs": ["CMP-UNKNOWN-EXPERIMENT"],
    "hypothesis": "Run an experiment to validate equivalence and resolve uncertainty",
    "action": "Measure evidence before optimization",
    "evidence_dependency": "new evidence required",
}
issues = validate_recommendation_comparison_refs(recommendation, {"CMP-UNKNOWN-EXPERIMENT": unknown_economic})
assert not issues, [issue.to_dict() for issue in issues]
"@

Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import validate_recommendation_comparison_refs

equivalent = {
    "comparison_id": "CMP-EQUIVALENT-VALID",
    "governance_status": "allowed",
    "comparison_type": ["economic_efficiency_claim"],
    "compared_universes": [
        {"universe_id": "u1", "universe_label": "Universe 1", "strategic_equivalence": "equivalent"},
        {"universe_id": "u2", "universe_label": "Universe 2", "strategic_equivalence": "equivalent"},
    ],
}
recommendation = {
    "recommendation_id": "REC-EQUIVALENT-VALID",
    "category": "verifiable_action",
    "comparison_refs": ["CMP-EQUIVALENT-VALID"],
    "action": "Execute a verifiable action from equivalent governed comparison",
}
issues = validate_recommendation_comparison_refs(recommendation, {"CMP-EQUIVALENT-VALID": equivalent})
assert not issues, [issue.to_dict() for issue in issues]
"@



Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import validate_comparison_classification

claim = {
    "comparison_id": "CMP-REF-AGAINST-EMPTY-KS",
    "source_artifact": "knowledge_set",
    "provisional_claim_ref": {"type": "textual_excerpt", "value": "x", "status": "provisional_until_knowledge_stabilization"},
    "stabilized_claim_refs": {"knowledge_refs": ["K-MISSING"], "recommendation_refs": [], "reconciliation_status": "reconciled"},
    "compared_universes": [
        {"universe_id": "u1", "universe_label": "Universe 1", "strategic_equivalence": "equivalent"},
        {"universe_id": "u2", "universe_label": "Universe 2", "strategic_equivalence": "equivalent"},
    ],
    "comparison_type": ["descriptive_contrast"],
    "governance_status": "allowed",
    "allowed_projection_behavior": {"analytical": "preserve_full_context", "executive": "simplify_with_limitation"},
}
issues = validate_comparison_classification(claim, knowledge_set_stabilized=True, knowledge_items=[])
assert any(issue.code == "COMPARISON_KNOWLEDGE_REF_UNRESOLVED" for issue in issues), [issue.to_dict() for issue in issues]
"@

Invoke-PythonCheck @"
from tools.auc_001_analytical_product_contract import validate_recommendation_comparison_refs

classification = {
    "comparison_id": "CMP-UNKNOWN-REDISTRIBUIR-PRESUPUESTO",
    "governance_status": "presentation_restricted",
    "comparison_type": ["economic_efficiency_claim"],
    "compared_universes": [
        {"universe_id": "u1", "universe_label": "Universe 1", "strategic_equivalence": "unknown"},
        {"universe_id": "u2", "universe_label": "Universe 2", "strategic_equivalence": "equivalent"},
    ],
}
recommendation = {
    "recommendation_id": "REC-REDISTRIBUIR-PRESUPUESTO",
    "category": "verifiable_action",
    "comparison_refs": ["CMP-UNKNOWN-REDISTRIBUIR-PRESUPUESTO"],
    "action": "Redistribuir presupuesto hacia Universe 1 por mejor eficiencia",
}
issues = validate_recommendation_comparison_refs(recommendation, {classification["comparison_id"]: classification})
assert any(issue.code == "RECOMMENDATION_UNKNOWN_COMPARISON_CONCLUSIVE" for issue in issues), [issue.to_dict() for issue in issues]
"@

Write-Host "All AUC-001 comparison governance experiment tests passed"