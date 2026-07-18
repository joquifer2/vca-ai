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
]
model = build_cost_quality_model(leads, spend)
rows = {row.ad_id_norm: row for row in model.rows}
assert rows["100"].coverage_status == "matched"
assert rows["200"].coverage_status == "lead_only"
assert rows["300"].coverage_status == "spend_only"
assert rows["100"].cpl_commercial_matched == Decimal("15.00")
assert rows["100"].cost_per_ab_commercial_matched == Decimal("15.00")
assert rows["200"].cpl_commercial_matched is None
assert rows["300"].qualified_rate_ab_matched is None
assert model.aggregates["commercial_spend"] == Decimal("37.50")
assert model.aggregates["matched_spend"] == Decimal("30.00")
assert model.aggregates["spend_only_spend"] == Decimal("7.50")
assert model.aggregates["lead_total"] == 3
assert model.aggregates["matched_leads"] == 2
assert model.aggregates["lead_only_leads"] == 1
assert not model.has_blockers
print("full outer coverage, metrics, and invariants passed")
"@
Invoke-PythonCheck 'Full outer join coverage and canonical metrics' $modelCode

$blockingCode = @"
from tools.auc_001_canonical_cost_quality_model import build_cost_quality_model, validate_metric_name

collision = build_cost_quality_model(
    [
        {"lead_id": "L1", "ad_id": "ag:100", "ad_name": "Alpha", "lead_tier": "A"},
        {"lead_id": "L2", "ad_id": "100", "ad_name": "Alpha", "lead_tier": "B"},
    ],
    [{"ad_id": "100", "campaign_signal": "COMMERCIAL", "spend_amount": "1.00"}],
)
assert collision.has_blockers
assert any(issue.code == "AD_ID_NORM_COLLISION" for issue in collision.issues)

for name in ["CPL", "CPQL", "CPHQL"]:
    try:
        validate_metric_name(name)
    except ValueError:
        pass
    else:
        raise SystemExit(f"Accepted prohibited metric name: {name}")

validate_metric_name("cost_per_ab_commercial_matched")
print("blockers and metric naming policy passed")
"@
Invoke-PythonCheck 'Blockers and prohibited metric names' $blockingCode

$docCode = @"
from pathlib import Path

checks = {
    "docs/contracts/analytical.contract.md": [
        "AUC-001 Post-Closure Cost-Quality Analytical Model Rules",
        "auc_001_canonical_cost_quality_model",
        "ad_id_norm",
        "CPQL",
    ],
    "docs/contracts/data.contract.md": [
        "AUC-001 Post-Closure Cost-Quality Data Rules",
        "marts.fct_lead_enriched",
        "intermediate.int_faro_lead_scoring",
        "Historical outputs",
    ],
    "docs/contracts/evidence.contract.md": [
        "AUC-001 Post-Closure Cost-Quality Evidence Rules",
        "Coverage States",
        "Economic Universes And Metrics",
        "Publication Controls",
    ],
    ".github/skills/meta-lead-quality-analysis/CHECKLIST.md": [
        "AUC-001-PCI-001 Canonical Cost-Quality Model",
        "auc_001_canonical_cost_quality_model",
        "ad_name",
        "outputs/auc-001/2026-06-30/",
    ],
}

for path, markers in checks.items():
    text = Path(path).read_text(encoding="utf-8-sig")
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise SystemExit(f"{path} missing markers: {missing}")
print("documentary contract markers passed")
"@
Invoke-PythonCheck 'Documentary contract markers for AUC-001-PCI-001' $docCode

$failures = $Results | Where-Object { $_.Status -ne 'PASS' }
$Results | Format-Table -AutoSize

if ($failures.Count -gt 0) {
    Write-Host "`nAUC-001 canonical cost-quality model tests failed: $($failures.Count)" -ForegroundColor Red
    exit 1
}

Write-Host "`nAll AUC-001 canonical cost-quality model tests passed: $($Results.Count)" -ForegroundColor Green
exit 0
