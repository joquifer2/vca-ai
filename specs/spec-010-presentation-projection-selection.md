# Specification

## Metadata

### Spec ID

SPEC-010

### Title

Presentation Projection Selection

### Status

Draft

### Owner

Equipo VCA

### Last Updated

2026-07-13

---

## 1. Purpose

Definir la capacidad minima y verificable para seleccionar y materializar una proyeccion de presentacion en vca-ai a partir de un Execution Context canonicalizado.

Esta specification no introduce subtipos internos de la proyeccion analitica.

Esta specification no modifica AIF Foundation.

---

## 2. Background

La decision arquitectonica VCA-AUC-001-ARCH-001 establecio la necesidad de canonicalizar el alcance de ejecucion antes de congelar un Execution Context.

La decision arquitectonica VCA-AUC-001-ARCH-002 mostro que Presentation Layer debe producir dos representaciones paralelas del mismo contenido validado: una proyeccion analitica y una proyeccion ejecutiva.

La evidencia observada en vca-ai no demuestra todavia una necesidad independiente para subdividir la proyeccion analitica en modos adicionales. Por tanto, esta specification formaliza solo la distincion minima respaldada por evidencia: proyeccion analitica frente a proyeccion ejecutiva.

---

## 3. Objective

Esta capacidad debe conseguir que, dado un Execution Context canonicalizado, vca-ai seleccione de forma deterministica la proyeccion de presentacion adecuada para la audiencia, el proposito y el tipo de decision soportada.

El resultado debe permitir materializar una salida trazable sin introducir nuevo razonamiento, sin derivar una salida desde otra y sin reintroducir evidencia, prioridades o conclusiones no aprobadas.

---

## 4. Scope

### Included

- seleccion de proyeccion de presentacion a partir del Execution Context canonicalizado;
- distincion minima entre proyeccion analitica y proyeccion ejecutiva;
- consumo del mismo contenido canonico aprobado por ambas proyecciones;
- reglas para preservar trazabilidad, cobertura, limitaciones y restricciones materiales;
- criterios para impedir nuevo razonamiento, divergencia semantica y derivacion secuencial entre salidas.

### Excluded

- subdivision adicional de la proyeccion analitica en esta iteracion;
- modificaciones a AIF Foundation;
- diseno tecnico ejecutable de interfaces o renderers;
- nueva adquisicion de datos, nueva evidencia o nueva interpretacion;
- generacion de Tasks.

---

## 5. Actors

| Actor | Description |
|---|---|
| Framework | Canonicaliza el contexto y valida que la seleccion de proyeccion sea consistente con el alcance aprobado |
| Context Definition | Define objetivo, audiencia, proposito, decision soportada y restricciones iniciales |
| Execution Context | Congela la instancia de ejecucion y declara la proyeccion seleccionada |
| Presentation Layer | Materializa la proyeccion seleccionada sin decidirla ni reinterpretarla |
| Analytical Projection Consumer | Consume la representacion analitica para revision, auditoria o validacion metodologica |
| Executive Projection Consumer | Consume la representacion ejecutiva para lectura decisional y comunicacion de negocio |
| Reviewer | Verifica coherencia, trazabilidad y ausencia de nuevo razonamiento |

---

## 6. Inputs

| Input | Description |
|---|---|
| Context Definition | Objetivo, audiencia, proposito, decision soportada y restricciones declaradas |
| Execution Scope Canonicalization Result | Alcance de ejecucion resuelto y congelado antes de la presentacion |
| Knowledge Set | Insights, conclusiones, riesgos e incertidumbres ya validados |
| Recommendation Set | Acciones sugeridas aprobadas y priorizadas |
| Presentation Contract | Contenido aprobado que puede consumirse para construir la salida |
| Output Request | Solicitud de salida que declara la proyeccion requerida o la necesidad de bloqueo |

---

## 7. Outputs

| Output | Description |
|---|---|
| Presentation Mode | Modo de salida seleccionado: Analytical o Executive |
| Selected Presentation Projection | Proyeccion de presentacion materializada segun el Execution Context canonicalizado |
| Traceable Output | Salida final con referencias suficientes a artefactos fuente |
| Boundary Status | Indicacion de que no se introdujo nueva evidencia, interpretacion ni priorizacion |

---

## 8. Functional Requirements

### FR-001

La capacidad experimental en vca-ai debe distinguir como minimo entre una proyeccion analitica y una proyeccion ejecutiva.

### FR-002

La seleccion de la proyeccion debe derivarse del Execution Context canonicalizado y no de una decision ad hoc de Presentation Layer.

### FR-003

Presentation Layer debe materializar unicamente la proyeccion seleccionada.

### FR-004

Ambas proyecciones deben consumir el mismo contenido canonico aprobado y trazable.

### FR-005

Ninguna proyeccion puede introducir nueva evidencia, nuevo razonamiento, nuevas recomendaciones o cambios de prioridad.

### FR-006

La salida ejecutiva debe permanecer sintetica y no convertirse en un informe tecnico completo.

### FR-007

La salida analitica debe preservar el detalle necesario para revision, auditoria o validacion metodologica sin crear subdivisiones adicionales no respaldadas por evidencia.

---

## 9. Business Rules

### BR-001

La audiencia, el proposito y el tipo de decision soportada gobiernan la seleccion de proyeccion.

### BR-002

Si el Execution Context canonicalizado no permite determinar de forma inequívoca la proyeccion, el flujo debe bloquearse o solicitar aclaracion antes de presentar la salida.

### BR-003

La proyeccion analitica y la proyeccion ejecutiva deben permanecer como representaciones hermanas del mismo contenido validado, no como una cadena secuencial.

### BR-004

La trazabilidad debe preservarse en ambas proyecciones, pero la densidad de detalle puede variar segun la audiencia y el proposito.

### BR-005

Cualquier especializacion futura de la proyeccion analitica debe tratarse como una futura consideration, no como una capacidad vigente.

---

## 10. Constraints

- esta specification es documental y no ejecutable;
- no define subtipos adicionales para la proyeccion analitica;
- no permite que Presentation Layer decida la proyeccion por conveniencia narrativa;
- no permite que el Executive Report herede la estructura tecnica completa de la salida analitica;
- no altera la Source of Truth del proyecto ni la Foundation metodologica.

---

## 11. Assumptions

- el Execution Context canonicalizado ya existe y puede declarar audiencia, proposito y decision soportada;
- el contenido canonico necesario para presentar ya ha sido validado por los contracts previos;
- la necesidad observada en vca-ai es suficiente para validar la distincion minima entre representacion analitica y ejecutiva, pero no para introducir submodos analiticos adicionales.

---

## 12. Risks

| Risk | Impact | Notes |
|---|---|---|
| Introducir subtipos analiticos prematuros | Alto | Puede fijar una taxonomia no respaldada por evidencia experimental |
| Permitir que Presentation Layer elija la proyeccion ad hoc | Alto | Rompe la canonicalizacion del contexto y la trazabilidad de la decision |
| Convertir la salida ejecutiva en una copia tecnica | Medio | Reduce utilidad para audiencia decisional y aumenta ruido documental |
| Bloquear una salida por ambiguedad no declarada | Medio | Puede ocultar necesidad de mejorar el contexto canonicalizado |

---

## 13. Acceptance Criteria

### AC-001

La specification distingue explicitamente entre proyeccion analitica y proyeccion ejecutiva como unica particion normativamente respaldada.

### AC-002

La specification establece que la seleccion de proyeccion depende del Execution Context canonicalizado y no de una decision libre de Presentation Layer.

### AC-003

La specification prohibe cualquier subdivision adicional no sustentada por evidencia observada en vca-ai.

### AC-004

La specification deja trazabilidad entre Context Definition, Execution Context, Presentation Contract y la salida materializada.

### AC-005

La specification preserva la posibilidad de evolucionar la proyeccion analitica en el futuro sin convertir esa evolucion en un requisito actual.

---

## 14. Dependencies

- project_brief.md;
- docs/context_refs.md;
- specs/spec-001-analytical-lifecycle.md;
- specs/spec-002-component-boundaries.md;
- specs/spec-004-transversal-contracts.md;
- docs/contracts/context.contract.md;
- docs/contracts/presentation.contract.md;
- docs/evaluations/auc-001-presentation-projection-architectural-decision.md;
- docs/evaluations/auc-001-execution-scope-canonicalization-architectural-decision.md;
- docs/handoffs/auc-001-presentation-contract.md;
- docs/handoffs/auc-001-executive-report.md;
- analytical_use_cases/meta_lead_quality_analysis.md;
- .github/skills/meta-lead-quality-analysis/SKILL.md.

---

## 15. Open Questions

- si la salida analitica debe materializarse siempre como un unico formato documental o puede adoptar formatos derivados en iteraciones futuras;
- que nivel de detalle minimo debe conservarse en la salida ejecutiva para seguir siendo trazable sin volverse tecnica;
- si el framework necesitara en el futuro una taxonomia adicional solo para revisiones internas de la salida analitica.

---

## 16. Future Considerations

- posible especializacion futura de la proyeccion analitica si aparece evidencia adicional en vca-ai o en proyectos derivados;
- posible descomposicion documental de la salida analitica en una vista o informe solo si una nueva validacion experimental lo demuestra;
- posible extension del Presentation Contract para reflejar nuevas necesidades de representacion, sin alterar el nucleo canónico.

---

## 17. Related Artifacts

| Artifact | Relationship |
|---|---|
| Project Brief | Define el objeto del proyecto y sus limites generales |
| SPEC-001 Analytical Lifecycle | Define la fase final de presentacion y el cierre del ciclo analitico |
| SPEC-002 Component Boundaries | Define la separacion de responsabilidades entre capas |
| SPEC-004 Transversal Contracts | Define el marco comun de contracts |
| Context Contract | Delimita objetivo, alcance y decision soportada |
| Presentation Contract | Delimita el contenido aprobado para presentacion |
| AUC-001 Presentation Contract | Especializa el contenido aprobado del caso AUC-001 |
| AUC-001 Executive Output Artifact | Materializa la salida ejecutiva existente |
| VCA-AUC-001-ARCH-001 | Canoniza el alcance de ejecucion previo a la presentacion |
| VCA-AUC-001-ARCH-002 | Define la separacion entre representacion analitica y ejecutiva |

---

## Definition of Done

La specification esta completa cuando:

- la seleccion de proyeccion depende del Execution Context canonicalizado;
- la distincion entre proyeccion analitica y proyeccion ejecutiva queda explicitada;
- no aparece ninguna subdivision adicional de la proyeccion analitica como capacidad vigente;
- la salida ejecutiva no se convierte en un informe tecnico;
- la salida analitica mantiene el detalle necesario sin introducir subdivisiones no respaldadas por evidencia;
- la trazabilidad y las limitaciones permanecen visibles;
- los criterios de validacion son verificables en vca-ai;
- la especializacion futura de la proyeccion analitica queda pospuesta expresamente.