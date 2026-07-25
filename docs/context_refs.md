# Context References

Este documento es el índice detallado de trazabilidad y contexto oficial de `vca-ai`.

No sustituye a `README.md`, `project_brief.md`, las Specifications, los contratos, los gates ni los índices específicos de cada caso de uso.

Estado del proyecto: Development Authorized.

---

## 1. Identidad del proyecto

```yaml
proyecto:
  nombre: VCA IA
  id_proyecto: VCA-IA
  tipo_proyecto: Proyecto derivado SDD para un sistema analítico trazable de VCA
  estado: Development Authorized
  version: v1.0.0
  fecha_creacion: 2026-07-10
  responsable: VCA IA maintainers

cliente:
  id_cliente: VCA
  nombre_cliente: VCA
  estado_relacion: Contexto operativo del proyecto
```

---

## 2. Contexto requerido

| Clasificación | Recurso | Fuente |
|---|---|---|
| Required | Project Brief | [../project_brief.md](/project_brief.md) |
| Required | README | [../README.md](/README.md) |
| Required | Specifications | [../specs/](/specs/) |
| Required | Contracts | [contracts/](/docs/contracts/) |
| Required | BigQuery MCP discover_metadata Contract Reference | [contracts/bigquery-mcp-discover-metadata.contract.md](/docs/contracts/bigquery-mcp-discover-metadata.contract.md) |
| Required | Tasks Backlog | [tasks.md](/docs/tasks.md) |
| Supporting | Knowledge Base | [../knowledge/client/](/knowledge/client/) |
| Supporting | Glosario | [glosario_terminos.md](/docs/glosario_terminos.md) |

---

## 3. AUC-001 Source of Truth

| Clasificación | Recurso | Fuente |
|---|---|---|
| Required | Índice AUC-001 | [../analytical_use_cases/auc-001/README.md](/analytical_use_cases/auc-001/README.md) |
| Required | Definición AUC-001 | [../analytical_use_cases/meta_lead_quality_analysis.md](/analytical_use_cases/meta_lead_quality_analysis.md) |
| Required | Analytical Contract AUC-001 | [../analytical_use_cases/auc-001/analytical-contract.md](/analytical_use_cases/auc-001/analytical-contract.md) |
| Required | Skill Meta Lead Quality Analysis | [../.github/skills/meta-lead-quality-analysis/SKILL.md](/.github/skills/meta-lead-quality-analysis/SKILL.md) |
| Required | Runbook | [../.github/skills/meta-lead-quality-analysis/RUNBOOK.md](/.github/skills/meta-lead-quality-analysis/RUNBOOK.md) |
| Required | Checklist | [../.github/skills/meta-lead-quality-analysis/CHECKLIST.md](/.github/skills/meta-lead-quality-analysis/CHECKLIST.md) |
| Required | Closure Gate | [../gates/auc-001-experimental-closure-gate.md](/gates/auc-001-experimental-closure-gate.md) |
| Post-closure | SPEC-012 Canonical Cost-Quality Model | [../specs/spec-012-auc-001-canonical-cost-quality-model.md](/specs/spec-012-auc-001-canonical-cost-quality-model.md) |
| Post-closure | SPEC-013 Structured Reconciliation Output | [../specs/spec-013-auc-001-structured-reconciliation-output.md](/specs/spec-013-auc-001-structured-reconciliation-output.md) |
| P01 | SPEC-014 Analytical Product Contract | [../specs/spec-014-auc-001-analytical-product-contract.md](/specs/spec-014-auc-001-analytical-product-contract.md) |
| P04 | SPEC-015 Canonical Projection Consolidation | [../specs/spec-015-auc-001-canonical-projection-consolidation.md](/specs/spec-015-auc-001-canonical-projection-consolidation.md) |
| Post-P04 | SPEC-016 Operational Acceptance Package Contract | [../specs/spec-016-auc-001-operational-acceptance-package-contract.md](/specs/spec-016-auc-001-operational-acceptance-package-contract.md) |
| IC-001 | AUC-001 IC-001 Task Plan | [../tasks/auc-001-ic-001-integral-product-consolidation-task-plan.md](/tasks/auc-001-ic-001-integral-product-consolidation-task-plan.md) |
| IC-001 | AUC-001 IC-001 Entry Gate | [../gates/auc-001-ic-001-entry-gate.md](/gates/auc-001-ic-001-entry-gate.md) |
| IC-001 | AUC-001 IC-001 Closure Gate | [../gates/auc-001-ic-001-closure-gate.md](/gates/auc-001-ic-001-closure-gate.md) |
| P01 | P01 Analytical Product Contract Architectural Analysis | [decisions/auc-001/auc-001-p01-analytical-product-contract-architectural-analysis.md](/docs/decisions/auc-001/auc-001-p01-analytical-product-contract-architectural-analysis.md) |
| P01 | AUC-001 P01 Documentary Closure Gate | [../gates/auc-001-p01-documentary-closure-gate.md](/gates/auc-001-p01-documentary-closure-gate.md) |
| P02 | AUC-001 P02 Analytical Product Contract Implementation Task Plan | [../tasks/auc-001-p02-analytical-product-contract-implementation-task-plan.md](/tasks/auc-001-p02-analytical-product-contract-implementation-task-plan.md) |
| P02 | AUC-001 P02 Entry Gate | [../gates/auc-001-p02-entry-gate.md](/gates/auc-001-p02-entry-gate.md) |
| P02 | AUC-001 P02 Technical And Functional QA Validation | [evaluations/auc-001/validations/auc-001-p02-technical-functional-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-p02-technical-functional-qa-validation.md) |
| P02 | AUC-001 P02 Real Execution Authorization Gate | [../gates/auc-001-p02-real-execution-authorization-gate.md](/gates/auc-001-p02-real-execution-authorization-gate.md) |
| P02 | AUC-001 P02 Physical Product QA Revalidation | [evaluations/auc-001/validations/auc-001-p02-physical-product-qa-revalidation.md](/docs/evaluations/auc-001/validations/auc-001-p02-physical-product-qa-revalidation.md) |
| P02 | AUC-001 P02 Closure Gate | [../gates/auc-001-p02-closure-gate.md](/gates/auc-001-p02-closure-gate.md) |
| Transversal | AUC-001 P01 And Transversal Documentation Final Review | [evaluations/auc-001/validations/auc-001-p01-transversal-documentation-final-review.md](/docs/evaluations/auc-001/validations/auc-001-p01-transversal-documentation-final-review.md) |
| P02 | AUC-001 P02 Output Namespace | `outputs/auc-001/p02/2026-07-17/` |
| P03 | AUC-001 P03 Output Namespace | `outputs/auc-001/p03/2026-07-22/` |
| P04 | AUC-001 P04 Implementation Handoff | [evaluations/auc-001/validations/auc-001-p04-implementation-handoff.md](/docs/evaluations/auc-001/validations/auc-001-p04-implementation-handoff.md) |
| P04 | AUC-001 P04 Semantic Equivalence QA Gate | [../gates/auc-001-p04-semantic-equivalence-qa-gate.md](/gates/auc-001-p04-semantic-equivalence-qa-gate.md) |
| P04 | AUC-001 P04 Exit Gate | [../gates/auc-001-p04-exit-gate.md](/gates/auc-001-p04-exit-gate.md) |
| Post-P04 | AUC-001 SPEC-016 MCP Multi-table Query Gap | [evaluations/auc-001/validations/auc-001-spec-016-mcp-multitable-query-gap.md](/docs/evaluations/auc-001/validations/auc-001-spec-016-mcp-multitable-query-gap.md) |
| Post-P04 | AUC-001 SPEC-016 Controlled Proof Namespace | `outputs/auc-001/spec-016-controlled-proof/2026-07-22/` |
| Post-P04 | AUC-001 P04 Acceptance Real Execution Package | `outputs/auc-001/p04-acceptance/2026-07-22/` |
| Post-P04 | AUC-001 P04 Acceptance Final Physical Gate | [../gates/auc-001-p04-acceptance-final-physical-gate.md](/gates/auc-001-p04-acceptance-final-physical-gate.md) |
| Post-P04 | AUC-001 P04 Acceptance Final Physical Revalidation Gate | [../gates/auc-001-p04-acceptance-final-physical-revalidation-gate.md](/gates/auc-001-p04-acceptance-final-physical-revalidation-gate.md) |
| Experimental | AUC-001-EXP-COMP-001 Entry Gate | [../gates/auc-001-exp-comp-001-entry-gate.md](/gates/auc-001-exp-comp-001-entry-gate.md) |
| Experimental | AUC-001-EXP-COMP-001 Task Plan | [../tasks/auc-001-exp-comp-001-comparison-governance-task-plan.md](/tasks/auc-001-exp-comp-001-comparison-governance-task-plan.md) |
| Experimental | AUC-001-EXP-COMP-001 Final Experimental Specification | [evaluations/auc-001/experiments/auc-001-exp-comp-001-final-experimental-specification.md](/docs/evaluations/auc-001/experiments/auc-001-exp-comp-001-final-experimental-specification.md) |
| Experimental | AUC-001-EXP-COMP-001 Architectural Memo | [decisions/auc-001/auc-001-exp-comp-001-architectural-memo.md](/docs/decisions/auc-001/auc-001-exp-comp-001-architectural-memo.md) |
| Experimental | AUC-001-EXP-COMP-001 Reviewer Review | [evaluations/auc-001/validations/auc-001-exp-comp-001-reviewer-review.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-reviewer-review.md) |
| Experimental | AUC-001-EXP-COMP-001 Five Change Resolution Record | [evaluations/auc-001/validations/auc-001-exp-comp-001-five-change-resolution-record.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-five-change-resolution-record.md) |
| Experimental | AUC-001-EXP-COMP-001 Implementation Handoff | [evaluations/auc-001/validations/auc-001-exp-comp-001-implementation-handoff.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-implementation-handoff.md) |
| Experimental | AUC-001-EXP-COMP-001 Final QA Validation | [evaluations/auc-001/validations/auc-001-exp-comp-001-final-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-final-qa-validation.md) |
| Experimental | AUC-001-EXP-COMP-001 Experimental Execution Report | [evaluations/auc-001/validations/auc-001-exp-comp-001-experimental-execution-report.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-experimental-execution-report.md) |
| Experimental | AUC-001-EXP-COMP-001 Exit Gate | [../gates/auc-001-exp-comp-001-exit-gate.md](/gates/auc-001-exp-comp-001-exit-gate.md) |
| Experimental | AUC-001-EXP-COMP-001 Iteration Closure Record | [evaluations/auc-001/validations/auc-001-exp-comp-001-iteration-closure-record.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-iteration-closure-record.md) |
| P03 | AUC-001 P03 Revalidation Handoff | [handoffs/auc-001-p03-revalidation-handoff.md](/docs/handoffs/auc-001-p03-revalidation-handoff.md) |
| P03 | AUC-001 P03 Experimental Closure Gate | [../gates/auc-001-p03-experimental-closure-gate.md](/gates/auc-001-p03-experimental-closure-gate.md) |
| P03 | AUC-001 P03 Future Evidence Gaps Record | [evaluations/auc-001/validations/auc-001-p03-future-evidence-gaps-record.md](/docs/evaluations/auc-001/validations/auc-001-p03-future-evidence-gaps-record.md) |
| P04 | AUC-001 P04 Task Plan | [../tasks/auc-001-p04-canonical-projection-consolidation-task-plan.md](/tasks/auc-001-p04-canonical-projection-consolidation-task-plan.md) |
| P04 | AUC-001 P04 Entry Gate | [../gates/auc-001-p04-entry-gate.md](/gates/auc-001-p04-entry-gate.md) |
| Post-closure | ARCH-004 Canonical Cost-Quality Model Decision | [decisions/auc-001/auc-001-canonical-cost-quality-model-architectural-decision.md](/docs/decisions/auc-001/auc-001-canonical-cost-quality-model-architectural-decision.md) |
| Post-closure | AUC-001-PCI-001 Entry Gate | [../gates/auc-001-pci-001-entry-gate.md](/gates/auc-001-pci-001-entry-gate.md) |
| Post-closure | AUC-001-PCI-001 Exit Gate | [../gates/auc-001-pci-001-exit-gate.md](/gates/auc-001-pci-001-exit-gate.md) |
| Post-closure | SPEC-013 Entry Gate | [../gates/spec-013-auc-001-structured-reconciliation-output-entry-gate.md](/gates/spec-013-auc-001-structured-reconciliation-output-entry-gate.md) |
| Post-closure | SPEC-013 Exit Gate | [../gates/spec-013-auc-001-structured-reconciliation-output-exit-gate.md](/gates/spec-013-auc-001-structured-reconciliation-output-exit-gate.md) |
| Post-closure | AUC-001 P0 Operational Closure Gate | [../gates/auc-001-p0-operational-closure-gate.md](/gates/auc-001-p0-operational-closure-gate.md) |
| Post-closure | AUC-001 P0 Operational Closure QA Validation | [evaluations/auc-001/validations/auc-001-p0-operational-closure-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-p0-operational-closure-qa-validation.md) |
| Post-closure | AUC-001-PCI-002 Planning Review | [evaluations/auc-001/validations/auc-001-pci-002-planning-review.md](/docs/evaluations/auc-001/validations/auc-001-pci-002-planning-review.md) |
| Post-closure | AUC-001-PCI-002 Implementation Report | [evaluations/auc-001/validations/auc-001-pci-002-implementation-report.md](/docs/evaluations/auc-001/validations/auc-001-pci-002-implementation-report.md) |
| Post-closure | AUC-001-PCI-002 QA Handoff | [handoffs/auc-001-pci-002-qa-handoff.md](/docs/handoffs/auc-001-pci-002-qa-handoff.md) |
| Post-closure | AUC-001-PCI-002 Local Implementation QA Validation | [evaluations/auc-001/validations/auc-001-pci-002-local-implementation-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-pci-002-local-implementation-qa-validation.md) |
| Post-closure | AUC-001-PCI-002 Real Execution Authorization Gate | [../gates/auc-001-pci-002-real-execution-authorization-gate.md](/gates/auc-001-pci-002-real-execution-authorization-gate.md) |
| Post-closure | AUC-001-PCI-002 Real Execution Report | [evaluations/auc-001/validations/auc-001-pci-002-real-execution-report.md](/docs/evaluations/auc-001/validations/auc-001-pci-002-real-execution-report.md) |
| Post-closure | AUC-001-PCI-002 Physical QA Handoff | [handoffs/auc-001-pci-002-physical-qa-handoff.md](/docs/handoffs/auc-001-pci-002-physical-qa-handoff.md) |
| Post-closure | AUC-001-PCI-002 Physical Runtime QA Validation | [evaluations/auc-001/validations/auc-001-pci-002-physical-runtime-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-pci-002-physical-runtime-qa-validation.md) |
| Post-closure | AUC-001-PCI-002 Exit Gate | [../gates/auc-001-pci-002-exit-gate.md](/gates/auc-001-pci-002-exit-gate.md) |
| Post-closure | AUC-001 P0 Final QA Validation | [evaluations/auc-001/validations/auc-001-p0-operational-closure-final-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-p0-operational-closure-final-qa-validation.md) |
| Post-closure | AUC-001-PCI-002 Output Namespace | `outputs/auc-001/pci-002/2026-06-30/` |
| Post-closure | SPEC-013 Task Traceability | [../tasks/spec-013-auc-001-structured-reconciliation-output-tasks.md](/tasks/spec-013-auc-001-structured-reconciliation-output-tasks.md) |
| Post-closure | SPEC-013 Runtime Output Persistence Corrective Tasks | [../tasks/spec-013-auc-001-runtime-output-persistence-corrective-tasks.md](/tasks/spec-013-auc-001-runtime-output-persistence-corrective-tasks.md) |
| Post-closure | AUC-001-PCI-002 Runtime Output Persistence Task Plan | [../tasks/auc-001-pci-002-runtime-output-persistence-task-plan.md](/tasks/auc-001-pci-002-runtime-output-persistence-task-plan.md) |
| Post-closure | AUC-001-PCI-002 Entry Gate | [../gates/auc-001-pci-002-entry-gate.md](/gates/auc-001-pci-002-entry-gate.md) |
| Post-closure | AUC-001-PCI-002 Entry Gate Handoff To QA | [evaluations/auc-001/validations/auc-001-pci-002-entry-gate-handoff-to-qa.md](/docs/evaluations/auc-001/validations/auc-001-pci-002-entry-gate-handoff-to-qa.md) |
| Post-closure | AUC-001-PCI-001 Output Namespace | `outputs/auc-001/pci-001/2026-06-30/` |
| Required | Producto analítico validado | [../outputs/auc-001/2026-06-30/analytical-report.md](/outputs/auc-001/2026-06-30/analytical-report.md) |
| Supporting | Executive Report Handoff | [handoffs/auc-001-executive-report.md](/docs/handoffs/auc-001-executive-report.md) |
| Historical | Corpus AUC-001 | [corpus/auc-001/](/docs/corpus/auc-001/) |

---

## 4. Decisiones vigentes

| Fecha | Decision | Impacto | Fuente |
|---|---|---|---|
| 2026-07-11 | Adoptar AIF Foundation como dependencia metodológica reutilizable | Permite reutilizar la base SDD sin convertir la Foundation en objeto funcional | [../README.md](/README.md); [../project_brief.md](/project_brief.md) |
| 2026-07-11 | Validar AUC-001 y la skill como primer ciclo analítico trazable | Define la primera capacidad analítica aprobada | [../analytical_use_cases/auc-001/README.md](/analytical_use_cases/auc-001/README.md) |
| 2026-07-11 | Autorizar entrada a Development mediante SPEC-008 | Sitúa el proyecto en Development | [../gates/spec-008-development-entry-phase-gate.md](/gates/spec-008-development-entry-phase-gate.md) |
| 2026-07-13 | Execution Scope Canonicalization | Canonicaliza el alcance antes de seleccionar proyección | [decisions/auc-001/auc-001-execution-scope-canonicalization-architectural-decision.md](/docs/decisions/auc-001/auc-001-execution-scope-canonicalization-architectural-decision.md) |
| 2026-07-13 | Presentation Projection Architecture | Define proyecciones hermanas analítica y ejecutiva | [decisions/auc-001/auc-001-presentation-projection-architectural-decision.md](/docs/decisions/auc-001/auc-001-presentation-projection-architectural-decision.md) |
| 2026-07-14 | Communication Context Representation Transformation | Transforma representación preservando equivalencia semántica | [decisions/auc-001/auc-001-communication-context-representation-transformation-architectural-decision.md](/docs/decisions/auc-001/auc-001-communication-context-representation-transformation-architectural-decision.md) |
| 2026-07-13 | Documentary Alignment Decision | Autoriza alineamiento documental posterior a T-040/T-041/T-042 | [decisions/auc-001/auc-001-documentary-alignment-decision.md](/docs/decisions/auc-001/auc-001-documentary-alignment-decision.md) |
| 2026-07-16 | Cerrar experimentalmente AUC-001 | Declara `READY FOR CLOSURE`; el ciclo original queda cerrado | [../gates/auc-001-experimental-closure-gate.md](/gates/auc-001-experimental-closure-gate.md) |
| 2026-07-18 | Definir evolucion post-cierre del modelo coste-calidad canonico | Crea `AUC-001-PCI-001` como iteracion separada; no reabre el ciclo cerrado ni promueve a Foundation; instancia Entry Gate y Exit Gate propios; fija `outputs/auc-001/pci-001/2026-06-30/` como namespace oficial de primera iteracion post-cierre | [../specs/spec-012-auc-001-canonical-cost-quality-model.md](/specs/spec-012-auc-001-canonical-cost-quality-model.md); [decisions/auc-001/auc-001-canonical-cost-quality-model-architectural-decision.md](/docs/decisions/auc-001/auc-001-canonical-cost-quality-model-architectural-decision.md); [../gates/auc-001-pci-001-entry-gate.md](/gates/auc-001-pci-001-entry-gate.md); [../gates/auc-001-pci-001-exit-gate.md](/gates/auc-001-pci-001-exit-gate.md) |
| 2026-07-19 | Formalizar exposicion estructurada de reconciliacion AUC-001 | SPEC-013 implementa y valida tecnicamente el contrato estructurado de reconciliacion para futuras ejecuciones AUC-001; Exit Gate `PASS WITH CONDITIONS`; no modifica outputs historicos y no promueve a Foundation | [../specs/spec-013-auc-001-structured-reconciliation-output.md](/specs/spec-013-auc-001-structured-reconciliation-output.md); [../gates/spec-013-auc-001-structured-reconciliation-output-entry-gate.md](/gates/spec-013-auc-001-structured-reconciliation-output-entry-gate.md); [../gates/spec-013-auc-001-structured-reconciliation-output-exit-gate.md](/gates/spec-013-auc-001-structured-reconciliation-output-exit-gate.md); [evaluations/auc-001/validations/spec-013-structured-reconciliation-output-qa-validation.md](/docs/evaluations/auc-001/validations/spec-013-structured-reconciliation-output-qa-validation.md); [../tasks/spec-013-auc-001-structured-reconciliation-output-tasks.md](/tasks/spec-013-auc-001-structured-reconciliation-output-tasks.md) |
| 2026-07-19 | Bloquear cierre operativo P0 de AUC-001 hasta persistencia fisica SPEC-013 | La ultima ejecucion real hasta 2026-06-30 aporta cifras trazables, pero el `runtime-output.json` fisico localizado no cumple SPEC-013 ni expone `is_consumable = true`; P01 no se inicia | [../gates/auc-001-p0-operational-closure-gate.md](/gates/auc-001-p0-operational-closure-gate.md); [evaluations/auc-001/validations/auc-001-p0-operational-closure-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-p0-operational-closure-qa-validation.md) |
| 2026-07-19 | Formalizar correccion minima de persistencia bajo SPEC-013 | Decision `CORRECTIVE TASKS UNDER SPEC-013`; no se abre nueva SPEC; se propone `AUC-001-PCI-002` y namespace `outputs/auc-001/pci-002/<execution-date>/` antes de reabrir P0 | [../tasks/spec-013-auc-001-runtime-output-persistence-corrective-tasks.md](/tasks/spec-013-auc-001-runtime-output-persistence-corrective-tasks.md) |
| 2026-07-19 | Evaluar AUC-001-PCI-002 Entry Gate | Decision `PASS WITH CONDITIONS`; se autoriza implementacion tecnica acotada y se condiciona la ejecucion real en `outputs/auc-001/pci-002/2026-06-30/` a tests locales y validacion BigQuery MCP; P0 sigue bloqueado hasta QA fisico del runtime | [../gates/auc-001-pci-002-entry-gate.md](/gates/auc-001-pci-002-entry-gate.md); [../tasks/auc-001-pci-002-runtime-output-persistence-task-plan.md](/tasks/auc-001-pci-002-runtime-output-persistence-task-plan.md); [evaluations/auc-001/validations/auc-001-pci-002-entry-gate-handoff-to-qa.md](/docs/evaluations/auc-001/validations/auc-001-pci-002-entry-gate-handoff-to-qa.md) |
| 2026-07-19 | Implementar localmente AUC-001-PCI-002 | Implementacion local completa; tests 14/14 PASS; no se ejecuta BigQuery MCP ni ejecucion real; no se escribe outputs/auc-001/pci-002/2026-06-30/; queda listo para QA local | [evaluations/auc-001/validations/auc-001-pci-002-implementation-report.md](/docs/evaluations/auc-001/validations/auc-001-pci-002-implementation-report.md); [handoffs/auc-001-pci-002-qa-handoff.md](/docs/handoffs/auc-001-pci-002-qa-handoff.md) |
| 2026-07-19 | Autorizar ejecucion real AUC-001-PCI-002 via BigQuery MCP | QA valida implementacion local, tests 14/14 PASS y Data Provider Validation por `discover_metadata` canonico; se autoriza ejecucion real en `outputs/auc-001/pci-002/2026-06-30/`; P0 sigue bloqueado hasta QA fisico del runtime | [evaluations/auc-001/validations/auc-001-pci-002-local-implementation-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-pci-002-local-implementation-qa-validation.md); [../gates/auc-001-pci-002-real-execution-authorization-gate.md](/gates/auc-001-pci-002-real-execution-authorization-gate.md) |
| 2026-07-19 | Ejecutar paquete real AUC-001-PCI-002 | Se materializa `outputs/auc-001/pci-002/2026-06-30/execution/runtime-output.json` via BigQuery MCP con `is_consumable = true` e invariantes PASS; queda listo para QA fisico y P0 sigue bloqueado hasta esa validacion | [evaluations/auc-001/validations/auc-001-pci-002-real-execution-report.md](/docs/evaluations/auc-001/validations/auc-001-pci-002-real-execution-report.md); [handoffs/auc-001-pci-002-physical-qa-handoff.md](/docs/handoffs/auc-001-pci-002-physical-qa-handoff.md); [../outputs/auc-001/pci-002/2026-06-30/execution/runtime-output.json](/outputs/auc-001/pci-002/2026-06-30/execution/runtime-output.json) |
| 2026-07-19 | Cerrar PCI-002 y P0 Operational Closure | QA valida fisicamente el runtime PCI-002 desde disco, emite Exit Gate `PASS` y reevalua P0 como `P0 PASS WITH RESIDUAL OBSERVATIONS - READY FOR P01`; P01 no se inicia en esta decision | [evaluations/auc-001/validations/auc-001-pci-002-physical-runtime-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-pci-002-physical-runtime-qa-validation.md); [../gates/auc-001-pci-002-exit-gate.md](/gates/auc-001-pci-002-exit-gate.md); [evaluations/auc-001/validations/auc-001-p0-operational-closure-final-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-p0-operational-closure-final-qa-validation.md); [../gates/auc-001-p0-operational-closure-gate.md](/gates/auc-001-p0-operational-closure-gate.md) |
| 2026-07-21 | Cerrar documentalmente AUC-001-P01 | Architect Agent define el boundary del Analytical Product Contract; Specification Agent crea y corrige SPEC-014; Reviewer Agent confirma `PASS`; QA Gate Agent emite el cierre documental con `PASS`. Estado canonico: `AUC-001-P01 DOCUMENTARY CLOSURE PASS - READY FOR CONTROLLED POST-P01 IMPLEMENTATION PLANNING`. La implementacion, validacion experimental, task plans y outputs pertenecen a fases posteriores separadas | [../specs/spec-014-auc-001-analytical-product-contract.md](/specs/spec-014-auc-001-analytical-product-contract.md); [decisions/auc-001/auc-001-p01-analytical-product-contract-architectural-analysis.md](/docs/decisions/auc-001/auc-001-p01-analytical-product-contract-architectural-analysis.md); [../gates/auc-001-p01-documentary-closure-gate.md](/gates/auc-001-p01-documentary-closure-gate.md) |
| 2026-07-21 | Autorizar entrada a implementacion AUC-001-P02 | Tasks Planner Agent traduce exclusivamente SPEC-014 en plan implementable; Reviewer Agent confirma que no hay ampliacion informal de alcance; QA Gate Agent emite Entry Gate `PASS WITH CONDITIONS`. Estado canonico: `AUC-001-P02 ENTRY GATE PASS WITH CONDITIONS - CONTROLLED IMPLEMENTATION AUTHORIZED`. No autoriza BigQuery, ejecucion analitica real, outputs, validacion experimental ni cierre P02 | [../tasks/auc-001-p02-analytical-product-contract-implementation-task-plan.md](/tasks/auc-001-p02-analytical-product-contract-implementation-task-plan.md); [../gates/auc-001-p02-entry-gate.md](/gates/auc-001-p02-entry-gate.md) |
| 2026-07-21 | Autorizar ejecucion real AUC-001-P02 via BigQuery MCP | QA Gate Agent revisa el estado vigente de P02, confirma validacion tecnica y funcional `PASS` y emite Real Execution Authorization Gate con `PASS WITH CONDITIONS - REAL EXECUTION AUTHORIZED VIA BIGQUERY MCP`. Estado canonico: `AUC-001-P02 REAL EXECUTION AUTHORIZED VIA BIGQUERY MCP WITH CONDITIONS`. Autoriza ejecucion real, adquisicion de evidencia nueva y persistencia en namespace protegido `outputs/auc-001/p02/<execution-date-or-cutoff>/`, sujeto a Runbook, Data Provider Validation MCP y QA fisico posterior; no ejecuta el analisis ni cierra P02 | [evaluations/auc-001/validations/auc-001-p02-technical-functional-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-p02-technical-functional-qa-validation.md); [../gates/auc-001-p02-real-execution-authorization-gate.md](/gates/auc-001-p02-real-execution-authorization-gate.md) |
| 2026-07-21 | Cerrar AUC-001-P02 | QA Gate Agent revalida fisicamente el paquete `outputs/auc-001/p02/2026-07-17/` con `PASS WITH DECLARED LIMITATIONS`, cierra los blockers FND-001 y FND-002, verifica matriz SPEC-014 23/23, trazabilidad MCP 16/16, manifest, fingerprints, nucleo comun, informes y tests; emite Closure Gate de P02. Estado canonico: `AUC-001-P02 CLOSURE PASS WITH DECLARED LIMITATIONS - ANALYTICAL PRODUCT CONTRACT REAL EXECUTION CLOSED` | [evaluations/auc-001/validations/auc-001-p02-physical-product-qa-revalidation.md](/docs/evaluations/auc-001/validations/auc-001-p02-physical-product-qa-revalidation.md); [../gates/auc-001-p02-closure-gate.md](/gates/auc-001-p02-closure-gate.md); [../outputs/auc-001/p02/2026-07-17/execution/manifest.json](/outputs/auc-001/p02/2026-07-17/execution/manifest.json) |
| 2026-07-21 | Revisar alineacion documental final P01 y transversal | Documentation Agent revisa P01, gates P01/P02, README raiz, README AUC-001 y context refs; confirma enlaces canonicos, estado vigente P02 cerrado y preservacion del boundary historico de P01. Decision: `DOCUMENTATION ALIGNED - PASS` | [evaluations/auc-001/validations/auc-001-p01-transversal-documentation-final-review.md](/docs/evaluations/auc-001/validations/auc-001-p01-transversal-documentation-final-review.md) |
| 2026-07-22 | Cerrar experimentalmente AUC-001-P03 | QA Gate Agent emite cierre experimental `PASS` para la revision de representacion P03 sobre el producto canonico P02. Estado canonico: `AUC-001-P03 EXPERIMENTAL CLOSURE PASS - REPRESENTATION REVISION CLOSED`. No adquiere nueva evidencia, no modifica SPEC-014, no modifica outputs historicos ni reabre P02. Los gaps revenue/CRM, causalidad creativa, metadata creativa adicional y temporalidad coste-calidad quedan registrados como dependientes de evidencia futura | [../gates/auc-001-p03-experimental-closure-gate.md](/gates/auc-001-p03-experimental-closure-gate.md); [handoffs/auc-001-p03-revalidation-handoff.md](/docs/handoffs/auc-001-p03-revalidation-handoff.md); [evaluations/auc-001/validations/auc-001-p03-future-evidence-gaps-record.md](/docs/evaluations/auc-001/validations/auc-001-p03-future-evidence-gaps-record.md); [../outputs/auc-001/p03/2026-07-22/execution/manifest.json](/outputs/auc-001/p03/2026-07-22/execution/manifest.json) |
| 2026-07-22 | Cerrar AUC-001-P04 Canonical Projection Consolidation | QA Gate Agent emite Exit Gate `PASS` tras validar que `SPEC-015` queda implementada mediante `Canonical Projection Source`, proyecciones hermanas y bloqueos verificables contra nuevo conocimiento en Presentation. Estado canonico: `AUC-001-P04 EXIT GATE PASS - CANONICAL PROJECTION CONSOLIDATION CLOSED`. No adquiere nueva evidencia, no genera outputs analiticos, no modifica P02/P03 y preserva los gaps dependientes de evidencia futura | [../specs/spec-015-auc-001-canonical-projection-consolidation.md](/specs/spec-015-auc-001-canonical-projection-consolidation.md); [../gates/auc-001-p04-entry-gate.md](/gates/auc-001-p04-entry-gate.md); [evaluations/auc-001/validations/auc-001-p04-implementation-handoff.md](/docs/evaluations/auc-001/validations/auc-001-p04-implementation-handoff.md); [../gates/auc-001-p04-semantic-equivalence-qa-gate.md](/gates/auc-001-p04-semantic-equivalence-qa-gate.md); [../gates/auc-001-p04-exit-gate.md](/gates/auc-001-p04-exit-gate.md) |
| 2026-07-22 | Cerrar SPEC-016 Operational Acceptance Package Contract | Specification Agent define el contrato operativo de paquete aceptable para AUC-001; Reviewer Agent valida boundary y verificabilidad con `PASS`; QA Gate Agent valida fisicamente el paquete controlado y emite cierre formal `PASS`. Estado canonico: `SPEC-016 OPERATIONAL ACCEPTANCE PACKAGE CONTRACT CLOSED - READY FOR INTEGRAL ARTIFACT CONSOLIDATION INPUT`. No modifica SPEC-014, SPEC-015, outputs historicos ni servidor BigQuery MCP. El gap MCP multi-tabla queda registrado por separado | [../specs/spec-016-auc-001-operational-acceptance-package-contract.md](/specs/spec-016-auc-001-operational-acceptance-package-contract.md); [evaluations/auc-001/validations/auc-001-spec-016-mcp-multitable-query-gap.md](/docs/evaluations/auc-001/validations/auc-001-spec-016-mcp-multitable-query-gap.md); [../outputs/auc-001/spec-016-controlled-proof/2026-07-22/execution/manifest.json](/outputs/auc-001/spec-016-controlled-proof/2026-07-22/execution/manifest.json) |
| 2026-07-22 | Autorizar AUC-001-IC-001 Integral Product Consolidation | QA Gate Agent emite Entry Gate `PASS WITH CONDITIONS` para cambios estructurales, documentales y operativos. No autoriza BigQuery, nueva evidencia, outputs nuevos ni reinterpretacion de P02/P03/P04/SPEC-016. en ese momento `outputs/auc-001/p04-acceptance/2026-07-22/` conservaba su estado real antes del gate fisico final propio | [../tasks/auc-001-ic-001-integral-product-consolidation-task-plan.md](/tasks/auc-001-ic-001-integral-product-consolidation-task-plan.md); [../gates/auc-001-ic-001-entry-gate.md](/gates/auc-001-ic-001-entry-gate.md) |
| 2026-07-22 | Cerrar AUC-001-IC-001 Integral Product Consolidation | QA Gate Agent ejecuta suites SPEC-014, SPEC-015 y SPEC-016, valida rutas canonicas, comprueba conservacion de outputs e higiene de namespace y emite Closure Gate `PASS`. Estado canonico: `AUC-001-IC-001 CLOSURE PASS - INTEGRAL PRODUCT CONSOLIDATION CLOSED`. No abre nueva Specification, no ejecuta BigQuery, no adquiere evidencia, no genera outputs y no acepta el paquete `p04-acceptance` sin gate fisico final propio | [../gates/auc-001-ic-001-closure-gate.md](/gates/auc-001-ic-001-closure-gate.md); [evaluations/auc-001/validations/auc-001-ic-001-implementation-handoff.md](/docs/evaluations/auc-001/validations/auc-001-ic-001-implementation-handoff.md) |
| 2026-07-22 | Aceptar fisicamente el paquete real post-P04 AUC-001 | QA Gate Agent revalida el mismo paquete `outputs/auc-001/p04-acceptance/2026-07-22/` tras la remediacion fisica y emite `FINAL ACCEPTED`. El manifest del paquete permanece correctamente en `READY_FOR_REVALIDATION`; la aceptacion final la concede el gate QA, no el manifest. No modifica outputs historicos ni autoriza nueva ejecucion BigQuery | [../gates/auc-001-p04-acceptance-final-physical-revalidation-gate.md](/gates/auc-001-p04-acceptance-final-physical-revalidation-gate.md); [../gates/auc-001-p04-acceptance-final-physical-gate.md](/gates/auc-001-p04-acceptance-final-physical-gate.md); [../outputs/auc-001/p04-acceptance/2026-07-22/execution/manifest.json](/outputs/auc-001/p04-acceptance/2026-07-22/execution/manifest.json) |
| 2026-07-24 | Preparar AUC-001-EXP-COMP-001 para reevaluacion Entry Gate | Architect Agent clasifica la solucion como `EXPERIMENT FIRST`; Specification Agent mantiene el contrato experimental local en AUC-001; Reviewer Agent aprueba con cinco cambios aplicados. No modifica Strategic Context, no abre SPEC Foundation, no implementa codigo y no adquiere evidencia nueva | [decisions/auc-001/auc-001-exp-comp-001-architectural-memo.md](/docs/decisions/auc-001/auc-001-exp-comp-001-architectural-memo.md); [evaluations/auc-001/experiments/auc-001-exp-comp-001-final-experimental-specification.md](/docs/evaluations/auc-001/experiments/auc-001-exp-comp-001-final-experimental-specification.md); [evaluations/auc-001/validations/auc-001-exp-comp-001-reviewer-review.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-reviewer-review.md); [evaluations/auc-001/validations/auc-001-exp-comp-001-five-change-resolution-record.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-five-change-resolution-record.md) |
| 2026-07-24 | Autorizar Entry Gate AUC-001-EXP-COMP-001 | QA Gate Agent reevalua los artefactos fisicos persistidos y emite `PASS WITH CONDITIONS`. Autoriza Task Planning e implementacion controlada local; no autoriza evidencia nueva, BigQuery, outputs reales, cambios de Strategic Context, cambios de SPEC-014/SPEC-015/SPEC-016 ni promocion a Foundation | [../gates/auc-001-exp-comp-001-entry-gate.md](/gates/auc-001-exp-comp-001-entry-gate.md); [evaluations/auc-001/experiments/auc-001-exp-comp-001-final-experimental-specification.md](/docs/evaluations/auc-001/experiments/auc-001-exp-comp-001-final-experimental-specification.md) |
| 2026-07-24 | Planificar implementacion AUC-001-EXP-COMP-001 | Tasks Planner Agent traduce la especificacion experimental y el Entry Gate `PASS WITH CONDITIONS` en un plan implementable local. No ejecuta codigo, no adquiere evidencia, no usa BigQuery, no genera outputs reales y no modifica Strategic Context ni SPEC-014/SPEC-015/SPEC-016 | [../tasks/auc-001-exp-comp-001-comparison-governance-task-plan.md](/tasks/auc-001-exp-comp-001-comparison-governance-task-plan.md); [../gates/auc-001-exp-comp-001-entry-gate.md](/gates/auc-001-exp-comp-001-entry-gate.md) |
| 2026-07-25 | Implementar y validar AUC-001-EXP-COMP-001 | Implementation Agent implementa el contrato experimental local de gobernanza de comparaciones; Reviewer Agent y QA Gate Agent validan las correcciones; la ejecucion experimental local obtiene `PASS`. No adquiere evidencia nueva, no ejecuta BigQuery, no genera outputs reales y no promueve la solucion a Foundation | [evaluations/auc-001/validations/auc-001-exp-comp-001-implementation-handoff.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-implementation-handoff.md); [evaluations/auc-001/validations/auc-001-exp-comp-001-final-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-final-qa-validation.md); [evaluations/auc-001/validations/auc-001-exp-comp-001-experimental-execution-report.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-experimental-execution-report.md) |
| 2026-07-25 | Cerrar AUC-001-EXP-COMP-001 | QA Gate Agent emite Exit Gate `PASS` y Documentation Agent registra el cierre documental. Estado canonico: `AUC-001-EXP-COMP-001 CLOSED - EXPERIMENTAL COMPARISON GOVERNANCE PASS`. No autoriza ejecucion real, nueva evidencia, cambios de Strategic Context, SPEC Foundation ni promocion a AIF Foundation | [../gates/auc-001-exp-comp-001-exit-gate.md](/gates/auc-001-exp-comp-001-exit-gate.md); [evaluations/auc-001/validations/auc-001-exp-comp-001-iteration-closure-record.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-iteration-closure-record.md) |

---


## 4.1 Modelo operativo canónico AUC-001

AUC-001 se opera como producto consolidado mediante SPEC-014, SPEC-015 y SPEC-016 tras el cierre IC-001, sin abrir nueva Specification para la consolidacion integral.

| Capa | Responsabilidad vigente |
|---|---|
| Skill / Runbook / Checklist | Resolver la solicitud breve, ejecutar el orden operativo, bloquear si falla MCP/preflight/grano/cobertura y verificar completitud. |
| Data / MCP | Adquirir evidencia solo mediante BigQuery MCP cuando haya nueva ejecución; registrar preflight y todas las llamadas, incluidas rechazadas y descartadas. |
| Evidence | Construir hechos trazables, coverage states, `UNKNOWN`, `partial`, `not_available`, limitaciones y reconciliación local controlada. |
| Knowledge | Derivar interpretación únicamente desde Evidence estabilizada. |
| Recommendations | Derivar acciones únicamente desde Knowledge estabilizado, con criterio de éxito visible. |
| Common Product Core | Compartir contenido obligatorio definido por SPEC-014. |
| Canonical Projection Source | Fuente intermedia única de ambas proyecciones conforme a SPEC-015. |
| Presentation | Materializar analytical/executive como hermanas, sin nuevo conocimiento ni derivación entre proyecciones. |
| Execution Package | Persistir manifest, fingerprints, physical traceability, registros MCP, resultados de tests e higiene de namespace conforme a SPEC-016. |

El paquete real de aceptacion post-P04 `outputs/auc-001/p04-acceptance/2026-07-22/` queda `FINAL ACCEPTED` por gate QA fisico final independiente. Su manifest interno conserva `READY_FOR_REVALIDATION` como estado correcto del paquete producido por Implementation antes de aceptacion QA.

Los gaps MCP multi-tabla, revenue/CRM, causalidad creativa, metadata adicional y temporalidad limitada por proveedor quedan fuera del flujo operativo principal hasta nueva evidencia o decisión separada.

## 5. Evaluaciones principales

| Clasificación | Recurso | Fuente |
|---|---|---|
| Supporting | BigQuery MCP Integration Validation | [evaluations/auc-001/validations/auc-001-bigquery-mcp-integration-validation.md](/docs/evaluations/auc-001/validations/auc-001-bigquery-mcp-integration-validation.md) |
| Supporting | End-to-End Traceability Test Report | [evaluations/auc-001/validations/auc-001-end-to-end-traceability-test-report.md](/docs/evaluations/auc-001/validations/auc-001-end-to-end-traceability-test-report.md) |
| Supporting | Development Entry Readiness Evidence | [evaluations/auc-001/validations/auc-001-development-entry-readiness-evidence.md](/docs/evaluations/auc-001/validations/auc-001-development-entry-readiness-evidence.md) |
| Supporting | Knowledge Depth Recovery Validation | [evaluations/auc-001/validations/auc-001-knowledge-depth-recovery-validation.md](/docs/evaluations/auc-001/validations/auc-001-knowledge-depth-recovery-validation.md) |
| Supporting | Analytical Narrative Validation | [evaluations/auc-001/validations/auc-001-analytical-narrative-validation.md](/docs/evaluations/auc-001/validations/auc-001-analytical-narrative-validation.md) |
| Post-closure | SPEC-013 Structured Reconciliation Output QA Validation | [evaluations/auc-001/validations/spec-013-structured-reconciliation-output-qa-validation.md](/docs/evaluations/auc-001/validations/spec-013-structured-reconciliation-output-qa-validation.md) |
| Post-closure | AUC-001 P0 Operational Closure QA Validation | [evaluations/auc-001/validations/auc-001-p0-operational-closure-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-p0-operational-closure-qa-validation.md) |
| Post-closure | AUC-001-PCI-002 Local Implementation QA Validation | [evaluations/auc-001/validations/auc-001-pci-002-local-implementation-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-pci-002-local-implementation-qa-validation.md) |
| Post-closure | AUC-001-PCI-002 Physical Runtime QA Validation | [evaluations/auc-001/validations/auc-001-pci-002-physical-runtime-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-pci-002-physical-runtime-qa-validation.md) |
| P02 | AUC-001 P02 Technical And Functional QA Validation | [evaluations/auc-001/validations/auc-001-p02-technical-functional-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-p02-technical-functional-qa-validation.md) |
| P02 | AUC-001 P02 Physical Product QA Revalidation | [evaluations/auc-001/validations/auc-001-p02-physical-product-qa-revalidation.md](/docs/evaluations/auc-001/validations/auc-001-p02-physical-product-qa-revalidation.md) |
| P02 | AUC-001 P02 Closure Gate | [../gates/auc-001-p02-closure-gate.md](/gates/auc-001-p02-closure-gate.md) |
| P03 | AUC-001 P03 Experimental Closure Gate | [../gates/auc-001-p03-experimental-closure-gate.md](/gates/auc-001-p03-experimental-closure-gate.md) |
| P03 | AUC-001 P03 Revalidation Handoff | [handoffs/auc-001-p03-revalidation-handoff.md](/docs/handoffs/auc-001-p03-revalidation-handoff.md) |
| P03 | AUC-001 P03 Future Evidence Gaps Record | [evaluations/auc-001/validations/auc-001-p03-future-evidence-gaps-record.md](/docs/evaluations/auc-001/validations/auc-001-p03-future-evidence-gaps-record.md) |
| P03 | AUC-001 P03 Output Namespace | `outputs/auc-001/p03/2026-07-22/` |
| P04 | AUC-001 P04 Task Plan | [../tasks/auc-001-p04-canonical-projection-consolidation-task-plan.md](/tasks/auc-001-p04-canonical-projection-consolidation-task-plan.md) |
| P04 | AUC-001 P04 Entry Gate | [../gates/auc-001-p04-entry-gate.md](/gates/auc-001-p04-entry-gate.md) |
| P04 | AUC-001 P04 Implementation Handoff | [evaluations/auc-001/validations/auc-001-p04-implementation-handoff.md](/docs/evaluations/auc-001/validations/auc-001-p04-implementation-handoff.md) |
| P04 | AUC-001 P04 Semantic Equivalence QA Gate | [../gates/auc-001-p04-semantic-equivalence-qa-gate.md](/gates/auc-001-p04-semantic-equivalence-qa-gate.md) |
| P04 | AUC-001 P04 Exit Gate | [../gates/auc-001-p04-exit-gate.md](/gates/auc-001-p04-exit-gate.md) |
| Post-P04 | AUC-001 SPEC-016 MCP Multi-table Query Gap | [evaluations/auc-001/validations/auc-001-spec-016-mcp-multitable-query-gap.md](/docs/evaluations/auc-001/validations/auc-001-spec-016-mcp-multitable-query-gap.md) |
| Post-P04 | AUC-001 SPEC-016 Transversal Documentation Alignment Review | [evaluations/auc-001/validations/auc-001-spec-016-transversal-documentation-alignment-review.md](/docs/evaluations/auc-001/validations/auc-001-spec-016-transversal-documentation-alignment-review.md) |
| Post-P04 | AUC-001 SPEC-016 Controlled Proof Namespace | `outputs/auc-001/spec-016-controlled-proof/2026-07-22/` |
| Post-P04 | AUC-001 P04 Acceptance Real Execution Package | `outputs/auc-001/p04-acceptance/2026-07-22/` |
| Post-P04 | AUC-001 P04 Acceptance Final Physical Gate | [../gates/auc-001-p04-acceptance-final-physical-gate.md](/gates/auc-001-p04-acceptance-final-physical-gate.md) |
| Post-P04 | AUC-001 P04 Acceptance Final Physical Revalidation Gate | [../gates/auc-001-p04-acceptance-final-physical-revalidation-gate.md](/gates/auc-001-p04-acceptance-final-physical-revalidation-gate.md) |
| Experimental | AUC-001-EXP-COMP-001 Entry Gate | [../gates/auc-001-exp-comp-001-entry-gate.md](/gates/auc-001-exp-comp-001-entry-gate.md) |
| Experimental | AUC-001-EXP-COMP-001 Task Plan | [../tasks/auc-001-exp-comp-001-comparison-governance-task-plan.md](/tasks/auc-001-exp-comp-001-comparison-governance-task-plan.md) |
| Experimental | AUC-001-EXP-COMP-001 Final Experimental Specification | [evaluations/auc-001/experiments/auc-001-exp-comp-001-final-experimental-specification.md](/docs/evaluations/auc-001/experiments/auc-001-exp-comp-001-final-experimental-specification.md) |
| Experimental | AUC-001-EXP-COMP-001 Architectural Memo | [decisions/auc-001/auc-001-exp-comp-001-architectural-memo.md](/docs/decisions/auc-001/auc-001-exp-comp-001-architectural-memo.md) |
| Experimental | AUC-001-EXP-COMP-001 Reviewer Review | [evaluations/auc-001/validations/auc-001-exp-comp-001-reviewer-review.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-reviewer-review.md) |
| Experimental | AUC-001-EXP-COMP-001 Five Change Resolution Record | [evaluations/auc-001/validations/auc-001-exp-comp-001-five-change-resolution-record.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-five-change-resolution-record.md) |
| Experimental | AUC-001-EXP-COMP-001 Implementation Handoff | [evaluations/auc-001/validations/auc-001-exp-comp-001-implementation-handoff.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-implementation-handoff.md) |
| Experimental | AUC-001-EXP-COMP-001 Final QA Validation | [evaluations/auc-001/validations/auc-001-exp-comp-001-final-qa-validation.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-final-qa-validation.md) |
| Experimental | AUC-001-EXP-COMP-001 Experimental Execution Report | [evaluations/auc-001/validations/auc-001-exp-comp-001-experimental-execution-report.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-experimental-execution-report.md) |
| Experimental | AUC-001-EXP-COMP-001 Exit Gate | [../gates/auc-001-exp-comp-001-exit-gate.md](/gates/auc-001-exp-comp-001-exit-gate.md) |
| Experimental | AUC-001-EXP-COMP-001 Iteration Closure Record | [evaluations/auc-001/validations/auc-001-exp-comp-001-iteration-closure-record.md](/docs/evaluations/auc-001/validations/auc-001-exp-comp-001-iteration-closure-record.md) |
| IC-001 | AUC-001 IC-001 Entry Gate | [../gates/auc-001-ic-001-entry-gate.md](/gates/auc-001-ic-001-entry-gate.md) |
| IC-001 | AUC-001 IC-001 Implementation Handoff | [evaluations/auc-001/validations/auc-001-ic-001-implementation-handoff.md](/docs/evaluations/auc-001/validations/auc-001-ic-001-implementation-handoff.md) |
| IC-001 | AUC-001 IC-001 Closure Gate | [../gates/auc-001-ic-001-closure-gate.md](/gates/auc-001-ic-001-closure-gate.md) |
| Historical | Closure Reconciliation Review | [evaluations/auc-001/historical/auc-001-closure-reconciliation-review.md](/docs/evaluations/auc-001/historical/auc-001-closure-reconciliation-review.md) |
| Historical | SDD Readiness Assessment | [evaluations/transversal/historical/sdd_readiness_assessment.md](/docs/evaluations/transversal/historical/sdd_readiness_assessment.md) |

El inventario completo de documentos reestructurados vive en [repository-restructuring/auc-001-document-inventory.md](repository-restructuring/auc-001-document-inventory.md).

---

## 6. Fuentes tecnicas relacionadas

```yaml
google_cloud:
  proyectos:
    - project_id: datamart-vca-494114
      descripcion: Proyecto BigQuery validado para AUC-001
  bigquery:
    datasets:
      - intermediate
      - marts

apis:
  - nombre: BigQuery MCP Server
    uso_en_proyecto: Data Provider autorizado para adquisición de evidencia AUC-001 cuando se ejecuta el workflow completo
    discover_metadata_contract: docs/contracts/bigquery-mcp-discover-metadata.contract.md
```

---

## 7. Reglas de carga para agentes

1. Leer `README.md`, `project_brief.md` y este archivo para contexto general.
2. Para AUC-001, entrar por [../analytical_use_cases/auc-001/README.md](/analytical_use_cases/auc-001/README.md).
3. No usar documentos en `historical/` como contexto obligatorio salvo que la tarea sea auditoría, comparación o recuperación histórica.
4. No tratar corpus histórico como evidencia actual.
5. Respetar la precedencia documental definida por las instrucciones SDD y los contratos.

---

## 8. Trazabilidad

```yaml
ultima_actualizacion: 2026-07-25
actualizado_por: Documentation Agent
motivo: Cierre documental AUC-001-EXP-COMP-001 tras Exit Gate PASS; referencias alineadas sin reabrir P02/P03/P04/SPEC-016 ni outputs historicos
version_contexto: vca-ia-contexto-oficial-development-authorized-auc-001-exp-comp-001-closed
```