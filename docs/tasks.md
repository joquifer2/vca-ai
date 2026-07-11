# Tasks

## Propósito

Este documento actua como backlog auxiliar de gobernanza para la Foundation.

Su funcion es traducir specifications aprobadas, decisiones publicadas y handoffs documentales en una lista de trabajo trazable.

No sustituye a las specifications.

No redefine decisiones metodologicas.

No introduce trabajo fuera del alcance aprobado.

---

## Fuentes de contexto

- [project_brief.md](../project_brief.md)
- [README.md](../README.md)
- [docs/context_refs.md](context_refs.md)
- [docs/handoffs/specification_to_tasks_handoff.md](handoffs/specification_to_tasks_handoff.md)
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

## Backlog inicial

| ID | Tarea | Tipo | Fuentes | Dependencias | Criterio de finalizacion | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| T-001 | Consolidar la trazabilidad canonica entre Project Brief, README, context refs y el mapa de specs | Governance / Documentation | project_brief, README, context_refs, sdd.instructions | Ninguna | Las referencias canonicas quedan alineadas y sin rutas duplicadas | Completed |
| T-002 | Revisar la coherencia entre lifecycle, component boundaries y transversal contracts | Review / Validation | spec-001, spec-002, spec-004 | T-001 | La secuencia entre fases, limites y contracts queda consistente y trazable | Completed |
| T-003 | Definir el uso documental de readiness gates y documentary evaluations como mecanismo de avance | Governance / Planning | spec-005, spec-006, QA gate artefacts | T-002 | Existen criterios reutilizables para evaluar avance sin introducir automatizacion | Completed |
| T-004 | Mantener el modelo de extensibilidad y reutilizacion alineado con el dossier de compatibilidad | Documentation / Review | spec-003, spec-007, extension dossier | T-002 | La extensibilidad y la compatibilidad documental quedan descritas sin contradicciones | Completed |
| T-005 | Descomponer las specifications fundacionales en tareas trazables para proyectos derivados futuros | Planning | handoff, specs 001-007 | T-001, T-002, T-003, T-004 | El plan de tareas puede ser revisado por Reviewer o QA Gate sin huecos de alcance | Completed |

---

## Orden recomendado de ejecucion

1. D-001
2. D-002
3. D-003
4. D-004
5. D-005
6. D-006
7. D-007

---

## Estado actual de ejecucion

- T-001 completada: la trazabilidad canonica ya queda publicada en README, context refs, handoff y backlog.
- T-002 completada: la secuencia entre lifecycle, boundaries y transversal contracts queda consistente y trazable.
- T-003 completada: el uso documental de readiness gates y documentary evaluations ya queda formalizado en las specs 005 y 006.
- T-004 completada: el modelo de extensibilidad y el dossier de compatibilidad quedan alineados con SPEC-003 y SPEC-007.
- T-005 completada: el backlog inicial ya queda descompuesto en un plan trazable por specification para proyectos derivados.

---

## Desglose fundacional para proyectos derivados

Este despiece sirve como base reutilizable para planificar trabajo en proyectos derivados sin volver a definir el marco metodologico.

| ID | Spec base | Tipo | Objetivo | Dependencias | Resultado esperado | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| D-001 | SPEC-001 | Planning / Documentation | Instanciar el lifecycle analitico comun en el proyecto derivado con artefactos de contexto, discovery, preparacion, analisis, razonamiento, recomendaciones y salida | project_brief, context_refs, spec-001 | El proyecto derivado puede ejecutar el ciclo 0-6 con outputs trazables | Planned |
| D-002 | SPEC-002 | Governance / Review | Definir limites de componentes y handoffs entre Data Provider, Analytical Layer, Reasoning Layer, Presentation Layer y Framework | D-001 | Cada interaccion entre capas ocurre mediante artefactos o contracts explicitos | Planned |
| D-003 | SPEC-003 | Planning / Documentation | Seleccionar y documentar Skills, Routines, Templates y Contracts como extensiones compatibles | D-001, D-002 | El proyecto derivado dispone de criterios de extensibilidad sin alterar el core | Planned |
| D-004 | SPEC-004 | Planning / Validation | Instanciar contracts transversales minimos para datos, evidencia, conocimiento, recomendacion y presentacion | D-002, D-003 | Los handoffs entre componentes quedan desacoplados y trazables | Planned |
| D-005 | SPEC-005 | Governance / Validation | Definir gates de readiness para fases e hitos relevantes del proyecto derivado | D-001, D-004 | El avance entre fases puede evaluarse con criterios documentales y bloqueos explicitos | Planned |
| D-006 | SPEC-006 | Documentation / Validation | Definir evaluaciones documentales para artefactos, gates y contextos del proyecto derivado | D-005 | Las decisiones de avance pueden apoyarse en evaluaciones trazables y comparables | Planned |
| D-007 | SPEC-007 | Documentation / Review | Documentar compatibilidad y reutilizacion de extensiones concretas mediante dossier | D-003, D-004, D-006 | Cada extension relevante puede evaluarse sin ambiguedad sobre compatibilidad y reuso | Planned |

---

## Secuencia recomendada para derivacion

1. D-001
2. D-002
3. D-003
4. D-004
5. D-005
6. D-006
7. D-007

---

## Notas de uso

Este backlog debe actualizarse solo cuando cambien las specifications, las decisiones publicadas o el handoff de entrada a Tasks Planning.

Si aparece una nueva necesidad documental no cubierta por las tareas existentes, debe registrarse como revision de Specification y no como ampliacion informal del backlog.