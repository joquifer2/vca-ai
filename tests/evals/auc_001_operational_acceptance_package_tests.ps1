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
assert payload['decision'] == 'PASS', payload
assert payload['specification'] == 'SPEC-016'
print('controlled package validates SPEC-016 physical contract')
"@
Invoke-PythonCheck 'Controlled package physical validation' $physicalCode


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

$Results | Format-Table -AutoSize
$failures = @($Results | Where-Object { $_.Status -ne 'PASS' })
if ($failures.Count -gt 0) {
    Write-Host "`nAUC-001 SPEC-016 operational package tests failed: $($failures.Count)" -ForegroundColor Red
    exit 1
}

Write-Host "`nAll AUC-001 SPEC-016 operational package tests passed: $($Results.Count)" -ForegroundColor Green
exit 0

