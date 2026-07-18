# Knowledge Set

## Metadata

| Field | Value |
|---|---|
| knowledge_set_id | AUC-001-PCI-001-KNW-2026-06-30 |
| source_evidence_set | AUC-001-PCI-001-EVD-2026-06-30 |
| output_namespace | outputs/auc-001/pci-001/2026-06-30/ |
| status | Stabilized |
| analytical_profile | .github/skills/meta-lead-quality-analysis/ANALYTICAL_PROFILE.md |
| knowledge_construction_profile | .github/skills/meta-lead-quality-analysis/knowledge-construction-profile.md |

## Analytical Investigation Record

| Question | Evidence Used | Finding |
|---|---|---|
| What is the global quality level? | total_leads=1329, total_ab_leads=399 | A/B quality is 30.02% globally. |
| Does the matched commercial universe cover most relevant activity? | matched leads=1187, matched spend=873.65 EUR | Matched coverage captures 89.31% of leads, 86.72% of A/B leads and 99.75% of commercial spend. |
| What is the main cost-quality baseline? | matched commercial spend=873.65 EUR, matched A/B leads=346 | Cost per matched A/B lead is 2.53 EUR. |
| Is quality evenly distributed? | reconciled rows | Two matched ads concentrate 547 of 1187 matched leads and 290 of 346 matched A/B leads. |
| Are there material coverage exclusions? | lead_only=142 leads, spend_only=2.20 EUR | Lead-side exclusions are material for quality share; spend-only commercial exclusion is economically immaterial. |
| Are there signals outside commercial efficiency? | Activation=221.86 EUR, Attention=308.54 EUR | 37.72% of spend belongs to non-commercial signals and must not be mixed into commercial CPL/CPQL. |
| Is quality stable through time? | weekly quality summary | Weekly A/B volume fluctuates; the strongest complete week is 2026-06-15 with 75 A/B leads, while the final 2026-06-29 week is partial and not comparable as a full week. |

## Stabilized Knowledge

### K-001 Commercial matched universe is strong enough for cost-quality interpretation

The matched universe contains nearly all commercial spend and most lead-side volume. This supports the canonical matched metrics as the primary cost-quality view for AUC-001-PCI-001.

Confidence: High.

### K-002 Global and matched A/B rates are close, but lead-only quality is material

Global A/B rate is 30.02%; matched A/B rate is 29.15%. The gap is driven by 53 A/B leads in `lead_only`, especially one non-commercial/activation-scoped ad with 42 A/B leads.

Confidence: Medium-high.

### K-003 Cost-quality is concentrated in a small number of matched ads

The two largest matched ads represent most matched leads and A/B leads. This creates a concentration pattern: stable headline economics, but exposure to performance shifts in a small set of ads.

Confidence: High.

### K-004 One matched ad has weak A/B efficiency despite recommendation-eligible volume

Ad `120251257513780721` has 67 matched leads and 8 A/B leads, with cost per A/B of 6.25 EUR and matched A/B rate of 11.94%. It is materially weaker than the main matched baseline.

Confidence: High.

### K-005 Non-commercial signals must remain outside commercial efficiency

Activation and Attention spend sum to 530.40 EUR. Mixing those signals into commercial CPL or cost-per-A/B would materially distort the model.

Confidence: High.

### K-006 Temporal evidence supports monitoring, not a trend claim

Weekly A/B lead volume varies materially across the observed period. The evidence supports monitoring weekly quality as an operational slice, but it does not support a stable trend conclusion because the period includes partial weeks and uneven weekly volume.

Confidence: Medium.

## Analytical Narrative

AUC-001-PCI-001 shows a commercially usable matched cost-quality baseline, but that baseline is concentrated, coverage-dependent and not yet a temporal trend. The main commercial universe produces low observed cost per matched lead and 2.53 EUR per matched A/B lead, while a meaningful block of quality leads sits outside commercial matched coverage and non-commercial spend remains structurally separate. The strategic reading is not that the model found a universal winner, but that it established a governed commercial baseline and exposed where coverage, concentration and temporal monitoring must be managed before scaling decisions.

## Unknowns

- The model does not explain why `lead_only` rows lack matched commercial spend.
- The model does not infer creative, format or asset causality from ad labels.
- The model does not validate downstream sales quality beyond FARO tiers.
