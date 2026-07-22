# RUNBOOK - Meta Lead Quality Analysis

## Proposito

Definir el unico orden operativo canonico para ejecutar AUC-001 despues de activar la skill `meta-lead-quality-analysis`.

`SKILL.md` define activacion, alcance, modos e invariantes. Este Runbook define fases, inputs, acciones, outputs, gates, criterios de estabilizacion y manejo de bloqueos operativos.

## Workflow canonico

1. Skill Activation and Execution Mode Resolution.
2. Preliminary Request Resolution.
3. Official Context Loading.
4. Execution Context Canonicalization.
5. Data Provider Validation.
6. Context Definition Stabilization.
7. Evidence Acquisition.
8. Evidence Set Construction and Stabilization.
9. Knowledge Generation and Stabilization.
10. Recommendation Generation and Stabilization.
11. Canonical Content Validation Gate.
12. Canonical Projection Source and Presentation Materialization.
13. Final Checklist and Delivery.

## Fase 01 - Skill Activation and Execution Mode Resolution

Input:

- solicitud del usuario;
- `SKILL.md`;
- restricciones explicitas de la conversacion.

Acciones:

- confirmar que la solicitud pertenece a AUC-001 o a Meta lead quality analysis;
- resolver si la ejecucion es completa o representacion de un Evidence Set existente;
- registrar restricciones explicitamente indicadas por el usuario;
- detener si el modo no puede resolverse sin cambiar materialmente la peticion.

Output:

- modo de ejecucion resuelto;
- restricciones operativas iniciales.

Gate:

- no continuar si el modo solicitado es incompatible con una ejecucion completa;
- no continuar si el usuario prohibe el Data Provider obligatorio para el modo solicitado;
- la disponibilidad tecnica del BigQuery MCP Server se valida exclusivamente en la Fase 05.

Definition of Done:

- el modo esta resuelto y no contradice la solicitud del usuario.

## Fase 02 - Preliminary Request Resolution

Input:

- solicitud original;
- modo de ejecucion;
- restricciones iniciales.

Acciones:

- identificar objetivo, audiencia, tipo de salida, fecha de corte expresada, alcance aparente y restricciones;
- crear un Provisional Context Definition;
- si la solicitud usa `hasta [fecha]` sin fecha inicial, registrar la fecha indicada como cutoff y dejar el inicio como `PENDING_START_FROM_PROVIDER_COVERAGE`;
- no llamar estable al Context Definition en esta fase.

Output:

- Provisional Context Definition.

Gate:

- solicitar aclaracion solo si una ambiguedad cambia materialmente la ejecucion.

Definition of Done:

- existe un contexto provisional explicito con campos pendientes marcados, no inferidos.

## Fase 03 - Official Context Loading

Input:

- Provisional Context Definition;
- `references.md`.

Acciones:

- leer las fuentes oficiales aplicables: `docs/context_refs.md`, Analytical Use Case, Data Contract, Presentation Contract, CCD, FARO, CLARO, KPIs oficiales y `project_brief.md` cuando aplique;
- aplicar las definiciones oficiales por encima de inferencias del modelo de datos;
- registrar referencias ausentes o rutas rotas como limitaciones o bloqueos segun impacto.

Output:

- contexto oficial cargado;
- definiciones aplicables identificadas.

Gate:

- detener si falta una fuente obligatoria sin la cual no pueda verificarse el alcance.

Definition of Done:

- las fuentes obligatorias han sido cargadas o su ausencia queda registrada con decision de continuar o bloquear.

## Fase 04 - Execution Context Canonicalization

Input:

- Provisional Context Definition;
- contexto oficial cargado;
- contratos;
- CCD y definiciones oficiales;
- restricciones del caso y alcance solicitado.

Acciones:

- canonicalizar objetivo, periodo, fecha de corte, alcance, definicion de calidad, audiencia, tipo de salida y restricciones;
- aplicar contratos, CCD, definiciones oficiales, restricciones del caso y alcance solicitado;
- mantener como pendientes los campos que dependan del proveedor, como fecha inicial real o cobertura temporal;
- cuando la solicitud use `hasta [fecha]` sin fecha inicial, no sustituir automaticamente por el mes natural;
- usar mes natural solo si el usuario lo solicita explicitamente o existe restriccion contractual aplicable;
- registrar divergencias entre solicitud y alcance contractual.

Output:

- Execution Context canonicalizado con posibles campos dependientes del proveedor aun pendientes.

Gate:

- detener si el alcance contractual contradice materialmente la peticion y requiere aclaracion.

Definition of Done:

- el Execution Context esta canonicalizado y los campos pendientes estan nombrados explicitamente.

## Fase 05 - Data Provider Validation

Input:

- Execution Context canonicalizado;
- Data Contract;
- `configs/workspaces.json`;
- BigQuery MCP Server;
- contrato canonico observado de `discover_metadata`: `docs/contracts/bigquery-mcp-discover-metadata.contract.md`.

Acciones:

- resolver workspace;
- verificar mecanismo de acceso;
- confirmar MCP disponible;
- ejecutar y registrar preflight MCP obligatorio antes de cualquier consulta analitica;
- ejecutar `discover_metadata` usando exclusivamente el selector canonico publicado en `docs/contracts/bigquery-mcp-discover-metadata.contract.md`;
- verificar proyecto, datasets, tablas, allowlist y Data Contract a partir de los recursos autorizados necesarios para AUC-001;
- descubrir esquemas necesarios mediante MCP usando una unica forma canonica por recurso;
- verificar cobertura temporal;
- resolver campos dependientes del proveedor, incluido el inicio real si estaba en `PENDING_START_FROM_PROVIDER_COVERAGE`;
- confirmar que cada tabla pertenece al Data Contract y al workspace seleccionado;
- no probar formatos alternativos, FQN con proyecto, nombres logicos inferidos ni secuencias exploratorias durante una ejecucion analitica normal.

Output:

- Data Provider validado;
- fuentes autorizadas;
- cobertura temporal y campos dependientes del proveedor resueltos o bloqueados;
- resultado de fase: `PASS`, `PASS WITH OBSERVATION` o `FAIL`.

Gate:

- detener si el workspace no resuelve, MCP no esta disponible, una fuente necesaria no esta autorizada o una tabla no pertenece al Data Contract;
- detener si `discover_metadata` devuelve `ERR_AUTH_REQUIRED`, `ERR_SELECTOR_INVALID`, `ERR_RESOURCE_NOT_ALLOWLISTED`, un alcance no corregible o una respuesta no interpretable de forma segura.

### Contrato canonico de discover_metadata

El contrato real del servidor no se redefine en este Runbook. La referencia canonica para AUC-001 es:

```text
docs/contracts/bigquery-mcp-discover-metadata.contract.md
```

La Fase 05 debe construir sus llamadas desde esa referencia antes de iniciar la ejecucion. Para el workspace `vca`, las formas canonicas vigentes son:

```text
scope_request=workspace, resource_selector=workspace:vca
scope_request=dataset, resource_selector=dataset:intermediate
scope_request=dataset, resource_selector=dataset:marts
scope_request=table, resource_selector=table:intermediate.int_faro_lead_scoring
scope_request=table, resource_selector=table:marts.fct_spend
scope_request=table, resource_selector=table:marts.fct_lead_enriched
scope_request=table, resource_selector=table:marts.dim_campaign_signal
```

No estan permitidos los selectores con prefijo de proyecto, valores legacy plurales de `scope_request`, nombres de tabla sin dataset, comodines ni formatos no publicados por el schema actual del servidor.

### Interpretacion de errores de discover_metadata

| Error | Interpretacion | Comportamiento obligatorio |
|---|---|---|
| `ERR_AUTH_REQUIRED` | Credenciales ausentes, invalidas, identidad efectiva no aceptada o imposibilidad de validar la identidad read-only. | Detener. No probar otros selectores. No ejecutar consultas analiticas. Solicitar intervencion solo si hace falta renovar ADC, reiniciar servidor u otra accion local. |
| `ERR_SELECTOR_INVALID` | Tipo, campo, estructura o formato de selector incompatible con el contrato del servidor. | Detener la validacion. Registrar contrato esperado y selector enviado. Tratar como incompatibilidad entre `vca-ai` y servidor. |
| `ERR_SCOPE_TOO_BROAD` | Selector valido, pero alcance superior al permitido para la operacion. | Aplicar como maximo una reduccion determinista documentada antes de la ejecucion. No explorar recursos adicionales. |
| `ERR_RESOURCE_NOT_ALLOWLISTED` | Selector valido, pero recurso fuera del allowlist autorizado. | Detener para ese recurso. No buscar fuentes alternativas, no usar CLI, no usar historico y no modificar allowlist durante la ejecucion analitica. |

El schema observado actualmente no publica ningun codigo especifico de indisponibilidad funcional de `discover_metadata`. Por tanto, la ruta `PASS WITH OBSERVATION` no esta activa para ejecuciones actuales. Si el servidor publica en el futuro un codigo especifico de indisponibilidad funcional que no afecte a autenticacion, selector, alcance ni allowlist, la Fase 05 podra validar alternativamente mediante `query_read_only` solo cuando:

- la identidad MCP ya este validada;
- el selector enviado sea conforme al contrato canonico;
- la tabla este incluida en el allowlist;
- la consulta MCP sea minima y confirme acceso, existencia, esquema o cobertura minima;
- no se adquiera todavia evidencia analitica completa.

En ese caso el resultado debe registrarse como:

```text
Data Provider Validation: PASS WITH OBSERVATION
Provider: BigQuery MCP Server
Identity: validated
Metadata discovery: functionally unavailable
Access validation: query_read_only successful
Fallback outside MCP: not used
```

`query_read_only` no cambia y no es fallback externo. BigQuery CLI, credenciales alternativas, claves JSON, informes historicos y tablas fuera del allowlist permanecen prohibidos.

### Estados de salida de Fase 05

| Estado | Criterio |
|---|---|
| `PASS` | `discover_metadata` funciona, identidad valida, recursos autorizados confirmados y esquemas disponibles. |
| `PASS WITH OBSERVATION` | Reservado para un codigo funcional explicito publicado por el servidor en el futuro; actualmente no hay codigo oficial observado que active esta ruta. |
| `FAIL` | Autenticacion invalida, incompatibilidad de contrato, recurso fuera del allowlist, alcance no corregible, acceso denegado o respuesta MCP no interpretable con seguridad. |

### Convenciones SQL seguras para BigQuery MCP

Antes de enviar una consulta mediante `query_read_only`, revisar la SQL contra estas convenciones locales, derivadas del diagnostico AUC-001 v2:

- Construir `execution_context` como contrato cerrado. Debe contener exactamente estos campos:

```yaml
execution_context:
  project_id: <authorized_project_id>
  dataset_id: <authorized_dataset_id>
  max_bytes_billed: <workspace_cost_limit_bytes>
```

- Para el workspace `vca`, usar:

```yaml
execution_context:
  project_id: datamart-vca-494114
  dataset_id: intermediate|marts
  max_bytes_billed: 1073741824
```

- El `dataset_id` debe coincidir con el dataset de cada tabla consultada:
  - `intermediate` para consultas sobre `datamart-vca-494114.intermediate.*`.
  - `marts` para consultas sobre `datamart-vca-494114.marts.*`.
- No incluir dentro de `execution_context` campos descriptivos o no soportados, incluidos:
  - `workspace_id`;
  - `table_id`;
  - `purpose`;
  - `request_id`;
  - `resource_selector`;
  - `location`;
  - `auth_mode`;
  - cualquier otro campo no enumerado en el contrato cerrado.
- Mantener la separacion de responsabilidades de la llamada MCP:
  - `request_id` va en el nivel superior de la llamada;
  - la SQL va en `sql_query`;
  - la trazabilidad adicional va en artefactos de ejecucion o auditoria;
  - nada de lo anterior debe incorporarse dentro de `execution_context`.

- No usar `rows` como alias de columna.
  - Incorrecto: `COUNT(*) AS rows`
  - Correcto: `COUNT(*) AS row_count`
  - Tambien validos: `lead_count`, `spend_row_count`, `qualified_lead_count`.
- No reutilizar nombres dentro de una misma consulta.
  - Un nombre de CTE no debe reutilizarse como alias de columna.
  - Los aliases de columnas agregadas deben ser explicitos y unicos.
- No usar joins implicitos con coma.
  - Incorrecto: `FROM table_a, table_b`
  - Correcto: `FROM table_a CROSS JOIN table_b`
  - Preferir `JOIN ... ON`, `JOIN ... USING` o consultas separadas cuando sea mas claro.
- Antes de enviar la consulta MCP, comprobar aliases reservados, colisiones entre CTEs y columnas, referencias ambiguas, joins con coma y que el `execution_context` contiene exactamente `project_id`, `dataset_id` y `max_bytes_billed`.
- Ante `ERR_DRY_RUN_FAILED`, no repetir la misma forma con cambios irrelevantes; simplificar la consulta, revisar sintaxis y tipos, usar aliases explicitos y registrar la consulta rechazada como evidencia no utilizable.

Definition of Done:

- todas las fuentes que se consultaran estan autorizadas, verificadas y tienen cobertura conocida o limitacion explicita.
## Fase 06 - Context Definition Stabilization

Input:

- Execution Context canonicalizado;
- cobertura temporal validada;
- fuentes autorizadas;
- campos dependientes del proveedor resueltos.

Acciones:

- cerrar el Stabilized Context Definition;
- sustituir `PENDING_START_FROM_PROVIDER_COVERAGE` por la fecha inicial real o declarar bloqueo;
- registrar solicitud original, regla temporal aplicada, periodo final, scope, calidad, audience, restricciones, fuentes y divergencias.

Output:

- Stabilized Context Definition.

Gate:

- no construir Evidence Set si el Context Definition conserva pendientes materiales.

Definition of Done:

- existe un Context Definition estabilizado, explicito y trazable.

## Fase 07 - Evidence Acquisition

Input:

- Stabilized Context Definition;
- Data Provider validado;
- convenciones SQL BigQuery MCP.

Acciones:

- ejecutar consultas mediante BigQuery MCP Server cuando se requiera evidencia nueva;
- aplicar la estrategia canonica vigente: consultas independientes por tabla autorizada y reconciliacion local controlada, preservando `matched`, `lead_only`, `spend_only` y `UNKNOWN`;
- registrar SQL, request_id, execution_context, tablas, periodo, filtros, granularidad, dry run, coste estimado, bytes procesados, resultado, policy decision, trace ID y coverage;
- registrar consultas rechazadas, descartadas y su causa publica;
- no usar consultas rechazadas o descartadas como evidencia;
- no usar fallback, CLI ni clientes directos cuando el modo exige MCP.

Output:

- Evidence Acquisition Record con consultas exitosas y rechazadas separadas.

Gate:

- detener si no hay evidencia suficiente para construir el Evidence Set sin inferir.

Definition of Done:

- toda metrica candidata procede de una consulta autorizada y exitosa, o queda descartada como no utilizable.

## Fase 08 - Evidence Set Construction and Stabilization

Input:

- Evidence Acquisition Record;
- Stabilized Context Definition;
- Data Contract.

Acciones:

- construir hechos, metricas derivadas, coverage states, limitaciones, UNKNOWNs y trazabilidad;
- preservar `matched`, `lead_only`, `spend_only` y `UNKNOWN` cuando apliquen;
- excluir outputs rechazados o no verificables;
- separar hechos de interpretacion;
- no generar findings ni recomendaciones.

Output:

- Evidence Set estabilizado.

Gate:

- detener si la evidencia mezcla universos, granularidades o periodos sin declararlo.

Definition of Done:

- existe un Evidence Set trazable, cerrado y libre de interpretacion.

## Fase 09 - Knowledge Generation and Stabilization

Input:

- Evidence Set estabilizado;
- `ANALYTICAL_PROFILE.md`;
- `knowledge-construction-profile.md`.

Acciones:

- derivar conocimiento exclusivamente desde el Evidence Set estabilizado;
- aplicar los perfiles analiticos correspondientes;
- ejecutar un programa de investigacion analitica antes de estabilizar el Knowledge Set;
- seleccionar preguntas de negocio adaptadas a la evidencia disponible, incluyendo volumen, calidad, eficiencia, variables explicativas, equilibrio volumen-calidad-coste, trade-offs, patrones, anomalias, robustez y limitaciones cuando apliquen;
- aplicar operaciones analiticas compuestas, no solo lectura de tablas: segmentacion, comparacion, ranking multicriterio, analisis temporal, analisis relacional, combinaciones de variables, concentracion, cobertura, materialidad, robustez y contraste entre explicaciones alternativas;
- construir un Analytical Investigation Record interno con findings intermedios trazados al Evidence Set;
- para cada finding intermedio, registrar que se observa, que evidencia lo soporta, por que importa, que incertidumbre permanece y con que otros findings se relaciona;
- descartar observaciones que no superen el umbral de materialidad, robustez o utilidad para decision;
- consolidar findings relacionados en Knowledge: insights, hipotesis, conclusiones, prioridades, riesgos e incertidumbres;
- distinguir afirmaciones solidas, hipotesis observacionales y UNKNOWNs;
- conservar limitaciones, coverage states e incertidumbre;
- estabilizar el Knowledge Set antes de cualquier recomendacion;
- ejecutar una operacion explicita de Knowledge Synthesis / Analytical Narrative despues de estabilizar el Knowledge Set y antes de Recommendation Generation;
- construir la Analytical Narrative unicamente desde Context Definition, Knowledge Set estabilizado, limitaciones, UNKNOWNs, coverage states y niveles de confianza ya registrados;
- responder obligatoriamente en la Analytical Narrative: fenomeno principal, relaciones entre Knowledge items, findings estructurales y secundarios, trade-off principal, riesgo o limitacion dominante, implicacion estrategica e idea central memorable;
- mantener la Analytical Narrative breve y densa, como tesis integrada, no como lista adicional de insights;
- prohibir que la Analytical Narrative consulte BigQuery, Evidence Set bruto, tablas, outputs historicos, Recommendation Set o informes anteriores;
- prohibir que la Analytical Narrative genere nuevos findings, nuevo Knowledge, recomendaciones encubiertas o transformacion propia de Presentation Layer;
- no formular recomendaciones.

Output:

- Analytical Investigation Record interno;
- Knowledge Set estabilizado;
- Analytical Narrative / Strategic Interpretation estabilizada.

Gate:

- detener si no existe investigacion analitica previa al Knowledge Set;
- detener si los findings intermedios no estan trazados al Evidence Set;
- detener si el Knowledge Set solo repite metricas, rankings o tablas sin explicar significado, trade-offs, patrones, relaciones o limites;
- detener si el Knowledge Set introduce hechos no presentes en Evidence o recomendaciones prematuras;
- detener si la Analytical Narrative no deriva exclusivamente del Knowledge Set estabilizado;
- detener si la Analytical Narrative introduce recomendaciones, nueva evidencia, nuevo Knowledge o adaptacion de Presentation;
- detener si la Analytical Narrative se limita a repetir insights sin construir una tesis integrada.

Definition of Done:

- existe un Analytical Investigation Record trazable, usado como puente interno entre Evidence y Knowledge;
- existe un Knowledge Set consolidado, explicativo y derivado exclusivamente del Evidence Set;
- el Knowledge Set responde a las principales preguntas de negocio soportadas por la evidencia y declara explicitamente lo que no puede concluirse;
- existe una Analytical Narrative breve, trazable y derivada exclusivamente del Knowledge Set estabilizado;
- la Analytical Narrative identifica fenomeno principal, relaciones entre Knowledge items, hallazgos estructurales y secundarios, trade-off, riesgo dominante, implicacion estrategica e idea central memorable;
- la Analytical Narrative no introduce recomendaciones ni contenido no aprobado.

## Fase 10 - Recommendation Generation and Stabilization

Input:

- Knowledge Set estabilizado;
- restricciones del caso;
- prioridades y riesgos identificados.

Acciones:

- derivar recomendaciones exclusivamente del Knowledge Set;
- incluir prioridad, accion, soporte, riesgo, impacto esperado y validacion posterior;
- no introducir recomendaciones sin finding de soporte;
- estabilizar el Recommendation Set antes de Presentation.

Output:

- Recommendation Set estabilizado.

Gate:

- detener si existen recomendaciones no trazadas a Knowledge.

Definition of Done:

- todas las recomendaciones son trazables, priorizadas y derivadas del Knowledge Set.

## Fase 11 - Canonical Content Validation Gate

Input:

- Stabilized Context Definition;
- Evidence Set estabilizado;
- Knowledge Set estabilizado;
- Recommendation Set estabilizado.

Acciones:

- comprobar consistencia, trazabilidad, separacion Evidence/Knowledge/Recommendations, coverage states, UNKNOWNs, limitaciones, prioridades y equivalencia semantica;
- construir y validar Coverage Matrix y Common Product Core conforme a SPEC-014;
- construir y validar Canonical Projection Source conforme a SPEC-015 antes de cualquier informe;
- confirmar que Evidence no contiene interpretacion;
- confirmar que Knowledge no introduce evidencia nueva;
- confirmar que Recommendations derivan de Knowledge;
- no corregir inconsistencias dentro de Presentation.

Output:

- Canonical Content Validation result;
- Coverage Matrix validada;
- Common Product Core validado;
- Canonical Projection Source validado.

Gate:

- si falla la validacion, detener la ejecucion antes de Presentation.

Definition of Done:

- los artefactos canonicos, Common Product Core y Canonical Projection Source estan listos para representarse sin reconstruccion.

## Fase 12 - Canonical Projection Source and Presentation Materialization

Input:

- artefactos canonicos estabilizados;
- Common Product Core;
- Canonical Projection Source;
- Presentation Contract;
- Presentation Projection;
- Communication Context;
- Representation Constraints;
- Presentation Policy aplicable, cuando exista.

Acciones:

- resolver Presentation Projection;
- resolver Communication Context;
- resolver Representation Constraints;
- aplicar Presentation Policy cuando exista;
- consumir solo el Canonical Projection Source y artefactos estabilizados autorizados;
- materializar analytical report y executive report como proyecciones hermanas cuando ambas se soliciten;
- impedir derivacion entre proyecciones;
- no consultar datos;
- no generar evidencia;
- no generar nuevo conocimiento;
- no generar nuevas recomendaciones;
- preservar equivalencia semantica, coverage states, UNKNOWNs, limitaciones y prioridades.

Output:

- Presentation materializada.

Gate:

- detener si la representacion requiere modificar contenido canonico o inventar informacion.

Definition of Done:

- la Presentation comunica el contenido canonico sin alterarlo ni reconstruirlo.

## Fase 13 - Final Checklist and Delivery

Input:

- Presentation materializada;
- artefactos canonicos estabilizados;
- `CHECKLIST.md`.

Acciones:

- ejecutar `CHECKLIST.md`;
- confirmar fuentes;
- confirmar MCP-only cuando aplique;
- declarar artefactos consumidos;
- declarar proyeccion;
- declarar policy aplicada, cuando exista;
- confirmar aislamiento historico;
- confirmar trazabilidad;
- confirmar preservacion de limitaciones y UNKNOWNs;
- cuando exista execution package, validar contrato fisico SPEC-016: manifest, fingerprints, physical traceability, registros MCP completos, resultados de validacion, higiene de namespace y handoff con comandos/resultados;
- distinguir `READY_FOR_REVALIDATION` de aceptacion final por QA Gate.

Output:

- entrega final;
- resultado de checklist;
- limitaciones y desviaciones declaradas.

Gate:

- no entregar como completado si el checklist falla.

Definition of Done:

- la entrega final es trazable, declara fuentes y artefactos, preserva el contenido canonico y cumple el checklist.

## Manejo operativo de bloqueos

Cuando una fase falle:

- detener la ejecucion en la fase donde ocurre el fallo;
- registrar causa exacta, impacto y fase afectada;
- no saltar fases;
- no completar mediante inferencias;
- no sustituir MCP por otro mecanismo;
- solicitar aclaracion o correccion solo cuando sea necesaria para continuar.
