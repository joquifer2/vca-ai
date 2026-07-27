$ErrorActionPreference = 'Stop'

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot '..\..')
Set-Location $RepoRoot

$code = @"
import json
import tempfile
from pathlib import Path

from tools.auc_001_execution_orchestration import Auc001ExecutionBlocked
from tools.auc_001_canonical_presentation import (
    build_canonical_presentation_reports,
    materialize_canonical_presentation_reports_after_gate,
    validate_canonical_presentation_reports,
)


def write_json(root, rel, payload):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp)
    write_json(root, 'evidence/evidence-set.json', {
        'facts': {
            'lead_coverage': {'lead_count': 1329},
            'lead_tier_total': {
                'A': {'lead_count': 58, 'avg_lead_score': 86.9},
                'B': {'lead_count': 339, 'avg_lead_score': 68.0},
                'C': {'lead_count': 554, 'avg_lead_score': 48.8},
                'D': {'lead_count': 378, 'avg_lead_score': 29.2},
            },
            'monthly_tier': [
                {'month': '2026-04', 'leads': 184, 'ab': 57, 'a': 8},
                {'month': '2026-05', 'leads': 369, 'ab': 111, 'a': 19},
                {'month': '2026-06', 'leads': 776, 'ab': 229, 'a': 31},
            ],
            'platform': [{'platform': 'fb', 'leads': 894, 'ab': 278, 'a': 39}],
            'ticket_status': [{'bucket': 'tiene_billetes', 'leads': 177, 'ab': 157, 'a': 47}],
            'travel_window': [{'bucket': 'menos_de_1_mes', 'leads': 80, 'ab': 74, 'a': 26}],
            'campaigns': [{'campaign': '[META]_[CLP]_[CAPTACION]_[ABO]', 'leads': 1187, 'ab': 344, 'a': 48}],
            'spend_by_signal': {'COMMERCIAL': 875.85, 'ATTENTION': 308.54, 'ACTIVATION': 221.86, 'TOTAL': 1406.25},
            'commercial_matched': {'spend': 873.65, 'leads': 1187, 'ab': 344, 'cost_per_ab': 2.54},
            'activation_observed': {'spend': 221.18, 'leads': 142, 'ab': 53, 'cost_per_ab': 4.17},
            'top_ads': [{'ad_id_norm': '120245828603090721', 'leads': 643, 'ab': 187, 'a': 23}],
        }
    })
    write_json(root, 'knowledge/analytical-investigation-record.json', {'intermediate_findings': [{'finding_id': 'F-001'}]})
    write_json(root, 'knowledge/knowledge-set.json', {'knowledge_claims': [{'knowledge_id': 'K-001'}]})
    write_json(root, 'recommendations/recommendation-set.json', {'recommendations': [
        {'recommendation_id': 'R-001', 'category': 'measurable_experiment', 'action': 'Run intent test', 'primary_metric': 'A/B rate', 'guardrail': 'qualified volume', 'knowledge_refs': ['K-001']},
        {'recommendation_id': 'R-002', 'category': 'verifiable_action', 'action': 'Keep FARO layers separate', 'verifiable_result': 'No universal KPI ranking', 'knowledge_refs': ['K-001']},
        {'recommendation_id': 'R-003', 'category': 'measurable_experiment', 'hypothesis': 'Portfolio mix test', 'primary_metric': 'A/B by campaign role', 'guardrail': 'qualified volume', 'knowledge_refs': ['K-001']},
        {'recommendation_id': 'R-004', 'category': 'non_actionable_hypothesis', 'hypothesis': 'Ad cluster may carry intent framing', 'promotion_condition': 'Controlled creative test', 'knowledge_refs': ['K-001']},
        {'recommendation_id': 'R-005', 'category': 'verifiable_action', 'action': 'Keep missing dimensions out', 'verifiable_result': 'not_available visible', 'knowledge_refs': ['K-001']},
    ]})
    write_json(root, 'product-core/canonical-projection-source.json', {'semantic_fingerprint': 'synthetic-cps'})

    reports = build_canonical_presentation_reports(root)
    validation = validate_canonical_presentation_reports(root, reports)
    assert validation['decision'] == 'PASS', validation
    assert 'outputs/auc-001/2026-06-30/analytical-report.md' not in reports['analytical']
    assert '| Patron semanal | not_available |' in reports['analytical']
    assert '| Conjunto de anuncios | not_available |' in reports['analytical']
    assert 'capas no equivalentes' in reports['analytical']

    compact = validate_canonical_presentation_reports(root, {'analytical': '# short', 'executive': '# short'})
    assert compact['decision'] == 'BLOCKED', compact
    assert any(issue['code'] == 'ANALYTICAL_REPORT_TOO_COMPACT' for issue in compact['issues'])

    try:
        materialize_canonical_presentation_reports_after_gate(root)
        raise AssertionError('partial package was allowed to materialize canonical enriched Presentation')
    except Auc001ExecutionBlocked:
        pass

print('AUC-001 canonical enriched Presentation uses canonical artifacts, declares missing dimensions, blocks compact reports, and requires the canonical gate')
"@

$output = $code | python -
if ($LASTEXITCODE -ne 0) {
    Write-Host $output
    exit $LASTEXITCODE
}
Write-Host $output
exit 0
