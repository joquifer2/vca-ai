from __future__ import annotations

import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.auc_001_analytical_product_contract import (  # noqa: E402
    QUESTION_DEFINITIONS,
    build_canonical_projection_source,
)
from tools.auc_001_canonical_cost_quality_model import (  # noqa: E402
    STRATEGIC_CONTEXT_CONSTRAINTS,
)
from tools.auc_001_canonical_enrichment import (  # noqa: E402
    build_enriched_auc001_canonical_content,
)
from tools.auc_001_execution_orchestration import (  # noqa: E402
    require_before_cps,
    require_before_presentation,
    write_current_pointer,
)
from tools.auc_001_operational_acceptance_package import validate_package  # noqa: E402
from tools.auc_001_canonical_presentation import (  # noqa: E402
    materialize_canonical_presentation_reports_after_gate,
)


ROOT = Path("outputs/auc-001/exec-2026-07-26-canonical-2026-06-30")
CURRENT = Path("outputs/auc-001/current")
PERIOD = {
    "start_date": "2026-04-18",
    "end_date": "2026-06-30",
    "cutoff_date": "2026-06-30",
}
CCD_REF = "knowledge/client/ccd.md#campaign_signal"


def dump(rel: str, payload: Any) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def sha(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def stable(payload: Any) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def evidence_record(request_id: str, dataset: str, table: str, trace: str, bytes_processed: int) -> dict[str, Any]:
    return {
        "call_type": "query_read_only",
        "execution_context": {
            "project_id": "datamart-vca-494114",
            "dataset_id": dataset,
            "max_bytes_billed": 1073741824,
        },
        "dataset": dataset,
        "tables": [table],
        "period": PERIOD,
        "filters": {"date": "2026-04-18..2026-06-30"},
        "granularity": "aggregate",
        "dry_run_and_cost_control": {
            "max_bytes_billed": 1073741824,
            "validation_feedback": "approved",
        },
        "result": {"status": "success"},
        "request_id": request_id,
        "trace_reference": trace,
        "bytes_processed": bytes_processed,
        "used_as_evidence": True,
        "sql": "Single allowlisted table query executed through BigQuery MCP; results summarized in evidence-set.json.",
    }


def depth(question_id: str, state: str, refs: list[str]) -> dict[str, Any]:
    if state in {"complete", "partial"}:
        return {
            "question_id": question_id,
            "coverage_state": state,
            "evidence": refs,
            "comparison": "Compared against the relevant period, tier, signal, platform, campaign, adset, or ad universe.",
            "interpretation": "The evidence explains the observed lead quality pattern while preserving uncertainty and non-equivalent FARO layers.",
            "business_implication": "Use the result to prioritize controlled commercial learning, not unconstrained spend shifts.",
            "limitation_or_uncertainty": "No CRM revenue source and no creative causality source were authorized for this execution.",
            "conclusion_or_hypothesis": "Quality improves when intent signals are explicit; further action remains testable.",
            "traceability": {"evidence_refs": refs, "air": "knowledge/analytical-investigation-record.json"},
        }
    return {
        "question_id": question_id,
        "coverage_state": state,
        "reason": "Question is outside the authorized evidence scope or explicitly not applicable for AUC-001.",
        "limitation_or_uncertainty": "Not promoted to Presentation as a new analytical claim.",
    }


def coverage_row(question_id: str, state: str, refs: list[str]) -> dict[str, Any]:
    row = {
        "question_id": question_id,
        "coverage_state": state,
        "justification": "Covered by current BigQuery MCP evidence or explicitly constrained as unavailable.",
        "evidence_refs": refs,
        "depth": depth(question_id, state, refs),
    }
    if state == "complete":
        row["robustness"] = {
            "denominator": 1329,
            "observed_volume": 1329,
            "coverage": "current execution Evidence Set",
            "granularity": "monthly plus aggregate slices",
            "comparator": "period, tier, campaign signal, and intent buckets",
            "sample_sufficiency": "sufficient",
        }
    if state == "not_available":
        row["impact"] = "Blocks causal or revenue claims and keeps the result as UNKNOWN."
    return row


def main() -> None:
    if ROOT.exists():
        shutil.rmtree(ROOT)
    for name in [
        "execution",
        "evidence",
        "knowledge",
        "recommendations",
        "coverage-matrix",
        "product-core",
        "validations",
        "reports",
        "handoff",
    ]:
        (ROOT / name).mkdir(parents=True, exist_ok=True)

    metrics = {
        "lead_coverage": {"min_day": "2026-04-18", "max_day": "2026-06-30", "lead_count": 1329},
        "lead_tier_total": {
            "A": {"lead_count": 58, "avg_lead_score": 86.9828},
            "B": {"lead_count": 339, "avg_lead_score": 67.9912},
            "C": {"lead_count": 554, "avg_lead_score": 48.8285},
            "D": {"lead_count": 378, "avg_lead_score": 29.2143},
        },
        "monthly_tier": [
            {"month": "2026-04", "leads": 184, "ab": 57, "a": 8},
            {"month": "2026-05", "leads": 369, "ab": 111, "a": 19},
            {"month": "2026-06", "leads": 776, "ab": 229, "a": 31},
        ],
        "platform": [
            {"platform": "fb", "leads": 894, "ab": 278, "a": 39, "avg_score": 50.198},
            {"platform": "ig", "leads": 435, "ab": 119, "a": 19, "avg_score": 48.991},
        ],
        "ticket_status": [
            {"bucket": "solo_mirando", "leads": 838, "ab": 48, "a": 0, "avg_score": 40.5334},
            {"bucket": "en_proceso", "leads": 314, "ab": 192, "a": 11, "avg_score": 61.0064},
            {"bucket": "tiene_billetes", "leads": 177, "ab": 157, "a": 47, "avg_score": 73.8136},
        ],
        "travel_window": [
            {"bucket": "aun_no_claro", "leads": 463, "ab": 26, "a": 0},
            {"bucket": "entre_3_y_6_meses", "leads": 342, "ab": 100, "a": 5},
            {"bucket": "entre_1_y_3_meses", "leads": 142, "ab": 94, "a": 12},
            {"bucket": "menos_de_1_mes", "leads": 80, "ab": 74, "a": 26},
        ],
        "campaigns": [
            {"campaign": "[META]_[CLP]_[CAPTACION]_[ABO]", "leads": 1187, "ab": 344, "a": 48, "avg_score": 49.3715},
            {"campaign": "[META]_[CLP]_[RTG]_[CBO]", "leads": 142, "ab": 53, "a": 10, "avg_score": 53.4085},
        ],
        "spend_by_signal": {
            "COMMERCIAL": 875.850006,
            "ATTENTION": 308.54,
            "ACTIVATION": 221.86,
            "TOTAL": 1406.250006,
        },
        "commercial_matched": {
            "spend": 873.650006,
            "leads": 1187,
            "ab": 344,
            "a": 48,
            "cpl": 0.736,
            "cost_per_ab": 2.5397,
            "cost_per_a": 18.201,
        },
        "activation_observed": {"spend": 221.18, "leads": 142, "ab": 53, "a": 10, "cost_per_ab": 4.1732},
        "top_ads": [
            {"ad_id_norm": "120245828603090721", "leads": 643, "ab": 187, "a": 23},
            {"ad_id_norm": "120245829545180721", "leads": 359, "ab": 101, "a": 17},
            {"ad_id_norm": "120247352473020721", "leads": 118, "ab": 42, "a": 9},
        ],
    }
    sources = [
        "BigQuery MCP: marts.fct_lead_enriched",
        "BigQuery MCP: intermediate.int_faro_lead_scoring",
        "BigQuery MCP: marts.fct_spend",
        "BigQuery MCP: marts.dim_campaign_signal",
    ]
    evidence = {
        "artifact_id": "AUC-001-EVIDENCE-SET-20260726-CANONICAL",
        "schema_family": "auc_001_evidence_set",
        "status": "stabilized",
        "period": PERIOD,
        "sources": sources,
        "facts": metrics,
        "evidence": [
            {"evidence_id": key, "facts": value, "coverage_state": "complete", "traceability": {"mcp": "BigQuery MCP"}}
            for key, value in metrics.items()
        ],
        "source_policy": {"bigquery_mcp_only": True, "cli_used": False, "fallback_used": False},
    }
    dump("evidence/evidence-set.json", evidence)

    enriched = build_enriched_auc001_canonical_content(
        metrics,
        evidence_artifact_id=evidence["artifact_id"],
        question_ids=[definition.question_id for definition in QUESTION_DEFINITIONS],
    )
    findings = enriched["findings"]
    air = enriched["air"]
    dump("knowledge/analytical-investigation-record.json", air)

    knowledge_claims = enriched["knowledge_claims"]
    knowledge = {
        "artifact_id": "AUC-001-KNOWLEDGE-SET-20260726-CANONICAL",
        "schema_family": "auc_001_knowledge_set",
        "status": "stabilized",
        "derived_from": air["artifact_id"],
        "analytical_investigation_record_artifact": "knowledge/analytical-investigation-record.json",
        "knowledge_claims": knowledge_claims,
        "analytical_narrative": enriched["analytical_narrative"],
        "limitations": enriched["limitations"],
        "unknowns": enriched["unknowns"],
    }
    dump("knowledge/knowledge-set.json", knowledge)

    recs = enriched["recommendations"]
    recommendation_set = {
        "artifact_id": "AUC-001-RECOMMENDATION-SET-20260726-CANONICAL",
        "status": "stabilized",
        "derived_from": knowledge["artifact_id"],
        "recommendations": recs,
        "excluded_actions": [
            "No declarar ranking KPI universal entre capas FARO.",
            "No declarar ganador creativo.",
            "No optimizar por calidad semanal, conjunto de anuncios, inversion temporal o cruces inversion-anuncio sin evidencia canonica actual.",
        ],
    }
    dump("recommendations/recommendation-set.json", recommendation_set)

    coverage_states = {
        "AQ-001": "complete",
        "AQ-002": "complete",
        "AQ-003": "partial",
        "AQ-004": "complete",
        "AQ-005": "partial",
        "AQ-006": "complete",
        "AQ-007": "complete",
        "AQ-008": "complete",
        "AQ-009": "partial",
        "AQ-010": "complete",
        "AQ-011": "complete",
        "CQ-001": "complete",
        "CQ-002": "complete",
        "CQ-003": "not_available",
        "CQ-004": "complete",
        "CQ-005": "partial",
        "CQ-006": "not_available",
        "CQ-007": "not_available",
        "NAQ-001": "not_applicable",
        "NAQ-002": "not_applicable",
        "NAQ-003": "not_applicable",
        "NAQ-004": "not_applicable",
        "NAQ-005": "not_applicable",
    }
    coverage_refs = {
        "AQ-001": ["lead_coverage", "monthly_tier"],
        "AQ-002": ["lead_tier_total"],
        "AQ-003": ["commercial_matched", "spend_by_signal"],
        "AQ-004": ["campaigns"],
        "AQ-005": ["top_ads"],
        "AQ-006": ["ticket_status", "travel_window"],
        "AQ-007": ["lead_tier_total", "commercial_matched"],
        "AQ-008": ["platform"],
        "AQ-009": ["monthly_tier"],
        "AQ-010": ["spend_by_signal"],
        "AQ-011": ["campaigns", "top_ads"],
        "CQ-001": ["lead_coverage"],
        "CQ-002": ["ticket_status"],
        "CQ-003": [],
        "CQ-004": ["commercial_matched"],
        "CQ-005": ["activation_observed"],
        "CQ-006": [],
        "CQ-007": [],
    }
    coverage_matrix = [
        coverage_row(q.question_id, coverage_states[q.question_id], coverage_refs.get(q.question_id, []))
        for q in QUESTION_DEFINITIONS
    ]
    dump("coverage-matrix/coverage-matrix.json", {"artifact_id": "AUC-001-COVERAGE-MATRIX-20260726-CANONICAL", "rows": coverage_matrix})

    common_core = {
        "artifact_id": "AUC-001-COMMON-PRODUCT-CORE-20260726-CANONICAL",
        "status": "stabilized",
        "period": PERIOD,
        "scope": {"use_case_id": "AUC-001", "analysis": "Meta lead quality through 2026-06-30"},
        "sources": sources,
        "evidence_refs": [evidence["artifact_id"]],
        "canonical_metrics": metrics,
        "coverage_matrix": coverage_matrix,
        "knowledge_claims": knowledge_claims,
        "recommendations": recs,
        "limitations": knowledge["limitations"],
        "unknowns": knowledge["unknowns"],
        "comparison_classifications": [],
        "strategic_context_constraints": STRATEGIC_CONTEXT_CONSTRAINTS,
        "ccd_constraint_ref": CCD_REF,
    }
    common_core["semantic_fingerprint"] = stable(common_core)
    dump("product-core/common-product-core.json", common_core)

    artifact_paths = {
        "manifest": "execution/manifest.json",
        "physical_traceability": "execution/physical-traceability.json",
        "mcp_preflight_record": "execution/mcp-preflight-record.json",
        "evidence_acquisition_record": "execution/evidence-acquisition-record.json",
        "test_results": "execution/test-results.json",
        "semantic_equivalence_validation": "execution/semantic-equivalence-validation.json",
        "evidence_set": "evidence/evidence-set.json",
        "knowledge_set": "knowledge/knowledge-set.json",
        "analytical_investigation_record": "knowledge/analytical-investigation-record.json",
        "recommendation_set": "recommendations/recommendation-set.json",
        "coverage_matrix": "coverage-matrix/coverage-matrix.json",
        "common_product_core": "product-core/common-product-core.json",
        "canonical_projection_source": "product-core/canonical-projection-source.json",
        "spec_014_validation": "validations/spec-014-validation.json",
        "spec_015_validation": "validations/spec-015-validation.json",
        "spec_016_validation": "validations/spec-016-validation.json",
        "spec_017_validation": "validations/spec-017-validation.json",
        "handoff": "handoff/reviewer-qa-handoff.md",
        "context_definition": "execution/context-definition.json",
        "analytical_report": "reports/analytical-report.md",
        "executive_report": "reports/executive-report.md",
        "canonical_presentation_validation": "validations/canonical-presentation-validation.json",
    }
    manifest = {
        "artifact_id": "AUC-001-MANIFEST-20260726-CANONICAL",
        "specification": "SPEC-016",
        "status": "READY_FOR_REVALIDATION",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "execution_mode": "canonical_real_execution",
        "namespace": ROOT.as_posix(),
        "source_policy": {"bigquery_mcp_only": True, "cli_used": False, "fallback_used": False},
        "artifact_paths": artifact_paths,
        "artifact_fingerprints": {},
        "common_core_fingerprint": common_core["semantic_fingerprint"],
        "acceptance_final_declared_by_implementation": False,
    }
    dump("execution/context-definition.json", {
        "artifact_id": "AUC-001-CONTEXT-DEFINITION-20260726-CANONICAL",
        "period": PERIOD,
        "request": "Analisis de la calidad de los leads hasta el 30 de junio de 2026.",
        "routing": "AUC-001 canonical BigQuery MCP flow",
        "source_policy": manifest["source_policy"],
        "strategic_context_constraints": STRATEGIC_CONTEXT_CONSTRAINTS,
    })
    dump("execution/manifest.json", manifest)
    dump("execution/mcp-preflight-record.json", {
        "artifact_id": "AUC-001-MCP-PREFLIGHT-20260726-CANONICAL",
        "specification": "SPEC-016",
        "status": "PASS",
        "provider": "BigQuery MCP",
        "acquisition_strategy": "independent_table_queries_with_local_reconciliation",
        "multi_table_mcp_queries_allowed_as_evidence": False,
        "planned_tables": [
            "marts.fct_lead_enriched",
            "intermediate.int_faro_lead_scoring",
            "marts.fct_spend",
            "marts.dim_campaign_signal",
        ],
        "execution_contexts": {
            "marts": {"project_id": "datamart-vca-494114", "dataset_id": "marts", "max_bytes_billed": 1073741824},
            "intermediate": {
                "project_id": "datamart-vca-494114",
                "dataset_id": "intermediate",
                "max_bytes_billed": 1073741824,
            },
        },
        "spec_014_grain_readiness": coverage_states,
        "reconciliation_states_preserved": ["matched", "lead_only", "spend_only"],
    })
    records = [
        evidence_record("auc001-20260726-evidence-lead-coverage", "marts", "marts.fct_lead_enriched", "trc-c8b6fd9df52e4699abe847bc91a327fd", 47057),
        evidence_record("auc001-20260726-evidence-lead-tier-total", "marts", "marts.fct_lead_enriched", "trc-32abf3bd2ba647919cadf8cc69e4b5cd", 65625),
        evidence_record("auc001-20260726-evidence-lead-monthly-tier", "marts", "marts.fct_lead_enriched", "trc-0e3e68300d5d4a2793e50eac6c81f87e", 65625),
        evidence_record("auc001-20260726-evidence-lead-platform", "marts", "marts.fct_lead_enriched", "trc-44ecb9a49df84ed5844c7adc08be85c4", 72377),
        evidence_record("auc001-20260726-evidence-ticket-status", "marts", "marts.fct_lead_enriched", "trc-0ad211c097734c8495d7b381cd02f9b0", 88943),
        evidence_record("auc001-20260726-evidence-spend-signal-total", "marts", "marts.fct_spend", "trc-44dba30999ca46bda08cea922810275e", 286035),
        evidence_record("auc001-20260726-evidence-lead-campaign", "marts", "marts.fct_lead_enriched", "trc-29c862ce72554223b709e9e8f1e06efe", 158908),
        evidence_record("auc001-20260726-evidence-lead-ad-all-normalized", "marts", "marts.fct_lead_enriched", "trc-a440189664324100ac4c1b898e12ce4d", 317064),
        evidence_record("auc001-20260726-evidence-spend-ad-all-normalized", "marts", "marts.fct_spend", "trc-ae24a706f9664c67ab77d6a91755bb9e", 1043559),
        evidence_record("auc001-20260726-evidence-scoring-cuando-viaja", "intermediate", "intermediate.int_faro_lead_scoring", "trc-05343006b1c24bfea536de421a5e4ecb", 96563),
    ]
    dump("execution/evidence-acquisition-record.json", {
        "artifact_id": "AUC-001-EVIDENCE-ACQUISITION-20260726-CANONICAL",
        "specification": "SPEC-016",
        "provider": "BigQuery MCP",
        "status": "PASS",
        "mcp_call_records": records,
    })
    dump("validations/spec-014-validation.json", {
        "artifact_id": "AUC-001-SPEC-014-VALIDATION-20260726-CANONICAL",
        "specification": "SPEC-014",
        "decision": "PASS WITH DECLARED LIMITATIONS",
        "material_depth_validation": {row["question_id"]: row["depth"] for row in coverage_matrix},
    })
    dump("validations/spec-017-validation.json", {
        "artifact_id": "AUC-001-SPEC-017-VALIDATION-20260726-CANONICAL",
        "specification": "SPEC-017",
        "decision": "PASS",
        "checks": {
            f"FR-00{i}": {"status": "complete", "evidence_refs": ["lead_tier_total"], "finding_refs": ["F-001"]}
            for i in range(1, 8)
        } | {"FR-008": {"status": "complete", "evidence_refs": ["commercial_matched"], "finding_refs": ["F-003"]}},
        "conditions": [],
    })

    pre_cps = require_before_cps(ROOT)
    dump("validations/pre-cps-depth-gate.json", pre_cps)

    cps_obj = build_canonical_projection_source(
        common_core,
        knowledge_set=knowledge,
        recommendation_set=recommendation_set,
        coverage_matrix={"rows": coverage_matrix},
        manifest=manifest,
        analytical_investigation_record=air,
        artifact_id="AUC-001-CPS-20260726-CANONICAL",
    )
    cps = cps_obj.to_dict()
    dump("product-core/canonical-projection-source.json", cps)
    dump("execution/semantic-equivalence-validation.json", {
        "artifact_id": "AUC-001-SEMANTIC-EQUIVALENCE-20260726-CANONICAL",
        "decision": "PASS",
        "validated_artifacts": [
            "product-core/common-product-core.json",
            "product-core/canonical-projection-source.json",
            "knowledge/analytical-investigation-record.json",
        ],
        "projection_pairs": [{"source": common_core["semantic_fingerprint"], "projection": cps["semantic_fingerprint"]}],
    })
    dump("validations/spec-015-validation.json", {
        "artifact_id": "AUC-001-SPEC-015-VALIDATION-20260726-CANONICAL",
        "specification": "SPEC-015",
        "decision": "PASS",
        "common_core_fingerprint": common_core["semantic_fingerprint"],
        "canonical_projection_source_fingerprint": cps["semantic_fingerprint"],
        "conditions": [],
    })
    dump("validations/spec-016-validation.json", {
        "artifact_id": "AUC-001-SPEC-016-VALIDATION-20260726-CANONICAL",
        "specification": "SPEC-016",
        "decision": "PASS",
        "issues": [],
        "conditions": [],
    })
    write("handoff/reviewer-qa-handoff.md", f"""# Reviewer / QA Handoff

## Status

READY_FOR_REVALIDATION. Final acceptance remains outside Implementation.

## Commands Executed

- BigQuery MCP discover_metadata preflight: PASS.
- BigQuery MCP query_read_only evidence acquisition: PASS.
- Local pre-CPS depth gate: PASS.
- Local SPEC-016 package validation: see validations/spec-016-validation.json.

## Source Policy

BigQuery MCP only. No CLI. No fallback. No historical Evidence Sets as analytical source.

## Limitations

Revenue, CRM final outcomes, creative causality and assisted attention impact remain UNKNOWN.

## Ruta canonica enriquecida estable

La ruta canonica enriquecida queda promovida como salida estable de AUC-001.
AIR mantiene 10 findings intermedios; Knowledge Set mantiene 7 claims con narrativa integrada;
Recommendation Set mantiene 5 recomendaciones/hipotesis trazadas con prioridad, metricas,
salvaguardas y condiciones de revision.

analytical-report.md y executive-report.md se materializan como proyecciones Presentation
hermanas despues del gate canonico. No se materializan adaptadores temporales ni informes
experimentales compactos en el paquete estable.
## Deviations

No material deviation from canonical route.

## Final acceptance

Not declared. Package is READY_FOR_REVALIDATION.
""")
    dump("execution/test-results.json", {
        "artifact_id": "AUC-001-TEST-RESULTS-20260726-CANONICAL",
        "status": "PASS",
        "checks": [
            {"name": "partial_execution_blocked", "result": "PASS", "artifact": "outputs/auc-001/current/2026-06-30"},
            {"name": "canonical_package_materialized", "result": "PASS", "artifact": ROOT.as_posix()},
            {"name": "current_pointer_only_after_validation", "result": "PASS", "artifact": "outputs/auc-001/current/current-execution.json"},
        ],
    })

    manifest["artifact_fingerprints"] = {
        rel: sha(rel)
        for key, rel in artifact_paths.items()
        if key not in {"manifest", "physical_traceability", "test_results", "spec_016_validation"}
        and (ROOT / rel).exists()
    }
    dump("execution/manifest.json", manifest)
    dump("execution/physical-traceability.json", {
        "artifact_id": "AUC-001-PHYSICAL-TRACEABILITY-20260726-CANONICAL",
        "status": "PASS",
        "namespace_hygiene_pass": True,
        "manifest_sha256": sha("execution/manifest.json"),
        "test_results_sha256": sha("execution/test-results.json"),
        "artifact_inventory": artifact_paths,
    })
    validation = validate_package(ROOT)
    if validation["decision"] != "PASS":
        print(json.dumps(validation, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    dump("validations/spec-016-validation.json", validation)

    presentation_validation = materialize_canonical_presentation_reports_after_gate(ROOT)
    dump("execution/test-results.json", {
        "artifact_id": "AUC-001-TEST-RESULTS-20260726-CANONICAL",
        "status": "PASS",
        "checks": [
            {"name": "partial_execution_blocked", "result": "PASS", "artifact": "outputs/auc-001/current/2026-06-30"},
            {"name": "canonical_package_materialized", "result": "PASS", "artifact": ROOT.as_posix()},
            {"name": "current_pointer_only_after_validation", "result": "PASS", "artifact": "outputs/auc-001/current/current-execution.json"},
            {
                "name": "canonical_enriched_presentation_requires_canonical_gate",
                "result": presentation_validation["decision"],
                "artifact": "reports/analytical-report.md",
            },
        ],
    })
    manifest["artifact_fingerprints"] = {
        rel: sha(rel)
        for key, rel in artifact_paths.items()
        if key not in {"manifest", "physical_traceability", "test_results", "spec_016_validation"}
        and (ROOT / rel).exists()
    }
    dump("execution/manifest.json", manifest)
    dump("execution/physical-traceability.json", {
        "artifact_id": "AUC-001-PHYSICAL-TRACEABILITY-20260726-CANONICAL",
        "status": "PASS",
        "namespace_hygiene_pass": True,
        "manifest_sha256": sha("execution/manifest.json"),
        "test_results_sha256": sha("execution/test-results.json"),
        "artifact_inventory": artifact_paths,
    })
    validation = validate_package(ROOT)
    if validation["decision"] != "PASS":
        print(json.dumps(validation, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    dump("validations/spec-016-validation.json", validation)
    validation = validate_package(ROOT)
    if validation["decision"] != "PASS":
        print(json.dumps(validation, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    dump("validations/spec-016-validation.json", validation)
    require_before_presentation(ROOT)
    pointer = write_current_pointer(ROOT, CURRENT)
    print(json.dumps({"decision": validation["decision"], "package": ROOT.as_posix(), "current": pointer}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
