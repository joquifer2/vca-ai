# Tasks

## Propósito

Este documento actua como backlog auxiliar de gobernanza para el proyecto derivado.

Estado de transicion del proyecto derivado: PENDING adaptacion.

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
- Development permanece fuera de alcance mientras la fase vigente siga en Specification / Structure.

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

## Notas de uso

Este backlog debe actualizarse solo cuando cambien las specifications, las decisiones publicadas o el handoff de entrada a Tasks Planning del proyecto derivado.

Si aparece una nueva necesidad documental no cubierta por las tareas existentes, debe registrarse como revision de Specification y no como ampliacion informal del backlog.