# Specification

## Metadata

### Spec ID

SPEC-001

### Title

Analytical Lifecycle

### Status

Draft

### Owner

Foundation maintainers

### Last Updated

2026-07-10

---

## 1. Purpose

Definir el ciclo de vida analitico comun que toda implementacion derivada de AIF debe seguir para transformar contexto y datos en conocimiento accionable.

---

## 2. Background

El Project Brief establece que la Foundation debe formalizar el proceso de razonamiento analitico y evitar que los informes condicionen el analisis. Esta specification concreta ese proceso como una secuencia reusable de fases con criterios de avance claros.

---

## 3. Objective

Esta capacidad debe conseguir que cualquier analisis basado en la Foundation siga una metodologia unica, trazable y verificable desde la definicion del contexto hasta la generacion del artefacto final.

El resultado debe ser un marco comun que separe preparacion, evidencia, razonamiento y presentacion sin depender de dominio ni tecnologia concretos.

---

## 4. Scope

### Included

- definicion de las fases 0 a 6 del ciclo analitico;
- definicion de entradas y salidas esperadas por fase;
- definicion de criterios minimos de progresion entre fases;
- reglas metodologicas para preservar separacion entre evidencia, conocimiento y artefactos de salida.

### Excluded

- implementacion tecnica de orquestacion o runtime;
- definicion detallada de contratos de datos concretos;
- reglas de negocio o metrica especifica de una Skill;
- automatizacion operativa de ejecucion de fases.

---

## 5. Actors

| Actor | Description |
| --- | --- |
| Framework | Coordina el ciclo analitico y valida el cierre metodologico de cada fase |
| Data Provider | Expone datos mediante contratos estandarizados sin imponer logica de analisis |
| Analytical Routines | Ejecutan transformaciones y analisis para producir evidencia |
| Reasoning Routines | Transforman evidencia en insights, hipotesis y recomendaciones |
| Template Builder | Convierte conocimiento ya generado en artefactos de salida |
| Skill Author | Extiende reglas, metricas o interpretaciones de dominio sin alterar el ciclo comun |

---

## 6. Inputs

| Input | Description |
| --- | --- |
| Analysis Objective | Proposito del analisis, decision a soportar y restricciones declaradas |
| Context References | Fuentes oficiales de contexto relevantes para el analisis |
| Data Provider Contract | Estructura estandarizada para adquirir datos desde una fuente externa |
| Skill Knowledge | Reglas y definiciones de dominio aportadas por Skills cuando aplique |
| Output Request | Tipo de artefacto final solicitado sin alterar el proceso analitico |

---

## 7. Outputs

| Output | Description |
| --- | --- |
| Context Definition | Objetivo, restricciones y decision soportada definidos para el analisis |
| Discovery Model | Descripcion logica de datasets, entidades, relaciones, metricas y limitaciones |
| Analytical Model | Datos preparados para analisis bajo un modelo coherente |
| Evidence Set | Hallazgos observables obtenidos del analisis |
| Knowledge Set | Insights, hipotesis priorizadas y conclusiones respaldadas por evidencia |
| Recommendation Set | Acciones sugeridas con impacto, esfuerzo, dependencias y riesgos |
| Output Artifact | Representacion final del conocimiento en el formato requerido |

---

## 7.1 Phase Definitions

### Phase 0. Contexto

**Objective**

Delimitar el analisis antes de tocar datos o producir interpretaciones.

**Expected Activities**

- definir el objetivo del analisis y la decision a soportar;
- identificar restricciones, supuestos y criterios de relevancia;
- confirmar las fuentes oficiales de contexto y su jerarquia.

**Primary Outputs**

- Context Definition;
- lista de fuentes de contexto aplicables.

**Transition Criteria**

Solo puede avanzarse a Discovery cuando el objetivo, las restricciones y las fuentes oficiales de contexto hayan quedado explicitados.

**Definition of Done**

El analisis tiene una finalidad declarada, un alcance delimitado y un marco de contexto verificable.

### Phase 1. Discovery

**Objective**

Entender la estructura logica del espacio de datos y sus limitaciones antes de preparar informacion para analisis.

**Expected Activities**

- identificar datasets, entidades, dimensiones, metricas y relaciones relevantes;
- registrar supuestos, vacios y limitaciones observadas en la fuente de datos;
- delimitar que porcion del espacio de datos sera util para el objetivo definido.

**Primary Outputs**

- Discovery Model.

**Transition Criteria**

Solo puede avanzarse a Preparacion cuando existe una descripcion logica suficiente del espacio de datos y sus limitaciones.

**Definition of Done**

Quedan documentados los elementos de datos relevantes, sus relaciones principales y las restricciones que condicionan el analisis.

### Phase 2. Preparacion

**Objective**

Transformar los datos identificados en un modelo analitico coherente y apto para producir evidencia.

**Expected Activities**

- consolidar, normalizar o derivar estructuras necesarias para el analisis;
- validar integridad, coherencia y suficiencia minima de los datos preparados;
- dejar explicitas las transformaciones que afectan a la interpretacion posterior.

**Primary Outputs**

- Analytical Model.

**Transition Criteria**

Solo puede avanzarse a Analisis cuando el modelo preparado es coherente con el objetivo, interpretable y utilizable sin ambiguedad material.

**Definition of Done**

Existe un modelo analitico estable, entendible y con validaciones minimas suficientes para producir evidencia.

### Phase 3. Analisis

**Objective**

Producir evidencia observable a partir del modelo analitico preparado.

**Expected Activities**

- explorar patrones, comparaciones, distribuciones, anomalias o tendencias;
- aislar hallazgos observables sin convertirlos todavia en conclusiones;
- registrar limites de lectura, huecos y sensibilidad de los hallazgos.

**Primary Outputs**

- Evidence Set.

**Transition Criteria**

Solo puede avanzarse a Razonamiento cuando existe evidencia suficiente para sostener interpretaciones sin inventar hechos no observados.

**Definition of Done**

Los hallazgos observables estan estructurados, trazables y separados de cualquier interpretacion o recomendacion.

### Phase 4. Razonamiento

**Objective**

Transformar evidencia en conocimiento explicito, manteniendo la trazabilidad entre hechos e interpretacion.

**Expected Activities**

- convertir evidencia en insights, hipotesis, oportunidades y riesgos;
- priorizar interpretaciones segun relevancia para la decision soportada;
- declarar incertidumbres, conflictos o estados UNKNOWN cuando la evidencia no sea concluyente.

**Primary Outputs**

- Knowledge Set.

**Transition Criteria**

Solo puede avanzarse a Recomendaciones cuando las interpretaciones estan respaldadas por evidencia identificable y las incertidumbres han sido declaradas.

**Definition of Done**

Existe un conjunto de conocimiento estructurado, trazable y diferenciado de la evidencia original.

### Phase 5. Recomendaciones

**Objective**

Convertir el conocimiento priorizado en acciones sugeridas, justificadas y evaluables.

**Expected Activities**

- formular acciones sugeridas alineadas con el objetivo del analisis;
- justificar impacto esperado, esfuerzo, dependencias y riesgos;
- explicitar la relacion entre cada recomendacion y la evidencia o insight que la respalda.

**Primary Outputs**

- Recommendation Set.

**Transition Criteria**

Solo puede avanzarse a Constructor de Informes cuando cada recomendacion tiene justificacion, trazabilidad y nivel de confianza declarado.

**Definition of Done**

Las recomendaciones son accionables, priorizadas y trazables al conocimiento y evidencia que las sustentan.

### Phase 6. Constructor de Informes

**Objective**

Representar conocimiento y recomendaciones ya validados metodologicamente en el formato de salida requerido.

**Expected Activities**

- seleccionar la estructura de salida adecuada sin alterar el contenido analitico;
- transformar conocimiento y recomendaciones en un artefacto legible;
- verificar que el formato no omite evidencia, incertidumbre ni trazabilidad relevante.

**Primary Outputs**

- Output Artifact.

**Transition Criteria**

Esta es la fase final del ciclo. No puede reabrir fases previas salvo que se detecte una inconsistencia metodologica explicita.

**Definition of Done**

El artefacto final presenta el conocimiento ya generado sin introducir nueva evidencia, nueva interpretacion ni nuevas recomendaciones.

---

## 8. Functional Requirements

### FR-001

La Foundation debe definir un ciclo de vida comun compuesto por las fases Contexto, Discovery, Preparacion, Analisis, Razonamiento, Recomendaciones y Constructor de Informes.

### FR-002

Cada fase debe declarar objetivo, actividades esperadas y Definition of Done minimo antes de permitir el avance a la siguiente fase.

### FR-003

La fase de Discovery debe identificar datasets, entidades, dimensiones, metricas, relaciones y limitaciones relevantes antes de preparar los datos.

### FR-004

La fase de Preparacion debe producir un modelo analitico consistente y apto para analisis, incluyendo validacion de integridad y metricas derivadas cuando correspondan.

### FR-005

La fase de Analisis debe generar evidencia suficiente para sustentar razonamiento posterior, incluyendo patrones, comparaciones, anomalias o distribuciones segun el caso.

### FR-006

La fase de Razonamiento debe transformar la evidencia en conocimiento explicitando insights, hipotesis, oportunidades, riesgos y prioridades.

### FR-007

La fase de Recomendaciones debe producir acciones priorizadas y justificar al menos que hacer, por que, impacto esperado, esfuerzo requerido, dependencias y riesgos.

### FR-008

La fase de Constructor de Informes solo puede ejecutarse cuando el conocimiento ya ha sido generado y validado metodologicamente.

---

## 9. Business Rules

### BR-001

El analisis siempre precede al informe. Ningun formato de salida puede redefinir ni omitir fases analiticas obligatorias.

### BR-002

La evidencia precede a las conclusiones. Si la evidencia es insuficiente, la salida debe indicarlo de forma explicita.

### BR-003

Los hechos, las evidencias, los insights, las hipotesis y las recomendaciones deben mantenerse como categorias separadas.

### BR-004

Las Skills pueden enriquecer el contenido de una fase, pero no eliminar ni alterar la secuencia metodologica comun.

---

## 10. Constraints

- esta specification debe permanecer independiente de tecnologia, proveedor o runtime;
- no debe introducir automatizacion ejecutable ni implementacion productiva;
- no debe incorporar conocimiento de dominio dentro del nucleo comun;
- las definiciones deben ser aplicables a proyectos derivados con diferentes fuentes de datos.

---

## 11. Assumptions

- existe una necesidad recurrente de reutilizar un mismo proceso analitico en distintos dominios;
- los proyectos derivados dispondran de contratos o estructuras equivalentes para adquirir datos;
- la suficiencia de evidencia podra evaluarse con criterios mas concretos en specs o gates posteriores.

---

## 12. Risks

| Risk | Impact | Notes |
| --- | --- | --- |
| Definir fases demasiado abstractas | Medio | Puede dificultar implementacion consistente en proyectos derivados |
| Permitir atajos entre fases | Alto | Rompe trazabilidad y reduce auditabilidad |
| No formalizar que significa evidencia suficiente | Alto | Debilita la calidad del razonamiento posterior |

---

## 13. Acceptance Criteria

### AC-001

La specification documenta las siete fases del ciclo y el objetivo de cada una.

### AC-002

La specification deja explicito que el reporte es una fase final de presentacion y no un sustituto del razonamiento.

### AC-003

La specification define reglas suficientes para impedir la mezcla entre evidencia, interpretacion y recomendacion.

---

## 14. Dependencies

- project_brief.md;
- docs/context_refs.md;
- spec-004-transversal-contracts.md;
- spec-005-readiness-gates.md;
- spec-006-documentary-evaluations.md.

---

## 15. Open Questions

- que gates concretos convendria instanciar por fase o por bloque del ciclo;
- que nivel de granularidad deben tener los contratos de evidencia y conocimiento;
- como se medira de forma reusable la suficiencia de evidencia en distintos dominios.

---

## 16. Future Considerations

- instanciar contracts transversales alineados con SPEC-004 cuando una fase requiera mayor formalizacion de handoff;
- crear gates de readiness por fase o por bloque del ciclo analitico usando SPEC-005 cuando el alcance lo requiera;
- crear evaluaciones documentales alineadas con SPEC-006 para verificar trazabilidad entre evidencia y recomendaciones.

---

## 17. Related Artifacts

| Artifact | Relationship |
| --- | --- |
| project_brief.md | Define el proposito y alcance de la Foundation |
| docs/context_refs.md | Fuente oficial de contexto utilizada para esta spec |
| spec-002-component-boundaries.md | Define limites y handoffs entre componentes que ejecutan el ciclo |
| spec-003-extensibility-model.md | Define como extender el ciclo mediante Skills, Routines y Templates |
| spec-004-transversal-contracts.md | Define contracts transversales que soportan los handoffs entre fases |
| spec-005-readiness-gates.md | Define gates reutilizables para validar avance y suficiencia documental |
| spec-006-documentary-evaluations.md | Define evaluaciones documentales que pueden medir suficiencia de evidencia |

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