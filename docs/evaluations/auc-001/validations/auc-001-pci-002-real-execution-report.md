# AUC-001-PCI-002 Real Execution Report

## Metadata

| Field | Value |
| --- | --- |
| Report ID | EXEC-AUC-001-PCI-002-REAL-RUNTIME-PERSISTENCE |
| Agent | Implementation Agent |
| Date | 2026-07-19 |
| Authorization Gate | `gates/auc-001-pci-002-real-execution-authorization-gate.md` |
| Namespace | `outputs/auc-001/pci-002/2026-06-30/` |
| Runtime Output | `outputs/auc-001/pci-002/2026-06-30/execution/runtime-output.json` |
| Decision | REAL EXECUTION PACKAGE COMPLETE - READY FOR QA PHYSICAL VALIDATION |

---

## 1. Execution Summary

The authorized AUC-001-PCI-002 real execution package has been produced through BigQuery MCP only.

The physical SPEC-013 runtime output exists at:

```text
outputs/auc-001/pci-002/2026-06-30/execution/runtime-output.json
```

Runtime SHA256:

```text
d606aa10960942eef5c47bb7ba474b1e56bbb228cd14422b3cb35fefa22163ab
```

---

## 2. MCP Evidence Acquisition

| Query | Status | Trace Reference |
| --- | --- | --- |
| Lead coverage | success | `trc-30eaa444a4234c68b9e1470b37893208` |
| Spend coverage | success | `trc-82b59a3ccea149c2964b271218b555b2` |
| Lead aggregates | success | `trc-a8fbe1a84b284ac4871bb3c16a0e2132` |
| Spend aggregates | success | `trc-7e6d52c62c004fbe979ede02b9cdfdb2` |

No BigQuery CLI, direct BigQuery client or fallback was used.

---

## 3. Runtime Validation Snapshot

| Check | Result |
| --- | --- |
| Physical runtime-output exists | PASS |
| `schema_family` present | PASS |
| `output_schema_version` present | PASS |
| `spend_reconciliation` present | PASS |
| `coverage_reconciliation` present | PASS |
| `coverage_reconciliation.unknown.reason_codes` present | PASS |
| Deprecated aliases coherent | PASS |
| Required invariants PASS | PASS, 10/10 |
| `is_consumable = true` | PASS |
| `package_status.is_complete = true` | PASS |
| Markdown used as data source | No |
| Protected namespaces modified | No |

---

## 4. Core Runtime Figures

| Metric | Value |
| --- | ---: |
| Period | 2026-04-18 to 2026-06-30 |
| Leads | 1,329 |
| Leads A/B | 399 |
| Tier A leads | 59 |
| Total spend all signals | 1,406.25 EUR |
| Commercial spend total | 875.85 EUR |
| Matched commercial spend | 873.65 EUR |
| Spend-only commercial spend | 2.20 EUR |
| Matched leads | 1,187 |
| Matched A/B leads | 346 |
| Matched Tier A leads | 49 |
| `cpl_commercial_matched` | 0.74 EUR |
| `cost_per_ab_commercial_matched` | 2.53 EUR |
| `cost_per_tier_a_commercial_matched` | 17.83 EUR |
| `qualified_rate_ab_matched` | 29.15% |

---

## 5. Package Artifacts

| Artifact | Path |
| --- | --- |
| Context Definition | `outputs/auc-001/pci-002/2026-06-30/execution/context-definition.json` |
| Runtime Output | `outputs/auc-001/pci-002/2026-06-30/execution/runtime-output.json` |
| Execution Validation | `outputs/auc-001/pci-002/2026-06-30/execution/execution-validation.json` |
| Package Manifest | `outputs/auc-001/pci-002/2026-06-30/execution/package-manifest.json` |
| Evidence Acquisition Record | `outputs/auc-001/pci-002/2026-06-30/evidence/evidence-acquisition-record.json` |
| Evidence Set | `outputs/auc-001/pci-002/2026-06-30/evidence/evidence-set.json` |
| Knowledge Set | `outputs/auc-001/pci-002/2026-06-30/knowledge/knowledge-set.json` |
| Recommendation Set | `outputs/auc-001/pci-002/2026-06-30/recommendations/recommendation-set.json` |
| Presentation Lineage | `outputs/auc-001/pci-002/2026-06-30/presentation/presentation-lineage.md` |
| Analytical Report | `outputs/auc-001/pci-002/2026-06-30/analytical-report/analytical-report.md` |

---

## 6. Local Verification

Commands run after package materialization:

```powershell
python -m py_compile tools\auc_001_canonical_cost_quality_model.py
powershell -ExecutionPolicy Bypass -File tests\evals\auc_001_canonical_cost_quality_model_tests.ps1
```

Result:

```text
All AUC-001 canonical cost-quality model tests passed: 14
```

Protected namespace check:

```powershell
git status --short -- outputs\auc-001\2026-06-30 outputs\auc-001\pci-001\2026-06-30
```

Result: empty output.

---

## 7. Handoff Decision

```text
READY FOR QA PHYSICAL VALIDATION
```

QA Gate Agent should now validate the physical JSON from disk and then determine whether P0 can move from `P0 BLOCKED` to the appropriate final closure decision.