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
    if ($LASTEXITCODE -eq 0) { Add-Result $Name 'PASS' 'tools/auc_001_operational_acceptance_package.py' $output }
    else { Add-Result $Name 'FAIL' 'tools/auc_001_operational_acceptance_package.py' $output }
}

$preflightCode = @"
from tools.auc_001_operational_acceptance_package import validate_mcp_preflight_record

preflight = {
    'specification': 'SPEC-016',
    'status': 'PASS',
    'provider': 'BigQuery MCP',
    'acquisition_strategy': 'independent_table_queries_with_local_reconciliation',
    'multi_table_mcp_queries_allowed_as_evidence': False,
    'planned_tables': ['marts.fct_lead_enriched', 'marts.fct_spend', 'intermediate.int_faro_lead_scoring'],
    'execution_contexts': {
        'marts': {'project_id': 'datamart-vca-494114', 'dataset_id': 'marts', 'max_bytes_billed': 1073741824},
        'intermediate': {'project_id': 'datamart-vca-494114', 'dataset_id': 'intermediate', 'max_bytes_billed': 1073741824},
    },
    'spec_014_grain_readiness': {'AQ-001': 'ready', 'AQ-003': 'ready', 'AQ-009': 'partial_allowed'},
    'reconciliation_states_preserved': ['matched', 'lead_only', 'spend_only'],
}
assert validate_mcp_preflight_record(preflight) == []
bad = dict(preflight)
bad['acquisition_strategy'] = 'multi_table_query'
issues = validate_mcp_preflight_record(bad)
assert any(issue.code == 'PREFLIGHT_STRATEGY_INVALID' for issue in issues), [issue.to_dict() for issue in issues]
bad_grain = dict(preflight)
bad_grain['spec_014_grain_readiness'] = {'AQ-003': 'blocked'}
grain_issues = validate_mcp_preflight_record(bad_grain)
assert any(issue.code == 'PREFLIGHT_SPEC014_GRAIN_BLOCKED' for issue in grain_issues), [issue.to_dict() for issue in grain_issues]
print('preflight blocks non-canonical strategy and insufficient SPEC-014 grain')
"@
Invoke-PythonCheck 'MCP preflight contract' $preflightCode

$recordCode = @"
from tools.auc_001_operational_acceptance_package import validate_mcp_records

base_context = {'project_id': 'datamart-vca-494114', 'dataset_id': 'marts', 'max_bytes_billed': 1073741824}
record = {
    'mcp_call_records': [
        {
            'call_type': 'query_read_only',
            'sql': 'SELECT COUNT(*) AS lead_count FROM `datamart-vca-494114.marts.fct_lead_enriched`',
            'execution_context': base_context,
            'dataset': 'marts',
            'tables': ['marts.fct_lead_enriched'],
            'period': {'start': '2026-04-18', 'end': '2026-07-22'},
            'filters': 'none',
            'granularity': 'table',
            'dry_run_and_cost_control': {'dry_run_status': 'approved', 'max_bytes_billed': 1073741824, 'bytes_processed': 100},
            'result': {'status': 'success'},
            'request_id': 'req-1',
            'trace_reference': 'trc-1',
            'bytes_processed': 100,
            'used_as_evidence': True,
        },
        {
            'call_type': 'query_read_only',
            'sql': 'SELECT * FROM leads CROSS JOIN spend',
            'execution_context': base_context,
            'dataset': 'marts',
            'tables': ['marts.fct_lead_enriched', 'marts.fct_spend'],
            'period': {'start': '2026-04-18', 'end': '2026-07-22'},
            'filters': 'none',
            'granularity': 'cross-table',
            'dry_run_and_cost_control': {'dry_run_status': 'not_available_rejected_before_usable_dry_run', 'max_bytes_billed': 1073741824, 'bytes_processed': None},
            'result': {'status': 'rejected', 'error_code': 'ERR_SCOPE_DENIED'},
            'request_id': 'req-2',
            'trace_reference': 'trc-2',
            'bytes_processed': None,
            'used_as_evidence': False,
        },
    ]
}
assert validate_mcp_records(record) == []
bad = {'mcp_call_records': [dict(record['mcp_call_records'][1], used_as_evidence=True, result={'status': 'success'})]}
issues = validate_mcp_records(bad)
assert any(issue.code == 'MULTITABLE_QUERY_USED_AS_EVIDENCE' for issue in issues), [issue.to_dict() for issue in issues]
bad_rejected = {'mcp_call_records': [dict(record['mcp_call_records'][1], used_as_evidence=True)]}
rejected_issues = validate_mcp_records(bad_rejected)
assert any(issue.code == 'REJECTED_OR_DISCARDED_USED_AS_EVIDENCE' for issue in rejected_issues), [issue.to_dict() for issue in rejected_issues]
print('MCP records preserve rejected calls and prohibit rejected or multi-table Evidence')
"@
Invoke-PythonCheck 'MCP acquisition record contract' $recordCode

$physicalCode = @"
from pathlib import Path
from tools.auc_001_operational_acceptance_package import validate_package

root = Path('outputs/auc-001/spec-016-controlled-proof/2026-07-22')
payload = validate_package(root)
assert payload['decision'] == 'BLOCKED', payload
assert payload['specification'] == 'SPEC-016'
issue_codes = {item['code'] for item in payload['issues']}
assert 'PACKAGE_ROLE_MISSING' in issue_codes or 'AIR_NOT_MATERIALIZED' in issue_codes, payload
print('legacy controlled package is blocked by current Phase 09 physical-depth gate')
"@
Invoke-PythonCheck 'Legacy package blocked by Phase 09 depth gate' $physicalCode


$strategicTraceabilityCode = @"
from tools.auc_001_operational_acceptance_package import validate_strategic_context_traceability

valid = {
    'strategic_context_constraints': {
        'source_artifact': 'knowledge/client/ccd.md',
        'source_refs': ['knowledge/client/ccd.md#campaign_signal'],
        'layers': {'ATTENTION': {}, 'ACTIVATION': {}, 'COMMERCIAL': {}},
        'global_rules': {'required_traceability': 'ccd_constraint_ref'},
    }
}
assert validate_strategic_context_traceability(valid) == []
missing = {}
assert any(issue.code == 'STRATEGIC_CONTEXT_CONSTRAINTS_MISSING' for issue in validate_strategic_context_traceability(missing))
bad = {'strategic_context_constraints': dict(valid['strategic_context_constraints'], source_artifact='docs/context_refs.md')}
assert any(issue.code == 'STRATEGIC_CONTEXT_SOURCE_INVALID' for issue in validate_strategic_context_traceability(bad))
missing_layer = {'strategic_context_constraints': dict(valid['strategic_context_constraints'], layers={'ATTENTION': {}, 'COMMERCIAL': {}})}
assert any(issue.code == 'STRATEGIC_CONTEXT_LAYER_MISSING' for issue in validate_strategic_context_traceability(missing_layer))
print('future package CCD/FARO strategic context traceability helper passed')
"@
Invoke-PythonCheck 'CCD/FARO strategic traceability helper' $strategicTraceabilityCode


$phase09Code = @"
from tools.auc_001_analytical_product_contract import (
    validate_analytical_investigation_record,
    validate_phase09_material_depth,
    validate_spec_017_validation,
)

air = {
    'artifact_id': 'AIR-001',
    'derived_from': 'EVD-001',
    'analytical_questions': ['AQ-003'],
    'alternative_hypotheses': ['retargeting vs mature intent'],
    'contrasts_performed': ['commercial matched vs signal buckets'],
    'discarded_hypotheses': ['creative causality confirmed'],
    'robustness_and_limits': ['monthly only'],
    'findings': [{
        'finding_id': 'FND-001',
        'analytical_question_id': 'AQ-003',
        'observation': 'cost-quality is only direct in commercial matched',
        'evidence_refs': ['EVD-001'],
        'contrast': 'COMMERCIAL vs non-equivalent FARO layers',
        'importance': 'prevents universal KPI ranking',
        'uncertainty': 'CRM final unavailable',
        'related_findings': ['FND-002'],
    }],
}
knowledge = {
    'knowledge_claims': [{
        'knowledge_id': 'K-001',
        'evidence_refs': ['EVD-001'],
        'finding_refs': ['FND-001'],
        'interpretation': 'COMMERCIAL matched is the only direct cost-quality universe.',
        'limitation_or_uncertainty': 'FARO layers are not equivalent.',
    }],
    'analytical_narrative': {
        'text': 'Quality is constrained by verified intent and non-equivalent signal layers.',
        'phenomenon': 'verified intent concentrates quality',
        'trade_off': 'volume vs qualified quality',
        'dominant_risk': 'universal ranking across FARO layers',
        'strategic_implication': 'optimize commercial matched without erasing layer boundaries',
        'knowledge_refs': ['K-001'],
    },
}
spec017 = {
    'specification': 'SPEC-017',
    'decision': 'PASS WITH CONDITIONS',
    'checks': {rid: {'status': 'partial', 'finding_refs': ['FND-001'], 'condition': 'validated with declared coverage limitation'} for rid in ['FR-001','FR-002','FR-003','FR-004','FR-005','FR-006','FR-007','FR-008']},
}
assert validate_analytical_investigation_record(air) == []
assert validate_phase09_material_depth(knowledge, air) == []
assert validate_spec_017_validation(spec017) == []
weak = {'knowledge_claims': [{'knowledge_id': 'K-001', 'claim': '1329 leads', 'evidence_refs': ['EVD-001']}], 'analytical_narrative': {'text': 'summary'}}
descriptive = {'knowledge_claims': [{'knowledge_id': 'K-002', 'evidence_refs': ['EVD-001'], 'finding_refs': ['FND-001'], 'interpretation': '1329 leads and 14 percent Tier A', 'limitation_or_uncertainty': 'coverage limited'}], 'analytical_narrative': knowledge['analytical_narrative']}
issues = validate_phase09_material_depth(weak, {})
assert any(issue.code == 'AIR_NOT_MATERIALIZED' for issue in issues)
assert any(issue.code == 'KNOWLEDGE_WITHOUT_FINDING' for issue in issues)
assert any(issue.code == 'KNOWLEDGE_DESCRIPTIVE_CLAIM' for issue in issues)
descriptive_issues = validate_phase09_material_depth(descriptive, air)
assert any(issue.code == 'KNOWLEDGE_DESCRIPTIVE_INTERPRETATION' for issue in descriptive_issues), [issue.to_dict() for issue in descriptive_issues]
blocking_spec017 = dict(spec017)
blocking_spec017['conditions'] = [{'severity': 'blocking', 'message': 'open blocker'}]
assert any(issue.code == 'SPEC017_BLOCKING_CONDITION_OPEN' for issue in validate_spec_017_validation(blocking_spec017))
partial_without_condition = {'specification': 'SPEC-017', 'decision': 'PASS WITH CONDITIONS', 'checks': {rid: {'status': 'partial', 'finding_refs': ['FND-001']} for rid in ['FR-001','FR-002','FR-003','FR-004','FR-005','FR-006','FR-007','FR-008']}}
assert any(issue.code == 'SPEC017_PARTIAL_WITHOUT_CONDITION' for issue in validate_spec_017_validation(partial_without_condition))
print('Phase 09 material depth validators pass valid AIR and block descriptive Knowledge')
"@
Invoke-PythonCheck 'Phase 09 AIR and material depth validators' $phase09Code

$reviewRegressionCode = @"
from tools.auc_001_analytical_product_contract import validate_canonical_projection_source
from tools.auc_001_operational_acceptance_package import (
    validate_cps_air_physical_link,
    validate_semantic_equivalence_validation,
    validate_spec014_material_validation,
    validate_spec015_validation,
    validate_spec016_validation,
)

single_question_spec014 = {
    'specification': 'SPEC-014',
    'decision': 'PASS',
    'material_depth_validation': {
        'AQ-001': {
            'status': 'complete',
            'evidence': 'EVD-001',
            'comparison': 'A vs B',
            'interpretation': 'explains material difference',
            'business_implication': 'supports a decision',
            'limitation_or_uncertainty': 'none declared',
            'conclusion_or_hypothesis': 'supported hypothesis',
        }
    },
}
spec014_issues = validate_spec014_material_validation(single_question_spec014)
assert any(issue.code == 'SPEC014_QUESTION_MISSING' for issue in spec014_issues), [issue.to_dict() for issue in spec014_issues]

condition_shadow = {
    'specification': 'SPEC-015',
    'decision': 'PASS WITH CONDITIONS',
    'conditions': [{'severity': 'non_blocking'}],
    'issues': [{'severity': 'blocking', 'message': 'hidden blocker'}],
}
assert any(issue.code == 'SPEC015_BLOCKING_CONDITION_OPEN' for issue in validate_spec015_validation(condition_shadow, []))
assert any(issue.code == 'SEMANTIC_EQUIVALENCE_BLOCKING_CONDITION_OPEN' for issue in validate_semantic_equivalence_validation({'decision': 'PASS', 'source_artifacts': ['cps'], 'conditions': [{'severity': 'non_blocking'}], 'issues': [{'severity': 'blocking'}]}))
assert any(issue.code == 'SPEC016_BLOCKING_CONDITION_OPEN' for issue in validate_spec016_validation({'specification': 'SPEC-016', 'decision': 'PASS', 'conditions': [{'severity': 'non_blocking'}], 'issues': [{'severity': 'blocking'}]}))

physical_air = {'findings': [{'finding_id': 'FND-PHYSICAL'}]}
cps = {
    'source_artifacts': {'analytical_investigation_record': 'knowledge/analytical-investigation-record.json'},
    'integrated_view': {'signals': [{'finding_id': 'FND-EMBEDDED'}]},
}
link_issues = validate_cps_air_physical_link(cps, physical_air, 'knowledge/analytical-investigation-record.json', 'product-core/canonical-projection-source.json')
assert any(issue.code == 'CPS_AIR_FINDING_NOT_PRESERVED' for issue in link_issues), [issue.to_dict() for issue in link_issues]
assert any(issue.code == 'CPS_AIR_FINDING_NOT_PHYSICAL' for issue in link_issues), [issue.to_dict() for issue in link_issues]
source_issues = validate_cps_air_physical_link(cps, physical_air, 'knowledge/other-air.json', 'product-core/canonical-projection-source.json')
assert any(issue.code == 'CPS_AIR_SOURCE_ARTIFACT_MISMATCH' for issue in source_issues), [issue.to_dict() for issue in source_issues]

cps_without_support = {
    'schema_family': 'auc_001_canonical_projection_source',
    'specification': 'SPEC-015',
    'source_artifacts': {'analytical_investigation_record': 'knowledge/analytical-investigation-record.json', 'spec_017_validation': 'validations/spec-017-validation.json'},
    'product_contract': {'id': 'SPEC-014'},
    'projection_contracts': {'projection_selection': 'SPEC-010', 'communication_context_transformation': 'SPEC-011', 'canonical_projection_consolidation': 'SPEC-015'},
    'period': {'start': '2026-01-01'},
    'scope': {'case': 'AUC-001'},
    'sources': ['evidence/evidence-set.json'],
    'canonical_metrics': {'lead_count': 1},
    'coverage_states': {qid: 'not_applicable' for qid in ['AQ-001','AQ-002','AQ-003','AQ-004','AQ-005','AQ-006','AQ-007','AQ-008','AQ-009','AQ-010','AQ-011','CQ-001','CQ-002','CQ-003','CQ-004','CQ-005','CQ-006','CQ-007','NAQ-001','NAQ-002','NAQ-003','NAQ-004','NAQ-005']},
    'knowledge_claims': [{'knowledge_id': 'K-001', 'evidence_refs': ['EVD-001'], 'interpretation': 'because trace exists', 'limitation_or_uncertainty': 'none'}],
    'integrated_view': {'signals': [{'finding_id': 'FND-SUPPORT', 'observation': 'obs', 'support': []}]},
    'recommendations': [{'recommendation_id': 'R-001', 'knowledge_refs': ['K-001'], 'action': 'review', 'rationale': 'because trace exists'}],
    'limitations': ['none'],
    'unknowns': ['none'],
    'traceability': {'common_core_fingerprint': 'abc'},
    'strategic_context_constraints': {'source_artifact': 'knowledge/client/ccd.md', 'source_refs': ['ccd'], 'layers': {}, 'global_rules': {'required_traceability': 'ccd_constraint_ref'}},
}
assert any(issue.code == 'CPS_FINDING_WITHOUT_SUPPORT' for issue in validate_canonical_projection_source(cps_without_support))
support_mismatch = validate_cps_air_physical_link(
    {'source_artifacts': {'analytical_investigation_record': 'knowledge/analytical-investigation-record.json'}, 'integrated_view': {'signals': [{'finding_id': 'FND-SUPPORT', 'support': []}]}},
    {'findings': [{'finding_id': 'FND-SUPPORT', 'evidence_refs': ['EVD-001']}]},
    'knowledge/analytical-investigation-record.json',
    'product-core/canonical-projection-source.json',
)
assert any(issue.code == 'CPS_AIR_SUPPORT_MISMATCH' for issue in support_mismatch), [issue.to_dict() for issue in support_mismatch]
print('review regression cases block incomplete SPEC-014, shadowed blockers, AIR/CPS drift and support loss')
"@
Invoke-PythonCheck 'Reviewer regression blockers' $reviewRegressionCode
$retry2BlockedCode = @"
from pathlib import Path
from tools.auc_001_operational_acceptance_package import validate_package

root = Path('outputs/auc-001/exec-2026-07-24-strategic-context-full-rerun-retry-2026-06-30')
payload = validate_package(root)
assert payload['decision'] == 'BLOCKED', payload
codes = {issue['code'] for issue in payload['issues']}
assert 'PACKAGE_ROLE_MISSING' in codes, payload
assert 'AIR_NOT_MATERIALIZED' in codes, payload
assert 'SPEC017_VALIDATION_NOT_MATERIALIZED' in codes, payload
assert 'SPEC014_MATERIAL_DEPTH_MISSING' in codes, payload
print('2026-07-24 retry2 package is blocked by current operational depth validation')
"@
Invoke-PythonCheck 'Retry2 package blocked by operational depth gate' $retry2BlockedCode

$Results | Format-Table -AutoSize
$failures = @($Results | Where-Object { $_.Status -ne 'PASS' })
if ($failures.Count -gt 0) {
    Write-Host "`nAUC-001 SPEC-016 operational package tests failed: $($failures.Count)" -ForegroundColor Red
    exit 1
}

Write-Host "`nAll AUC-001 SPEC-016 operational package tests passed: $($Results.Count)" -ForegroundColor Green
exit 0

