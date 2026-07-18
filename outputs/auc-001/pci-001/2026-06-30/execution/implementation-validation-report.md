# AUC-001-PCI-001 Implementation Validation Report

## Metadata

| Field | Value |
|---|---|
| execution_id | AUC-001-PCI-001-2026-06-30 |
| role | Implementation Agent |
| status | PASS |
| period_start | 2026-04-18 |
| period_end | 2026-06-30 |
| namespace | outputs/auc-001/pci-001/2026-06-30/ |
| runtime | tools/auc_001_canonical_cost_quality_model.py |
| historical_outputs_used_as_expected_values | No |
| historical_namespace_modified | No |

## Preconditions

| Precondition | Result |
|---|---|
| Entry Gate is PASS | PASS |
| Official namespace is `outputs/auc-001/pci-001/2026-06-30/` | PASS |
| Historical namespace `outputs/auc-001/2026-06-30/` is immutable | PASS |
| BigQuery MCP available | PASS |
| Authorized sources and period fixed | PASS |
| Blocking QA conditions open | None found for execution |

## BigQuery MCP Discovery

| request_id | resource | status | trace_reference |
|---|---|---|---|
| auc-001-pci-001-impl-revalidation-discover-workspace | workspace:vca | success | trc-d8d62bdf1e8a4c5580b0bfb4adbf3535 |
| auc-001-pci-001-impl-revalidation-discover-intermediate | dataset:intermediate | success | trc-87a1efd7bbb74ad3b1e8d10bebd86023 |
| auc-001-pci-001-impl-revalidation-discover-marts | dataset:marts | success | trc-0f31f384b36849ecbc92cee01c6e1b7b |
| auc-001-pci-001-impl-revalidation-discover-leads | table:marts.fct_lead_enriched | success | trc-b25a05d1529b4924a6fa2e0689668cfe |
| auc-001-pci-001-impl-revalidation-discover-spend | table:marts.fct_spend | success | trc-2596612a0b2d467ea71f1261af71e5d8 |
| auc-001-pci-001-impl-revalidation-discover-scoring | table:intermediate.int_faro_lead_scoring | success | trc-e0e66a7c29084c978551450f7c6cdaf4 |

## BigQuery MCP Evidence Queries

| request_id | purpose | status | bytes_processed | trace_reference |
|---|---|---|---:|---|
| auc-001-pci-001-impl-lead-tier-aggregate | Lead-side tier aggregate by raw `ad_id` | success | 52802 | trc-07687b3e835447fcb59d4c42951b5411 |
| auc-001-pci-001-impl-spend-signal-aggregate | Spend-side aggregate by `ad_id` and signal | success | 490475 | trc-52348c6630424e60a9e40f92d22d3755 |
| auc-001-pci-001-impl-scoring-tier-summary | Scoring validation by tier | success | 83660 | trc-8c1100e277364210822cc31f95b25f08 |
| auc-001-pci-001-impl-lead-quality-controls | Lead-side quality controls | success | 79001 | trc-1f7f246792f1448396624239e3915308 |
| auc-001-pci-001-impl-spend-quality-controls | Spend-side quality controls | success | 490475 | trc-148ae5d69b69401ba3879aa11b643414 |
| auc-001-pci-001-impl-spend-signal-summary | Spend by signal | success | 286035 | trc-5524d50ce40d48d7b40541daf7b91555 |
| auc-001-pci-001-impl-signal-domain | Signal domain | success | 92 | trc-76af62ae596b41e8ab3064d6930e8249 |
| auc-001-pci-001-impl-normalization-collision-controls-v2 | Normalization collision controls | success | 131667 | trc-c39ade5894464999a43ebc527b04d3f0 |

Rejected and not used:

| request_id | status | reason |
|---|---|---|
| auc-001-pci-001-impl-normalization-collision-controls | rejected | ERR_SCOPE_DENIED |

## Runtime Execution

The runtime was executed through `build_cost_quality_model` using MCP-acquired aggregates.

Adapter policy:

- Lead-side MCP tier aggregates were expanded into tier-preserving runtime records.
- Spend-side MCP signal aggregates were acquired for all signals.
- Only `COMMERCIAL` spend rows were passed into the canonical runtime model.
- No source join was performed before the runtime call.
- `ad_name` was not used as key, fallback or reconciliation mechanism.

Runtime artifacts:

- `execution/runtime-inputs.json`
- `execution/runtime-output.json`
- `execution/runtime-validation.md`

Input hashes:

| Input | SHA-256 |
|---|---|
| lead_tier_aggregate | 6d5bed44fb19c174149ad6316c3c27f709a3c46d88ee1ed525d1142ee43c90da |
| spend_signal_aggregate | b29586b537567450f9151f6fa59772d79d6a65bf47fc76555c1729f0f865e5fc |
| lead_runtime_records | eebca122da4b58c99407b0cb2f068bf6d6d510ef3164fa04370efef975f14eb4 |
| spend_runtime_records | 48d832f2dbeecdb067dab4f0e2c66348b5f1cd297d4ca583b8a747ebec1c4641 |

## Metrics And Invariants

| Metric | Value |
|---|---:|
| commercial_spend | 875.85 EUR |
| matched_spend | 873.65 EUR |
| spend_only_spend | 2.20 EUR |
| lead_total | 1329 |
| matched_leads | 1187 |
| lead_only_leads | 142 |
| ab_total | 399 |
| matched_ab_leads | 346 |
| lead_only_ab_leads | 53 |
| tier_a_total | 59 |
| matched_tier_a | 49 |
| lead_only_tier_a | 10 |
| tier_b_total | 340 |
| matched_tier_b | 297 |
| lead_only_tier_b | 43 |
| prepared_ad_count | 15 |
| matched_ad_count | 8 |
| lead_only_ad_count | 5 |
| spend_only_ad_count | 2 |

| Invariant | Result |
|---|---|
| commercial_spend = matched_spend + spend_only_spend | PASS |
| lead_total = matched_leads + lead_only_leads | PASS |
| ab_total = matched_ab_leads + lead_only_ab_leads | PASS |
| tier_a_total = matched_tier_a + lead_only_tier_a | PASS |
| tier_b_total = matched_tier_b + lead_only_tier_b | PASS |
| prepared_ad_count = matched_ad_count + lead_only_ad_count + spend_only_ad_count | PASS |

## Technical Validations

| Validation | Command / Evidence | Result |
|---|---|---|
| Runtime compilation | `python -m py_compile tools\auc_001_canonical_cost_quality_model.py` | PASS |
| Unit/local tests | `powershell -ExecutionPolicy Bypass -File tests\evals\auc_001_canonical_cost_quality_model_tests.ps1` | PASS, 4/4 |
| Namespace validation | File inventory under `outputs/auc-001/pci-001/2026-06-30/` | PASS |
| Historical output immutability | `git status --short outputs\auc-001\2026-06-30` | PASS, no changes reported |
| Runtime invariants with real MCP aggregates | `execution/runtime-validation.md` | PASS |

## Blockers And Observations

Blockers: none.

Observations:

- One MCP collision-control query was rejected by policy and excluded. A simpler allowlisted query provided the collision controls.
- Comparison with the historical execution was documentary only: this package uses a separated post-closure namespace and does not use historical outputs as expected values.
- This Implementation Agent report does not declare the Exit Gate as PASS and does not close the iteration.

## QA Readiness

The package is ready for QA Gate Agent review of the experimental validation evidence.

Recommended next step:

```text
Usa el QA Gate Agent para revisar la validacion experimental de AUC-001-PCI-001 contenida en outputs/auc-001/pci-001/2026-06-30/, verificando runtime-validation.md, implementation-validation-report.md, evidence-set.md, invariantes, trazabilidad MCP, namespace y no modificacion de outputs historicos. No ejecutar BigQuery salvo que QA lo requiera expresamente.
```
