# SPEC-017 - AUC-001 Diagnostico Analitico Multicapa

## Estado

Approved - Reviewer PASS. Documentary/local closure PASS.

## Fecha

2026-07-25

## Ambito

AUC-001 Meta Lead Quality Analysis.

## Titulo

Diagnostico Analitico Multicapa para AUC-001.

## Decision base

Esta Specification incorpora la specification aprobada de Diagnostico Analitico Multicapa al alcance local de AUC-001.

Especializa los criterios de profundidad analitica dentro de AUC-001. No sustituye, contradice ni modifica SPEC-014, SPEC-015, SPEC-016, Data Contract, Presentation Contract ni contratos existentes.

No autoriza implementacion, arquitectura tecnica, seleccion tecnologica, consultas BigQuery, nueva evidencia, modificacion de outputs historicos, ampliacion de fuentes, gates de ejecucion o aceptacion final ni gobernanza transversal. Un gate documental de entrada puede persistirse solo para trazar una autorizacion QA conversacional y no constituye aceptacion final ni real execution gate.

---

## 1. Proposito

Definir la capacidad minima de AUC-001 para producir diagnostico analitico multicapa sobre calidad de leads de Meta Ads.

El diagnostico debe explicar, con trazabilidad y limites visibles:

* volumen;
* calidad;
* coste;
* eficiencia;
* senales explicativas;
* evolucion;
* concentracion;
* trade-offs;
* recomendaciones trazables.

---

## 2. Boundary

### Incluye

* criterios funcionales de profundidad analitica para AUC-001;
* requisitos minimos de Knowledge Generation;
* requisitos minimos de Recommendation Generation derivados del Knowledge Set;
* reglas de suficiencia para `complete`, `partial`, `not_available`, `not_applicable`, `UNKNOWN` y `blocked`;
* criterios de aceptacion verificables.

### Excluye

* implementacion;
* arquitectura tecnica;
* seleccion tecnologica;
* consultas BigQuery;
* nueva evidencia;
* modificacion de contratos existentes;
* ampliacion de fuentes;
* gates de ejecucion, cierre o aceptacion final nuevos;
* gobernanza transversal.

---

## 3. Separacion por capa

### 3.1 Knowledge Generation

Knowledge Generation produce observaciones, comparaciones, hipotesis, conclusiones, riesgos, incertidumbres y limites interpretativos desde el Evidence Set estabilizado.

Knowledge Generation no formula acciones ni recomendaciones.

### 3.2 Recommendation Generation

Recommendation Generation transforma Knowledge estabilizado en recomendaciones accionables o hipotesis no accionables.

Recommendation Generation no introduce nueva evidencia, nuevas metricas ni nuevas hipotesis analiticas.

---

## 4. Requisitos funcionales

### FR-001 - Matriz Coste-Calidad Multicriterio

Knowledge Generation debe comparar campanas y anuncios con:

* volumen de leads;
* tasa A/B con denominador explicito;
* Tier A con denominador explicito;
* `matched_commercial_spend`;
* `cost_per_ab_commercial_matched`;
* `cost_per_tier_a_commercial_matched` si el denominador es suficiente;
* peso relativo en leads, A/B, Tier A y gasto;
* coverage `matched`, `lead_only`, `spend_only` o `UNKNOWN`;
* suficiencia de muestra.

Las metricas genericas solo son aceptables si se anclan explicitamente a metricas canonicas o a una equivalencia documentada con universo, denominador y coverage.

### FR-002 - Analisis Temporal Granular

Knowledge Generation debe analizar fluctuaciones semanales comparables, anomalias y cambios de tendencia cuando exista evidencia suficiente.

Las lecturas de aprendizaje, fatiga o asociacion observable de piezas recientes solo pueden formularse como hipotesis observables condicionadas por evidencia comparable, metadata, comparabilidad y soporte suficiente.

No se permite causalidad creativa.

Si falta evidencia comparable, se debe declarar `UNKNOWN`, `not_available` o `partial` segun corresponda.

### FR-003 - Trade-Off Volumen-Calidad-Coste

Knowledge Generation debe cuantificar ganancias o perdidas al mover foco entre campanas, anuncios, capas o segmentos mediante variacion estimada o hipotetica condicionada por evidencia.

La lectura debe cubrir volumen, tasa A/B o Tier A, `cost_per_ab_commercial_matched` o `cost_per_tier_a_commercial_matched`, riesgo de perdida de escala y condicion de revision.

### FR-004 - Concentracion y Dependencia

Knowledge Generation debe medir peso relativo en leads, A/B, Tier A y `matched_commercial_spend`.

Debe declarar riesgo cuando una unidad dominante pueda afectar materialmente el resultado si pierde rendimiento.

### FR-005 - Localizacion del Ruido C/D

Knowledge Generation debe localizar ruido C/D por anuncio, campana, capa, intencion declarada, madurez temporal y audiencia cuando exista evidencia.

Si falta cobertura, debe declarar insuficiencia, `not_available`, `UNKNOWN` o `not_applicable`.

### FR-006 - Cruces Explicativos con Inversion

Knowledge Generation debe cruzar billetes, madurez, campanas, anuncios y capas como asociaciones observables no causales.

### FR-007 - Contraste de Hipotesis Alternativas

Knowledge Generation debe contrastar, cuando aplique, hipotesis alternativas como retargeting frente a intencion madura, muestra baja, creatividad no causal, trafico frio y mezcla interna.

Las hipotesis no resolubles deben quedar como `UNKNOWN` u observacionales.

### FR-008 - Recomendaciones Evaluables

Recommendation Generation debe derivar recomendaciones exclusivamente desde el Knowledge Set estabilizado.

Cada recomendacion debe incluir:

* prioridad;
* impacto estimado o hipotetico condicionado por evidencia;
* metrica de exito;
* guardrail;
* confianza;
* condicion de revision.

---

## 5. Criterios minimos de profundidad

Un diagnostico AUC-001 conforme debe:

* comparar al menos dos dimensiones relevantes cuando existan;
* declarar denominador, coverage y muestra;
* distinguir volumen bruto de calidad util;
* usar `matched_commercial_spend`, `cost_per_ab_commercial_matched` y `cost_per_tier_a_commercial_matched` cuando trate eficiencia;
* preservar `matched`, `lead_only`, `spend_only` y `UNKNOWN`;
* separar observacion, interpretacion, hipotesis y recomendacion;
* identificar trade-off;
* declarar limites cerca de la conclusion afectada;
* evitar causalidad;
* conservar `UNKNOWN`, `not_available` y `not_applicable`.

---

## 6. Estados y marcadores

### Estados

| Estado | Uso |
|---|---|
| `complete` | La lectura cumple evidencia, comparacion, denominador, coverage, muestra, interpretacion y limites. |
| `partial` | Existe lectura util, pero falta granularidad, coverage, muestra, comparabilidad o profundidad. |
| `not_available` | La fuente, dimension, metrica o granularidad no esta disponible en el boundary autorizado. |
| `not_applicable` | La lectura no corresponde al periodo, fuente, boundary o decision analitica. |
| `UNKNOWN` | La evidencia existe o es parcial, pero no permite concluir con seguridad. |
| `blocked` | Una pregunta obligatoria critica no puede evaluarse sin inferencia prohibida o ruptura contractual. |

### Marcadores

| Marcador | Uso |
|---|---|
| `low_sample` | El denominador o volumen no sostiene una conclusion robusta. |
| `not_comparable` | La comparacion no es valida por periodo, universo, coverage, muestra o granularidad. |
| `missing_dimension` | Falta una dimension necesaria para resolver la lectura. |
| `coverage_limited` | La cobertura limita interpretacion, recomendacion o comparabilidad. |

---

## 7. Matriz de trazabilidad

| Gap formalizado | FR | Acceptance Criteria |
|---|---|---|
| Gap coste-calidad | FR-001 | AC-003 |
| Temporalidad | FR-002 | AC-004, AC-011 |
| Trade-off | FR-003 | AC-005 |
| Concentracion | FR-004 | AC-006 |
| Ruido C/D | FR-005 | AC-007 |
| Cruces senal-inversion | FR-006 | AC-008 |
| Hipotesis alternativas | FR-007 | AC-009 |
| Recomendaciones evaluables | FR-008 | AC-010 |

---

## 8. Criterios de aceptacion

### AC-001 - Scope local

La specification queda limitada a AUC-001 y no redefine contracts, fuentes, gates ni gobernanza transversal.

### AC-002 - Ocho gaps formalizados

Los ocho gaps analiticos quedan formalizados como requisitos funcionales verificables.

### AC-003 - Matriz coste-calidad canonica

La matriz coste-calidad usa metricas canonicas, denominadores, coverage y muestra suficiente o declara limitacion.

### AC-004 - Temporalidad comparable sin causalidad creativa

La temporalidad se analiza solo con comparabilidad suficiente y no afirma causalidad creativa.

### AC-005 - Trade-offs estimados o hipoteticos

Los trade-offs volumen-calidad-coste se expresan con variacion estimada o hipotetica condicionada por evidencia.

### AC-006 - Concentracion por leads, A/B, Tier A y spend

La concentracion declara peso relativo por leads, A/B, Tier A y `matched_commercial_spend`.

### AC-007 - Ruido localizado o insuficiencia declarada

El ruido C/D queda localizado por las capas disponibles o se declara insuficiencia de cobertura.

### AC-008 - Cruces visibles no causales

Los cruces explicativos con inversion se presentan como asociaciones observables no causales.

### AC-009 - Hipotesis alternativas contrastadas

Las hipotesis alternativas se contrastan y las no resolubles permanecen `UNKNOWN` u observacionales.

### AC-010 - Recomendaciones con estructura evaluable

Cada recomendacion incluye prioridad, impacto, metrica, guardrail, confianza y condicion de revision.

### AC-011 - Estados para fatiga, aprendizaje y temporalidad

Fatiga, aprendizaje y temporalidad admiten `UNKNOWN`, `not_available`, `partial` o `not_applicable` cuando la evidencia no permite conclusion completa.

### AC-012 - Sin ampliacion de alcance

La specification no introduce implementacion, arquitectura, fuentes, gates ni gobernanza transversal.

---

## 9. Dependencias

| Artefacto | Relacion |
|---|---|
| AUC-001 Analytical Contract | Fuente local de preguntas, limites y capacidades analiticas. |
| SPEC-012 | Fuente de metricas canonicas de coste-calidad. |
| SPEC-013 | Fuente de preservacion de universos reconciliados y coverage states. |
| SPEC-014 | Contrato de suficiencia del producto analitico. |
| SPEC-015 | Contrato de Canonical Projection Source y proyecciones hermanas. |
| SPEC-016 | Contrato operativo del execution package. |
| Data Contract | Fuente de tablas, campos y proveedor autorizado. |
| Presentation Contract | Fuente de invariantes de representacion. |
| `.github/skills/meta-lead-quality-analysis/ANALYTICAL_PROFILE.md` | Guia operativa de preguntas y criterios de calidad analitica. |
| `.github/skills/meta-lead-quality-analysis/knowledge-construction-profile.md` | Guia interna de construccion de Knowledge. |

---

## 10. No objetivos

Esta specification no pretende:

* validar una ejecucion analitica;
* producir informes;
* adquirir evidencia;
* modificar SPEC-014, SPEC-015 o SPEC-016;
* modificar Data Contract o Presentation Contract;
* cambiar fuentes autorizadas;
* crear gates de ejecucion, cierre o aceptacion final;
* implementar runtime;
* alterar outputs historicos.

---

## 11. Readiness para Reviewer/QA

Reviewer Agent debe comprobar coherencia documental, boundary local, trazabilidad de FR a AC, separacion de capas y ausencia de contradiccion con SPEC-014, SPEC-015 y SPEC-016.

QA Gate Agent debe comprobar que los artefactos operativos/documentales de AUC-001 referencian esta specification sin declarar aceptacion final de una ejecucion, sin adquirir evidencia y sin modificar outputs historicos.

---

## Definition of Done

La specification queda incorporada cuando:

* existe como artefacto versionado local de AUC-001;
* esta referenciada desde el indice oficial de contexto;
* esta referenciada desde los artefactos operativos de la skill AUC-001;
* el Checklist permite verificar sus criterios antes de Presentation;
* existe handoff para Reviewer/QA;
* no se han modificado SPEC-014, SPEC-015, SPEC-016 ni outputs historicos.
