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
12. Presentation Materialization.
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
- BigQuery MCP Server.

Acciones:

- resolver workspace;
- verificar mecanismo de acceso;
- confirmar MCP disponible;
- verificar proyecto, datasets, tablas, allowlist y Data Contract;
- descubrir esquemas necesarios mediante MCP cuando aplique;
- verificar cobertura temporal;
- resolver campos dependientes del proveedor, incluido el inicio real si estaba en `PENDING_START_FROM_PROVIDER_COVERAGE`;
- confirmar que cada tabla pertenece al Data Contract y al workspace seleccionado.

Output:

- Data Provider validado;
- fuentes autorizadas;
- cobertura temporal y campos dependientes del proveedor resueltos o bloqueados.

Gate:

- detener si el workspace no resuelve, MCP no esta disponible, una fuente necesaria no esta autorizada o una tabla no pertenece al Data Contract.

### Convenciones SQL seguras para BigQuery MCP

Antes de enviar una consulta mediante `query_read_only`, revisar la SQL contra estas convenciones locales, derivadas del diagnostico AUC-001 v2:

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
- Antes de enviar la consulta MCP, comprobar aliases reservados, colisiones entre CTEs y columnas, referencias ambiguas, joins con coma y que el `dataset_id` del `execution_context` corresponde al alcance principal de la consulta.
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
- registrar SQL, request_id, execution_context, tablas, periodo, filtros, granularidad, dry run, coste estimado, bytes procesados, resultado, policy decision, trace ID y coverage;
- registrar consultas rechazadas y su causa publica;
- no usar consultas rechazadas como evidencia;
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
- construir findings mediante comparacion, segmentacion, evolucion temporal, descomposicion, contraste volumen-calidad, contraste calidad-coste, analisis de cobertura y anomalias;
- conservar limitaciones e incertidumbre;
- no formular recomendaciones.

Output:

- Knowledge Set estabilizado.

Gate:

- detener si el Knowledge Set solo repite metricas o introduce hechos no presentes en Evidence.

Definition of Done:

- existe un Knowledge Set consolidado, explicativo y derivado exclusivamente del Evidence Set.

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
- confirmar que Evidence no contiene interpretacion;
- confirmar que Knowledge no introduce evidencia nueva;
- confirmar que Recommendations derivan de Knowledge;
- no corregir inconsistencias dentro de Presentation.

Output:

- Canonical Content Validation result.

Gate:

- si falla la validacion, detener la ejecucion antes de Presentation.

Definition of Done:

- los cuatro artefactos canonicos estan listos para representarse sin reconstruccion.

## Fase 12 - Presentation Materialization

Input:

- artefactos canonicos estabilizados;
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
- consumir solo artefactos estabilizados;
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
- confirmar preservacion de limitaciones y UNKNOWNs.

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