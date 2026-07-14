$ErrorActionPreference = 'Stop'

function New-Spec011Result {
    param(
        [Parameter(Mandatory = $true)][string]$Status,
        [Parameter(Mandatory = $true)][string]$WorkPackage,
        [string[]]$Evidence = @(),
        [string[]]$BlockingReasons = @(),
        [hashtable]$Data = @{}
    )

    [pscustomobject]@{
        status = $Status
        work_package = $WorkPackage
        evidence = $Evidence
        blocking_reasons = $BlockingReasons
        data = $Data
    }
}

function Get-Spec011MissingField {
    param(
        [Parameter(Mandatory = $true)][hashtable]$InputObject,
        [Parameter(Mandatory = $true)][string[]]$Fields
    )

    $missing = @()
    foreach ($field in $Fields) {
        if (-not $InputObject.ContainsKey($field) -or $null -eq $InputObject[$field] -or [string]::IsNullOrWhiteSpace([string]$InputObject[$field])) {
            $missing += $field
        }
    }
    return $missing
}

function Test-Spec011BoundaryInput {
    param(
        [Parameter(Mandatory = $true)][hashtable]$ContextDefinition,
        [Parameter(Mandatory = $true)][hashtable]$ExecutionScopeCanonicalizationResult,
        [Parameter(Mandatory = $true)][hashtable]$SelectedPresentationProjection,
        [Parameter(Mandatory = $true)][hashtable]$PresentationContract,
        [Parameter(Mandatory = $true)][hashtable]$CanonicalContent
    )

    $reasons = @()

    $contextMissing = Get-Spec011MissingField $ContextDefinition @('context_id', 'audience', 'purpose', 'decision_supported')
    if ($contextMissing.Count -gt 0) {
        $reasons += 'Context Definition is incomplete: ' + ($contextMissing -join ', ')
    }

    $executionStatus = [string]$ExecutionScopeCanonicalizationResult['status']
    if ($executionStatus -notin @('Frozen', 'Canonicalized')) {
        $reasons += 'Execution Scope Canonicalization Result must be Frozen or Canonicalized before representation transformation.'
    }

    $projectionStatus = [string]$SelectedPresentationProjection['status']
    if ($projectionStatus -ne 'Selected') {
        $reasons += 'Selected Presentation Projection must be already selected before transformation.'
    }

    if ($SelectedPresentationProjection.ContainsKey('candidate_projections')) {
        $reasons += 'Projection candidates were supplied to transformation; projection selection is out of scope for SPEC-011.'
    }

    $boundaryStatus = [string]$PresentationContract['boundary_status']
    if ($boundaryStatus -ne 'No new evidence, interpretation or prioritization') {
        $reasons += 'Presentation Contract boundary status does not explicitly prevent new evidence, interpretation and prioritization.'
    }

    if (-not $CanonicalContent.ContainsKey('content_blocks') -or $CanonicalContent['content_blocks'].Count -eq 0) {
        $reasons += 'Canonical content must contain approved content_blocks.'
    }

    if ($reasons.Count -gt 0) {
        return New-Spec011Result -Status 'Blocked' -WorkPackage 'WP-001' -Evidence @('SPEC-011 FR-002', 'SPEC-011 AC-007', 'ARCH-003 boundaries') -BlockingReasons $reasons
    }

    return New-Spec011Result -Status 'Ready' -WorkPackage 'WP-001' -Evidence @('Execution scope is frozen', 'Presentation projection is selected', 'Presentation boundary is explicit')
}

function New-Spec011RepresentationConstraints {
    param(
        [Parameter(Mandatory = $true)][hashtable]$CommunicationContext,
        [Parameter(Mandatory = $true)][hashtable]$CanonicalContent,
        [Parameter(Mandatory = $true)][hashtable]$PresentationContract
    )

    $required = @(
        'audience',
        'communicative_purpose',
        'supported_decision_type',
        'abstraction_level',
        'information_density',
        'traceability_visibility',
        'format_constraints'
    )

    $missing = Get-Spec011MissingField $CommunicationContext $required
    if ($missing.Count -gt 0) {
        return New-Spec011Result -Status 'Blocked' -WorkPackage 'WP-002' -Evidence @('SPEC-011 BR-001', 'SPEC-011 BR-005') -BlockingReasons @('Communication Context is ambiguous or incomplete: ' + ($missing -join ', '))
    }

    $constraints = [ordered]@{
        audience = $CommunicationContext['audience']
        communicative_purpose = $CommunicationContext['communicative_purpose']
        supported_decision_type = $CommunicationContext['supported_decision_type']
        abstraction_level = $CommunicationContext['abstraction_level']
        information_density = $CommunicationContext['information_density']
        traceability_visibility = $CommunicationContext['traceability_visibility']
        format_constraints = $CommunicationContext['format_constraints']
        experimental_active_dimension = 'traceability_visibility'
        deferred_dimensions = @('abstraction_level', 'information_density', 'vocabulary', 'narrative_organization', 'terminological_transformation', 'structural_transformation', 'abstraction_transformation', 'information_density_transformation')
        allowed_transformations = @('traceability_visibility')
        prohibited_changes = @('new_evidence', 'new_reasoning', 'new_interpretation', 'new_recommendation', 'priority_rewrite', 'coverage_change')
        material_limitations_required = $true
        canonical_artifact_id = $CanonicalContent['artifact_id']
        presentation_contract_id = $PresentationContract['contract_id']
    }

    return New-Spec011Result -Status 'Ready' -WorkPackage 'WP-002' -Evidence @('Communication Context derived into Representation Constraints before transformation', 'Experimental active dimension is traceability_visibility; remaining SPEC-011 dimensions are deferred') -Data @{ representation_constraints = [pscustomobject]$constraints }
}

function New-Spec011PresentationLayerOutput {
    param(
        [Parameter(Mandatory = $true)][hashtable]$CanonicalContent,
        [Parameter(Mandatory = $true)][pscustomobject]$RepresentationConstraints,
        [Parameter(Mandatory = $true)][hashtable]$SelectedPresentationProjection,
        [Parameter(Mandatory = $true)][hashtable]$OutputRequest
    )

    $blocks = @()
    foreach ($block in $CanonicalContent['content_blocks']) {
        $sourceRefs = @($block['traceability'])
        if ($RepresentationConstraints.traceability_visibility -eq 'summary') {
            $sourceRefs = @($block['id'])
        }

        $blocks += [pscustomobject]@{
            source_block_id = $block['id']
            block_type = $block['type']
            text = $block['text']
            priority = $block['priority']
            traceability = $sourceRefs
            limitations = @($block['limitations'])
        }
    }

    [pscustomobject]@{
        output_request_id = $OutputRequest['request_id']
        selected_presentation_projection = $SelectedPresentationProjection['name']
        communication_fit = 'Compatible with declared Communication Context'
        semantic_equivalence_status = 'Pending verification'
        boundary_status = 'No new evidence, interpretation or prioritization introduced'
        representation_constraints = $RepresentationConstraints
        output_blocks = $blocks
        material_limitations = @($CanonicalContent['limitations'])
        traceability = @(
            $CanonicalContent['artifact_id'],
            $RepresentationConstraints.presentation_contract_id,
            $SelectedPresentationProjection['source']
        )
    }
}

function Test-Spec011SemanticEquivalence {
    param(
        [Parameter(Mandatory = $true)][hashtable]$CanonicalContent,
        [Parameter(Mandatory = $true)][pscustomobject]$PresentationLayerOutput
    )

    $reasons = @()
    $canonicalById = @{}
    foreach ($block in $CanonicalContent['content_blocks']) {
        $canonicalById[$block['id']] = $block
    }

    foreach ($outputBlock in $PresentationLayerOutput.output_blocks) {
        if (-not $canonicalById.ContainsKey($outputBlock.source_block_id)) {
            $reasons += "Output block '$($outputBlock.source_block_id)' is not traceable to canonical content."
            continue
        }

        $source = $canonicalById[$outputBlock.source_block_id]
        if ([string]$outputBlock.text -ne [string]$source['text']) {
            $reasons += "Output block '$($outputBlock.source_block_id)' changes canonical text without an approved equivalence verifier."
        }
        if ([string]$outputBlock.priority -ne [string]$source['priority']) {
            $reasons += "Output block '$($outputBlock.source_block_id)' changes approved priority."
        }

        foreach ($limitation in @($source['limitations'])) {
            if ($limitation -and @($outputBlock.limitations) -notcontains $limitation) {
                $reasons += "Output block '$($outputBlock.source_block_id)' omits material limitation '$limitation'."
            }
        }
    }

    if ($CanonicalContent.ContainsKey('limitations')) {
        foreach ($limitation in @($CanonicalContent['limitations'])) {
            if ($null -eq $limitation) { continue }
            $limitationId = if ($limitation -is [hashtable] -and $limitation.ContainsKey('id')) { $limitation['id'] } else { [string]$limitation }
            $visible = $false
            foreach ($visibleLimitation in @($PresentationLayerOutput.material_limitations)) {
                $visibleId = if ($visibleLimitation -is [hashtable] -and $visibleLimitation.ContainsKey('id')) { $visibleLimitation['id'] } else { [string]$visibleLimitation }
                if ($visibleId -eq $limitationId) { $visible = $true }
            }
            if (-not $visible) {
                $reasons += "Material limitation '$limitationId' is not visible in the output."
            }
        }
    }

    if ($reasons.Count -gt 0) {
        return New-Spec011Result -Status 'Blocked' -WorkPackage 'WP-003' -Evidence @('SPEC-011 FR-003', 'SPEC-011 FR-005', 'SPEC-011 FR-006', 'SPEC-011 AC-006') -BlockingReasons $reasons
    }

    $PresentationLayerOutput.semantic_equivalence_status = 'Verified by canonical block preservation'
    return New-Spec011Result -Status 'Ready' -WorkPackage 'WP-003' -Evidence @('Semantic equivalence verified', 'No priority rewrite detected', 'Material limitations remain visible') -Data @{ presentation_layer_output = $PresentationLayerOutput }
}

function Invoke-Spec011CommunicationContextTransformation {
    param(
        [Parameter(Mandatory = $true)][hashtable]$ContextDefinition,
        [Parameter(Mandatory = $true)][hashtable]$ExecutionScopeCanonicalizationResult,
        [Parameter(Mandatory = $true)][hashtable]$SelectedPresentationProjection,
        [Parameter(Mandatory = $true)][hashtable]$CommunicationContext,
        [Parameter(Mandatory = $true)][hashtable]$PresentationContract,
        [Parameter(Mandatory = $true)][hashtable]$CanonicalContent,
        [Parameter(Mandatory = $true)][hashtable]$OutputRequest
    )

    $boundary = Test-Spec011BoundaryInput -ContextDefinition $ContextDefinition -ExecutionScopeCanonicalizationResult $ExecutionScopeCanonicalizationResult -SelectedPresentationProjection $SelectedPresentationProjection -PresentationContract $PresentationContract -CanonicalContent $CanonicalContent
    if ($boundary.status -ne 'Ready') { return $boundary }

    $constraintResult = New-Spec011RepresentationConstraints -CommunicationContext $CommunicationContext -CanonicalContent $CanonicalContent -PresentationContract $PresentationContract
    if ($constraintResult.status -ne 'Ready') { return $constraintResult }

    $output = New-Spec011PresentationLayerOutput -CanonicalContent $CanonicalContent -RepresentationConstraints $constraintResult.data.representation_constraints -SelectedPresentationProjection $SelectedPresentationProjection -OutputRequest $OutputRequest
    $equivalence = Test-Spec011SemanticEquivalence -CanonicalContent $CanonicalContent -PresentationLayerOutput $output
    if ($equivalence.status -ne 'Ready') { return $equivalence }

    return New-Spec011Result -Status 'Materialized' -WorkPackage 'WP-004' -Evidence @('Presentation Layer Output materialized', 'Traceability visibility transformed experimentally', 'Boundary status preserved') -Data @{ presentation_layer_output = $equivalence.data.presentation_layer_output }
}

Export-ModuleMember -Function @(
    'Test-Spec011BoundaryInput',
    'New-Spec011RepresentationConstraints',
    'New-Spec011PresentationLayerOutput',
    'Test-Spec011SemanticEquivalence',
    'Invoke-Spec011CommunicationContextTransformation'
)