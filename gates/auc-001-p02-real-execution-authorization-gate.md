# AUC-001-P02 Real Execution Authorization Gate

## Metadatos

| Campo | Valor |
| --- | --- |
| Gate ID | AUC-001-P02-REAL-EXECUTION-AUTHORIZATION-GATE |
| Tipo | QA / Real Execution Authorization Gate |
| Categoria | Execution Authorization |
| Caso de uso padre | AUC-001 - Meta Lead Quality Analysis |
| Fase | AUC-001-P02 - Ejecucion real del Analytical Product Contract |
| Responsable | QA Gate Agent |
| Fecha | 2026-07-21 |
| Estado | Autorizado con condiciones |
| Decision | PASS WITH CONDITIONS - REAL EXECUTION AUTHORIZED VIA BIGQUERY MCP |

---

## 1. Proposito

Este gate evalua si AUC-001-P02 puede avanzar desde implementacion local validada hacia una ejecucion real controlada del Analytical Product Contract definido en SPEC-014.

La autorizacion permite al Implementation Agent ejecutar una corrida real de AUC-001-P02 usando exclusivamente el Runbook de AUC-001 y BigQuery MCP Server como Data Provider.

Este gate no ejecuta el analisis, no adquiere evidencia, no materializa outputs y no cierra P02.

---

## 2. Entradas Revisadas

| Artefacto | Estado | Resultado |
| --- | --- | --- |
| `specs/spec-014-auc-001-analytical-product-contract.md` | Cerrada | Fuente normativa vigente del Product Contract. |
| `gates/auc-001-p02-entry-gate.md` | PASS WITH CONDITIONS | Autorizo implementacion controlada, no ejecucion real. |
| `docs/evaluations/auc-001/validations/auc-001-p02-local-implementation-report.md` | Implementacion local completada; QA revalidation PASS | Evidencia de implementacion local. |
| `docs/evaluations/auc-001/validations/auc-001-p02-technical-functional-qa-validation.md` | PASS | Conformidad tecnica y funcional con SPEC-014. |
| `.github/skills/meta-lead-quality-analysis/RUNBOOK.md` | Vigente | Orden operativo obligatorio para ejecucion real. |
| `.github/skills/meta-lead-quality-analysis/references.md` | Vigente | Referencias oficiales y Data Provider autorizado. |
| `docs/contracts/bigquery-mcp-discover-metadata.contract.md` | Vigente | Contrato canonico de validacion MCP. |
| `configs/workspaces.json` | Vigente | Workspace `vca`, proyecto `datamart-vca-494114`, allowlist y limite de coste. |

---

## 3. Evaluacion Del Gate

| Verificacion | Resultado | Notas |
| --- | --- | --- |
| SPEC-014 esta aprobada y cerrada | PASS | La implementacion debe seguir SPEC-014 sin reinterpretarla. |
| P02 tiene Entry Gate previo | PASS | El gate previo autorizo implementacion local y exigio autorizacion posterior para ejecucion real. |
| Validacion tecnica y funcional P02 | PASS | QA revalido la implementacion local con decision `PASS`. |
| BigQuery MCP como unico Data Provider | PASS WITH CONDITIONS | Se autoriza su uso; la disponibilidad efectiva debe validarse en Fase 05 mediante `discover_metadata`. |
| Adquisicion de evidencia nueva | PASS WITH CONDITIONS | Autorizada solo despues de Data Provider Validation `PASS` o `PASS WITH OBSERVATION` segun Runbook. |
| Generacion de nucleo comun y matriz de cobertura | PASS WITH CONDITIONS | Debe derivar exclusivamente de evidencia y artefactos canonicos de la ejecucion actual. |
| Evidence, Knowledge y Recommendations | PASS WITH CONDITIONS | Deben estabilizarse en ese orden y sin mezclar responsabilidades. |
| Proyecciones analitica y ejecutiva | PASS WITH CONDITIONS | Solo pueden consumir el nucleo comun aprobado y preservar equivalencia semantica. |
| Persistencia en namespace nuevo y protegido | PASS WITH CONDITIONS | Autorizada solo en el namespace P02 definido por este gate; prohibido modificar namespaces historicos. |

---

## 4. Alcance Autorizado

El Implementation Agent queda autorizado a ejecutar AUC-001-P02 como ejecucion real completa, incluyendo:

- validacion de BigQuery MCP mediante `discover_metadata` canonico;
- adquisicion de evidencia nueva solo desde fuentes autorizadas por workspace y Data Contract;
- construccion y estabilizacion de Context Definition;
- construccion y estabilizacion de Evidence Set;
- generacion y estabilizacion de Knowledge Set;
- generacion y estabilizacion de Recommendation Set;
- construccion del nucleo comun del producto analitico;
- generacion de la matriz de cobertura conforme a SPEC-014;
- validacion de completitud por pregunta, criticidad, profundidad y robustez;
- generacion de proyeccion analitica desde el nucleo comun;
- generacion de proyeccion ejecutiva desde el nucleo comun;
- persistencia fisica de los artefactos de la ejecucion en un namespace nuevo y protegido.

---

## 5. Namespace Autorizado

El namespace autorizado para la ejecucion real P02 es:

```text
outputs/auc-001/p02/<execution-date-or-cutoff>/
```

El Implementation Agent debe resolver el segmento final del namespace a partir del Execution Context canonicalizado. Si la solicitud de ejecucion indica una fecha de corte explicita, debe usarse esa fecha como identificador del paquete salvo que el Runbook determine otra regla mas especifica.

El paquete persistido debe mantener separacion fisica minima entre:

```text
context/
evidence/
knowledge/
recommendations/
product-core/
coverage-matrix/
presentations/analytical/
presentations/executive/
execution/
qa/
```

La persistencia debe incluir un manifest o metadata equivalente que declare:

- execution_id;
- periodo canonicalizado;
- fecha de corte;
- fuentes autorizadas consultadas;
- version de SPEC-014;
- version del Product Contract runtime;
- fingerprint del nucleo comun;
- rutas de artefactos generados;
- resultado de Data Provider Validation;
- resultado de validacion de Product Contract;
- estado de completitud por pregunta y criticidad;
- lista de limitaciones, `UNKNOWN`, `not_available` y `partial` materiales.

---

## 6. Fuentes BigQuery MCP Autorizadas

La ejecucion solo puede consultar los recursos allowlisted del workspace `vca`:

| Dataset | Tabla | Selector canonico |
| --- | --- | --- |
| `intermediate` | `int_faro_lead_scoring` | `table:intermediate.int_faro_lead_scoring` |
| `marts` | `fct_spend` | `table:marts.fct_spend` |
| `marts` | `fct_lead_enriched` | `table:marts.fct_lead_enriched` |
| `marts` | `dim_campaign_signal` | `table:marts.dim_campaign_signal` |

Antes de consultar datos, Fase 05 debe validar:

```text
scope_request=workspace, resource_selector=workspace:vca
scope_request=dataset, resource_selector=dataset:intermediate
scope_request=dataset, resource_selector=dataset:marts
scope_request=table, resource_selector=table:intermediate.int_faro_lead_scoring
scope_request=table, resource_selector=table:marts.fct_spend
scope_request=table, resource_selector=table:marts.fct_lead_enriched
scope_request=table, resource_selector=table:marts.dim_campaign_signal
```

Cada llamada `query_read_only` debe usar `execution_context` cerrado con:

```yaml
project_id: datamart-vca-494114
dataset_id: intermediate|marts
max_bytes_billed: 1073741824
```

---

## 7. Condiciones Obligatorias De Ejecucion

| Condicion | Requisito |
| --- | --- |
| C01 | La ejecucion debe seguir estrictamente `.github/skills/meta-lead-quality-analysis/RUNBOOK.md` desde Fase 01 hasta Fase 13. |
| C02 | Antes de adquirir evidencia, debe completarse Data Provider Validation con BigQuery MCP y selectores canonicos. |
| C03 | Si `discover_metadata` devuelve `ERR_AUTH_REQUIRED`, `ERR_SELECTOR_INVALID`, `ERR_SCOPE_TOO_BROAD`, `ERR_RESOURCE_NOT_ALLOWLISTED` o una respuesta no interpretable, la ejecucion debe detenerse. |
| C04 | Esta prohibido usar BigQuery CLI, clientes directos, credenciales alternativas, outputs historicos o fallback. |
| C05 | La evidencia nueva solo puede proceder de consultas MCP autorizadas, exitosas y registradas. |
| C06 | Evidence debe contener hechos, metricas, cobertura, limitaciones y trazabilidad; no debe contener findings ni recomendaciones. |
| C07 | Knowledge debe derivar exclusivamente de Evidence estabilizada y debe preservar `UNKNOWN`, cobertura parcial, baja muestra e incertidumbre. |
| C08 | Recommendations deben derivar exclusivamente de Knowledge estabilizado y clasificarse como `measurable_experiment`, `verifiable_action` o `non_actionable_hypothesis`. |
| C09 | El nucleo comun debe preceder a las proyecciones y conservar periodo, scope, fuentes, evidence refs, metricas canonicas, matriz, Knowledge, recomendaciones, limitaciones y `UNKNOWN`. |
| C10 | La matriz de cobertura debe evaluarse por pregunta y criticidad; ninguna fila puede ser `complete` por presencia formal de una tabla o seccion. |
| C11 | Una fila `complete` no puede tener muestra `low_sample`, `insufficient` o `not_evaluable`; debe degradarse o bloquearse segun SPEC-014. |
| C12 | `not_available` debe distinguirse de `UNKNOWN` y debe incluir justificacion e impacto cuando aplique. |
| C13 | La ausencia de `ad_name` no bloquea AQ-005 por si sola si existe `ad_id_norm` o identificador tecnico equivalente y metricas trazables. |
| C14 | `ticket_status` sigue siendo condicional a fuente post-lead autorizada, trazable y reconciliada; no puede imputarse desde FARO. |
| C15 | La evolucion semanal solo puede declararse comparable con semanas completas o regla explicita para semanas parciales; la base mensual sigue siendo minima para AQ-009. |
| C16 | Las proyecciones analitica y ejecutiva no pueden introducir evidencia, Knowledge, Recommendations, cambios de coverage state, `UNKNOWN` o limitaciones nuevas. |
| C17 | La persistencia debe realizarse solo en `outputs/auc-001/p02/<execution-date-or-cutoff>/` y no puede modificar namespaces historicos. |
| C18 | El paquete generado debe quedar listo para QA fisico posterior desde disco; este gate no sustituye esa validacion. |

---

## 8. Explicitamente No Autorizado

Este gate no autoriza:

- uso de BigQuery CLI;
- uso de clientes directos de BigQuery;
- fuentes fuera del allowlist del workspace `vca`;
- ampliacion del Data Contract, Analytical Contract, SPEC-014 o Product Contract runtime;
- modificacion de `outputs/auc-001/2026-06-30/`;
- modificacion de `outputs/auc-001/pci-001/`;
- modificacion de `outputs/auc-001/pci-002/`;
- uso de reports historicos como evidence, expected values o fuente de nuevo conocimiento;
- inferencias causales no validadas;
- recomendaciones no trazadas a Knowledge;
- cierre de P02 sin QA fisico posterior;
- promocion de la capacidad a Foundation.

---

## 9. Condiciones De Bloqueo Durante La Ejecucion

La ejecucion real debe detenerse si ocurre cualquiera de estas condiciones:

- no puede resolverse el modo de ejecucion completa;
- falta una referencia obligatoria del Runbook;
- no puede identificarse el Data Contract vigente;
- BigQuery MCP no esta disponible o no valida identidad read-only;
- cualquier fuente necesaria no pertenece al allowlist autorizado;
- una consulta MCP falla y no puede registrarse como evidencia rechazada sin afectar la suficiencia minima;
- el Context Definition conserva pendientes materiales;
- Evidence mezcla universos, granularidades o periodos sin declararlo;
- Knowledge introduce evidencia nueva o recomendaciones;
- Recommendations no trazan a Knowledge;
- el nucleo comun no pasa validacion del Product Contract;
- una proyeccion rompe equivalencia semantica;
- la persistencia intenta escribir fuera del namespace autorizado;
- se detecta modificacion de namespaces historicos protegidos.

---

## 10. QA Posterior Requerido

Tras la ejecucion real, Implementation Agent debe entregar un handoff fisico para QA Gate Agent con:

- rutas exactas de todos los artefactos persistidos;
- manifest o metadata del paquete;
- resultado de Data Provider Validation;
- registro de consultas aceptadas y rechazadas;
- Evidence Set estabilizado;
- Knowledge Set estabilizado;
- Recommendation Set estabilizado;
- nucleo comun del producto;
- matriz de cobertura;
- proyeccion analitica;
- proyeccion ejecutiva;
- resultado del checklist final;
- declaracion de no modificacion de namespaces historicos.

QA Gate Agent debera validar fisicamente el paquete antes de cualquier cierre documental u operacional de P02.

---

## 11. Decision

```text
PASS WITH CONDITIONS - REAL EXECUTION AUTHORIZED VIA BIGQUERY MCP
```

AUC-001-P02 queda autorizado para ejecucion real controlada, adquisicion de evidencia nueva mediante BigQuery MCP y persistencia en namespace nuevo y protegido, sujeto a las condiciones de este gate.

La autorizacion no ejecuta el analisis, no genera outputs por si misma y no cierra P02.