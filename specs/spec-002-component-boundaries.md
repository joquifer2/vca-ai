# Specification

## Metadata

### Spec ID

SPEC-002

### Title

Component Boundaries

### Status

Draft

### Owner

Foundation maintainers

### Last Updated

2026-07-10

---

## 1. Purpose

Definir los limites de responsabilidad y las reglas de interaccion entre los componentes principales de AIF para evitar acoplamientos impropios entre datos, analisis, razonamiento y presentacion.

---

## 2. Background

El Project Brief y la vision de AIF requieren una separacion estricta entre capas. Esta specification convierte ese principio en una definicion operativa de responsabilidades, handoffs y restricciones entre componentes.

---

## 3. Objective

Esta capacidad debe conseguir que la Foundation tenga una arquitectura conceptual desacoplada, donde cada componente posea una unica responsabilidad y toda colaboracion ocurra mediante contratos o artefactos estandarizados.

El resultado debe impedir que una decision de datos, una interpretacion de dominio o una necesidad de presentacion contamine otras capas.

---

## 4. Scope

### Included

- definicion de responsabilidades para Data Provider, capa analitica, capa de razonamiento y capa de presentacion;
- definicion de handoffs permitidos entre componentes;
- definicion de prohibiciones de acoplamiento entre capas;
- definicion del papel del Framework como coordinador metodologico.

### Excluded

- diseno tecnico detallado de interfaces ejecutables;
- seleccion de framework, lenguaje o herramienta;
- implementacion de componentes concretos;
- contratos de datos con estructura final de campos.

---

## 5. Actors

| Actor | Description |
| --- | --- |
| Framework | Coordina el flujo metodologico y valida transiciones entre componentes |
| Data Provider | Adquiere informacion desde fuentes externas y la expone mediante contratos |
| Analytical Layer | Prepara datos y produce evidencia observable |
| Reasoning Layer | Interpreta evidencia para generar conocimiento accionable |
| Presentation Layer | Construye artefactos finales sin introducir logica analitica |
| Skill | Aporta conocimiento especifico que se aplica dentro de limites controlados |

---

## 6. Inputs

| Input | Description |
| --- | --- |
| Data Contract | Informacion estructurada entregada por un Data Provider |
| Evidence Contract | Evidencia producida por la capa analitica |
| Knowledge Contract | Insights, hipotesis y recomendaciones generados por razonamiento |
| Presentation Request | Requisitos del artefacto final |
| Skill Rules | Reglas y conocimiento de dominio compatibles con la Foundation |

---

## 7. Outputs

| Output | Description |
| --- | --- |
| Responsibility Map | Mapa de responsabilidades por componente |
| Handoff Rules | Reglas de intercambio permitidas entre componentes |
| Boundary Constraints | Restricciones para prevenir solapamientos y acoplamientos |
| Coordination Principles | Principios de coordinacion que debe aplicar el Framework |

---

## 7.1 Responsibility Map

| Component | Primary Responsibility | Must Not Do |
| --- | --- | --- |
| Data Provider | Adquirir y exponer informacion mediante contratos estandarizados | Interpretar datos, priorizar hallazgos o formular recomendaciones |
| Analytical Layer | Preparar datos y producir evidencia observable | Introducir conclusiones de negocio o reescribir contexto de dominio |
| Reasoning Layer | Convertir evidencia en conocimiento accionable | Reconsultar la fuente original para compensar evidencia mal definida |
| Presentation Layer | Construir artefactos finales a partir de conocimiento ya generado | Crear nueva evidencia, reinterpretar conclusiones o alterar prioridades |
| Framework | Coordinar el flujo metodologico y validar precondiciones de handoff | Actuar como runtime productivo o sustituir responsabilidades de una capa |
| Skill | Aportar reglas de dominio dentro de limites controlados | Reasignar el rol basal de un componente o eliminar fases del ciclo |

---

## 7.2 Handoff Rules

| From | To | Allowed Artifact | Receiver Preconditions | Sender Exit Condition |
| --- | --- | --- | --- | --- |
| Data Provider | Analytical Layer | Data Contract | El contrato identifica origen, estructura y limitaciones relevantes | La informacion fue expuesta sin interpretacion analitica |
| Analytical Layer | Reasoning Layer | Evidence Contract | La evidencia es observable, trazable y separada de conclusiones | Los hallazgos estan estructurados y respaldados por el modelo analitico |
| Reasoning Layer | Presentation Layer | Knowledge Contract | El conocimiento incluye insights, hipotesis, prioridades e incertidumbres declaradas | La interpretacion esta respaldada por evidencia identificable |
| Reasoning Layer | Framework | Recommendation Set o Knowledge Contract | El Framework puede verificar trazabilidad, completitud y cumplimiento metodologico | Las recomendaciones o conclusiones estan justificadas |
| Framework | Presentation Layer | Presentation Approval o equivalente documental | Existe validacion metodologica previa del contenido a presentar | Se verifico que el formato no sustituye al analisis |
| Skill | Analytical Layer o Reasoning Layer | Skill Rules | La extension declara su alcance, inputs y outputs | Las reglas de dominio no alteran responsabilidades fundacionales |

---

## 7.3 Boundary Constraints

- el Data Provider no puede emitir insights, hipotesis ni conclusiones;
- la capa analitica no puede formular recomendaciones ni reescribir objetivos de negocio;
- la capa de razonamiento no puede modificar retrospectivamente los hechos observados para sostener una conclusion;
- la capa de presentacion no puede introducir nueva evidencia, nueva interpretacion ni nuevo orden de prioridad;
- el Framework solo valida secuencia, completitud y precondiciones metodologicas;
- las Skills solo pueden enriquecer criterios o interpretaciones dentro de la capa donde se apliquen.

---

## 7.4 Coordination Principles

- todo handoff debe materializarse en un artefacto identificable y revisable;
- cada componente recibe solo la informacion necesaria para su responsabilidad;
- si falta una precondicion, el flujo debe detenerse o marcar el estado como incompleto en lugar de compensarlo informalmente;
- cualquier excepcion o estado UNKNOWN debe propagarse de forma explicita al siguiente componente cuando afecte la interpretacion.

---

## 8. Functional Requirements

### FR-001

La Foundation debe distinguir como minimo los componentes Data Provider, capa analitica, capa de razonamiento y capa de presentacion.

### FR-002

El Data Provider debe limitarse a adquirir y exponer informacion sin realizar interpretacion analitica ni razonamiento.

### FR-003

La capa analitica debe transformar datos en evidencia sin introducir conclusiones de negocio ni recomendaciones.

### FR-004

La capa de razonamiento debe consumir evidencia y producir conocimiento sin depender directamente de la fuente de datos original.

### FR-005

La capa de presentacion debe consumir conocimiento estructurado sin contener logica analitica ni reescribir conclusiones.

### FR-006

El Framework debe coordinar handoffs entre componentes y verificar que cada salida cumpla las precondiciones del siguiente componente.

### FR-007

Toda interaccion entre componentes debe ocurrir mediante contratos o artefactos definidos, no mediante dependencias implicitas o comparticion informal de contexto.

---

## 9. Business Rules

### BR-001

Cada componente debe tener una unica responsabilidad principal claramente definida.

### BR-002

Ningun componente puede asumir responsabilidades de una capa anterior o posterior para compensar huecos de definicion.

### BR-003

La interpretacion de negocio pertenece al razonamiento apoyado por Skills, no a la adquisicion ni a la presentacion.

### BR-004

Los Templates pueden transformar formato, pero no crear nueva evidencia ni nuevas conclusiones.

---

## 10. Constraints

- esta spec define limites conceptuales, no interfaces ejecutables;
- no debe fijar una topologia de despliegue ni una tecnologia de integracion;
- los componentes deben permanecer reutilizables entre distintos dominios y fuentes de datos;
- las Skills no pueden modificar el rol basal de cada componente.

---

## 11. Assumptions

- los proyectos derivados necesitaran desacoplar fuentes de datos y logica analitica;
- existiran contratos suficientes para intercambiar datos, evidencia y conocimiento entre capas;
- el Framework puede validar handoffs metodologicos sin convertirse en runtime operativo.

---

## 12. Risks

| Risk | Impact | Notes |
| --- | --- | --- |
| Limites demasiado ambiguos entre analisis y razonamiento | Alto | Puede mezclar evidencia con interpretacion |
| Handoffs poco definidos | Medio | Dificulta reutilizacion y validacion |
| Permitir que Templates alteren contenido | Alto | Debilita trazabilidad y explicabilidad |

---

## 13. Acceptance Criteria

### AC-001

La spec distingue explicitamente responsabilidades, handoffs y restricciones para cada componente principal.

### AC-002

La spec deja prohibido que la presentacion contenga logica analitica o que la adquisicion introduzca razonamiento.

### AC-003

La spec establece que las interacciones entre capas dependen de contratos o artefactos estandarizados.

---

## 14. Dependencies

- project_brief.md;
- docs/context_refs.md;
- spec-001-analytical-lifecycle.md;
- spec-004-transversal-contracts.md.

---

## 15. Open Questions

- que nivel de formalismo requeriran los contracts entre capas;
- si el Framework necesitara un artefacto documental propio para validar handoffs;
- como se representaran las excepciones o estados UNKNOWN entre componentes.

---

## 16. Future Considerations

- crear una taxonomia de artefactos de handoff;
- alinear los handoffs con las categorias contractuales ya definidas en SPEC-004;
- definir gates especificos para validar boundary compliance apoyandose en SPEC-005.

---

## 17. Related Artifacts

| Artifact | Relationship |
| --- | --- |
| project_brief.md | Define el proposito y alcance fundacional |
| docs/context_refs.md | Fuente oficial de contexto utilizada para esta spec |
| spec-001-analytical-lifecycle.md | Describe la secuencia comun que estos componentes soportan |
| spec-003-extensibility-model.md | Define como extender componentes sin romper sus limites |
| spec-004-transversal-contracts.md | Define contracts reutilizables para materializar handoffs entre capas |
| spec-005-readiness-gates.md | Define gates que pueden validar cumplimiento de limites y handoffs |

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