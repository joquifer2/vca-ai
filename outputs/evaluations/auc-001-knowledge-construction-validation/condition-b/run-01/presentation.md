# AUC-001 Executive Decision Support

## 1. Executive Summary

The June 2026 Meta Lead Ads evidence supports guarded decision-making at ad-reference level. The strongest efficiency-oriented reading comes from the `matched` evidence, where both lead quality and commercial spend are present for 8 ad references.

The main decision point is not simply which row has the best metric. The evidence is concentrated: one matched ad reference, `120245828603090721` / `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`, carries most matched lead volume, qualified leads, and spend. That makes it central to the current reading, but not proof of causal superiority.

RTG/CBO lead-only evidence should remain visible as quality evidence, but it should not be treated as matched spend-efficiency evidence. Campaign/adset and creative-level claims require caution because the approved model does not provide direct campaign/adset spend attribution or creative asset metadata.

## 2. Key Messages

### What Is Happening

- The prepared model contains 15 ad references, 772 distinct leads, 226 qualified leads, and 496.56 spend for June 2026.
- Coverage is split into 8 matched ad references, 5 lead-only ad references, and 2 spend-only ad references.
- The matched coverage state contains 680 leads, 191 qualified leads, and 494.36 spend.
- The lead-only coverage state contains 92 leads and 35 qualified leads, but no matched commercial spend in the approved model.
- Spend-only evidence totals 2.20 spend and cannot support quality rate, cost per lead, or campaign/adset interpretation.

### Why It Matters

Prepared totals are useful for orientation, but they combine coverage states that answer different questions. Decisions should preserve the distinction:

- `matched`: quality plus commercial spend can be read together.
- `lead_only`: quality can be read without matched spend efficiency.
- `spend_only`: spend is visible, but lead quality and ratios are UNKNOWN.

### The Main Analytical Reading

The dominant matched ad reference explains most of the matched signal by volume and spend. Its qualified rate is close to the matched aggregate, so the evidence supports a concentration reading more than a claim of exceptional quality.

Smaller matched references show some stronger ratios, but their volumes are narrow. They are useful candidate signals, not stable performance conclusions.

## 3. Recommended Decisions

| Priority | Recommendation | Decision Meaning |
|---|---|---|
| P1 | Use matched ad-level evidence as the primary basis for efficiency-oriented decisions. | Start efficiency discussion where lead quality and commercial spend are both present. |
| P1 | Treat RTG lead-only evidence as a separate quality reading, not matched spend efficiency. | Keep RTG quality visible without inventing spend comparisons. |
| P2 | Validate or document campaign/adset spend mapping before campaign-level spend recommendations. | Avoid unsupported campaign/adset budget conclusions. |
| P2 | Keep creative recommendations at ad-reference level unless creative asset metadata is added. | Do not convert ad-name concentration into creative asset causality. |
| P2 | Preserve duplicate/test-record uncertainty in downstream decisions and final output. | Avoid overstating lead-count certainty. |
| P3 | Exclude impressions, clicks, and CTR from recommendations unless source scope is expanded. | Keep funnel-entry recommendations outside the current evidence scope. |

## 4. Risks And Decision Constraints

| Risk | Decision Impact | Required Handling |
|---|---|---|
| Matched spend may be mistaken for direct lead-level commercial classification. | Could overstate what the lead rows prove. | Preserve that `campaign_signal` is spend-side only. |
| Campaign/adset spend may be inferred where metadata is absent. | Could lead to unsupported campaign-level spend decisions. | Require approved mapping before campaign/adset spend recommendations. |
| Ad-reference concentration may be treated as creative causality. | Could drive unsupported creative production decisions. | Keep creative statements at ad-reference/name level. |
| Lead-only evidence may be used for cost-efficiency conclusions. | Could create false RTG efficiency comparisons. | Keep lead-only quality separate from matched spend efficiency. |
| Duplicate/test-record uncertainty may be hidden. | Could make lead counts appear more certain than evidenced. | Keep the limitation visible. |
| Prepared totals may hide coverage-state differences. | Could make the evidence look more uniform than it is. | Present totals with coverage-state distinctions. |

## 5. Main Indicators

| Coverage State | Ad Count | Leads | Qualified Leads | Spend | Qualified Rate | Decision Reading |
|---|---:|---:|---:|---:|---:|---|
| matched | 8 | 680 | 191 | 494.36 | 28.09% | Strongest base for combined quality and spend reading. |
| lead_only | 5 | 92 | 35 | 0.00 | 38.04% | Quality evidence only; not spend-efficiency evidence. |
| spend_only | 2 | 0 | 0 | 2.20 | UNKNOWN | Spend visibility only; quality and ratios UNKNOWN. |
| prepared total | 15 | 772 | 226 | 496.56 | 29.27% | Orientation total; not a single uniform evidence class. |

## 6. Evidence Summary

### Matched Evidence

Matched evidence supports the current efficiency-oriented discussion because both lead quality and commercial spend are present. The most material matched reference is:

| Ad Reference | Leads | Qualified Leads | Spend | Qualified Rate | Spend / Qualified |
|---|---:|---:|---:|---:|---:|
| `120245828603090721` / `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1` | 519 | 152 | 374.79 | 29.29% | 2.47 |

This reference dominates matched volume and spend, but its qualified rate is close to the matched aggregate. The executive reading is concentration with usable efficiency evidence, not causal superiority.

### Lead-Only Evidence

Lead-only RTG/CBO evidence contains 92 leads and 35 qualified leads. Its qualified rate is higher than the matched aggregate, but there is no matched commercial spend in the approved model. It should inform quality discussion only.

### Spend-Only Evidence

Spend-only evidence is small at 2.20 spend, but it matters because its quality and ratio fields are UNKNOWN. It should not be used for lead-quality, CPL, cost-per-qualified, or campaign/adset conclusions.

## 7. Limitations And UNKNOWNs

- Duplicate/test-record flags are not explicitly mapped; lead counts should remain qualified.
- Spend-only campaign/adset metadata is UNKNOWN.
- Impressions, clicks, and CTR are unavailable.
- Creative asset metadata is unavailable.
- `campaign_signal` is spend-side only; lead rows should not be described as directly commercial.
- Lead-only spend is zero by model alignment, not proof of absent real-world spend.
- Spend-only ratios are UNKNOWN.
- Campaign/adset values are lead-side metadata and must remain coverage-qualified.

## 8. Traceability

| Content Area | Source |
|---|---|
| Execution scope | VCA-AUC-001-EXEC-2026-06 |
| Evidence | EVD-001, EVD-002, EVD-003, EVD-004 |
| Knowledge | FND-001 through FND-007; INS-001 through INS-004; HYP-001 through HYP-003; CON-001 through CON-004 |
| Recommendations | REC-001 through REC-006 |
| Presentation policy | Executive decision support |

## 9. Final Statement

The current output supports executive review of June 2026 Meta Lead Ads lead quality and spend efficiency within the corrected model. The recommended decision posture is to act from matched ad-level evidence for efficiency discussions, keep lead-only quality evidence separate, and preserve the documented limitations before moving into campaign/adset or creative-level decisions.