# AUC-001 Data Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-AUC-001-DATA-001 |
| Contract Name | AUC-001 BigQuery MCP Server Data Contract |
| Contract Category | Data Contract |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Related Base Contract | VCA-DATA-001 |
| Status | Documentado; exposición del proveedor verificada en T-018; acceso MCP pendiente |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Backing Task | T-017 |

---

## Purpose

Formalizar el Data Contract especifico de AUC-001 para la ejecucion de junio de 2026 antes de adquirir evidencia desde el Data Provider principal.

Este contract define productor, consumidor, alcance solicitado, estructura logica esperada, limitaciones y trazabilidad.

Este contract no ejecuta consultas.

Este contract no produce evidencia.

Este contract no interpreta datos.

Este contract no formula hallazgos, conclusiones ni recomendaciones.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-017 |
| Task | Implementar el Data Contract del caso AUC-001 |
| Specifications | SPEC-001 Analytical Lifecycle; SPEC-002 Component Boundaries; SPEC-004 Transversal Contracts |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | Existe un Data Contract reusable para el Data Provider principal, con productor, consumidor, estructura y limitaciones trazables |

---

## Producer And Consumer

| Role | Value | Status |
|---|---|---|
| Producer | BigQuery MCP Server | Declared principal Data Provider |
| Underlying data platform | BigQuery / CLARO | Declared by official context |
| Business logic source | FARO | Declared by official context |
| Consumer | Framework, Discovery flow and Analytical Layer | Declared |
| Downstream artifact | Future Discovery Contract for AUC-001 | Pending T-019 |

---

## Upstream Inputs

| Input | Source | Status |
|---|---|---|
| Context Definition | [AUC-001 Context Definition](auc-001-context-definition.md) | Validated |
| Execution Context | [AUC-001 Execution Context](auc-001-execution-context.md) | Validated |
| Base Data Contract | [VCA-DATA-001](../contracts/data.contract.md) | Documented |
| AUC-001 | [Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md) | Approved analytical use case |
| Skill | [meta-lead-quality-analysis](../../.github/skills/meta-lead-quality-analysis/SKILL.md) | Approved skill |
| Client context | [CCD](../../knowledge/client/ccd.md) | Available |
| Data Provider reference | [docs/context_refs.md](../context_refs.md) | BigQuery provider exposure verified in T-018; direct MCP access pending |

---

## Requested Data Scope

| Field | Value | Source |
|---|---|---|
| execution_id | VCA-AUC-001-EXEC-2026-06 | Execution Context |
| context_definition_id | VCA-AUC-001-CTX-DEF-2026-06 | Context Definition |
| analysis_period | 2026-06-01 to 2026-06-30 | Context Definition |
| channel | Meta Ads / Meta Lead Ads | AUC-001; CCD; Execution Context |
| campaign_scope | Todas las campanas de Meta Lead Ads con inversion o leads durante el periodo | Execution Context |
| ad_set_scope | Todos los conjuntos de anuncios de Meta Lead Ads con inversion o leads durante el periodo | Execution Context |
| creative_scope | Todas las creatividades de Meta Lead Ads con inversion o leads durante el periodo | Execution Context |
| required_filter_campaign_signal | campaign_signal = COMMERCIAL | Execution Context; CCD |
| exclusion_filters | Excluir registros de prueba; excluir duplicados; excluir leads sin identificador valido | Execution Context |
| geographic_filter | Sin filtro geografico adicional | Execution Context |
| lead_quality_definition | Qualified Lead segun FARO, equivalente a Lead Tier A o B | Execution Context; CCD |

---

## Source Declaration

| Field | Value | Status |
|---|---|---|
| data_provider | BigQuery MCP Server | Declared |
| data_platform | Google BigQuery via CLARO | Declared by CCD |
| source_reference | BigQuery MCP Server | Available as provider reference |
| dataset_reference | `datamart-vca-494114.marts` | Verified in T-018 |
| table_or_view_reference | `fct_lead_enriched`; `fct_performance_daily`; `fct_spend`; `dim_campaign_signal` | Verified in T-018 |
| access_method | BigQuery CLI aggregate queries against BigQuery | Verified for source exposure |
| access_status | Verified for source exposure | Verified through BigQuery CLI aggregate queries in T-018; direct MCP access remains pending |
| provider_documentation_status | Partially verified | docs/context_refs.md still marks BigQuery MCP Server documentation as PENDING |

---

## Logical Structure

| Category | Required Logical Elements | Status | Notes |
|---|---|---|---|
| Entities | Lead, campaign, ad set, creative, time period | Expected / provider mapping pending | Required by AUC-001 and Execution Context |
| Dimensions | date or period, campaign, ad set, creative, campaign_signal, lead tier or quality class | Expected / provider mapping pending | Exact field names must not be inferred |
| Metrics | leads, impressions, clicks, conversions, spend, CPL/CPA or equivalent cost metric, qualified leads | Expected / provider mapping pending | AUC-001 requires volume, quality and economic efficiency |
| Quality signals | Qualified Lead, Lead Tier A, Lead Tier B | Expected / provider mapping pending | FARO defines Qualified Lead; execution maps quality to Lead Tier A or B |
| Filters | campaign_signal = COMMERCIAL; valid lead identifier; non-test; non-duplicate | Expected / provider mapping pending | Exact filtering fields must be verified in T-018 |
| Granularity | Campaign, ad set, creative and period-level granularity | Expected / provider mapping pending | Minimum required for AUC-001 scope |
| Relationships | Lead-to-campaign/ad set/creative relationships | UNKNOWN / provider mapping pending | Must be verified from provider metadata or query results |

---

## Minimum Evidence Families To Expose

| Evidence Family | Required Data | Source Basis | Status |
|---|---|---|---|
| Volumen de captacion | Leads, impressions, clicks, conversions by period | AUC-001 | Required / mapping pending |
| Calidad del lead | Qualified Lead, Lead Tier A/B or equivalent quality signal | AUC-001; Execution Context; CCD | Required / mapping pending |
| Eficiencia economica | Spend, CPL, CPA or equivalent cost metrics | AUC-001 | Required / mapping pending |
| Campanas y creatividades | Campaign, ad set and creative performance | AUC-001; Execution Context | Required / mapping pending |
| Segmentacion | Differences by period, audience or applicable segment when available | AUC-001 | Optional if provider exposes it; must not be inferred |
| Contexto de negocio | FARO, CLARO, KPIs oficiales and Knowledge Base references | CCD; docs/context_refs.md | Context only; not Data Provider output |

---

## Exposed Scope

| Field | Value | Status |
|---|---|---|
| exposed_period | 2026-06-01 to 2026-06-30 | Verified in T-018 |
| exposed_campaign_scope | Commercial performance/spend exposed; lead table exposes campaign/adset/ad references without campaign_signal | Verified with limitations in T-018 |
| exposed_entities | Lead; campaign; ad set; ad; concept; version; angle; period | Verified in T-018 |
| exposed_dimensions | day/spend_period; campaign_id/name; adset_id/name; ad_id/name; campaign_signal; lead_tier; concept_id; version_id; angle_id | Verified with limitations in T-018 |
| exposed_metrics | leads; distinct_leads; lead_tier A/B counts; spend; cpl; billetes_yes; billetes_process; solo_mirando | Verified in T-018 |
| exposed_granularity | Lead-level in fct_lead_enriched; day/concept/version/angle in fct_performance_daily; spend_period/ad/concept/version/angle in fct_spend | Verified with limitations in T-018 |
| exposed_limitations | Granularity and relationship differences across lead, performance and spend tables | Recorded in T-018 |

---

## Validation Rules

| Rule | Result | Evidence |
|---|---|---|
| Context dependency | Pass | Context Definition is validated |
| Provider boundary | Pass | Contract does not emit insights, conclusions or recommendations |
| Scope alignment | Pass for requested scope | Requested scope matches Context Definition; exposed scope remains pending provider verification |
| Source declaration | Pass | Provider is declared; source exposure is verified and MCP access remains pending |
| Limitation visibility | Pass | Provider mapping and access limitations are explicit |
| No inferred schema | Pass | Logical structure is expected but exact fields remain documented only for the verified exposure |
| Transition blocking | Pass with limitations | Ready for T-018 provider verification; Discovery remains limited by explicitly pending MCP access and by any unresolved source mappings |

---

## Limitations

| Limitation | Impact | Handling |
|---|---|---|
| BigQuery MCP Server documentation is PENDING in docs/context_refs.md | Data access and query mechanism are not yet verified | Validate in T-018 before evidence acquisition |
| Dataset, table, view or model identifiers for the verified exposure are published in this contract | Exact source reference is documented for the current verified exposure | Do not infer additional source names beyond the published contract scope |
| Exact field names are not fully enumerated beyond the verified exposure | Query shape can be inferred only from the documented exposure | Use the published source exposure and do not invent extra fields |
| Exposed period is confirmed for June 2026 | Evidence completeness for June 2026 is verified for the current scope | Preserve the documented June 2026 window |
| Exposed campaign/ad set/creative scope is confirmed for the current verified exposure | Scope alignment is verified for the current scope | Preserve the documented scope in this contract |
| Lead Tier A/B field or derivation is mapped through `lead_tier` | Quality calculation can be executed for the current scope | Preserve the verified quality mapping documented in T-018 |
| Direct MCP access is not yet verified | Provider boundary remains partially validated | Treat CLI verification as source exposure only until MCP is exercised |

---

## Unknowns And Pending Items

| Item | Status | Required Resolution |
|---|---|---|
| BigQuery provider availability | Verified for source exposure; MCP validation pending | T-018 |
| Dataset/table/view identifiers | Verified for the published marts tables | T-018 |
| Field mapping for dimensions and metrics | Verified for the exposed June 2026 scope | T-018; relationship validation remains for Discovery |
| Field mapping for Qualified Lead / Lead Tier A/B | Verified via `lead_tier` | T-018 |
| Data freshness or latency | Observed for the documented June 2026 window | Source max dates recorded in T-018 |
| Duplicates/test-record flags and valid identifier fields | Partially verified | Valid lead_id checked; duplicate/test flags remain a Discovery limitation |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-018 - Adquisicion de evidencia desde BigQuery MCP Server | Completed with limitations | Provider availability, selected source identifiers and aggregate evidence exposure were verified in T-018. |
| Discovery | Ready with limitations | Discovery can formalize entities, dimensions, metrics, relationships and limitations observed in T-018; MCP access remains pending. |
| Analytical preparation | Not authorized | Analytical preparation requires Discovery and confirmed data exposure. |

---

## Traceability

- [T-017 in docs/tasks.md](../tasks.md)
- [AUC-001 Context Definition](auc-001-context-definition.md)
- [AUC-001 Execution Context](auc-001-execution-context.md)
- [AUC-001 Context Resolution](auc-001-context-resolution.md)
- [VCA-DATA-001 Base Data Contract](../contracts/data.contract.md)
- [VCA-CTX-001 Context Contract](../contracts/context.contract.md)
- [SPEC-001 Analytical Lifecycle](../../specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](../../specs/spec-002-component-boundaries.md)
- [SPEC-004 Transversal Contracts](../../specs/spec-004-transversal-contracts.md)
- [Project Brief](../../project_brief.md)
- [Context References](../context_refs.md)
- [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md)
- [Client CCD](../../knowledge/client/ccd.md)

---

## Completion Statement

T-017 is complete as a case-specific Data Contract for AUC-001 June 2026.

The contract identifies the producer, consumer, requested scope, logical structure, required evidence families, limitations and the explicitly pending MCP access.

T-018 verified provider availability and concrete source exposure with limitations. The next permitted increment is T-019, the Discovery Contract for AUC-001.