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

$cpsBuildCode = @"
import json
from pathlib import Path
from tools.auc_001_analytical_product_contract import (
    CANONICAL_PROJECTION_SCHEMA_FAMILY,
    build_canonical_projection_source,
    validate_canonical_projection_source,
)

base = Path('outputs/auc-001/p02/2026-07-17')
common_core = json.loads((base / 'product-core/common-product-core.json').read_text(encoding='utf-8'))
knowledge_set = json.loads((base / 'knowledge/knowledge-set.json').read_text(encoding='utf-8'))
recommendation_set = json.loads((base / 'recommendations/recommendation-set.json').read_text(encoding='utf-8'))
coverage_matrix = json.loads((base / 'coverage-matrix/coverage-matrix.json').read_text(encoding='utf-8'))
manifest = json.loads((base / 'execution/manifest.json').read_text(encoding='utf-8'))

cps = build_canonical_projection_source(
    common_core,
    knowledge_set=knowledge_set,
    recommendation_set=recommendation_set,
    coverage_matrix=coverage_matrix,
    manifest=manifest,
)
payload = cps.to_dict()
assert payload['schema_family'] == CANONICAL_PROJECTION_SCHEMA_FAMILY
assert payload['specification'] == 'SPEC-015'
assert payload['projection_contracts']['projection_selection'] == 'SPEC-010'
assert payload['projection_contracts']['communication_context_transformation'] == 'SPEC-011'
assert payload['product_contract']['id'] == 'SPEC-014'
assert len(payload['knowledge_claims']) == 6
assert len(payload['recommendations']) == 4
assert payload['integrated_view']['signals'][0]['finding_id'] == 'FND-001'
assert payload['coverage_states']['AQ-010'] == 'complete'
assert payload['future_evidence_gaps']['revenue_or_crm'] == 'declared_dependency_on_future_evidence'
assert payload['future_evidence_gaps']['creative_causality'] == 'declared_dependency_on_future_evidence'
assert payload['future_evidence_gaps']['additional_creative_metadata'] == 'declared_dependency_on_future_evidence'
assert payload['future_evidence_gaps']['provider_limited_temporality'] == 'declared_dependency_on_future_evidence'
issues = validate_canonical_projection_source(cps)
assert issues == [], [issue.to_dict() for issue in issues]
print('CPS builds from P02 canonical artifacts and validates SPEC-015 blocks')
"@
Invoke-PythonCheck 'CPS canonical source construction' $cpsBuildCode

$projectionCode = @"
import json
from pathlib import Path
from tools.auc_001_analytical_product_contract import (
    build_canonical_projection_source,
    build_projection_from_cps,
    validate_projection_against_cps,
)

base = Path('outputs/auc-001/p02/2026-07-17')
common_core = json.loads((base / 'product-core/common-product-core.json').read_text(encoding='utf-8'))
knowledge_set = json.loads((base / 'knowledge/knowledge-set.json').read_text(encoding='utf-8'))
recommendation_set = json.loads((base / 'recommendations/recommendation-set.json').read_text(encoding='utf-8'))
coverage_matrix = json.loads((base / 'coverage-matrix/coverage-matrix.json').read_text(encoding='utf-8'))
manifest = json.loads((base / 'execution/manifest.json').read_text(encoding='utf-8'))

cps = build_canonical_projection_source(common_core, knowledge_set=knowledge_set, recommendation_set=recommendation_set, coverage_matrix=coverage_matrix, manifest=manifest)
analytical = build_projection_from_cps(cps, 'analytical', sections=({'title': 'coverage matrix summary', 'content_ref': 'cps.integrated_view'},))
executive = build_projection_from_cps(cps, 'executive', sections=({'title': 'decision summary', 'content_ref': 'cps.decision_patterns'},))
assert validate_projection_against_cps(cps, analytical) == []
assert validate_projection_against_cps(cps, executive) == []
assert analytical.canonical_projection_source_fingerprint == executive.canonical_projection_source_fingerprint
assert analytical.to_dict()['recommendation_refs'] == executive.to_dict()['recommendation_refs']
assert analytical.to_dict()['coverage_states'] == executive.to_dict()['coverage_states']
with_items = build_projection_from_cps(cps, 'executive', sections=({'title': 'decision summary', 'content_ref': 'cps.decision_patterns', 'items': [{'title': 'priority', 'content_ref': 'cps.decision_patterns[0]'}]},))
assert validate_projection_against_cps(cps, with_items) == []
print('analytical and executive projections derive as siblings from the same CPS')
"@
Invoke-PythonCheck 'Sibling projection derivation from CPS' $projectionCode

$newKnowledgeBlockCode = @"
import json
from pathlib import Path
from tools.auc_001_analytical_product_contract import (
    build_canonical_projection_source,
    build_projection_from_cps,
    validate_projection_against_cps,
)

base = Path('outputs/auc-001/p02/2026-07-17')
common_core = json.loads((base / 'product-core/common-product-core.json').read_text(encoding='utf-8'))
knowledge_set = json.loads((base / 'knowledge/knowledge-set.json').read_text(encoding='utf-8'))
recommendation_set = json.loads((base / 'recommendations/recommendation-set.json').read_text(encoding='utf-8'))
coverage_matrix = json.loads((base / 'coverage-matrix/coverage-matrix.json').read_text(encoding='utf-8'))
manifest = json.loads((base / 'execution/manifest.json').read_text(encoding='utf-8'))

cps = build_canonical_projection_source(common_core, knowledge_set=knowledge_set, recommendation_set=recommendation_set, coverage_matrix=coverage_matrix, manifest=manifest)
projection = build_projection_from_cps(cps, 'executive', sections=({'title': 'summary', 'text': 'El producto recupera el valor historico.'},))
issues = validate_projection_against_cps(cps, projection)
assert any(issue.code == 'PROJECTION_NEW_KNOWLEDGE_BLOCKED' for issue in issues), [issue.to_dict() for issue in issues]
field_projection = build_projection_from_cps(cps, 'analytical', sections=({'title': 'bad', 'new_knowledge': 'hidden claim'},))
field_issues = validate_projection_against_cps(cps, field_projection)
assert any(issue.code == 'PROJECTION_FIELD_PROHIBITED' for issue in field_issues), [issue.to_dict() for issue in field_issues]
free_text_projection = build_projection_from_cps(cps, 'executive', sections=({'title': 'summary', 'text': 'Subir presupuesto manana porque la calidad ya esta validada comercialmente.'},))
free_text_issues = validate_projection_against_cps(cps, free_text_projection)
assert any(issue.code == 'PROJECTION_UNAPPROVED_SECTION_FIELD' for issue in free_text_issues), [issue.to_dict() for issue in free_text_issues]
assert any(issue.code == 'PROJECTION_SECTION_UNTRACED' for issue in free_text_issues), [issue.to_dict() for issue in free_text_issues]
items_text_projection = build_projection_from_cps(cps, 'executive', sections=({'title': 'summary', 'content_ref': 'cps.decision_patterns', 'items': ['Subir presupuesto manana porque la calidad ya esta validada comercialmente.']},))
items_text_issues = validate_projection_against_cps(cps, items_text_projection)
assert any(issue.code == 'PROJECTION_ITEM_FREE_TEXT' for issue in items_text_issues), [issue.to_dict() for issue in items_text_issues]
items_untraced_projection = build_projection_from_cps(cps, 'executive', sections=({'title': 'summary', 'content_ref': 'cps.decision_patterns', 'items': [{'title': 'loose item'}]},))
items_untraced_issues = validate_projection_against_cps(cps, items_untraced_projection)
assert any(issue.code == 'PROJECTION_ITEM_UNTRACED' for issue in items_untraced_issues), [issue.to_dict() for issue in items_untraced_issues]
print('Presentation blocks historical value claims, free narrative claims, free-text items and injected canonical content')
"@
Invoke-PythonCheck 'Presentation new knowledge blockers' $newKnowledgeBlockCode

$semanticDivergenceCode = @"
import json
from pathlib import Path
from tools.auc_001_analytical_product_contract import (
    build_canonical_projection_source,
    build_projection_from_cps,
    validate_projection_against_cps,
)

base = Path('outputs/auc-001/p02/2026-07-17')
common_core = json.loads((base / 'product-core/common-product-core.json').read_text(encoding='utf-8'))
knowledge_set = json.loads((base / 'knowledge/knowledge-set.json').read_text(encoding='utf-8'))
recommendation_set = json.loads((base / 'recommendations/recommendation-set.json').read_text(encoding='utf-8'))
coverage_matrix = json.loads((base / 'coverage-matrix/coverage-matrix.json').read_text(encoding='utf-8'))
manifest = json.loads((base / 'execution/manifest.json').read_text(encoding='utf-8'))

cps = build_canonical_projection_source(common_core, knowledge_set=knowledge_set, recommendation_set=recommendation_set, coverage_matrix=coverage_matrix, manifest=manifest)
projection = build_projection_from_cps(cps, 'executive')
payload = projection.to_dict()
payload['coverage_states']['AQ-009'] = 'complete'
payload['recommendation_refs'][0]['success_criterion'] = 'changed by presentation'
payload['derived_from_projection'] = 'analytical'
issues = validate_projection_against_cps(cps, payload)
assert any(issue.code == 'PROJECTION_COVERAGE_DIVERGENCE' for issue in issues), [issue.to_dict() for issue in issues]
assert any(issue.code == 'PROJECTION_RECOMMENDATION_DIVERGENCE' for issue in issues), [issue.to_dict() for issue in issues]
assert any(issue.code == 'PROJECTION_SIBLING_RULE_VIOLATION' for issue in issues), [issue.to_dict() for issue in issues]
print('semantic equivalence blocks coverage, recommendation and sibling-rule drift')
"@
Invoke-PythonCheck 'Semantic equivalence divergence blockers' $semanticDivergenceCode

$Results | Format-Table -AutoSize
$failures = @($Results | Where-Object { $_.Status -ne 'PASS' })
if ($failures.Count -gt 0) {
    Write-Host "`nAUC-001 P04 CPS tests failed: $($failures.Count)" -ForegroundColor Red
    exit 1
}

Write-Host "`nAll AUC-001 P04 CPS tests passed: $($Results.Count)" -ForegroundColor Green
exit 0
