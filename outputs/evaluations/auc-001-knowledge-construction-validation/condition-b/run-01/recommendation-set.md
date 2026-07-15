# AUC-001 Recommendation Set

## Metadata

| Field | Value |
|---|---|
| Artifact Type | Recommendation Set |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Execution ID | VCA-AUC-001-EXEC-2026-06 |
| Period | 2026-06-01 to 2026-06-30 |
| Source Model | `ad_quality_spend_model` |
| Knowledge Basis | Stabilized Knowledge Set |
| Status | Stabilized |

## Scope

This Recommendation Set derives exclusively from the stabilized Knowledge Set. It does not create evidence, re-rank knowledge, execute operational actions, or authorize implementation.

Recommendation priorities express decision attention for the current AUC-001 output:

- P1: required to preserve the main decision reading.
- P2: important control for avoiding unsupported interpretation.
- P3: scope guardrail.

## Recommendations

| Recommendation ID | Priority | Suggested Action | Knowledge Links | Validation Criterion |
|---|---|---|---|---|
| REC-001 | P1 | Base near-term efficiency discussion on matched ad-level evidence first, especially the 8 matched ad references where both lead quality and commercial spend are present. | CON-001, CON-002, PRI-001, INS-001, FND-001, FND-002 | Any efficiency claim references `coverage_status = matched` and remains at ad-reference grain. |
| REC-002 | P1 | Report and reason about RTG lead-only evidence separately from matched commercial-spend efficiency evidence. | INS-002, FND-005, HYP-002, PRI-002, CON-003, UNC-005, UNC-006 | Lead-only quality statements are not presented as spend-efficiency statements. |
| REC-003 | P2 | Before issuing campaign-level or adset-level spend recommendations, validate an approved campaign/adset spend mapping or keep those recommendations out of scope. | CON-003, PRI-003, RSK-002, UNC-002, FND-007 | Campaign/adset spend recommendations are absent unless a validated mapping exists. |
| REC-004 | P2 | Keep creative-related recommendations at `ad_id_norm` / `ad_name` reference level unless approved creative asset metadata is added. | INS-001, HYP-001, HYP-003, RSK-003, UNC-004, FND-002, FND-004 | No claims are made about media, format, visual attributes, or asset-level creative causes. |
| REC-005 | P2 | Preserve duplicate/test-record uncertainty in downstream decisions and presentation. | UNC-001, RSK-005 | Lead-count language remains qualified and does not imply complete duplicate/test remediation. |
| REC-006 | P3 | Exclude impressions, clicks, and CTR from recommendations unless the approved source scope is expanded. | PRI-004, UNC-003, CON-001 | No funnel-entry or CTR recommendation appears in the current output. |

## Priority Rationale

| Priority | Recommendation IDs | Rationale |
|---|---|---|
| P1 | REC-001, REC-002 | These recommendations protect the main analytical distinction: matched evidence can support efficiency reading, while lead-only evidence can support quality reading only. |
| P2 | REC-003, REC-004, REC-005 | These recommendations prevent common overreach around campaign/adset attribution, creative causality, and lead-count certainty. |
| P3 | REC-006 | This recommendation keeps unavailable funnel-entry metrics outside the current decision frame. |

## Recommendation Details

### REC-001 - Use Matched Ad-Level Evidence First

Priority: P1

Suggested action: Use matched ad-level evidence as the primary basis for any near-term efficiency-oriented discussion.

Justification: The Knowledge Set concludes that matched rows are the strongest base for combined quality-and-spend reasoning because they contain both lead outcomes and commercial spend. The dominant matched reference concentrates much of the observed matched lead and spend signal, making ad-reference grain the most defensible starting point.

Expected impact: High qualitative impact on decision reliability.

Effort: Low to medium.

Dependencies:

- Stabilized Knowledge Set.
- Preservation of `coverage_status`.
- Ad-reference grain retained in presentation and review.

Risk: This recommendation may underuse lead-only quality evidence if stakeholders treat matched evidence as the only relevant quality lens.

Confidence: High within corrected model scope.

Validation criterion: Efficiency statements are explicitly tied to matched ad references and do not collapse all coverage states into prepared totals.

### REC-002 - Separate RTG Lead-Only Quality From Matched Efficiency

Priority: P1

Suggested action: Treat RTG lead-only evidence as a separate quality reading, not as matched spend-efficiency evidence.

Justification: Lead-only RTG/CBO evidence has its own quality signal, but the model does not provide matched commercial spend for those rows. The Knowledge Set preserves this distinction to avoid false spend comparisons.

Expected impact: High qualitative impact on methodological correctness.

Effort: Low.

Dependencies:

- `coverage_status = lead_only`.
- Visibility of the campaign/adset spend attribution limitation.

Risk: Stakeholders may expect RTG spend comparison even though the approved model cannot support it.

Confidence: High for the separation requirement; low for any spend interpretation outside the approved model.

Validation criterion: RTG lead-only observations appear as quality evidence only, with no cost-efficiency claim.

### REC-003 - Validate Campaign/Adset Spend Mapping Before Campaign-Level Spend Decisions

Priority: P2

Suggested action: Validate or document an approved campaign/adset spend mapping before campaign-level or adset-level spend recommendations are made.

Justification: Campaign/adset reasoning is partial. Available campaign/adset values are lead-side metadata, and spend-only campaign/adset metadata is UNKNOWN.

Expected impact: Medium to high qualitative impact by preventing unsupported campaign/adset conclusions.

Effort: UNKNOWN.

Dependencies:

- Future source-table decision or contract revision if campaign/adset spend attribution is required.
- Documented mapping at a grain compatible with the analysis.

Risk: Campaign-level recommendations may be delayed if a validated mapping is unavailable.

Confidence: High for the validation need; effort UNKNOWN.

Validation criterion: The current output contains no campaign/adset spend recommendation unless mapping is explicitly validated.

### REC-004 - Keep Creative Guidance At Ad-Reference Level

Priority: P2

Suggested action: Frame creative-related guidance at ad-reference level only, using `ad_id_norm` and `ad_name`, unless approved creative asset metadata is added.

Justification: The Knowledge Set identifies ad-reference concentration but also preserves that creative asset metadata is unavailable. Ad reference is not evidence of media, format, copy, or visual attributes.

Expected impact: Medium qualitative impact by reducing overinterpretation risk.

Effort: Low for wording discipline; UNKNOWN for asset-level analysis.

Dependencies:

- Ad-reference naming.
- Explicit preservation of the creative metadata limitation.

Risk: Output may feel less actionable for creative production until richer metadata exists.

Confidence: High for current scope; UNKNOWN for asset-level analysis.

Validation criterion: Creative statements remain at reference/name level and do not explain performance through asset attributes.

### REC-005 - Preserve Duplicate/Test-Record Uncertainty

Priority: P2

Suggested action: Carry duplicate/test-record uncertainty into downstream recommendation and presentation artifacts.

Justification: Duplicate/test-record flags are not explicitly mapped. Lead counts are usable under the approved model but should not be overstated as fully remediated.

Expected impact: Medium qualitative impact by improving auditability.

Effort: Low for documentation; UNKNOWN for data remediation.

Dependencies:

- Future source mapping if complete resolution is required.
- Limitation visibility in the final output.

Risk: Downstream decisions may appear more certain than evidence supports if this uncertainty is omitted.

Confidence: High for propagation requirement.

Validation criterion: Lead-volume and qualified-lead language remains qualified where certainty matters.

### REC-006 - Exclude Unavailable Funnel-Entry Metrics

Priority: P3

Suggested action: Do not make recommendations based on impressions, clicks, or CTR in the current AUC-001 output.

Justification: The corrected approved source set does not include impressions, clicks, or CTR. The Knowledge Set requires these missing evidence families to remain explicit.

Expected impact: Medium qualitative impact by keeping recommendations evidence-aligned.

Effort: Low for the current output; UNKNOWN if source expansion is requested.

Dependencies:

- Future source-table decision for funnel-entry metrics, if required.

Risk: The output may be less complete for stakeholders expecting full-funnel media diagnostics.

Confidence: High for current exclusion.

Validation criterion: The current recommendation set contains no CTR, click, or impression-based action.

## Uncertainty Propagation

| Uncertainty | Affected Recommendations | Handling |
|---|---|---|
| Duplicate/test-record flags are not explicitly mapped. | REC-005 | Preserve limitation in final output and avoid overstating lead-count certainty. |
| Spend-only campaign/adset metadata is UNKNOWN. | REC-003 | Do not issue campaign/adset spend recommendations without mapping. |
| Impressions, clicks, and CTR are unavailable. | REC-006 | Exclude from current recommendations unless source scope expands. |
| Creative asset metadata is unavailable. | REC-004 | Keep creative recommendations at ad-reference level. |
| `campaign_signal` is spend-side only. | REC-002 | Do not state that lead rows directly carry commercial signal. |
| Lead-only spend is zero by model alignment. | REC-002 | Do not convert lead-only quality evidence into cost-efficiency evidence. |

## Stabilization Statement

The Recommendation Set is stabilized for Presentation. It derives only from the stabilized Knowledge Set, preserves P1/P2/P3 priorities, and keeps all material limitations and UNKNOWNs visible.