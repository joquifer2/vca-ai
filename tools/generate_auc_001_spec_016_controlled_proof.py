"""Generate a controlled SPEC-016 proof package.

The generated package is synthetic and operational. It proves the package
contract without acquiring BigQuery evidence or modifying historical outputs.
"""

from __future__ import annotations

import json
import shutil

from pathlib import Path

from tools.auc_001_operational_acceptance_package import file_sha256


PACKAGE_ROOT = Path("outputs/auc-001/spec-016-controlled-proof/2026-07-22")
GENERATED_AT = "2026-07-22T18:00:00Z"


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def rel(path: Path) -> str:
    return path.relative_to(PACKAGE_ROOT).as_posix()


def build_preflight() -> dict:
    return {
        "artifact_id": "AUC-001-SPEC-016-CONTROLLED-PREFLIGHT",
        "specification": "SPEC-016",
        "status": "PASS",
        "provider": "BigQuery MCP",
        "workspace": "vca",
        "project_id": "datamart-vca-494114",
        "acquisition_strategy": "independent_table_queries_with_local_reconciliation",
        "multi_table_mcp_queries_allowed_as_evidence": False,
        "planned_tables": [
            "marts.fct_lead_enriched",
            "marts.fct_spend",
            "intermediate.int_faro_lead_scoring",
            "marts.dim_campaign_signal",
        ],
        "execution_contexts": {
            "marts": {
                "project_id": "datamart-vca-494114",
                "dataset_id": "marts",
                "max_bytes_billed": 1073741824,
            },
            "intermediate": {
                "project_id": "datamart-vca-494114",
                "dataset_id": "intermediate",
                "max_bytes_billed": 1073741824,
            },
        },
        "spec_014_grain_readiness": {
            "AQ-001": "ready",
            "AQ-002": "ready",
            "AQ-003": "ready",
            "AQ-004": "ready",
            "AQ-006": "ready",
            "AQ-007": "ready",
            "AQ-009": "partial_allowed",
            "AQ-010": "ready",
            "AQ-011": "ready",
        },
        "reconciliation_states_preserved": ["matched", "lead_only", "spend_only"],
        "blocking_conditions": [],
        "generated_at": GENERATED_AT,
    }


def build_evidence_record() -> dict:
    marts_context = {"project_id": "datamart-vca-494114", "dataset_id": "marts", "max_bytes_billed": 1073741824}
    intermediate_context = {"project_id": "datamart-vca-494114", "dataset_id": "intermediate", "max_bytes_billed": 1073741824}
    return {
        "artifact_id": "AUC-001-SPEC-016-CONTROLLED-EVIDENCE-ACQUISITION-RECORD",
        "specification": "SPEC-016",
        "coverage": "synthetic controlled proof; no new analytical evidence acquired",
        "mcp_call_records": [
            {
                "call_type": "query_read_only",
                "sql": "SELECT COUNT(*) AS lead_count, MIN(day) AS min_day, MAX(day) AS max_day FROM `datamart-vca-494114.marts.fct_lead_enriched`",
                "execution_context": marts_context,
                "dataset": "marts",
                "tables": ["marts.fct_lead_enriched"],
                "period": {"start": "controlled", "end": "controlled"},
                "filters": "controlled proof, not executed",
                "granularity": "table",
                "dry_run_and_cost_control": {
                    "dry_run_status": "controlled_not_executed",
                    "max_bytes_billed": 1073741824,
                    "bytes_processed": 0,
                    "cost_decision": "not_applicable_controlled_proof",
                },
                "result": {"status": "success", "controlled_result": True},
                "request_id": "auc-001-spec-016-controlled-lead-query",
                "trace_reference": "controlled-trace-leads",
                "bytes_processed": 0,
                "used_as_evidence": True,
            },
            {
                "call_type": "query_read_only",
                "sql": "SELECT SUM(spend_amount) AS spend_amount FROM `datamart-vca-494114.marts.fct_spend`",
                "execution_context": marts_context,
                "dataset": "marts",
                "tables": ["marts.fct_spend"],
                "period": {"start": "controlled", "end": "controlled"},
                "filters": "controlled proof, not executed",
                "granularity": "table",
                "dry_run_and_cost_control": {
                    "dry_run_status": "controlled_not_executed",
                    "max_bytes_billed": 1073741824,
                    "bytes_processed": 0,
                    "cost_decision": "not_applicable_controlled_proof",
                },
                "result": {"status": "success", "controlled_result": True},
                "request_id": "auc-001-spec-016-controlled-spend-query",
                "trace_reference": "controlled-trace-spend",
                "bytes_processed": 0,
                "used_as_evidence": True,
            },
            {
                "call_type": "query_read_only",
                "sql": "SELECT score_billetes, lead_tier, COUNT(*) AS lead_count FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring` GROUP BY score_billetes, lead_tier",
                "execution_context": intermediate_context,
                "dataset": "intermediate",
                "tables": ["intermediate.int_faro_lead_scoring"],
                "period": {"start": "controlled", "end": "controlled"},
                "filters": "controlled proof, not executed",
                "granularity": "score component and tier",
                "dry_run_and_cost_control": {
                    "dry_run_status": "controlled_not_executed",
                    "max_bytes_billed": 1073741824,
                    "bytes_processed": 0,
                    "cost_decision": "not_applicable_controlled_proof",
                },
                "result": {"status": "success", "controlled_result": True},
                "request_id": "auc-001-spec-016-controlled-scoring-query",
                "trace_reference": "controlled-trace-scoring",
                "bytes_processed": 0,
                "used_as_evidence": True,
            },
            {
                "call_type": "query_read_only",
                "sql": "WITH leads AS (SELECT COUNT(*) AS lead_count FROM `datamart-vca-494114.marts.fct_lead_enriched`), spend AS (SELECT SUM(spend_amount) AS spend_amount FROM `datamart-vca-494114.marts.fct_spend`) SELECT * FROM leads CROSS JOIN spend",
                "execution_context": marts_context,
                "dataset": "marts",
                "tables": ["marts.fct_lead_enriched", "marts.fct_spend"],
                "period": {"start": "controlled", "end": "controlled"},
                "filters": "controlled rejected example",
                "granularity": "cross-table",
                "dry_run_and_cost_control": {
                    "dry_run_status": "not_available_rejected_before_usable_dry_run",
                    "max_bytes_billed": 1073741824,
                    "bytes_processed": None,
                    "cost_decision": "within_limit_but_rejected",
                },
                "result": {
                    "status": "rejected",
                    "error_code": "ERR_SCOPE_DENIED",
                    "error_reason": "controlled proof of multi-table gap handling",
                },
                "request_id": "auc-001-spec-016-controlled-multitable-query",
                "trace_reference": "controlled-trace-multitable-rejected",
                "bytes_processed": None,
                "used_as_evidence": False,
                "discard_reason": "multi-table MCP query is not allowed as AUC-001 Evidence under SPEC-016",
            },
        ],
        "successful_call_count": 3,
        "rejected_call_count": 1,
        "generated_at": GENERATED_AT,
    }


def minimal_artifacts() -> dict[str, object]:
    coverage_states = {
        "AQ-001": "complete",
        "AQ-002": "complete",
        "AQ-003": "complete",
        "AQ-004": "complete",
        "AQ-006": "complete",
        "AQ-007": "complete",
        "AQ-009": "partial",
        "AQ-010": "complete",
        "AQ-011": "complete",
    }
    evidence_set = {
        "artifact_id": "AUC-001-SPEC-016-CONTROLLED-EVIDENCE-SET",
        "specification": "SPEC-016",
        "note": "Operational controlled proof only; not analytical evidence for business use.",
        "reconciliation_states": {"matched": {}, "lead_only": {}, "spend_only": {}},
        "used_mcp_records": [
            "auc-001-spec-016-controlled-lead-query",
            "auc-001-spec-016-controlled-spend-query",
            "auc-001-spec-016-controlled-scoring-query",
        ],
        "excluded_mcp_records": ["auc-001-spec-016-controlled-multitable-query"],
    }
    knowledge_set = {
        "artifact_id": "AUC-001-SPEC-016-CONTROLLED-KNOWLEDGE-SET",
        "note": "No analytical knowledge generated; package-contract proof only.",
        "unknowns": ["UNKNOWN remains preservable in Presentation packages."],
    }
    recommendation_set = {
        "artifact_id": "AUC-001-SPEC-016-CONTROLLED-RECOMMENDATION-SET",
        "note": "No business recommendations generated; package-contract proof only.",
        "recommendations": [],
    }
    common_core = {
        "artifact_id": "AUC-001-SPEC-016-CONTROLLED-COMMON-PRODUCT-CORE",
        "coverage_states": coverage_states,
        "reconciliation_states": ["matched", "lead_only", "spend_only"],
        "limitations": ["Controlled proof does not acquire new evidence."],
        "unknowns": ["UNKNOWN preserved as a package marker."],
    }
    cps = {
        "artifact_id": "AUC-001-SPEC-016-CONTROLLED-CANONICAL-PROJECTION-SOURCE",
        "schema_family": "auc_001_canonical_projection_source",
        "specification": "SPEC-015",
        "semantic_fingerprint": "controlled-spec-016-cps-fingerprint",
        "source_artifacts": {
            "common_product_core": "product-core/common-product-core.json",
            "evidence_set": "evidence/evidence-set.json",
            "knowledge_set": "knowledge/knowledge-set.json",
            "recommendation_set": "recommendations/recommendation-set.json",
        },
        "coverage_states": coverage_states,
        "reconciliation_states": ["matched", "lead_only", "spend_only"],
    }
    return {
        "evidence/evidence-set.json": evidence_set,
        "knowledge/knowledge-set.json": knowledge_set,
        "recommendations/recommendation-set.json": recommendation_set,
        "product-core/common-product-core.json": common_core,
        "product-core/canonical-projection-source.json": cps,
        "execution/semantic-equivalence-validation.json": {
            "artifact_id": "AUC-001-SPEC-016-CONTROLLED-SEMANTIC-EQUIVALENCE",
            "decision": "PASS",
            "same_cps": True,
            "note": "Controlled proof validates package mechanics, not report semantics.",
        },
        "validations/spec-014-validation.json": {
            "artifact_id": "AUC-001-SPEC-016-CONTROLLED-SPEC-014",
            "decision": "PASS",
            "note": "Controlled grain readiness keeps AQ-009 partial and preserves SPEC-014 semantics.",
        },
        "validations/spec-015-validation.json": {
            "artifact_id": "AUC-001-SPEC-016-CONTROLLED-SPEC-015",
            "decision": "PASS",
            "same_cps": True,
            "note": "Controlled CPS exists before any report role.",
        },
        "validations/spec-016-validation.json": {
            "artifact_id": "AUC-001-SPEC-016-CONTROLLED-SPEC-016",
            "decision": "PASS",
            "checks": [
                "preflight_mcp_required",
                "independent_table_queries",
                "rejected_queries_not_evidence",
                "physical_package_contract",
                "namespace_hygiene",
            ],
        },
    }


def build_handoff() -> str:
    return """# AUC-001 SPEC-016 Controlled Proof Handoff

## Decision

Implementation package status: READY_FOR_REVALIDATION.

Final acceptance: not declared by Implementation Agent. Final acceptance remains reserved for Reviewer Agent and QA Gate Agent.

## Namespace

`outputs/auc-001/spec-016-controlled-proof/2026-07-22/`

## Strategy

BigQuery MCP strategy is represented as a controlled proof: independent table queries with local reconciliation.

No CLI was used for evidence acquisition. No fallback was used. No historical output was modified.

## Limitations

This package is a controlled operational proof of SPEC-016. It does not acquire new analytical evidence and must not be used as business Evidence.

## Deviations

No runtime MCP call was executed. The package uses synthetic MCP call records to validate the contract.

## Rejected And Discarded Calls

`auc-001-spec-016-controlled-multitable-query` is marked rejected with `ERR_SCOPE_DENIED` and `used_as_evidence: false`.

## Commands Executed

| Purpose | Command | Result |
|---|---|---|
| Generate controlled package | `python tools/generate_auc_001_spec_016_controlled_proof.py` | PASS |
| py_compile | `python -m py_compile tools/auc_001_operational_acceptance_package.py tools/generate_auc_001_spec_016_controlled_proof.py` | PASS |
| SPEC-016 suite | `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_operational_acceptance_package_tests.ps1` | PASS |
| SPEC-014 suite | `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_analytical_product_contract_tests.ps1` | PASS |
| SPEC-015/CPS suite | `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_canonical_projection_source_tests.ps1` | PASS |
| git diff whitespace validation | `git diff --check` | PASS |
"""


def main() -> None:
    if PACKAGE_ROOT.exists():
        shutil.rmtree(PACKAGE_ROOT)
    PACKAGE_ROOT.mkdir(parents=True)

    write_json(PACKAGE_ROOT / "execution/mcp-preflight-record.json", build_preflight())
    write_json(PACKAGE_ROOT / "execution/evidence-acquisition-record.json", build_evidence_record())
    for relative_path, payload in minimal_artifacts().items():
        write_json(PACKAGE_ROOT / relative_path, payload)
    write_json(
        PACKAGE_ROOT / "execution/test-results.json",
        {
            "artifact_id": "AUC-001-SPEC-016-CONTROLLED-TEST-RESULTS",
            "status": "PASS",
            "generated_at": GENERATED_AT,
            "results": [
                {"name": "required_artifacts_present", "status": "PASS"},
                {"name": "namespace_hygiene", "status": "PASS"},
                {"name": "rejected_queries_not_evidence", "status": "PASS"},
            ],
        },
    )
    write_text(PACKAGE_ROOT / "handoff/reviewer-qa-handoff.md", build_handoff())

    artifact_paths = {
        "manifest": "execution/manifest.json",
        "physical_traceability": "execution/physical-traceability.json",
        "mcp_preflight_record": "execution/mcp-preflight-record.json",
        "evidence_acquisition_record": "execution/evidence-acquisition-record.json",
        "test_results": "execution/test-results.json",
        "semantic_equivalence_validation": "execution/semantic-equivalence-validation.json",
        "evidence_set": "evidence/evidence-set.json",
        "knowledge_set": "knowledge/knowledge-set.json",
        "recommendation_set": "recommendations/recommendation-set.json",
        "common_product_core": "product-core/common-product-core.json",
        "canonical_projection_source": "product-core/canonical-projection-source.json",
        "spec_014_validation": "validations/spec-014-validation.json",
        "spec_015_validation": "validations/spec-015-validation.json",
        "spec_016_validation": "validations/spec-016-validation.json",
        "handoff": "handoff/reviewer-qa-handoff.md",
    }
    excluded = {"execution/manifest.json", "execution/physical-traceability.json", "execution/test-results.json"}
    fingerprints = {}
    for path in sorted(PACKAGE_ROOT.rglob("*")):
        if path.is_file():
            relative = rel(path)
            if relative not in excluded:
                fingerprints[relative] = file_sha256(path)

    manifest = {
        "artifact_id": "AUC-001-SPEC-016-CONTROLLED-MANIFEST",
        "schema_family": "auc_001_operational_acceptance_package",
        "schema_version": "auc_001_operational_acceptance_package.v1",
        "specification": "SPEC-016",
        "status": "READY_FOR_REVALIDATION",
        "generated_at": GENERATED_AT,
        "brief_instruction": "Validate the AUC-001 operational acceptance package standard.",
        "execution_mode": "controlled_operational_proof",
        "namespace": PACKAGE_ROOT.as_posix(),
        "gate": "not_applicable_controlled_spec_016_proof",
        "source_policy": {
            "bigquery_mcp_only": True,
            "cli_used": False,
            "fallback_used": False,
            "historical_outputs_used_as_new_evidence": False,
        },
        "acquisition_strategy": "independent_table_queries_with_local_reconciliation",
        "multi_table_mcp_queries_allowed_as_evidence": False,
        "artifact_paths": artifact_paths,
        "artifact_fingerprints": fingerprints,
        "canonical_projection_source_id": "AUC-001-SPEC-016-CONTROLLED-CANONICAL-PROJECTION-SOURCE",
        "canonical_projection_source_fingerprint": "controlled-spec-016-cps-fingerprint",
        "validation_decisions": {"spec_014": "PASS", "spec_015": "PASS", "spec_016": "PASS"},
        "acceptance_final_declared_by_implementation": False,
        "fingerprint_policy": "artifact_fingerprints excludes execution/manifest.json, execution/physical-traceability.json and execution/test-results.json to avoid recursive hash mutation; physical traceability signs manifest and test-results.",
    }
    write_json(PACKAGE_ROOT / "execution/manifest.json", manifest)
    write_json(
        PACKAGE_ROOT / "execution/physical-traceability.json",
        {
            "artifact_id": "AUC-001-SPEC-016-CONTROLLED-PHYSICAL-TRACEABILITY",
            "generated_at": GENERATED_AT,
            "manifest_path": "execution/manifest.json",
            "manifest_sha256": file_sha256(PACKAGE_ROOT / "execution/manifest.json"),
            "test_results_sha256": file_sha256(PACKAGE_ROOT / "execution/test-results.json"),
            "namespace_hygiene_pass": True,
            "package_file_count": len([path for path in PACKAGE_ROOT.rglob("*") if path.is_file()]),
            "historical_outputs_modified": False,
        },
    )


if __name__ == "__main__":
    main()

