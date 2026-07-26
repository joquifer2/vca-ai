$ErrorActionPreference = 'Stop'

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot '..\..')
Set-Location $RepoRoot

$code = @"
import hashlib
import json
import tempfile
from pathlib import Path

from tools.auc_001_analytical_product_contract import QUESTION_DEFINITIONS
from tools.auc_001_canonical_cost_quality_model import STRATEGIC_CONTEXT_CONSTRAINTS
from tools.auc_001_execution_orchestration import (
    Auc001ExecutionBlocked,
    require_before_cps,
    require_before_presentation,
    validate_current_representation,
    validate_canonical_execution_package,
    write_current_pointer,
)


def write_json(root, rel, payload):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_text(root, rel, text):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def sha(root, rel):
    return hashlib.sha256((root / rel).read_bytes()).hexdigest()


def build_complete_package(root):
    ccd_ref = 'knowledge/client/ccd.md#campaign_signal'
    period = {'start_date': '2026-04-18', 'end_date': '2026-06-30'}
    evidence = {
        'artifact_id': 'EVD-001',
        'status': 'stabilized',
        'facts': {'lead_count': 1329},
        'coverage_state': 'complete',
        'traceability': {'mcp_request_ids': ['req-1']},
    }
    finding = {
        'finding_id': 'FND-001',
        'analytical_question_id': 'AQ-003',
        'observation': 'Commercial matched evidence separates direct cost-quality from non-equivalent layers.',
        'evidence_refs': ['EVD-001'],
        'contrast': 'COMMERCIAL matched compared with non-equivalent FARO layers.',
        'importance': 'It prevents a universal KPI ranking and changes optimization scope.',
        'uncertainty': 'CRM/revenue remains unavailable.',
        'related_findings': ['FND-002'],
    }
    air = {
        'artifact_id': 'AIR-001',
        'derived_from': 'EVD-001',
        'analytical_questions': ['AQ-001', 'AQ-002', 'AQ-003'],
        'alternative_hypotheses': ['volume alone explains quality', 'verified intent explains quality concentration'],
        'contrasts_performed': ['commercial matched vs FARO layer boundaries'],
        'discarded_hypotheses': ['creative causality is confirmed'],
        'robustness_and_limits': ['monthly evidence is sufficient for package proof; CRM remains unavailable'],
        'findings': [finding],
    }
    knowledge_item = {
        'knowledge_id': 'K-001',
        'evidence_refs': ['EVD-001'],
        'finding_refs': ['FND-001'],
        'interpretation': 'Because FARO layers are non-equivalent, cost-quality can only be interpreted inside commercial matched coverage.',
        'limitation_or_uncertainty': 'CRM/revenue remains UNKNOWN.',
    }
    knowledge = {
        'artifact_id': 'KNW-001',
        'status': 'stabilized',
        'derived_from': 'AIR-001',
        'knowledge_claims': [knowledge_item],
        'analytical_narrative': {
            'text': 'Quality is explained by verified intent under non-equivalent FARO layers.',
            'phenomenon': 'verified intent concentrates quality',
            'trade_off': 'volume versus qualified quality',
            'dominant_risk': 'universal KPI ranking across FARO layers',
            'strategic_implication': 'optimize commercial matched while preserving layer boundaries',
            'knowledge_refs': ['K-001'],
        },
    }
    recommendation = {
        'recommendation_id': 'R-001',
        'category': 'measurable_experiment',
        'knowledge_refs': ['K-001'],
        'hypothesis': 'Intent filters improve A/B share without collapsing volume.',
        'action': 'Run a controlled commercial matched test.',
        'population': 'commercial matched Meta leads',
        'primary_metric': 'A/B rate',
        'guardrail': 'minimum commercial matched lead volume',
        'expected_direction': 'increase A/B share',
        'success_criterion': 'A/B rate increases with volume guardrail preserved',
        'validation_window': 'next comparable period',
        'evidence_dependency': 'authorized MCP evidence',
        'uncertainty': 'CRM/revenue remains unavailable',
        'stop_or_review_condition': 'stop if volume guardrail fails',
    }
    recommendations = {'artifact_id': 'REC-001', 'status': 'stabilized', 'recommendations': [recommendation]}
    coverage_rows = []
    material_depth = {}
    for definition in QUESTION_DEFINITIONS:
        qid = definition.question_id
        state = 'not_applicable' if qid.startswith('NAQ-') else 'complete'
        coverage_rows.append({
            'question_id': qid,
            'coverage_state': state,
            'justification': 'synthetic local package covers the gate contract',
            'evidence_refs': ['EVD-001'],
            'depth': {
                'evidence': 'EVD-001',
                'comparison': 'controlled contrast',
                'interpretation': 'because it changes the decision boundary',
                'business_implication': 'supports or constrains action',
                'limitation_or_uncertainty': 'declared limitation',
                'conclusion_or_hypothesis': 'supported conclusion',
                'traceability': 'FND-001',
            },
            'robustness': {
                'denominator': 1329,
                'observed_volume': 1329,
                'coverage': 'complete',
                'granularity': 'aggregate',
                'comparator': 'controlled contrast',
                'sample_sufficiency': 'sufficient for gate proof',
            },
            'impact': 'material',
        })
        material_depth[qid] = {
            'status': state,
            'evidence': 'EVD-001',
            'comparison': 'controlled contrast',
            'interpretation': 'because it changes the decision boundary',
            'business_implication': 'supports or constrains action',
            'limitation_or_uncertainty': 'declared limitation',
            'conclusion_or_hypothesis': 'supported conclusion',
        }
    core = {
        'artifact_id': 'CORE-001',
        'status': 'validated',
        'period': period,
        'scope': {'use_case_id': 'AUC-001'},
        'sources': ['marts.fct_lead_enriched'],
        'evidence_refs': ['EVD-001'],
        'canonical_metrics': {'lead_count': 1329},
        'coverage_matrix': coverage_rows,
        'knowledge_claims': [knowledge_item],
        'recommendations': [recommendation],
        'limitations': ['CRM unavailable'],
        'unknowns': ['revenue UNKNOWN'],
        'strategic_context_constraints': STRATEGIC_CONTEXT_CONSTRAINTS,
    }
    cps = {
        'artifact_id': 'CPS-001',
        'schema_family': 'auc_001_canonical_projection_source',
        'specification': 'SPEC-015',
        'source_artifacts': {
            'context_definition': 'execution/context-definition.json',
            'evidence_set': 'evidence/evidence-set.json',
            'knowledge_set': 'knowledge/knowledge-set.json',
            'recommendation_set': 'recommendations/recommendation-set.json',
            'common_product_core': 'product-core/common-product-core.json',
            'analytical_investigation_record': 'knowledge/analytical-investigation-record.json',
            'spec_017_validation': 'validations/spec-017-validation.json',
            'manifest': 'execution/manifest.json',
        },
        'product_contract': {'id': 'SPEC-014'},
        'projection_contracts': {'projection_selection': 'SPEC-010', 'communication_context_transformation': 'SPEC-011', 'canonical_projection_consolidation': 'SPEC-015'},
        'period': period,
        'scope': {'use_case_id': 'AUC-001'},
        'sources': ['marts.fct_lead_enriched'],
        'canonical_metrics': {'lead_count': 1329},
        'coverage_states': {definition.question_id: ('not_applicable' if definition.question_id.startswith('NAQ-') else 'complete') for definition in QUESTION_DEFINITIONS},
        'knowledge_claims': [knowledge_item],
        'integrated_view': {'signals': [{'finding_id': 'FND-001', 'observation': finding['observation'], 'support': ['EVD-001']}]},
        'recommendations': [recommendation],
        'limitations': ['CRM unavailable'],
        'unknowns': ['revenue UNKNOWN'],
        'traceability': {'common_core_fingerprint': 'synthetic-core'},
        'strategic_context_constraints': STRATEGIC_CONTEXT_CONSTRAINTS,
    }

    artifacts = {
        'execution/context-definition.json': {'artifact_id': 'CTX-001', 'status': 'stabilized'},
        'execution/mcp-preflight-record.json': {
            'specification': 'SPEC-016', 'status': 'PASS', 'provider': 'BigQuery MCP',
            'acquisition_strategy': 'independent_table_queries_with_local_reconciliation',
            'multi_table_mcp_queries_allowed_as_evidence': False,
            'planned_tables': ['marts.fct_lead_enriched'],
            'execution_contexts': {'marts': {'project_id': 'datamart-vca-494114', 'dataset_id': 'marts', 'max_bytes_billed': 1073741824}},
            'reconciliation_states_preserved': ['matched', 'lead_only', 'spend_only'],
        },
        'execution/evidence-acquisition-record.json': {'mcp_call_records': [{
            'call_type': 'query_read_only', 'sql': 'SELECT COUNT(*) AS lead_count FROM table',
            'execution_context': {'project_id': 'datamart-vca-494114', 'dataset_id': 'marts', 'max_bytes_billed': 1073741824},
            'dataset': 'marts', 'tables': ['marts.fct_lead_enriched'], 'period': period,
            'filters': {'period': period}, 'granularity': 'aggregate',
            'dry_run_and_cost_control': {'max_bytes_billed': 1073741824},
            'result': {'status': 'success'}, 'request_id': 'req-1', 'trace_reference': 'trc-1',
            'bytes_processed': 100, 'used_as_evidence': True,
        }]},
        'execution/test-results.json': {'status': 'PASS'},
        'execution/semantic-equivalence-validation.json': {'decision': 'PASS', 'source_artifacts': ['product-core/canonical-projection-source.json']},
        'evidence/evidence-set.json': evidence,
        'knowledge/analytical-investigation-record.json': air,
        'knowledge/knowledge-set.json': knowledge,
        'recommendations/recommendation-set.json': recommendations,
        'product-core/common-product-core.json': core,
        'product-core/canonical-projection-source.json': cps,
        'validations/spec-014-validation.json': {'specification': 'SPEC-014', 'decision': 'PASS', 'material_depth_validation': material_depth},
        'validations/spec-015-validation.json': {'specification': 'SPEC-015', 'decision': 'PASS'},
        'validations/spec-016-validation.json': {'specification': 'SPEC-016', 'decision': 'PASS'},
        'validations/spec-017-validation.json': {'specification': 'SPEC-017', 'decision': 'PASS', 'checks': {rid: {'status': 'complete', 'finding_refs': ['FND-001']} for rid in ['FR-001','FR-002','FR-003','FR-004','FR-005','FR-006','FR-007','FR-008']}},
    }
    for rel, payload in artifacts.items():
        write_json(root, rel, payload)
    write_text(root, 'handoff/reviewer-qa-handoff.md', '## Commands Executed\nREADY_FOR_REVALIDATION\nBigQuery MCP\nNo CLI\nNo fallback\nLimitations\nDeviations\nFinal acceptance\n')
    paths = {
        'manifest': 'execution/manifest.json',
        'physical_traceability': 'execution/physical-traceability.json',
        'mcp_preflight_record': 'execution/mcp-preflight-record.json',
        'evidence_acquisition_record': 'execution/evidence-acquisition-record.json',
        'test_results': 'execution/test-results.json',
        'semantic_equivalence_validation': 'execution/semantic-equivalence-validation.json',
        'evidence_set': 'evidence/evidence-set.json',
        'knowledge_set': 'knowledge/knowledge-set.json',
        'analytical_investigation_record': 'knowledge/analytical-investigation-record.json',
        'recommendation_set': 'recommendations/recommendation-set.json',
        'common_product_core': 'product-core/common-product-core.json',
        'canonical_projection_source': 'product-core/canonical-projection-source.json',
        'spec_014_validation': 'validations/spec-014-validation.json',
        'spec_015_validation': 'validations/spec-015-validation.json',
        'spec_016_validation': 'validations/spec-016-validation.json',
        'spec_017_validation': 'validations/spec-017-validation.json',
        'handoff': 'handoff/reviewer-qa-handoff.md',
        'context_definition': 'execution/context-definition.json',
    }
    manifest = {
        'specification': 'SPEC-016',
        'status': 'READY_FOR_REVALIDATION',
        'source_policy': {'bigquery_mcp_only': True, 'cli_used': False, 'fallback_used': False},
        'acceptance_final_declared_by_implementation': False,
        'artifact_paths': paths,
        'artifact_fingerprints': {rel: sha(root, rel) for role, rel in paths.items() if role not in {'manifest', 'physical_traceability'}},
    }
    write_json(root, 'execution/manifest.json', manifest)
    write_json(root, 'execution/physical-traceability.json', {
        'manifest_sha256': sha(root, 'execution/manifest.json'),
        'test_results_sha256': sha(root, 'execution/test-results.json'),
        'namespace_hygiene_pass': True,
    })


with tempfile.TemporaryDirectory() as tmp:
    tmp_root = Path(tmp)
    partial = tmp_root / 'partial'
    write_json(partial, 'evidence/evidence-set.json', {'artifact_id': 'EVD-LEGACY'})
    write_json(partial, 'knowledge/knowledge-set.json', {'artifact_id': 'KNW-LEGACY'})
    write_json(partial, 'product-core/canonical-projection-source.json', {'artifact_id': 'CPS-LEGACY'})
    write_text(partial, 'presentation/analytical-report.md', '# legacy presentation\n')

    partial_validation = validate_canonical_execution_package(partial)
    assert partial_validation['decision'] == 'BLOCKED', partial_validation
    partial_codes = {issue['code'] for issue in partial_validation['issues']}
    assert 'PACKAGE_ROLE_MISSING' in partial_codes, partial_validation
    try:
        require_before_cps(partial)
        raise AssertionError('partial package was allowed into CPS')
    except Auc001ExecutionBlocked:
        pass
    try:
        require_before_presentation(partial)
        raise AssertionError('partial package was allowed into Presentation')
    except Auc001ExecutionBlocked:
        pass

    canonical = tmp_root / 'canonical'
    build_complete_package(canonical)
    canonical_validation = validate_canonical_execution_package(canonical)
    assert canonical_validation['decision'] == 'PASS', canonical_validation
    assert require_before_cps(canonical)['decision'] == 'PASS'
    assert require_before_presentation(canonical)['decision'] == 'PASS'

    current = tmp_root / 'current'
    pointer = write_current_pointer(canonical, current)
    assert pointer['current_represents_validated_execution'] is True, pointer
    assert validate_current_representation(current)['decision'] == 'PASS'

print('AUC-001 execution orchestration gates block partial packages, pass canonical packages, and restrict current/ to validated pointers')
"@

$output = $code | python -
if ($LASTEXITCODE -ne 0) {
    Write-Host $output
    exit $LASTEXITCODE
}
Write-Host $output
exit 0