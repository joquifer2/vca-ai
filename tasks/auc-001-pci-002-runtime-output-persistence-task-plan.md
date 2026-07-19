# AUC-001-PCI-002 Runtime Output Persistence Task Plan

## Metadata

| Field | Value |
| --- | --- |
| Artifact ID | TASK-PLAN-AUC-001-PCI-002-RUNTIME-OUTPUT-PERSISTENCE |
| Use Case | AUC-001 - Meta Lead Quality Analysis |
| Iteration | AUC-001 Post-Closure Iteration 2 |
| Iteration ID | AUC-001-PCI-002 |
| Parent Specification | `specs/spec-013-auc-001-structured-reconciliation-output.md` |
| Corrective Formalization | `tasks/spec-013-auc-001-runtime-output-persistence-corrective-tasks.md` |
| Agent | Tasks Planner Agent |
| Created | 2026-07-19 |
| Template | Inferred SDD task-plan structure; no compatible task-plan template exists in `docs/templates/` |
| Status | QA local validation PASS; real execution authorized via BigQuery MCP |
| Implementation Authorized | Real execution authorized by `gates/auc-001-pci-002-real-execution-authorization-gate.md` |
| Entry Gate Owner | QA Gate Agent |

---

## 1. Objective

Plan the minimum corrective work required for a real AUC-001 execution to persist a physical `execution/runtime-output.json` conforming to SPEC-013 in a new protected namespace.

This plan does not implement code, regenerate reports, query BigQuery, modify historical outputs or open P01.

---

## 2. Source Artifacts

| Type | Artifact |
| --- | --- |
| Specification | `specs/spec-013-auc-001-structured-reconciliation-output.md` |
| Corrective formalization | `tasks/spec-013-auc-001-runtime-output-persistence-corrective-tasks.md` |
| Parent model specification | `specs/spec-012-auc-001-canonical-cost-quality-model.md` |
| QA blockage | `gates/auc-001-p0-operational-closure-gate.md` |
| QA validation | `docs/evaluations/auc-001/validations/auc-001-p0-operational-closure-qa-validation.md` |
| SPEC-013 validation | `docs/evaluations/auc-001/validations/spec-013-structured-reconciliation-output-qa-validation.md` |
| AUC-001 routing | `.github/skills/meta-lead-quality-analysis/RUNBOOK.md` |
| AUC-001 index | `analytical_use_cases/auc-001/README.md` |

---

## 3. Scope

In scope:

- create the PCI-002 implementation plan;
- preserve the requirement that QA Gate Agent performs the Entry Gate;
- plan a minimal AUC-001-local persistence bridge from `CostQualityModel.structured_output`;
- plan adapter correction to preserve all spend signals for structured reconciliation;
- plan physical JSON validation and package-completion blocking behavior;
- plan QA revalidation of P0 only after a real PCI-002 package exists.

Out of scope:

- code implementation;
- BigQuery execution;
- report regeneration;
- historical namespace mutation;
- new specification creation;
- P01 initiation;
- analytical improvements such as ticket status analysis or experiment design.

---

## 4. Namespace Policy

PCI-002 must use:

```text
outputs/auc-001/pci-002/<execution-date>/
```

If the authorized corrective execution revalidates the same business cutoff as the blocked P0 review, the candidate namespace is:

```text
outputs/auc-001/pci-002/2026-06-30/
```

The exact namespace must be confirmed by the QA Entry Gate before any write.

Protected namespaces:

```text
outputs/auc-001/2026-06-30/
outputs/auc-001/pci-001/2026-06-30/
```

These namespaces must not be modified, backfilled or retrofitted.

---

## 5. Task Register

| ID | Task | Type | Owner | Depends On | Expected Result | Completion Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| PCI2-T001 | Publish PCI-002 task plan | Planning | Tasks Planner Agent | Corrective formalization | Implementation scope, sequence and constraints are explicit | This task plan exists and is indexed |
| PCI2-T002 | Prepare Entry Gate handoff for QA | Governance | Tasks Planner Agent | PCI2-T001 | QA receives criteria and evidence checklist without a gate decision | QA handoff artifact exists |
| PCI2-T003 | Evaluate PCI-002 Entry Gate | Validation | QA Gate Agent | PCI2-T001, PCI2-T002 | QA decides whether implementation may start | `gates/auc-001-pci-002-entry-gate.md` created by QA Gate Agent |
| PCI2-T004 | Locate execution packaging integration point | Development | Implementation Agent | PCI2-T003 PASS | Exact persistence insertion point is confirmed | Implementation notes or code references in implementation validation |
| PCI2-T005 | Implement minimal runtime-output writer | Development | Implementation Agent | PCI2-T004 | `CostQualityModel.structured_output` can be serialized to `execution/runtime-output.json` | Code diff and serialization test |
| PCI2-T006 | Preserve all spend signals through adapter | Development | Implementation Agent | PCI2-T004 | SPEC-013 all-signal reconciliation fields are available before persistence | Unit test covering commercial and non-commercial spend |
| PCI2-T007 | Persist execution metadata and lineage | Development | Implementation Agent | PCI2-T005 | Runtime JSON includes execution ID, period, provider/source lineage, namespace and input hashes or equivalent traceability | Runtime metadata test |
| PCI2-T008 | Enforce package completion blockers | Development | Implementation Agent | PCI2-T005 | `is_consumable = false`, invariant failure or write failure prevents completed packaging | Negative-path tests |
| PCI2-T009 | Add protected namespace safeguards | Development | Implementation Agent | PCI2-T005 | Historical namespaces cannot be overwritten by the corrective writer | Overwrite rejection test |
| PCI2-T010 | Run local validation suite | Validation | Implementation Agent | PCI2-T005 to PCI2-T009 | Technical changes compile and tests pass | Test command output recorded in validation |
| PCI2-T011 | Produce authorized real PCI-002 execution package | Development | Implementation Agent | PCI2-T003 PASS, PCI2-T010 PASS, MCP authorization when needed | New PCI-002 namespace contains physical execution artifacts | `outputs/auc-001/pci-002/<execution-date>/execution/runtime-output.json` exists |
| PCI2-T012 | Validate physical SPEC-013 runtime output | Validation | QA Gate Agent | PCI2-T011 | QA validates JSON from disk, not Markdown | QA validation artifact records physical checks |
| PCI2-T013 | Reopen P0 Operational Closure Gate | Validation | QA Gate Agent | PCI2-T012 PASS | P0 decision is updated using PCI-002 evidence | Updated P0 closure gate |
| PCI2-T014 | Index final PCI-002 outcome | Documentation | Documentation Agent | PCI2-T013 | Roadmap, AUC index and context refs reflect final state | Updated indexes only |

---

## 6. Recommended Execution Order

1. Complete planning and QA handoff: PCI2-T001, PCI2-T002.
2. QA Gate Agent performs Entry Gate: PCI2-T003.
3. Implementation Agent performs scoped technical correction: PCI2-T004 to PCI2-T010.
4. Authorized real execution package is produced: PCI2-T011.
5. QA Gate Agent validates physical runtime and reopens P0: PCI2-T012, PCI2-T013.
6. Documentation Agent indexes the final outcome: PCI2-T014.

---

## 7. Blocking Conditions

Implementation must not start if:

- QA Entry Gate has not been created by QA Gate Agent;
- QA Entry Gate is not PASS or explicitly equivalent authorization;
- namespace is unresolved;
- the proposed work would modify protected historical outputs;
- the proposed work requires a new specification;
- BigQuery access is needed but MCP authorization is not available at execution time.

P0 must remain blocked if:

- no physical PCI-002 runtime JSON exists;
- the JSON does not conform to SPEC-013;
- `is_consumable` is absent or false;
- required invariants are not all PASS;
- QA must rely on Markdown as the source of data;
- protected namespaces changed.

---

## 8. Residual Observations Routing

The following observations do not belong to the PCI-002 P0 closure correction unless they contradict formal SPEC-013 acceptance criteria:

| Observation | Routing |
| --- | --- |
| Use of `ad_id_norm` without `ad_name` in the main table | P01 / backlog |
| No `ticket_status` analysis | P01 / backlog |
| Weekly evolution summarized rather than complete | P01 / backlog |
| Recommendations not yet expressed as measurable experiments | P01 / backlog |

---

## 9. Definition of Done

This plan is complete when:

- PCI-002 scope is explicit and bounded;
- the QA Entry Gate is reserved to QA Gate Agent;
- tasks are sequenced and objectively verifiable;
- historical namespace protection is restated;
- no implementation, BigQuery execution, output mutation or report regeneration has occurred;
- the next agent is identified.

---

## 10. Next Agent

Next required agent: **Implementation Agent**.

Required next action:

```text
Actua como Implementation Agent de vca-ai. Ejecuta el paquete real AUC-001-PCI-002 autorizado por `gates/auc-001-pci-002-real-execution-authorization-gate.md`, usando exclusivamente BigQuery MCP y el Runbook AUC-001. Escribe solo en `outputs/auc-001/pci-002/2026-06-30/`, persiste `execution/runtime-output.json` conforme a SPEC-013 y detente ante cualquier bloqueo MCP, invariant failure, `is_consumable = false`, fallo de escritura o intento de tocar namespaces protegidos.
```
