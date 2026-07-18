$ErrorActionPreference = 'Stop'

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot '..\..')
Set-Location $RepoRoot

$Results = New-Object System.Collections.Generic.List[object]

function Add-Result {
    param([string]$Name, [string]$Status, [string]$Evidence, [string]$Details = '')
    $Results.Add([pscustomobject]@{ Name = $Name; Status = $Status; Evidence = $Evidence; Details = $Details }) | Out-Null
}

function Assert-ContainsAll {
    param([string]$Name, [string]$Path, [string[]]$Patterns)
    $text = Get-Content -Raw -LiteralPath $Path
    $missing = @()
    foreach ($pattern in $Patterns) {
        if ($text -notlike "*$pattern*") { $missing += $pattern }
    }
    if ($missing.Count -eq 0) { Add-Result $Name 'PASS' $Path ('Checked ' + $Patterns.Count + ' markers') }
    else { Add-Result $Name 'FAIL' $Path ('Missing: ' + ($missing -join '; ')) }
}

function Invoke-PythonCheck {
    param([string]$Name, [string]$Code)
    $output = $Code | python -
    if ($LASTEXITCODE -eq 0) { Add-Result $Name 'PASS' 'tools/vca_mcp_contract.py' $output }
    else { Add-Result $Name 'FAIL' 'tools/vca_mcp_contract.py' $output }
}

Assert-ContainsAll 'Canonical contract reference documents only the active selector contract' 'docs/contracts/bigquery-mcp-discover-metadata.contract.md' @(
    'scope_request',
    'resource_selector',
    'workspace:vca',
    'dataset:marts',
    'table:marts.fct_spend',
    'Invalid Selector Categories',
    'does not publish a specific functional-unavailability error'
)

Assert-ContainsAll 'Runbook Phase 05 uses deterministic discovery states and errors' '.github/skills/meta-lead-quality-analysis/RUNBOOK.md' @(
    'PASS WITH OBSERVATION',
    'ERR_SELECTOR_INVALID',
    'ERR_SCOPE_TOO_BROAD',
    'ERR_RESOURCE_NOT_ALLOWLISTED',
    'ERR_AUTH_REQUIRED',
    'no probar formatos alternativos',
    'actualmente no hay codigo oficial observado',
    'docs/contracts/bigquery-mcp-discover-metadata.contract.md'
)

Assert-ContainsAll 'Checklist enforces canonical discover_metadata validation' '.github/skills/meta-lead-quality-analysis/CHECKLIST.md' @(
    'selector canonico',
    'No se ejecutaron reintentos exploratorios',
    'PASS WITH OBSERVATION',
    'FAIL',
    'actualmente no hay codigo oficial observado'
)

Assert-ContainsAll 'Smoke script uses canonical selectors' 'tools/vca_mcp_smoke.py' @(
    'workspace:vca',
    'dataset:marts',
    'table:marts.fct_spend',
    'build_discover_request'
)

$smokeText = Get-Content -Raw -LiteralPath 'tools/vca_mcp_smoke.py'
$legacyMarkers = @(
    '"scope_' + 'request": "data' + 'sets"',
    '"scope_' + 'request": "tab' + 'les"',
    '"scope_' + 'request": "sch' + 'ema"',
    '"resource_' + 'selector": "datamart-vca' + '-494114"',
    '"resource_' + 'selector": "datamart-vca' + '-494114.marts"'
)
$foundLegacy = @()
foreach ($marker in $legacyMarkers) {
    if ($smokeText -like "*$marker*") { $foundLegacy += $marker }
}
if ($foundLegacy.Count -eq 0) { Add-Result 'Legacy selector combinations are absent from smoke script' 'PASS' 'tools/vca_mcp_smoke.py' }
else { Add-Result 'Legacy selector combinations are absent from smoke script' 'FAIL' 'tools/vca_mcp_smoke.py' ($foundLegacy -join '; ') }

$selectorCode = @"
from tools.vca_mcp_contract import build_discover_request, validate_discover_selector

valid = [
    ("workspace", "workspace:vca"),
    ("dataset", "dataset:marts"),
    ("table", "table:marts.fct_spend"),
]
for scope, selector in valid:
    build_discover_request("test", scope, selector)

project = "datamart-vca" + "-494114"
invalid = [
    ("data" + "sets", project),
    ("tab" + "les", project + ".marts"),
    ("sch" + "ema", project + ".marts.fct_spend"),
    ("table", project + ".marts.fct_spend"),
    ("table", "fct_" + "spend"),
]
for scope, selector in invalid:
    try:
        validate_discover_selector(scope, selector)
    except ValueError:
        continue
    raise SystemExit(f"Accepted invalid selector: {scope} {selector}")
print("canonical selectors accepted; legacy selectors rejected")
"@
Invoke-PythonCheck 'Canonical selector and legacy rejection behavior' $selectorCode

$errorCode = @"
from tools.vca_mcp_contract import classify_discover_error, phase05_status, requires_user_authorization, FUNCTIONAL_DISCOVERY_ERRORS

if FUNCTIONAL_DISCOVERY_ERRORS:
    raise SystemExit(f"Unexpected functional discovery error codes: {FUNCTIONAL_DISCOVERY_ERRORS}")
expected = {
    "ERR_SELECTOR_INVALID": "stop_contract_incompatibility",
    "ERR_SCOPE_TOO_BROAD": "apply_at_most_one_documented_deterministic_reduction",
    "ERR_RESOURCE_NOT_ALLOWLISTED": "stop_resource_not_authorized",
    "ERR_AUTH_REQUIRED": "stop_and_request_local_intervention_if_needed",
}
for code, action in expected.items():
    actual = classify_discover_error(code)["action"]
    if actual != action:
        raise SystemExit(f"{code}: {actual} != {action}")
if classify_discover_error("ERR_FUTURE_DISCOVERY_FUNCTIONAL_CODE")["status"] != "FAIL":
    raise SystemExit("Unknown functional-looking codes must fail until the server publishes them")
if phase05_status(True, False, False) != "PASS":
    raise SystemExit("PASS status failed")
if phase05_status(False, True, True) != "PASS WITH OBSERVATION":
    raise SystemExit("PASS WITH OBSERVATION status failed")
if phase05_status(False, False, True) != "FAIL":
    raise SystemExit("FAIL status failed")
for action in ["renew_adc", "restart_server", "modify_configuration", "change_allowlist", "update_runtime"]:
    if not requires_user_authorization(action):
        raise SystemExit(f"Expected authorization for {action}")
for action in ["correct_selector_within_documented_contract", "query_read_only_validation", "continue_after_pass_with_observation"]:
    if requires_user_authorization(action):
        raise SystemExit(f"Unexpected authorization for {action}")
print("error interpretation, statuses, authorization behavior, and empty functional-code set are deterministic")
"@
Invoke-PythonCheck 'Error codes map to deterministic Phase 05 behavior' $errorCode

$failures = $Results | Where-Object { $_.Status -ne 'PASS' }
$Results | Format-Table -AutoSize

if ($failures.Count -gt 0) {
    Write-Host "`nAUC-001 discover_metadata contract tests failed: $($failures.Count)" -ForegroundColor Red
    exit 1
}

Write-Host "`nAll AUC-001 discover_metadata contract tests passed: $($Results.Count)" -ForegroundColor Green
exit 0