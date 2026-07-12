# AUC-001 Context Resolution

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-CTX-RES-001 |
| Artifact Type | Context Resolution |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Related Contract | VCA-CTX-001 |
| Status | Documented with blocking UNKNOWNs |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Task | T-015 |

---

## Purpose

Resolver el contexto oficial disponible para AUC-001 a partir de una instancia de Execution Context antes de iniciar validacion del Context Definition, adquisicion de datos, Discovery, preparacion, analisis o razonamiento.

Este artefacto no produce evidencia.

Este artefacto no interpreta datos.

Este artefacto no formula conclusiones ni recomendaciones.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-015 |
| Task | Implementar la resolucion del contexto oficial para AUC-001 |
| Specification | SPEC-001 Analytical Lifecycle, Phase 0 Contexto |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | El flujo identifica las fuentes oficiales, el objetivo, el periodo y el alcance operativo del caso |

## Upstream Artifact

| Field | Value |
|---|---|
| Execution Context | [AUC-001 Execution Context](auc-001-execution-context.md) |
| Relationship | Input operativo que normaliza la solicitud antes de la resolucion oficial |

---

## Official Context Sources

| Source | Role | Status | Notes |
|---|---|---|---|
| [project_brief.md](../../project_brief.md) | Project Source of Truth | Available | Define VCA IA purpose, scope, constraints, success criteria and AUC-001 as initial approved analytical use case. |
| [docs/context_refs.md](../context_refs.md) | Context index | Available | Declares official context sources, Knowledge Base, runtime sources and pending technical references. |
| [knowledge/client/ccd.md](../../knowledge/client/ccd.md) | Client context | Available | Provides client, ecosystem, FARO, CLARO, Meta Ads, BigQuery and business interpretation context. |
| [analytical_use_cases/meta_lead_quality_analysis.md](../../analytical_use_cases/meta_lead_quality_analysis.md) | Analytical use case | Available | Defines AUC-001 objective, scope, evidence inventory, flow, validation criteria and expected outcome. |
| [.github/skills/meta-lead-quality-analysis/SKILL.md](../../.github/skills/meta-lead-quality-analysis/SKILL.md) | Skill rules | Available | Defines operational flow, required context, evidence rules and blocking criteria for the analysis. |
| [docs/contracts/context.contract.md](../contracts/context.contract.md) | Context Contract | Available | Defines required fields, validation rules and UNKNOWN handling for context resolution. |
| [specs/spec-001-analytical-lifecycle.md](../../specs/spec-001-analytical-lifecycle.md) | Lifecycle specification | Available | Requires objective, restrictions and official context sources before Discovery. |
| [specs/spec-002-component-boundaries.md](../../specs/spec-002-component-boundaries.md) | Boundary specification | Available | Requires handoffs to be materialized in identifiable, reviewable artifacts. |
| [specs/spec-004-transversal-contracts.md](../../specs/spec-004-transversal-contracts.md) | Contract specification | Available | Requires explicit traceability and UNKNOWN handling in contracts and contractual artifacts. |

---

## Context Definition Inputs

| Field | Resolved Value | Status | Source |
|---|---|---|---|
| analysis_objective | Generar una capacidad analitica para producir un informe ejecutivo sobre calidad de leads captados mediante Meta Ads, separando contexto, evidencia, preparacion, analisis, razonamiento, recomendaciones y construccion del informe. | Resolved | AUC-001; skill; project brief |
| supported_decision | Apoyar la lectura ejecutiva sobre volumen de captacion, calidad de leads, eficiencia economica, rendimiento de campanas y creatividades, oportunidades de optimizacion y recomendaciones priorizadas. | Resolved | AUC-001 |
| official_context_scope | VCA IA como sistema analitico corporativo de VCA que consume la plataforma de datos existente sin sustituirla. | Resolved | project brief; README; docs/context_refs.md |
| client_context_scope | Ecosistema VCA Project: captacion, FARO, CLARO, Meta Ads, BigQuery, scoring, activacion, integraciones y reporting. | Resolved | knowledge/client/ccd.md |
| primary_data_provider | BigQuery MCP Server. | Resolved as intended provider | AUC-001; docs/context_refs.md; skill |
| analysis_period | UNKNOWN. No existe un periodo concreto de analisis publicado para la ejecucion de AUC-001. | Blocking UNKNOWN | AUC-001; skill; Context Contract |
| campaign_scope | UNKNOWN. No existe delimitacion publicada de campanas, conjuntos de anuncios, creatividades, audiencias o segmentos concretos para esta ejecucion. | Blocking UNKNOWN | AUC-001; skill; Context Contract |
| lead_quality_criterion | Parcialmente resuelto: la definicion de Qualified Lead y el Modelo de Scoring FARO existen como criterio oficial de cualificacion, pero no hay una parametrizacion ejecutable publicada para esta ejecucion de AUC-001. | Partial / Blocking UNKNOWN | knowledge/client/ccd.md; AUC-001; skill |
| report_audience | Audiencia ejecutiva: analista de negocio, direccion, responsable de Marketing, especialistas de Meta Ads y equipo Comercial. | Resolved | AUC-001 |
| output_type | Informe ejecutivo trazable. | Resolved | AUC-001; skill |

---

## Operational Scope

| Dimension | Current Resolution | Status |
|---|---|---|
| Channel | Meta Ads | Resolved |
| Business object | Leads captados mediante Meta Ads | Resolved |
| Analytical focus | Volumen, calidad, eficiencia economica, campanas, creatividades, segmentacion y oportunidades de optimizacion | Resolved |
| Context framework | FARO, CLARO, KPIs oficiales y Knowledge Base del proyecto cuando esten disponibles | Resolved at context level |
| Data platform | BigQuery via BigQuery MCP Server as intended provider | Resolved as intended provider |
| Period | UNKNOWN | Blocking |
| Campaign / ad set / creative scope | UNKNOWN | Blocking |
| Executable lead-quality threshold | UNKNOWN / partial | Blocking |

---

## Constraints

- No se debe asumir contexto de negocio no publicado.
- No se deben inventar datos, segmentos, campanas, periodos ni conclusiones no sustentadas.
- BigQuery MCP Server es el Data Provider principal previsto, pero su documentacion aparece como PENDING en `docs/context_refs.md`.
- AIF Foundation debe tratarse como dependencia metodologica, no como objeto funcional del sistema.
- La fase Contexto no puede producir evidencia, interpretacion, conclusiones ni recomendaciones.
- Si falta periodo, alcance o criterio operativo suficiente, el flujo debe detenerse antes de Discovery o adquisicion de datos.

---

## Assumptions

| Assumption | Status | Basis |
|---|---|---|
| AUC-001 es el primer caso analitico aprobado para validar VCA IA. | Verified | project brief; AUC-001; docs/context_refs.md |
| BigQuery MCP Server sera la fuente principal de evidencia cuando los datos esten disponibles. | Verified as intended provider | AUC-001; skill |
| FARO y CLARO son contexto oficial del ecosistema de captacion y datos. | Verified | knowledge/client/ccd.md |
| El periodo de analisis se definira fuera de este artefacto antes de la ejecucion. | UNKNOWN | No hay fuente publicada con periodo concreto |

---

## Unknowns

| Unknown | Impact | Required Resolution Artifact |
|---|---|---|
| Periodo concreto de analisis | Bloquea la validacion completa del Context Definition y cualquier adquisicion de evidencia. | AUC-001 o solicitud/contexto operativo de ejecucion |
| Alcance concreto de campanas, conjuntos, creatividades, audiencias o segmentos | Bloquea una lectura operacional cerrada y puede afectar a Discovery. | AUC-001 o solicitud/contexto operativo de ejecucion |
| Parametrizacion ejecutable del criterio de calidad de lead para esta ejecucion | Bloquea la evaluacion completa de calidad si se requiere umbral operativo. | FARO/CLARO/Knowledge Base o Data Contract del caso |
| Disponibilidad tecnica/documentacion del BigQuery MCP Server | No bloquea esta resolucion de contexto, pero debe evaluarse antes de adquisicion de evidencia. | docs/context_refs.md o Data Contract del caso |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-016 - Validacion del Context Definition de AUC-001 | Ready for validation with blocking UNKNOWNs | Las fuentes oficiales, objetivo y alcance conceptual estan identificados, pero periodo, alcance operativo concreto y criterio ejecutable de calidad permanecen UNKNOWN. |
| Discovery / Data acquisition | Blocked | SPEC-001, AUC-001, la skill y VCA-CTX-001 exigen periodo y alcance suficientes antes de avanzar. |

---

## Traceability

- [T-015 in docs/tasks.md](../tasks.md)
- [AUC-001 Execution Context](auc-001-execution-context.md)
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

T-015 queda materializada como resolucion de contexto oficial para AUC-001.

La resolucion identifica las fuentes oficiales, el objetivo, el periodo y el alcance operativo del caso. El periodo y parte del alcance operativo se identifican como UNKNOWN porque no existe una fuente publicada que los concrete.

No se debe continuar hacia adquisicion de datos, Discovery, analisis o razonamiento hasta resolver los UNKNOWN bloqueantes o validarlos formalmente en T-016 como bloqueo.