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

- [project_brief.md](../project_brief.md)
- [README.md](../README.md)
- [docs/context_refs.md](context_refs.md)
- [analytical_use_cases/meta_lead_quality_analysis.md](../analytical_use_cases/meta_lead_quality_analysis.md)
- [.github/skills/meta-lead-quality-analysis/SKILL.md](../.github/skills/meta-lead-quality-analysis/SKILL.md)
- [specs/spec-001-analytical-lifecycle.md](../specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](../specs/spec-002-component-boundaries.md)
- [specs/spec-003-extensibility-model.md](../specs/spec-003-extensibility-model.md)
- [specs/spec-004-transversal-contracts.md](../specs/spec-004-transversal-contracts.md)
- [specs/spec-005-readiness-gates.md](../specs/spec-005-readiness-gates.md)
- [specs/spec-006-documentary-evaluations.md](../specs/spec-006-documentary-evaluations.md)
- [specs/spec-007-extension-compatibility-reusability.md](../specs/spec-007-extension-compatibility-reusability.md)

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
| T-032 | Implementar la evaluacion documental de contracts transversales de AUC-001 | Validation / Governance | specs/spec-004-transversal-contracts.md, specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, analytical_use_cases/meta_lead_quality_analysis.md | T-006, T-007, T-008, T-009, T-010, T-011, T-012, T-013, T-014 | El flujo produce una evaluation documental del conjunto de contracts con hallazgos, gaps, riesgos y recomendaciones trazables | Not started |
| T-033 | Implementar la evaluacion documental de contexto y adquisicion de AUC-001 | Validation / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, docs/context_refs.md, analytical_use_cases/meta_lead_quality_analysis.md | T-015, T-016, T-017, T-018 | El flujo produce una evaluation documental del arranque, el Context Definition y la adquisicion de evidencia | Not started |
| T-034 | Implementar la evaluacion documental de preparacion y evidencia de AUC-001 | Validation / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, analytical_use_cases/meta_lead_quality_analysis.md | T-019, T-020, T-021, T-022, T-023 | El flujo produce una evaluation documental del Analytical Model y del Evidence Set con hallazgos, gaps, riesgos y recomendaciones trazables | Not started |
| T-035 | Implementar la evaluacion documental de razonamiento y recomendaciones de AUC-001 | Validation / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-004-transversal-contracts.md, specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, analytical_use_cases/meta_lead_quality_analysis.md | T-024, T-025, T-026, T-027, T-028, T-029 | El flujo produce una evaluation documental del Knowledge Set y del Recommendation Set con trazabilidad completa | Not started |
| T-036 | Implementar la evaluacion documental de presentacion e informe de AUC-001 | Validation / Governance | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, analytical_use_cases/meta_lead_quality_analysis.md | T-030, T-031 | El flujo produce una evaluation documental del Presentation Contract y del Output Artifact final | Not started |
| T-037 | Implementar la evidencia del readiness gate de entrada a Development | Validation / Governance | specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, specs/spec-008-development-entry-phase-gate.md, docs/context_refs.md, analytical_use_cases/meta_lead_quality_analysis.md | T-032, T-033, T-034, T-035, T-036 | El flujo consolida la evidencia necesaria para emitir Pass, Pass with observations o Blocked sobre el arranque del desarrollo | Not started |
| T-038 | Implementar las pruebas de trazabilidad end-to-end del caso AUC-001 | Validation | specs/spec-001-analytical-lifecycle.md, specs/spec-002-component-boundaries.md, specs/spec-003-extensibility-model.md, specs/spec-004-transversal-contracts.md, specs/spec-005-readiness-gates.md, specs/spec-006-documentary-evaluations.md, analytical_use_cases/meta_lead_quality_analysis.md, .github/skills/meta-lead-quality-analysis/SKILL.md | T-031, T-032, T-033, T-034, T-035, T-036, T-037 | Las pruebas verifican handoffs, contracts, separacion entre capas y correspondencia entre evidencia y salida | Not started |

---

## Notas de uso

Este backlog debe actualizarse solo cuando cambien las specifications, las decisiones publicadas o el handoff de entrada a Tasks Planning del proyecto derivado.

Si aparece una nueva necesidad documental no cubierta por las tareas existentes, debe registrarse como revision de Specification y no como ampliacion informal del backlog.
