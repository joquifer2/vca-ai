# Gates

Este directorio contiene gates documentales y records de decision de avance o cierre. Los gates no deben mezclarse con evaluaciones.

| Gate | Tipo | Estado | Decision |
|---|---|---|---|
| [spec-008-development-entry-phase-gate.md](spec-008-development-entry-phase-gate.md) | Phase Gate | Passed with observations | Development Authorized |
| [auc-001-experimental-closure-gate.md](auc-001-experimental-closure-gate.md) | Closure Gate | Passed | READY FOR CLOSURE |
| [auc-001-pci-001-entry-gate.md](auc-001-pci-001-entry-gate.md) | Post-Closure Iteration Entry Gate | Passed | PASS |
| [auc-001-pci-001-exit-gate.md](auc-001-pci-001-exit-gate.md) | Post-Closure Iteration Exit Gate | Passed With Conditions | PASS WITH CONDITIONS |
| [spec-013-auc-001-structured-reconciliation-output-entry-gate.md](spec-013-auc-001-structured-reconciliation-output-entry-gate.md) | Post-Closure Specification Entry Gate | Passed | PASS |
| [spec-013-auc-001-structured-reconciliation-output-exit-gate.md](spec-013-auc-001-structured-reconciliation-output-exit-gate.md) | Post-Closure Specification Exit Gate | Passed With Conditions | PASS WITH CONDITIONS |
| [auc-001-p0-operational-closure-gate.md](auc-001-p0-operational-closure-gate.md) | P0 Operational Closure Gate | Passed With Residual Observations | P0 PASS WITH RESIDUAL OBSERVATIONS - READY FOR P01 |
| [auc-001-pci-002-entry-gate.md](auc-001-pci-002-entry-gate.md) | Post-Closure Iteration Entry Gate | Passed With Conditions | PASS WITH CONDITIONS |
| [auc-001-pci-002-real-execution-authorization-gate.md](auc-001-pci-002-real-execution-authorization-gate.md) | Post-Closure Iteration Execution Authorization Gate | Passed | REAL EXECUTION AUTHORIZED VIA BIGQUERY MCP |
| [auc-001-pci-002-exit-gate.md](auc-001-pci-002-exit-gate.md) | Post-Closure Iteration Exit Gate | Passed | PASS |
| [auc-001-p01-documentary-closure-gate.md](auc-001-p01-documentary-closure-gate.md) | P01 Documentary Closure Gate | Passed | PASS |
| [auc-001-p02-entry-gate.md](auc-001-p02-entry-gate.md) | P02 Implementation Entry Gate | Passed With Conditions | PASS WITH CONDITIONS |
| [specs-001-003-qa-gate.md](specs-001-003-qa-gate.md) | QA Gate | Documented | Historical/supporting |
| [specs-004-007-qa-gate.md](specs-004-007-qa-gate.md) | QA Gate | Documented | Historical/supporting |

## Tipos

- Phase Gates: autorizan transicion de fase.
- Acceptance Gates: validan aceptacion de capabilities o casos segun specs.
- Closure Gates: cierran ciclos experimentales o documentales aprobados.
- Post-Closure Iteration Gates: gobiernan iteraciones sucesoras separadas sin reabrir ni sobrescribir el ciclo cerrado anterior.

## Output Namespace Governance

`AUC-001-PCI-001` uses `outputs/auc-001/pci-001/2026-06-30/` as its official post-closure output namespace.

The original namespace `outputs/auc-001/2026-06-30/` is immutable historical output from the closed cycle. `outputs/auc-001-pci-001/` is not authorized. Future post-closure iterations must use `outputs/auc-001/pci-00N/<execution-date>/`. `AUC-001-PCI-002` used `outputs/auc-001/pci-002/2026-06-30/` for the authorized real execution. Its Exit Gate is PASS, P0 Operational Closure is `P0 PASS WITH RESIDUAL OBSERVATIONS - READY FOR P01`, P01 Documentary Closure is `AUC-001-P01 DOCUMENTARY CLOSURE PASS - READY FOR CONTROLLED POST-P01 IMPLEMENTATION PLANNING`, and P02 Entry Gate is `PASS WITH CONDITIONS` for controlled implementation only.

Entry gates require the namespace to be defined before execution. Exit gates validate only artifacts contained inside the corresponding namespace.
