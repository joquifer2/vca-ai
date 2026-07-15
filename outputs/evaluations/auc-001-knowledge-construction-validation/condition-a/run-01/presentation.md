# AUC-001 Executive Decision Support Presentation

## Metadata

| Field | Value |
|---|---|
| Artifact Type | Presentation Output |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Execution ID | VCA-AUC-001-EXEC-2026-06 |
| Period | 2026-06-01 to 2026-06-30 |
| Projection | executive-decision-support |
| Presentation Policy | Executive Decision Support |
| Source Model | `ad_quality_spend_model` |

## Executive Summary

June 2026 Meta Lead Ads evidence is sufficient for decision support at ad-reference level inside the corrected model. The strongest basis for efficiency-oriented discussion is the matched evidence: 8 ad references with both lead quality and commercial spend.

The model contains 15 prepared ad references, 772 distinct leads, 226 qualified A/B leads and 496.56 spend. Overall prepared quality rate is 29.3% and spend per qualified A/B lead is 2.20 within the approved model.

The most important management point is methodological: matched CAPTACION evidence and lead-only RTG evidence must be read separately. RTG shows lead quality evidence, but it cannot be used as matched spend-efficiency evidence without approved spend mapping.

## Key Messages

### 1. Matched evidence should guide near-term efficiency decisions

Matched rows contain 680 leads, 191 qualified A/B leads and 494.36 spend. This is the strongest current basis for efficiency-oriented decisions because both quality and spend are present.

Within matched evidence, one ad reference concentrates the largest observed signal: `120245828603090721` / `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`, with 519 leads and 152 qualified A/B leads.

Decision implication: use matched ad-level evidence first when discussing efficiency, while avoiding causal claims about creative superiority.

### 2. RTG lead-only evidence is useful, but not for spend efficiency

The RTG/CBO row contains 92 leads and 35 qualified A/B leads, with a 38.0% quality rate in lead-only coverage. Because it is lead-only in the approved model, it must not be treated as matched commercial-spend efficiency.

Decision implication: read RTG as a separate quality signal unless campaign/adset spend mapping is validated later.

### 3. Campaign/adset and creative decisions need guardrails

Campaign/adset evidence is partially supported because campaign and adset values come from lead-side metadata. Spend-only rows have UNKNOWN campaign/adset metadata.

Creative reasoning is limited to ad reference and ad name. The current evidence does not include creative asset metadata, media format, visual elements or copy attributes.

Decision implication: avoid campaign/adset spend recommendations and asset-level creative guidance until approved source coverage supports them.

## Recommended Decisions

| Priority | Recommendation | Decision Use |
|---|---|---|
| P1 | REC-001: Use matched ad-level evidence as the primary basis for efficiency-oriented decisions. | Supports near-term efficiency discussion using rows where both lead quality and commercial spend exist. |
| P1 | REC-002: Treat RTG lead-only evidence as a separate quality reading, not matched spend efficiency. | Prevents mixing quality evidence with unsupported spend-efficiency conclusions. |
| P2 | REC-003: Validate or document campaign/adset spend mapping before campaign-level spend recommendations. | Avoids unsupported campaign/adset spend decisions. |
| P2 | REC-004: Keep creative recommendations at ad-reference level unless creative asset metadata is added. | Prevents creative causality claims beyond available evidence. |
| P2 | REC-005: Preserve duplicate/test-record uncertainty in downstream decisions and final output. | Keeps lead-count certainty appropriately qualified. |
| P3 | REC-006: Exclude impressions, clicks and CTR from recommendations unless source scope is expanded. | Keeps the current output aligned with available source coverage. |

## Risks And Uncertainties

| Risk Or Uncertainty | Decision Impact |
|---|---|
| `campaign_signal` is spend-side only. | Lead rows must not be described as directly commercial. |
| Campaign/adset spend mapping is not directly available. | Campaign/adset spend recommendations are not supported in the current output. |
| Duplicate/test-record flags are not explicitly mapped. | Lead-count certainty should not be overstated. |
| Creative asset metadata is unavailable. | Creative guidance must remain at ad-reference/name level. |
| Impressions, clicks and CTR are unavailable. | Funnel-entry and CTR decisions are outside the current evidence scope. |
| Spend-only ratios are UNKNOWN. | Spend-only rows cannot support cost-per-lead or quality-rate statements. |

## Main Indicators

| Indicator | Value | Reading |
|---|---:|---|
| Prepared ads | 15 | Approved model universe for this execution. |
| Distinct leads | 772 | Lead count within corrected model scope. |
| Qualified A/B leads | 226 | Quality rule: Lead Tier A or B. |
| Prepared spend | 496.56 | Commercial spend in approved model. |
| Prepared quality rate | 29.3% | Derived from qualified A/B over distinct leads. |
| Spend per qualified A/B | 2.20 | Prepared-model ratio; not valid for spend-only rows. |

## Evidence Summary

| Coverage State | Ads | Leads | Qualified A/B | Spend | Executive Reading |
|---|---:|---:|---:|---:|---|
| matched | 8 | 680 | 191 | 494.36 | Strongest basis for efficiency-oriented reading. |
| lead_only | 5 | 92 | 35 | 0.00 | Quality evidence without matched commercial spend. |
| spend_only | 2 | 0 | 0 | 2.20 | Structurally important; ratios remain UNKNOWN. |

## Required Limitations

- This output uses only the approved canonical content for AUC-001 June 2026.
- Evidence is from `ad_quality_spend_model` at normalized ad-reference grain.
- No new evidence, BigQuery query, metric family or source expansion is introduced.
- Campaign/adset reasoning is coverage-qualified because campaign/adset metadata is lead-side only.
- Creative discussion is limited to `ad_id_norm` and `ad_name`.
- Impressions, clicks, CTR and creative asset metadata are unavailable.
- Duplicate/test-record exclusion completeness remains uncertain.
- Recommendations are documentary suggested actions and do not authorize execution by themselves.

## Traceability Annex

| Content | Source |
|---|---|
| Execution context | VCA-AUC-001-EXEC-2026-06 |
| Evidence | EVD-001, EVD-002, EVD-003, EVD-004 |
| Knowledge | INS-001, INS-002, INS-003; HYP-001, HYP-002; CON-001, CON-002; PRI-001..PRI-004; RSK-001..RSK-005; UNC-001..UNC-005 |
| Recommendations | REC-001, REC-002, REC-003, REC-004, REC-005, REC-006 |
| Presentation constraint | VCA-AUC-001-PRS-001; executive-decision-support policy |

## Equivalence Statement

This presentation preserves the semantic content of the stabilized Knowledge Set and Recommendation Set. It reorganizes the material for executive decision support without adding evidence, reconstructing knowledge, generating new recommendations, changing priorities or hiding material limitations.
