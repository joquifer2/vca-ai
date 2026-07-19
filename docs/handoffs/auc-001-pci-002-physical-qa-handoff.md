# AUC-001-PCI-002 Physical QA Handoff

## Metadata

| Field | Value |
| --- | --- |
| Handoff ID | HANDOFF-AUC-001-PCI-002-REAL-EXECUTION-TO-QA |
| From | Implementation Agent |
| To | QA Gate Agent |
| Date | 2026-07-19 |
| Scope | Physical SPEC-013 runtime validation after real PCI-002 execution |
| Execution Report | `docs/evaluations/auc-001/validations/auc-001-pci-002-real-execution-report.md` |
| Runtime Output | `outputs/auc-001/pci-002/2026-06-30/execution/runtime-output.json` |
| Namespace | `outputs/auc-001/pci-002/2026-06-30/` |

---

## 1. Purpose

Hand off the completed real AUC-001-PCI-002 execution package to QA Gate Agent.

This handoff requests physical validation of the runtime JSON from disk. It does not claim P0 closure by itself.

---

## 2. What QA Should Validate

QA should validate physically:

- `outputs/auc-001/pci-002/2026-06-30/execution/runtime-output.json` exists;
- `schema_family = auc_001_reconciliation_output`;
- `output_schema_version = auc_001_reconciliation_output.v1`;
- `spend_reconciliation` and `coverage_reconciliation` are present;
- `coverage_reconciliation.unknown.reason_codes` is present;
- all required spend and coverage invariants have `result = PASS`;
- `is_consumable = true`;
- `package_status.is_complete = true`;
- deprecated aliases equal their canonical fields;
- protected historical namespaces are unchanged;
- Markdown reports are not used as the data source.

---

## 3. Key Runtime Values For Traceability

| Field | Value |
| --- | --- |
| Runtime SHA256 | `d606aa10960942eef5c47bb7ba474b1e56bbb228cd14422b3cb35fefa22163ab` |
| Period | 2026-04-18 to 2026-06-30 |
| Leads | 1,329 |
| Leads A/B | 399 |
| Tier A leads | 59 |
| Total spend all signals | 1,406.25 EUR |
| Commercial spend total | 875.85 EUR |
| Matched commercial spend | 873.65 EUR |
| Matched leads | 1,187 |
| Matched A/B leads | 346 |
| Matched Tier A leads | 49 |

---

## 4. Execution Notes

- BigQuery MCP was the only data provider.
- No BigQuery CLI or direct client was used.
- The runtime was persisted from `CostQualityModel.structured_output`.
- The analytical report is not a data source for QA validation.
- Residual analytical observations remain routed to P01/backlog unless QA identifies a formal SPEC-013 contradiction.

---

## 5. Recommended QA Decision Set

QA should emit one of:

```text
P0 PASS - READY FOR P01
P0 PASS WITH RESIDUAL OBSERVATIONS - READY FOR P01
P0 BLOCKED
```

The recommended decision, if physical validation confirms this handoff, is:

```text
P0 PASS WITH RESIDUAL OBSERVATIONS - READY FOR P01
```