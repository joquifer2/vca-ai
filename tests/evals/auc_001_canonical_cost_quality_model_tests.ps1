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
    if ($LASTEXITCODE -eq 0) { Add-Result $Name 'PASS' 'tools/auc_001_canonical_cost_quality_model.py' $output }
    else { Add-Result $Name 'FAIL' 'tools/auc_001_canonical_cost_quality_model.py' $output }
}

$normalizationCode = @"
from tools.auc_001_canonical_cost_quality_model import normalize_lead_ad_id, normalize_spend_ad_id

assert normalize_lead_ad_id("ag:123") == "123"
assert normalize_lead_ad_id("xag:123") == "xag:123"
assert normalize_lead_ad_id("123") == "123"
assert normalize_lead_ad_id("") is None
assert normalize_lead_ad_id(None) is None
assert normalize_spend_ad_id("123") == "123"
print("strict ad_id_norm normalization passed")
"@
Invoke-PythonCheck 'Strict ad_id_norm normalization' $normalizationCode

$modelCode = @"
from decimal import Decimal
from tools.auc_001_canonical_cost_quality_model import build_cost_quality_model

leads = [
    {"lead_id": "L1", "ad_id": "ag:100", "ad_name": "Alpha", "lead_tier": "A"},
    {"lead_id": "L2", "ad_id": "ag:100", "ad_name": "Alpha", "lead_tier": "B"},
    {"lead_id": "L3", "ad_id": "ag:200", "ad_name": "Beta", "lead_tier": "C"},
]
spend = [
    {"ad_id": "100", "ad_name": "Alpha", "campaign_signal": "COMMERCIAL", "spend_amount": "30.00"},
    {"ad_id": "300", "ad_name": "Gamma", "campaign_signal": "COMMERCIAL", "spend_amount": "7.50"},
    {"ad_id": "100", "ad_name": "Alpha", "campaign_signal": "ATTENTION", "spend_amount": "5.00"},
    {"ad_id": "400", "ad_name": "Delta", "campaign_signal": "ATTENTION", "spend_amount": "2.00"},
]
model = build_cost_quality_model(leads, spend)
rows = {row.ad_id_norm: row for row in model.rows}
assert set(rows) == {"100", "200", "300"}
assert rows["100"].coverage_status == "matched"
assert rows["200"].coverage_status == "lead_only"
assert rows["300"].coverage_status == "spend_only"
assert rows["100"].cpl_commercial_matched == Decimal("15.00")
assert rows["100"].cost_per_ab_commercial_matched == Decimal("15.00")
assert rows["200"].cpl_commercial_matched is None
assert rows["300"].qualified_rate_ab_matched is None
assert model.aggregates["commercial_spend"] == Decimal("37.50")
assert model.aggregates["matched_spend"] == Decimal("30.00")
assert model.aggregates["matched_commercial_spend"] == Decimal("30.00")
assert model.aggregates["spend_only_spend"] == Decimal("7.50")
assert model.aggregates["spend_only_commercial_spend"] == Decimal("7.50")
assert model.aggregates["total_spend_all_signals"] == Decimal("44.50")
assert model.aggregates["non_commercial_spend"] == Decimal("7.00")
assert model.aggregates["lead_total"] == 3
assert model.aggregates["matched_leads"] == 2
assert model.aggregates["lead_only_leads"] == 1
assert not model.has_blockers
assert model.is_consumable
print("coverage, commercial metrics, aliases, and all-signal spend passed")
"@
Invoke-PythonCheck 'Full outer coverage and canonical commercial metrics' $modelCode

$schemaCode = @"
from tools.auc_001_canonical_cost_quality_model import build_cost_quality_model

model = build_cost_quality_model(
    [{"lead_id": "L1", "ad_id": "ag:100", "lead_tier": "A"}],
    [
        {"ad_id": "100", "campaign_signal": "COMMERCIAL", "spend_amount": "10.00"},
        {"ad_id": "200", "campaign_signal": "ATTENTION", "spend_amount": "3.25"},
    ],
)
output = model.structured_output
assert output["schema_family"] == "auc_001_reconciliation_output"
assert output["output_schema_version"] == "auc_001_reconciliation_output.v1"
assert output["model_name"] == "auc_001_canonical_cost_quality_model"
assert "SPEC-012" in output["specification_versions"]
assert "SPEC-013" in output["specification_versions"]
assert output["schema_status"] == "active"
assert output["deprecated_aliases"]["matched_spend"] == "matched_commercial_spend"
assert output["deprecated_aliases"]["spend_only_spend"] == "spend_only_commercial_spend"
assert output["is_consumable"] is True
print("schema family, versioning, model identity, and compatibility aliases passed")
"@
Invoke-PythonCheck 'Structured output schema identity and aliases' $schemaCode

$spendReconciliationCode = @"
from decimal import Decimal
from tools.auc_001_canonical_cost_quality_model import build_cost_quality_model

model = build_cost_quality_model(
    [{"lead_id": "L1", "ad_id": "ag:100", "lead_tier": "A"}],
    [
        {"ad_id": "100", "campaign_signal": "COMMERCIAL", "spend_amount": "10.00"},
        {"ad_id": "300", "campaign_signal": "COMMERCIAL", "spend_amount": "5.00"},
        {"ad_id": "400", "campaign_signal": "ATTENTION", "spend_amount": "2.00"},
        {"ad_id": "500", "campaign_signal": "CONSIDERATION", "spend_amount": "1.50"},
    ],
)
spend = model.spend_reconciliation
assert spend["total_spend_all_signals"] == "18.50"
assert spend["commercial_spend"] == "15.00"
assert spend["matched_commercial_spend"] == "10.00"
assert spend["spend_only_commercial_spend"] == "5.00"
assert spend["matched_spend"] == spend["matched_commercial_spend"]
assert spend["spend_only_spend"] == spend["spend_only_commercial_spend"]
assert spend["non_commercial_spend"] == "3.50"
assert spend["spend_by_signal"] == {"ATTENTION": "2.00", "COMMERCIAL": "15.00", "CONSIDERATION": "1.50"}
assert spend["non_commercial_spend_by_signal"] == {"ATTENTION": "2.00", "CONSIDERATION": "1.50"}
assert "total_spend_by_signal_identity" in {invariant["name"] for invariant in spend["invariants"]}
for invariant in spend["invariants"]:
    assert {"name", "expression", "left_value", "right_value", "tolerance", "result"} <= set(invariant)
    assert invariant["result"] == "PASS"
print("spend reconciliation identities and invariant records passed")
"@
Invoke-PythonCheck 'Spend reconciliation structured contract' $spendReconciliationCode

$coverageReconciliationCode = @"
from tools.auc_001_canonical_cost_quality_model import build_cost_quality_model

model = build_cost_quality_model(
    [
        {"lead_id": "L1", "ad_id": "ag:100", "lead_tier": "A"},
        {"lead_id": "L2", "ad_id": "ag:200", "lead_tier": "B"},
    ],
    [
        {"ad_id": "100", "campaign_signal": "COMMERCIAL", "spend_amount": "10.00"},
        {"ad_id": "300", "campaign_signal": "COMMERCIAL", "spend_amount": "5.00"},
    ],
)
coverage = model.coverage_reconciliation
assert set(["matched", "lead_only", "spend_only", "unknown", "invariants"]) <= set(coverage)
assert coverage["matched"]["ad_count"] == 1
assert coverage["matched"]["leads"] == 1
assert coverage["lead_only"]["ad_count"] == 1
assert coverage["spend_only"]["ad_count"] == 1
assert coverage["unknown"]["ad_count"] == 0
assert coverage["unknown"]["leads"] == 0
assert coverage["unknown"]["reason_codes"] == []
assert coverage["matched"]["matched_commercial_spend"] == "10.00"
assert coverage["spend_only"]["spend_only_commercial_spend"] == "5.00"
assert "commercial_spend_coverage_identity" in {invariant["name"] for invariant in coverage["invariants"]}
for invariant in coverage["invariants"]:
    assert {"name", "expression", "left_value", "right_value", "tolerance", "result"} <= set(invariant)
    assert invariant["result"] == "PASS"
print("coverage reconciliation with explicit unknown and invariant records passed")
"@
Invoke-PythonCheck 'Coverage reconciliation structured contract' $coverageReconciliationCode

$failInvariantCode = @"
from tools.auc_001_canonical_cost_quality_model import build_cost_quality_model, validate_required_invariant_records

model = build_cost_quality_model(
    [{"lead_id": "L1", "ad_id": "ag:100", "lead_tier": "A"}],
    [{"ad_id": "100", "campaign_signal": "COMMERCIAL", "spend_amount": "10.00"}],
)
assert model.is_consumable
model.coverage_reconciliation["invariants"][0]["result"] = "FAIL"
assert model.has_failed_required_invariants
assert not model.is_consumable
issues = validate_required_invariant_records(model.required_invariants)
assert any(issue.code == "REQUIRED_INVARIANT_FAILED" and issue.severity == "blocking" for issue in issues)
print("mandatory invariant FAIL blocks consumer contract consumption passed")
"@
Invoke-PythonCheck 'Mandatory invariant FAIL blocks output consumption' $failInvariantCode

$metricValidationCode = @"
from tools.auc_001_canonical_cost_quality_model import validate_metric_name, validate_structured_metric_request

for name in ["CPL", "CPQL", "CPHQL"]:
    try:
        validate_metric_name(name)
    except ValueError:
        pass
    else:
        raise SystemExit(f"Accepted prohibited metric name: {name}")

validate_metric_name("cost_per_ab_commercial_matched")
validate_structured_metric_request(
    "cost_per_ab_commercial_matched",
    signal="COMMERCIAL",
    coverage_status="matched",
    universe="commercial_matched",
    numerator_source="matched_commercial_spend",
    denominator_value=1,
)
invalid_requests = [
    dict(signal="ATTENTION", coverage_status="matched", universe="commercial_matched", numerator_source="matched_commercial_spend", denominator_value=1),
    dict(signal="COMMERCIAL", coverage_status="lead_only", universe="commercial_matched", numerator_source="matched_commercial_spend", denominator_value=1),
    dict(signal="COMMERCIAL", coverage_status="matched", universe="all_signals", numerator_source="total_spend_all_signals", denominator_value=1),
    dict(signal="COMMERCIAL", coverage_status="matched", universe="commercial_matched", numerator_source="matched_commercial_spend", denominator_value=0),
]
for request in invalid_requests:
    try:
        validate_structured_metric_request("cost_per_ab_commercial_matched", **request)
    except ValueError:
        pass
    else:
        raise SystemExit(f"Accepted invalid metric universe: {request}")
print("structured metric validation remains limited to SPEC-013 output guards")
"@
Invoke-PythonCheck 'Structured metric validation guards' $metricValidationCode

$consumerContractCode = @"
import json
from tools.auc_001_canonical_cost_quality_model import build_cost_quality_model

model = build_cost_quality_model(
    [{"lead_id": "L1", "ad_id": "ag:100", "lead_tier": "A"}],
    [{"ad_id": "100", "campaign_signal": "COMMERCIAL", "spend_amount": "10.00"}],
)
output = model.structured_output
json.dumps(output, sort_keys=True)
required_top_level = [
    "schema_family",
    "output_schema_version",
    "model_name",
    "specification_versions",
    "schema_status",
    "spend_reconciliation",
    "coverage_reconciliation",
]
for key in required_top_level:
    assert key in output
assert "markdown" not in output
assert "narrative" not in output
assert all(block in output["coverage_reconciliation"] for block in ["matched", "lead_only", "spend_only", "unknown"])
print("consumer contract can read structured output without Markdown parsing")
"@
Invoke-PythonCheck 'Consumer contract no-Markdown structured consumption' $consumerContractCode

$blockingCode = @"
from tools.auc_001_canonical_cost_quality_model import build_cost_quality_model

collision = build_cost_quality_model(
    [
        {"lead_id": "L1", "ad_id": "ag:100", "ad_name": "Alpha", "lead_tier": "A"},
        {"lead_id": "L2", "ad_id": "100", "ad_name": "Alpha", "lead_tier": "B"},
    ],
    [{"ad_id": "100", "campaign_signal": "COMMERCIAL", "spend_amount": "1.00"}],
)
assert collision.has_blockers
assert not collision.is_consumable
assert any(issue.code == "AD_ID_NORM_COLLISION" for issue in collision.issues)
print("blocking issues make output non-consumable passed")
"@
Invoke-PythonCheck 'Blockers make output non-consumable' $blockingCode

$docCode = @"
from pathlib import Path

checks = {
    "docs/contracts/evidence.contract.md": [
        "Contextual Constraint Declaration",
        "perfil o artefacto local",
        "fuente canonica",
        "UNKNOWN",
    ],
    "analytical_use_cases/auc-001/faro-strategic-context-profile.json": [
        "AUC-001-FARO-STRATEGIC-CONTEXT-PROFILE",
        "campaign_signal_interpretation",
        "AUC-001-FARO-GLOBAL-NO-UNIVERSAL-KPI",
        "knowledge/client/ccd.md",
    ],
    "specs/spec-013-auc-001-structured-reconciliation-output.md": [
        "auc_001_reconciliation_output",
        "runtime-output.json",
        "Consumer Contract",
        "Entry Gate",
    ],
    "gates/spec-013-auc-001-structured-reconciliation-output-entry-gate.md": [
        "Pass with minor conditions",
        "Decision",
        "SPEC-013",
    ],
}

for path, markers in checks.items():
    text = Path(path).read_text(encoding="utf-8-sig")
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise SystemExit(f"{path} missing markers: {missing}")
print("documentary contract, local profile, and gate markers passed")
"@
Invoke-PythonCheck 'Documentary contract, local profile, specification, and Entry Gate markers' $docCode


$runtimePersistenceCode = @"
import json
import tempfile
from pathlib import Path
from tools.auc_001_canonical_cost_quality_model import build_cost_quality_model, build_runtime_output_payload, persist_runtime_output

metadata = {
    "execution_id": "AUC-001-PCI-002-LOCAL-TEST",
    "period_start": "2026-04-18",
    "period_end": "2026-06-30",
    "data_provider": "BigQuery MCP Server",
    "source_tables": ["marts.fct_spend", "marts.fct_lead_enriched", "intermediate.int_faro_lead_scoring"],
    "input_hashes": {"lead_records": "sha256:test-leads", "spend_records": "sha256:test-spend"},
}
model = build_cost_quality_model(
    [{"lead_id": "L1", "ad_id": "ag:100", "lead_tier": "A"}],
    [
        {"ad_id": "100", "campaign_signal": "COMMERCIAL", "spend_amount": "10.00"},
        {"ad_id": "200", "campaign_signal": "ATTENTION", "spend_amount": "2.50"},
    ],
)
with tempfile.TemporaryDirectory() as temp_dir:
    namespace = Path(temp_dir) / "outputs" / "auc-001" / "pci-002" / "2026-06-30"
    payload = build_runtime_output_payload(model, execution_metadata=metadata, namespace_path=namespace)
    json.dumps(payload, sort_keys=True)
    for key in ["schema_family", "output_schema_version", "spend_reconciliation", "coverage_reconciliation", "strategic_context_constraints", "is_consumable", "execution_id", "period_start", "period_end", "source_tables", "input_hashes", "namespace"]:
        assert key in payload
    assert payload["spend_reconciliation"]["total_spend_all_signals"] == "12.50"
    assert payload["spend_reconciliation"]["non_commercial_spend"] == "2.50"
    assert payload["package_status"]["is_complete"] is True
    result = persist_runtime_output(model, namespace, execution_metadata=metadata, repo_root=temp_dir)
    assert result["write_status"] == "PASS"
    assert result["is_package_complete"] is True
    runtime_path = namespace / "execution" / "runtime-output.json"
    assert runtime_path.exists()
    persisted = json.loads(runtime_path.read_text(encoding="utf-8"))
    assert persisted["schema_family"] == "auc_001_reconciliation_output"
    assert persisted["execution_id"] == "AUC-001-PCI-002-LOCAL-TEST"
    assert persisted["runtime_output_path"].endswith("execution/runtime-output.json")
print("runtime-output payload serialization and physical persistence passed")
"@
Invoke-PythonCheck 'Runtime output payload serialization and physical persistence' $runtimePersistenceCode

$protectedNamespaceCode = @"
import tempfile
from pathlib import Path
from tools.auc_001_canonical_cost_quality_model import build_cost_quality_model, persist_runtime_output

metadata = {
    "execution_id": "AUC-001-PROTECTED-TEST",
    "period_start": "2026-04-18",
    "period_end": "2026-06-30",
    "data_provider": "BigQuery MCP Server",
    "source_tables": ["marts.fct_spend"],
    "input_hashes": {"spend_records": "sha256:test"},
}
model = build_cost_quality_model([], [{"ad_id": "100", "campaign_signal": "COMMERCIAL", "spend_amount": "1.00"}])
with tempfile.TemporaryDirectory() as temp_dir:
    protected = Path(temp_dir) / "outputs" / "auc-001" / "pci-001" / "2026-06-30"
    result = persist_runtime_output(model, protected, execution_metadata=metadata, repo_root=temp_dir)
    assert result["write_status"] == "FAIL"
    assert result["error"] == "PROTECTED_NAMESPACE"
    assert result["is_package_complete"] is False
    assert not (protected / "execution" / "runtime-output.json").exists()
print("protected historical namespace rejection passed")
"@
Invoke-PythonCheck 'Runtime output protected namespace rejection' $protectedNamespaceCode

$nonConsumablePersistenceCode = @"
import json
import tempfile
from pathlib import Path
from tools.auc_001_canonical_cost_quality_model import build_cost_quality_model, persist_runtime_output

metadata = {
    "execution_id": "AUC-001-NON-CONSUMABLE-TEST",
    "period_start": "2026-04-18",
    "period_end": "2026-06-30",
    "data_provider": "BigQuery MCP Server",
    "source_tables": ["marts.fct_spend", "marts.fct_lead_enriched"],
    "input_hashes": {"lead_records": "sha256:test", "spend_records": "sha256:test"},
}
model = build_cost_quality_model(
    [
        {"lead_id": "L1", "ad_id": "ag:100", "lead_tier": "A"},
        {"lead_id": "L2", "ad_id": "100", "lead_tier": "B"},
    ],
    [{"ad_id": "100", "campaign_signal": "COMMERCIAL", "spend_amount": "1.00"}],
)
assert not model.is_consumable
with tempfile.TemporaryDirectory() as temp_dir:
    namespace = Path(temp_dir) / "outputs" / "auc-001" / "pci-002" / "2026-06-30"
    result = persist_runtime_output(model, namespace, execution_metadata=metadata, repo_root=temp_dir)
    assert result["write_status"] == "PASS"
    assert result["is_consumable"] is False
    assert result["is_package_complete"] is False
    persisted = json.loads((namespace / "execution" / "runtime-output.json").read_text(encoding="utf-8"))
    assert persisted["is_consumable"] is False
    assert persisted["package_status"]["is_complete"] is False
    assert persisted["package_status"]["blockers"]
print("non-consumable runtime persists but blocks package completion passed")
"@
Invoke-PythonCheck 'Runtime output non-consumable package blocker' $nonConsumablePersistenceCode

$writeFailureCode = @"
import tempfile
from pathlib import Path
from tools.auc_001_canonical_cost_quality_model import build_cost_quality_model, persist_runtime_output

metadata = {
    "execution_id": "AUC-001-WRITE-FAILURE-TEST",
    "period_start": "2026-04-18",
    "period_end": "2026-06-30",
    "data_provider": "BigQuery MCP Server",
    "source_tables": ["marts.fct_spend"],
    "input_hashes": {"spend_records": "sha256:test"},
}
model = build_cost_quality_model([], [{"ad_id": "100", "campaign_signal": "COMMERCIAL", "spend_amount": "1.00"}])
with tempfile.TemporaryDirectory() as temp_dir:
    namespace = Path(temp_dir) / "outputs" / "auc-001" / "pci-002" / "2026-06-30"
    first = persist_runtime_output(model, namespace, execution_metadata=metadata, repo_root=temp_dir)
    second = persist_runtime_output(model, namespace, execution_metadata=metadata, repo_root=temp_dir)
    assert first["write_status"] == "PASS"
    assert second["write_status"] == "FAIL"
    assert second["error"] == "WRITE_FAILED"
    assert second["is_package_complete"] is False
print("runtime-output write failure blocks package completion passed")
"@
Invoke-PythonCheck 'Runtime output write failure package blocker' $writeFailureCode
$failures = @($Results | Where-Object { $_.Status -ne 'PASS' })
$Results | Format-Table -AutoSize

if ($failures.Count -gt 0) {
    Write-Host "`nAUC-001 canonical cost-quality model tests failed: $($failures.Count)" -ForegroundColor Red
    exit 1
}

Write-Host "`nAll AUC-001 canonical cost-quality model tests passed: $($Results.Count)" -ForegroundColor Green
exit 0