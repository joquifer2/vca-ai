# AUC-001 Knowledge Set

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-KNW-SET-CONDITION-C-RUN-01 |
| Artifact Type | Knowledge Set |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Execution ID | VCA-AUC-001-EXEC-2026-06 |
| Period | 2026-06-01 to 2026-06-30 |
| Source Evidence Contract | VCA-AUC-001-EVD-001 |
| Source Evidence Set | VCA-AUC-001-EVD-SET-001 |
| Knowledge Construction Profile | v0.2 |
| Status | Stabilized |

## Scope And Boundary

This Knowledge Set transforms the authorized Evidence Set into consolidated knowledge for AUC-001.

It does not create new evidence, execute new queries, introduce new metrics, or formulate recommendations.

The approved quality rule is:

Qualified Lead = Lead Tier A or B.

The approved evidence scope is June 2026 Meta Lead Ads evidence from `ad_quality_spend_model`, at normalized `ad_id` grain.

## Evidence Basis

| Evidence ID | Role In Knowledge Generation |
|---|---|
| EVD-001 | Coverage-state comparison across `matched`, `lead_only`, and `spend_only` |
| EVD-002 | Prepared model totals for overall quality and spend context |
| EVD-003 | Ad-reference distribution, concentration, cost, and quality comparison |
| EVD-004 | Campaign/adset evidence where lead-side metadata exists |

## Knowledge Construction Notes

The strongest reading emerges only after separating coverage states. The aggregate model total is useful as context, but it mixes three structurally different evidence types:

- `matched`: lead quality and commercial spend are both present.
- `lead_only`: lead quality is present without matched commercial spend in the approved model.
- `spend_only`: spend is present without lead quality ratios.

Because these states do not support the same interpretation, the Knowledge Set treats coverage status as a primary explanatory variable.

## Findings

### FND-001 - Matched evidence carries the strongest efficiency reading

The 8 `matched` ad references contain 680 leads, 191 qualified A/B leads, and 494.36 spend. This is the only coverage state where lead quality and commercial spend can be read together.

This matters because efficiency-oriented reasoning is materially safer at matched ad-reference level than at total, campaign/adset, lead-only, or spend-only level.

Evidence links: EVD-001, EVD-002, EVD-003.

Limits: `campaign_signal` is spend-side only; matched evidence does not mean the lead rows themselves carry commercial classification.

### FND-002 - The matched signal is highly concentrated in one ad reference

Ad `120245828603090721` / `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1` accounts for 519 of 680 matched leads and 152 of 191 matched qualified A/B leads. It also carries 374.79 of 494.36 matched spend.

This is informative because the main matched reading is not evenly distributed across ads. Any overall efficiency or quality statement is substantially shaped by this one reference.

Evidence links: EVD-001, EVD-003.

Limits: concentration is not superiority, causality, or creative proof. Creative asset metadata is unavailable.

### FND-003 - Smaller matched ads show stronger quality or cost ratios, but with weaker volume robustness

Several smaller matched references show higher qualified rates or lower spend per qualified A/B than the dominant matched ad. For example, `ViajaComoInvitado_Estatus_ExperienciaCalidad_Reel_v1` has 4 qualified A/B out of 8 leads and 1.09 spend per qualified A/B, while `ViajeSinEstres_PrevencionDeRiesgo_ErroresViaje_Reel_v1` has 3 qualified A/B out of 9 leads and 1.17 spend per qualified A/B.

This matters because the apparent best ratio is not necessarily the most decision-stable signal. Volume changes the robustness of the interpretation.

Evidence links: EVD-003.

Limits: small denominators make these observations fragile. They support comparative reading, not definitive performance ranking.

### FND-004 - Lead-only RTG evidence is quality evidence, not matched spend efficiency evidence

The `lead_only` coverage state contains 92 leads and 35 qualified A/B leads, with a 38.04% qualified rate. This is higher than the `matched` qualified rate of 28.09%, but the spend field is zero by model alignment.

This changes the reading because RTG lead quality should not be collapsed into the matched efficiency view. It may be relevant for quality interpretation, but it cannot support cost-efficiency conclusions in the current model.

Evidence links: EVD-001, EVD-004.

Limits: lead-only rows do not prove absence of spend outside the approved model; they only state lack of matched commercial spend in this model.

### FND-005 - Campaign/adset interpretation is structurally partial

Campaign/adset evidence separates a matched CAPTACION/ABO row from a lead-only RTG/CBO row, but campaign/adset values come from lead-side metadata and spend-only rows have UNKNOWN campaign/adset metadata.

This matters because campaign/adset-level decisions would overstate the evidence if they treated the current model as a full spend attribution source.

Evidence links: EVD-004; Evidence Contract limitations.

Limits: no direct campaign/adset spend mapping exists in the approved evidence scope.

### FND-006 - Spend-only rows are financially small but methodologically important

The `spend_only` state contains 2 ad references and 2.20 spend, with no leads and UNKNOWN quality or cost-per-lead ratios.

This matters because its monetary weight is small, but it marks a boundary: not every spend row can be converted into lead-quality or efficiency knowledge.

Evidence links: EVD-001, EVD-003.

Limits: no lead-quality, CPL, or campaign/adset interpretation is authorized for spend-only rows.

### FND-007 - The prepared total is decision-useful only when coverage limitations remain attached

The prepared model total is 772 leads, 226 qualified A/B leads, 496.56 spend, 29.27% qualified rate, and 2.20 spend per qualified A/B.

This matters because the total is compact and useful for orientation, but it combines matched, lead-only, and spend-only evidence. Reading it without coverage states would blur quality and efficiency boundaries.

Evidence links: EVD-001, EVD-002.

Limits: totals are prepared-model totals, not a complete business universe beyond the approved scope.

## Insights

| Insight ID | Insight | Evidence Links | Limit |
|---|---|---|---|
| INS-001 | The strongest efficiency-readable evidence is the matched ad-level subset, not the aggregate total. | EVD-001, EVD-002, EVD-003 | Applies only inside corrected model scope |
| INS-002 | Matched evidence is materially concentrated in one ad reference, making aggregate interpretation sensitive to that reference. | EVD-001, EVD-003 | Concentration does not prove causality or creative superiority |
| INS-003 | Lead-only RTG evidence has a stronger observed quality rate than matched evidence, but cannot be used for matched spend efficiency. | EVD-001, EVD-004 | Lead-only spend behavior outside the model remains unproven |
| INS-004 | Smaller matched ads contain potentially interesting quality/cost signals, but lower volume weakens robustness. | EVD-003 | Not sufficient for definitive ranking |
| INS-005 | Campaign/adset reasoning is coverage-qualified because metadata and spend attribution are incomplete at that level. | EVD-004; limitations | No unsupported campaign/adset spend conclusions |
| INS-006 | Spend-only rows are a boundary marker for UNKNOWN ratios rather than a basis for quality interpretation. | EVD-001, EVD-003 | Quality and CPL remain UNKNOWN |

## Hypotheses

| Hypothesis ID | Hypothesis | Evidence Links | Validation Condition |
|---|---|---|---|
| HYP-001 | June 2026 lead quality and commercial spend may be concentrated around a limited subset of matched ad references. | EVD-001, EVD-003 | Validate with additional periods before treating as stable pattern |
| HYP-002 | RTG lead-only evidence may represent a distinct quality pattern from matched CAPTACION/ABO evidence. | EVD-001, EVD-004 | Requires approved spend mapping before efficiency comparison |
| HYP-003 | Some lower-volume matched ads may merit closer review because their quality/cost ratios differ materially from the dominant ad. | EVD-003 | Requires robustness checks with larger volume or repeated periods |

## Conclusions

| Conclusion ID | Conclusion | Evidence Links | Scope Limit |
|---|---|---|---|
| CON-001 | AUC-001 has sufficient evidence to reason about ad-level lead quality and commercial spend where coverage is `matched`. | EVD-001, EVD-002, EVD-003 | Excludes impressions, clicks, CTR, creative asset metadata, and direct campaign/adset spend attribution |
| CON-002 | Coverage state is the key constraint for valid interpretation; `matched`, `lead_only`, and `spend_only` must remain separate. | EVD-001, EVD-004 | No coverage state may inherit the interpretive rights of another |
| CON-003 | The dominant matched ad reference shapes the overall matched reading, so total-level conclusions are less robust than coverage-qualified ad-level readings. | EVD-001, EVD-003 | Does not imply the ad is causally better |
| CON-004 | Campaign/adset-level reasoning is only partially supported and must remain documentary, not spend-prescriptive. | EVD-004; limitations | Requires approved mapping for spend recommendations |

## Reasoning Priorities

| Priority ID | Priority | Basis | Boundary |
|---|---|---|---|
| PRI-001 | Read matched ad-level evidence first for efficiency-oriented interpretation. | INS-001, CON-001 | Not an action priority |
| PRI-002 | Preserve coverage-state separation before using totals. | INS-003, INS-006, CON-002 | Do not collapse lead-only or spend-only into matched |
| PRI-003 | Treat concentration as a robustness issue, not as proof of superiority. | INS-002, CON-003 | No causal claim |
| PRI-004 | Keep campaign/adset and creative interpretations limited to authorized metadata. | INS-005, CON-004 | No asset-level or unsupported spend attribution |
| PRI-005 | Propagate missing evidence families into downstream artifacts. | UNC-001..UNC-005 | Do not fill gaps by assumption |

## Risks

| Risk ID | Risk | Source | Required Handling |
|---|---|---|---|
| RSK-001 | Treating matched spend as direct commercial classification of lead rows. | UNC-005 | Preserve spend-side-only `campaign_signal` boundary |
| RSK-002 | Using lead-only RTG rows for cost-efficiency claims. | FND-004 | Keep quality and efficiency readings separate |
| RSK-003 | Treating ad-reference concentration as creative causality. | FND-002; UNC-004 | Keep claims at ad-reference/name level |
| RSK-004 | Issuing campaign/adset spend conclusions without spend mapping. | FND-005; UNC-002 | Keep campaign/adset reasoning coverage-qualified |
| RSK-005 | Overstating lead-count certainty because duplicate/test flags are not explicitly mapped. | UNC-001 | Keep data-quality limitation visible |
| RSK-006 | Creating funnel-entry conclusions from unavailable impressions, clicks, or CTR. | UNC-003 | Exclude those interpretations |

## Uncertainties

| Uncertainty ID | Uncertainty | Effect |
|---|---|---|
| UNC-001 | Duplicate/test-record flags are not explicitly mapped. | Lead counts are usable but certainty must not be overstated |
| UNC-002 | Spend-only campaign/adset metadata is UNKNOWN. | Spend-only rows cannot support campaign/adset interpretation |
| UNC-003 | Impressions, clicks and CTR are unavailable. | Funnel-entry analysis is out of scope |
| UNC-004 | Creative asset metadata is unavailable. | Creative reasoning remains at ad-reference/name level |
| UNC-005 | `campaign_signal` is spend-side only. | Lead rows must not be described as directly commercial |

## Stabilization Statement

This Knowledge Set is stabilized for downstream Recommendation Generation.

Recommendations may derive from this Knowledge Set, but must preserve coverage states, limitations, uncertainties, and the boundary between quality evidence and efficiency evidence.
