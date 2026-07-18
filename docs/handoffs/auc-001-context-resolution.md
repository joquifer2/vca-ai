# AUC-001 Context Resolution

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-CTX-RES-001 |
| Artifact Type | Context Resolution |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Related Contract | VCA-CTX-001 |
| Status | Validated |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Task | T-015 / T-016 |

---

## Purpose

Resolver el contexto oficial disponible para AUC-001 a partir de una instancia validada de Execution Context antes de iniciar validacion del Context Definition, adquisicion de datos, Discovery, preparacion, analisis o razonamiento.

Este artefacto no produce evidencia.

Este artefacto no interpreta datos.

Este artefacto no formula conclusiones ni recomendaciones.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-015 / T-016 |
| Task | Resolucion del contexto oficial y validacion del Analysis Request y Context Definition de AUC-001 |
| Specification | SPEC-001 Analytical Lifecycle, Phase 0 Contexto |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | El flujo identifica y valida fuentes oficiales, objetivo, periodo y alcance operativo antes de adquisicion de datos |

## Upstream Artifacts

| Field | Value |
|---|---|
| Analysis Request | [AUC-001 Analysis Request](auc-001-analysis-request.md) |
| Execution Context | [AUC-001 Execution Context](auc-001-execution-context.md) |
| Relationship | Inputs operativos que normalizan la solicitud antes de la resolucion oficial |

---

## Official Context Sources

| Source | Role | Status | Notes |
|---|---|---|---|
| [project_brief.md](/project_brief.md) | Project Source of Truth | Available | Define VCA IA purpose, scope, constraints, success criteria and AUC-001 as initial approved analytical use case. |
| [docs/context_refs.md](/docs/context_refs.md) | Context index | Available | Declares official context sources, Knowledge Base, runtime sources and pending technical references. |
| [knowledge/client/ccd.md](/knowledge/client/ccd.md) | Client context | Available | Provides client, ecosystem, FARO, CLARO, Meta Ads, BigQuery and business interpretation context. |
| [analytical_use_cases/meta_lead_quality_analysis.md](/analytical_use_cases/meta_lead_quality_analysis.md) | Analytical use case | Available | Defines AUC-001 objective, scope, evidence inventory, flow, validation criteria and expected outcome. |
| [.github/skills/meta-lead-quality-analysis/SKILL.md](/.github/skills/meta-lead-quality-analysis/SKILL.md) | Skill rules | Available | Defines operational flow, required context, evidence rules and blocking criteria for the analysis. |
| [docs/contracts/context.contract.md](/docs/contracts/context.contract.md) | Context Contract | Available | Defines required fields, validation rules and UNKNOWN handling for context resolution. |
| [specs/spec-001-analytical-lifecycle.md](/specs/spec-001-analytical-lifecycle.md) | Lifecycle specification | Available | Requires objective, restrictions and official context sources before Discovery. |
| [specs/spec-002-component-boundaries.md](/specs/spec-002-component-boundaries.md) | Boundary specification | Available | Requires handoffs to be materialized in identifiable, reviewable artifacts. |
| [specs/spec-004-transversal-contracts.md](/specs/spec-004-transversal-contracts.md) | Contract specification | Available | Requires explicit traceability and UNKNOWN handling in contracts and contractual artifacts. |

---

## Context Definition Inputs

| Field | Resolved Value | Status | Source |
|---|---|---|---|
| analysis_objective | Analizar la calidad de leads de Meta Ads para la corrida mensual de junio de 2026 dentro del caso AUC-001. | Resolved | Analysis Request; AUC-001; skill; project brief |
| supported_decision | Apoyar la lectura ejecutiva sobre volumen de captacion, calidad de leads, eficiencia economica, rendimiento de campanas y creatividades, oportunidades de optimizacion y recomendaciones priorizadas. | Resolved | AUC-001; Analysis Request |
| official_context_scope | VCA IA como sistema analitico corporativo de VCA que consume la plataforma de datos existente sin sustituirla. | Resolved | project brief; README; docs/context_refs.md |
| client_context_scope | Ecosistema VCA Project: captacion, FARO, CLARO, Meta Ads, BigQuery, scoring, activacion, integraciones y reporting. | Resolved | knowledge/client/ccd.md |
| primary_data_provider | BigQuery MCP Server. | Resolved as intended provider | AUC-001; docs/context_refs.md; skill |
| analysis_period | 2026-06-01 to 2026-06-30 | Resolved | Analysis Request; Execution Context |
| campaign_scope | Todas las campanas, conjuntos y creatividades de Meta Lead Ads con inversion o leads durante el periodo. | Resolved | Analysis Request; Execution Context |
| filters | campaign_signal = COMMERCIAL; excluir registros de prueba, duplicados y leads sin identificador valido; sin filtro geografico adicional. | Resolved | Analysis Request; Execution Context |
| lead_quality_criterion | Qualified Lead segun FARO, equivalente a Lead Tier A o B. | Resolved | Analysis Request; Execution Context; knowledge/client/ccd.md |
| report_audience | Analista de negocio, direccion, responsable de Marketing, especialistas de Meta Ads y equipo Comercial. | Resolved | AUC-001 |
| output_type | Informe ejecutivo trazable. | Resolved | AUC-001; skill; Analysis Request |

---

## Operational Scope

| Dimension | Current Resolution | Status |
|---|---|---|
| Channel | Meta Ads | Resolved |
| Business object | Leads captados mediante Meta Lead Ads | Resolved |
| Analytical focus | Volumen, calidad, eficiencia economica, campanas, creatividades, segmentacion y oportunidades de optimizacion | Resolved |
| Context framework | FARO, CLARO, KPIs oficiales y Knowledge Base del proyecto cuando esten disponibles | Resolved at context level |
| Data platform | BigQuery via BigQuery MCP Server as intended provider | Resolved as intended provider |
| Period | 2026-06-01 to 2026-06-30 | Resolved |
| Campaign / ad set / creative scope | Todas las campanas, conjuntos y creatividades de Meta Lead Ads con inversion o leads durante el periodo | Resolved |
| Filters | campaign_signal = COMMERCIAL; excluir registros de prueba, duplicados y leads sin identificador valido; sin filtro geografico adicional | Resolved |
| Lead-quality definition | Qualified Lead segun FARO, equivalente a Lead Tier A o B | Resolved |

---

## Constraints

- No se debe asumir contexto de negocio no publicado.
- No se deben inventar datos, segmentos, campanas, periodos ni conclusiones no sustentadas.
- BigQuery MCP Server es el Data Provider principal previsto, pero su documentacion aparece como PENDING en `docs/context_refs.md`; su disponibilidad tecnica debe validarse en T-017/T-018.
- AIF Foundation debe tratarse como dependencia metodologica, no como objeto funcional del sistema.
- La fase Contexto no puede producir evidencia, interpretacion, conclusiones ni recomendaciones.
- Los parametros operativos pertenecen a esta ejecucion concreta y no modifican AUC-001.

---

## Assumptions

| Assumption | Status | Basis |
|---|---|---|
| AUC-001 es el primer caso analitico aprobado para validar VCA IA. | Verified | project brief; AUC-001; docs/context_refs.md |
| BigQuery MCP Server sera la fuente principal de evidencia cuando los datos esten disponibles. | Verified as intended provider | AUC-001; skill |
| FARO y CLARO son contexto oficial del ecosistema de captacion y datos. | Verified | knowledge/client/ccd.md |
| No existe filtro geografico adicional para esta corrida. | Verified for execution | Analysis Request; Execution Context |
| El criterio operativo de calidad para esta corrida es Qualified Lead segun FARO, equivalente a Lead Tier A o B. | Verified for execution | Analysis Request; Execution Context |

---

## Unknowns

| Unknown | Impact | Required Resolution Artifact |
|---|---|---|
| Disponibilidad tecnica/documentacion del BigQuery MCP Server | No bloquea el Context Definition; debe evaluarse antes de adquisicion de evidencia. | Data Contract del caso; T-017 / T-018 |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-016 - Validacion del Analysis Request y Context Definition de AUC-001 | Ready / Validated | La solicitud analitica concreta, el periodo, el alcance operativo, los filtros y el criterio de calidad estan trazados. |
| T-017 - Data Contract del caso AUC-001 | Ready | El contexto operativo esta suficientemente definido para formalizar el Data Contract del caso. |
| Discovery / Data acquisition | Not yet authorized | Debe completarse primero T-017 Data Contract y T-018 adquisicion de evidencia. |

---

## Traceability

- [T-015 and T-016 in docs/tasks.md](/docs/tasks.md)
- [AUC-001 Analysis Request](auc-001-analysis-request.md)
- [AUC-001 Execution Context](auc-001-execution-context.md)
- [AUC-001 Context Definition](auc-001-context-definition.md)
- [VCA-CTX-001 Context Contract](/docs/contracts/context.contract.md)
- [SPEC-001 Analytical Lifecycle](/specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](/specs/spec-002-component-boundaries.md)
- [SPEC-004 Transversal Contracts](/specs/spec-004-transversal-contracts.md)
- [Project Brief](/project_brief.md)
- [Context References](/docs/context_refs.md)
- [AUC-001 Meta Lead Quality Analysis](/analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](/.github/skills/meta-lead-quality-analysis/SKILL.md)
- [Client CCD](/knowledge/client/ccd.md)

---

## Completion Statement

The Context Resolution for AUC-001 June 2026 is validated.

The resolution identifies official sources, objective, supported decision, period, operational scope, filters and lead-quality criterion for this execution.

This artifact does not authorize data acquisition by itself. It enables T-017, where the case-specific Data Contract must validate the Data Provider boundary before evidence acquisition.