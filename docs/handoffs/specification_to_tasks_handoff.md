# Handoff de Specification a Tasks Planning

## Propósito

Este documento define el relevo documental desde la fase de Specification hacia la fase de Tasks Planning dentro del estado SDD vigente de la Foundation.

Su objetivo es convertir specifications aprobadas y decisiones ya publicadas en un punto de partida trazable para descomponer trabajo sin introducir alcance nuevo.

Este documento no crea tareas por si mismo.

Este documento no redefine specs, gates ni precedencias documentales.

---

## Fase actual

Specification / Structure.

En esta fase ya existen specifications fundacionales, contexto oficial y reglas de gobierno suficientes para planificar trabajo derivado.

---

## Fase destino

Tasks Planning.

La salida esperada es un plan de tareas trazable, ordenado por dependencias y limitado al alcance ya aprobado.

---

## Artefactos fuente

- [project_brief.md](../../project_brief.md)
- [README.md](../../README.md)
- [docs/context_refs.md](../../docs/context_refs.md)
- [specs/spec-001-analytical-lifecycle.md](../../specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](../../specs/spec-002-component-boundaries.md)
- [specs/spec-003-extensibility-model.md](../../specs/spec-003-extensibility-model.md)
- [specs/spec-004-transversal-contracts.md](../../specs/spec-004-transversal-contracts.md)
- [specs/spec-005-readiness-gates.md](../../specs/spec-005-readiness-gates.md)
- [specs/spec-006-documentary-evaluations.md](../../specs/spec-006-documentary-evaluations.md)
- [specs/spec-007-extension-compatibility-reusability.md](../../specs/spec-007-extension-compatibility-reusability.md)
- [.github/instructions/sdd.instructions.md](../../.github/instructions/sdd.instructions.md)

---

## Alcance del relevo

El Task Planner debe descomponer trabajo ya aprobado, no proponer nuevas decisiones metodologicas.

El relevo incluye:

- traducir specifications en tareas concretas y trazables;
- ordenar dependencias logicas entre artefactos;
- distinguir tareas de documentacion, gobernanza, validacion y revision;
- identificar bloqueos o dependencias documentales antes de cualquier cambio posterior.

---

## Restricciones

- no introducir Development;
- no ampliar el alcance funcional de la Foundation;
- no redefinir jerarquias documentales;
- no convertir decisiones pendientes en trabajo ejecutable;
- no crear tareas sin respaldo documental.

---

## Resultado esperado

Un plan de tareas debe ser utilizable cuando:

- cada tarea referencia una spec, decision o artefacto de contexto;
- las dependencias principales estan explicitadas;
- las tareas respetan el estado Specification / Structure;
- no existen tareas ambiguas ni fuera de alcance;
- el plan puede ser revisado por Reviewer o QA Gate antes de avanzar.

---

## Siguiente paso recomendado

Elaborar el plan inicial de tareas a partir de las specifications ya publicadas y registrar cualquier hueco documental como bloqueo, no como supuesto.