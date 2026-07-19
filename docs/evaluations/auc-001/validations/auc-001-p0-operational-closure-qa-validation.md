# AUC-001 P0 Operational Closure QA Validation

## Metadata

| Field | Value |
|---|---|
| Validation ID | AUC-001-P0-OPERATIONAL-CLOSURE-QA-20260719 |
| Validation Agent | QA Gate Agent |
| Validation Date | 2026-07-19 |
| Scope | P0 operational closure using the latest real AUC-001 analytical execution evidence to 2026-06-30 |
| Decision | P0 BLOCKED |
| Runtime output inspected | `outputs/auc-001/pci-001/2026-06-30/execution/runtime-output.json` |
| BigQuery queried | No |
| Report regenerated | No |
| Historical output modified | No |

---

## 1. Gate Evaluated

This validation evaluates whether P0 can close operationally and advance to P01 after the latest real AUC-001 analytical execution produced MCP-acquired evidence and an analytical report to 2026-06-30.

The user-provided execution evidence reports:

- period resolved as 2026-04-18 to 2026-06-30;
- 1,329 leads;
- 399 A/B leads;
- 59 Tier A leads;
- 1,406.25 EUR total spend;
- 873.65 EUR matched commercial spend;
- 1,187 matched leads;
- 346 matched A/B leads;
- 49 matched Tier A leads;
- `cpl_commercial_matched = 0.74 EUR`;
- `cost_per_ab_commercial_matched = 2.53 EUR`;
- `cost_per_tier_a_commercial_matched = 17.83 EUR`;
- `qualified_rate_ab_matched = 29.15%`;
- explicit `matched / lead_only / spend_only` reconciliation;
- concentration, temporal and platform/product analysis;
- explicit causality and coverage limitations.

---

## 2. Phase Current And Phase Target

| Field | Value |
|---|---|
| Current phase | P0 operational validation / closure |
| Target phase | P01 |
| Required decision | `P0 PASS`, `P0 PASS WITH RESIDUAL OBSERVATIONS`, or `P0 BLOCKED` |

---

## 3. Namespace And Runtime Location

Physical runtime-output files found under `outputs/auc-001`:

```text
outputs/auc-001/pci-001/2026-06-30/execution/runtime-output.json
```

No separate new namespace for the latest conversational AUC-001 rerun was found. Therefore QA can only validate the existing physical `runtime-output.json` for the 2026-06-30 execution namespace.

This is a critical distinction:

- the latest analytical execution evidence is usable as additional QA context;
- the physical SPEC-013 persistence claim must be validated against an actual `runtime-output.json` file;
- the only located physical runtime output is the protected `AUC-001-PCI-001-2026-06-30` runtime output.

---

## 4. Physical SPEC-013 Conformance

QA inspected:

```text
outputs/auc-001/pci-001/2026-06-30/execution/runtime-output.json
```

Physical schema check:

| SPEC-013 requirement | Physical result | Status |
|---|---|---|
| `schema_family` present | Missing | FAIL |
| `output_schema_version` present | Missing | FAIL |
| `model_name` present | Missing | FAIL |
| `specification_versions` present | Missing | FAIL |
| `deprecated_aliases` present when aliases exist | Missing | FAIL |
| `spend_reconciliation` block present | Missing | FAIL |
| `coverage_reconciliation` block present | Missing | FAIL |
| `coverage_reconciliation.unknown` explicit | Missing | FAIL |
| `is_consumable` present | Missing | FAIL |
| Required invariant records with `PASS/FAIL` | Missing as structured SPEC-013 records | FAIL |

The runtime implementation and automated tests currently pass, but the physical `runtime-output.json` located in the execution namespace does not conform to SPEC-013. This fails the P0 closure condition requested by the user:

```text
if the runtime fisico cumple SPEC-013
```

---

## 5. Figure Traceability Against Physical Runtime

The physical runtime output supports these figures:

| Requested figure | Physical runtime value | Status |
|---|---:|---|
| period start | 2026-04-18 | PASS |
| period end | 2026-06-30 | PASS |
| leads | 1,329 | PASS |
| A/B leads | 399 | PASS |
| Tier A | 59 | PASS |
| matched commercial spend | 873.65 EUR | PASS |
| matched leads | 1,187 | PASS |
| matched A/B | 346 | PASS |
| matched Tier A | 49 | PASS |
| `cpl_commercial_matched` | 873.65 / 1,187 = 0.735... -> 0.74 EUR | PASS |
| `cost_per_ab_commercial_matched` | 873.65 / 346 = 2.525... -> 2.53 EUR | PASS |
| `cost_per_tier_a_commercial_matched` | 873.65 / 49 = 17.829... -> 17.83 EUR | PASS |
| `qualified_rate_ab_matched` | 346 / 1,187 = 29.15% | PASS |
| total spend all signals | Not exposed in physical runtime output | FAIL for SPEC-013 physical reconciliation |
| `matched / lead_only / spend_only` | Present in legacy `coverage_summary` | PARTIAL |
| explicit `unknown` coverage | Missing | FAIL |

The physical runtime output is sufficient to trace the core cost-quality metrics, but insufficient to close SPEC-013 physical persistence because total spend reconciliation, explicit `unknown`, schema identity and structured invariants are absent.

---

## 6. Required Confirmations

| Confirmation requested | QA result | Notes |
|---|---|---|
| Mandatory invariants are PASS | FAIL / not verifiable in SPEC-013 form | Legacy aggregates satisfy known identities, but structured invariant records are missing from physical `runtime-output.json`. |
| `is_consumable = true` | FAIL | Field missing. |
| Canonical fields and deprecated aliases are coherent | FAIL / not verifiable | Legacy aliases `matched_spend` and `spend_only_spend` exist, but `deprecated_aliases` and canonical structured fields are missing physically. |
| Historical protected namespace not modified | PASS | `git status --short -- outputs/auc-001/2026-06-30 outputs/auc-001/pci-001/2026-06-30` returned no changes. |
| Report does not use Markdown as data source | FAIL / not physically verifiable | Logical implementation tests cover no-Markdown consumption, but the latest report was not persisted with a structured runtime-output lineage package. |

---

## 7. Automated Validation

QA executed:

```powershell
python -m py_compile tools\auc_001_canonical_cost_quality_model.py
powershell -ExecutionPolicy Bypass -File tests\evals\auc_001_canonical_cost_quality_model_tests.ps1
git status --short -- outputs\auc-001\2026-06-30 outputs\auc-001\pci-001\2026-06-30
```

Results:

| Check | Result |
|---|---|
| Runtime compile | PASS |
| SPEC-013 logical runtime tests | PASS, 10/10 |
| Historical namespace immutability | PASS |
| Physical `runtime-output.json` SPEC-013 persistence | FAIL |

The implementation is capable of producing the structured contract in test coverage, but the located physical runtime output has not persisted that contract.

---

## 8. Non-Blocking Analytical Observations

These observations do not cause the P0 blockage. They are assigned to backlog/P01 unless a future P01 gate promotes them to formal acceptance criteria.

| Observation | QA classification | Destination |
|---|---|---|
| Main table uses `ad_id_norm` without `ad_name` | Non-blocking; consistent with SPEC-012 key policy, but less readable for business review | P01/backlog presentation enrichment |
| No `ticket_status` analysis | Non-blocking; useful analytical depth gap, not required for SPEC-013 physical persistence | P01/backlog analytical depth |
| Weekly evolution is summarized rather than complete | Non-blocking; enough for P0 reading, can be expanded later | P01/backlog presentation/evidence detail |
| Recommendations are not yet expressed as measurable experiments | Non-blocking for P0 runtime validation; useful productization gap | P01/backlog recommendation design |

---

## 9. Criteria Met

- AUC-001 route and period are clear.
- MCP acquisition evidence exists from the latest execution context.
- The existing physical runtime output traces the main figures except all-signal total spend in structured form.
- Historical protected namespaces were not modified.
- Runtime implementation compiles.
- SPEC-013 logical tests pass.
- Residual analytical observations are not formal blockers by themselves.

---

## 10. Criteria Not Met

- The located physical `runtime-output.json` does not conform to SPEC-013.
- `is_consumable = true` cannot be confirmed because the field is absent.
- Required structured invariant records cannot be confirmed because the blocks are absent.
- Canonical structured spend fields and deprecated alias declarations cannot be confirmed physically.
- No physical new execution namespace was found for the latest AUC-001 rerun.
- No physical structured lineage package proves that the report consumed runtime JSON without Markdown as a data source.

---

## 11. Blockers

| Blocker | Severity | Reason |
|---|---|---|
| Physical `runtime-output.json` does not persist SPEC-013 schema | Blocking | P0 closure request explicitly depends on physical runtime conformance. |
| No persisted runtime output for latest real rerun | Blocking | QA cannot validate a non-existent physical artifact as the corresponding runtime package. |

---

## 12. Decision

```text
P0 BLOCKED
```

Rationale:

The recommended decision `P0 PASS WITH RESIDUAL OBSERVATIONS — READY FOR P01` is not available because a formal acceptance condition is not met: the physical `runtime-output.json` corresponding to the located execution namespace does not comply with SPEC-013 and does not expose `is_consumable = true`.

This is a persistence/packaging blocker, not an analytical-content blocker. The latest execution improves confidence that the AUC-001 analytical figures are reproducible through MCP, but it does not close the physical runtime-output condition.

---

## 13. Required Next Step

Do not start P01 yet.

Minimum required correction before re-evaluating P0:

1. Produce a new authorized AUC-001 execution namespace for the latest rerun or an explicitly authorized follow-up rerun.
2. Persist `execution/runtime-output.json` from the current SPEC-013-capable runtime without retrofitting the protected historical namespace.
3. Verify that the physical JSON includes `schema_family`, `output_schema_version`, `model_name`, `specification_versions`, `deprecated_aliases`, `spend_reconciliation`, `coverage_reconciliation`, explicit `unknown`, invariant records and `is_consumable = true`.
4. Re-run QA Gate for P0 closure.

