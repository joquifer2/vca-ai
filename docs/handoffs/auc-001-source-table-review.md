# AUC-001 Source Table Review

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-SRC-REV-001 |
| Artifact Type | Corrective Source Table Review |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Status | Resolved for T-019 and T-020; T-021 implemented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Trigger | User review before T-022 |

---

## Purpose

Registrar la revision correctiva iniciada antes de T-022 tras detectar que el grano y las tablas usadas en T-020/T-021 no estaban suficientemente alineadas con las tablas disponibles en el workspace BigQuery ni con el alcance de AUC-001.

Este artefacto no sustituye el Data Contract, Discovery Contract ni Analytical Contract.

Este artefacto bloquea la produccion del Evidence Set hasta revalidar fuentes, grano y preparacion.

---

## Trigger

El usuario indico que las tablas de donde deben extraerse los datos para AUC-001 son las que existen en el workspace y cuestiono el grano `day + concept_id + version_id + angle_id` usado como modelo principal en T-020/T-021.

La revision confirma que el grano anterior fue derivado de una seleccion operativa de tablas, no de una fuente documental canonica que lo autorizara como Analytical Model principal.

---

## Workspace Inventory Findings

La documentacion canonica del repositorio no publica una lista cerrada de tablas para AUC-001. `docs/context_refs.md` mantiene `google_cloud.bigquery.tablas: []` y declara BigQuery MCP Server como proveedor principal pendiente de documentacion.

La inspeccion del workspace BigQuery `datamart-vca-494114` muestra tablas relevantes adicionales que no fueron utilizadas como fuentes principales en T-020/T-021.

### Candidate FARO / CLARO Tables

| Table | Layer | Relevance For AUC-001 | June 2026 Coverage |
|---|---|---|---:|
| `intermediate.int_faro_daily_grain` | Intermediate | Daily FARO grain with `campaign_signal`, leads breakdown and spend | 257 rows |
| `intermediate.int_faro_lead_scoring` | Intermediate | Lead-level scoring with campaign/adset/ad/form fields and `lead_tier` | 772 rows |
| `intermediate.int_faro_leads_unified` | Intermediate | Lead-level unified source with campaign/adset/ad/form fields | 772 rows |
| `marts.agg_performance_daily_angle` | Mart | Daily angle-level performance with `qualified_leads`, `qualified_cpl`, `qualified_rate`, `campaign_signal`, leads and spend | 220 rows |
| `marts.agg_performance_daily_concept` | Mart | Daily concept-level performance with `qualified_leads`, `qualified_cpl`, `qualified_rate`, `campaign_signal`, leads and spend | 143 rows |
| `marts.agg_decision_state_angle` | Mart | Decision-state snapshot by angle with qualified metrics and suggested action | 0 June rows; snapshot as of 2026-07-12 |
| `marts.agg_decision_state_concept` | Mart | Decision-state snapshot by concept with qualified metrics and suggested action | 0 June rows; snapshot as of 2026-07-12 |
| `raw_meta.facebook_ad_insights` | Raw Meta | Ad-level campaign/adset/ad metrics including impressions, clicks, spend and lead action fields | Coverage requires separate validation |

---
## User Confirmation

The user confirmed that the suitable AUC-001 extraction tables are:

- `marts.fct_spend`;
- `intermediate.int_faro_lead_scoring`;
- `marts.fct_lead_enriched`.

This confirmation supersedes the broader candidate list for the corrected T-019 Discovery path.
---

## Corrective Assessment

| Previous Statement | Assessment | Required Correction |
|---|---|---|
| `commercial_quality_efficiency_model` is the prepared primary model | Not sufficiently supported | Supersede until the source tables and analytical grain are reselected |
| Primary grain is `day + concept_id + version_id + angle_id` | Incomplete for AUC-001 | Re-evaluate against FARO/CLARO tables and AUC scope for campaign/adset/creative evidence |
| Qualified Leads must be reconstructed from `lead_tier IN ('A','B')` after alignment | Over-specific and potentially unnecessary | Use published FARO/CLARO `qualified_leads` where available; reconcile with lead-level scoring only when needed |
| Campaign/adset/creative can be excluded from primary model | Not aligned with AUC-001 scope | Campaign/adset/creative evidence must be either prepared from available workspace tables or explicitly blocked |
| T-022 was ready before correction | Incorrect at review time | T-022 had to remain blocked until T-019/T-020/T-021 were corrected |

---

## Immediate Blocking Decision

At the time of this corrective review, T-022 had to remain blocked until the preceding artifacts were corrected.

T-019, T-020 and T-021 required revision because the selected Discovery and Analytical Model did not sufficiently use the FARO/CLARO tables available in the workspace and did not justify why campaign/adset/creative evidence was excluded from the primary model.

T-017 and T-018 remain useful as provider-access evidence, but their selected source table list is incomplete for the corrected preparation path.

---

## Required Rework

| Artifact | Required Change |
|---|---|
| `auc-001-data-contract.md` | Record the expanded candidate source tables from workspace inventory and distinguish published FARO/CLARO tables from raw Meta tables |
| `auc-001-evidence-acquisition.md` | Add acquisition checks for FARO marts/intermediate tables and raw Meta ad-level table if needed |
| `auc-001-discovery-contract.md` | Rebuild Discovery around available FARO/CLARO tables, including qualified metrics and campaign/adset/creative availability |
| `auc-001-analytical-preparation.md` | Supersede the previous primary model and prepare a corrected model only after source/grain validation |
| `auc-001-analytical-contract.md` | Supersede the previous contract until the corrected Analytical Model is formalized |
| `docs/tasks.md` | Correct the revision state for T-019, T-020 and T-021; keep T-022 not started until the corrected T-021 contract exists |

---

## Traceability

- [AUC-001 Data Contract](auc-001-data-contract.md)
- [AUC-001 Evidence Acquisition](auc-001-evidence-acquisition.md)
- [AUC-001 Discovery Contract](auc-001-discovery-contract.md)
- [AUC-001 Analytical Preparation](auc-001-analytical-preparation.md)
- [AUC-001 Analytical Contract](auc-001-analytical-contract.md)
- [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md)

---


## Ad ID Correction

The user clarified that AUC-001 must not align lead quality and spend using `ad_id + concept_id + version_id + angle_id`.

The correct alignment key is `ad_id`.

Validation showed that lead tables store ad identifiers with an `ag:` prefix while `fct_spend.ad_id` stores the numeric Meta ad identifier without that prefix. After normalizing lead `ad_id` with `REGEXP_REPLACE(ad_id, r'^ag:', '')`, 8 of 10 commercial-spend ads match lead data, covering 680 leads, 191 Lead Tier A/B leads and 494.3600089999987 of commercial spend.
---
## T-020 Review Resolution

The T-020 review identified four issues: backlog contradiction, `qualified_ab` metric decision, creative scope and validation against `int_faro_lead_scoring`.

Resolution applied in `auc-001-analytical-preparation.md`:

- T-020 was temporarily removed from completed status during correction and is now completed after approval.
- `qualified_ab` is declared as a derived metric because approved source tables do not expose a published `qualified_leads` field.
- Creative scope is prepared as ad/creative reference using normalized `ad_id` and `ad_name`; full creative asset metadata remains unavailable.
- `int_faro_lead_scoring` validation is query-backed at normalized `ad_id` grain and matches `fct_lead_enriched` across 13 ads, 772 rows and 226 Lead Tier A/B.

T-020 has been approved after review; this section records the correction and approval basis.
---

## Completion Statement

The corrective review previously blocked T-022 until T-019, T-020 and T-021 were corrected.

The previous T-020/T-021 model must not be used as the basis for evidence production; use the corrected `ad_quality_spend_model` and the revised Analytical Contract.

T-019 Discovery has been revised using the user-confirmed source tables: `fct_spend`, `int_faro_lead_scoring` and `fct_lead_enriched`. T-020 revision has been approved. T-021 has been revised to formalize the corrected `ad_quality_spend_model`. T-022 may start only from the corrected T-021 Analytical Contract.