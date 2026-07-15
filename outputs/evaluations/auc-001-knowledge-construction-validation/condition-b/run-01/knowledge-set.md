# AUC-001 Knowledge Set

## Metadata

| Field | Value |
|---|---|
| Artifact Type | Knowledge Set |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Execution ID | VCA-AUC-001-EXEC-2026-06 |
| Period | 2026-06-01 to 2026-06-30 |
| Source Model | `ad_quality_spend_model` |
| Evidence Basis | EVD-001, EVD-002, EVD-003, EVD-004 |
| Status | Stabilized |

## Scope

This Knowledge Set transforms the stabilized Evidence Set into decision-oriented knowledge for the June 2026 Meta Lead Ads analysis.

It does not create new evidence, execute new queries, formulate recommendations, or extend the approved source scope.

Qualified Lead means Lead Tier A or B. Commercial spend is represented only through the approved spend-side filter. Coverage states remain separate: `matched`, `lead_only`, and `spend_only`.

## Reasoning Boundaries

- `matched` rows support combined ad-level reasoning about lead quality and commercial spend.
- `lead_only` rows support lead-quality reasoning without matched commercial spend.
- `spend_only` rows support spend visibility only; lead quality, cost per lead, and quality rate remain UNKNOWN.
- Campaign and adset evidence is available only where lead-side metadata exists.
- Ad references are not creative asset metadata.
- Impressions, clicks, CTR, and asset-level creative attributes are unavailable.
- Duplicate/test-record exclusion is not fully evidenced by explicit mapped fields.

## Findings

| Finding ID | Finding | Evidence Links | Limit |
|---|---|---|---|
| FND-001 | The strongest combined quality-and-spend reasoning base is the `matched` coverage state, because it contains both lead outcomes and commercial spend for 8 ad references. | EVD-001, EVD-003 | Applies only inside the corrected source model and does not classify lead rows themselves as commercial. |
| FND-002 | Matched evidence is highly concentrated in one ad reference: `120245828603090721` / `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`, which accounts for 519 of 680 matched leads, 152 of 191 matched qualified leads, and 374.79 of 494.36 matched spend. | EVD-001, EVD-003 | Concentration is not proof of causal superiority or creative performance. |
| FND-003 | The largest matched ad reference has a qualified rate of 29.29%, close to the matched aggregate rate of 28.09%, so its importance comes mainly from volume and spend concentration rather than a clearly exceptional quality rate. | EVD-001, EVD-003 | This compares only approved matched ad references; it does not explain why the pattern occurs. |
| FND-004 | Several smaller matched ad references show higher qualified rates or lower spend per qualified lead than the dominant reference, but their lead counts are narrow, making them weaker as standalone conclusions. | EVD-003 | Low-volume rows are candidate signals, not stable proof of better performance. |
| FND-005 | Lead-only RTG/CBO evidence has a higher qualified rate than matched CAPTACION/ABO evidence, but it cannot support spend-efficiency reasoning because there is no matched commercial spend in the approved model. | EVD-001, EVD-004 | Lead-only spend values are model-alignment zeroes, not evidence of no real-world spend. |
| FND-006 | Spend-only evidence is numerically small but methodologically important because quality rates and cost ratios are UNKNOWN for those rows. | EVD-001, EVD-003, EVD-004 | Spend-only rows cannot be attributed to campaign/adset or quality performance. |
| FND-007 | Campaign/adset-level reasoning is partial: the available rows separate matched CAPTACION/ABO evidence from lead-only RTG/CBO evidence, while spend-only campaign/adset metadata is UNKNOWN. | EVD-004 | No unsupported campaign/adset spend attribution is allowed. |

## Insights

| Insight ID | Insight | Evidence Links | Why It Matters | Limitation |
|---|---|---|---|---|
| INS-001 | The June signal is concentrated around a limited set of matched ad references, with one reference carrying most matched lead volume, qualified leads, and spend. | EVD-001, EVD-002, EVD-003 | Near-term efficiency discussion has a defensible base at matched ad-reference grain. | This is concentration, not proof that the reference is intrinsically better. |
| INS-002 | Matched and lead-only evidence answer different questions: matched rows support quality plus spend reading, while lead-only rows support quality reading without commercial-spend efficiency. | EVD-001, EVD-004 | Mixing them would overstate what the model can support and may create false campaign comparisons. | Lead-only evidence remains useful for quality, but not for cost efficiency. |
| INS-003 | Spend-only rows are too small to drive the business story numerically, but they enforce a boundary: missing lead linkage blocks quality and cost-per-lead interpretation. | EVD-001, EVD-003 | This prevents presentation from converting spend visibility into performance interpretation. | Campaign/adset metadata and quality ratios remain UNKNOWN for spend-only rows. |
| INS-004 | The prepared totals show 772 distinct leads, 226 qualified leads, 496.56 spend, and a 29.27% qualified rate, but these totals combine different coverage states and must not be read as one uniform evidence class. | EVD-001, EVD-002 | The total is useful for orientation, while decisions need coverage-qualified interpretation. | Prepared totals are inside the approved model, not a full-funnel business universe. |

## Hypotheses

| Hypothesis ID | Hypothesis | Evidence Links | What Would Support It | What Could Refute It |
|---|---|---|---|---|
| HYP-001 | The June 2026 observed lead-quality and commercial-spend signal may be concentrated around a limited subset of matched ad references. | EVD-001, EVD-003 | Similar concentration across additional approved periods or a validated campaign/adset spend mapping. | A broader approved dataset showing distributed quality and spend across many references. |
| HYP-002 | RTG lead-quality evidence should be managed as a distinct coverage case from matched commercial-spend efficiency evidence. | EVD-001, EVD-004 | Continued presence of lead-only RTG evidence without matched spend linkage in approved models. | A future approved mapping that links RTG leads to commercial spend at comparable grain. |
| HYP-003 | Smaller matched references with strong ratios may indicate useful quality patterns, but current row volumes are too limited for stable performance claims. | EVD-003 | Repeated high quality or low spend per qualified lead across larger volumes or future periods. | Regression toward matched-average quality once more volume is observed. |

## Conclusions

| Conclusion ID | Conclusion | Evidence Links | Scope Limit |
|---|---|---|---|
| CON-001 | AUC-001 has sufficient evidence to reason about ad-level lead quality and commercial spend within the corrected model when coverage states are preserved. | EVD-001, EVD-002, EVD-003 | Excludes impressions, clicks, CTR, creative asset metadata, and direct campaign/adset spend attribution. |
| CON-002 | The most reliable efficiency-oriented reading should start from matched ad-level evidence, not prepared totals alone. | EVD-001, EVD-003 | Lead-only quality signals should remain visible but separate. |
| CON-003 | Campaign/adset-level reasoning is only partially supported and must remain coverage-qualified. | EVD-004, Evidence Contract limitations | Campaign/adset spend conclusions require an approved mapping that is not present here. |
| CON-004 | The output can support guarded decision-making, but not causal explanations about why specific ads, campaigns, adsets, or creative assets performed as observed. | EVD-003, Evidence Contract limitations | All causal and asset-level interpretations remain outside scope. |

## Reasoning Priorities

| Priority ID | Priority | Evidence Basis | Boundary |
|---|---|---|---|
| PRI-001 | Preserve matched ad-level evidence as the strongest base for spend-efficiency discussion. | EVD-001, EVD-003 | This is a reasoning priority, not an instruction to ignore lead-only quality evidence. |
| PRI-002 | Treat lead-only evidence as quality evidence without matched commercial spend. | EVD-001, EVD-004 | Do not infer absent spend behavior from model-alignment zeroes. |
| PRI-003 | Keep campaign/adset reasoning coverage-qualified. | EVD-004 | Do not infer campaign/adset spend attribution where metadata is missing. |
| PRI-004 | Propagate missing impressions, clicks, CTR, creative asset metadata, and duplicate/test-record uncertainty. | Evidence Contract limitations | Do not fill gaps by assumption. |

## Risks

| Risk ID | Risk | Evidence Basis | Required Handling |
|---|---|---|---|
| RSK-001 | Treating matched spend as direct lead-level commercial classification. | Evidence Contract limitations | Preserve that `campaign_signal` is spend-side only. |
| RSK-002 | Interpreting campaign/adset spend where approved metadata is absent. | EVD-004, Evidence Contract limitations | Avoid unsupported campaign/adset spend conclusions. |
| RSK-003 | Turning ad-reference concentration into creative causality. | EVD-003, creative metadata limitation | Keep reasoning at ad reference/name level. |
| RSK-004 | Using lead-only rows for cost-efficiency conclusions. | EVD-001, EVD-004 | Preserve `lead_only` as a separate coverage state. |
| RSK-005 | Overstating lead-count certainty despite incomplete duplicate/test-record field mapping. | Evidence Contract uncertainty notes | Keep the uncertainty visible in downstream artifacts. |
| RSK-006 | Letting prepared totals hide coverage-state differences. | EVD-001, EVD-002 | Present totals with matched, lead-only, and spend-only distinctions. |

## Uncertainties

| Uncertainty ID | Uncertainty | Effect |
|---|---|---|
| UNC-001 | Duplicate/test-record flags are not explicitly mapped. | Lead counts are usable but should not be overstated as fully remediated. |
| UNC-002 | Spend-only campaign/adset metadata is UNKNOWN. | Spend-only rows cannot support campaign/adset interpretation. |
| UNC-003 | Impressions, clicks, and CTR are unavailable. | Funnel-entry and CTR interpretations are outside scope. |
| UNC-004 | Creative asset metadata is unavailable. | Creative discussion must remain at ad reference/name level. |
| UNC-005 | `campaign_signal` is spend-side only. | Lead rows should not be described as directly carrying commercial signal. |
| UNC-006 | Lead-only spend is zero by model alignment. | Lead-only quality evidence cannot be converted into spend-efficiency evidence. |

## Stabilization Statement

The Knowledge Set is stabilized for Recommendation Generation. It derives only from the approved Evidence Set and Evidence Contract, preserves coverage states and UNKNOWNs, and does not contain recommendations.