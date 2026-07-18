# Tasks

## Propósito

Este documento actua como backlog auxiliar de gobernanza para el proyecto derivado.

Estado de transicion del proyecto derivado: Development Authorized.

Su funcion es traducir specifications aprobadas, decisiones publicadas y handoffs documentales en una lista de trabajo trazable.

No sustituye a las specifications.

No redefine decisiones metodologicas.

No introduce trabajo fuera del alcance aprobado.

---

## Fuentes de contexto

- [project_brief.md](/project_brief.md)
- [README.md](/README.md)
- [docs/context_refs.md](/docs/context_refs.md)
- [analytical_use_cases/meta_lead_quality_analysis.md](/analytical_use_cases/meta_lead_quality_analysis.md)
- [.github/skills/meta-lead-quality-analysis/SKILL.md](/.github/skills/meta-lead-quality-analysis/SKILL.md)
- [specs/spec-001-analytical-lifecycle.md](/specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](/specs/spec-002-component-boundaries.md)
- [specs/spec-003-extensibility-model.md](/specs/spec-003-extensibility-model.md)
- [specs/spec-004-transversal-contracts.md](/specs/spec-004-transversal-contracts.md)
- [specs/spec-005-readiness-gates.md](/specs/spec-005-readiness-gates.md)
- [specs/spec-006-documentary-evaluations.md](/specs/spec-006-documentary-evaluations.md)
- [specs/spec-007-extension-compatibility-reusability.md](/specs/spec-007-extension-compatibility-reusability.md)

---

## Reglas de planificacion

- Cada tarea debe estar respaldada por una spec, decision o artefacto de contexto.
- Las tareas deben representar trabajo significativo, no actividad diaria.
- Las dependencias deben quedar explicitadas antes de avanzar.
- Si una tarea requiere nueva definicion, debe volver a Specification.
- Development ya esta autorizado; las tareas registradas deben mantenerse dentro del alcance aprobado y conservar trazabilidad con specs, AUC y skills.

---

## Backlog inicial del proyecto derivado

| ID | Tarea | Tipo | Fuentes | Dependencias | Criterio de finalizacion | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| T-001 | Delimitar el primer caso analitico | Documentation | project_brief, context_refs, AUC-001 | Ninguna | El alcance del caso AUC-001 queda acotado y alineado con el brief y las referencias oficiales | Completed |
| T-002 | Preparar el inventario de evidencia | Planning / Documentation | AUC-001, skill meta-lead-quality-analysis, context_refs | T-001 | Quedan identificadas las fuentes de contexto, los Data Providers y el esquema minimo de evidencia para el analisis | Completed |
| T-003 | Estructurar el flujo de analisis | Documentation / Planning | AUC-001, skill meta-lead-quality-analysis, project_brief | T-002 | El flujo de contexto, evidencia, preparacion, analisis, razonamiento y recomendaciones queda definido para el primer caso | Completed |
| T-004 | Definir criterios de validacion | Review / Validation | AUC-001, skill meta-lead-quality-analysis, context_refs | T-003 | Los criterios de validacion y trazabilidad del caso quedan listos para su ejecucion y revision | Completed |
| T-005 | Registrar la evidencia de validacion | Governance / Documentation | AUC-001, docs/context_refs, project_brief | T-004 | La validacion queda documentada y enlazada con las fuentes oficiales del proyecto | Completed |

---

## Backlog de implementacion inicial

Este backlog traduce las specifications aprobadas, AUC-001 y la skill aprobada en capacidades implementables para Development. Las tareas se ordenan desde la base contractual y de contexto hasta la salida ejecutiva y las validaciones de trazabilidad.

| ID | Tarea | Tipo | Fuentes | Dependencias | Criterio de finalizacion | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| T-006 | Implementar el Context Contract | Development / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | Ninguna | Existe un Context Contract reutilizable con objetivo, restricciones, fuentes y UNKNOWN declarados | Completed |
| T-007 | Implementar el Data Contract | Development / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-006 | Existe un Data Contract reusable para el Data Provider principal, con productor, consumidor, estructura y limitaciones trazables | Completed |
| T-008 | Implementar el Discovery Contract | Development / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-007 | Existe un Discovery Contract que formaliza entidades, dimensiones, metricas y limitaciones observadas antes de la preparacion | Completed |
| T-009 | Implementar el Analytical Contract | Development / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-008 | Existe un Analytical Contract que formaliza el modelo preparado y sus transformaciones relevantes para analisis | Completed |
| T-010 | Implementar el Evidence Contract | Development / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-009 | Existe un Evidence Contract con hallazgos observables separados de interpretacion y trazados a su modelo analitico | Completed |
| T-011 | Implementar el Knowledge Contract | Development / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-010 | Existe un Knowledge Contract con insights, hipotesis, prioridades e incertidumbres declaradas | Completed |
| T-012 | Implementar el Recommendation Contract | Development / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-011 | Existe un Recommendation Contract con acciones sugeridas, justificacion, prioridad y trazabilidad explicita | Completed |
| T-013 | Implementar el Presentation Contract | Development / Governance | specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md | T-012 | Existe un Presentation Contract que delimita el contenido aprobado para la capa de presentacion sin nueva interpretacion | Completed |
| T-014 | Implementar el Extension Contract | Development / Governance | specs/spec-003-extensibility-model.md, specs/spec-004-transversal-contracts.md, specs/spec-007-extension-compatibility-reusability.md | Ninguna | Existe un Extension Contract con reglas de entrada, salida, compatibilidad y reuso para extensiones del proyecto | Completed |
| T-015 | Implementar la resolucion del contexto oficial para AUC-001 | Development | docs/context_refs.md, project_brief.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md, specs/spec-001-analytical-lifecycle.md | T-006 | El flujo identifica las fuentes oficiales, el objetivo, el periodo y el alcance operativo del caso | Completed |
| T-016 | Implementar la validacion del Analysis Request y del Context Definition de AUC-001 | Development | docs/context_refs.md, project_brief.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md, specs/spec-001-analytical-lifecycle.md, docs/handoffs/auc-001-analysis-request.md | T-015 | La solicitud analitica concreta y el Context Definition quedan trazados y validados antes de iniciar la adquisicion de datos | Completed |
| T-017 | Implementar el Data Contract del caso AUC-001 | Development / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-016 | Existe un Data Contract reusable para el Data Provider principal, con productor, consumidor, estructura y limitaciones trazables | Completed |
| T-018 | Implementar la adquisicion de evidencia desde BigQuery con verificacion de exposicion por CLI y MCP pendiente | Development | analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md, specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, docs/context_refs.md | T-017 | El Data Provider expone evidencia reproducible con origen, periodo, metricas y limitaciones explicitadas; la validacion directa del MCP Server permanece pendiente | Completed |
| T-019 | Implementar el Discovery Contract del caso AUC-001 | Development / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-018 | Existe un Discovery Contract que formaliza entidades, dimensiones, metricas y limitaciones observadas antes de la preparacion | Completed |
| T-020 | Implementar la preparacion analitica del caso AUC-001 | Development | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-019 | La capa analitica transforma los datos adquiridos en un Analytical Model coherente para el caso | Completed |
| T-021 | Implementar el Analytical Contract del caso AUC-001 | Development / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-020 | Existe un Analytical Contract que formaliza el modelo preparado y sus transformaciones relevantes para analisis | Completed |
| T-022 | Implementar el Evidence Set de AUC-001 | Development | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-021 | Existe un Evidence Set con hallazgos observables separados de interpretacion y trazados a su modelo analitico | Completed |
| T-023 | Implementar el Evidence Contract del caso AUC-001 | Development / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-022 | Existe un Evidence Contract que formaliza los hallazgos observables y su trazabilidad al modelo analitico | Completed |
| T-024 | Implementar la capa de razonamiento del caso AUC-001 | Development | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-023 | El flujo convierte la evidencia en insights, hipotesis y conclusiones respaldadas por evidencia identificable | Completed |
| T-025 | Implementar el Knowledge Contract del caso AUC-001 | Development / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-024 | Existe un Knowledge Contract con insights, hipotesis, prioridades e incertidumbres declaradas | Completed |
| T-026 | Implementar el Knowledge Set de AUC-001 | Development | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-025 | Existe un Knowledge Set trazable con hipotesis priorizadas e incertidumbres declaradas | Completed |
| T-027 | Implementar la capa de recomendaciones del caso AUC-001 | Development | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-026 | El flujo convierte el conocimiento en acciones sugeridas, justificadas y priorizadas | Completed |
| T-028 | Implementar el Recommendation Contract del caso AUC-001 | Development / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-027 | Existe un Recommendation Contract con acciones sugeridas, justificacion, prioridad y trazabilidad explicita | Completed |
| T-029 | Implementar el Recommendation Set de AUC-001 | Development | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-028 | Existe un Recommendation Set con acciones priorizadas, justificacion y trazabilidad a la evidencia y al conocimiento | Completed |
| T-030 | Implementar el Presentation Contract del caso AUC-001 | Development / Governance | specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, analytical_use_cases/meta_lead_quality_analysis.md | T-029 | Existe un Presentation Contract que delimita el contenido aprobado para la capa de presentacion sin nueva interpretacion | Completed |
| T-031 | Implementar el constructor del informe ejecutivo trazable | Development | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-030 | El Output Artifact presenta contexto, evidencia, razonamiento, recomendaciones y limitaciones sin reintroducir nueva interpretacion | Completed |
| T-032 | Implementar la evaluacion documental de contracts transversales de AUC-001 | Validation / Governance | specs/spec-004-transversal-contracts.md, specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, analytical_use_cases/meta_lead_quality_analysis.md | T-006, T-007, T-008, T-009, T-010, T-011, T-012, T-013, T-014 | El flujo produce una evaluation documental del conjunto de contracts con hallazgos, gaps, riesgos y recomendaciones trazables | Completed |
| T-033 | Implementar la evaluacion documental de contexto y adquisicion de AUC-001 | Validation / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, docs/context_refs.md, analytical_use_cases/meta_lead_quality_analysis.md | T-015, T-016, T-017, T-018 | El flujo produce una evaluation documental del arranque, el Context Definition y la adquisicion de evidencia | Completed |
| T-034 | Implementar la evaluacion documental de preparacion y evidencia de AUC-001 | Validation / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, analytical_use_cases/meta_lead_quality_analysis.md | T-019, T-020, T-021, T-022, T-023 | El flujo produce una evaluation documental del Analytical Model y del Evidence Set con hallazgos, gaps, riesgos y recomendaciones trazables | Completed |
| T-035 | Implementar la evaluacion documental de razonamiento y recomendaciones de AUC-001 | Validation / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, analytical_use_cases/meta_lead_quality_analysis.md | T-024, T-025, T-026, T-027, T-028, T-029 | El flujo produce una evaluation documental del Knowledge Set y del Recommendation Set con trazabilidad completa | Completed |
| T-036 | Implementar la evaluacion documental de presentacion y salida ejecutiva de AUC-001 | Validation / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, analytical_use_cases/meta_lead_quality_analysis.md, docs/handoffs/auc-001-presentation-contract.md, docs/handoffs/auc-001-executive-report.md | T-030, T-031 | El flujo produce una evaluation documental del Presentation Contract y del Executive Output Artifact final VCA-AUC-001-OUT-001, con observaciones, hallazgos, gaps, riesgos, recomendaciones y trazabilidad explicita | Completed |
| T-037 | Implementar la evidencia del readiness gate de entrada a Development | Validation / Governance | specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, specs/spec-008-development-entry-phase-gate.md, docs/context_refs.md, analytical_use_cases/meta_lead_quality_analysis.md | T-032, T-033, T-034, T-035, T-036 | El flujo consolida la evidencia necesaria para emitir Pass, Pass with observations o Blocked sobre el arranque del desarrollo | Completed |
| T-038 | Implementar las pruebas de trazabilidad end-to-end del caso AUC-001 | Validation | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-003-extensibility-model.md, specs/spec-004-transversal-contracts.md, specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-031, T-032, T-033, T-034, T-035, T-036, T-037 | Las pruebas verifican handoffs, contracts, separacion entre capas y correspondencia entre evidencia y salida | Completed |

---

## Backlog de validacion de cierre

Este backlog recoge validaciones documentadas para el cierre del caso y su trazabilidad, sin confundirlas con la adquisicion ya completada por CLI.

| ID | Tarea | Tipo | Fuentes | Dependencias | Criterio de finalizacion | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| T-039 | Validar la integracion MCP de BigQuery para AUC-001 | Validation / Governance | docs/context_refs.md, docs/handoffs/auc-001-data-contract.md, docs/handoffs/auc-001-evidence-acquisition.md, docs/evaluations/auc-001/validations/auc-001-context-acquisition-evaluation.md, docs/evaluations/auc-001/historical/auc-001-closure-reconciliation-review.md, docs/evaluations/auc-001/validations/auc-001-bigquery-mcp-integration-validation.md | T-018, T-033, T-037 | Existe una validacion documental y tecnica del acceso directo al BigQuery MCP Server, con evidencia separada de la adquisicion CLI y trazabilidad explicita de origen | Completed |

---

## Backlog de alineamiento del repositorio

Este backlog organiza tareas metodologicas de analisis de impacto, alineamiento arquitectonico y decision documental para introducir la capacidad minima aprobada por VCA-AUC-001-ARCH-002 y SPEC-010.

Las tareas de este bloque no presuponen modificaciones documentales. Cada una debe poder cerrarse con uno de estos resultados:

- no se requieren cambios en los artefactos evaluados;
- se requieren cambios documentales justificados en uno o varios artefactos.

La modificacion documental, cuando proceda, debe ser consecuencia de la tarea y no un supuesto previo.

### T-040 — Base Contracts Alignment Assessment

| Campo | Valor |
|---|---|
| Tipo | Validation / Review |
| Objetivo | Evaluar el impacto de la nueva capacidad sobre [docs/contracts/context.contract.md](/docs/contracts/context.contract.md) y [docs/contracts/presentation.contract.md](/docs/contracts/presentation.contract.md) para determinar si requieren especializacion explicita o pueden permanecer intactos. |
| Dependencias | SPEC-001; SPEC-002; SPEC-004; VCA-AUC-001-ARCH-001; VCA-AUC-001-ARCH-002; SPEC-010 |
| Criterios de aceptacion | La tarea concluye con una decision trazable sobre cada contract evaluado; la decision puede ser que no se requieren cambios o que existen cambios justificados; la conclusion debe estar respaldada por evidencia documental observada. |
| Definition of Done | Existe una evaluacion clara de impacto por contract; se identifican brechas reales o se documenta explicitamente que no hay necesidad de cambio; cualquier propuesta de modificacion queda condicionada a la decision de la tarea. |
| Resultado | Evaluacion completada en [docs/evaluations/auc-001/historical/auc-001-base-contracts-alignment-assessment.md](/docs/evaluations/auc-001/historical/auc-001-base-contracts-alignment-assessment.md). |
| Resultado posible | No se requieren cambios en los contracts evaluados, o se requieren cambios documentales justificados. |
| Estado | Completed |

### T-041 — AUC-001 Presentation Alignment Assessment

| Campo | Valor |
|---|---|
| Tipo | Validation / Review |
| Objetivo | Evaluar el impacto de la nueva capacidad sobre [docs/handoffs/auc-001-presentation-contract.md](/docs/handoffs/auc-001-presentation-contract.md) y [docs/handoffs/auc-001-executive-report.md](/docs/handoffs/auc-001-executive-report.md) para verificar si siguen alineados con la capacidad minima aprobada. |
| Dependencias | T-040; SPEC-010; VCA-AUC-001-ARCH-002; docs/decisions/auc-001/auc-001-presentation-projection-architectural-decision.md |
| Criterios de aceptacion | La tarea identifica si los handoffs AUC-001 conservan la terminologia y el alcance vigentes; la conclusion puede ser no cambios o cambios justificados; la evaluacion debe preservar la distincion entre contenido aprobado y contenido pendiente. |
| Definition of Done | El estado de alineamiento de ambos handoffs queda documentado con trazabilidad suficiente; si no hay brechas, se registra explicitamente que no se requieren cambios; si las hay, se identifican con precision y sin aplicar ediciones aun. |
| Resultado | Evaluacion completada en [docs/evaluations/auc-001/historical/auc-001-presentation-alignment-assessment.md](/docs/evaluations/auc-001/historical/auc-001-presentation-alignment-assessment.md). |
| Resultado posible | No se requieren cambios en los handoffs evaluados, o se requieren cambios documentales justificados. |
| Estado | Completed |

### T-042 — Context And Traceability Alignment Assessment

| Campo | Valor |
|---|---|
| Tipo | Validation / Governance |
| Objetivo | Evaluar el impacto de la nueva capacidad sobre [docs/context_refs.md](/docs/context_refs.md) y la trazabilidad oficial del repositorio para asegurar que la terminologia vigente y las decisiones relacionadas reflejan solo la capacidad aprobada. |
| Dependencias | T-041; SPEC-010; docs/decisions/auc-001/auc-001-presentation-projection-architectural-decision.md |
| Criterios de aceptacion | La tarea verifica si el indice de contexto necesita ajustes o puede permanecer intacto; la conclusion debe dejar claro si la referencia a la decision y a SPEC-010 es suficiente o requiere refinamiento. |
| Definition of Done | Existe una conclusion explicita sobre el estado del indice de contexto y de las decisiones relacionadas; la tarea puede cerrar con ausencia de cambios o con cambios justificados, pero nunca por defecto. |
| Resultado | Evaluacion completada en [docs/evaluations/auc-001/historical/auc-001-context-traceability-alignment-assessment.md](/docs/evaluations/auc-001/historical/auc-001-context-traceability-alignment-assessment.md). |
| Resultado posible | No se requieren cambios en context_refs.md, o se requieren cambios documentales justificados. |
| Estado | Completed |

### T-043 — Documentary Alignment Decision

| Campo | Valor |
|---|---|
| Tipo | Review / Governance |
| Objetivo | Consolidar los resultados de las evaluaciones previas y decidir, de forma trazable, que artefactos permanecen intactos y cuales requieren cambios documentales. |
| Dependencias | T-040; T-041; T-042 |
| Criterios de aceptacion | La decision debe clasificar cada artefacto revisado como sin cambios o con cambios justificados; no debe asumir modificaciones no demostradas; debe dejar evidencia suficiente para sustentar el siguiente paso. |
| Definition of Done | Existe una decision documental de alineamiento con alcance cerrado; la salida de la tarea es una decision, no una implementacion; cualquier cambio posterior queda condicionado a esta decision. |
| Resultado | Decision documentada en [docs/decisions/auc-001/auc-001-documentary-alignment-decision.md](/docs/decisions/auc-001/auc-001-documentary-alignment-decision.md). |
| Resultado posible | Ningun cambio adicional, o lista justificada de artefactos a modificar. |
| Estado | Completed |

### T-044 — Align Base Contracts

| Campo | Valor |
|---|---|
| Tipo | Documentation / Governance |
| Objetivo | Evaluar el impacto de la nueva capacidad sobre [docs/contracts/context.contract.md](/docs/contracts/context.contract.md) y [docs/contracts/presentation.contract.md](/docs/contracts/presentation.contract.md) para determinar si requieren especializacion explicita o pueden permanecer intactos. |
| Dependencias | T-043; SPEC-001; SPEC-002; SPEC-004; VCA-AUC-001-ARCH-001; VCA-AUC-001-ARCH-002; SPEC-010 |
| Criterios de aceptacion | La tarea concluye con una decision trazable sobre cada contract evaluado; la decision puede ser que no se requieren cambios o que existen cambios justificados; la conclusion debe estar respaldada por evidencia documental observada. |
| Definition of Done | Existe una evaluacion clara de impacto por contract; se identifican brechas reales o se documenta explicitamente que no hay necesidad de cambio; cualquier propuesta de modificacion queda condicionada a la decision de la tarea. |
| Resultado | Alineamiento documentado en [docs/evaluations/auc-001/validations/auc-001-base-contracts-alignment-record.md](/docs/evaluations/auc-001/validations/auc-001-base-contracts-alignment-record.md). |
| Resultado posible | No se requieren cambios en los contracts evaluados, o se requieren cambios documentales justificados. |
| Estado | Completed |

### T-045 — Align AUC-001 Artifacts

| Campo | Valor |
|---|---|
| Tipo | Validation / Governance |
| Objetivo | Evaluar el impacto de la nueva capacidad sobre [docs/handoffs/auc-001-presentation-contract.md](/docs/handoffs/auc-001-presentation-contract.md) y [docs/handoffs/auc-001-executive-report.md](/docs/handoffs/auc-001-executive-report.md) para verificar si siguen alineados con la capacidad minima aprobada. |
| Dependencias | T-044; SPEC-010; VCA-AUC-001-ARCH-002; docs/decisions/auc-001/auc-001-presentation-projection-architectural-decision.md |
| Criterios de aceptacion | La tarea identifica si los handoffs AUC-001 conservan la terminologia y el alcance vigentes; la conclusion puede ser no cambios o cambios justificados; la evaluacion debe preservar la distincion entre contenido aprobado y contenido pendiente. |
| Definition of Done | El estado de alineamiento de ambos handoffs queda documentado con trazabilidad suficiente; si no hay brechas, se registra explicitamente que no se requieren cambios; si las hay, se identifican con precision y sin aplicar ediciones aun. |
| Resultado | Alineamiento documentado en [docs/evaluations/auc-001/validations/auc-001-presentation-artifacts-alignment-record.md](/docs/evaluations/auc-001/validations/auc-001-presentation-artifacts-alignment-record.md). |
| Resultado posible | No se requieren cambios en los handoffs evaluados, o se requieren cambios documentales justificados. |
| Estado | Completed |

### T-046 — Align Context References

| Campo | Valor |
|---|---|
| Tipo | Validation / Governance |
| Objetivo | Evaluar el impacto de la nueva capacidad sobre [docs/context_refs.md](/docs/context_refs.md) y la trazabilidad oficial del repositorio para asegurar que la terminologia vigente y las decisiones relacionadas reflejan solo la capacidad aprobada. |
| Dependencias | T-045; SPEC-010; docs/decisions/auc-001/auc-001-presentation-projection-architectural-decision.md |
| Criterios de aceptacion | La tarea verifica si el indice de contexto necesita ajustes o puede permanecer intacto; la conclusion debe dejar claro si la referencia a la decision y a SPEC-010 es suficiente o requiere refinamiento. |
| Definition of Done | Existe una conclusion explicita sobre el estado del indice de contexto y de las decisiones relacionadas; la tarea puede cerrar con ausencia de cambios o con cambios justificados, pero nunca por defecto. |
| Resultado | Alineamiento documentado en [docs/evaluations/auc-001/validations/auc-001-context-references-alignment-record.md](/docs/evaluations/auc-001/validations/auc-001-context-references-alignment-record.md). |
| Resultado posible | No se requieren cambios en context_refs.md, o se requieren cambios documentales justificados. |
| Estado | Completed |

### T-047 — Presentation Projection Readiness Evaluation

| Campo | Valor |
|---|---|
| Tipo | Validation / Governance |
| Objetivo | Verificar que el repositorio ha quedado coherente tras la incorporacion de la capacidad, confirmando consistencia documental, consistencia metodologica y consistencia entre artefactos. |
| Dependencias | T-044; T-045; T-046; SPEC-001; SPEC-002; SPEC-004; SPEC-010; VCA-AUC-001-ARCH-001; VCA-AUC-001-ARCH-002 |
| Criterios de aceptacion | La evaluacion debe confirmar coherencia o señalar brechas residuales; debe comprobar la ausencia de terminologia descartada, la seleccion de proyeccion desde Execution Context y la compatibilidad con las specs fundacionales. |
| Definition of Done | Existe una evaluation documental final de readiness que puede emitir Pass, Pass with observations, Fail o Blocked segun la evidencia; la tarea valida la coherencia del repositorio tras la incorporacion del cambio y no reabre la arquitectura. |
| Resultado | Evaluacion completada en [docs/evaluations/auc-001/validations/auc-001-presentation-projection-readiness-evaluation.md](/docs/evaluations/auc-001/validations/auc-001-presentation-projection-readiness-evaluation.md). |
| Resultado posible | El repositorio queda coherente tras la incorporacion de la capacidad, o se identifican observaciones o cambios residuales justificados. |
| Estado | Completed |

---

# Methodological Observation

Durante la planificación de SPEC-011 ha surgido una posible evolución metodológica de AIF Foundation.

La observación es la siguiente:

La traducción de una Specification aprobada a un backlog implementable parece requerir una fase intermedia de planificación estructurada.

Actualmente esta fase ha aparecido representada mediante T-048, T-049 y T-050.

Su comportamiento es diferente al de un backlog tradicional de implementación:

- consume una Specification y una Architectural Decision ya aprobadas;
- produce un backlog implementable y verificable;
- no implementa la capacidad;
- prepara la implementación.

---

## Importante

No queremos iniciar todavía un nuevo ciclo SDD.

No queremos una Architectural Decision.

No queremos una Specification.

No queremos Tasks nuevas.

No queremos proponer cambios en AIF Foundation.

---

## Trabajo solicitado

Documenta esta situación como una **Methodological Observation** o equivalente.

La documentación debe contener únicamente:

### 1. Observación

Describe objetivamente la fase detectada y en qué consiste.

### 2. Evidencia disponible

Resume la evidencia obtenida durante SPEC-011.

### 3. Hipótesis

Explica por qué esta fase podría constituir una responsabilidad metodológica reusable.

Presenta esta conclusión explícitamente como una hipótesis, no como un hecho validado.

### 4. Evidencia pendiente

Define qué evidencia experimental será necesaria para confirmar o rechazar esta hipótesis.

En particular, indica qué deberá observarse durante la implementación y validación experimental de SPEC-011 para decidir si esta fase merece convertirse en una nueva capacidad metodológica de AIF Foundation.

### 5. Estado

Clasifica explícitamente esta observación como:

Candidate Methodological Capability

o una denominación equivalente que deje claro que:

- ha sido descubierta;
- ha sido analizada;
- todavía no ha sido validada experimentalmente.

---

## Restricciones

No abrir todavía un nuevo ciclo SDD.

No crear una nueva Architectural Decision.

No crear una nueva Specification.

No modificar la metodología actual.

No alterar el backlog existente.

Queremos únicamente preservar el descubrimiento y definir qué evidencia futura permitirá decidir si esta observación debe evolucionar o no hacia una capacidad reusable del framework.

---

## Notas de uso

Este backlog debe actualizarse solo cuando cambien las specifications, las decisiones publicadas o el handoff de entrada a Tasks Planning del proyecto derivado.

Si aparece una nueva necesidad documental no cubierta por las tareas existentes, debe registrarse como revision de Specification y no como ampliacion informal del backlog.



