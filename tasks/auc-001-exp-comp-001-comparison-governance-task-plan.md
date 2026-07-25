# AUC-001-EXP-COMP-001 Comparison Governance Task Plan

## Metadatos

| Campo | Valor |
| --- | --- |
| Artifact ID | TASK-PLAN-AUC-001-EXP-COMP-001-COMPARISON-GOVERNANCE |
| Caso de uso | AUC-001 - Meta Lead Quality Analysis |
| Iteracion | AUC-001-EXP-COMP-001 |
| Tipo | Plan de implementacion experimental controlada |
| Fuente normativa | `docs/evaluations/auc-001/experiments/auc-001-exp-comp-001-final-experimental-specification.md` |
| Decision arquitectonica | `EXPERIMENT FIRST`; solucion hibrida local en AUC-001 |
| Entry Gate | `gates/auc-001-exp-comp-001-entry-gate.md` |
| Decision de Entry Gate | PASS WITH CONDITIONS |
| Agente | Tasks Planner Agent |
| Fecha | 2026-07-24 |
| Estado | Ready for implementation handoff review |
| BigQuery | No ejecutado |
| Implementacion | No ejecutada en este plan |
| Outputs analiticos | No generados |

---

## 1. Estado autorizado

`AUC-001-EXP-COMP-001` queda autorizado para Task Planning e implementacion controlada por el Entry Gate `PASS WITH CONDITIONS`.

La autorizacion se limita a validar experimentalmente, dentro de `vca-ai` y solo para AUC-001, que una clasificacion explicita de comparaciones o claims entre universos estrategicos no equivalentes reduce inferencias economicas, causalidades, optimizaciones o jerarquias implicitas sin eliminar comparaciones descriptivas utiles.

Este plan no implementa codigo, no adquiere evidencia, no consulta BigQuery MCP, no genera outputs y no modifica contratos vigentes.

---

## 2. Objetivo de implementacion

Implementar soporte local experimental para que AUC-001:

- detecte y clasifique comparaciones o claims durante Analytical Reasoning;
- preserve la clasificacion hasta Knowledge, Recommendation Set cuando aplique, Common Product Core (CPC) y Canonical Projection Source (CPS);
- adapte Presentation por audiencia sin crear conocimiento nuevo ni convertir claims restringidos en conclusiones;
- produzca evidencia QA controlada que permita validar casos positivos y negativos sin evidencia nueva.

---

## 3. Boundary

Incluido:

- contrato local de `comparison_classification`;
- resolucion multi-etiqueta de `comparison_type` mediante `restrictive_type_priority`;
- regla para `strategic_equivalence = unknown`;
- reconciliacion `provisional_claim_ref -> knowledge_refs`;
- transporte de clasificacion, limitacion semantica, comportamiento por proyeccion y trazabilidad hasta CPC y CPS;
- restricciones de Presentation analitica y ejecutiva;
- fixtures y validadores experimentales sin datos nuevos.

Fuera de alcance:

- modificar Strategic Context;
- abrir o modificar SPEC Foundation;
- crear taxonomia universal;
- modificar SPEC-014, SPEC-015 o SPEC-016;
- adquirir evidencia nueva;
- ejecutar BigQuery MCP, BigQuery CLI o cualquier fallback;
- generar informes u outputs reales de AUC-001;
- usar outputs historicos como Evidence o expected values;
- promover la solucion a AIF Foundation;
- cerrar la iteracion sin Reviewer, QA y ejecucion experimental posteriores.

---

## 4. Dependencias

| Dependencia | Rol en la iteracion | Estado requerido |
| --- | --- | --- |
| AUC-001-EXP-COMP-001 Final Experimental Specification | Fuente normativa directa | Vigente, no modificada por este plan |
| AUC-001-EXP-COMP-001 Entry Gate | Autoriza planificacion e implementacion controlada | PASS WITH CONDITIONS |
| Memo arquitectonico | Fija `EXPERIMENT FIRST` y solucion local | Aprobado |
| Reviewer Review y Resolution Record | Confirman cinco cambios aplicados | Persistidos |
| SPEC-014 | Define Common Product Core y contrato analitico vigente | Dependencia no modificable |
| SPEC-015 | Define Canonical Projection Source y proyecciones hermanas | Dependencia no modificable |
| SPEC-016 | Define paquete operativo aceptable | Dependencia no modificable |
| Skill / Runbook AUC-001 | Orden operativo y restricciones MCP/no fallback | Vigentes |
| Perfil local FARO | Fuente de restricciones estrategicas existentes | Solo lectura; no modificar |

---

## 5. Plan de tareas

### 5.1 Precondiciones y localizacion

| ID | Tarea | Responsable sugerido | Depende de | Resultado esperado | Evidencia de cierre |
| --- | --- | --- | --- | --- | --- |
| EXPCOMP-T001 | Confirmar Entry Gate `PASS WITH CONDITIONS` antes de implementar | Implementation Agent | Ninguna | La implementacion solo inicia con gate fisico autorizado | Handoff cita `gates/auc-001-exp-comp-001-entry-gate.md` |
| EXPCOMP-T002 | Localizar puntos locales de Analytical Reasoning, Knowledge, Recommendations, CPC, CPS, Presentation y validadores | Implementation Agent | EXPCOMP-T001 | Mapa de rutas candidatas sin fijar nueva arquitectura | Nota en handoff con rutas inspeccionadas |
| EXPCOMP-T003 | Confirmar que no se requiere evidencia nueva ni BigQuery | Implementation Agent | EXPCOMP-T002 | La implementacion opera con fixtures controlados y contratos existentes | Handoff declara `new_evidence_acquired: false` |
| EXPCOMP-T004 | Confirmar proteccion de Strategic Context y specs vigentes | Implementation Agent | EXPCOMP-T002 | Strategic Context, SPEC-014, SPEC-015 y SPEC-016 quedan fuera de cambios | `git status` o diff acotado sin cambios en esas rutas |

### 5.2 Contrato local de clasificacion

| ID | Tarea | Responsable sugerido | Depende de | Resultado esperado | Evidencia de cierre |
| --- | --- | --- | --- | --- | --- |
| EXPCOMP-T010 | Materializar el contrato local `comparison_classification` | Implementation Agent | EXPCOMP-T002 | Estructura local con campos de la especificacion experimental | Tests o fixture de schema valido |
| EXPCOMP-T011 | Implementar identificacion obligatoria `comparison_id` | Implementation Agent | EXPCOMP-T010 | Toda comparacion relevante queda identificada | Test positivo y negativo |
| EXPCOMP-T012 | Implementar `comparison_type` multi-etiqueta | Implementation Agent | EXPCOMP-T010 | Un claim puede combinar contraste descriptivo, eficiencia, jerarquia y causalidad/optimizacion | Fixture con multiples tipos |
| EXPCOMP-T013 | Implementar `restrictive_type_priority` | Implementation Agent | EXPCOMP-T012 | `governance_status` se resuelve por el tipo mas restrictivo | Test de prioridad restrictiva |
| EXPCOMP-T014 | Implementar semantica `required_limitation_or_disclaimer_semantics` | Implementation Agent | EXPCOMP-T010 | Se preserva semantica obligatoria sin imponer wording literal | Test de campo obligatorio cuando aplique |

### 5.3 Analytical Reasoning y equivalencia estrategica

| ID | Tarea | Responsable sugerido | Depende de | Resultado esperado | Evidencia de cierre |
| --- | --- | --- | --- | --- | --- |
| EXPCOMP-T020 | Detectar comparaciones explicitas e implicitas antes de Knowledge | Implementation Agent | EXPCOMP-T010 | Comparaciones materiales se clasifican antes de estabilizar Knowledge | Fixture con comparacion explicita e implicita |
| EXPCOMP-T021 | Registrar universos comparados y `strategic_equivalence` | Implementation Agent | EXPCOMP-T020 | Cada comparacion declara universos y equivalencia `equivalent`, `non_equivalent` o `unknown` | Test de universos presentes |
| EXPCOMP-T022 | Aplicar regla para `strategic_equivalence = non_equivalent` | Implementation Agent | EXPCOMP-T021 | No se emite jerarquia estrategica sin limitacion explicita | Fixture no equivalente con jerarquia restringida |
| EXPCOMP-T023 | Aplicar regla para `strategic_equivalence = unknown` | Implementation Agent | EXPCOMP-T021 | Claims economicos, jerarquicos, causales u orientados a optimizacion se degradan, restringen o bloquean | Fixture `unknown` sin decision economica concluyente |
| EXPCOMP-T024 | Bloquear causalidad, optimizacion o reasignacion no soportada | Implementation Agent | EXPCOMP-T013 | Claims no autorizados quedan `blocked` | Fixture de claim bloqueado |
| EXPCOMP-T025 | Preservar comparaciones descriptivas utiles | Implementation Agent | EXPCOMP-T013 | Contrastes descriptivos sin ranking, causalidad ni recomendacion economica permanecen visibles | Fixture de comparacion descriptiva permitida |

### 5.4 Reconciliacion con Knowledge y Recommendations

| ID | Tarea | Responsable sugerido | Depende de | Resultado esperado | Evidencia de cierre |
| --- | --- | --- | --- | --- | --- |
| EXPCOMP-T030 | Implementar `provisional_claim_ref` durante Analytical Reasoning | Implementation Agent | EXPCOMP-T020 | Claims previos a Knowledge tienen ancla textual o provisional | Test de claim provisional |
| EXPCOMP-T031 | Reconciliar `provisional_claim_ref` contra `knowledge_refs` | Implementation Agent | EXPCOMP-T030 | Claims materiales quedan reconciliados antes de Knowledge estabilizado | Registro o fixture de reconciliacion |
| EXPCOMP-T032 | Bloquear claim material no reconciliable | Implementation Agent | EXPCOMP-T031 | Claim material sin reconciliacion queda `blocked` | Test negativo |
| EXPCOMP-T033 | Controlar `recommendation_refs` despues de Recommendation Set | Implementation Agent | EXPCOMP-T031 | `recommendation_refs` no aparecen antes de Recommendation Set estabilizado | Test de orden |
| EXPCOMP-T034 | Impedir recomendaciones desde claims `blocked` | Implementation Agent | EXPCOMP-T033 | Recommendation Set no deriva acciones desde claims bloqueados | Fixture de recomendacion rechazada |
| EXPCOMP-T035 | Impedir priorizacion economica concluyente desde equivalencia `unknown` | Implementation Agent | EXPCOMP-T033 | Recomendaciones con equivalencia desconocida quedan restringidas o bloqueadas | Test de no decision economica concluyente |

### 5.5 Transporte a CPC y CPS

| ID | Tarea | Responsable sugerido | Depende de | Resultado esperado | Evidencia de cierre |
| --- | --- | --- | --- | --- | --- |
| EXPCOMP-T040 | Transportar clasificacion al Common Product Core (CPC) | Implementation Agent | EXPCOMP-T031 | CPC conserva `governance_status`, limitacion semantica y trazabilidad | Fixture CPC con clasificacion |
| EXPCOMP-T041 | Impedir suavizado o eliminacion de restricciones en CPC | Implementation Agent | EXPCOMP-T040 | CPC no degrada bloqueos ni limitaciones | Test negativo |
| EXPCOMP-T042 | Transportar clasificacion al Canonical Projection Source (CPS) | Implementation Agent | EXPCOMP-T040 | CPS conserva clasificacion y comportamiento permitido por proyeccion | Fixture CPS con clasificacion |
| EXPCOMP-T043 | Declarar `allowed_projection_behavior` por audiencia | Implementation Agent | EXPCOMP-T042 | CPS identifica comportamiento analytical y executive | Test de comportamiento por proyeccion |
| EXPCOMP-T044 | Validar trazabilidad `Evidence -> Knowledge -> Recommendations -> CPC -> CPS` | Implementation Agent | EXPCOMP-T042 | La matriz de trazabilidad queda reconstruible para QA | Matriz local de trazabilidad |

### 5.6 Presentation por audiencia

| ID | Tarea | Responsable sugerido | Depende de | Resultado esperado | Evidencia de cierre |
| --- | --- | --- | --- | --- | --- |
| EXPCOMP-T050 | Adaptar Presentation analitica a clasificacion autorizada | Implementation Agent | EXPCOMP-T042 | Analytical puede mostrar comparacion completa con limitacion visible y trazabilidad | Fixture analytical |
| EXPCOMP-T051 | Adaptar Presentation ejecutiva a clasificacion autorizada | Implementation Agent | EXPCOMP-T042 | Executive evita ranking, eficiencia u optimizacion cuando no estan autorizados | Fixture executive |
| EXPCOMP-T052 | Bloquear claims `blocked` en cualquier proyeccion | Implementation Agent | EXPCOMP-T050, EXPCOMP-T051 | Ningun claim bloqueado llega a Presentation | Test negativo |
| EXPCOMP-T053 | Impedir que `allowed_with_limitation` se vuelva concluyente | Implementation Agent | EXPCOMP-T050, EXPCOMP-T051 | Presentation conserva limitacion semantica | Test de no-promocion |
| EXPCOMP-T054 | Validar que la adaptacion no altera contenido canonico | Implementation Agent | EXPCOMP-T050, EXPCOMP-T051 | Variacion de forma sin cambio semantico | Validador o snapshot semantico |

### 5.7 QA experimental y fixtures

| ID | Tarea | Responsable sugerido | Depende de | Resultado esperado | Evidencia de cierre |
| --- | --- | --- | --- | --- | --- |
| EXPCOMP-T060 | Crear fixture con `comparison_type` multiple | Implementation Agent | EXPCOMP-T013 | QA verifica prioridad restrictiva | Test PASS |
| EXPCOMP-T061 | Crear fixture `strategic_equivalence = unknown` | Implementation Agent | EXPCOMP-T023 | QA verifica degradacion, restriccion o bloqueo | Test PASS |
| EXPCOMP-T062 | Crear fixture de claim bloqueado | Implementation Agent | EXPCOMP-T024 | QA verifica bloqueo hasta Presentation | Test PASS |
| EXPCOMP-T063 | Crear fixture de comparacion descriptiva preservada | Implementation Agent | EXPCOMP-T025 | QA verifica que no se elimina contraste util | Test PASS |
| EXPCOMP-T064 | Crear fixture ejecutivo con jerarquia implicita degradada | Implementation Agent | EXPCOMP-T051 | QA verifica adaptacion ejecutiva restringida | Test PASS |
| EXPCOMP-T065 | Crear matriz `comparison_id -> comparison_type -> governance_status -> CPC -> CPS -> projection` | Implementation Agent | EXPCOMP-T044, EXPCOMP-T050, EXPCOMP-T051 | QA puede auditar transporte completo | Matriz persistida o generada por test |
| EXPCOMP-T066 | Ejecutar suite local experimental completa | Implementation Agent | EXPCOMP-T060 a EXPCOMP-T065 | Todos los casos experimentales pasan sin evidencia nueva | Resultado de comandos en handoff |

### 5.8 Handoffs y revision

| ID | Tarea | Responsable sugerido | Depende de | Resultado esperado | Evidencia de cierre |
| --- | --- | --- | --- | --- | --- |
| EXPCOMP-T070 | Preparar handoff de implementacion para Reviewer Agent | Implementation Agent | EXPCOMP-T066 | Reviewer recibe rutas modificadas, alcance, fixtures, tests y no-autorizados respetados | Handoff documental |
| EXPCOMP-T071 | Preparar handoff de QA experimental | Implementation Agent | EXPCOMP-T070 | QA recibe matriz, fixtures, resultados y limitaciones | Handoff documental |
| EXPCOMP-T072 | Actualizar indices solo tras revision o QA que lo autorice | Documentation Agent | Reviewer/QA posterior | Estado canonico no se adelanta prematuramente | Diffs documentales posteriores |

---

## 6. Matriz de trazabilidad

| Requisito de la especificacion | Tareas |
| --- | --- |
| Clasificar cada comparacion | EXPCOMP-T010 a EXPCOMP-T025 |
| `comparison_type` multi-etiqueta y prioridad restrictiva | EXPCOMP-T012, EXPCOMP-T013, EXPCOMP-T060 |
| Regla para `strategic_equivalence = unknown` | EXPCOMP-T023, EXPCOMP-T061 |
| `provisional_claim_ref` y `stabilized_claim_refs` | EXPCOMP-T030 a EXPCOMP-T032 |
| Recommendation Set no deriva desde claims bloqueados | EXPCOMP-T033 a EXPCOMP-T035 |
| Transporte hasta CPC | EXPCOMP-T040, EXPCOMP-T041 |
| Transporte hasta CPS | EXPCOMP-T042 a EXPCOMP-T044 |
| Adaptacion analytical | EXPCOMP-T050 |
| Adaptacion executive | EXPCOMP-T051, EXPCOMP-T064 |
| No presentar claims `blocked` | EXPCOMP-T052, EXPCOMP-T062 |
| No convertir limitaciones en conclusiones | EXPCOMP-T053 |
| Preservar comparaciones descriptivas utiles | EXPCOMP-T025, EXPCOMP-T063 |
| Evidencia QA sin datos nuevos | EXPCOMP-T060 a EXPCOMP-T066 |
| Sin Strategic Context, Foundation, BigQuery ni outputs reales | EXPCOMP-T003, EXPCOMP-T004, EXPCOMP-T070 |

---

## 7. Orden recomendado

1. Confirmar gate, no-evidencia y protecciones de alcance: EXPCOMP-T001 a EXPCOMP-T004.
2. Materializar contrato local de clasificacion: EXPCOMP-T010 a EXPCOMP-T014.
3. Integrar clasificacion en Analytical Reasoning: EXPCOMP-T020 a EXPCOMP-T025.
4. Reconciliar claims con Knowledge y Recommendations: EXPCOMP-T030 a EXPCOMP-T035.
5. Transportar clasificacion hasta CPC y CPS: EXPCOMP-T040 a EXPCOMP-T044.
6. Aplicar restricciones de Presentation por audiencia: EXPCOMP-T050 a EXPCOMP-T054.
7. Crear y ejecutar fixtures QA experimentales: EXPCOMP-T060 a EXPCOMP-T066.
8. Preparar handoffs para Reviewer y QA: EXPCOMP-T070 a EXPCOMP-T071.
9. Actualizar indices solo tras revision o QA posterior: EXPCOMP-T072.

---

## 8. Condiciones de bloqueo

La implementacion debe detenerse si:

- requiere modificar Strategic Context;
- requiere abrir SPEC Foundation o taxonomia universal;
- requiere modificar SPEC-014, SPEC-015 o SPEC-016;
- requiere adquirir evidencia nueva o ejecutar BigQuery;
- intenta usar outputs historicos como Evidence o expected values;
- no puede reconciliar un `provisional_claim_ref` material con Knowledge;
- no puede transportar la clasificacion hasta CPC y CPS;
- Presentation necesita inventar contexto para adaptar un claim;
- una recomendacion depende de un claim `blocked`;
- QA no puede verificar los casos experimentales sin evidencia nueva.

---

## 9. Criterios de finalizacion de implementacion

La implementacion podra considerarse lista para Reviewer y QA cuando exista evidencia de que:

- todas las comparaciones relevantes reciben `comparison_id`;
- `comparison_type` multi-etiqueta se resuelve por prioridad restrictiva;
- `strategic_equivalence = unknown` no permite decisiones economicas concluyentes;
- `provisional_claim_ref` queda reconciliado o bloqueado si el claim es material;
- CPC y CPS preservan clasificacion, restricciones, comportamiento por proyeccion y trazabilidad;
- Presentation analitica conserva detalle con limitacion visible;
- Presentation ejecutiva degrada o suprime jerarquias implicitas no autorizadas;
- claims `blocked` no llegan a Presentation ni Recommendations;
- comparaciones descriptivas utiles se preservan;
- fixtures QA cubren positivos y negativos;
- no se adquirio evidencia nueva, no se ejecuto BigQuery y no se generaron outputs reales;
- Strategic Context, SPEC-014, SPEC-015 y SPEC-016 permanecen sin cambios.

---

## 10. Riesgos

| Riesgo | Impacto | Mitigacion planificada |
| --- | --- | --- |
| Sobrerrestringir comparaciones descriptivas | Se pierde utilidad analitica | Fixture de comparacion descriptiva preservada. |
| Clasificacion debil permite ranking implicito | Se mantiene el defecto experimental | Prioridad restrictiva y fixtures de claims bloqueados. |
| `unknown` se usa como salida permissiva | Decision economica concluyente no autorizada | Regla y test especifico para equivalencia desconocida. |
| Presentation suaviza limitaciones | Cambia la semantica canonica | Tests de no-promocion y behavior por audiencia. |
| Se crea taxonomia universal de facto | Exceso de alcance | Boundary local AUC-001 y no-Fundation como bloqueo. |
| QA queda dependiente de outputs reales | Rompe alcance experimental sin evidencia nueva | Fixtures controlados y matriz local de trazabilidad. |

---

## 11. Preparacion para Implementation Agent

Este plan queda listo para handoff de implementacion porque:

- parte de Entry Gate `PASS WITH CONDITIONS`;
- traduce exclusivamente la especificacion experimental aprobada;
- mantiene alcance local AUC-001;
- no disena una taxonomia universal;
- no autoriza evidencia nueva, BigQuery ni outputs reales;
- define tareas, dependencias, bloqueos, riesgos, criterios de cierre y evidencia QA esperada.

Decision de readiness del plan:

```text
READY FOR IMPLEMENTATION AGENT
```
