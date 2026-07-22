# AUC-001-P04 Canonical Projection Consolidation Task Plan

## Metadatos

| Campo | Valor |
| --- | --- |
| Artifact ID | TASK-PLAN-AUC-001-P04-CANONICAL-PROJECTION-CONSOLIDATION |
| Caso de uso | AUC-001 - Meta Lead Quality Analysis |
| Fase | AUC-001-P04 |
| Fuente normativa | `specs/spec-015-auc-001-canonical-projection-consolidation.md` |
| Dependencias normativas | SPEC-010, SPEC-011, SPEC-014 |
| Decision documental precedente | AUC-001-P04 Documentary Closure PASS |
| Agente | Tasks Planner Agent |
| Creado | 2026-07-22 |
| Estado | Ready for controlled implementation planning review |
| Entry Gate | No creado en este plan |
| BigQuery | No ejecutado |
| Implementacion | No ejecutada |
| Outputs | No generados |

---

## 1. Estado real reconstruido

El estado vigente de AUC-001 para esta planificacion es:

- SPEC-010 y SPEC-011 gobiernan seleccion de proyeccion y transformacion por Communication Context.
- SPEC-014 esta cerrada como Contrato de Producto Analitico de AUC-001.
- P02 produjo un paquete real conforme a SPEC-014, con limitaciones declaradas.
- P02 dejo un antecedente fisico del nucleo comun en `outputs/auc-001/p02/2026-07-17/product-core/common-product-core.json`.
- P03 valido experimentalmente que la riqueza analitica se recupera cuando la vista integrada de senales, la narrativa y los criterios de exito son visibles.
- P03 tambien confirmo que Presentation no puede introducir valoraciones comparativas ni conocimiento nuevo.
- SPEC-015 fue aprobada con revision `PASS` y QA documental `PASS`, quedando lista para planificacion controlada de implementacion.

Este plan traduce SPEC-015 en tareas implementables. No modifica SPEC-010, SPEC-011, SPEC-014, P02, P03, outputs historicos, codigo ni gates.

---

## 2. Objetivo de P04

Implementar, en una fase posterior autorizada, la consolidacion definitiva de las proyecciones analitica y ejecutiva de AUC-001 para que ambas deriven del mismo `Canonical Projection Source`, del mismo Knowledge Set, del mismo Recommendation Set y del Contrato de Producto Analitico vigente.

La finalidad tecnica es eliminar la dependencia de prompts distintos como fuente de contenido y sustituirla por:

- un artefacto canonico intermedio verificable;
- transformaciones de Presentation sin nuevo conocimiento;
- validadores de equivalencia semantica;
- trazabilidad entre common core, Knowledge, Recommendations, Coverage Matrix y proyecciones;
- reglas explicitas para limitaciones, `UNKNOWN`, coverage states y recomendaciones.

---

## 3. Boundary

Incluido en la implementacion futura de P04:

- definir y materializar el `Canonical Projection Source`;
- conectar el `Canonical Projection Source` con common product core, Knowledge Set, Recommendation Set y Coverage Matrix;
- adaptar las proyecciones analytical y executive para derivar exclusivamente del `Canonical Projection Source`;
- implementar validacion de equivalencia semantica;
- implementar bloqueos por nuevo conocimiento en Presentation;
- preservar limitaciones, `UNKNOWN`, coverage states, exclusiones y recomendaciones;
- registrar trazabilidad suficiente en manifest o artefacto equivalente;
- crear pruebas locales y contractuales.

Fuera de P04:

- adquirir evidencia nueva;
- ejecutar BigQuery o BigQuery MCP;
- ampliar fuentes;
- modificar SPEC-010, SPEC-011 o SPEC-014;
- modificar P02, P03 u outputs historicos;
- resolver revenue/CRM, causalidad creativa, metadata adicional o temporalidad limitada por proveedor;
- crear una capability transversal de Foundation;
- abrir gates desde este plan;
- generar nuevos outputs analiticos desde este plan.

---

## 4. Dependencias

| Dependencia | Rol en P04 | Estado requerido |
| --- | --- | --- |
| SPEC-010 | Define seleccion de proyeccion como proyecciones hermanas. | Vigente, no modificada. |
| SPEC-011 | Define transformacion por Communication Context con equivalencia semantica. | Vigente, no modificada. |
| SPEC-014 | Define suficiencia del producto, preguntas, vistas, coverage y restricciones interpretativas. | Cerrada y aprobada. |
| SPEC-015 | Fuente normativa directa de P04. | Reviewer PASS y QA documental PASS. |
| Presentation Contract | Prohibe que Presentation cree evidencia, Knowledge o Recommendations. | Vigente. |
| P02 common product core | Antecedente fisico del nucleo comun. | Solo lectura; no modificar. |
| P02 Knowledge Set | Fuente canonica de claims. | Solo lectura en regresion; no modificar. |
| P02 Recommendation Set | Fuente canonica de recomendaciones. | Solo lectura en regresion; no modificar. |
| P02 Coverage Matrix | Fuente de coverage states. | Solo lectura en regresion; no modificar. |
| P03 validacion experimental | Aprendizajes sobre riqueza analitica y limites de Presentation. | Solo lectura; no usar como evidencia de negocio. |

---

## 5. Principios de traduccion desde SPEC-015

| Principio aprobado | Traduccion a tareas P04 |
| --- | --- |
| Un artefacto canonico intermedio debe preceder a Presentation | Crear generador y schema del `Canonical Projection Source` antes de report builders. |
| Analytical y Executive son proyecciones hermanas | Ambas deben consumir el mismo CPS; ninguna deriva de la otra. |
| Presentation no crea conocimiento | Validar que todo claim, metrica, limite y recomendacion procede de artefactos canonicos. |
| La equivalencia no exige igualdad textual | Validar identidad semantica por IDs, refs, coverage states, prioridades y significado. |
| La narrativa rica debe nacer del canon | Mover vista integrada, patrones y criterios de exito al CPS, no a prompts. |
| Los limites deben ser visibles donde condicionan decision | Exigir preservacion contextual de `UNKNOWN`, `partial`, `not_available` y gaps. |
| Recomendaciones deben conservar accionabilidad | Preservar categoria, prioridad, metrica primaria, guardrail, criterio de exito y condicion de revision. |
| Los gaps futuros no se resuelven en P04 | Mantener revenue/CRM, causalidad creativa, metadata adicional y temporalidad proveedor como limitaciones declaradas. |

---

## 6. Plan de tareas recomendado

### 6.1 Preparacion tecnica y boundary

| ID | Tarea | Tipo | Responsable sugerido | Depende de | Resultado esperado | Evidencia de finalizacion |
| --- | --- | --- | --- | --- | --- | --- |
| P04-T001 | Confirmar autorizacion de Entry Gate antes de implementar | Gobernanza | QA Gate Agent | Este plan | La implementacion no empieza sin gate o autorizacion equivalente | Gate futuro o autorizacion formal, no creado por este plan |
| P04-T002 | Localizar puntos de integracion actuales de common core y Presentation | Analisis tecnico | Implementation Agent | P04-T001 PASS futuro | Mapa de builders, manifests, report generators y validadores existentes | Nota tecnica con rutas de codigo y artefactos implicados |
| P04-T003 | Confirmar que P04 no requiere nueva evidencia | Control de alcance | Implementation Agent | P04-T002 | La implementacion opera sobre artefactos ya generados en ejecuciones autorizadas | Registro de precondicion sin BigQuery ni nuevas fuentes |
| P04-T004 | Definir estrategia de compatibilidad con paquetes existentes | Diseno tecnico | Implementation Agent | P04-T002 | P02/P03 quedan protegidos y las nuevas ejecuciones usan namespace futuro | Handoff tecnico con politica de no mutacion historica |

### 6.2 Canonical Projection Source

| ID | Tarea | Tipo | Responsable sugerido | Depende de | Resultado esperado | Evidencia de finalizacion |
| --- | --- | --- | --- | --- | --- | --- |
| P04-T010 | Definir schema fisico del `Canonical Projection Source` | Contrato estructurado | Implementation Agent | P04-T002 | Schema versionado con identidad, fuentes, metricas, coverage, Knowledge, vista integrada, recomendaciones, limitaciones, exclusiones y trazabilidad | Tests de schema y fixtures validos/invalidos |
| P04-T011 | Implementar constructor de CPS desde artefactos canonicos | Runtime / producto | Implementation Agent | P04-T010 | CPS se construye despues de Context, Evidence, Knowledge, Recommendations, Coverage Matrix y common core | Test de orden y dependencias de generacion |
| P04-T012 | Incorporar contenido compartido obligatorio en CPS | Runtime / producto | Implementation Agent | P04-T011 | CPS contiene todos los bloques obligatorios de SPEC-015 seccion 6 | Test de completitud por bloque |
| P04-T013 | Elevar vista integrada de senales y combinaciones al CPS | Runtime / producto | Implementation Agent | P04-T011 | Senales, combinaciones, trade-offs, concentraciones, temporalidad y patrones quedan en canon, no solo en report | Test que falla si el report introduce estos elementos fuera del CPS |
| P04-T014 | Elevar patrones de decision y narrativa autorizada al CPS | Runtime / producto | Implementation Agent | P04-T011 | Tesis, implicaciones y patrones ejecutivos proceden de Knowledge trazado | Tests de refs Knowledge por patron narrativo |
| P04-T015 | Elevar criterios de exito de recomendaciones al CPS | Runtime / producto | Implementation Agent | P04-T011 | Cada recomendacion accionable conserva metrica, guardrail, criterio de exito, ventana y condicion de revision | Tests de recomendaciones completas e incompletas |
| P04-T016 | Registrar limitaciones, `UNKNOWN`, coverage states y exclusiones en CPS | Runtime / producto | Implementation Agent | P04-T011 | CPS preserva gaps futuros y estados `partial`, `not_available`, `not_applicable`, `UNKNOWN` y `blocked` | Tests de preservacion y no normalizacion indebida |

### 6.3 Materializacion de proyecciones hermanas

| ID | Tarea | Tipo | Responsable sugerido | Depende de | Resultado esperado | Evidencia de finalizacion |
| --- | --- | --- | --- | --- | --- | --- |
| P04-T020 | Adaptar la proyeccion analytical para consumir solo CPS | Presentation | Implementation Agent | P04-T010 a P04-T016 | Informe analitico deriva del CPS y conserva detalle tecnico suficiente | Test o snapshot de derivacion sin acceso directo a prompts analiticos como fuente de conocimiento |
| P04-T021 | Adaptar la proyeccion executive para consumir solo CPS | Presentation | Implementation Agent | P04-T010 a P04-T016 | Informe ejecutivo deriva del CPS y condensa sin cambiar significado | Test o snapshot de derivacion sin acceso directo a prompts ejecutivos como fuente de conocimiento |
| P04-T022 | Impedir derivacion entre proyecciones | Presentation / arquitectura | Implementation Agent | P04-T020, P04-T021 | Analytical y Executive se generan como hermanas desde el mismo CPS | Test de grafo/dependencias o comprobacion de manifest |
| P04-T023 | Declarar explicitamente origen CPS en ambas proyecciones futuras | Presentation / trazabilidad | Implementation Agent | P04-T020, P04-T021 | Cada report referencia CPS, version y fingerprint o identificador equivalente | Validacion de presencia en reports o manifests |
| P04-T024 | Mantener variaciones permitidas por proyeccion | Presentation | Implementation Agent | P04-T020, P04-T021 | Analytical puede ampliar detalle y Executive puede condensar sin crear contenido nuevo | Tests de campos permitidos y bloqueados por tipo de proyeccion |

### 6.4 Validadores y bloqueos

| ID | Tarea | Tipo | Responsable sugerido | Depende de | Resultado esperado | Evidencia de finalizacion |
| --- | --- | --- | --- | --- | --- | --- |
| P04-T030 | Implementar validador de equivalencia semantica CPS -> Analytical | QA / contrato | Implementation Agent | P04-T020 | Claims, metricas, coverage, limitaciones, prioridades y recomendaciones permanecen equivalentes | Tests positivos y negativos |
| P04-T031 | Implementar validador de equivalencia semantica CPS -> Executive | QA / contrato | Implementation Agent | P04-T021 | Condensacion ejecutiva no cambia certeza, prioridad, alcance ni accionabilidad | Tests positivos y negativos |
| P04-T032 | Implementar bloqueo por claims o metricas nuevas en Presentation | QA / contrato | Implementation Agent | P04-T030, P04-T031 | Presentation falla si introduce evidencia, ratios o conclusiones fuera del CPS | Fixtures con claims/metrica no autorizados |
| P04-T033 | Implementar bloqueo por valoraciones historicas en Presentation | QA / contrato | Implementation Agent | P04-T032 | El report no puede declarar que recupera o supera valor historico | Fixture que reproduce el incidente menor de P03 |
| P04-T034 | Implementar bloqueo por causalidad no validada | QA / contrato | Implementation Agent | P04-T032 | Causalidad creativa, plataforma o comercial no validada queda bloqueada | Fixtures de causalidad prohibida |
| P04-T035 | Implementar bloqueo por degradacion de `UNKNOWN` o `not_available` | QA / contrato | Implementation Agent | P04-T032 | `UNKNOWN` no se convierte en conclusion y `not_available` no se oculta | Tests por estado de coverage |
| P04-T036 | Implementar bloqueo por recomendacion alterada | QA / contrato | Implementation Agent | P04-T032 | Presentation no reprioriza ni convierte experimentos en ordenes operativas | Tests de categoria, prioridad, criterio de exito y condicion de revision |

### 6.5 Manifest, trazabilidad y auditoria

| ID | Tarea | Tipo | Responsable sugerido | Depende de | Resultado esperado | Evidencia de finalizacion |
| --- | --- | --- | --- | --- | --- | --- |
| P04-T040 | Extender manifest de paquete futuro con referencia CPS | Trazabilidad | Implementation Agent | P04-T011 | Manifest registra CPS path, version, hash o fingerprint equivalente | Test de manifest |
| P04-T041 | Registrar lineage de artefactos canonicos consumidos | Trazabilidad | Implementation Agent | P04-T040 | Manifest o CPS permite reconstruir common core, Evidence, Knowledge, Recommendations, Coverage Matrix y Product Contract | Test de lineage completo |
| P04-T042 | Registrar estado de equivalencia por proyeccion | Trazabilidad / QA | Implementation Agent | P04-T030, P04-T031 | Cada proyeccion futura declara resultado de validacion semanticamente verificable | Manifest con estado PASS/FAIL o equivalente |
| P04-T043 | Registrar transformacion SPEC-010/SPEC-011 aplicada | Trazabilidad | Implementation Agent | P04-T040 | Seleccion de proyeccion y Communication Context quedan auditables sin consultar prompts originales | Validacion de campos obligatorios |

### 6.6 Pruebas y regresion documental

| ID | Tarea | Tipo | Responsable sugerido | Depende de | Resultado esperado | Evidencia de finalizacion |
| --- | --- | --- | --- | --- | --- | --- |
| P04-T050 | Crear suite de contrato para CPS | Tests | Implementation Agent | P04-T010 a P04-T016 | CPS falla si omite bloques compartidos obligatorios | Suite local PASS |
| P04-T051 | Crear suite de derivacion de proyecciones | Tests | Implementation Agent | P04-T020 a P04-T024 | Reports futuros no consumen fuentes no canonicas para contenido | Suite local PASS |
| P04-T052 | Crear suite de equivalencia semantica cruzada | Tests | Implementation Agent | P04-T030 a P04-T036 | Analytical y Executive conservan semantica compartida y variaciones permitidas | Suite local PASS |
| P04-T053 | Crear fixtures de regresion a partir del aprendizaje P03 | Tests | Implementation Agent | P04-T033, P04-T035, P04-T036 | Incidentes conocidos de P03 quedan cubiertos sin modificar outputs P03 | Fixtures locales PASS |
| P04-T054 | Validar que gaps futuros permanecen declarados | Tests / contrato | Implementation Agent | P04-T016, P04-T020, P04-T021 | Revenue/CRM, causalidad creativa, metadata adicional y temporalidad proveedor no se resuelven ni ocultan | Tests de presencia y no-promocion |
| P04-T055 | Ejecutar validacion local completa antes de QA | Validacion | Implementation Agent | P04-T050 a P04-T054 | Cambios tecnicos pasan pruebas y validadores | Resultado de comandos de test documentado en handoff |

### 6.7 Handoff y documentacion posterior

| ID | Tarea | Tipo | Responsable sugerido | Depende de | Resultado esperado | Evidencia de finalizacion |
| --- | --- | --- | --- | --- | --- | --- |
| P04-T060 | Preparar handoff de implementacion para Reviewer Agent | Handoff | Implementation Agent | P04-T055 | Reviewer recibe alcance, diffs, pruebas, riesgos y no-mutacion de outputs historicos | Handoff futuro creado por Implementation Agent |
| P04-T061 | Preparar handoff de QA para cierre tecnico | Handoff | Implementation Agent | P04-T060 | QA recibe checklist de SPEC-015 y evidencias verificables | Handoff futuro creado, sin decision de gate |
| P04-T062 | Actualizar documentacion canonica solo tras QA PASS | Documentacion | Documentation Agent | Gate futuro PASS | Indices reflejan implementacion aprobada y gaps dependientes de evidencia futura | Diffs documentales posteriores al PASS |

---

## 7. Matriz de trazabilidad SPEC-015 a tareas

| Requisito SPEC-015 | Tareas P04 |
| --- | --- |
| Definir `Canonical Projection Source` | P04-T010, P04-T011 |
| Contenido compartido obligatorio | P04-T012, P04-T050 |
| Vista integrada de senales y combinaciones | P04-T013, P04-T054 |
| Patrones de decision y narrativa autorizada | P04-T014, P04-T030, P04-T031 |
| Criterios de exito de recomendaciones | P04-T015, P04-T036 |
| Limitaciones, `UNKNOWN` y coverage states | P04-T016, P04-T035, P04-T054 |
| Variaciones permitidas analytical/executive | P04-T020, P04-T021, P04-T024 |
| Proyecciones hermanas | P04-T022, P04-T042 |
| Reglas de equivalencia semantica | P04-T030, P04-T031, P04-T052 |
| Bloqueos por nuevo conocimiento en Presentation | P04-T032 a P04-T036 |
| Prohibicion de valoracion historica en Presentation | P04-T033 |
| Trazabilidad reconstruible | P04-T040 a P04-T043 |
| Preservacion de gaps futuros | P04-T016, P04-T054, P04-T062 |
| Ausencia de nueva evidencia | P04-T003, P04-T054 |

---

## 8. Orden recomendado

1. Someter este plan a QA Gate Agent para Entry Gate de implementacion P04.
2. Si el Entry Gate aprueba, localizar puntos de integracion y confirmar no-mutacion historica: P04-T002 a P04-T004.
3. Implementar schema y constructor del `Canonical Projection Source`: P04-T010 a P04-T016.
4. Adaptar analytical y executive como proyecciones hermanas desde CPS: P04-T020 a P04-T024.
5. Implementar validadores y bloqueos de Presentation: P04-T030 a P04-T036.
6. Extender manifest y trazabilidad: P04-T040 a P04-T043.
7. Ejecutar pruebas y regresion documental: P04-T050 a P04-T055.
8. Preparar handoffs de Reviewer y QA: P04-T060 a P04-T061.
9. Actualizar documentacion canonica solo tras QA PASS futuro: P04-T062.

---

## 9. Condiciones de bloqueo

La implementacion futura debe detenerse si:

- no existe Entry Gate PASS o autorizacion equivalente;
- una tarea requiere nueva evidencia, BigQuery o ampliacion de fuentes;
- la solucion intenta modificar P02, P03 u outputs historicos;
- la solucion cambia SPEC-010, SPEC-011, SPEC-014 o SPEC-015;
- el CPS crea evidencia, Knowledge o Recommendations nuevos;
- una proyeccion consume directamente otra proyeccion como fuente semantica;
- Presentation introduce claims, metricas, recomendaciones, prioridades o valoraciones historicas no presentes en el CPS;
- se ocultan revenue/CRM `not_available`, causalidad creativa `UNKNOWN`, metadata adicional `not_available` o temporalidad limitada por proveedor;
- los validadores no pueden auditar equivalencia sin consultar prompts originales.

---

## 10. Criterios de finalizacion de P04 implementada

P04 podra considerarse implementada solo cuando exista evidencia verificable de que:

- el `Canonical Projection Source` existe antes de cualquier proyeccion;
- el CPS referencia common core, Evidence Set, Knowledge Set, Recommendation Set, Coverage Matrix y Product Contract;
- analytical y executive derivan del mismo CPS y no entre si;
- ambas proyecciones declaran origen canonico o queda registrado en manifest equivalente;
- claims, metricas, coverage states, limitaciones, exclusiones y recomendaciones son semanticamente equivalentes;
- los criterios de exito de experimentos o acciones son visibles en ambas proyecciones cuando correspondan;
- `UNKNOWN`, `partial`, `not_available`, `not_applicable` y `blocked` se preservan;
- Presentation bloquea nuevo conocimiento, causalidad no validada, comparativas historicas de valor y repriorizacion;
- los gaps dependientes de evidencia futura permanecen declarados y no resueltos;
- la suite local y los validadores contractuales pasan;
- QA puede validar desde artefactos fisicos o estructurados, no desde prompts.

---

## 11. Riesgos

| Riesgo | Impacto | Mitigacion planificada |
| --- | --- | --- |
| Convertir el CPS en una copia del common core sin enriquecer contenido de Presentation | No se recupera la riqueza validada en P03 | Tareas especificas para vista integrada, patrones y criterios de exito. |
| Crear un nuevo prompt canonico en lugar de un artefacto verificable | Persisten dependencias no auditables | Schema, manifest y validadores obligatorios. |
| Ejecutar mejoras narrativas dentro de Presentation | Riesgo de nuevo conocimiento no trazado | Bloqueadores P04-T032 a P04-T036. |
| Hacer Executive demasiado pobre por miedo a introducir conocimiento | Pierde valor para Direccion | Permitir condensacion con senales, decisiones, limites y criterios de exito derivados del CPS. |
| Hacer Analytical demasiado dependiente del formato P02 | Fragilidad ante variaciones validas | Validar equivalencia semantica, no igualdad textual. |
| Resolver gaps futuros sin evidencia | Deriva analitica y ruptura de boundary | Tests de no-promocion de gaps y precondicion sin BigQuery. |
| Actualizar documentacion antes de QA | Estado canonico prematuro | Documentacion posterior condicionada a QA PASS. |

---

## 12. Preparacion para Entry Gate

Este plan queda listo para revision de Entry Gate porque:

- parte de SPEC-015 aprobada;
- mantiene SPEC-010, SPEC-011 y SPEC-014 como dependencias no modificadas;
- separa CPS, Presentation, validadores, manifest, tests y documentacion;
- no ejecuta BigQuery;
- no implementa codigo;
- no genera outputs;
- no abre gates;
- protege P02, P03 y outputs historicos;
- define tareas, dependencias, criterios verificables, bloqueos y riesgos.

Decision de readiness del plan:

```text
READY FOR P04 ENTRY GATE REVIEW
```
