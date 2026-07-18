# Evidence Set

## Metadata

| Field | Value |
|---|---|
| evidence_set_id | AUC-001-PCI-001-EVD-2026-06-30 |
| execution_id | AUC-001-PCI-001-2026-06-30 |
| contract_id | VCA-EVD-001 |
| specification | SPEC-012 |
| provider | BigQuery MCP Server |
| output_namespace | outputs/auc-001/pci-001/2026-06-30/ |
| transition_status | Ready for Knowledge generation |

## Source Validation

| Check | Canonical lead source | Scoring validation source | Result |
|---|---:|---:|---|
| row_count | 1329 | 1329 | PASS |
| distinct_lead_count | 1329 | 1329 | PASS |
| Tier A | 59 | 59 | PASS |
| Tier B | 340 | 340 | PASS |
| Tier A/B | 399 | 399 | PASS |
| Tier C | 554 | 554 | PASS |
| Tier D | 376 | 376 | PASS |
| distinct_ad_id_norm_count | 13 | 13 | PASS |
| period | 2026-04-18 to 2026-06-30 | 2026-04-18 to 2026-06-30 | PASS |

## Lead Quality Totals

| Metric | Value |
|---|---:|
| total_leads | 1329 |
| total_ab_leads | 399 |
| tier_a_total | 59 |
| tier_b_total | 340 |
| tier_c_total | 554 |
| tier_d_total | 376 |
| qualified_rate_ab_global | 30.02% |

## Spend Totals

| Metric | Value |
|---|---:|
| total_spend_all_signals | 1406.25 EUR |
| commercial_spend | 875.85 EUR |
| activation_spend | 221.86 EUR |
| attention_spend | 308.54 EUR |
| commercial_spend_share | 62.28% |
| activation_spend_share | 15.78% |
| attention_spend_share | 21.94% |

## Coverage Aggregates

| coverage_status | ad_count | leads | ab_leads | tier_a | tier_b | commercial_spend |
|---|---:|---:|---:|---:|---:|---:|
| matched | 8 | 1187 | 346 | 49 | 297 | 873.65 EUR |
| lead_only | 5 | 142 | 53 | 10 | 43 | 0.00 EUR |
| spend_only | 2 | 0 | 0 | 0 | 0 | 2.20 EUR |

## Canonical Metrics

| Metric | Value | Universe |
|---|---:|---|
| cpl_commercial_matched | 0.74 EUR | matched commercial spend / matched leads |
| qualified_rate_ab_matched | 29.15% | matched A/B leads / matched leads |
| cost_per_ab_commercial_matched | 2.53 EUR | matched commercial spend / matched A/B leads |
| cost_per_tier_a_commercial_matched | 17.83 EUR | matched commercial spend / matched Tier A leads |
| spend_share_matched | 99.75% | matched commercial spend / commercial spend |
| lead_share_matched | 89.31% | matched leads / total leads |
| ab_share_matched | 86.72% | matched A/B leads / total A/B leads |
| commercial_spend_per_matched_lead_observed | 0.74 EUR | diagnostic only |

## Reconciled Rows

| ad_id_norm | coverage_status | leads | ab_leads | tier_a | tier_b | commercial_spend | cpl_matched | cost_per_ab | sample_status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 120245828603090721 | matched | 643 | 187 | 23 | 164 | 468.06 EUR | 0.73 EUR | 2.50 EUR | recommendation_eligible |
| 120245829545180721 | matched | 360 | 103 | 18 | 85 | 245.84 EUR | 0.68 EUR | 2.39 EUR | recommendation_eligible |
| 120245407987450721 | matched | 57 | 22 | 3 | 19 | 48.96 EUR | 0.86 EUR | 2.23 EUR | recommendation_eligible |
| 120245407987440721 | matched | 19 | 10 | 2 | 8 | 25.16 EUR | 1.32 EUR | 2.52 EUR | ranking_eligible |
| 120251257513780721 | matched | 67 | 8 | 0 | 8 | 50.03 EUR | 0.75 EUR | 6.25 EUR | recommendation_eligible |
| 120245829746630721 | matched | 20 | 8 | 1 | 7 | 18.22 EUR | 0.91 EUR | 2.28 EUR | recommendation_eligible |
| 120245829115590721 | matched | 16 | 6 | 2 | 4 | 12.52 EUR | 0.78 EUR | 2.09 EUR | ranking_eligible |
| 120251254823190721 | matched | 5 | 2 | 0 | 2 | 4.86 EUR | 0.97 EUR | 2.43 EUR | descriptive_only |
| 120247352473020721 | lead_only | 118 | 42 | 9 | 33 | 0.00 EUR | NULL | NULL | not_applicable |
| 120245823087500721 | lead_only | 18 | 9 | 1 | 8 | 0.00 EUR | NULL | NULL | not_applicable |
| 120251255543170721 | lead_only | 2 | 2 | 0 | 2 | 0.00 EUR | NULL | NULL | not_applicable |
| 120245823087510721 | lead_only | 3 | 0 | 0 | 0 | 0.00 EUR | NULL | NULL | not_applicable |
| 120251255543160721 | lead_only | 1 | 0 | 0 | 0 | 0.00 EUR | NULL | NULL | not_applicable |
| 120251249759480721 | spend_only | 0 | 0 | 0 | 0 | 1.20 EUR | NULL | NULL | not_applicable |
| 120251252180570721 | spend_only | 0 | 0 | 0 | 0 | 1.00 EUR | NULL | NULL | not_applicable |

## Weekly Quality Summary

| week_start | leads | ab_leads | tier_a | tier_b |
|---|---:|---:|---:|---:|
| 2026-04-13 | 36 | 10 | 2 | 8 |
| 2026-04-20 | 140 | 43 | 6 | 37 |
| 2026-04-27 | 7 | 4 | 0 | 4 |
| 2026-05-04 | 181 | 58 | 12 | 46 |
| 2026-05-11 | 182 | 55 | 8 | 47 |
| 2026-05-18 | 7 | 0 | 0 | 0 |
| 2026-06-01 | 213 | 53 | 7 | 46 |
| 2026-06-08 | 182 | 57 | 9 | 48 |
| 2026-06-15 | 194 | 75 | 8 | 67 |
| 2026-06-22 | 155 | 41 | 7 | 34 |
| 2026-06-29 | 32 | 3 | 0 | 3 |

## Invariants

| Invariant | Result |
|---|---|
| commercial_spend = matched_spend + spend_only_spend | PASS: 875.85 = 873.65 + 2.20 |
| lead_total = matched_leads + lead_only_leads | PASS: 1329 = 1187 + 142 |
| ab_total = matched_ab_leads + lead_only_ab_leads | PASS: 399 = 346 + 53 |
| tier_a_total = matched_tier_a + lead_only_tier_a | PASS: 59 = 49 + 10 |
| tier_b_total = matched_tier_b + lead_only_tier_b | PASS: 340 = 297 + 43 |
| prepared_ad_count = matched_ad_count + lead_only_ad_count + spend_only_ad_count | PASS: 15 = 8 + 5 + 2 |

## Limitations And Unknowns

- `lead_only` rows do not support CPL or cost-per-A/B metrics.
- `spend_only` rows do not imply zero real leads; they only indicate no matched canonical lead-side aggregate in this model execution.
- Activation and Attention spend are excluded from commercial efficiency metrics.
- Rankings are descriptive and threshold-bound; no creative causality is inferred from `ad_name`.
- Historical outputs were not used as expected values.

## Blockers

None detected for the canonical Evidence Set.
