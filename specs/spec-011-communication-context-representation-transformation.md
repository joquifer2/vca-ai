# Specification

## Metadata

### Spec ID

SPEC-011

### Title

Communication Context Representation Transformation

### Status

Draft

### Owner

Equipo VCA

### Last Updated

2026-07-14

---

## 1. Purpose

Definir la capacidad minima y verificable para transformar la representacion de una salida ya seleccionada a partir de un Communication Context compuesto, preservando equivalencia semantica, trazabilidad y boundaries metodologicos.

Esta specification no introduce nuevas responsabilidades de conocimiento o recomendacion.

Esta specification no modifica AIF Foundation.

---

## 2. Background

La decision arquitectonica VCA-AUC-001-ARCH-001 establecio la necesidad de canonicalizar el alcance de ejecucion antes de congelar un Execution Context.

La decision arquitectonica VCA-AUC-001-ARCH-002 mostro que Presentation Layer debe producir dos representaciones paralelas del mismo contenido validado: una proyeccion analitica y una proyeccion ejecutiva.

La decision arquitectonica VCA-AUC-001-ARCH-003 formaliza que la forma de comunicar esa salida depende de un Communication Context compuesto y que la equivalencia semantica gobierna la transformacion de representacion.

La evidencia observada en vca-ai no demuestra todavia una necesidad independiente para crear una capa de conocimiento o recomendacion adicional. Por tanto, esta specification formaliza solo la distincion minima respaldada por evidencia: transformar la representacion de la salida sin alterar el contenido canónico ni la proyeccion ya seleccionada.

---

## 3. Objective

Esta capacidad debe conseguir que, dado un contenido canónico ya validado y una proyeccion de presentacion ya seleccionada, vca-ai adapte el Presentation Layer Output a un contexto comunicativo concreto sin introducir nueva evidencia, nuevo razonamiento ni nuevas recomendaciones.

El resultado debe permitir materializar una salida trazable cuyo significado sea equivalente al contenido canónico aprobado, aunque la terminologia, la secuencia narrativa, la densidad informativa o la organización documental cambien segun el contexto comunicativo.

---

## 4. Scope

### Included

- transformacion de la representacion de una salida ya seleccionada a partir de un Communication Context compuesto;
- adaptacion de la salida a audiencia, proposito, decision soportada y nivel de abstraccion;
- variacion controlada de densidad informativa, orden de exposicion, jerarquia comunicativa, vocabulario y visibilidad de trazabilidad;
- preservacion de equivalencia semantica del contenido canónico;
- preservacion de prioridad, cobertura, limitaciones materiales y estados UNKNOWN;
- preservacion de la trazabilidad hacia Evidence, Knowledge y Recommendation Sets;
- reglas para impedir nueva evidencia, nueva interpretacion, nueva recomendacion o reordenacion del contenido aprobado.

### Excluded

- canonicalizacion del alcance de ejecucion;
- seleccion de proyeccion de presentacion;
- subdivision adicional de la proyeccion analitica en esta iteracion;
- nuevas responsabilidades de generacion de conocimiento o recomendaciones;
- diseno tecnico ejecutable de interfaces o renderers;
- nueva adquisicion de datos, nueva evidencia o nueva interpretacion;
- generacion de Tasks.

---

## 5. Conceptual Transformation Workflow

El flujo conceptual de esta capacidad sigue una secuencia interna estable que permite comprender como el Presentation Layer Output se deriva sin alterar el contenido canónico ni la proyeccion ya seleccionada.

### Secuencia Logica

1. Recepcion del contenido canónico ya validado.
2. Recepcion del Communication Context compuesto.
3. Derivacion de Representation Constraints a partir del Communication Context y del contexto canonico disponible.
4. Aplicacion de las transformaciones permitidas sobre el contenido canónico, segun las restricciones derivadas.
5. Verificacion de equivalencia semantica respecto del contenido canonico aprobado.
6. Materializacion del Presentation Layer Output adaptado al contexto comunicativo declarado.

### Representation Constraints

El Communication Context no transforma directamente el Presentation Layer Output.

Primero determina un conjunto de Representation Constraints que acotan como puede expresarse el contenido canonico sin cambiar su significado autorizado.

Despues, la transformacion aplica dichas restricciones sobre el contenido canónico y sobre la proyeccion ya seleccionada para producir la salida final.

Las Representation Constraints pueden acotar, como minimo, la audiencia, el proposito comunicativo, el nivel de abstraccion, la densidad informativa, la visibilidad de trazabilidad, la organizacion narrativa y las restricciones de formato.

En la evidencia actual de vca-ai, Representation Constraints se consideran un concepto interno de esta capacidad y no existe aun evidencia suficiente para promoverlas a Contract transversal del framework.

### Transformaciones Permitidas

Las transformaciones permitidas se limitan a variaciones controladas que preservan la equivalencia semantica del contenido canonico.

Se distinguen cuatro clases conceptuales:

- transformaciones terminologicas, que ajustan el vocabulario o la formulacion sin alterar la interpretacion autorizada;
- transformaciones estructurales, que reorganizan la secuencia o agrupacion documental sin modificar el contenido aprobado;
- transformaciones de abstraccion, que ajustan el nivel de detalle o la granularidad comunicativa;
- transformaciones de densidad informativa, que condensan o expanden la presentacion sin introducir nuevo significado.

Una transformacion terminologica nunca puede convertirse en una transformacion semantica.

Cualquier cambio de vocabulario debe preservar exactamente la interpretacion autorizada del contenido canonico.

---

## 6. Actors

| Actor | Description |
|---|---|
| Framework | Verifica que la transformacion de representacion sea consistente con el contexto canonico y con la salida seleccionada |
| Context Definition | Define objetivo, audiencia, proposito, decision soportada y restricciones de salida |
| Execution Context | Congela la instancia de ejecucion y la proyeccion seleccionada antes de la materializacion |
| Communication Context | Declara la combinacion de dimensiones comunicativas que gobierna la adaptacion de la representacion |
| Presentation Layer | Materializa la salida adaptada sin decidir la proyeccion ni alterar el contenido canonico |
| Analytical Projection Consumer | Consume la representacion analitica para revision, auditoria o validacion metodologica |
| Executive Projection Consumer | Consume la representacion ejecutiva para lectura decisional y comunicacion de negocio |
| Reviewer | Verifica coherencia, trazabilidad, equivalencia semantica y ausencia de nuevo razonamiento |

---

## 7. Inputs

| Input | Description |
|---|---|
| Context Definition | Objetivo, audiencia, proposito, decision soportada y restricciones declaradas |
| Execution Scope Canonicalization Result | Alcance de ejecucion resuelto y congelado antes de la presentacion |
| Selected Presentation Projection | Proyeccion ya materializable segun el Execution Context canonicalizado |
| Communication Context | Audiencia, proposito comunicativo, tipo de decision soportada, nivel de abstraccion, densidad informativa, visibilidad de trazabilidad y restricciones de formato |
| Knowledge Set | Insights, conclusiones, riesgos e incertidumbres ya validados |
| Recommendation Set | Acciones sugeridas aprobadas y priorizadas |
| Presentation Contract | Contenido aprobado que puede consumirse para construir la salida |
| Output Request | Solicitud de salida que declara la instancia comunicativa o la necesidad de bloqueo |

---

## 8. Outputs

| Output | Description |
|---|---|
| Presentation Layer Output | Salida final adaptada al contexto comunicativo declarado |
| Semantic Equivalence Status | Indicacion de que el contenido representado conserva el significado aprobado |
| Traceable Output | Salida final con referencias suficientes a artefactos fuente |
| Communication Fit | Indicacion de que la forma de salida es compatible con el contexto comunicativo declarado |
| Boundary Status | Indicacion de que no se introdujo nueva evidencia, interpretacion ni priorizacion |

---

## 9. Functional Requirements

### FR-001

La capacidad debe definir una capacidad reusable para adaptar la representacion de una salida ya seleccionada a un Communication Context compuesto.

### FR-002

La transformacion debe consumir una proyeccion de presentacion ya seleccionada y no decidirla.

### FR-003

La transformacion debe preservar equivalencia semantica con el contenido canónico aprobado.

### FR-004

La transformacion debe poder variar, de forma controlada, la organizacion narrativa, la jerarquia comunicativa, la densidad informativa, el vocabulario y la visibilidad de trazabilidad.

### FR-005

La transformacion no debe modificar evidencia, conclusiones, prioridades, recomendaciones ni limitaciones materiales aprobadas.

### FR-006

La transformacion no debe introducir nueva evidencia, nuevo razonamiento, nueva interpretacion ni nuevas recomendaciones.

### FR-007

La transformacion debe conservar trazabilidad suficiente hacia Evidence, Knowledge y Recommendation Sets para reconstruir el significado fuente.

### FR-008

La transformacion debe mantener visible la informacion material que condicione la interpretacion de la salida, incluyendo UNKNOWN relevantes y coverage states cuando apliquen.

---

## 10. Business Rules

### BR-001

La audiencia por si sola no gobierna la transformacion; la decision depende de un Communication Context compuesto.

### BR-002

El nivel de abstraccion y la densidad informativa pueden variar segun el contexto comunicativo, siempre que el significado permanezca equivalente.

### BR-003

La terminologia, la secuencia narrativa y la estructura documental pueden cambiar si y solo si no se altera la equivalencia semantica.

### BR-004

La visibilidad de trazabilidad no es opcional cuando afecta a la interpretacion, la auditabilidad o la decision soportada.

### BR-005

Si el Communication Context no permite determinar de forma inequívoca la forma de representacion, el flujo debe bloquearse o solicitar aclaracion antes de presentar la salida.

### BR-006

La transformacion de representacion debe permanecer como responsabilidad de Presentation Layer o de su funcion de materializacion adyacente, no como capa de conocimiento o recomendacion.

---

## 11. Constraints

- esta specification es documental y no ejecutable;
- no define subtipos adicionales para la proyeccion analitica;
- no permite que Presentation Layer decida la proyeccion por conveniencia narrativa;
- no permite que la transformacion altere el significado o la prioridad del contenido aprobado;
- no altera la Source of Truth del proyecto ni la Foundation metodologica.

---

## 12. Assumptions

- el Execution Context canonicalizado ya existe y puede declarar audiencia, proposito y decision soportada;
- la proyeccion seleccionada ya ha sido determinada por SPEC-010 y ARCH-002;
- el contenido canónico necesario para presentar ya ha sido validado por los contracts previos;
- la necesidad observada en vca-ai es suficiente para validar la transformacion de representacion, pero no para introducir capas adicionales de conocimiento o recomendacion.

---

## 13. Risks

| Risk | Impact | Notes |
|---|---|---|
| Tratar la adaptacion comunicativa como una simple variacion estilistica | Medio | Puede ocultar la necesidad de preservar equivalencia semantica y trazabilidad |
| Permitir que la transformacion modifique prioridades o conclusiones | Alto | Rompe el contenido aprobado y la boundary compliance |
| Confundir Communication Context con Execution Context | Alto | Mezcla el limite de entrada con el limite de representacion |
| Convertir la salida final en una copia tecnica de la fuente analitica | Medio | Reduce utilidad para la audiencia decisional |
| Bloquear una salida por ambiguedad no declarada | Medio | Puede ocultar la necesidad de mejorar el contexto comunicativo |

---

## 14. Acceptance Criteria

### AC-001

La specification distingue explicitamente entre la seleccion de proyeccion y la transformacion de representacion.

### AC-002

La specification establece que la transformacion depende de un Communication Context compuesto y no solo de la audiencia.

### AC-003

La specification deja explicita la equivalencia semantica como principio arquitectonico que gobierna la representacion.

### AC-004

La specification permite variar la forma de la salida sin alterar su significado aprobado.

### AC-005

La specification preserva trazabilidad hacia los artefactos fuente y mantiene visibles las limitaciones materiales.

### AC-006

La specification prohibe nueva evidencia, nuevo razonamiento, nuevas recomendaciones y cambios de prioridad durante la transformacion.

### AC-007

La specification mantiene la compatibilidad con Execution Scope Canonicalization y Presentation Projection Selection.

### AC-008

La specification define de forma explicita el flujo conceptual completo de transformacion entre Communication Context, Representation Constraints, Transformation, Semantic Equivalence Verification y Presentation Layer Output.

---

## 15. Dependencies

- project_brief.md;
- docs/context_refs.md;
- specs/spec-001-analytical-lifecycle.md;
- specs/spec-002-component-boundaries.md;
- specs/spec-004-transversal-contracts.md;
- specs/spec-010-presentation-projection-selection.md;
- docs/contracts/context.contract.md;
- docs/contracts/presentation.contract.md;
- docs/evaluations/auc-001-execution-scope-canonicalization-architectural-decision.md;
- docs/evaluations/auc-001-presentation-projection-architectural-decision.md;
- docs/evaluations/auc-001-communication-context-representation-transformation-architectural-decision.md;
- docs/handoffs/auc-001-presentation-contract.md;
- docs/handoffs/auc-001-executive-report.md;
- analytical_use_cases/meta_lead_quality_analysis.md;
- .github/skills/meta-lead-quality-analysis/SKILL.md.

---

## 16. Open Questions

- si la transformacion de representacion debe materializarse siempre como una sola forma documental por salida seleccionada o puede admitir variantes derivadas en el futuro;
- que nivel minimo de trazabilidad debe conservarse para seguir siendo util en revision y auditoria sin volver la salida excesivamente tecnica;
- si futuros casos de uso requeriran una taxonomia adicional de contextos comunicativos internos o si el contexto compuesto actual sera suficiente.

---

## 17. Future Considerations

- posible refinamiento futuro del Communication Context si aparecen nuevas dimensiones de representacion en proyectos derivados;
- posible especializacion futura de la transformacion de representacion si una nueva validacion experimental lo demuestra;
- posible extension del Presentation Contract para reflejar nuevas necesidades de representacion, sin alterar el nucleo canónico;
- posible alineamiento futuro de skills, templates y artefactos consumidores tras la validacion experimental de esta capacidad;
- Communication Context y Presentation Projection Selection son dimensiones ortogonales del framework; la evolucion futura de una de ellas no debe implicar automaticamente cambios en la otra.

---

## 18. Related Artifacts

| Artifact | Relationship |
|---|---|
| Project Brief | Define el objeto del proyecto y sus limites generales |
| SPEC-001 Analytical Lifecycle | Define el cierre del ciclo analitico y la representacion final del conocimiento ya validado |
| SPEC-002 Component Boundaries | Refuerza la separacion entre consumo de conocimiento y nueva interpretacion |
| SPEC-004 Transversal Contracts | Sostiene la existencia de contracts transversales para Knowledge, Recommendation y Presentation |
| SPEC-010 Presentation Projection Selection | Define la seleccion de proyeccion antes de la transformacion de representacion |
| Context Contract | Delimita objetivo, alcance y decision soportada |
| Presentation Contract | Delimita el contenido aprobado para presentacion |
| AUC-001 Presentation Contract | Especializa el contenido aprobado del caso AUC-001 |
| AUC-001 Executive Output Artifact | Materializa la salida ejecutiva existente |
| VCA-AUC-001-ARCH-001 | Canoniza el alcance de ejecucion previo a la presentacion |
| VCA-AUC-001-ARCH-002 | Define la separacion entre representacion analitica y ejecutiva |
| VCA-AUC-001-ARCH-003 | Define la transformacion de representacion guiada por Communication Context |

---

## Definition of Done

La specification esta completa cuando:

- la transformacion de representacion queda definida como capacidad reusable;
- la seleccion de proyeccion queda separada de la adaptacion comunicativa;
- el Communication Context queda explicitado como driver de la transformacion;
- la equivalencia semantica queda formalizada como principio arquitectonico;
- no aparece ninguna nueva responsabilidad de conocimiento o recomendacion;
- la salida conserva trazabilidad y limitaciones visibles;
- los criterios de validacion son verificables en vca-ai;
- la revision futura de artefactos consumidores queda diferida hasta la validacion experimental de la capacidad.
