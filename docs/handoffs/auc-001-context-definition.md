# AUC-001 Context Definition

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-CTX-DEF-001 |
| Artifact Type | Context Definition |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Related Contract | VCA-CTX-001 |
| Status | Validated |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Backing Task | T-016 |

---

## Purpose

Formalizar el Context Definition validado para la ejecucion AUC-001 de junio de 2026 antes de iniciar el Data Contract, Discovery o adquisicion de evidencia.

Este artefacto materializa la salida de la fase Contexto de SPEC-001 para una ejecucion concreta.

Este artefacto no produce evidencia.

Este artefacto no interpreta datos.

Este artefacto no formula conclusiones ni recomendaciones.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-016 |
| Task | Implementar la validacion del Analysis Request y del Context Definition de AUC-001 |
| Specification | SPEC-001 Analytical Lifecycle, Phase 0 Contexto |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | La solicitud analitica concreta y el Context Definition quedan trazados y validados antes de iniciar la adquisicion de datos |

---

## Upstream Artifacts

| Artifact | Relationship |
|---|---|
| [AUC-001 Analysis Request](auc-001-analysis-request.md) | Solicitud analitica concreta validada |
| [AUC-001 Execution Context](auc-001-execution-context.md) | Parametros operativos normalizados y congelados |
| [AUC-001 Context Resolution](auc-001-context-resolution.md) | Resolucion de fuentes oficiales y contexto aplicable |
| [VCA-CTX-001 Context Contract](../contracts/context.contract.md) | Contract reusable que define campos criticos y reglas de validacion |

---

## Context Definition

| Field | Value | Status |
|---|---|---|
| context_definition_id | VCA-AUC-001-CTX-DEF-2026-06 |
| analysis_objective | Analizar la calidad de leads de Meta Ads para la corrida mensual de junio de 2026 dentro del caso AUC-001. | Validated |
| supported_decision | Apoyar la lectura ejecutiva sobre volumen de captacion, calidad de leads, eficiencia economica, rendimiento de campanas y creatividades, oportunidades de optimizacion y recomendaciones priorizadas. | Validated |
| analysis_period | 2026-06-01 to 2026-06-30 | Validated |
| operational_scope | Todas las campanas, conjuntos y creatividades de Meta Lead Ads con inversion o leads durante el periodo. | Validated |
| filters | campaign_signal = COMMERCIAL; excluir registros de prueba; excluir duplicados; excluir leads sin identificador valido; sin filtro geografico adicional. | Validated |
| lead_quality_definition | Qualified Lead segun FARO, equivalente a Lead Tier A o B. | Validated |
| primary_data_provider | BigQuery MCP Server as intended provider. | Validated for next contract |
| audience | Analista de negocio, direccion, responsable de Marketing, especialistas de Meta Ads y equipo Comercial. | Validated |
| output_request | Informe ejecutivo trazable. | Validated |
| official_context_sources | project_brief.md; docs/context_refs.md; knowledge/client/ccd.md; analytical_use_cases/meta_lead_quality_analysis.md; .github/skills/meta-lead-quality-analysis/SKILL.md; docs/contracts/context.contract.md; specs/spec-001-analytical-lifecycle.md. | Validated |

---

## Constraints

- No ampliar AUC-001 con parametros especificos de ejecucion.
- No inventar datos, segmentos, campanas, periodos ni conclusiones no sustentadas.
- Mantener separadas las categorias contexto, evidencia, analisis, razonamiento, recomendaciones y presentacion.
- BigQuery MCP Server debe formalizar su frontera en el Data Contract del caso antes de adquisicion de evidencia.
- La definicion de Lead de Calidad se limita a la solicitud de ejecucion: Qualified Lead segun FARO, equivalente a Lead Tier A o B.
- La ausencia de filtro geografico adicional queda congelada como parametro de esta ejecucion, no como regla general de AUC-001.

---

## Validation

| Criterion | Result | Evidence |
|---|---|---|
| Analysis Request exists and is validated | Pass | auc-001-analysis-request.md |
| Execution Context exists and is validated | Pass | auc-001-execution-context.md |
| Objective is explicit | Pass | Context Definition table |
| Supported decision is explicit | Pass | Context Definition table |
| Period is explicit | Pass | 2026-06-01 to 2026-06-30 |
| Operational scope is explicit | Pass | All Meta Lead Ads campaigns, ad sets and creatives with investment or leads during period |
| Filters are explicit | Pass | campaign_signal and exclusion filters declared |
| Lead-quality criterion is explicit | Pass | Qualified Lead according to FARO, Lead Tier A or B |
| Official sources are explicit | Pass | Official context sources listed |
| No evidence or interpretation introduced | Pass | Artifact is context-only |
| AUC-001 remains reusable | Pass | Execution parameters are contained in handoff artifacts |

---

## Unknowns And Pending Items

| Item | Status | Handling |
|---|---|---|
| BigQuery MCP Server technical availability and concrete data structure | Pending for Data Contract | Must be handled in T-017 / T-018 |
| Dataset, table, field and granularity mapping | Pending for Data Contract | Must not be inferred in Context Definition |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-017 - Data Contract del caso AUC-001 | Ready | The Context Definition is validated and provides the operational scope required by the Data Contract. |
| Discovery / Data acquisition | Not yet authorized | T-017 Data Contract and T-018 evidence acquisition remain pending. |

---

## Traceability

- User request provided in conversation on 2026-07-12.
- [AUC-001 Analysis Request](auc-001-analysis-request.md)
- [AUC-001 Execution Context](auc-001-execution-context.md)
- [AUC-001 Context Resolution](auc-001-context-resolution.md)
- [VCA-CTX-001 Context Contract](../contracts/context.contract.md)
- [SPEC-001 Analytical Lifecycle](../../specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](../../specs/spec-002-component-boundaries.md)
- [SPEC-004 Transversal Contracts](../../specs/spec-004-transversal-contracts.md)
- [Project Brief](../../project_brief.md)
- [Context References](../context_refs.md)
- [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md)
- [Client CCD](../../knowledge/client/ccd.md)
- [docs/tasks.md](../tasks.md)

---

## Completion Statement

T-016 is complete for AUC-001 June 2026.

The Analysis Request and Context Definition are traced and validated before data acquisition.

The next permitted increment is T-017, the case-specific Data Contract for AUC-001.