$ErrorActionPreference = 'Stop'

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot '..\..')
Set-Location $RepoRoot

Import-Module (Join-Path $RepoRoot 'tools\spec011_communication_context_transform.psm1') -Force

$Results = New-Object System.Collections.Generic.List[object]

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

function Assert-True {
    param(
        [string]$Name,
        [bool]$Condition,
        [string]$Evidence,
        [string]$Details = ''
    )
    if ($Condition) {
        Add-Result $Name 'PASS' $Evidence $Details
    } else {
        Add-Result $Name 'FAIL' $Evidence $Details
    }
}

$ContextDefinition = @{
    context_id = 'VCA-AUC-001-CTX-DEF-2026-06'
    audience = 'decision_owner'
    purpose = 'executive_decision_support'
    decision_supported = 'prioritize_next_campaign_learning_action'
}

$ExecutionScopeCanonicalizationResult = @{
    canonicalization_id = 'VCA-AUC-001-EXEC-SCOPE-2026-06'
    status = 'Frozen'
}

$SelectedPresentationProjection = @{
    name = 'Executive Report'
    status = 'Selected'
    source = 'Execution Context canonicalized by SPEC-010'
}

$PresentationContract = @{
    contract_id = 'VCA-AUC-001-PRS-001'
    boundary_status = 'No new evidence, interpretation or prioritization'
}

$CommunicationContext = @{
    audience = 'decision_owner'
    communicative_purpose = 'support commercial prioritization decision'
    supported_decision_type = 'campaign learning prioritization'
    abstraction_level = 'executive'
    information_density = 'concise'
    traceability_visibility = 'summary'
    format_constraints = 'markdown_traceable_output'
}

$CanonicalContent = @{
    artifact_id = 'VCA-AUC-001-CANONICAL-CONTENT'
    content_blocks = @(
        @{
            id = 'INS-001'
            type = 'knowledge'
            text = 'RTG genera una tasa A/B superior en lectura lead-side, pero no tiene spend comercial emparejado en las fuentes aprobadas.'
            priority = 'P1'
            traceability = @('EVD-002', 'KNW-001')
            limitations = @('UNC-002')
        },
        @{
            id = 'REC-003'
            type = 'recommendation'
            text = 'No escalar inversión sobre RTG hasta resolver la lectura de eficiencia económica asociada al spend.'
            priority = 'P2'
            traceability = @('REC-003', 'EVD-004', 'UNC-002')
            limitations = @('UNC-002')
        }
    )
    limitations = @(
        @{ id = 'UNC-002'; text = 'Spend comercial no emparejado para RTG.' }
    )
}

$OutputRequest = @{
    request_id = 'SPEC-011-EXPERIMENT-001'
    requested_output = 'traceable executive representation'
}

$result = Invoke-Spec011CommunicationContextTransformation `
    -ContextDefinition $ContextDefinition `
    -ExecutionScopeCanonicalizationResult $ExecutionScopeCanonicalizationResult `
    -SelectedPresentationProjection $SelectedPresentationProjection `
    -CommunicationContext $CommunicationContext `
    -PresentationContract $PresentationContract `
    -CanonicalContent $CanonicalContent `
    -OutputRequest $OutputRequest

Assert-True 'SPEC-011 success path materializes output' ($result.status -eq 'Materialized' -and $result.work_package -eq 'WP-004') 'VC-001..VC-004' ('Status: ' + $result.status)

$output = $result.data.presentation_layer_output
Assert-True 'Representation Constraints are derived before transformation' ($output.representation_constraints.audience -eq 'decision_owner' -and $output.representation_constraints.canonical_artifact_id -eq 'VCA-AUC-001-CANONICAL-CONTENT') 'WP-002; SPEC-011 conceptual workflow' 'Constraint set is present in output metadata'
Assert-True 'Semantic equivalence is verified by canonical preservation' ($output.semantic_equivalence_status -eq 'Verified by canonical block preservation') 'FR-003; AC-003' $output.semantic_equivalence_status
Assert-True 'Traceability remains visible under summary visibility' (($output.output_blocks[0].traceability -contains 'INS-001') -and ($output.traceability -contains 'VCA-AUC-001-CANONICAL-CONTENT')) 'FR-007; VC-004' 'Block and artifact traceability preserved'
Assert-True 'Material UNKNOWN remains visible' ($output.material_limitations[0].id -eq 'UNC-002') 'FR-008; VC-004' 'UNC-002 propagated'
Assert-True 'Projection selection is consumed, not recalculated' ($output.selected_presentation_projection -eq 'Executive Report') 'FR-002; VC-001' 'Selected projection copied from input'

$AmbiguousCommunicationContext = $CommunicationContext.Clone()
$AmbiguousCommunicationContext.Remove('supported_decision_type')

$ambiguousResult = Invoke-Spec011CommunicationContextTransformation `
    -ContextDefinition $ContextDefinition `
    -ExecutionScopeCanonicalizationResult $ExecutionScopeCanonicalizationResult `
    -SelectedPresentationProjection $SelectedPresentationProjection `
    -CommunicationContext $AmbiguousCommunicationContext `
    -PresentationContract $PresentationContract `
    -CanonicalContent $CanonicalContent `
    -OutputRequest $OutputRequest

Assert-True 'Ambiguous Communication Context blocks materialization' ($ambiguousResult.status -eq 'Blocked' -and $ambiguousResult.work_package -eq 'WP-002') 'BR-005; VC-003' ($ambiguousResult.blocking_reasons -join '; ')

$driftOutput = New-Spec011PresentationLayerOutput `
    -CanonicalContent $CanonicalContent `
    -RepresentationConstraints $output.representation_constraints `
    -SelectedPresentationProjection $SelectedPresentationProjection `
    -OutputRequest $OutputRequest
$driftOutput.output_blocks[1].priority = 'P1'
$driftOutput.output_blocks[1].text = 'Escalar inversión sobre RTG inmediatamente.'

$driftResult = Test-Spec011SemanticEquivalence -CanonicalContent $CanonicalContent -PresentationLayerOutput $driftOutput
Assert-True 'Semantic drift blocks output release' ($driftResult.status -eq 'Blocked' -and $driftResult.work_package -eq 'WP-003') 'FR-005; FR-006; VC-003' ($driftResult.blocking_reasons -join '; ')

$consumerFiles = @(
    '.github/skills/meta-lead-quality-analysis/SKILL.md',
    'docs/templates/ccd.template.md',
    'docs/handoffs/auc-001-presentation-contract.md',
    'docs/handoffs/auc-001-executive-report.md'
)
$unchangedConsumerCheckpoint = $true
foreach ($file in $consumerFiles) {
    if (-not (Test-Path -LiteralPath $file)) {
        $unchangedConsumerCheckpoint = $false
    }
}
Assert-True 'Deferred consumer alignment checkpoint remains non-blocking' $unchangedConsumerCheckpoint 'WP-005; VC-005' 'Consumer artifacts are only checked for existence by this experimental test'

$failures = $Results | Where-Object { $_.Status -ne 'PASS' }
$Results | Format-Table -AutoSize

if ($failures.Count -gt 0) {
    Write-Host "`nSPEC-011 communication context transformation tests failed: $($failures.Count)" -ForegroundColor Red
    exit 1
}

Write-Host "`nSPEC-011 communication context transformation tests passed: $($Results.Count)" -ForegroundColor Green
exit 0