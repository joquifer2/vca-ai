$ErrorActionPreference = 'Stop'

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot '..\..')
Set-Location $RepoRoot

$Results = New-Object System.Collections.Generic.List[object]

$Auc001ValidationDir = 'docs/evaluations/auc-001/validations'
$TransversalContractsEvaluation = Join-Path $Auc001ValidationDir 'auc-001-transversal-contracts-evaluation.md'
$ContextAcquisitionEvaluation = Join-Path $Auc001ValidationDir 'auc-001-context-acquisition-evaluation.md'
$PreparationEvidenceEvaluation = Join-Path $Auc001ValidationDir 'auc-001-preparation-evidence-evaluation.md'
$ReasoningRecommendationsEvaluation = Join-Path $Auc001ValidationDir 'auc-001-reasoning-recommendations-evaluation.md'
$PresentationOutputEvaluation = Join-Path $Auc001ValidationDir 'auc-001-presentation-output-evaluation.md'
$DevelopmentEntryReadinessEvidence = Join-Path $Auc001ValidationDir 'auc-001-development-entry-readiness-evidence.md'

function Add-Result {
    param(
        [string]$Name,
        [string]$Status,
        [string]$Evidence,
        [string]$Details = ''
    )
    $Results.Add([pscustomobject]@{
        Name = $Name
        Status = $Status
        Evidence = $Evidence
        Details = $Details
    }) | Out-Null
}

function Read-Doc {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        throw "Missing required artifact: $Path"
    }
    return Get-Content -Raw -LiteralPath $Path
}

function Assert-ContainsAll {
    param(
        [string]$Name,
        [string]$Path,
        [string[]]$Patterns
    )
    $text = Read-Doc $Path
    $missing = @()
    foreach ($pattern in $Patterns) {
        if ($text -notlike "*$pattern*") {
            $missing += $pattern
        }
    }
    if ($missing.Count -eq 0) {
        Add-Result $Name 'PASS' $Path ('Checked ' + $Patterns.Count + ' required markers')
    } else {
        Add-Result $Name 'FAIL' $Path ('Missing markers: ' + ($missing -join '; '))
    }
}

function Assert-PathsExist {
    param(
        [string]$Name,
        [string[]]$Paths
    )
    $missing = @()
    foreach ($path in $Paths) {
        if (-not (Test-Path -LiteralPath $path)) {
            $missing += $path
        }
    }
    if ($missing.Count -eq 0) {
        Add-Result $Name 'PASS' 'repository filesystem' ('Checked ' + $Paths.Count + ' paths')
    } else {
        Add-Result $Name 'FAIL' 'repository filesystem' ('Missing paths: ' + ($missing -join '; '))
    }
}

function Resolve-RepoMarkdownTarget {
    param(
        [string]$SourcePath,
        [string]$Target
    )
    $targetWithoutAnchor = ($Target -split '#', 2)[0]
    if ([string]::IsNullOrWhiteSpace($targetWithoutAnchor)) {
        return $null
    }
    if ($targetWithoutAnchor -match '^(https?:|mailto:)') {
        return $null
    }
    if ($targetWithoutAnchor.StartsWith('/')) {
        return Join-Path $RepoRoot ($targetWithoutAnchor.TrimStart('/'))
    }
    $base = Split-Path $SourcePath
    return Join-Path $base $targetWithoutAnchor
}

function Assert-MarkdownLinksResolve {
    param(
        [string]$Name,
        [string[]]$Paths
    )
    $missing = @()
    foreach ($path in $Paths) {
        $text = Read-Doc $path
        $matches = [regex]::Matches($text, '\]\(([^)]+)\)')
        foreach ($match in $matches) {
            $target = $match.Groups[1].Value
            $resolved = Resolve-RepoMarkdownTarget $path $target
            if ($null -eq $resolved) { continue }
            if (-not (Test-Path -LiteralPath $resolved)) {
                $missing += "$path -> $target"
            }
        }
    }
    if ($missing.Count -eq 0) {
        Add-Result $Name 'PASS' ($Paths -join ', ') 'All local markdown links resolve'
    } else {
        Add-Result $Name 'FAIL' ($Paths -join ', ') ('Broken links: ' + ($missing -join '; '))
    }
}

$requiredArtifacts = @(
    'docs/handoffs/auc-001-analysis-request.md',
    'docs/handoffs/auc-001-context-definition.md',
    'docs/handoffs/auc-001-data-contract.md',
    'docs/handoffs/auc-001-discovery-contract.md',
    'docs/handoffs/auc-001-analytical-contract.md',
    'docs/handoffs/auc-001-evidence-set.md',
    'docs/handoffs/auc-001-evidence-contract.md',
    'docs/handoffs/auc-001-knowledge-set.md',
    'docs/handoffs/auc-001-knowledge-contract.md',
    'docs/handoffs/auc-001-recommendation-set.md',
    'docs/handoffs/auc-001-recommendation-contract.md',
    'docs/handoffs/auc-001-presentation-contract.md',
    'docs/handoffs/auc-001-executive-report.md',
    $TransversalContractsEvaluation,
    $ContextAcquisitionEvaluation,
    $PreparationEvidenceEvaluation,
    $ReasoningRecommendationsEvaluation,
    $PresentationOutputEvaluation,
    $DevelopmentEntryReadinessEvidence
)

Assert-PathsExist 'Required AUC-001 traceability artifacts exist' $requiredArtifacts

Assert-ContainsAll 'Backlog dependencies T-031 through T-037 are complete' 'docs/tasks.md' @(
    '| T-031 |', '| T-032 |', '| T-033 |', '| T-034 |', '| T-035 |', '| T-036 |', '| T-037 |', '| Completed |'
)

Assert-ContainsAll 'Context-to-output IDs are preserved' 'docs/handoffs/auc-001-executive-report.md' @(
    'VCA-AUC-001-PRS-001',
    'VCA-AUC-001-CTX-DEF-2026-06',
    'VCA-AUC-001-EVD-001',
    'VCA-AUC-001-KNW-001',
    'VCA-AUC-001-REC-001'
)

Assert-ContainsAll 'Evidence IDs propagate into final output' 'docs/handoffs/auc-001-executive-report.md' @(
    'EVD-001', 'EVD-002', 'EVD-003', 'EVD-004',
    'matched', 'lead_only', 'spend_only'
)

Assert-ContainsAll 'Knowledge IDs propagate into final output' 'docs/handoffs/auc-001-executive-report.md' @(
    'INS-001', 'INS-002', 'INS-003',
    'HYP-001', 'HYP-002',
    'CON-001', 'CON-002',
    'PRI-001', 'PRI-002', 'PRI-003', 'PRI-004'
)

Assert-ContainsAll 'Recommendation IDs propagate into final output' 'docs/handoffs/auc-001-executive-report.md' @(
    'REC-001', 'REC-002', 'REC-003', 'REC-004', 'REC-005', 'REC-006',
    'P1', 'P2', 'P3'
)

Assert-ContainsAll 'Material UNKNOWNs propagate into final output' 'docs/handoffs/auc-001-executive-report.md' @(
    'UNC-001', 'UNC-002', 'UNC-003', 'UNC-004', 'UNC-005',
    'Duplicate/test-record flags are not explicitly mapped',
    'Impressions, clicks and CTR are unavailable',
    'Creative asset metadata is unavailable'
)

Assert-ContainsAll 'Analytical layer does not introduce reasoning or recommendations' 'docs/handoffs/auc-001-evidence-set.md' @(
    'Este artefacto no interpreta causas',
    'Este artefacto no produce insights',
    'No recommendation',
    'Require T-023 Evidence Contract and downstream phases first'
)

Assert-ContainsAll 'Reasoning layer remains separated from recommendations' 'docs/handoffs/auc-001-knowledge-set.md' @(
    'no recommendations or execution plan',
    'No recommendations',
    'No suggested action or execution plan is included',
    'T-027 may now begin recommendation-layer work'
)

Assert-ContainsAll 'Recommendation layer does not create evidence or presentation artifact' 'docs/handoffs/auc-001-recommendation-set.md' @(
    'no execution, no presentation artifact, no new evidence',
    'No new evidence',
    'No conclusion rewrite',
    'No presentation artifact'
)

Assert-ContainsAll 'Presentation layer does not add evidence, interpretation or recommendations' 'docs/handoffs/auc-001-executive-report.md' @(
    'Este artefacto no crea evidencia nueva',
    'Este artefacto no introduce nueva interpretacion',
    'Este artefacto no altera prioridades',
    'do not authorize operational execution by themselves'
)

Assert-ContainsAll -Name 'Readiness evidence carries active observations into T-038' -Path $DevelopmentEntryReadinessEvidence -Patterns @(
    'PASS WITH OBSERVATIONS',
    'ACT-OBS-001', 'ACT-OBS-002', 'ACT-OBS-003', 'ACT-OBS-004', 'ACT-OBS-005', 'ACT-OBS-006', 'ACT-OBS-007',
    'Keep active observations visible during T-038'
)

Assert-ContainsAll -Name 'Context references expose canonical T-037 readiness evidence' -Path 'docs/context_refs.md' -Patterns @(
    'Development Entry Readiness Evidence',
    '/docs/evaluations/auc-001/validations/auc-001-development-entry-readiness-evidence.md'
)

Assert-ContainsAll -Name 'AUC-001 index exposes canonical T-037 readiness evidence' -Path 'analytical_use_cases/auc-001/README.md' -Patterns @(
    'Development Entry Readiness Evidence',
    '/docs/evaluations/auc-001/validations/auc-001-development-entry-readiness-evidence.md'
)
Assert-MarkdownLinksResolve -Name 'Evaluation artifact local links resolve' -Paths @(
    $ReasoningRecommendationsEvaluation,
    $PresentationOutputEvaluation,
    $DevelopmentEntryReadinessEvidence
)

$failures = $Results | Where-Object { $_.Status -ne 'PASS' }
$Results | Format-Table -AutoSize

if ($failures.Count -gt 0) {
    Write-Host "`nTraceability tests failed: $($failures.Count)" -ForegroundColor Red
    exit 1
}

Write-Host "`nAll AUC-001 traceability tests passed: $($Results.Count)" -ForegroundColor Green
exit 0