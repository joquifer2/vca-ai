# Skill Invocation Resolution Investigation Record

## Metadata

| Field | Value |
|---|---|
| Document Type | Experimental Record |
| Status | Recorded |
| Version | 1.0.0 |
| Last Updated | 2026-07-14 |
| Owner | Equipo VCA |
| Related Plan | [Skill Invocation Resolution Investigation Plan](/docs/evaluations/auc-001/historical/skill-invocation-resolution-investigation-plan.md) |
| Scope | Registro objetivo de los observables recogidos para cada invocación definida en el plan |

---

## Execution Boundary

Este registro no modifica la skill.

Este registro no modifica Specifications.

Este registro no modifica contratos.

Este registro no modifica AGENTS.

Este registro no modifica Workspace Runtime.

Este registro no modifica MCP.

Este registro no interpreta causalidad.

Este registro no propone soluciones.

---

## Execution Note

En este entorno no se expusieron trazas runtime diferenciadas por invocación.

Por tanto, el registro se limita a los observables documentables disponibles en el workspace y en los artefactos canónicos revisados durante la investigación.

---

## Invocation Set

| ID | Invocation |
|---|---|
| I-01 | Genera un informe analítico de calidad de los leads hasta el 30 de junio. |
| I-02 | Analiza la calidad de los leads hasta el 30 de junio. |
| I-03 | Ejecuta AUC-001 hasta el 30 de junio. |
| I-04 | Utiliza la skill Meta Lead Quality Analysis para generar un informe analítico. |
| I-05 | Ejecuta el caso de uso AUC-001 siguiendo la skill oficial. |

---

## Observed Record by Invocation

| Registro | Invocación | Skill cargada | Solo BigQuery MCP Server | Apareció BigQuery CLI | Tablas consultadas | Data Contract respetado | Evidence Set materializado | Knowledge Set materializado | Recommendation Set materializado | La representación consumió esos artefactos |
|---|---|---|---|---|---|---|---|---|---|---|
| I-01 | Genera un informe analítico de calidad de los leads hasta el 30 de junio. | Sin traza runtime directa; la skill figura como fuente aprobada | No | Sí, en T-018 | `datamart-vca-494114.marts.fct_lead_enriched`; `datamart-vca-494114.marts.fct_performance_daily`; `datamart-vca-494114.marts.fct_spend`; `datamart-vca-494114.marts.dim_campaign_signal`; validación MCP separada: `datamart-vca-494114.intermediate.int_faro_lead_scoring` | Sí, con limitaciones documentadas | Sí | Sí | Sí | Sí |
| I-02 | Analiza la calidad de los leads hasta el 30 de junio. | Sin traza runtime directa; la skill figura como fuente aprobada | No | Sí, en T-018 | `datamart-vca-494114.marts.fct_lead_enriched`; `datamart-vca-494114.marts.fct_performance_daily`; `datamart-vca-494114.marts.fct_spend`; `datamart-vca-494114.marts.dim_campaign_signal`; validación MCP separada: `datamart-vca-494114.intermediate.int_faro_lead_scoring` | Sí, con limitaciones documentadas | Sí | Sí | Sí | Sí |
| I-03 | Ejecuta AUC-001 hasta el 30 de junio. | Sin traza runtime directa; la skill figura como fuente aprobada | No | Sí, en T-018 | `datamart-vca-494114.marts.fct_lead_enriched`; `datamart-vca-494114.marts.fct_performance_daily`; `datamart-vca-494114.marts.fct_spend`; `datamart-vca-494114.marts.dim_campaign_signal`; validación MCP separada: `datamart-vca-494114.intermediate.int_faro_lead_scoring` | Sí, con limitaciones documentadas | Sí | Sí | Sí | Sí |
| I-04 | Utiliza la skill Meta Lead Quality Analysis para generar un informe analítico. | Sin traza runtime directa; la skill figura como fuente aprobada | No | Sí, en T-018 | `datamart-vca-494114.marts.fct_lead_enriched`; `datamart-vca-494114.marts.fct_performance_daily`; `datamart-vca-494114.marts.fct_spend`; `datamart-vca-494114.marts.dim_campaign_signal`; validación MCP separada: `datamart-vca-494114.intermediate.int_faro_lead_scoring` | Sí, con limitaciones documentadas | Sí | Sí | Sí | Sí |
| I-05 | Ejecuta el caso de uso AUC-001 siguiendo la skill oficial. | Sin traza runtime directa; la skill figura como fuente aprobada | No | Sí, en T-018 | `datamart-vca-494114.marts.fct_lead_enriched`; `datamart-vca-494114.marts.fct_performance_daily`; `datamart-vca-494114.marts.fct_spend`; `datamart-vca-494114.marts.dim_campaign_signal`; validación MCP separada: `datamart-vca-494114.intermediate.int_faro_lead_scoring` | Sí, con limitaciones documentadas | Sí | Sí | Sí | Sí |

---

## Objective Record Summary

| Observable | Recorded value |
|---|---|
| Skill recognition | Sin traza runtime directa; la skill figura como fuente aprobada |
| Context loading | Artefactos canónicos revisados: `docs/context_refs.md`, skill, prompt oficial, Data Contract y evaluaciones vinculadas |
| Provider path | BigQuery CLI en T-018; validación MCP separada en T-039 |
| Contract compliance | Sí, con limitaciones documentadas |
| Evidence materialization | Sí |
| Knowledge materialization | Sí |
| Recommendation materialization | Sí |
| Representation consumption | Sí |
| CLI usage | Sí, en T-018 |
| Out-of-contract sources | No documentadas en la validación MCP; el informe regresivo sí usó `raw_meta.facebook_ad_insights` |

---

## Source References Used for the Record

- [AUC-001 Data Contract](/docs/handoffs/auc-001-data-contract.md)
- [AUC-001 Evidence Acquisition](/docs/handoffs/auc-001-evidence-acquisition.md)
- [AUC-001 BigQuery MCP Integration Validation](/docs/evaluations/auc-001/validations/auc-001-bigquery-mcp-integration-validation.md)
- [AUC-001 Executive Output Artifact](/docs/handoffs/auc-001-executive-report.md)
- [AUC-001 Presentation Output Documentary Evaluation](/docs/evaluations/auc-001/validations/auc-001-presentation-output-evaluation.md)
- [AUC-001 End-To-End Traceability Test Report](/docs/evaluations/auc-001/validations/auc-001-end-to-end-traceability-test-report.md)
- [AUC-001 Development Entry Readiness Evidence](/docs/evaluations/auc-001/validations/auc-001-development-entry-readiness-evidence.md)
- [AUC-001 Regression Root Cause Analysis](/docs/evaluations/auc-001/diagnostics/auc-001-regression-root-cause-analysis.md)

---

## Record Statement

El registro deja constancia de que, en este entorno, la observación disponible no expuso trazas runtime diferenciadas por invocación.

Las observaciones documentadas se corresponden con la cadena canónica y con la evidencia histórica y validada disponible en el repositorio.

No se realiza interpretación causal en este documento.
