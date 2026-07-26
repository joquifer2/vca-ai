"""AUC-001 SPEC-016 operational acceptance package helpers.

This module validates the physical and operational package contract. It does
not call BigQuery, acquire evidence, modify historical outputs, or interpret
analytical content.
"""

from __future__ import annotations

import hashlib
import json
import os

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from tools.auc_001_canonical_cost_quality_model import STRATEGIC_CONTEXT_CONSTRAINTS as DEFAULT_STRATEGIC_CONTEXT_CONSTRAINTS
from tools.auc_001_analytical_product_contract import (
    QUESTION_DEFINITIONS,
    VALID_PRODUCT_COVERAGE_STATES,
    analytical_investigation_findings,
    validate_analytical_investigation_record,
    validate_canonical_projection_source,
    validate_coverage_matrix,
    validate_knowledge_item,
    validate_phase09_material_depth,
    validate_recommendation,
    validate_spec_017_validation,
)


SPECIFICATION = "SPEC-016"
CONTRACT_ID = "AUC-001-OPERATIONAL-ACCEPTANCE-PACKAGE-CONTRACT"
CONTRACT_VERSION = "spec-016.v1"
SCHEMA_FAMILY = "auc_001_operational_acceptance_package"
SCHEMA_VERSION = "auc_001_operational_acceptance_package.v1"

AUTHORIZED_PROJECT_ID = "datamart-vca-494114"
AUTHORIZED_MAX_BYTES_BILLED = 1073741824
ALLOWED_DATASETS = {"intermediate", "marts"}
ALLOWED_TABLES = {
    "intermediate.int_faro_lead_scoring",
    "marts.fct_lead_enriched",
    "marts.fct_spend",
    "marts.dim_campaign_signal",
}
EXECUTION_CONTEXT_FIELDS = {"project_id", "dataset_id", "max_bytes_billed"}
RECONCILIATION_STATES = {"matched", "lead_only", "spend_only"}
REQUIRED_STRATEGIC_CONTEXT_SOURCE = DEFAULT_STRATEGIC_CONTEXT_CONSTRAINTS.get("source_artifact")
REQUIRED_STRATEGIC_CONTEXT_LAYERS = set(DEFAULT_STRATEGIC_CONTEXT_CONSTRAINTS.get("layers", {}))
REQUIRED_STRATEGIC_CONTEXT_TRACEABILITY = (DEFAULT_STRATEGIC_CONTEXT_CONSTRAINTS.get("global_rules") or {}).get("required_traceability")

REQUIRED_PACKAGE_ROLES = {
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
    "common_product_core": "product-core/common-product-core.json",
    "canonical_projection_source": "product-core/canonical-projection-source.json",
    "spec_014_validation": "validations/spec-014-validation.json",
    "spec_015_validation": "validations/spec-015-validation.json",
    "spec_016_validation": "validations/spec-016-validation.json",
    "spec_017_validation": "validations/spec-017-validation.json",
    "handoff": "handoff/reviewer-qa-handoff.md",
}

REQUIRED_MCP_RECORD_FIELDS = {
    "call_type",
    "execution_context",
    "dataset",
    "tables",
    "period",
    "filters",
    "granularity",
    "dry_run_and_cost_control",
    "result",
    "request_id",
    "trace_reference",
    "bytes_processed",
    "used_as_evidence",
}


@dataclass(frozen=True)
class PackageIssue:
    code: str
    severity: str
    message: str
    artifact: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "severity": self.severity,
            "message": self.message,
            "artifact": self.artifact,
        }


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_json_if_exists(path: Path) -> dict[str, Any]:
    return read_json(path) if path.exists() else {}


def stable_json_hash(payload: Any) -> str:
    text = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def posix_rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def as_records(record_payload: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    value = record_payload.get("mcp_call_records")
    if value is None:
        value = record_payload.get("query_records")
    if isinstance(value, list):
        return [item for item in value if isinstance(item, Mapping)]
    return []


def validate_execution_context(context: Mapping[str, Any], dataset: str, artifact: str) -> list[PackageIssue]:
    issues: list[PackageIssue] = []
    keys = set(context)
    if keys != EXECUTION_CONTEXT_FIELDS:
        issues.append(PackageIssue("EXECUTION_CONTEXT_NOT_CLOSED", "blocking", "execution_context must contain only project_id, dataset_id and max_bytes_billed", artifact))
    if context.get("project_id") != AUTHORIZED_PROJECT_ID:
        issues.append(PackageIssue("EXECUTION_CONTEXT_PROJECT_INVALID", "blocking", "execution_context project_id is not authorized", artifact))
    if context.get("dataset_id") != dataset:
        issues.append(PackageIssue("EXECUTION_CONTEXT_DATASET_MISMATCH", "blocking", "execution_context dataset_id must match record dataset", artifact))
    if context.get("dataset_id") not in ALLOWED_DATASETS:
        issues.append(PackageIssue("EXECUTION_CONTEXT_DATASET_INVALID", "blocking", "execution_context dataset_id is not allowed", artifact))
    if context.get("max_bytes_billed") != AUTHORIZED_MAX_BYTES_BILLED:
        issues.append(PackageIssue("EXECUTION_CONTEXT_COST_LIMIT_INVALID", "blocking", "execution_context max_bytes_billed is not canonical", artifact))
    return issues


def validate_mcp_preflight_record(preflight: Mapping[str, Any], artifact: str = "mcp-preflight-record.json") -> list[PackageIssue]:
    issues: list[PackageIssue] = []
    if preflight.get("specification") != SPECIFICATION:
        issues.append(PackageIssue("PREFLIGHT_SPEC_INVALID", "blocking", "preflight must declare SPEC-016", artifact))
    if preflight.get("status") != "PASS":
        issues.append(PackageIssue("PREFLIGHT_NOT_PASS", "blocking", "MCP preflight must pass before evidence acquisition", artifact))
    if preflight.get("provider") != "BigQuery MCP":
        issues.append(PackageIssue("PREFLIGHT_PROVIDER_INVALID", "blocking", "provider must be BigQuery MCP", artifact))
    if preflight.get("acquisition_strategy") != "independent_table_queries_with_local_reconciliation":
        issues.append(PackageIssue("PREFLIGHT_STRATEGY_INVALID", "blocking", "AUC-001 acquisition strategy must use independent table queries with local reconciliation", artifact))
    if preflight.get("multi_table_mcp_queries_allowed_as_evidence") is not False:
        issues.append(PackageIssue("PREFLIGHT_MULTITABLE_POLICY_INVALID", "blocking", "multi-table MCP queries must be disallowed as Evidence", artifact))

    planned_tables = set(preflight.get("planned_tables") or [])
    missing_tables = sorted(planned_tables - ALLOWED_TABLES)
    if missing_tables:
        issues.append(PackageIssue("PREFLIGHT_TABLE_NOT_ALLOWLISTED", "blocking", f"planned table is not allowlisted: {missing_tables}", artifact))

    for name, context in dict(preflight.get("execution_contexts") or {}).items():
        if not isinstance(context, Mapping):
            issues.append(PackageIssue("PREFLIGHT_CONTEXT_INVALID", "blocking", f"execution context is not an object: {name}", artifact))
            continue
        dataset = str(context.get("dataset_id") or name)
        issues.extend(validate_execution_context(context, dataset, artifact))

    grain = dict(preflight.get("spec_014_grain_readiness") or {})
    blocking_questions = [qid for qid, state in grain.items() if state == "blocked"]
    if blocking_questions:
        issues.append(PackageIssue("PREFLIGHT_SPEC014_GRAIN_BLOCKED", "blocking", f"planned grain blocks SPEC-014 questions: {blocking_questions}", artifact))

    states = set(preflight.get("reconciliation_states_preserved") or [])
    if not RECONCILIATION_STATES <= states:
        issues.append(PackageIssue("PREFLIGHT_RECONCILIATION_STATES_MISSING", "blocking", "preflight must preserve matched, lead_only and spend_only", artifact))
    return issues


def validate_mcp_records(record_payload: Mapping[str, Any], artifact: str = "evidence-acquisition-record.json") -> list[PackageIssue]:
    issues: list[PackageIssue] = []
    records = as_records(record_payload)
    if not records:
        issues.append(PackageIssue("MCP_RECORDS_MISSING", "blocking", "evidence acquisition record must contain MCP call records", artifact))
        return issues

    for index, record in enumerate(records):
        record_artifact = f"{artifact}#{index}"
        missing = sorted(REQUIRED_MCP_RECORD_FIELDS - set(record))
        if record.get("call_type") == "discover_metadata":
            missing = [field for field in missing if field not in {"sql", "period", "filters", "granularity", "bytes_processed"}]
        elif "sql" not in record:
            missing.append("sql")
        if missing:
            issues.append(PackageIssue("MCP_RECORD_FIELD_MISSING", "blocking", f"MCP record missing fields: {missing}", record_artifact))

        context = record.get("execution_context")
        if isinstance(context, Mapping):
            dataset = str(record.get("dataset") or context.get("dataset_id") or "")
            issues.extend(validate_execution_context(context, dataset, record_artifact))
        else:
            issues.append(PackageIssue("MCP_RECORD_CONTEXT_INVALID", "blocking", "MCP record execution_context must be an object", record_artifact))

        for table in record.get("tables") or []:
            if table not in ALLOWED_TABLES:
                issues.append(PackageIssue("MCP_RECORD_TABLE_NOT_ALLOWLISTED", "blocking", f"MCP record table is not allowlisted: {table}", record_artifact))

        result = dict(record.get("result") or {})
        status = result.get("status")
        used = record.get("used_as_evidence")
        tables = list(record.get("tables") or [])
        if status in {"rejected", "discarded", "error"} and used is not False:
            issues.append(PackageIssue("REJECTED_OR_DISCARDED_USED_AS_EVIDENCE", "blocking", "rejected, discarded or error records cannot be used as Evidence", record_artifact))
        if len(tables) > 1 and used is not False:
            issues.append(PackageIssue("MULTITABLE_QUERY_USED_AS_EVIDENCE", "blocking", "multi-table MCP records cannot be used as Evidence for AUC-001", record_artifact))
        if used is False and not (record.get("discard_reason") or result.get("error_code") or result.get("error_reason")):
            issues.append(PackageIssue("NON_EVIDENCE_RECORD_WITHOUT_REASON", "blocking", "non-evidence MCP records must declare rejection or discard reason", record_artifact))

    successful_used = [item for item in records if dict(item.get("result") or {}).get("status") == "success" and item.get("used_as_evidence") is True]
    if not successful_used:
        issues.append(PackageIssue("NO_SUCCESSFUL_EVIDENCE_RECORDS", "blocking", "at least one successful MCP record must be used as Evidence in a non-blocked package", artifact))
    return issues


def validate_manifest(manifest: Mapping[str, Any], package_root: Path) -> list[PackageIssue]:
    issues: list[PackageIssue] = []
    if manifest.get("specification") != SPECIFICATION:
        issues.append(PackageIssue("MANIFEST_SPEC_INVALID", "blocking", "manifest must declare SPEC-016", "manifest.json"))
    if manifest.get("status") == "FINAL_ACCEPTED" and not manifest.get("final_acceptance_reference"):
        issues.append(PackageIssue("FINAL_ACCEPTED_WITHOUT_QA_REFERENCE", "blocking", "FINAL_ACCEPTED requires a QA final acceptance reference", "manifest.json"))
    if manifest.get("status") not in {"READY_FOR_REVALIDATION", "BLOCKED", "REJECTED_BY_REVIEW", "FINAL_ACCEPTED"}:
        issues.append(PackageIssue("MANIFEST_STATUS_INVALID", "blocking", "manifest status is not valid for SPEC-016", "manifest.json"))

    source_policy = dict(manifest.get("source_policy") or {})
    if source_policy.get("bigquery_mcp_only") is not True or source_policy.get("cli_used") is not False or source_policy.get("fallback_used") is not False:
        issues.append(PackageIssue("SOURCE_POLICY_INVALID", "blocking", "source policy must be MCP-only with no CLI or fallback", "manifest.json"))
    if manifest.get("acceptance_final_declared_by_implementation") is not False:
        issues.append(PackageIssue("IMPLEMENTATION_DECLARED_FINAL_ACCEPTANCE", "blocking", "Implementation package cannot declare final acceptance", "manifest.json"))

    paths = dict(manifest.get("artifact_paths") or {})
    for role, default_path in REQUIRED_PACKAGE_ROLES.items():
        rel = paths.get(role, default_path)
        if not (package_root / rel).exists():
            issues.append(PackageIssue("PACKAGE_ROLE_MISSING", "blocking", f"required package role missing: {role}", rel))

    fingerprints = dict(manifest.get("artifact_fingerprints") or {})
    for rel, expected in fingerprints.items():
        path = package_root / rel
        if not path.exists():
            issues.append(PackageIssue("FINGERPRINT_PATH_MISSING", "blocking", "fingerprinted path is missing", rel))
            continue
        actual = file_sha256(path)
        if actual != expected:
            issues.append(PackageIssue("FINGERPRINT_MISMATCH", "blocking", "artifact fingerprint does not match file", rel))
    return issues


def validate_physical_traceability(traceability: Mapping[str, Any], package_root: Path) -> list[PackageIssue]:
    issues: list[PackageIssue] = []
    manifest_path = package_root / "execution/manifest.json"
    test_results_path = package_root / "execution/test-results.json"
    if traceability.get("manifest_sha256") != file_sha256(manifest_path):
        issues.append(PackageIssue("PHYSICAL_MANIFEST_HASH_MISMATCH", "blocking", "physical traceability manifest hash does not match", "physical-traceability.json"))
    if traceability.get("test_results_sha256") != file_sha256(test_results_path):
        issues.append(PackageIssue("PHYSICAL_TEST_RESULTS_HASH_MISMATCH", "blocking", "physical traceability test-results hash does not match", "physical-traceability.json"))
    if traceability.get("namespace_hygiene_pass") is not True:
        issues.append(PackageIssue("PHYSICAL_NAMESPACE_HYGIENE_NOT_PASS", "blocking", "physical traceability must declare namespace hygiene pass", "physical-traceability.json"))
    return issues


def find_namespace_hygiene_issues(package_root: Path) -> list[PackageIssue]:
    issues: list[PackageIssue] = []
    for root, dirs, files in os.walk(package_root):
        root_path = Path(root)
        for dirname in dirs:
            if dirname == "__pycache__":
                issues.append(PackageIssue("NAMESPACE_PYCACHE_PRESENT", "blocking", "__pycache__ is not allowed in output namespace", posix_rel(root_path / dirname, package_root)))
        for filename in files:
            lower = filename.lower()
            if lower.endswith(".pyc") or lower.endswith(".tmp") or lower.endswith(".log"):
                issues.append(PackageIssue("NAMESPACE_TEMPORARY_FILE_PRESENT", "blocking", "temporary, log or .pyc file is not allowed in output namespace", posix_rel(root_path / filename, package_root)))
    return issues


def validate_handoff_text(text: str, artifact: str = "reviewer-qa-handoff.md") -> list[PackageIssue]:
    required_markers = (
        "## Commands Executed",
        "READY_FOR_REVALIDATION",
        "BigQuery MCP",
        "No CLI",
        "No fallback",
        "Limitations",
        "Deviations",
        "Final acceptance",
    )
    issues = []
    for marker in required_markers:
        if marker not in text:
            issues.append(PackageIssue("HANDOFF_MARKER_MISSING", "blocking", f"handoff missing marker: {marker}", artifact))
    return issues



def validate_strategic_context_traceability(
    payload: Mapping[str, Any],
    artifact: str = "canonical-projection-source.json",
) -> list[PackageIssue]:
    """Validate strategic-context transport for future use-case packages."""
    issues: list[PackageIssue] = []
    constraints = payload.get("strategic_context_constraints")
    if not isinstance(constraints, Mapping):
        issues.append(PackageIssue("STRATEGIC_CONTEXT_CONSTRAINTS_MISSING", "blocking", "artifact must carry strategic_context_constraints", artifact))
        return issues
    if constraints.get("source_artifact") != REQUIRED_STRATEGIC_CONTEXT_SOURCE:
        issues.append(PackageIssue("STRATEGIC_CONTEXT_SOURCE_INVALID", "blocking", "strategic context must trace to the profile-declared canonical source", artifact))
    if not constraints.get("source_refs"):
        issues.append(PackageIssue("STRATEGIC_CONTEXT_REFS_MISSING", "blocking", "strategic context must preserve CCD source refs", artifact))
    layers = constraints.get("layers")
    if not isinstance(layers, Mapping):
        issues.append(PackageIssue("STRATEGIC_CONTEXT_LAYERS_MISSING", "blocking", "strategic context must declare profile layers", artifact))
        return issues
    missing_layers = sorted(REQUIRED_STRATEGIC_CONTEXT_LAYERS - set(layers))
    if missing_layers:
        issues.append(PackageIssue("STRATEGIC_CONTEXT_LAYER_MISSING", "blocking", f"strategic context missing profile layers: {missing_layers}", artifact))
    global_rules = constraints.get("global_rules")
    if not isinstance(global_rules, Mapping) or global_rules.get("required_traceability") != REQUIRED_STRATEGIC_CONTEXT_TRACEABILITY:
        issues.append(PackageIssue("STRATEGIC_CONTEXT_TRACEABILITY_RULE_MISSING", "blocking", "context-dependent interpretation must require the profile-declared traceability field", artifact))
    return issues

def product_issues_to_package_issues(product_issues: list[Any], artifact: str) -> list[PackageIssue]:
    converted: list[PackageIssue] = []
    for issue in product_issues:
        payload = issue.to_dict() if hasattr(issue, "to_dict") else dict(issue)
        converted.append(PackageIssue(str(payload.get("code")), str(payload.get("severity") or "blocking"), str(payload.get("message")), str(payload.get("artifact") or artifact)))
    return converted


def artifact_path(root: Path, manifest: Mapping[str, Any], role: str) -> Path:
    rel = dict(manifest.get("artifact_paths") or {}).get(role) or REQUIRED_PACKAGE_ROLES[role]
    return root / rel


def artifact_ref(path: Path, root: Path, role: str) -> str:
    return posix_rel(path, root) if path.exists() else REQUIRED_PACKAGE_ROLES[role]


def material_condition_is_blocking(entry: Mapping[str, Any]) -> bool:
    state = str(entry.get("severity") or entry.get("status") or entry.get("decision") or "").lower()
    return state in {"blocking", "blocked", "fail", "failed"} or entry.get("blocking") is True


def material_condition_entries(payload: Mapping[str, Any], *field_names: str) -> list[Mapping[str, Any]]:
    entries: list[Mapping[str, Any]] = []
    for field_name in field_names:
        value = payload.get(field_name) or []
        if isinstance(value, Mapping):
            value = value.values()
        if isinstance(value, (str, bytes)):
            continue
        try:
            iterator = iter(value)
        except TypeError:
            continue
        entries.extend(item for item in iterator if isinstance(item, Mapping))
    return entries


def canonical_spec014_question_ids() -> set[str]:
    return {definition.question_id for definition in QUESTION_DEFINITIONS}

def expected_spec014_question_ids(*payloads: Mapping[str, Any]) -> set[str]:
    question_ids: set[str] = canonical_spec014_question_ids()
    for payload in payloads:
        if not isinstance(payload, Mapping):
            continue
        states = payload.get("coverage_states")
        if isinstance(states, Mapping):
            question_ids.update(str(key) for key in states)
        matrix = payload.get("coverage_matrix") or payload.get("rows")
        if isinstance(matrix, Mapping):
            matrix = matrix.get("rows")
        if isinstance(matrix, list):
            for row in matrix:
                if isinstance(row, Mapping) and row.get("question_id"):
                    question_ids.add(str(row.get("question_id")))
    return question_ids


def validate_common_product_core_payload(payload: Mapping[str, Any], artifact: str = "common-product-core.json") -> list[PackageIssue]:
    issues: list[PackageIssue] = []
    required = ("period", "scope", "sources", "evidence_refs", "canonical_metrics", "knowledge_claims", "recommendations", "limitations", "unknowns", "strategic_context_constraints")
    for field_name in required:
        if not payload.get(field_name):
            issues.append(PackageIssue("COMMON_CORE_FIELD_MISSING", "blocking", f"Common Product Core missing field: {field_name}", artifact))
    coverage_states = payload.get("coverage_states")
    coverage_matrix = payload.get("coverage_matrix")
    if isinstance(coverage_matrix, Mapping):
        coverage_matrix = coverage_matrix.get("rows")
    if isinstance(coverage_matrix, list):
        issues.extend(product_issues_to_package_issues(validate_coverage_matrix(coverage_matrix), artifact))
    elif isinstance(coverage_states, Mapping) and coverage_states:
        for question_id, state in coverage_states.items():
            if state not in VALID_PRODUCT_COVERAGE_STATES:
                issues.append(PackageIssue("COMMON_CORE_COVERAGE_STATE_INVALID", "blocking", f"Common Product Core invalid coverage state for {question_id}: {state}", artifact))
    else:
        issues.append(PackageIssue("COMMON_CORE_COVERAGE_MISSING", "blocking", "Common Product Core must carry coverage matrix or coverage states", artifact))
    for index, item in enumerate(payload.get("knowledge_claims") or []):
        if not isinstance(item, Mapping):
            issues.append(PackageIssue("COMMON_CORE_KNOWLEDGE_NOT_STRUCTURED", "blocking", "Common Product Core knowledge claims must be structured Knowledge items", f"{artifact}#knowledge_claims[{index}]"))
            continue
        issues.extend(product_issues_to_package_issues(validate_knowledge_item(item), f"{artifact}#knowledge_claims[{index}]"))
    for index, item in enumerate(payload.get("recommendations") or []):
        if not isinstance(item, Mapping):
            issues.append(PackageIssue("COMMON_CORE_RECOMMENDATION_NOT_STRUCTURED", "blocking", "Common Product Core recommendations must be structured Recommendation items", f"{artifact}#recommendations[{index}]"))
            continue
        issues.extend(product_issues_to_package_issues(validate_recommendation(item), f"{artifact}#recommendations[{index}]"))
    issues.extend(validate_strategic_context_traceability(payload, artifact))
    return issues


def validate_spec015_validation(payload: Mapping[str, Any], cps_issues: list[PackageIssue], artifact: str = "spec-015-validation.json") -> list[PackageIssue]:
    issues: list[PackageIssue] = []
    if payload.get("specification") != "SPEC-015":
        issues.append(PackageIssue("SPEC015_SPECIFICATION_INVALID", "blocking", "SPEC-015 validation must declare SPEC-015", artifact))
    if payload.get("decision") not in {"PASS", "PASS WITH CONDITIONS"} and payload.get("status") not in {"PASS", "PASS WITH CONDITIONS"}:
        issues.append(PackageIssue("SPEC015_VALIDATION_NOT_PASS", "blocking", "SPEC-015 validation must pass before Presentation", artifact))
    for entry in material_condition_entries(payload, "conditions", "issues", "open_conditions", "blocking_conditions"):
        if material_condition_is_blocking(entry):
            issues.append(PackageIssue("SPEC015_BLOCKING_CONDITION_OPEN", "blocking", "SPEC-015 validation cannot pass with blocking conditions", artifact))
    if any(issue.severity == "blocking" for issue in cps_issues):
        issues.append(PackageIssue("SPEC015_CPS_CONTENT_INVALID", "blocking", "SPEC-015 validation cannot pass while CPS content has blocking issues", artifact))
    return issues


def validate_semantic_equivalence_validation(payload: Mapping[str, Any], artifact: str = "semantic-equivalence-validation.json") -> list[PackageIssue]:
    issues: list[PackageIssue] = []
    decision = payload.get("decision") or payload.get("status")
    if decision not in {"PASS", "PASS WITH CONDITIONS"}:
        issues.append(PackageIssue("SEMANTIC_EQUIVALENCE_NOT_PASS", "blocking", "semantic equivalence validation must pass before Presentation", artifact))
    if not payload.get("source_artifacts") and not payload.get("validated_artifacts") and not payload.get("projection_pairs"):
        issues.append(PackageIssue("SEMANTIC_EQUIVALENCE_TRACE_MISSING", "blocking", "semantic equivalence validation must declare validated artifacts", artifact))
    for entry in material_condition_entries(payload, "conditions", "issues", "open_conditions", "blocking_conditions"):
        if material_condition_is_blocking(entry):
            issues.append(PackageIssue("SEMANTIC_EQUIVALENCE_BLOCKING_CONDITION_OPEN", "blocking", "semantic equivalence cannot pass with blocking conditions", artifact))
    return issues


def validate_spec016_validation(payload: Mapping[str, Any], artifact: str = "spec-016-validation.json") -> list[PackageIssue]:
    issues: list[PackageIssue] = []
    if payload.get("specification") != "SPEC-016":
        issues.append(PackageIssue("SPEC016_SPECIFICATION_INVALID", "blocking", "SPEC-016 validation artifact must declare SPEC-016", artifact))
    if payload.get("decision") not in {"PASS", "PASS WITH CONDITIONS", "READY_FOR_REVALIDATION"} and payload.get("status") not in {"PASS", "PASS WITH CONDITIONS", "READY_FOR_REVALIDATION"}:
        issues.append(PackageIssue("SPEC016_VALIDATION_NOT_PASS", "blocking", "SPEC-016 validation artifact must declare local validation success", artifact))
    for entry in material_condition_entries(payload, "conditions", "issues", "open_conditions", "blocking_conditions"):
        if material_condition_is_blocking(entry):
            issues.append(PackageIssue("SPEC016_BLOCKING_CONDITION_OPEN", "blocking", "SPEC-016 validation cannot pass with blocking conditions", artifact))
    return issues


def validate_spec014_material_validation(
    payload: Mapping[str, Any],
    artifact: str = "spec-014-validation.json",
    expected_question_ids: set[str] | None = None,
) -> list[PackageIssue]:
    issues: list[PackageIssue] = []
    if payload.get("specification") != "SPEC-014":
        issues.append(PackageIssue("SPEC014_SPECIFICATION_INVALID", "blocking", "SPEC-014 validation must declare SPEC-014", artifact))
    if payload.get("decision") not in {"PASS", "PASS WITH CONDITIONS", "PASS WITH DECLARED LIMITATIONS"}:
        issues.append(PackageIssue("SPEC014_VALIDATION_NOT_PASS", "blocking", "SPEC-014 validation must pass with material depth checks", artifact))
    material = payload.get("material_depth_validation") or payload.get("question_depth_checks") or payload.get("coverage_question_checks")
    if not isinstance(material, Mapping) or not material:
        issues.append(PackageIssue("SPEC014_MATERIAL_DEPTH_MISSING", "blocking", "SPEC-014 validation must evaluate depth by analytical question", artifact))
        return issues
    expected_question_ids = expected_question_ids if expected_question_ids is not None else canonical_spec014_question_ids()
    missing = sorted(expected_question_ids - {str(question_id) for question_id in material})
    for question_id in missing:
        issues.append(PackageIssue("SPEC014_QUESTION_MISSING", "blocking", f"SPEC-014 validation missing analytical question: {question_id}", artifact))
    blocked = []
    for question_id, check in material.items():
        if not isinstance(check, Mapping):
            issues.append(PackageIssue("SPEC014_QUESTION_CHECK_INVALID", "blocking", f"SPEC-014 question check is not structured: {question_id}", artifact))
            continue
        state = check.get("coverage_state") or check.get("status")
        if state == "blocked" or check.get("decision") == "FAIL":
            blocked.append(str(question_id))
        material_fields = ("evidence", "comparison", "interpretation", "business_implication", "limitation_or_uncertainty", "conclusion_or_hypothesis")
        if state in {"complete", "partial"}:
            for field_name in material_fields:
                if not check.get(field_name):
                    issues.append(PackageIssue("SPEC014_MATERIAL_DEPTH_FIELD_MISSING", "blocking", f"Question lacks material depth field {field_name}: {question_id}", artifact))
        elif state in {"not_available", "not_applicable", "UNKNOWN"}:
            if not (check.get("limitation_or_uncertainty") or check.get("insufficiency_reason") or check.get("reason")):
                issues.append(PackageIssue("SPEC014_INSUFFICIENCY_REASON_MISSING", "blocking", f"Question with insufficient coverage must declare reason: {question_id}", artifact))
        else:
            issues.append(PackageIssue("SPEC014_QUESTION_STATUS_INVALID", "blocking", f"SPEC-014 question status invalid: {question_id}", artifact))
    if blocked:
        issues.append(PackageIssue("SPEC014_QUESTION_BLOCKED", "blocking", f"SPEC-014 blocked questions prevent CPS/Presentation: {blocked}", artifact))
    return issues


def validate_cps_air_physical_link(cps: Mapping[str, Any], air: Mapping[str, Any], air_artifact: str, cps_artifact: str) -> list[PackageIssue]:
    issues: list[PackageIssue] = []
    if not isinstance(cps, Mapping) or not isinstance(air, Mapping) or not cps or not air:
        return issues

    air_support_by_id = {
        str(item.get("finding_id")): set(str(ref) for ref in (item.get("support") or item.get("evidence_refs") or []))
        for item in analytical_investigation_findings(air)
        if item.get("finding_id")
    }
    cps_signals = dict(cps.get("integrated_view") or {}).get("signals") or []
    cps_support_by_id = {
        str(item.get("finding_id")): set(str(ref) for ref in (item.get("support") or []))
        for item in cps_signals
        if isinstance(item, Mapping) and item.get("finding_id")
    }
    air_ids = set(air_support_by_id)
    cps_ids = set(cps_support_by_id)

    missing_from_cps = sorted(air_ids - cps_ids)
    extra_in_cps = sorted(cps_ids - air_ids)
    if missing_from_cps:
        issues.append(PackageIssue("CPS_AIR_FINDING_NOT_PRESERVED", "blocking", f"CPS integrated view omits physical AIR findings: {missing_from_cps}", cps_artifact))
    if extra_in_cps:
        issues.append(PackageIssue("CPS_AIR_FINDING_NOT_PHYSICAL", "blocking", f"CPS integrated view contains findings absent from physical AIR: {extra_in_cps}", cps_artifact))
    for finding_id in sorted(air_ids & cps_ids):
        if air_support_by_id[finding_id] != cps_support_by_id[finding_id]:
            issues.append(PackageIssue("CPS_AIR_SUPPORT_MISMATCH", "blocking", f"CPS support does not match physical AIR support for finding: {finding_id}", cps_artifact))

    source_artifacts = dict(cps.get("source_artifacts") or {})
    if source_artifacts.get("analytical_investigation_record") != air_artifact:
        issues.append(PackageIssue("CPS_AIR_SOURCE_ARTIFACT_MISMATCH", "blocking", "CPS must point to the physical AIR artifact it preserves", cps_artifact))
    return issues

def evidence_reference_index(evidence_set: Mapping[str, Any]) -> set[str]:
    refs: set[str] = set()
    if evidence_set.get("artifact_id"):
        refs.add(str(evidence_set.get("artifact_id")))
    facts = evidence_set.get("facts")
    if isinstance(facts, Mapping):
        refs.update(str(key) for key in facts)
    for field_name in ("evidence", "records", "items", "metrics"):
        value = evidence_set.get(field_name)
        if isinstance(value, Mapping):
            value = value.values()
        if isinstance(value, list):
            for item in value:
                if isinstance(item, Mapping):
                    for id_field in ("evidence_id", "id", "metric_id", "artifact_id"):
                        if item.get(id_field):
                            refs.add(str(item.get(id_field)))
    return refs


def validate_air_evidence_trace(air: Mapping[str, Any], evidence_set: Mapping[str, Any], artifact: str) -> list[PackageIssue]:
    issues: list[PackageIssue] = []
    evidence_refs = evidence_reference_index(evidence_set)
    if not evidence_refs:
        issues.append(PackageIssue("EVIDENCE_REFERENCE_INDEX_EMPTY", "blocking", "Evidence Set must expose stable references before AIR can be traced", artifact))
        return issues
    for finding in analytical_investigation_findings(air):
        finding_id = str(finding.get("finding_id") or artifact)
        support_refs = finding.get("support") or finding.get("evidence_refs") or []
        if isinstance(support_refs, (str, bytes)):
            support_refs = [support_refs]
        missing = sorted(str(ref) for ref in support_refs if str(ref) not in evidence_refs)
        if missing:
            issues.append(PackageIssue("AIR_FINDING_EVIDENCE_REF_MISSING", "blocking", f"AIR finding references Evidence not present in physical Evidence Set: {missing}", finding_id))
    return issues


def validate_pre_cps_depth_gate(package_root: str | Path) -> dict[str, Any]:
    root = Path(package_root)
    issues: list[PackageIssue] = []
    if not root.exists():
        issues.append(PackageIssue("PACKAGE_ROOT_MISSING", "blocking", "package root does not exist", str(root)))
        return validation_payload(root, issues)

    required_roles = (
        "manifest",
        "evidence_set",
        "knowledge_set",
        "analytical_investigation_record",
        "spec_014_validation",
        "spec_017_validation",
    )
    manifest_path = root / REQUIRED_PACKAGE_ROLES["manifest"]
    if not manifest_path.exists():
        for role in required_roles:
            rel = REQUIRED_PACKAGE_ROLES[role]
            if not (root / rel).exists():
                issues.append(PackageIssue("PRE_CPS_ROLE_MISSING", "blocking", f"pre-CPS depth gate role missing: {role}", rel))
        return validation_payload(root, issues)

    manifest = read_json(manifest_path)
    paths = {role: artifact_path(root, manifest, role) for role in required_roles}
    for role, path in paths.items():
        if not path.exists():
            issues.append(PackageIssue("PRE_CPS_ROLE_MISSING", "blocking", f"pre-CPS depth gate role missing: {role}", artifact_ref(path, root, role)))

    evidence_set = read_json(paths["evidence_set"]) if paths["evidence_set"].exists() else {}
    knowledge_set = read_json(paths["knowledge_set"]) if paths["knowledge_set"].exists() else {}
    air = read_json(paths["analytical_investigation_record"]) if paths["analytical_investigation_record"].exists() else {}
    spec014_validation = read_json(paths["spec_014_validation"]) if paths["spec_014_validation"].exists() else {}
    spec017_validation = read_json(paths["spec_017_validation"]) if paths["spec_017_validation"].exists() else {}

    issues.extend(product_issues_to_package_issues(validate_analytical_investigation_record(air), artifact_ref(paths["analytical_investigation_record"], root, "analytical_investigation_record")))
    issues.extend(validate_air_evidence_trace(air, evidence_set, artifact_ref(paths["analytical_investigation_record"], root, "analytical_investigation_record")))
    issues.extend(product_issues_to_package_issues(validate_phase09_material_depth(knowledge_set, air), artifact_ref(paths["knowledge_set"], root, "knowledge_set")))
    issues.extend(validate_spec014_material_validation(spec014_validation, artifact_ref(paths["spec_014_validation"], root, "spec_014_validation")))
    issues.extend(product_issues_to_package_issues(validate_spec_017_validation(spec017_validation), artifact_ref(paths["spec_017_validation"], root, "spec_017_validation")))
    return validation_payload(root, issues)

def validate_package(package_root: str | Path) -> dict[str, Any]:
    root = Path(package_root)
    issues: list[PackageIssue] = []
    if not root.exists():
        issues.append(PackageIssue("PACKAGE_ROOT_MISSING", "blocking", "package root does not exist", str(root)))
        return validation_payload(root, issues)

    issues.extend(find_namespace_hygiene_issues(root))

    manifest_path = root / REQUIRED_PACKAGE_ROLES["manifest"]
    if not manifest_path.exists():
        for role, rel in REQUIRED_PACKAGE_ROLES.items():
            if not (root / rel).exists():
                issues.append(PackageIssue("PACKAGE_ROLE_MISSING", "blocking", f"required package role missing: {role}", rel))
        return validation_payload(root, issues)

    manifest = read_json(manifest_path)
    traceability = read_json_if_exists(root / "execution/physical-traceability.json")
    preflight = read_json_if_exists(root / "execution/mcp-preflight-record.json")
    evidence_record = read_json_if_exists(root / "execution/evidence-acquisition-record.json")
    handoff_path = root / "handoff/reviewer-qa-handoff.md"
    handoff = handoff_path.read_text(encoding="utf-8") if handoff_path.exists() else ""

    issues.extend(validate_manifest(manifest, root))
    if traceability:
        issues.extend(validate_physical_traceability(traceability, root))
    if preflight:
        issues.extend(validate_mcp_preflight_record(preflight))
    if evidence_record:
        issues.extend(validate_mcp_records(evidence_record))
    if handoff:
        issues.extend(validate_handoff_text(handoff))

    paths = {role: artifact_path(root, manifest, role) for role in REQUIRED_PACKAGE_ROLES}
    knowledge_path = paths["knowledge_set"]
    air_path = paths["analytical_investigation_record"]
    coverage_path = paths.get("coverage_matrix")
    common_core_path = paths["common_product_core"]
    cps_path = paths["canonical_projection_source"]
    semantic_path = paths["semantic_equivalence_validation"]
    spec014_path = paths["spec_014_validation"]
    spec015_path = paths["spec_015_validation"]
    spec016_path = paths["spec_016_validation"]
    spec017_path = paths["spec_017_validation"]

    knowledge_set = read_json(knowledge_path) if knowledge_path.exists() else {}
    air = read_json(air_path) if air_path.exists() else {}
    coverage_matrix = read_json(coverage_path) if coverage_path and coverage_path.exists() else {}
    common_core = read_json(common_core_path) if common_core_path.exists() else {}
    cps = read_json(cps_path) if cps_path.exists() else {}
    semantic_validation = read_json(semantic_path) if semantic_path.exists() else {}
    spec014_validation = read_json(spec014_path) if spec014_path.exists() else {}
    spec015_validation = read_json(spec015_path) if spec015_path.exists() else {}
    spec016_validation = read_json(spec016_path) if spec016_path.exists() else {}
    spec017_validation = read_json(spec017_path) if spec017_path.exists() else {}

    expected_questions = expected_spec014_question_ids(coverage_matrix, common_core)
    air_artifact = artifact_ref(air_path, root, "analytical_investigation_record")
    cps_artifact = artifact_ref(cps_path, root, "canonical_projection_source")
    cps_content_issues = product_issues_to_package_issues(validate_canonical_projection_source(cps), cps_artifact) if cps else [PackageIssue("CPS_NOT_MATERIALIZED", "blocking", "Canonical Projection Source content is required before Presentation", REQUIRED_PACKAGE_ROLES["canonical_projection_source"])]

    issues.extend(product_issues_to_package_issues(validate_analytical_investigation_record(air), air_artifact))
    issues.extend(product_issues_to_package_issues(validate_phase09_material_depth(knowledge_set, air), artifact_ref(knowledge_path, root, "knowledge_set")))
    issues.extend(validate_common_product_core_payload(common_core, artifact_ref(common_core_path, root, "common_product_core")))
    issues.extend(cps_content_issues)
    issues.extend(validate_cps_air_physical_link(cps, air, air_artifact, cps_artifact))
    issues.extend(validate_semantic_equivalence_validation(semantic_validation, artifact_ref(semantic_path, root, "semantic_equivalence_validation")))
    issues.extend(validate_spec014_material_validation(spec014_validation, artifact_ref(spec014_path, root, "spec_014_validation"), expected_questions))
    issues.extend(validate_spec015_validation(spec015_validation, cps_content_issues, artifact_ref(spec015_path, root, "spec_015_validation")))
    issues.extend(validate_spec016_validation(spec016_validation, artifact_ref(spec016_path, root, "spec_016_validation")))
    issues.extend(product_issues_to_package_issues(validate_spec_017_validation(spec017_validation), artifact_ref(spec017_path, root, "spec_017_validation")))
    return validation_payload(root, issues)


def validation_payload(root: Path, issues: list[PackageIssue]) -> dict[str, Any]:
    blocking = [issue for issue in issues if issue.severity == "blocking"]
    return {
        "artifact_id": "AUC-001-SPEC-016-VALIDATION",
        "schema_family": SCHEMA_FAMILY,
        "schema_version": SCHEMA_VERSION,
        "specification": SPECIFICATION,
        "contract_id": CONTRACT_ID,
        "contract_version": CONTRACT_VERSION,
        "package_root": root.as_posix(),
        "decision": "PASS" if not blocking else "BLOCKED",
        "issues": [issue.to_dict() for issue in issues],
    }
