# Recommendation Set

## Metadata

| Field | Value |
|---|---|
| recommendation_set_id | AUC-001-PCI-001-REC-2026-06-30 |
| source_knowledge_set | AUC-001-PCI-001-KNW-2026-06-30 |
| output_namespace | outputs/auc-001/pci-001/2026-06-30/ |
| status | Stabilized |

## Recommendations

| ID | Priority | Action | Support | Risk | Validation |
|---|---|---|---|---|---|
| R-001 | High | Use the matched commercial universe as the official cost-quality baseline for this iteration. | K-001 | Misreading non-commercial or lead-only activity as part of commercial efficiency. | Re-run AUC-001-PCI-001 with the same namespace pattern and compare only against same-method future executions. |
| R-002 | High | Preserve visibility of `lead_only` rows and do not assign zero cost to them. | K-002 | Understating cost or overstating efficiency for non-commercial/coverage-excluded activity. | Track whether future iterations reduce lead-only volume or explain its source. |
| R-003 | Medium | Review ad `120251257513780721` before scaling, because it is recommendation-eligible by volume but weak on A/B efficiency. | K-004 | Acting on low-quality volume as if it matched the baseline. | Monitor matched A/B rate and cost per A/B in the next post-closure execution. |
| R-004 | Medium | Treat the two largest matched ads as concentration drivers rather than isolated creative proof. | K-003 | Over-attributing performance to labels without creative metadata. | Require additional creative/asset metadata before causal creative conclusions. |
| R-005 | Medium | Keep Activation and Attention spend out of commercial efficiency metrics. | K-005 | Distorted CPL/CPQL through signal mixing. | Validate signal separation in the Exit Gate for every future PCI execution. |

## Explicit Non-Recommendations

- Do not reallocate budget based on `lead_only` rows alone.
- Do not treat `spend_only` rows as zero-lead ads.
- Do not infer creative causality from `ad_name`.
- Do not compare against historical outputs as expected values.
