$ErrorActionPreference = 'Stop'

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot '..\..')
Set-Location $RepoRoot

$Results = New-Object System.Collections.Generic.List[object]

function Add-Result {
    param([string]$Name, [string]$Status, [string]$Evidence, [string]$Details = '')
    $Results.Add([pscustomobject]@{ Name = $Name; Status = $Status; Evidence = $Evidence; Details = $Details }) | Out-Null
}

function Invoke-PythonCheck {
    param([string]$Name, [string]$Code)
    $output = $Code | python -
    if ($LASTEXITCODE -eq 0) { Add-Result $Name 'PASS' 'tools/auc_001_analytical_product_contract.py' $output }
    else { Add-Result $Name 'FAIL' 'tools/auc_001_analytical_product_contract.py' $output }
}

$contractSchemaCode = @"
from tools.auc_001_analytical_product_contract import (
    build_analytical_product_contract,
    COVERAGE_UNKNOWN,
    COVERAGE_NOT_AVAILABLE,
    RECOMMENDATION_MEASURABLE_EXPERIMENT,
)

contract = build_analytical_product_contract()
payload = contract.to_dict()
question_ids = [row['question_id'] for row in payload['coverage_matrix']]
assert payload['contract_id'] == 'AUC-001-ANALYTICAL-PRODUCT-CONTRACT'
assert payload['schema_family'] == 'auc_001_analytical_product_contract'
assert payload['schema_version'] == 'auc_001_analytical_product_contract.v1'
assert payload['specification'] == 'SPEC-014'
assert len([qid for qid in question_ids if qid.startswith('AQ-')]) == 11
assert len([qid for qid in question_ids if qid.startswith('CQ-')]) == 7
assert len([qid for qid in question_ids if qid.startswith('NAQ-')]) == 5
assert COVERAGE_UNKNOWN in payload['coverage_states']
assert COVERAGE_NOT_AVAILABLE in payload['coverage_states']
assert RECOMMENDATION_MEASURABLE_EXPERIMENT in payload['recommendation_categories']
assert 'ad_creative' in payload['required_views']
print('SPEC-014 contract schema, taxonomy, states and categories passed')
"@
Invoke-PythonCheck 'P02 contract schema and taxonomy' $contractSchemaCode

$completeMatrixCode = @"
from tools.auc_001_analytical_product_contract import (
    QUESTION_DEFINITIONS,
    CoverageMatrixRow,
    RobustnessRecord,
    COVERAGE_COMPLETE,
    COVERAGE_NOT_APPLICABLE,
    validate_coverage_matrix,
)

def depth(qid):
    return {
        'evidence': f'{qid} observed evidence',
        'comparison': f'{qid} relevant comparison',
        'interpretation': f'{qid} separated interpretation',
        'business_implication': f'{qid} business implication',
        'limitation_or_uncertainty': f'{qid} limitation',
        'conclusion_or_hypothesis': f'{qid} conclusion',
        'traceability': [f'EVD-{qid}'],
    }

def robustness():
    return RobustnessRecord(
        denominator=100,
        observed_volume=100,
        coverage='matched',
        granularity='question',
        comparator='period baseline',
        sample_sufficiency='sufficient',
    )

rows = []
for definition in QUESTION_DEFINITIONS:
    if definition.taxonomy == 'not_applicable':
        rows.append(CoverageMatrixRow(definition.question_id, COVERAGE_NOT_APPLICABLE, 'outside SPEC-014 product boundary'))
    elif definition.taxonomy == 'conditional':
        rows.append(CoverageMatrixRow(definition.question_id, COVERAGE_NOT_APPLICABLE, 'condition does not apply in this execution'))
    else:
        rows.append(CoverageMatrixRow(definition.question_id, COVERAGE_COMPLETE, 'answered with required depth', (f'EVD-{definition.question_id}',), depth(definition.question_id), robustness()))
issues = validate_coverage_matrix(rows)
assert issues == [], [issue.to_dict() for issue in issues]
print('complete matrix validates every AQ/CQ/NAQ row by question and state')
"@
Invoke-PythonCheck 'Coverage matrix complete by question' $completeMatrixCode

$depthNegativeCode = @"
from tools.auc_001_analytical_product_contract import CoverageMatrixRow, RobustnessRecord, COVERAGE_COMPLETE, validate_coverage_row

row = CoverageMatrixRow(
    'AQ-001',
    COVERAGE_COMPLETE,
    'table exists but depth is missing',
    ('table-volume',),
    {'evidence': 'a table was present'},
    RobustnessRecord(denominator=10, observed_volume=10, coverage='matched', granularity='month', comparator='previous month', sample_sufficiency='sufficient'),
)
issues = validate_coverage_row(row)
assert any(issue.code == 'MISSING_DEPTH_FIELD' for issue in issues)
print('formal table presence alone cannot complete mandatory depth')
"@
Invoke-PythonCheck 'Mandatory depth rejects table-only completion' $depthNegativeCode

$coverageStateCode = @"
from tools.auc_001_analytical_product_contract import (
    CoverageMatrixRow,
    COVERAGE_NOT_AVAILABLE,
    COVERAGE_UNKNOWN,
    validate_coverage_row,
    assess_ad_name_applicability,
)

ad_name_absent = assess_ad_name_applicability(has_ad_id_norm=True, has_ad_metrics=True, has_ad_name=False)
assert ad_name_absent['coverage_state'] == COVERAGE_NOT_AVAILABLE
assert ad_name_absent['ad_name_is_blocking_by_itself'] is False
row = CoverageMatrixRow('AQ-005', COVERAGE_NOT_AVAILABLE, 'ad_name label unavailable', impact='executive readability degrades, ad_id_norm remains usable')
assert validate_coverage_row(row) == []
critical_absence = CoverageMatrixRow('AQ-002', COVERAGE_NOT_AVAILABLE, 'tier distribution missing', impact='quality cannot be answered')
issues = validate_coverage_row(critical_absence)
assert any(issue.code in {'STATE_NOT_ALLOWED_FOR_QUESTION', 'MANDATORY_HIGH_NOT_AVAILABLE'} for issue in issues)
unknown_row = CoverageMatrixRow('AQ-005', COVERAGE_UNKNOWN, 'metrics exist but value/waste cannot be concluded', depth={'limitation_or_uncertainty': 'sample too low to conclude'})
assert validate_coverage_row(unknown_row) == []
print('not_available and UNKNOWN remain distinct; ad_name absence alone is not blocking')
"@
Invoke-PythonCheck 'Coverage state semantics and ad_name rule' $coverageStateCode

$robustnessCode = @"
from tools.auc_001_analytical_product_contract import RobustnessRecord, validate_robustness_record

missing = validate_robustness_record({'denominator': 10, 'observed_volume': 10})
assert any(issue.code == 'MISSING_ROBUSTNESS_FIELD' for issue in missing)
low = validate_robustness_record(RobustnessRecord(denominator=2, observed_volume=2, coverage='matched', granularity='ad', comparator='peer ads', sample_sufficiency='low_sample'))
assert any(issue.code == 'LOW_SAMPLE_REQUIRES_DEGRADATION' and issue.severity == 'warning' for issue in low)
complete = validate_robustness_record(RobustnessRecord(denominator=30, observed_volume=30, coverage='matched', granularity='ad', comparator='peer ads', sample_sufficiency='sufficient'))
assert complete == []
print('robustness fields and low-sample degradation signal passed')
"@
Invoke-PythonCheck 'Robustness and sample sufficiency guards' $robustnessCode

$layerSeparationCode = @"
from tools.auc_001_analytical_product_contract import validate_evidence_item, validate_knowledge_item

valid_evidence = {'evidence_id': 'EVD-001', 'facts': {'leads': 10}, 'coverage_state': 'complete', 'traceability': ['runtime-output.json']}
assert validate_evidence_item(valid_evidence) == []
invalid_evidence = dict(valid_evidence, opportunity='optimize this')
assert any(issue.code == 'EVIDENCE_CONTAINS_INTERPRETATION' for issue in validate_evidence_item(invalid_evidence))
valid_knowledge = {'knowledge_id': 'KNW-001', 'evidence_refs': ['EVD-001'], 'interpretation': 'quality is concentrated', 'limitation_or_uncertainty': 'sample limited'}
assert validate_knowledge_item(valid_knowledge) == []
invalid_knowledge = dict(valid_knowledge, recommendation='increase budget')
assert any(issue.code == 'KNOWLEDGE_FIELD_PROHIBITED' for issue in validate_knowledge_item(invalid_knowledge))
print('Evidence remains factual and Knowledge remains recommendation-free')
"@
Invoke-PythonCheck 'Evidence and Knowledge separation' $layerSeparationCode

$recommendationsCode = @"
from tools.auc_001_analytical_product_contract import (
    validate_recommendation,
    RECOMMENDATION_MEASURABLE_EXPERIMENT,
    RECOMMENDATION_VERIFIABLE_ACTION,
    RECOMMENDATION_NON_ACTIONABLE_HYPOTHESIS,
)

experiment = {
    'category': RECOMMENDATION_MEASURABLE_EXPERIMENT,
    'knowledge_refs': ['KNW-001'],
    'hypothesis': 'Ad group A may improve A/B rate',
    'action': 'Run controlled budget test',
    'population': 'matched ads',
    'primary_metric': 'A/B rate',
    'guardrail': 'cost per A/B does not worsen',
    'expected_direction': 'increase',
    'success_criterion': 'material lift with stable cost',
    'validation_window': 'two complete weeks',
    'evidence_dependency': 'EVD-001',
    'uncertainty': 'observational evidence only',
    'stop_or_review_condition': 'low sample or cost degradation',
}
assert validate_recommendation(experiment) == []
weak_experiment = dict(experiment)
weak_experiment.pop('primary_metric')
assert any(issue.code == 'RECOMMENDATION_MISSING_FIELD' for issue in validate_recommendation(weak_experiment))
action = {
    'category': RECOMMENDATION_VERIFIABLE_ACTION,
    'knowledge_refs': ['KNW-002'],
    'action': 'Review naming coverage',
    'supporting_evidence': 'ad_name missingness',
    'verifiable_result': 'coverage register updated',
    'closure_criterion': 'all missing labels classified',
    'risk': 'manual process drift',
    'dependency': 'authorized metadata source',
}
assert validate_recommendation(action) == []
hypothesis = {
    'category': RECOMMENDATION_NON_ACTIONABLE_HYPOTHESIS,
    'knowledge_refs': ['KNW-003'],
    'hypothesis': 'post-lead status may explain quality',
    'support': 'FARO variation observed',
    'uncertainty': 'CRM source absent',
    'missing_evidence': 'authorized ticket_status',
    'promotion_condition': 'source becomes authorized and reconciled',
}
assert validate_recommendation(hypothesis) == []
print('recommendations require measurable experiments, verifiable actions, or non-actionable hypotheses')
"@
Invoke-PythonCheck 'Recommendation category validation' $recommendationsCode

$projectionCode = @"
from tools.auc_001_analytical_product_contract import (
    QUESTION_DEFINITIONS,
    CoverageMatrixRow,
    RobustnessRecord,
    CommonProductCore,
    COVERAGE_COMPLETE,
    COVERAGE_NOT_APPLICABLE,
    build_projection,
    validate_projection_equivalence,
    build_contract_acceptance_payload,
)

def depth(qid):
    return {
        'evidence': 'observed',
        'comparison': 'baseline',
        'interpretation': 'meaning',
        'business_implication': 'decision relevance',
        'limitation_or_uncertainty': 'declared limit',
        'conclusion_or_hypothesis': 'supported conclusion',
        'traceability': ['EVD-001'],
    }
robustness = RobustnessRecord(denominator=100, observed_volume=100, coverage='matched', granularity='question', comparator='baseline', sample_sufficiency='sufficient')
rows = []
for definition in QUESTION_DEFINITIONS:
    if definition.taxonomy == 'mandatory':
        rows.append(CoverageMatrixRow(definition.question_id, COVERAGE_COMPLETE, 'answered', ('EVD-001',), depth(definition.question_id), robustness))
    else:
        rows.append(CoverageMatrixRow(definition.question_id, COVERAGE_NOT_APPLICABLE, 'outside current execution boundary'))
recommendation = {
    'category': 'verifiable_action',
    'knowledge_refs': ['KNW-001'],
    'action': 'Review tracking coverage',
    'supporting_evidence': 'coverage limitation',
    'verifiable_result': 'coverage register updated',
    'closure_criterion': 'missingness classified',
    'risk': 'manual drift',
    'dependency': 'authorized source',
}
core = CommonProductCore(
    period={'start': '2026-06-01', 'end': '2026-06-30'},
    scope={'use_case': 'AUC-001'},
    sources=('marts.fct_lead_enriched', 'marts.fct_spend'),
    evidence_refs=('EVD-001',),
    canonical_metrics={'matched_leads': 100},
    coverage_matrix=tuple(rows),
    knowledge_claims=({'knowledge_id': 'KNW-001', 'evidence_refs': ['EVD-001'], 'interpretation': 'coverage limit matters', 'limitation_or_uncertainty': 'partial source'},),
    recommendations=(recommendation,),
    limitations=('partial coverage remains visible',),
    unknowns=('creative causality UNKNOWN',),
)
analytical = build_projection(core, 'analytical', sections=({'title': 'matrix'},))
executive = build_projection(core, 'executive', sections=({'title': 'decision summary'},))
assert validate_projection_equivalence(core, analytical) == []
assert validate_projection_equivalence(core, executive) == []
tampered = executive.to_dict()
tampered['coverage_states']['AQ-001'] = 'partial'
assert any(issue.code == 'PROJECTION_COVERAGE_DIVERGENCE' for issue in validate_projection_equivalence(core, tampered))
acceptance = build_contract_acceptance_payload(core)
assert acceptance['is_product_contract_acceptance_envelope'] is True
assert acceptance['is_complete_global_boolean'] is None
assert acceptance['completion_is_by_question_and_criticality'] is True
assert acceptance['is_contractually_acceptable_for_local_implementation'] is True
print('common core, projections and acceptance envelope passed')
"@
Invoke-PythonCheck 'Common core and projection equivalence' $projectionCode

$gapRulesCode = @"
from tools.auc_001_analytical_product_contract import assess_ticket_status_applicability, assess_temporal_comparability

no_ticket = assess_ticket_status_applicability(source_authorized=False, coverage_sufficient=False)
assert no_ticket['coverage_state'] == 'not_available'
assert no_ticket['may_impute_from_faro'] is False
partial_ticket = assess_ticket_status_applicability(source_authorized=True, coverage_sufficient=False)
assert partial_ticket['coverage_state'] == 'partial'
monthly_only = assess_temporal_comparability(has_monthly_series=True, has_complete_weeks=False, has_partial_week_rule=False)
assert monthly_only['coverage_state'] == 'partial'
assert monthly_only['minimum_temporal_basis'] == 'monthly'
assert monthly_only['weekly_view_applicable'] is False
weekly = assess_temporal_comparability(has_monthly_series=True, has_complete_weeks=True, has_partial_week_rule=False)
assert weekly['coverage_state'] == 'complete'
blocked = assess_temporal_comparability(has_monthly_series=False, has_complete_weeks=True, has_partial_week_rule=True)
assert blocked['coverage_state'] == 'blocked'
print('ticket_status and temporal comparability conditional rules passed')
"@
Invoke-PythonCheck 'Functional gap applicability rules' $gapRulesCode

$docMarkersCode = @"
from pathlib import Path

checks = {
    'specs/spec-014-auc-001-analytical-product-contract.md': [
        'completitud se eval',
        'not_available',
        'UNKNOWN',
        'ad_name',
        'ticket_status',
    ],
    'gates/auc-001-p02-entry-gate.md': [
        'PASS WITH CONDITIONS',
        'BigQuery MCP',
        'delimitada por SPEC-014',
    ],
    'tasks/auc-001-p02-analytical-product-contract-implementation-task-plan.md': [
        'P02-T010',
        'P02-T055',
        'READY FOR P02 ENTRY GATE REVIEW',
    ],
}
for path, markers in checks.items():
    text = Path(path).read_text(encoding='utf-8-sig')
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise SystemExit(f'{path} missing markers: {missing}')
print('P02 documentation and gate markers remain available')
"@
Invoke-PythonCheck 'P02 documentary markers' $docMarkersCode


$adversarialClosureCode = @"
from tools.auc_001_analytical_product_contract import (
    QUESTION_DEFINITIONS,
    CoverageMatrixRow,
    RobustnessRecord,
    CommonProductCore,
    COVERAGE_COMPLETE,
    COVERAGE_NOT_AVAILABLE,
    COVERAGE_NOT_APPLICABLE,
    validate_coverage_row,
    validate_common_core,
    build_projection,
    validate_projection_equivalence,
)

# FND-001: AQ-010 explicitly permits justified not_available.
aq010 = CoverageMatrixRow(
    'AQ-010',
    COVERAGE_NOT_AVAILABLE,
    'No actionable opportunities can be derived from approved Knowledge in this execution',
    impact='Recommendations cannot be produced; product must disclose absence',
)
aq010_issues = validate_coverage_row(aq010)
assert aq010_issues == [], [issue.to_dict() for issue in aq010_issues]

# FND-002: complete rows cannot carry low, insufficient, or non-evaluable samples.
depth = {
    'evidence': 'observed',
    'comparison': 'baseline',
    'interpretation': 'meaning',
    'business_implication': 'decision relevance',
    'limitation_or_uncertainty': 'low sample',
    'conclusion_or_hypothesis': 'tentative conclusion',
    'traceability': ['EVD-001'],
}
low_sample_row = CoverageMatrixRow(
    'AQ-005',
    COVERAGE_COMPLETE,
    'answered but low sample',
    ('EVD-001',),
    depth,
    RobustnessRecord(denominator=2, observed_volume=2, coverage='matched', granularity='ad', comparator='peer ads', sample_sufficiency='low_sample'),
)
low_sample_issues = validate_coverage_row(low_sample_row)
assert any(issue.code == 'COMPLETE_WITH_INSUFFICIENT_SAMPLE' and issue.severity == 'blocking' for issue in low_sample_issues), [issue.to_dict() for issue in low_sample_issues]

valid_rows = []
robustness = RobustnessRecord(denominator=20, observed_volume=20, coverage='matched', granularity='question', comparator='baseline', sample_sufficiency='sufficient')
for definition in QUESTION_DEFINITIONS:
    if definition.taxonomy == 'mandatory':
        valid_rows.append(CoverageMatrixRow(definition.question_id, COVERAGE_COMPLETE, 'answered', ('EVD-001',), depth, robustness))
    else:
        valid_rows.append(CoverageMatrixRow(definition.question_id, COVERAGE_NOT_APPLICABLE, 'outside current execution boundary'))
recommendation = {
    'category': 'verifiable_action',
    'knowledge_refs': ['KNW-001'],
    'action': 'review',
    'supporting_evidence': 'coverage limitation',
    'verifiable_result': 'coverage register updated',
    'closure_criterion': 'missingness classified',
    'risk': 'manual drift',
    'dependency': 'authorized source',
}

# FND-003: CommonProductCore must validate knowledge_claims and block recommendations hidden inside Knowledge.
bad_knowledge = {'knowledge_id': 'KNW-001', 'evidence_refs': ['EVD-001'], 'interpretation': 'x', 'limitation_or_uncertainty': 'y', 'recommendation': 'hidden action'}
core = CommonProductCore(
    period={'start': '2026-06-01', 'end': '2026-06-30'},
    scope={'use_case': 'AUC-001'},
    sources=('marts.fct_lead_enriched',),
    evidence_refs=('EVD-001',),
    canonical_metrics={},
    coverage_matrix=tuple(valid_rows),
    knowledge_claims=(bad_knowledge,),
    recommendations=(recommendation,),
    limitations=('limit',),
    unknowns=('unknown',),
)
core_issues = validate_common_core(core)
assert any(issue.code == 'KNOWLEDGE_FIELD_PROHIBITED' for issue in core_issues), [issue.to_dict() for issue in core_issues]

# FND-004: Presentation sections must be inspected for canonical content injection.
valid_core = CommonProductCore(
    period={'start': '2026-06-01', 'end': '2026-06-30'},
    scope={'use_case': 'AUC-001'},
    sources=('marts.fct_lead_enriched',),
    evidence_refs=('EVD-001',),
    canonical_metrics={},
    coverage_matrix=tuple(valid_rows),
    knowledge_claims=({'knowledge_id': 'KNW-001', 'evidence_refs': ['EVD-001'], 'interpretation': 'x', 'limitation_or_uncertainty': 'y'},),
    recommendations=(recommendation,),
    limitations=('limit',),
    unknowns=('unknown',),
)
projection = build_projection(valid_core, 'executive', sections=({'title': 'summary', 'nested': {'new_knowledge': 'hidden claim'}},))
projection_issues = validate_projection_equivalence(valid_core, projection)
assert any(issue.code == 'PROJECTION_FIELD_PROHIBITED' for issue in projection_issues), [issue.to_dict() for issue in projection_issues]
print('QA blocking adversarial cases are covered')
"@
Invoke-PythonCheck 'QA blocking adversarial closure cases' $adversarialClosureCode
$failures = @($Results | Where-Object { $_.Status -ne 'PASS' })
$Results | Format-Table -AutoSize

if ($failures.Count -gt 0) {
    Write-Host "`nAUC-001 P02 analytical product contract tests failed: $($failures.Count)" -ForegroundColor Red
    exit 1
}

Write-Host "`nAll AUC-001 P02 analytical product contract tests passed: $($Results.Count)" -ForegroundColor Green
exit 0