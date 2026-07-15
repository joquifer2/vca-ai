# AUC-001 Recommendation Set

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-REC-SET-CONDITION-C-RUN-01 |
| Artifact Type | Recommendation Set |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Execution ID | VCA-AUC-001-EXEC-2026-06 |
| Period | 2026-06-01 to 2026-06-30 |
| Source Knowledge Set | VCA-AUC-001-KNW-SET-CONDITION-C-RUN-01 |
| Source Recommendation Contract | VCA-AUC-001-REC-001 |
| Status | Stabilized |

## Scope And Boundary

This Recommendation Set derives exclusively from the stabilized Knowledge Set.

It does not create evidence, reinterpret evidence, change coverage states, or introduce operational authorization.

## Recommendation Summary

| Recommendation ID | Priority | Action Summary | Knowledge Links |
|---|---|---|---|
| REC-001 | P1 | Use matched ad-level evidence as the primary basis for efficiency-oriented decisions. | INS-001; CON-001; PRI-001 |
| REC-002 | P1 | Treat RTG lead-only evidence as a separate quality reading, not matched spend efficiency. | INS-003; CON-002; PRI-002 |
| REC-003 | P2 | Validate or document campaign/adset spend mapping before campaign-level spend recommendations. | INS-005; CON-004; RSK-004 |
| REC-004 | P2 | Keep creative recommendations at ad-reference level unless creative asset metadata is added. | INS-002; RSK-003; UNC-004 |
| REC-005 | P2 | Preserve duplicate/test-record uncertainty in downstream decisions and final output. | RSK-005; UNC-001 |
| REC-006 | P3 | Exclude impressions, clicks and CTR from current recommendations unless source scope is expanded. | PRI-005; RSK-006; UNC-003 |

## Detailed Recommendations

### REC-001 - Base efficiency discussion on matched ad-level evidence

Priority: P1.

Suggested action: Use the 8 matched ad references as the primary evidence base for near-term efficiency discussion because those rows contain both lead quality and commercial spend.

Justification: The Knowledge Set concludes that matched ad-level evidence is the strongest basis for efficiency-oriented interpretation inside the corrected model.

Expected impact: High qualitative impact on decision reliability.

Effort: Low to medium.

Dependencies: Stabilized Knowledge Set; preservation of `coverage_status`.

Risks: May underuse lead-only quality evidence if mistakenly treated as the only valid quality lens.

Validation criterion: Any efficiency statement can be traced to matched ad-level evidence and does not claim direct commercial classification of lead rows.

### REC-002 - Separate RTG lead-only quality from matched spend efficiency

Priority: P1.

Suggested action: Present RTG lead-only evidence as a distinct quality reading and do not compare it as spend efficiency against matched commercial-spend evidence.

Justification: Lead-only evidence has observable quality information, but the Knowledge Set preserves its lack of matched commercial spend.

Expected impact: High qualitative impact on methodological correctness.

Effort: Low.

Dependencies: `coverage_status = lead_only`; campaign/adset spend attribution limitation.

Risks: Stakeholders may expect RTG efficiency comparison that the current model cannot support.

Validation criterion: RTG lead-only references are not used for CPL, spend-per-qualified, or campaign/adset spend conclusions.

### REC-003 - Validate campaign/adset spend mapping before campaign-level spend recommendations

Priority: P2.

Suggested action: Before making campaign-level spend recommendations, either validate an approved campaign/adset spend mapping or keep campaign/adset spend recommendations explicitly out of scope.

Justification: Campaign/adset reasoning is partially supported, but current campaign/adset values are lead-side metadata and spend-only campaign/adset metadata is UNKNOWN.

Expected impact: Medium to high qualitative impact by preventing unsupported attribution.

Effort: UNKNOWN.

Dependencies: Future approved source-table decision or data-contract revision if campaign/adset spend attribution is required.

Risks: Campaign-level recommendations may be delayed if mapping remains unavailable.

Validation criterion: No campaign/adset spend recommendation appears without approved mapping.

### REC-004 - Keep creative guidance at ad-reference level

Priority: P2.

Suggested action: Frame any creative-related discussion at `ad_id_norm` / `ad_name` reference level only.

Justification: The Knowledge Set identifies ad-reference concentration, but creative asset metadata is unavailable and concentration does not prove creative causality.

Expected impact: Medium qualitative impact by reducing overinterpretation risk.

Effort: Low for wording discipline; UNKNOWN for asset-level analysis.

Dependencies: Ad-reference naming; explicit creative metadata limitation.

Risks: Limits creative production guidance until richer creative metadata exists.

Validation criterion: The output does not make claims about media, format, visual attributes, or copy attributes.

### REC-005 - Preserve duplicate/test-record uncertainty

Priority: P2.

Suggested action: Keep the duplicate/test-record limitation visible wherever lead counts, quality rates, or decision confidence are summarized.

Justification: The Knowledge Set identifies this as a material uncertainty affecting lead-count certainty.

Expected impact: Medium qualitative impact by improving auditability.

Effort: Low for documentation; UNKNOWN for data remediation.

Dependencies: Future source mapping required for full resolution.

Risks: If omitted, downstream materials may appear more certain than the evidence supports.

Validation criterion: Final presentation includes the duplicate/test-record limitation near the decision-relevant summary or limitations section.

### REC-006 - Exclude unavailable funnel-entry metrics

Priority: P3.

Suggested action: Do not make recommendations based on impressions, clicks, CTR, or funnel-entry behavior in the current AUC-001 output.

Justification: The Knowledge Set preserves impressions, clicks, and CTR as unavailable in the corrected source scope.

Expected impact: Medium qualitative impact by keeping recommendations evidence-aligned.

Effort: Low for current output; UNKNOWN if source expansion is requested.

Dependencies: Future approved source expansion if funnel-entry metrics are required.

Risks: The output may feel less complete for stakeholders expecting full-funnel analysis.

Validation criterion: No recommendation uses impressions, clicks, CTR, or funnel-entry interpretation.

## Priority Contract

| Priority | Recommendation IDs | Rationale |
|---|---|---|
| P1 | REC-001; REC-002 | Highest need to preserve valid quality and efficiency interpretation from coverage-separated knowledge |
| P2 | REC-003; REC-004; REC-005 | Important controls for campaign/adset, creative, and data-quality uncertainty |
| P3 | REC-006 | Scope guardrail for unavailable funnel-entry metrics |

## Uncertainty Propagation

| Uncertainty | Affected Recommendations | Handling |
|---|---|---|
| UNC-001 duplicate/test-record flags not explicitly mapped | REC-005 | Preserve limitation in downstream artifacts |
| UNC-002 spend-only campaign/adset metadata UNKNOWN | REC-003 | Do not issue campaign/adset spend recommendations without mapping |
| UNC-003 impressions/clicks/CTR unavailable | REC-006 | Exclude from current recommendations unless source scope expands |
| UNC-004 creative asset metadata unavailable | REC-004 | Keep creative discussion at ad-reference level |
| UNC-005 `campaign_signal` spend-side only | REC-001; REC-002 | Do not describe lead rows as directly commercial |

## Stabilization Statement

This Recommendation Set is stabilized for Presentation Layer.

Presentation may reorganize, summarize, and adapt vocabulary, but must not add recommendations, change priorities, remove limitations, or alter traceability.
