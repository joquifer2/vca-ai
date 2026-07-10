# Specification

## Metadata

### Spec ID

SPEC-005

### Title

Readiness Gates

### Status

Draft

### Owner

Foundation maintainers

### Last Updated

2026-07-10

---

## 1. Purpose

Definir el marco fundacional de readiness gates que la Foundation utilizara para evaluar si una capacidad o un conjunto de artefactos puede avanzar de una fase SDD a la siguiente.

---

## 2. Background

El roadmap fundacional prioriza artefactos para readiness gates despues de los contracts transversales.

La definicion del lifecycle, de los limites entre componentes, del modelo de extensibilidad y del marco contractual crea la necesidad de puntos de control verificables que determinen si existe evidencia suficiente para avanzar sin introducir implementacion prematura.

El QA Gate Agent ya define como debe evaluarse un gate. Esta specification formaliza que tipos de gates debe reconocer la Foundation, que informacion minima deben declarar y que criterios comunes deben preservar.

---

## 3. Objective

Esta capacidad debe conseguir que la Foundation disponga de un modelo comun para describir, revisar y aplicar gates de readiness documentales.

El resultado debe permitir validar avances entre fases y entre hitos documentales mediante criterios verificables, evidencias identificables, decisiones normalizadas y bloqueos explicitados.

---

## 4. Scope

### Included

- definicion de categorias fundacionales de readiness gates;
- definicion de metadata minima obligatoria para cualquier gate;
- definicion de criterios generales de evaluacion, bloqueo y decision;
- definicion de la relacion entre gates, evidencias, artefactos y fases SDD.

### Excluded

- automatizacion ejecutable de gates;
- implementacion tecnica de pipelines de validacion;
- reglas especificas de un proyecto derivado o de un cliente concreto;
- aprobacion humana final como acto automatizable.

---

## 5. Actors

| Actor | Description |
| --- | --- |
| QA Gate Agent | Evalua si un gate puede considerarse superado o no |
| Reviewer | Revisa coherencia, contradicciones y calidad documental asociadas al gate |
| Specification Agent | Produce artefactos cuya suficiencia puede ser evaluada por un gate |
| Documentation Agent | Mantiene artefactos, indices y evidencias necesarios para el gate |
| Foundation Maintainers | Toman la decision humana final cuando aplica |
| Derived Project Team | Reutiliza el marco de gates en proyectos derivados |

---

## 6. Inputs

| Input | Description |
| --- | --- |
| Phase Context | Fase actual y fase destino que el gate pretende validar |
| Required Artifacts | Artefactos obligatorios que deben existir para el gate |
| Evidence Set | Evidencias documentales observables que respaldan la evaluacion |
| Dependency Context | Dependencias, riesgos y decisiones previas relevantes |
| Gate Criteria | Criterios de cumplimiento, bloqueo y decision aplicables |

---

## 7. Outputs

| Output | Description |
| --- | --- |
| Gate Categories | Tipos fundacionales de gates admitidos |
| Gate Metadata Rules | Campos minimos obligatorios para describir un gate |
| Decision Model | Decisiones normalizadas que puede emitir un gate |
| Evaluation Rules | Reglas comunes para validar cumplimiento, bloqueo y evidencia |

---

## 7.1 Gate Categories

La Foundation debe reconocer como minimo las siguientes categorias de readiness gates:

| Category | Purpose |
| --- | --- |
| Phase Gate | Validar el avance entre fases SDD |
| Artifact Gate | Validar la suficiencia de un artefacto o conjunto de artefactos |
| Boundary Gate | Validar que se preservan limites y responsabilidades entre componentes |
| Contract Gate | Validar que los contracts requeridos existen y son utilizables |
| Readiness Gate | Validar que un hito documental o metodologico puede considerarse listo para el siguiente paso |
| Evaluation Gate | Validar que existe evidencia suficiente para emitir una conclusion o recomendacion de avance |

Readiness Gate es la categoria paraguas. Evaluation Gate es una especializacion de Readiness Gate orientada a verificar suficiencia de evidencia cuando la decision depende principalmente de una evaluacion documental.

---

## 7.2 Minimum Gate Metadata

Todo readiness gate debe declarar, como minimo, lo siguiente:

| Field | Required Content |
| --- | --- |
| Gate ID | Identificador unico y estable |
| Gate Name | Nombre claro y reutilizable |
| Gate Category | Categoria fundacional a la que pertenece |
| Gate Scope | Alcance principal del gate: Phase, Artifact, Contract, Boundary o Evaluation |
| Phase Current | Fase actual evaluada |
| Phase Target | Fase o hito destino cuya readiness se evalua |
| Purpose | Objetivo metodologico del gate |
| Required Artifacts | Artefactos obligatorios para su evaluacion |
| Required Evidence | Evidencias minimas que deben observarse |
| Pass Criteria | Condiciones minimas para recomendar Pass |
| Block Criteria | Condiciones que obligan a bloquear o fallar |
| Decision Options | Conjunto de decisiones admisibles para ese gate |
| Risks If Passed | Riesgos residuales que pueden persistir aun superando el gate |
| Traceability Links | Referencias a specs, context refs, evaluaciones u otros artefactos relacionados |

---

## 7.3 Decision Model

Todo readiness gate debe emitir una decision dentro del siguiente conjunto normalizado:

| Decision | Meaning |
| --- | --- |
| Pass | El gate puede considerarse superado sin condiciones relevantes |
| Pass with minor conditions | El gate puede superarse, pero requiere condiciones menores explicitadas |
| Fail — changes required | El gate no puede superarse hasta corregir defectos relevantes |
| Blocked | El gate no puede evaluarse o avanzar por ausencia de decisiones, evidencias o artefactos criticos |

---

## 7.4 Evaluation Rules

Un readiness gate solo puede considerarse utilizable cuando:

- identifica de forma explicita la fase actual y la fase o hito destino;
- declara un Gate Scope que permita distinguir si aplica a una transicion de fase, a un artefacto, a un contract, a un limite o a una evaluacion;
- declara artefactos y evidencias requeridos de forma verificable;
- separa criterios cumplidos, no cumplidos, riesgos y bloqueos;
- no sustituye la decision humana final cuando esta sea necesaria;
- explicita dependencias y contradicciones de alta precedencia cuando existan;
- evita aprobar avances por intencion en ausencia de evidencia observable;
- mantiene trazabilidad hacia los artefactos que justifican la decision.

---

## 8. Functional Requirements

### FR-001

La Foundation debe definir un conjunto minimo de categorias de readiness gates reutilizables entre artefactos, fases y hitos documentales.

### FR-002

Todo readiness gate debe declarar metadata minima suficiente para identificar su categoria, alcance, contexto de fase cuando aplique, artefactos requeridos, evidencias requeridas y decisiones posibles.

### FR-003

Los readiness gates deben poder evaluar avances entre Specification, Structure y futuros hitos de readiness sin requerir automatizacion ejecutable.

### FR-004

La Foundation debe exigir que toda decision de gate se apoye en evidencias documentales identificables.

### FR-005

Los readiness gates deben permanecer independientes de tecnologia, proveedor y dominio especifico.

### FR-006

Un gate reusable puede especializar criterios o artefactos requeridos, pero debe preservar el decision model comun y los criterios de bloqueo fundacionales.

### FR-007

La Foundation debe permitir que futuros templates o documentos de gates reutilicen este marco sin redefinir sus reglas nucleares.

---

## 9. Business Rules

### BR-001

Ningun avance de fase o readiness relevante debe aprobarse sin un gate o evaluacion equivalente respaldada por evidencia.

### BR-002

Un gate no puede sustituir artefactos obligatorios ausentes mediante interpretacion informal o contexto tacito.

### BR-003

Si existe una contradiccion documental de alta precedencia, el gate debe fallar o bloquearse hasta resolverla.

### BR-004

Si una decision requiere criterio humano no documentado, el gate debe marcarse como Blocked en lugar de asumir aprobacion.

---

## 10. Constraints

- esta specification debe permanecer documental y no ejecutable;
- no debe definir automatizaciones operativas, pipelines ni checks tecnicos productivos;
- no debe reemplazar la funcion de reviewer o maintainer como decision humana final;
- debe mantenerse compatible con el SDD Harness y con la definicion del QA Gate Agent.

---

## 11. Assumptions

- los proyectos derivados necesitaran gates reutilizables para validar readiness de artefactos y fases;
- existe valor en normalizar decisiones y bloqueos para hacer comparables las evaluaciones;
- las evidencias documentales seran la base minima suficiente para gates en esta fase de la Foundation.

---

## 12. Risks

| Risk | Impact | Notes |
| --- | --- | --- |
| Definir gates demasiado abstractos | Medio | Puede dificultar su aplicacion en evaluaciones concretas |
| Permitir decisiones sin evidencia suficiente | Alto | Debilita el control de calidad y favorece avances prematuros |
| Mezclar gates con aprobaciones operativas o tecnicas | Alto | Rompe el alcance documental de la Foundation |

---

## 13. Acceptance Criteria

### AC-001

La spec define categorias fundacionales de readiness gates y su proposito diferenciado.

### AC-002

La spec deja explicita la metadata minima que cualquier readiness gate debe declarar.

### AC-003

La spec fija reglas suficientes para preservar evidencia, trazabilidad, decisiones normalizadas y bloqueo conservador en futuros gates reutilizables.

---

## 14. Dependencies

- project_brief.md;
- docs/context_refs.md;
- spec-001-analytical-lifecycle.md;
- spec-002-component-boundaries.md;
- spec-004-transversal-contracts.md;
- .github/agents/qa-gate.agent.md.

---

## 15. Open Questions

- que granularidad deberian tener los artifact gates frente a los phase gates;
- si convendra definir gates separados para readiness metodologica y readiness documental;
- que template reutilizable deberia usarse para instanciar gates fundacionales o de proyecto derivado.

---

## 16. Future Considerations

- crear un template reutilizable para gate evaluations alineado con este marco;
- definir evaluaciones documentales que operen como evidencias estructuradas para gates;
- definir la relacion exacta entre readiness gates, approvals y artefactos de compatibilidad de extensiones.

---

## 17. Related Artifacts

| Artifact | Relationship |
| --- | --- |
| project_brief.md | Define el roadmap fundacional que prioriza readiness gates |
| docs/context_refs.md | Actua como fuente oficial de contexto y decisiones para esta spec |
| spec-001-analytical-lifecycle.md | Define las fases cuyo avance puede requerir gates |
| spec-002-component-boundaries.md | Define limites y handoffs que ciertos gates deben proteger |
| spec-004-transversal-contracts.md | Define contracts que pueden ser prerequisito o evidencia de un gate |
| .github/agents/qa-gate.agent.md | Define el comportamiento metodologico del agente que evaluara gates |

---

## Definition of Done

La specification esta completa cuando:

- el objetivo esta definido;
- el alcance esta definido;
- los limites estan definidos;
- los inputs estan definidos;
- los outputs estan definidos;
- los requisitos funcionales estan definidos;
- las reglas principales estan documentadas;
- los riesgos relevantes estan identificados;
- existen criterios de aceptacion verificables.