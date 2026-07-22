# SPEC-016 - AUC-001 Operational Acceptance Package Contract

## Estado

Draft - ready for Reviewer Agent.

## Fecha

2026-07-22

## Ambito

AUC-001 operational consolidation before integral artifact consolidation.

## Titulo

Contrato operativo de paquete de ejecucion aceptable para AUC-001.

## Decision base

Esta Specification materializa el memo arquitectonico posterior a la prueba real end-to-end post-P04.

SPEC-016 no modifica la semantica de SPEC-014 ni SPEC-015.

SPEC-016 no modifica outputs historicos, no amplia fuentes, no modifica el BigQuery MCP Server y no redefine contratos del proveedor.

---

## 1. Proposito

Definir de forma verificable como una ejecucion real o controlada de AUC-001 debe quedar empaquetada, trazada, validada y entregada para revision.

El objetivo es impedir que una ejecucion analiticamente correcta quede operacionalmente fragil por:

* preflight MCP incompleto;
* consultas multi-tabla no controladas;
* registros MCP incompletos;
* uso accidental de consultas rechazadas como Evidence;
* fingerprints no reproducibles;
* contaminacion fisica del namespace;
* handoff incompleto;
* confusion entre `READY_FOR_REVALIDATION` y aceptacion final.

---

## 2. Relacion con Specifications existentes

| Specification | Rol | Relacion con SPEC-016 |
|---|---|---|
| SPEC-014 | Define suficiencia, profundidad, coverage, recomendaciones y limites del producto analitico. | SPEC-016 bloquea la ejecucion si la evidencia adquirida no permite cumplir el grano requerido por SPEC-014. |
| SPEC-015 | Define `Canonical Projection Source` y equivalencia semantica entre proyecciones. | SPEC-016 exige que el paquete demuestre fisicamente que CPS existe antes de reports y que ambas proyecciones derivan de el. |

SPEC-016 es un contrato operativo de paquete. No es un contrato de producto ni de Presentation.

---

## 3. Boundary

### Incluye

* preflight MCP obligatorio;
* estrategia canonica de adquisicion AUC-001;
* registro completo de llamadas MCP;
* separacion entre consultas exitosas, rechazadas y descartadas;
* preservacion de `matched`, `lead_only` y `spend_only`;
* bloqueo por grano insuficiente para SPEC-014;
* contrato fisico del execution package;
* manifest, fingerprints y physical traceability reproducibles;
* higiene del namespace;
* handoff verificable;
* separacion de estados de paquete y aceptacion final.

### Excluye

* cambios en SPEC-014 o SPEC-015;
* nuevas fuentes o tablas;
* cambios en Data Contract;
* cambios en BigQuery MCP Server;
* adquisicion de evidencia fuera de MCP;
* modificacion de outputs historicos;
* cambios semanticos en Evidence, Knowledge, Recommendations, CPS o reports.

---

## 4. Preflight MCP obligatorio

Antes de ejecutar cualquier consulta de evidencia, la ejecucion debe producir un `mcp-preflight-record`.

El preflight debe validar:

* workspace resuelto;
* mecanismo de acceso MCP;
* proyecto autorizado;
* datasets autorizados;
* tablas allowlisted;
* contrato cerrado de `execution_context`;
* limite `max_bytes_billed`;
* estrategia de consulta por tabla;
* grano requerido por SPEC-014;
* politica de rechazo y descarte.

El preflight debe bloquear si:

* falta una fuente necesaria;
* una tabla no esta allowlisted;
* `execution_context` contiene campos no permitidos;
* el dataset de `execution_context.dataset_id` no coincide con la tabla consultada;
* el grano planificado no permite responder una pregunta obligatoria de SPEC-014 sin inferencia;
* la estrategia requiere una consulta multi-tabla MCP para generar Evidence.

---

## 5. Estrategia canonica de adquisicion AUC-001

AUC-001 debe adquirir evidencia mediante consultas independientes por tabla o recurso autorizado.

La reconciliacion entre tablas debe hacerse localmente, dentro del proceso de construccion de Evidence Set, usando salidas MCP exitosas y trazadas.

La estrategia canonica es:

1. consultar `marts.fct_lead_enriched` para hechos de leads, FARO, formularios, plataforma, ticket/status disponible y granularidades de lead;
2. consultar `intermediate.int_faro_lead_scoring` para componentes de scoring cuando se requiera explicar FARO;
3. consultar `marts.fct_spend` para spend, campana, anuncio, signal y granularidades economicas;
4. consultar `marts.dim_campaign_signal` como dimension descriptiva cuando aplique;
5. reconciliar localmente por claves tecnicas autorizadas, manteniendo universos separados.

Queda prohibido usar una consulta MCP multi-tabla como fuente primaria de Evidence para AUC-001.

Una consulta multi-tabla puede aparecer solo como intento rechazado, descartado o diagnostico no-evidencial, y debe registrarse como `used_as_evidence: false`.

---

## 6. Preservacion de universos reconciliados

Todo paquete que trate coste-calidad debe preservar explicitamente:

* `matched`;
* `lead_only`;
* `spend_only`;
* `UNKNOWN` cuando aplique.

La reconciliacion local no puede:

* convertir `lead_only` en coste cero;
* convertir `spend_only` en ausencia real de leads;
* ocultar `UNKNOWN`;
* mezclar granularidades sin declararlo;
* calcular eficiencia economica sin universo y denominador.

Si los resultados adquiridos no permiten reconstruir estos universos, el paquete debe bloquear antes de Knowledge.

---

## 7. Bloqueo por grano insuficiente

El paquete debe declarar el grano adquirido por consulta y por vista requerida.

Debe bloquearse si el grano no permite cumplir SPEC-014 para una pregunta obligatoria alta, incluyendo:

* AQ-001: periodo y evolucion minima;
* AQ-002: distribucion FARO con denominador;
* AQ-003: coste-calidad reconciliada;
* AQ-004: campana/adset o equivalente con cobertura;
* AQ-006: senales explicativas autorizadas;
* AQ-007: trade-off volumen-calidad-coste;
* AQ-009: temporalidad minima mensual;
* AQ-010: recomendaciones derivables de Knowledge;
* AQ-011: limites, `UNKNOWN` y coverage.

Un grano parcial puede ser conforme solo cuando SPEC-014 permite `partial`, el impacto esta declarado y no se presenta como completitud.

---

## 8. Registro completo de llamadas MCP

El `evidence-acquisition-record` debe contener un registro por cada llamada MCP relevante:

* metadata discovery;
* query preflight si usa MCP;
* consultas exitosas;
* consultas rechazadas;
* consultas descartadas antes de convertirse en Evidence;
* intentos diagnosticos no-evidenciales.

Cada registro debe incluir como minimo:

* `call_type`;
* SQL completo cuando exista;
* selector MCP cuando aplique;
* `execution_context`;
* dataset y tablas;
* periodo y filtros;
* granularidad;
* estado de dry run y control de coste;
* resultado o error;
* `request_id`;
* `trace_reference`;
* bytes procesados cuando esten disponibles;
* `used_as_evidence`;
* razon de descarte cuando no se use como Evidence.

Las consultas rechazadas o descartadas nunca pueden alimentar Evidence, Knowledge, Recommendations, CPS ni Presentation.

---

## 9. Contrato fisico del execution package

Todo paquete conforme debe persistir, como minimo:

```text
execution/
  manifest.json
  physical-traceability.json
  mcp-preflight-record.json
  evidence-acquisition-record.json
  test-results.json
  semantic-equivalence-validation.json
evidence/
  evidence-set.json
knowledge/
  knowledge-set.json
recommendations/
  recommendation-set.json
product-core/
  common-product-core.json
  canonical-projection-source.json
validations/
  spec-014-validation.json
  spec-015-validation.json
  spec-016-validation.json
handoff/
  reviewer-qa-handoff.md
```

Los nombres pueden variar solo si `manifest.json` permite reconstruir inequivocamente los roles.

---

## 10. Manifest, fingerprints y trazabilidad fisica

El manifest debe declarar:

* instruccion original;
* modo de ejecucion;
* namespace;
* gate o autorizacion aplicable;
* source policy;
* estrategia de adquisicion;
* rutas de artefactos;
* fingerprints de artefactos firmables;
* CPS id y fingerprint;
* resultados SPEC-014, SPEC-015 y SPEC-016;
* estado `READY_FOR_REVALIDATION` o bloqueo;
* ausencia de aceptacion final.

La politica de fingerprints debe ser reproducible.

Regla canonica:

* `artifact_fingerprints` firma artefactos estables del paquete;
* `manifest.json`, `physical-traceability.json` y `test-results.json` se excluyen de `artifact_fingerprints` para evitar mutacion recursiva;
* `physical-traceability.json` firma el hash final de `manifest.json` y `test-results.json`;
* cualquier artefacto de cierre posterior debe declararse explicitamente en `physical-traceability.json` o generar una revision nueva.

---

## 11. Higiene del namespace

El namespace de outputs no puede contener:

* `__pycache__`;
* `.pyc`;
* temporales de editor;
* logs locales no trazables;
* credenciales;
* artefactos fuera del manifest salvo que se declaren como auxiliares no firmados.

La validacion fisica debe ejecutarse despues de limpiar y antes de entregar handoff.

---

## 12. Handoff verificable

El handoff debe incluir:

* instruccion original;
* namespace;
* estado del paquete;
* resumen de estrategia MCP;
* lista de artefactos;
* comandos exactos ejecutados;
* resultado de cada comando;
* limitaciones y desviaciones;
* consultas rechazadas o descartadas;
* confirmacion de no CLI/fallback;
* confirmacion de no modificacion de historicos;
* distincion entre `READY_FOR_REVALIDATION` y aceptacion final.

Un paquete sin handoff verificable no puede avanzar a Reviewer Agent.

---

## 13. Estados de paquete y aceptacion

Estados validos de paquete:

| Estado | Significado |
|---|---|
| `BLOCKED` | La ejecucion no puede producir paquete aceptable. |
| `READY_FOR_REVALIDATION` | El paquete fue generado y validado por Implementation, pendiente de Reviewer/QA. |
| `REJECTED_BY_REVIEW` | Reviewer o QA detectaron condiciones abiertas. |
| `FINAL_ACCEPTED` | QA Gate emitio aceptacion final y el paquete fue actualizado o referenciado por cierre formal. |

Implementation Agent no puede declarar aceptacion final.

La aceptacion final corresponde a QA Gate Agent y debe quedar como artefacto separado o como revision controlada del paquete.

---

## 14. Gap separado: consultas multi-tabla MCP

La prueba post-P04 evidencio que determinadas formas multi-tabla pueden recibir `ERR_SCOPE_DENIED` aunque las tablas individuales esten autorizadas.

SPEC-016 adopta una estrategia canonica que no depende de consultas multi-tabla MCP.

El gap debe registrarse por separado como dependencia operativa del proveedor, sin modificar el servidor MCP ni ampliar fuentes.

---

## 15. Criterios de aceptacion

SPEC-016 esta lista para Reviewer Agent si:

* define preflight MCP obligatorio;
* exige estrategia de consultas independientes por tabla;
* preserva `matched`, `lead_only` y `spend_only`;
* bloquea por grano insuficiente para SPEC-014;
* exige registro completo de llamadas MCP;
* prohibe usar consultas rechazadas como Evidence;
* define contrato fisico de paquete;
* define manifest, fingerprints y physical traceability reproducibles;
* define higiene de namespace;
* define handoff verificable;
* separa `READY_FOR_REVALIDATION` de aceptacion final;
* registra por separado el gap multi-tabla MCP;
* no cambia SPEC-014, SPEC-015, outputs historicos ni servidor MCP.

