# SPEC-013 Corrective Tasks - AUC-001 Runtime Output Persistence

## Metadata

| Field | Value |
| --- | --- |
| Artifact ID | TASKS-SPEC-013-AUC-001-RUNTIME-OUTPUT-PERSISTENCE-CORRECTION |
| Parent Specification | `specs/spec-013-auc-001-structured-reconciliation-output.md` |
| Parent Use Case | AUC-001 - Meta Lead Quality Analysis |
| Agent | Specification Agent |
| Formalized | 2026-07-19 |
| Decision | CORRECTIVE TASKS UNDER SPEC-013 |
| P0 Status | P0 BLOCKED until physical SPEC-013 runtime output is validated |
| Implementation Authorized | Real execution authorized by `gates/auc-001-pci-002-real-execution-authorization-gate.md` |
| Planning Status | AUC-001-PCI-002 QA local validation PASS; real execution authorized via BigQuery MCP |

---

## 1. Purpose

Formalize the minimum corrective work required for a real AUC-001 execution to persist a physical `execution/runtime-output.json` that conforms to SPEC-013.

This artifact does not create a new specification. It constrains a corrective implementation path under SPEC-013 because SPEC-013 already requires future AUC-001 executions to persist structured spend and coverage reconciliation.

---

## 2. Formalization Decision

```text
CORRECTIVE TASKS UNDER SPEC-013
```

Rationale:

- SPEC-013 purpose already covers physical structured persistence for future AUC-001 executions.
- SPEC-013 AC-001 and AC-002 already require full spend and coverage reconciliation to be persisted.
- SPEC-013 explicitly protects `outputs/auc-001/pci-001/2026-06-30/` and applies only to future executions.
- The P0 QA blockage is a failure to satisfy a residual physical persistence condition, not a gap in the model contract.
- The Architect Agent investigation classified the cause as an integration gap between Execution Workflow, adapter and Persistence/Packaging.
- No reusable Foundation-level orchestration capability is required to close this AUC-001-specific condition.

Rejected options:

| Option | Decision | Reason |
| --- | --- | --- |
| `SPEC-013 ADDENDUM REQUIRED` | Rejected | The required behavior is already inside SPEC-013 purpose, scope, acceptance criteria and residual conditions. |
| `NEW SPECIFICATION REQUIRED` | Rejected | The correction does not require a new artifact type, product contract, Foundation capability or general orchestration model. |

---

## 3. Minimum Behavior Required

### 3.1 Pipeline Point

Persistence must run after `build_cost_quality_model(...)` returns a `CostQualityModel` instance and before Evidence Set, Knowledge, Recommendations or Presentation are considered packaged for the execution.

The persistence step belongs between:

```text
Analytical Preparation / Runtime Model Construction
        -> Runtime Output Persistence
        -> Evidence Set Construction / Packaging
```

### 3.2 Responsible Component

The responsible component is the AUC-001 execution packaging layer or execution orchestrator for the concrete authorized run.

If no dedicated orchestrator exists, Implementation Agent must introduce the minimum AUC-001-local packaging bridge needed to persist the runtime output. This must not become a general framework orchestration system.

### 3.3 Required Input

The persistence step requires:

- `CostQualityModel` returned by `build_cost_quality_model(...)`;
- execution metadata;
- source acquisition metadata already available from the execution;
- namespace target approved before writing;
- adapter output that preserves all spend signals needed for SPEC-013 reconciliation.

### 3.4 Required Runtime Contract Source

The persisted `execution/runtime-output.json` must use `CostQualityModel.structured_output` as the authoritative source for the SPEC-013 contract.

The writer may wrap that object with execution metadata, but it must not reconstruct, recalculate or manually restate the structured reconciliation from Markdown, presentation tables or legacy aggregates.

### 3.5 Required Execution Metadata

The physical JSON must include or preserve at minimum:

- `execution_id`;
- `period_start`;
- `period_end`;
- `runtime` or `model_name`;
- `schema_family`;
- `output_schema_version`;
- `specification_versions` including `SPEC-012` and `SPEC-013`;
- `source_tables` or source acquisition reference;
- `data_provider = BigQuery MCP Server` when new evidence is acquired;
- `input_hashes` or equivalent deterministic input traceability;
- `namespace` or output path;
- `is_consumable`;
- `issues` and blockers if present.

### 3.6 JSON Serialization

Serialization must produce a valid UTF-8 JSON file at:

```text
<authorized_namespace>/execution/runtime-output.json
```

The JSON must preserve decimal precision sufficient for invariant validation. Presentation rounding must not be used as the persisted source of truth.

### 3.7 Namespace

The correction must use a new authorized post-closure namespace:

```text
outputs/auc-001/pci-002/<execution-date>/
```

For a revalidation of the same business cutoff used by the blocked P0 review, the candidate namespace is:

```text
outputs/auc-001/pci-002/2026-06-30/
```

The exact execution date/cutoff must be fixed by the next Entry Gate or authorized execution request before writing.

### 3.8 Historical Namespace Protection

The following namespaces must not be modified:

```text
outputs/auc-001/2026-06-30/
outputs/auc-001/pci-001/2026-06-30/
```

Retrofitting either namespace to satisfy SPEC-013 is prohibited.

### 3.9 Invariant Failure

If any required SPEC-013 invariant is `FAIL`:

- `is_consumable` must be `false`;
- the failure must be persisted in `runtime-output.json`;
- Evidence Set, Knowledge, Recommendations and Presentation must not be declared complete for the execution;
- P0 Operational Closure Gate must remain blocked.

### 3.10 Non-Consumable Runtime

If `is_consumable = false` for any reason:

- the execution package may preserve diagnostic artifacts;
- the analytical report must not be declared fully packaged;
- downstream consumers must reject or quarantine the output;
- QA must treat the run as not ready for P0 closure.

### 3.11 Write Failure

If writing `execution/runtime-output.json` fails:

- the execution package is incomplete;
- no report generated from that execution can be treated as fully packaged;
- QA must block P0 closure;
- the failure must be recorded in the execution validation artifact.

### 3.12 Relation To Report Materialization

Presentation may only be considered complete when either:

- it consumes the persisted structured runtime output directly; or
- it carries an explicit physical lineage reference to the persisted runtime output used by Evidence Set construction.

Markdown reports must not be used as the data source to complete or validate `runtime-output.json`.

---

## 4. Spend Adapter Requirement

The adapter must preserve enough spend information to produce the SPEC-013 reconciliation fields:

- `total_spend_all_signals`;
- `spend_by_signal`;
- `commercial_spend`;
- `matched_commercial_spend`;
- `spend_only_commercial_spend`;
- `non_commercial_spend`;
- `non_commercial_spend_by_signal`.

The adapter must not reduce all spend evidence to `COMMERCIAL` before the structured reconciliation is built.

This does not redesign SPEC-012. Commercial efficiency metrics remain restricted to the commercial matched universe. Non-commercial signals are retained for reconciliation and descriptive spend shares only.

---

## 5. Namespace Decision

The correction constitutes `AUC-001-PCI-002`, not a continuation write into `AUC-001-PCI-001`.

Rationale:

- `AUC-001-PCI-001` has an Exit Gate already evaluated as `PASS WITH CONDITIONS`.
- Its physical namespace is protected and must not be retrofitted.
- Repository governance says future post-closure iterations use `outputs/auc-001/pci-00N/<execution-date>/`.
- The correction requires a new real execution package that QA can inspect physically.

---

## 6. Corrective Task Set

| Task | Title | Owner | Status | Acceptance Evidence |
| --- | --- | --- | --- | --- |
| CT-001 | Define `AUC-001-PCI-002` execution namespace before any write | Tasks Planner / QA Gate | Proposed | Entry gate or task plan records `outputs/auc-001/pci-002/<execution-date>/`. |
| CT-002 | Add minimal AUC-001 packaging bridge for runtime output persistence | Implementation Agent | Proposed | `execution/runtime-output.json` is written from `CostQualityModel.structured_output`. |
| CT-003 | Preserve all spend signals through adapter until structured reconciliation is built | Implementation Agent | Proposed | Runtime output exposes `total_spend_all_signals`, `spend_by_signal` and non-commercial spend. |
| CT-004 | Persist execution metadata with structured runtime output | Implementation Agent | Proposed | JSON includes execution ID, period, provider/source lineage, input hashes and schema metadata. |
| CT-005 | Block package completion when `is_consumable = false` or required invariants fail | Implementation Agent | Proposed | Tests and validation show non-consumable output prevents completed packaging. |
| CT-006 | Block package completion on runtime-output write failure | Implementation Agent | Proposed | Tests simulate write failure and confirm packaging is incomplete. |
| CT-007 | Add lineage from Evidence/Presentation artifacts to persisted runtime output | Implementation Agent / Documentation Agent | Proposed | Report or validation artifact references physical runtime output path and hash. |
| CT-008 | Add physical persistence tests | Implementation Agent | Proposed | Tests cover serialization, namespace write, overwrite rejection and physical JSON validation. |
| CT-009 | Run authorized real AUC-001 execution package without historical overwrite | Implementation Agent | Proposed | New PCI-002 namespace contains execution artifacts; protected namespaces unchanged. |
| CT-010 | Re-run P0 Operational Closure Gate | QA Gate Agent | Proposed | QA validates physical `runtime-output.json` without using Markdown as data source. |

---

## 7. Acceptance Criteria

### AC-COR-001

A real authorized AUC-001 execution generates a new namespace under `outputs/auc-001/pci-002/<execution-date>/`.

### AC-COR-002

`execution/runtime-output.json` exists physically in the new namespace.

### AC-COR-003

The physical JSON contains all mandatory SPEC-013 fields: `schema_family`, `output_schema_version`, `model_name`, `specification_versions`, `deprecated_aliases`, `spend_reconciliation`, `coverage_reconciliation`, invariant records and `is_consumable`.

### AC-COR-004

`coverage_reconciliation.unknown` is present explicitly, even when all values are zero.

### AC-COR-005

Deprecated aliases are present only as declared aliases and equal their canonical fields.

### AC-COR-006

All required spend and coverage invariants are persisted with `result = PASS`.

### AC-COR-007

`is_consumable = true` for a closable execution.

### AC-COR-008

The runtime preserves spend across all authorized signals required for reconciliation.

### AC-COR-009

Presentation consumes the structured runtime output or carries unequivocal physical lineage to it.

### AC-COR-010

A persistence failure prevents execution packaging from being declared complete.

### AC-COR-011

Historical namespaces remain unchanged.

### AC-COR-012

QA can validate the physical runtime artifact without using Markdown as a data source.

---

## 8. Required Tests

| Test ID | Test | Minimum Expected Result |
| --- | --- | --- |
| TST-COR-001 | Serialize `CostQualityModel.structured_output` to JSON | Required SPEC-013 fields persist. |
| TST-COR-002 | Write runtime output into a new namespace | File exists at `execution/runtime-output.json`. |
| TST-COR-003 | Reject overwrite of `outputs/auc-001/2026-06-30/` and `outputs/auc-001/pci-001/2026-06-30/` | Write is blocked before mutation. |
| TST-COR-004 | Preserve all spend signals through adapter | `total_spend_all_signals`, `spend_by_signal` and `non_commercial_spend` are correct. |
| TST-COR-005 | `is_consumable = false` blocks package completion | Execution package status is not complete. |
| TST-COR-006 | Required invariant `FAIL` blocks package completion | Runtime persists failure and package remains non-consumable. |
| TST-COR-007 | Write failure blocks package completion | Error is surfaced and no complete report package is declared. |
| TST-COR-008 | Analytical report lineage references persisted runtime output | Report/validation contains path and hash or equivalent immutable reference. |
| TST-COR-009 | Physical end-to-end validation | QA validates JSON from disk, not Markdown. |

---

## 9. Constraints

- No code implementation is authorized by this Specification Agent artifact.
- No BigQuery query is authorized by this artifact.
- No report regeneration is authorized by this artifact.
- No historical namespace modification is authorized.
- No SPEC-012 redesign is authorized.
- No product analytical contract is created.
- No AIF Foundation promotion or transversal orchestration capability is introduced.

---

## 10. Dependencies

- `specs/spec-013-auc-001-structured-reconciliation-output.md`;
- `specs/spec-012-auc-001-canonical-cost-quality-model.md`;
- `tools/auc_001_canonical_cost_quality_model.py`;
- `tests/evals/auc_001_canonical_cost_quality_model_tests.ps1`;
- `gates/spec-013-auc-001-structured-reconciliation-output-entry-gate.md`;
- `gates/spec-013-auc-001-structured-reconciliation-output-exit-gate.md`;
- `docs/evaluations/auc-001/validations/spec-013-structured-reconciliation-output-qa-validation.md`;
- `docs/evaluations/auc-001/validations/auc-001-p0-operational-closure-qa-validation.md`;
- `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`;
- `analytical_use_cases/auc-001/README.md`;
- `docs/context_refs.md`.

---

## 11. Cross-Artifact Impact Analysis

| Artifact | Impact | Proposed update |
| --- | --- | --- |
| SPEC-013 | No addendum required | Keep specification intact; treat this artifact as corrective task formalization. |
| SPEC-012 | No impact | Keep canonical metric rules unchanged. |
| AUC-001 index | Impact | Link this corrective task artifact and mark PCI-002 as proposed corrective execution. |
| Context References | Impact | Index this artifact as post-closure SPEC-013 corrective traceability. |
| Gates | Impact | Existing P0 gate remains blocked; a PCI-002 Entry Gate should be created before implementation/execution. |
| Tasks | Impact | This file becomes the task proposal for Tasks Planner / Implementation Agent. |
| Contracts | No immediate impact | Do not update unless implementation discovers contradiction. |
| Skills / Runbook | Possible impact | Only update later if packaging becomes a mandatory AUC-001 runbook step. |
| Glossary | No immediate impact | Defer unless terms recur. |

---

## 12. Conditions To Reopen P0 Operational Closure Gate

P0 Operational Closure Gate may be reopened only after:

1. A PCI-002 Entry Gate or equivalent authorization exists.
2. A real AUC-001 execution package is produced in a new authorized namespace.
3. `execution/runtime-output.json` exists physically and conforms to SPEC-013.
4. The physical runtime output has `is_consumable = true`.
5. All required invariant records are `PASS`.
6. The runtime output includes all-signal spend reconciliation.
7. Presentation or execution validation records physical lineage to the runtime output.
8. Protected historical namespaces show no changes.
9. QA validates the physical JSON without using Markdown as source data.

---

## 13. Next Recommended Agent

Next recommended agent: **Implementation Agent**.

Recommended instruction:

```text
Actua como Implementation Agent de vca-ai. Ejecuta el paquete real AUC-001-PCI-002 autorizado via BigQuery MCP, sin ampliar alcance, sin iniciar P01 y sin tocar namespaces historicos protegidos. El runtime fisico debe persistirse en `outputs/auc-001/pci-002/2026-06-30/execution/runtime-output.json` conforme a SPEC-013 para posterior validacion QA.
```

---

## Definition of Done

This corrective formalization is complete when:

- the methodological decision is explicit;
- the behavior required for runtime output persistence is bounded;
- PCI-002 namespace governance is defined;
- adapter requirements are stated without redesigning SPEC-012;
- acceptance criteria and tests are verifiable;
- historical namespace protection is preserved;
- conditions to reopen P0 are explicit;
- the next agent is identified.