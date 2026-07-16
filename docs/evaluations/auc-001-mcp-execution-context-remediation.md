# AUC-001 MCP Execution Context Remediation

## Purpose

Documentar la correccion operativa aplicada tras diagnosticar un `ERR_SCOPE_DENIED` provocado por la forma del `execution_context` enviado a `query_read_only` del BigQuery MCP Server.

Esta evaluacion no modifica el servidor MCP, el workspace, la allowlist, IAM ni la configuracion local.

## Failed Payload

```yaml
tool: query_read_only
request_id: auc001-20260715-provider-smoke-test
sql_query: "SELECT COUNT(*) AS row_count FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring` LIMIT 1"
execution_context:
  workspace_id: vca
  project_id: datamart-vca-494114
  dataset_id: intermediate
  table_id: int_faro_lead_scoring
  purpose: AUC-001 Data Provider Validation smoke test for allowlisted table only
error_code: ERR_SCOPE_DENIED
trace_id: trc-1001129e601b409a88459c0468d6cf7e
```

## Valid Payload

```yaml
tool: query_read_only
request_id: auc001-scope-diagnostic-query-scoring
sql_query: |
  SELECT COUNT(1) AS row_count
  FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring`
  WHERE lead_date <= DATE '2026-06-30'
execution_context:
  project_id: datamart-vca-494114
  dataset_id: intermediate
  max_bytes_billed: 1073741824
```

## Root Cause

El recurso no estaba fuera de allowlist y el workspace efectivo era correcto.

La causa raiz fue enviar un `execution_context` con campos descriptivos o no soportados:

- `workspace_id`
- `table_id`
- `purpose`

La misma tabla respondio correctamente cuando `execution_context` se construyo como contrato cerrado con `project_id`, `dataset_id` y `max_bytes_billed`.

## Applied Change

Se actualizo el procedimiento operativo de AUC-001 para declarar que `query_read_only.execution_context` es un contrato cerrado.

Campos permitidos:

```yaml
execution_context:
  project_id: <authorized_project_id>
  dataset_id: <authorized_dataset_id>
  max_bytes_billed: <workspace_cost_limit_bytes>
```

Para el workspace `vca`:

```yaml
project_id: datamart-vca-494114
max_bytes_billed: 1073741824
```

Regla de alineacion:

- usar `dataset_id: intermediate` para consultas sobre `datamart-vca-494114.intermediate.*`;
- usar `dataset_id: marts` para consultas sobre `datamart-vca-494114.marts.*`.

Campos prohibidos dentro de `execution_context`:

- `workspace_id`
- `table_id`
- `purpose`
- `request_id`
- `resource_selector`
- `location`
- `auth_mode`
- cualquier otro campo no enumerado en el contrato cerrado

La trazabilidad debe conservarse fuera de `execution_context`:

- `request_id` en el nivel superior de la llamada;
- SQL en `sql_query`;
- trazabilidad adicional en artefactos de ejecucion o auditoria.

## Example Validation

Los ejemplos operativos quedan validados contra esta forma:

```yaml
request_id: <stable_request_id>
sql_query: <read_only_sql>
execution_context:
  project_id: datamart-vca-494114
  dataset_id: intermediate|marts
  max_bytes_billed: 1073741824
```

No deben incluirse `workspace_id`, `table_id`, `purpose`, `request_id`, `resource_selector`, `location`, `auth_mode` ni otros campos descriptivos dentro de `execution_context`.

## Correct Smoke Test Result

```yaml
tool: query_read_only
request_id: auc001-scope-diagnostic-query-scoring
resource: datamart-vca-494114.intermediate.int_faro_lead_scoring
execution_context_dataset: intermediate
status: success
error_code: null
trace_id: trc-585f437387c84be8b213795ca2441044
row_count: 1321
bytes_processed: 12000
policy_decision: allow
```

Additional individual smoke tests also succeeded:

```yaml
lead_enriched:
  request_id: auc001-scope-diagnostic-query-lead
  dataset_id: marts
  status: success
  row_count: 1321
  trace_id: trc-30427776fa484da496f42b252569d1e2
spend:
  request_id: auc001-scope-diagnostic-query-spend
  dataset_id: marts
  status: success
  row_count: 7332
  trace_id: trc-2f87c14099784c4d940905c1572b54fc
campaign_signal:
  request_id: auc001-scope-diagnostic-query-signal
  dataset_id: marts
  status: success
  row_count: 4
  trace_id: trc-7ca2f81e91544270b06fba7d4d3cfe1c
```

## Retry Criterion For AUC-001

AUC-001 may be retried when every `query_read_only` call satisfies all of the following:

1. `execution_context` contains exactly `project_id`, `dataset_id` and `max_bytes_billed`.
2. `dataset_id` matches the dataset of every queried table.
3. `request_id` remains at the top level.
4. SQL remains in `sql_query`.
5. No descriptive, traceability or resource selector fields are placed inside `execution_context`.

## Outcome

```yaml
server_changed: false
workspace_changed: false
allowlist_changed: false
configuration_change_required: false
ready_to_retry_auc001: true
```