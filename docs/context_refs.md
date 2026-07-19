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

---

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
ultima_actualizacion: 2026-07-19
actualizado_por: QA Gate Agent
motivo: Validacion fisica QA AUC-001-PCI-002, Exit Gate PASS y P0 ready for P01
version_contexto: vca-ia-contexto-oficial-development-authorized-auc-001-p0-pass-ready-for-p01
```