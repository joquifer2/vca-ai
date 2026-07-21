# AUC-001-P02 Analytical Product Contract Implementation Task Plan

## Metadatos

| Campo | Valor |
| --- | --- |
| Artifact ID | TASK-PLAN-AUC-001-P02-ANALYTICAL-PRODUCT-CONTRACT-IMPLEMENTATION |
| Caso de uso | AUC-001 - Meta Lead Quality Analysis |
| Fase | AUC-001-P02 |
| Fuente normativa | `specs/spec-014-auc-001-analytical-product-contract.md` |
| Gate precedente | `gates/auc-001-p01-documentary-closure-gate.md` |
| Agente | Tasks Planner Agent |
| Creado | 2026-07-21 |
| Estado | Ready for Entry Gate review |
| Entry Gate | No creado en este plan |
| BigQuery | No ejecutado |
| Implementacion | No ejecutada |
| Outputs | No generados |

---

## 1. Estado real reconstruido

El estado real del repositorio para AUC-001 es:

- El ciclo experimental original de AUC-001 permanece cerrado con `READY FOR CLOSURE`.
- P0 fue cerrado tras PCI-002 con `P0 PASS WITH RESIDUAL OBSERVATIONS - READY FOR P01`.
- PCI-002 dejo disponible un runtime output fisico consumible para el objetivo de reconciliacion estructurada de SPEC-013.
- P01 fue cerrado documentalmente por QA Gate Agent con `PASS`.
- SPEC-014 esta cerrada como contrato aprobado de producto analitico para AUC-001.
- El estado canonico vigente es `AUC-001-P01 DOCUMENTARY CLOSURE PASS - READY FOR CONTROLLED POST-P01 IMPLEMENTATION PLANNING`.
- P02 no esta autorizado para ejecucion hasta que un Entry Gate posterior lo apruebe.

Este plan traduce exclusivamente requisitos aprobados de SPEC-014 en tareas implementables, ordenadas, trazables y verificables. No usa informes historicos como expected values, no incorpora conocimiento analitico nuevo y no modifica el contrato aprobado.

---

## 2. Objetivo de P02

Preparar la implementacion controlada del Contrato de Producto Analitico de AUC-001 definido en SPEC-014, de forma que futuras ejecuciones puedan producir productos conformes con:

- matriz de cobertura por pregunta, criticidad y estado;
- vistas analiticas requeridas o equivalentes;
- profundidad minima verificable por pregunta obligatoria;
- tratamiento explicito de `UNKNOWN`, `not_available`, `partial`, `not_applicable` y `blocked`;
- regla minima de robustez y suficiencia de muestra;
- nucleo comun de producto y proyecciones analitica y ejecutiva semanticamente equivalentes;
- recomendaciones clasificadas como `measurable_experiment`, `verifiable_action` o `non_actionable_hypothesis`;
- tratamiento contractual de `ad_name`, `ticket_status` y evolucion temporal cuando correspondan.

---

## 3. Boundary

Incluido en P02:

- planificar cambios de runtime o contratos estructurados necesarios para expresar el Product Contract;
- planificar la generacion futura de Evidence, Knowledge y Recommendations conforme a SPEC-014;
- planificar la construccion futura de informes analitico y ejecutivo desde un nucleo comun;
- planificar pruebas, validaciones locales y handoffs QA;
- planificar documentacion minima para trazabilidad.

Fuera de P02 en este artefacto:

- implementar codigo;
- ejecutar BigQuery o BigQuery MCP;
- generar Evidence Sets, Knowledge Sets, Recommendation Sets, reports u outputs;
- abrir Entry Gate, Exit Gate o cualquier otro gate;
- modificar outputs historicos;
- usar outputs historicos como valores esperados;
- ampliar fuentes, metricas o reglas fuera de SPEC-014.

---

## 4. Dependencias

| Dependencia | Tipo | Estado requerido antes de ejecutar P02 |
| --- | --- | --- |
| SPEC-014 | Normativa | Cerrada y aprobada con P01 Documentary Closure PASS. |
| P01 Documentary Closure Gate | Gobernanza | PASS. |
| SPEC-012 | Modelo coste-calidad | Disponible para metricas canonicas de coste-calidad. |
| SPEC-013 | Salida estructurada de reconciliacion | Disponible para cobertura `matched`, `lead_only`, `spend_only` y `UNKNOWN`. |
| Analytical Contract AUC-001 | Contrato analitico | Vigente como fuente de preguntas y restricciones analiticas. |
| Evidence Contract | Contrato transversal | Vigente para hechos, cobertura y trazabilidad. |
| Knowledge Contract | Contrato transversal | Vigente para separacion evidencia/conocimiento. |
| Recommendation Contract | Contrato transversal | Vigente para acciones trazables y evaluables. |
| Presentation Contract | Contrato transversal | Vigente para proyecciones sin nuevo conocimiento. |
| AUC-001 Runbook | Operativo | Obligatorio para cualquier ejecucion posterior que adquiera evidencia. |
| BigQuery MCP Server | Data Provider | Solo requerido en fases posteriores con evidencia nueva; no requerido para este plan. |

---

## 5. Principios de traduccion desde SPEC-014

| Principio aprobado | Traduccion a tareas P02 |
| --- | --- |
| Completitud por pregunta y criticidad | Crear modelo de matriz y evaluador por AQ/CQ/NAQ, no un booleano global. |
| `not_available` no implica incumplimiento automatico | Implementar justificacion e impacto por ausencia. |
| `UNKNOWN` es resultado analitico valido | Mantenerlo separado de ausencia de fuente o dimension. |
| Vistas analiticas, no tablas literales | Implementar contratos de vista con formato equivalente permitido. |
| Profundidad minima verificable | Crear checklist por pregunta: evidencia, comparacion, interpretacion, implicacion, limitacion y conclusion/hipotesis. |
| Robustez minima | Registrar denominador, volumen, cobertura, granularidad, comparador y suficiencia antes de conclusiones. |
| Nucleo comun y proyecciones | Construir artefacto canonico comun antes de informes analitico y ejecutivo. |
| Recomendaciones clasificadas | Validar toda recomendacion accionable como experimento medible o accion verificable. |
| Residuos P0/P01 clasificados | Tratar `ad_name`, `ticket_status` y evolucion semanal segun aplicabilidad y cobertura. |

---

## 6. Plan de tareas recomendado

### 6.1 Preparacion y boundary

| ID | Tarea | Tipo | Responsable sugerido | Depende de | Resultado esperado | Evidencia de finalizacion |
| --- | --- | --- | --- | --- | --- | --- |
| P02-T001 | Confirmar Entry Gate readiness package para P02 sin abrir el gate | Planificacion | Tasks Planner Agent | SPEC-014, P01 Gate | Alcance, restricciones y dependencias listos para QA Gate Agent | Este plan revisado y referenciable |
| P02-T002 | Identificar puntos de integracion existentes para Evidence, Knowledge, Recommendations y Presentation | Analisis tecnico | Implementation Agent | P02 Entry Gate futuro | Mapa de componentes candidatos sin modificar codigo | Nota tecnica o handoff con rutas y responsabilidades |
| P02-T003 | Definir estrategia de compatibilidad con SPEC-012 y SPEC-013 | Contrato estructurado | Implementation Agent | P02-T002 | Reglas de consumo de metricas canonicas y reconciliacion estructurada | Diseño tecnico aprobado para implementacion |

### 6.2 Cambios de runtime o contratos estructurados

| ID | Tarea | Tipo | Responsable sugerido | Depende de | Resultado esperado | Evidencia de finalizacion |
| --- | --- | --- | --- | --- | --- | --- |
| P02-T010 | Implementar estructura de `analytical_product_contract` para ejecuciones AUC-001 | Runtime / contrato estructurado | Implementation Agent | P02 Entry Gate futuro, P02-T003 | Objeto estructurado con version, scope, preguntas, vistas, estados, robustez, nucleo comun y proyecciones | Tests de serializacion y schema |
| P02-T011 | Implementar matriz de cobertura integrada | Runtime / contrato estructurado | Implementation Agent | P02-T010 | Matriz por AQ/CQ/NAQ con criticidad, vista requerida, evidencia minima, interpretacion minima, recomendacion requerida y estado valido | Test de matriz completa contra IDs de SPEC-014 |
| P02-T012 | Implementar validacion de estados de cobertura | Runtime / contrato estructurado | Implementation Agent | P02-T011 | Estados permitidos: `complete`, `partial`, `not_available`, `not_applicable`, `UNKNOWN`, `blocked` con reglas diferenciadas | Tests positivos y negativos por estado |
| P02-T013 | Implementar evaluacion de completitud por pregunta y criticidad | Runtime / contrato estructurado | Implementation Agent | P02-T012 | Resultado por pregunta, sin booleano global que oculte brechas | Test que falla si una pregunta obligatoria critica queda incompleta sin justificacion |
| P02-T014 | Implementar registro de robustez y suficiencia de muestra | Runtime / contrato estructurado | Implementation Agent | P02-T011 | Cada vista/ranking/comparacion/recomendacion declara denominador, volumen, cobertura, granularidad, comparador y suficiencia | Tests de `low_sample`, `partial`, `UNKNOWN` y `not_available` |
| P02-T015 | Implementar estructura de nucleo comun de producto | Runtime / contrato estructurado | Implementation Agent | P02-T010 | Nucleo comun con periodo, scope, fuentes, evidence refs, metricas canonicas, coverage status, Knowledge claims, recomendaciones aprobadas y limitaciones | Test de presencia y trazabilidad del nucleo comun |
| P02-T016 | Implementar validadores de equivalencia para proyeccion analitica y ejecutiva | Runtime / contrato estructurado | Implementation Agent | P02-T015 | Proyecciones no pueden crear evidencia, Knowledge, Recommendations ni alterar estados | Tests de no divergencia semantica |

### 6.3 Generacion de Evidence, Knowledge y Recommendations

| ID | Tarea | Tipo | Responsable sugerido | Depende de | Resultado esperado | Evidencia de finalizacion |
| --- | --- | --- | --- | --- | --- | --- |
| P02-T020 | Extender construccion de Evidence Set para alimentar vistas requeridas | Evidence | Implementation Agent | P02-T010, ejecucion autorizada futura | Evidencia trazable para volumen, calidad FARO, coste-calidad, campana/adset, anuncio/creatividad, temporal, senales, concentracion y limites; las oportunidades solo podran derivarse despues en Knowledge/Recommendations | Evidence Set con referencias por vista y pregunta, sin findings, oportunidades ni recomendaciones |
| P02-T021 | Incorporar `ad_name` como etiqueta interpretativa condicional | Evidence / gap funcional | Implementation Agent | P02-T020 | `ad_name` se incluye si esta disponible; no se usa como clave tecnica ni fallback | Test o validacion de que `ad_id_norm` sigue siendo identificador tecnico |
| P02-T022 | Evaluar `ticket_status` como dimension condicional post-lead | Evidence / gap funcional | Implementation Agent | P02-T020, fuente autorizada futura | Si existe fuente autorizada y cobertura suficiente, se declara CQ-002; si no, `not_available` o `not_applicable` justificado | Registro de aplicabilidad y ausencia de imputacion desde FARO |
| P02-T023 | Implementar lectura temporal mensual y semanal condicionada por comparabilidad | Evidence / gap funcional | Implementation Agent | P02-T020 | AQ-009 siempre recibe vista temporal comparable; semanal solo con semanas completas o regla explicita | Test de semanas parciales y degradacion a `partial` o `not_available` |
| P02-T024 | Extender Knowledge Generation con evaluacion por pregunta analitica | Knowledge | Implementation Agent | P02-T020 | Cada AQ obligatoria cubierta incluye evidencia, comparacion, interpretacion, implicacion, limitacion y conclusion/hipotesis/`UNKNOWN` | Knowledge Set con profundidad verificable por pregunta |
| P02-T025 | Implementar control de inferencias prohibidas | Knowledge | Implementation Agent | P02-T024 | No causalidad creativa/plataforma/comercial no validada; no imputacion de `ticket_status`; no comparacion incompatible sin advertencia | Tests o validaciones de restricciones interpretativas |
| P02-T026 | Generar Recommendations desde Knowledge aprobado | Recommendations | Implementation Agent | P02-T024 | Recomendaciones derivadas solo de Knowledge, con soporte y prioridad | Recommendation Set trazado a Knowledge |
| P02-T027 | Clasificar recomendaciones accionables | Recommendations | Implementation Agent | P02-T026 | Cada accion es `measurable_experiment` o `verifiable_action`; hipotesis no ejecutables quedan como `non_actionable_hypothesis` | Tests de campos obligatorios por categoria |

### 6.4 Construccion de informes

| ID | Tarea | Tipo | Responsable sugerido | Depende de | Resultado esperado | Evidencia de finalizacion |
| --- | --- | --- | --- | --- | --- | --- |
| P02-T030 | Construir representacion del nucleo comun de producto | Presentation / reports | Implementation Agent | P02-T015, P02-T024, P02-T027 | Artefacto canonico consumible por proyecciones analitica y ejecutiva | Producto comun estructurado con trazabilidad completa |
| P02-T031 | Construir informe analitico desde nucleo comun | Presentation / reports | Implementation Agent | P02-T030, P02-T016 | Informe analitico con vistas completas, matriz de cobertura, comparaciones, reconciliacion, senales y limites | Report analitico generado en ejecucion autorizada futura |
| P02-T032 | Construir informe ejecutivo desde nucleo comun | Presentation / reports | Implementation Agent | P02-T030, P02-T016 | Informe ejecutivo con mensajes, implicaciones, oportunidades, riesgos y recomendaciones experimentales sin ocultar limites | Report ejecutivo generado en ejecucion autorizada futura |
| P02-T033 | Validar equivalencia semantica entre informes | Presentation / QA | QA Gate Agent | P02-T031, P02-T032 | Las proyecciones no cambian evidencia, Knowledge, recomendaciones, `UNKNOWN` ni coverage states | Validacion comparativa documentada |

### 6.5 Documentacion

| ID | Tarea | Tipo | Responsable sugerido | Depende de | Resultado esperado | Evidencia de finalizacion |
| --- | --- | --- | --- | --- | --- | --- |
| P02-T040 | Documentar materializacion operativa de SPEC-014 sin crear contrato paralelo | Documentacion | Documentation Agent | P02-T010 a P02-T016 | Documentacion de como se materializa el contrato aprobado, sin reinterpretar ni ampliar SPEC-014 | Documento tecnico o seccion de uso referenciada que remite a SPEC-014 como unica fuente normativa |
| P02-T041 | Documentar reglas de aplicabilidad para `ad_name`, `ticket_status` y evolucion temporal | Documentacion | Documentation Agent | P02-T021, P02-T022, P02-T023 | Gaps funcionales quedan explicados sin convertir ausencias justificadas en incumplimientos automaticos | Referencia documental actualizada |
| P02-T042 | Actualizar indices canonicos tras implementacion y QA | Documentacion | Documentation Agent | QA posterior PASS | README, AUC README y context refs reflejan el resultado aprobado | Diffs documentales y estado canonico actualizado |

### 6.6 Pruebas y QA

| ID | Tarea | Tipo | Responsable sugerido | Depende de | Resultado esperado | Evidencia de finalizacion |
| --- | --- | --- | --- | --- | --- | --- |
| P02-T050 | Crear tests de schema para matriz y nucleo comun | QA / tests | Implementation Agent | P02-T010 a P02-T015 | Estructuras obligatorias presentes y versionadas | Suite local PASS |
| P02-T051 | Crear tests de estados de cobertura y degradacion | QA / tests | Implementation Agent | P02-T012, P02-T013, P02-T014 | Estados validos y bloqueos se comportan segun SPEC-014 | Suite local PASS |
| P02-T052 | Crear tests de profundidad minima por pregunta | QA / tests | Implementation Agent | P02-T024 | Una AQ obligatoria no puede ser `complete` sin los elementos minimos | Suite local PASS |
| P02-T053 | Crear tests de recomendaciones clasificadas | QA / tests | Implementation Agent | P02-T027 | Acciones sin metrica/guardrail/criterio o cierre no pasan como experimentos medibles | Suite local PASS |
| P02-T054 | Crear tests de proyecciones sin nuevo conocimiento | QA / tests | Implementation Agent | P02-T031, P02-T032 | Presentacion no reconstruye Evidence, Knowledge ni Recommendations | Suite local PASS |
| P02-T055 | Preparar handoff de QA para Entry/Exit futuro sin emitir gate | QA / documentacion | Tasks Planner Agent / Implementation Agent | P02-T001 o implementacion futura | QA recibe criterios objetivos para revisar readiness o cierre | Handoff documental, sin decision de gate |

---

## 7. Matriz de trazabilidad SPEC-014 a tareas

| Requisito SPEC-014 | Tareas P02 |
| --- | --- |
| Matriz de cobertura integrada | P02-T011, P02-T013, P02-T050, P02-T051 |
| Vistas analiticas requeridas | P02-T020, P02-T030, P02-T031 |
| Profundidad minima verificable | P02-T024, P02-T052 |
| Estados de cobertura | P02-T012, P02-T051 |
| Robustez y suficiencia de muestra | P02-T014, P02-T051 |
| `UNKNOWN`, evidencia insuficiente y cobertura parcial | P02-T012, P02-T014, P02-T024, P02-T051 |
| Nucleo comun del producto | P02-T015, P02-T030, P02-T050 |
| Proyeccion analitica | P02-T016, P02-T031, P02-T054 |
| Proyeccion ejecutiva | P02-T016, P02-T032, P02-T054 |
| Recomendaciones como experimentos medibles o acciones verificables | P02-T026, P02-T027, P02-T053 |
| `ad_name` como etiqueta interpretativa condicional | P02-T021, P02-T041 |
| `ticket_status` como dimension condicional post-lead | P02-T022, P02-T041 |
| Evolucion temporal mensual/semanal | P02-T023, P02-T031 |
| Prohibicion de expected values historicos | P02-T001, P02-T025, P02-T055 |
| Separacion Evidence/Knowledge/Recommendations/Presentation | P02-T020, P02-T024, P02-T026, P02-T030 a P02-T033, P02-T054 |

---

## 8. Orden recomendado

1. Pasar este plan a QA Gate Agent para Entry Gate de P02.
2. Si el Entry Gate aprueba, inspeccionar puntos de integracion y compatibilidad con SPEC-012/SPEC-013: P02-T002 a P02-T003.
3. Implementar contratos estructurados, matriz, estados, robustez, nucleo comun y proyecciones: P02-T010 a P02-T016.
4. Extender generacion futura de Evidence, Knowledge y Recommendations: P02-T020 a P02-T027.
5. Construir reports desde nucleo comun: P02-T030 a P02-T033.
6. Completar documentacion operativa e indices tras QA: P02-T040 a P02-T042.
7. Ejecutar pruebas locales y preparar handoff QA: P02-T050 a P02-T055.

---

## 9. Criterios de finalizacion de P02

P02 puede considerarse completado solo cuando exista evidencia verificable de que:

- la matriz de cobertura se genera por pregunta y criticidad;
- cada pregunta obligatoria tiene estado, justificacion, evidencia, comparacion, interpretacion, implicacion, limitacion y conclusion/hipotesis/`UNKNOWN` cuando proceda;
- los estados `UNKNOWN` y `not_available` no se mezclan;
- `partial`, `not_applicable` y `blocked` se aplican con reglas trazables;
- cada vista o comparacion declara denominador, volumen, cobertura, granularidad, comparador y suficiencia;
- `ad_name` se trata como etiqueta interpretativa condicional, nunca como clave tecnica;
- `ticket_status` se trata solo como dimension condicional autorizada, nunca imputada;
- la evolucion temporal mensual existe como minimo y la semanal solo se declara comparable cuando lo sea;
- toda recomendacion accionable queda clasificada como experimento medible o accion verificable;
- el nucleo comun conserva evidencia, Knowledge, recomendaciones, limitaciones y coverage states;
- las proyecciones analitica y ejecutiva preservan equivalencia semantica;
- las pruebas locales relevantes pasan;
- QA puede validar desde artefactos fisicos o estructurados, no desde narrativa Markdown como fuente de datos;
- los indices documentales se actualizan solo despues de una decision QA posterior.

---

## 10. Riesgos

| Riesgo | Impacto | Mitigacion planificada |
| --- | --- | --- |
| Convertir la matriz en checklist formal sin profundidad analitica | Producto aparentemente completo pero contractualmente insuficiente | Tests de profundidad minima y validacion por pregunta. |
| Mezclar `UNKNOWN` con `not_available` | Decisiones ambiguas o inferencias falsas | Validadores de estado y justificacion obligatoria. |
| Usar `ad_name` como clave tecnica | Joins fragiles o interpretacion incorrecta de anuncios | Mantener `ad_id_norm` o equivalente como identificador tecnico. |
| Tratar ausencia de `ticket_status` como incumplimiento automatico | Bloqueo indebido de productos conformes | Aplicabilidad condicional y fuente autorizada obligatoria. |
| Comparar semanas parciales como completas | Lectura temporal enganosa | Regla explicita de comparabilidad temporal. |
| Presentacion ejecutiva ocultando limites | Perdida de equivalencia semantica | Validacion de nucleo comun contra proyecciones. |
| Recomendar acciones sin metrica o criterio de cierre | Recomendaciones no verificables | Clasificacion obligatoria y campos minimos por categoria. |
| Reabrir alcance P01 o modificar SPEC-014 | Deriva metodologica | P02 implementa requisitos aprobados; cambios normativos requieren fase separada. |
| Ejecutar evidencia antes de autorizacion | Violacion del Runbook AUC-001 | Entry Gate y BigQuery MCP obligatorio solo en ejecucion posterior autorizada. |

---

## 11. Preparacion para Entry Gate

Este plan esta listo para ser presentado a QA Gate Agent como input de un futuro Entry Gate de P02 porque:

- parte de SPEC-014 cerrada y del P01 Documentary Closure Gate con PASS;
- mantiene el boundary de P02 como implementacion posterior separada;
- separa runtime/contratos estructurados, Evidence, Knowledge, Recommendations, reports, documentacion, pruebas y QA;
- no ejecuta BigQuery;
- no implementa codigo;
- no abre gates;
- no genera outputs;
- define dependencias, riesgos, orden y criterios verificables de finalizacion.

Decision de readiness del plan:

```text
READY FOR P02 ENTRY GATE REVIEW
```