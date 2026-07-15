# AUC-001 Knowledge Set

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-KNW-SET-001 |
| Artifact Type | Knowledge Set |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Execution ID | VCA-AUC-001-EXEC-2026-06 |
| Evidence Contract ID | VCA-AUC-001-EVD-001 |
| Status | Stabilized |
| Period | 2026-06-01 to 2026-06-30 |
| Source Model | `ad_quality_spend_model` |

## Purpose

Consolidar conocimiento trazable sobre la calidad de leads de Meta Ads para junio de 2026, derivado exclusivamente del Evidence Set y del Evidence Contract autorizados.

Este artefacto no crea evidencia nueva, no formula recomendaciones y no modifica coverage states, limitaciones ni UNKNOWNs.

## Scope

| Field | Value |
|---|---|
| Channel | Meta Ads / Meta Lead Ads |
| Model Grain | normalized `ad_id` (`ad_id_norm`) |
| Quality Rule | Qualified Lead = `lead_tier IN ('A', 'B')` |
| Spend Filter | `campaign_signal = 'COMMERCIAL'` |
| Coverage States | `matched`; `lead_only`; `spend_only` |

## Evidence Basis

| Evidence ID | Use In Knowledge Set |
|---|---|
| EVD-001 | Coverage by status: `matched`, `lead_only`, `spend_only` |
| EVD-002 | Prepared model totals |
| EVD-003 | Ad reference evidence by `ad_id_norm` and `ad_name` |
| EVD-004 | Campaign/adset evidence where lead-side metadata exists |

## Consolidated Insights

| Insight ID | Statement | Evidence Links | Limitations |
|---|---|---|---|
| INS-001 | Matched evidence is concentrated in one ad reference: `120245828603090721` / `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`. This ad accounts for 519 lead rows and 152 qualified A/B leads within the matched evidence. | EVD-001, EVD-002, EVD-003 | This is concentration evidence only. It does not prove causal superiority or creative effectiveness. |
| INS-002 | The evidence separates a matched CAPTACION/ABO campaign/adset row from a lead-only RTG/CBO campaign/adset row. The matched row contains 680 leads, 191 qualified A/B leads and 494.36 spend. The lead-only row contains 92 leads and 35 qualified A/B leads with no matched commercial spend in the approved model. | EVD-001, EVD-004 | Lead-only spend must remain a coverage state, not an inference that no spend existed outside the model. |
| INS-003 | Spend-only evidence is small in amount, 2 ads and 2.20 spend, but structurally important because it cannot support cost-per-lead or quality-rate statements. | EVD-001, EVD-003 | Spend-only cost-per-lead, spend-per-qualified and quality-rate values remain UNKNOWN. |

## Hypotheses

| Hypothesis ID | Hypothesis | Evidence Links | Validation Condition |
|---|---|---|---|
| HYP-001 | The June 2026 observed lead-quality and commercial-spend signal may be concentrated around a limited subset of matched ad references. | EVD-001, EVD-003 | Preserve as model-based concentration hypothesis, not causal explanation. |
| HYP-002 | RTG lead-quality evidence should be interpreted as a distinct coverage case from matched commercial-spend efficiency evidence. | EVD-001, EVD-004 | Do not convert into campaign-level spend interpretation without source expansion or approved mapping. |

## Conclusions

| Conclusion ID | Conclusion | Evidence Links | Scope Limit |
|---|---|---|---|
| CON-001 | AUC-001 has sufficient evidence to reason about ad-level lead quality and commercial spend within the corrected model. The prepared model covers 15 ads, 772 distinct leads, 226 qualified A/B leads and 496.56 spend. | EVD-001, EVD-002, Evidence Contract source metric links | Excludes impressions, clicks, CTR, creative asset metadata and direct campaign/adset spend attribution. |
| CON-002 | Campaign/adset-level reasoning is partially supported and must remain coverage-qualified. | EVD-004, Evidence Contract limitations | Campaign/adset values are lead-side metadata; direct campaign/adset spend mapping is unavailable in the approved model. |

## Reasoning Priorities

| Priority ID | Priority | Evidence Basis | Boundary |
|---|---|---|---|
| PRI-001 | Preserve ad-level matched evidence as the strongest reasoning base for efficiency-oriented reading. | EVD-001, EVD-003 | This is a reasoning priority, not an execution action. |
| PRI-002 | Treat lead-only evidence as quality evidence without matched commercial spend. | EVD-001, EVD-004 | Do not infer absent spend behavior. |
| PRI-003 | Keep campaign/adset reasoning coverage-qualified. | EVD-004, limitations | Do not infer campaign/adset spend attribution. |
| PRI-004 | Propagate missing impressions, clicks, CTR and creative asset metadata. | Evidence Contract limitations | Do not fill evidence gaps by assumption. |

## Risks

| Risk ID | Risk | Evidence Basis | Required Handling |
|---|---|---|---|
| RSK-001 | Treating matched spend as direct lead-level commercial classification. | Evidence Contract limitations | Preserve spend-side-only `campaign_signal` boundary. |
| RSK-002 | Interpreting campaign/adset spend where metadata is absent. | EVD-004; limitations | Avoid unsupported campaign/adset spend conclusions. |
| RSK-003 | Turning ad-reference concentration into creative causality. | EVD-003; creative metadata limitation | Keep reasoning at ad-reference level. |
| RSK-004 | Using lead-only rows for cost-efficiency conclusions. | EVD-001; Evidence Contract limitations | Preserve `lead_only` coverage status. |
| RSK-005 | Ignoring duplicate/test-record uncertainty. | Evidence Contract uncertainty notes | Keep uncertainty visible downstream. |

## Uncertainties

| Uncertainty ID | Uncertainty | Required Handling |
|---|---|---|
| UNC-001 | Duplicate/test-record flags are not explicitly mapped. | Keep visible in downstream contracts and final output. |
| UNC-002 | Spend-only campaign/adset metadata is UNKNOWN. | Do not reason about campaign/adset identity for spend-only rows. |
| UNC-003 | Impressions, clicks and CTR are unavailable. | Do not create funnel-entry interpretations beyond leads and spend. |
| UNC-004 | Creative asset metadata is unavailable. | Keep creative reasoning at ad reference/name level only. |
| UNC-005 | `campaign_signal` is spend-side only. | Do not state that lead rows directly carry commercial signal. |

## Stabilization Statement

The Knowledge Set is stabilized for downstream recommendation work. It derives exclusively from EVD-001 through EVD-004 and preserves all material limitations, UNKNOWNs and coverage states.
