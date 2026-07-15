# AUC-001 SQL Conventions Check

## Purpose

Local documentation check for the AUC-001 BigQuery MCP SQL conventions added after the AUC-001 v2 dry-run diagnostic.

This check does not modify BigQuery MCP Server, AIF Foundation, workspace configuration, allowlist, IAM, ADC, contracts, or Specifications.

## Checked Files

- `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`
- `.github/skills/meta-lead-quality-analysis/CHECKLIST.md`

## Rules Covered

```yaml
rules:
  no_rows_alias:
    recommended_examples:
      - "COUNT(*) AS row_count"
      - "COUNT(*) AS lead_count"
      - "COUNT(*) AS spend_row_count"
      - "COUNT(*) AS qualified_lead_count"
  no_cte_column_name_reuse:
    statement: "Un nombre de CTE no debe reutilizarse como alias de columna."
  no_comma_joins:
    recommended_examples:
      - "FROM table_a CROSS JOIN table_b"
      - "JOIN ... ON"
      - "JOIN ... USING"
  pre_mcp_review:
    checks:
      - aliases reservados
      - colisiones entre CTEs y columnas
      - referencias ambiguas
      - joins con coma
      - dataset_id del execution_context
  dry_run_failure_handling:
    checks:
      - no repetir la misma forma con cambios irrelevantes
      - simplificar la consulta
      - revisar sintaxis y tipos
      - usar aliases explicitos
      - registrar la consulta rechazada como evidencia no utilizable
```

## Documentation Validation

Recommended examples added by this change:

- do not use `AS rows`;
- do not contain comma joins;
- do not reuse a CTE name as a column alias.

The Runbook includes one explicit incorrect example for each demonstrated anti-pattern where useful:

- `COUNT(*) AS rows`
- `FROM table_a, table_b`

Those examples are labeled as incorrect and must not be copied into executable MCP queries.

## Result

```yaml
status: pass
framework_change: false
mcp_change: false
ready_for_natural_language_test: true
```