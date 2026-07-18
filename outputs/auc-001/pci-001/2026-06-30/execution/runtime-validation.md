# Runtime Validation Record

## Decision

PASS

## Runtime

| Field | Value |
|---|---|
| execution_id | AUC-001-PCI-001-2026-06-30 |
| runtime | tools/auc_001_canonical_cost_quality_model.py |
| period | 2026-04-18 to 2026-06-30 |
| input_source | BigQuery MCP query_read_only aggregates |
| adapter_policy | Tier-preserving expansion for lead aggregates; COMMERCIAL spend filter before runtime |
| blockers | False |

## Input Hashes

| Input | SHA-256 |
|---|---|
| lead_tier_aggregate | 6d5bed44fb19c174149ad6316c3c27f709a3c46d88ee1ed525d1142ee43c90da |
| spend_signal_aggregate | b29586b537567450f9151f6fa59772d79d6a65bf47fc76555c1729f0f865e5fc |
| lead_runtime_records | eebca122da4b58c99407b0cb2f068bf6d6d510ef3164fa04370efef975f14eb4 |
| spend_runtime_records | 48d832f2dbeecdb067dab4f0e2c66348b5f1cd297d4ca583b8a747ebec1c4641 |

## Runtime Input Counts

| Input | Count |
|---|---:|
| MCP lead tier aggregate rows | 42 |
| MCP spend signal aggregate rows | 23 |
| expanded lead runtime records | 1329 |
| commercial spend runtime records | 10 |

## Coverage Summary

| coverage_status | ad_count | leads | ab_leads | tier_a | tier_b | commercial_spend |
|---|---:|---:|---:|---:|---:|---:|
| lead_only | 5 | 142 | 53 | 10 | 43 | 0.00 EUR |
| matched | 8 | 1187 | 346 | 49 | 297 | 873.65 EUR |
| spend_only | 2 | 0 | 0 | 0 | 0 | 2.20 EUR |

## Runtime Rows

| ad_id_norm | coverage_status | leads | ab_leads | tier_a | tier_b | commercial_spend | sample_status |
|---|---|---:|---:|---:|---:|---:|---|
| 120245407987440721 | matched | 19 | 10 | 2 | 8 | 25.16 | ranking_eligible |
| 120245407987450721 | matched | 57 | 22 | 3 | 19 | 48.96 | recommendation_eligible |
| 120245823087500721 | lead_only | 18 | 9 | 1 | 8 | 0.00 | not_applicable |
| 120245823087510721 | lead_only | 3 | 0 | 0 | 0 | 0.00 | not_applicable |
| 120245828603090721 | matched | 643 | 187 | 23 | 164 | 468.06 | recommendation_eligible |
| 120245829115590721 | matched | 16 | 6 | 2 | 4 | 12.52 | ranking_eligible |
| 120245829545180721 | matched | 360 | 103 | 18 | 85 | 245.84 | recommendation_eligible |
| 120245829746630721 | matched | 20 | 8 | 1 | 7 | 18.22 | recommendation_eligible |
| 120247352473020721 | lead_only | 118 | 42 | 9 | 33 | 0.00 | not_applicable |
| 120251249759480721 | spend_only | 0 | 0 | 0 | 0 | 1.20 | not_applicable |
| 120251252180570721 | spend_only | 0 | 0 | 0 | 0 | 1.00 | not_applicable |
| 120251254823190721 | matched | 5 | 2 | 0 | 2 | 4.86 | descriptive_only |
| 120251255543160721 | lead_only | 1 | 0 | 0 | 0 | 0.00 | not_applicable |
| 120251255543170721 | lead_only | 2 | 2 | 0 | 2 | 0.00 | not_applicable |
| 120251257513780721 | matched | 67 | 8 | 0 | 8 | 50.03 | recommendation_eligible |

## Invariants

| Invariant | Result |
|---|---|
| commercial_spend = matched_spend + spend_only_spend | PASS: 875.85 = 873.65 + 2.2 |
| lead_total = matched_leads + lead_only_leads | PASS: 1329 = 1187 + 142 |
| ab_total = matched_ab_leads + lead_only_ab_leads | PASS: 399 = 346 + 53 |
| tier_a_total = matched_tier_a + lead_only_tier_a | PASS: 59 = 49 + 10 |
| tier_b_total = matched_tier_b + lead_only_tier_b | PASS: 340 = 297 + 43 |
| prepared_ad_count = matched_ad_count + lead_only_ad_count + spend_only_ad_count | PASS: 15 = 8 + 5 + 2 |

## Issues

Runtime blockers: none.

Runtime warnings: none.

## Reproduction

Run the local runtime tests:

```powershell
powershell -ExecutionPolicy Bypass -File tests\evals\auc_001_canonical_cost_quality_model_tests.ps1
```

Reproduce the runtime validation by acquiring the MCP aggregates and controls listed in `execution/implementation-validation-report.md`, using `execution/evidence-acquisition.md` as supporting acquisition traceability, then applying the adapter policy recorded here and calling `build_cost_quality_model` from `tools/auc_001_canonical_cost_quality_model.py`.
