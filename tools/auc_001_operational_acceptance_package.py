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
    "recommendation_set": "recommendations/recommendation-set.json",
    "common_product_core": "product-core/common-product-core.json",
    "canonical_projection_source": "product-core/canonical-projection-source.json",
    "spec_014_validation": "validations/spec-014-validation.json",
    "spec_015_validation": "validations/spec-015-validation.json",
    "spec_016_validation": "validations/spec-016-validation.json",
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
def validate_package(package_root: str | Path) -> dict[str, Any]:
    root = Path(package_root)
    issues: list[PackageIssue] = []
    if not root.exists():
        issues.append(PackageIssue("PACKAGE_ROOT_MISSING", "blocking", "package root does not exist", str(root)))
        return validation_payload(root, issues)

    issues.extend(find_namespace_hygiene_issues(root))
    manifest = read_json(root / "execution/manifest.json")
    traceability = read_json(root / "execution/physical-traceability.json")
    preflight = read_json(root / "execution/mcp-preflight-record.json")
    evidence_record = read_json(root / "execution/evidence-acquisition-record.json")
    handoff = (root / "handoff/reviewer-qa-handoff.md").read_text(encoding="utf-8")

    issues.extend(validate_manifest(manifest, root))
    issues.extend(validate_physical_traceability(traceability, root))
    issues.extend(validate_mcp_preflight_record(preflight))
    issues.extend(validate_mcp_records(evidence_record))
    issues.extend(validate_handoff_text(handoff))
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