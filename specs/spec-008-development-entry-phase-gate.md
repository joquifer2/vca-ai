# Specification

## Metadata

### Spec ID

SPEC-008

### Title

Development Entry Phase Gate

### Status

Draft

### Owner

Foundation maintainers

### Last Updated

2026-07-11

---

## 1. Purpose

Definir el gate fundacional reutilizable que autoriza o bloquea la transicion de un proyecto derivado desde Specification / Structure hacia Development.

Este gate establece un mecanismo canonico para consolidar la evidencia generada durante la fase documental y decidir si el proyecto puede iniciar trabajo de implementacion sin romper la separacion entre definicion y construccion.

---

## 2. Background

La Foundation ya define el lifecycle, los readiness gates y las evaluaciones documentales, pero el desarrollo del primer proyecto derivado ha mostrado un hueco metodologico: no existe un gate canonico que autorice el paso a Development de forma reutilizable para cualquier derivado.

La ausencia de este gate obliga a resolver esa transicion de forma implícita o ad hoc, lo que debilita la trazabilidad y hace menos clara la relacion entre la finalizacion documental y el inicio de implementacion.

Esta specification introduce ademas una clasificacion explicita entre:

- Quality Gates: validan la suficiencia, consistencia o calidad de un artefacto concreto o de un conjunto acotado de artefactos;
- Phase Gates: autorizan o bloquean la transicion entre fases metodologicas.

La clasificacion aporta claridad porque separa dos decisiones distintas: si un artefacto es aceptable y si el proyecto puede avanzar de fase. Tambien mejora la escalabilidad, porque evita mezclar evaluaciones locales con decisiones de transicion de mayor alcance.

---

## 3. Objective

Esta capacidad debe conseguir que cualquier proyecto derivado disponga de un Phase Gate canonico para determinar si puede iniciar Development.

El resultado debe permitir consolidar la evidencia producida durante Specification / Structure, emitir una decision normalizada y dejar trazabilidad suficiente para justificar la autorizacion o el bloqueo del paso a Development.

---

## 4. Scope

### Included

- definicion del Phase Gate de entrada a Development para proyectos derivados;
- definicion de su alcance como gate reutilizable y no especifico de vca-ai;
- definicion de las entradas, evidencias y criterios que consume;
- definicion de las decisiones posibles y su significado metodologico;
- definicion de la relacion entre Quality Gates y Phase Gates;
- definicion de su papel como consolidacion de evidencia previa a Development.

### Excluded

- autorizacion tecnica de despliegue, release o produccion;
- automatizacion ejecutable de validacion;
- reglas especificas de un proyecto derivado concreto;
- reemplazo de la revision humana del Reviewer o del QA Agent;
- definicion de criterios de implementacion del proyecto derivado.

---

## 5. Actors

| Actor | Description |
| --- | --- |
| Reviewer | Revisa coherencia, alcance, contradicciones y completitud documental del material evaluado |
| QA Gate Agent | Evalua la suficiencia de evidencia y aplica el gate conforme a la metodologia publicada |
| Specification Agent | Produce los artefactos y decisiones que seran consolidados por el gate |
| Documentation Agent | Mantiene la trazabilidad de artefactos, referencias y evidencias usadas por el gate |
| Foundation Maintainers | Mantienen la definicion canonica del gate para todos los proyectos derivados |
| Derived Project Team | Consume el gate para decidir si puede iniciar Development |

---

## 6. Inputs

| Input | Description |
| --- | --- |
| Project Context | Identificacion del proyecto derivado y estado metodologico actual |
| Specification Set | Specifications aplicables y su estado de revision |
| Supporting Documentation | README, context refs, glosario y artefactos metodologicos relacionados |
| Quality Gate Evidence | Resultados de quality gates relevantes sobre artefactos concretos |
| Review Evidence | Observaciones, correcciones o validaciones emitidas por Reviewer |
| QA Evidence | Conclusiones, bloqueos o observaciones emitidas por QA Gate Agent |
| Dependency Context | Dependencias, riesgos, preguntas abiertas y supuestos que puedan afectar la transicion |
| Development Readiness Evidence | Evidencias de que Specification / Structure esta completo dentro del alcance aprobado |

---

## 7. Outputs

| Output | Description |
| --- | --- |
| Gate Decision | Decision normalizada sobre si puede iniciarse Development |
| Decision Rationale | Justificacion trazable de la decision emitida |
| Blockers | Condiciones que impiden avanzar a Development |
| Observations | Condiciones o advertencias que no bloquean el avance, pero deben ser visibles |
| Traceability Links | Referencias a artefactos y evidencias utilizadas por el gate |

---

## 7.1 Decision Model

El gate debe emitir exactamente una de las siguientes decisiones:

| Decision | Meaning |
| --- | --- |
| PASS | La transicion a Development queda autorizada sin bloqueos materiales |
| PASS WITH OBSERVATIONS | La transicion a Development queda autorizada, pero con observaciones documentadas que deben mantenerse visibles durante el arranque |
| BLOCKED | La transicion a Development queda bloqueada hasta resolver evidencias ausentes, contradicciones o dependencias criticas |

Una decision PASS WITH OBSERVATIONS autoriza el paso a Development; no requiere un gate adicional para producir la autorizacion, pero si exige conservar y tratar las observaciones como deuda metodologica activa.

---

## 7.2 Execution Timing

Este gate debe ejecutarse una sola vez que se cumplan las siguientes condiciones previas:

- los Quality Gates relevantes sobre artefactos concretos han sido resueltos o aceptados con observaciones no bloqueantes;
- el Reviewer ha completado la revision documental del alcance que se pretende llevar a Development;
- el QA Gate Agent ha emitido evidencia o conclusion suficiente sobre readiness;
- la documentacion de contexto, specs y artefactos relacionados refleja el alcance aprobado sin contradicciones criticas;
- el proyecto derivado solicita formalmente la autorizacion para iniciar Development.

El gate se ejecuta inmediatamente antes de autorizar el inicio de Development y actua como la consolidacion final de la evidencia generada durante Specification / Structure.

---

## 7.3 Evaluation Criteria

### PASS

Debe emitirse PASS cuando:

- todos los artefactos requeridos por el alcance aprobado existen y son trazables;
- no existen preguntas abiertas criticas que afecten al arranque de Development;
- las contradicciones detectadas han sido resueltas o ya no afectan al alcance evaluado;
- la evidencia de Reviewer y QA es coherente con la autorizacion de fase;
- el alcance documentado es suficientemente estable para iniciar trabajo de implementacion.

### PASS WITH OBSERVATIONS

Debe emitirse PASS WITH OBSERVATIONS cuando:

- existe evidencia suficiente para iniciar Development;
- persisten observaciones documentadas que no bloquean la fase, pero deben mantenerse visibles;
- las observaciones no comprometen la trazabilidad minima ni la coherencia del alcance aprobado;
- el proyecto acepta iniciar Development con esas observaciones como deuda metodologica activa.

### BLOCKED

Debe emitirse BLOCKED cuando:

- faltan artefactos obligatorios o evidencias criticas;
- una contradiccion documental impide confiar en el alcance evaluado;
- persisten preguntas abiertas que afectan a la decision de inicio;
- el Reviewer o el QA Gate Agent no han producido evidencia suficiente para consolidar la transicion;
- el proyecto pretende iniciar Development sin cumplir las condiciones previas del gate.

---

## 8. Functional Requirements

### FR-001

La Foundation debe definir un Phase Gate reusable que determine si un proyecto derivado puede pasar de Specification / Structure a Development.

### FR-002

El gate debe consolidar evidencia ya producida durante Specification / Structure y no sustituirla por inferencias no verificables.

### FR-003

El gate debe distinguirse explicitamente de los Quality Gates que validan un artefacto concreto o un conjunto acotado de artefactos.

### FR-004

El gate debe emitir una decision normalizada que permita autorizar, autorizar con observaciones o bloquear la transicion a Development.

### FR-005

El gate debe permanecer independiente de dominio, tecnologia, proveedor y estructura interna del proyecto derivado.

### FR-006

El gate debe preservar trazabilidad hacia las evidencias, reviews, QA findings y artefactos que justifican la decision.

### FR-007

El gate no debe reemplazar la funcion del Reviewer ni del QA Agent, sino integrar su evidencia para una decision de fase.

### FR-008

La Foundation debe permitir que este Phase Gate sea reutilizable por cualquier proyecto derivado sin redefinir su logica nuclear.

---

## 9. Business Rules

### BR-001

Solo puede emitirse una decision de entrada a Development cuando existe un conjunto minimo de evidencias documentales observables y trazables.

### BR-002

La ausencia de evidencias obligatorias, preguntas abiertas criticas o contradicciones de alta precedencia debe conducir a BLOCKED.

### BR-003

Un resultado PASS WITH OBSERVATIONS puede autorizar el paso a Development, pero debe dejar constancia de las observaciones que acompañan la autorizacion.

### BR-004

Una decision de gate no puede basarse en expectativa de completitud futura ni en memoria informal.

### BR-005

Si una observacion afecta a la decision de fondo sobre readiness, el gate debe bloquearse hasta resolverla o reclasificarla con trazabilidad.

### BR-006

El gate debe considerar como prerequisito que los Quality Gates relevantes sobre artefactos concretos ya hayan sido resueltos o explicitamente aceptados como observaciones no bloqueantes.

---

## 10. Constraints

- esta specification debe permanecer documental y no ejecutable;
- no debe definir pipelines tecnicos, automatizaciones operativas ni checks productivos;
- no debe sustituir el juicio del Reviewer ni del QA Gate Agent;
- no debe mezclar validacion de artefactos con autorizacion de fase;
- debe mantenerse compatible con el SDD Harness y con el marco de readiness gates ya publicado.

---

## 11. Assumptions

- los proyectos derivados necesitaran una decision canonica para pasar de definicion a implementacion;
- la distincion entre quality gates y phase gates reduce ambiguedad y mejora escalabilidad metodologica;
- la evidencia documental producida durante Specification / Structure puede consolidarse sin requerir cambio de fase prematuro;
- Development solo debe iniciarse cuando el alcance documentado lo permita y exista trazabilidad suficiente.

---

## 12. Risks

| Risk | Impact | Notes |
| --- | --- | --- |
| Mezclar quality gates con phase gates | Alto | Puede confundir la validacion de artefactos con la autorizacion de fase |
| Aprobar Development con evidencia insuficiente | Alto | Introduce implementacion prematura y reduce trazabilidad |
| Convertir el gate en una aprobacion puramente formal | Medio | Debilita su valor como consolidacion de evidencia |
| Tratar PASS WITH OBSERVATIONS como equivalencia total a PASS | Medio | Puede ocultar deuda documental relevante |
| Retrasar el gate hasta que empiece Development | Medio | Rompe la funcion canonica del gate como autorizacion previa a la fase |

---

## 13. Acceptance Criteria

### AC-001

La specification define un Phase Gate reutilizable para autorizar o bloquear el paso a Development desde Specification / Structure.

### AC-002

La specification distingue explicitamente entre Quality Gates y Phase Gates y justifica por que esa diferenciacion mejora claridad y escalabilidad.

### AC-003

La specification define las entradas, evidencias, criterios y decisiones posibles del gate.

### AC-004

La specification deja explicito que el gate no sustituye al Reviewer ni al QA Agent.

### AC-005

La specification establece que el gate consolida la evidencia producida durante Specification / Structure antes de autorizar Development y define su momento de ejecucion.

### AC-006

La specification incluye riesgos, artefactos relacionados y Definition of Done verificables.

---

## 14. Dependencies

- [specs/spec-001-analytical-lifecycle.md](/specs/spec-001-analytical-lifecycle.md)
- [specs/spec-005-readiness-gates.md](/specs/spec-005-readiness-gates.md)
- [specs/spec-006-documentary-evaluations.md](/specs/spec-006-documentary-evaluations.md)
- [gates/specification_phase_close.md](/gates/spec-008-development-entry-phase-gate.md)
- [.github/instructions/sdd.instructions.md](/.github/instructions/sdd.instructions.md)
- [docs/context_refs.md](/docs/context_refs.md)
- [docs/glosario_terminos.md](/docs/glosario_terminos.md)

---

## 15. Open Questions

- Si futuros derivativos necesitan subtipos adicionales de Phase Gate, esta specification debera ampliarse o servir como base para una taxonomia mas rica.
- Debe evaluarse en futuras specs si otros hitos de fase requieren gates equivalentes con criterios propios.

---

## 16. Future Considerations

- posible extension a otros Phase Gates para hitos relevantes de proyectos derivados;
- posible alineacion con templates de evaluacion de readiness para reutilizar la decision model;
- posible formalizacion de subcategorias adicionales dentro de Quality Gates si el ecosistema metodologico crece.

---

## 17. Related Artifacts

| Artifact | Relationship |
| --- | --- |
| Project Brief | Define el marco fundacional y los limites que condicionan la transicion a Development |
| Specification | Esta spec establece el nuevo Phase Gate fundacional |
| QA Gate Agent | Consume la especificacion para evaluar la suficiencia de evidencia |
| Reviewer | Aporta revision documental que el gate consolida |
| Readiness Gates Spec | Proporciona el marco general de readiness gates |
| Documentary Evaluations Spec | Proporciona el marco general de evaluaciones documentales |
| Specification Phase Close Gate | Ejemplo de gate de fase ya publicado para el alcance fundacional inicial |
| Context References | Fuente oficial de contexto para consolidar evidencias |
| Glosario | Define la taxonomia metodologica relevante, incluida la diferenciacion entre gates |

---

## Definition of Done

La specification esta completa cuando:

- el propósito del Phase Gate está definido;
- el ámbito de aplicación está delimitado a proyectos derivados;
- el momento de ejecución está asociado a la transición desde Specification / Structure a Development;
- el momento de ejecución del gate está definido y situado antes del inicio de Development;
- las entradas, evidencias y criterios de evaluación están definidos;
- las decisiones posibles están normalizadas en PASS, PASS WITH OBSERVATIONS y BLOCKED;
- la diferencia entre Quality Gates y Phase Gates está explicitada y justificada;
- la relación con Reviewer y QA Agent está claramente delimitada;
- los riesgos, artefactos relacionados y criterios de aceptación están documentados;
- la spec puede pasar a revisión por Reviewer y QA antes de incorporarse al núcleo fundacional.