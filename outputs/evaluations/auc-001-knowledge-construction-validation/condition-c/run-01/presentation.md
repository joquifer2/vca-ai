# AUC-001 Executive Decision Support Presentation

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-PRS-CONDITION-C-RUN-01 |
| Artifact Type | Presentation |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Execution ID | VCA-AUC-001-EXEC-2026-06 |
| Period | 2026-06-01 to 2026-06-30 |
| Projection | executive-decision-support |
| Presentation Policy | Executive Decision Support |
| Source Knowledge Set | VCA-AUC-001-KNW-SET-CONDITION-C-RUN-01 |
| Source Recommendation Set | VCA-AUC-001-REC-SET-CONDITION-C-RUN-01 |
| Status | Final |

## Executive Summary

For June 2026, AUC-001 can support decision-making about Meta Lead Ads quality and spend, but only when coverage states remain separated.

The strongest decision base is the matched ad-level subset: 8 ad references where both lead quality and commercial spend are present. This subset contains 680 leads, 191 qualified A/B leads, and 494.36 spend.

The total prepared model shows 772 leads, 226 qualified A/B leads, 496.56 spend, and a 29.27% qualified rate. That total is useful for orientation, but it should not be used alone because it mixes matched, lead-only, and spend-only evidence.

The most important decision constraint is that RTG lead-only evidence has quality signal but cannot support spend-efficiency conclusions in the current model.

## Key Messages

### 1. Use matched ad-level evidence for efficiency decisions

Matched rows are the only part of the evidence where lead quality and commercial spend can be read together. They are therefore the safest basis for near-term efficiency discussion.

Decision impact: Efficiency conversations should start from matched ad references, not from total rows or campaign/adset summaries.

Traceability: INS-001; CON-001; REC-001; EVD-001; EVD-003.

### 2. The matched result is concentrated

One ad reference, `120245828603090721` / `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`, accounts for most matched leads, qualified A/B leads, and matched spend.

Decision impact: Total matched performance is sensitive to this reference. The concentration is meaningful, but it is not proof that the creative asset is causally superior.

Traceability: INS-002; CON-003; REC-004; EVD-003.

### 3. RTG lead-only evidence must be read separately

The RTG lead-only row has 92 leads and 35 qualified A/B leads, with a 38.04% qualified rate. This supports a quality reading, but not a spend-efficiency reading.

Decision impact: RTG can be discussed as quality evidence, but should not be compared against matched spend efficiency until spend mapping is approved.

Traceability: INS-003; CON-002; REC-002; EVD-001; EVD-004.

### 4. Campaign/adset decisions need more mapping before spend recommendations

Campaign/adset metadata is partial. Spend-only rows do not have campaign/adset metadata, and campaign/adset values in the current evidence are lead-side metadata.

Decision impact: Campaign-level spend recommendations should wait for validated campaign/adset spend mapping or remain explicitly out of scope.

Traceability: INS-005; CON-004; REC-003; EVD-004.

## Recommended Decisions

| Priority | Recommendation | Decision Use |
|---|---|---|
| P1 | Use matched ad-level evidence as the primary basis for efficiency-oriented decisions. | Sets the main evidence base for efficiency discussion |
| P1 | Treat RTG lead-only evidence as a separate quality reading, not matched spend efficiency. | Prevents unsupported RTG efficiency comparison |
| P2 | Validate or document campaign/adset spend mapping before campaign-level spend recommendations. | Avoids unsupported campaign/adset spend decisions |
| P2 | Keep creative recommendations at ad-reference level unless creative asset metadata is added. | Prevents creative causality claims |
| P2 | Preserve duplicate/test-record uncertainty in downstream decisions and final output. | Keeps lead-count confidence appropriately bounded |
| P3 | Exclude impressions, clicks and CTR from recommendations unless source scope is expanded. | Prevents unsupported full-funnel recommendations |

## Main Indicators

| Indicator | Value | Executive Reading |
|---|---:|---|
| Prepared ads | 15 | Approved model scope for June 2026 |
| Total leads | 772 | Usable as prepared-model total with duplicate/test limitation |
| Qualified A/B leads | 226 | Approved quality rule: Lead Tier A or B |
| Total qualified rate | 29.27% | Orientation metric; must be read with coverage states |
| Total spend | 496.56 | Prepared-model commercial spend |
| Spend per qualified A/B | 2.20 | Orientation metric; not valid for spend-only rows |
| Matched leads | 680 | Strongest efficiency-readable subset |
| Matched qualified A/B leads | 191 | Main quality base for matched efficiency |
| Lead-only leads | 92 | Quality-readable but not spend-efficiency-readable |
| Spend-only spend | 2.20 | Ratios remain UNKNOWN |

## Risks And Uncertainties

| Risk Or Uncertainty | Decision Impact |
|---|---|
| Duplicate/test-record flags are not explicitly mapped | Lead counts are usable but certainty should not be overstated |
| `campaign_signal` is spend-side only | Lead rows should not be described as directly commercial |
| Campaign/adset spend mapping is incomplete | Campaign-level spend recommendations are not supported yet |
| Creative asset metadata is unavailable | Creative claims must remain at ad-reference/name level |
| Impressions, clicks and CTR are unavailable | Full-funnel recommendations are out of scope |
| Spend-only ratios are UNKNOWN | Spend-only rows cannot support CPL or quality-rate conclusions |

## Evidence Summary

The evidence base contains four approved blocks:

| Evidence Block | What It Supports | Boundary |
|---|---|---|
| EVD-001 | Coverage-state comparison | Must preserve `matched`, `lead_only`, and `spend_only` distinctions |
| EVD-002 | Prepared model totals | Not a complete universe beyond approved scope |
| EVD-003 | Ad-reference evidence | No creative asset interpretation |
| EVD-004 | Campaign/adset evidence where available | Campaign/adset reasoning remains coverage-qualified |

## Traceability

| Presentation Content | Canonical Source |
|---|---|
| Scope and period | AUC-001 Execution Context |
| Evidence | AUC-001 Evidence Set; AUC-001 Evidence Contract |
| Knowledge messages | Condition C Knowledge Set; AUC-001 Knowledge Contract |
| Recommendations | Condition C Recommendation Set; AUC-001 Recommendation Contract |
| Presentation constraints | AUC-001 Presentation Contract; Executive Decision Support policy |

## Final Boundary Statement

This presentation preserves the canonical content and does not add evidence, knowledge, or recommendations.

The output is suitable for executive decision support within the June 2026 AUC-001 scope, with limitations and UNKNOWNs kept visible.
