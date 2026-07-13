# Specification

## Metadata

### Spec ID

SPEC-009

### Title

Analytical Use Case Completion / Acceptance Gate

### Status

Draft

### Owner

Foundation maintainers

### Last Updated

2026-07-13

---

## 1. Purpose

Definir un gate fundacional reutilizable para determinar si un Analytical Use Case ha quedado documentalmente completo y puede considerarse aceptado para cierre.

Este gate cubre el cierre de un caso analítico como unidad metodologica, no la transicion entre fases SDD.

---

## 2. Background

La Foundation ya dispone de especificaciones para lifecycle, boundaries, contracts, evaluaciones documentales, readiness gates y el Phase Gate de entrada a Development.

Sin embargo, la experiencia con el primer caso analitico ha mostrado una necesidad distinta: despues de completar contexto, contracts, evidencia, razonamiento, recomendaciones, presentacion y validaciones, hace falta un gate canonico para decidir si el Analytical Use Case puede declararse cerrado, aceptado y reutilizable.

Ese gate no debe confundirse con un Phase Gate. Tampoco debe reutilizar SPEC-008, porque SPEC-008 autoriza el paso a Development, mientras que este gate valida el cierre de un caso analitico ya ejecutado.

---

## 3. Objective

Esta capacidad debe conseguir que cualquier proyecto derivado pueda emitir una decision canonica sobre el cierre y la aceptacion de un Analytical Use Case.

El resultado debe consolidar la evidencia documental producida durante la ejecucion del caso, verificar la completitud del ciclo analitico, registrar la deuda aceptada y dejar trazabilidad suficiente para justificar el estado final del caso.

---

## 4. Scope

### Included

- validacion de completitud del contexto del caso;
- validacion de completitud de contracts relevantes;
- validacion de cumplimiento de boundaries entre contexto, evidencia, razonamiento, recomendaciones y presentacion;
- validacion de trazabilidad end-to-end entre entradas, proceso y salida;
- validacion de que las evaluaciones documentales requeridas han sido cerradas;
- validacion de que el output artifact o output final es aceptable dentro del alcance aprobado;
- registro de deuda aceptada, limitaciones visibles y observaciones residuales;
- determinacion de si el caso es apto para reutilizacion o referencia futura.

### Excluded

- autorizacion de entrada a Development;
- despliegue, release o autorizacion operativa;
- automatizacion ejecutable de validacion;
- redefinicion del alcance analitico original;
- sustitucion del juicio humano del Reviewer o del QA Gate Agent;
- conversion del gate en decision tecnica de produccion.

---

## 5. Actors

| Actor | Description |
| --- | --- |
| Reviewer | Revisa coherencia, alcance, contradicciones y completitud documental del caso analitico |
| QA Gate Agent | Evalua la suficiencia de evidencia para emitir la decision de cierre y aceptacion |
| Documentation Agent | Mantiene la trazabilidad entre artifacts, evaluaciones y decision final |
| Specification Agent | Produce las definiciones y artefactos que luego seran cerrados o aceptados |
| Derived Project Team | Consume la decision de cierre para reutilizacion, archivo o continuidad controlada |
| Foundation Maintainers | Mantienen la definicion canonica del gate para todos los proyectos derivados |

---

## 6. Inputs

| Input | Description |
| --- | --- |
| Case Context | Alcance, objetivo, periodo, criterio operativo y limites del Analytical Use Case |
| Contract Set | Contracts aplicables al caso, incluidos context, data, discovery, analytical, evidence, knowledge, recommendation y presentation cuando proceda |
| Evaluation Set | Evaluaciones documentales que confirman o limitan la suficiencia de cada etapa |
| Traceability Set | Enlaces y referencias entre artifacts, IDs y decisiones |
| Output Artifact | Informe final, executive report o artefacto de salida equivalente |
| Accepted Debt Register | Observaciones o limitaciones aceptadas que no invalidan el cierre |
| Reuse Signals | Evidencia de que el caso puede ser reutilizado como referencia, plantilla o baseline |
| Dependency Context | Dependencias, riesgos, preguntas abiertas y supuestos que puedan afectar al cierre |

---

## 7. Outputs

| Output | Description |
| --- | --- |
| Gate Decision | Decision normalizada sobre si el Analytical Use Case puede considerarse cerrado y aceptado |
| Decision Rationale | Justificacion trazable de la decision emitida |
| Closure Observations | Observaciones residuales que no bloquean el cierre pero deben quedar visibles |
| Accepted Debt | Limitaciones o deudas metodologicas aceptadas para el cierre |
| Residual Risks | Riesgos que permanecen aun cuando el cierre se considere valido |
| Reuse Readiness Note | Nota sobre si el caso puede servir como referencia reutilizable |
| Traceability Links | Referencias a artifacts y evidencias usadas por el gate |

---

## 7.1 Decision Model

Este gate debe emitir exactamente una de las siguientes decisiones normalizadas:

| Decision | Meaning |
| --- | --- |
| Pass | El Analytical Use Case puede considerarse cerrado y aceptado sin bloqueos materiales |
| Pass with observations | El caso puede considerarse cerrado y aceptado, pero con observaciones o deuda aceptada que deben permanecer visibles |
| Fail — changes required | El caso no puede considerarse cerrado hasta corregir defectos relevantes o completar evidencias faltantes |
| Blocked | El caso no puede evaluarse o cerrarse por ausencia de artefacts criticos, contradicciones de alta precedencia o decisiones pendientes |

La decision del gate afecta al estado de cierre del caso analitico, no a la autorizacion de fase metodologica.

---

## 7.2 Execution Timing

Este gate debe ejecutarse cuando:

- el caso analitico ya ha completado sus etapas documentales principales;
- las evaluaciones relevantes han sido emitidas o cerradas;
- el output final existe y puede relacionarse con sus evidencias de origen;
- el proyecto desea registrar el cierre del caso o su reutilizacion futura;
- las observaciones restantes pueden clasificarse como aceptadas, residuales o bloqueantes.

El gate se ejecuta al final del ciclo analitico, despues de que la evidencia documental necesaria haya quedado consolidada.

---

## 7.3 Evaluation Criteria

### Pass

Debe emitirse Pass cuando:

- el contexto del caso es completo para el alcance aprobado;
- los contracts requeridos existen y son coherentes;
- los boundaries entre capas se respetan;
- la trazabilidad end-to-end es verificable;
- las evaluaciones documentales del caso estan cerradas o aceptadas;
- el output final es consistente con la evidencia y el alcance;
- no existen contradicciones materiales pendientes.

### Pass with observations

Debe emitirse Pass with observations cuando:

- existe completitud suficiente para cerrar el caso;
- persisten observaciones o deuda aceptada que no invalidan el cierre;
- las observaciones estan documentadas y separadas de los bloqueos criticos;
- la reutilizacion futura es posible siempre que dichas observaciones permanezcan visibles.

### Fail — changes required

Debe emitirse Fail — changes required cuando:

- faltan artefacts esenciales para considerar el caso completo;
- el output final no puede trazarse correctamente a sus inputs;
- una contradiccion documental afecta a la validez del cierre;
- las evaluaciones requeridas siguen abiertas o incompletas.

### Blocked

Debe emitirse Blocked cuando:

- no existe evidencia suficiente para evaluar el cierre;
- faltan artefacts obligatorios de alta precedencia;
- la decision depende de una validacion pendiente que no puede inferirse;
- existen contradicciones o decisiones humanas pendientes que impiden concluir el caso.

---

## 8. Functional Requirements

### FR-001

La Foundation debe definir un gate reusable para determinar si un Analytical Use Case puede considerarse cerrado y aceptado.

### FR-002

El gate debe consolidar evidencia documental existente sin sustituirla por inferencias no verificables.

### FR-003

El gate debe distinguirse explicitamente de cualquier Phase Gate de transicion metodologica, incluido SPEC-008.

### FR-004

El gate debe validar completitud de contexto, contracts, boundaries, evaluaciones y output final.

### FR-005

El gate debe registrar de forma explicita la deuda aceptada y las observaciones residuales.

### FR-006

El gate debe preservar trazabilidad hacia los artefactos que justifican el cierre del caso.

### FR-007

El gate debe permitir que un caso analitico sea marcado como apto para reutilizacion o referencia futura cuando la evidencia lo soporte.

### FR-008

La Foundation debe permitir que este gate sea reutilizable por cualquier proyecto derivado sin redefinir su logica nuclear.

---

## 9. Business Rules

### BR-001

Un Analytical Use Case no puede considerarse cerrado si faltan artefactos criticos o evaluaciones esenciales del ciclo.

### BR-002

La aceptacion de deuda o de observaciones residuales solo es valida si estas quedan explicitamente documentadas.

### BR-003

El cierre de un caso analitico no autoriza por si mismo una transicion de fase metodologica.

### BR-004

Un resultado Pass with observations puede cerrar el caso, pero debe dejar visibles las observaciones que acompañan la aceptacion.

### BR-005

Si la trazabilidad end-to-end no puede demostrarse, el gate no debe emitir Pass.

### BR-006

Si la decision depende de una validacion pendiente no ejecutada, el gate debe permanecer Blocked o Fail — changes required segun el tipo de ausencia.

---

## 10. Constraints

- esta specification debe permanecer documental y no ejecutable;
- no debe definir pipelines tecnicos, automatizaciones operativas ni checks productivos;
- no debe sustituir el juicio del Reviewer ni del QA Gate Agent;
- no debe confundirse con un Phase Gate de Development;
- debe mantenerse compatible con el SDD Harness y con el marco de readiness gates ya publicado.

---

## 11. Assumptions

- los proyectos derivados necesitan un mecanismo canonico para declarar cierre y aceptacion de un caso analitico;
- la completitud documental de un caso puede evaluarse sin redefinir su fase metodologica;
- la deuda aceptada puede coexistir con un cierre valido si se documenta con suficiente claridad;
- la trazabilidad entre entradas, proceso y salida es suficiente para sostener la aceptacion del caso.

---

## 12. Risks

| Risk | Impact | Notes |
| --- | --- | --- |
| Confundir el gate de cierre con un Phase Gate | Alto | Puede introducir autorizacion de fase donde solo corresponde cierre de caso |
| Aceptar deuda sin documentarla | Alto | Debilita la trazabilidad y vuelve ambiguo el estado final |
| Cerrar casos con trazabilidad incompleta | Alto | Reduce reutilizacion y dificulta revisiones futuras |
| Mezclar output acceptance con autorizacion operativa | Alto | Rompe la separacion entre cierre documental y decision tecnica |

---

## 13. Acceptance Criteria

### AC-001

La spec define un gate reutilizable para cierre y aceptacion de Analytical Use Cases.

### AC-002

La spec deja explicita la diferencia entre cierre de caso y transicion de fase metodologica.

### AC-003

La spec define inputs, outputs, decision model, reglas y criterios suficientes para evaluar completitud, trazabilidad, deuda aceptada y reutilizacion.

### AC-004

La spec permanece independiente de tecnologia, proveedor y dominio especifico.

---

## 14. Dependencies

- SPEC-001 Analytical Lifecycle;
- SPEC-002 Component Boundaries;
- SPEC-004 Transversal Contracts;
- SPEC-005 Readiness Gates;
- SPEC-006 Documentary Evaluations;
- SPEC-008 Development Entry Phase Gate;
- analytical_use_cases/meta_lead_quality_analysis.md;
- docs/context_refs.md.

---

## 15. Open Questions

- debe existir un template especifico para closure reviews de Analytical Use Cases;
- el repositorio derivado debe registrar el cierre del caso como gate, review o ambos;
- la Foundation debe definir si este gate aplica solo a casos analiticos o tambien a otras unidades documentales reutilizables.

---

## 16. Future Considerations

- crear un template reutilizable para closure review;
- crear una evaluacion documental estandar para acceptance de output final;
- definir una taxonomia comun para deuda aceptada, observaciones residuales y limitaciones visibles;
- alinear este gate con futuros artefactos de reuse readiness.

---

## 17. Related Artifacts

| Artifact | Relationship |
| --- | --- |
| Project Brief | Define el proposito general del proyecto derivado que produce Analytical Use Cases |
| docs/tasks.md | Puede registrar la tarea de cierre o acceptance del caso |
| docs/context_refs.md | Indice oficial de contexto y decisiones aplicables |
| SPEC-005 Readiness Gates | Marco general de gates reutilizables |
| SPEC-006 Documentary Evaluations | Marco de evaluaciones documentales |
| SPEC-008 Development Entry Phase Gate | Gate distinto para autorizacion de entrada a Development |
| Closure Review | Evidencia documental de cierre del caso |
| Output Artifact | Artefacto final cuya aceptacion evalua este gate |

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
- existen criterios de aceptacion verificables;
- la diferencia con SPEC-008 queda explicitamente documentada.