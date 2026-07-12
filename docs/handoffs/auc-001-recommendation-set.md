# AUC-001 Recommendation Set

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-REC-SET-001 |
| Artifact Type | Recommendation Set |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Knowledge Contract ID | VCA-AUC-001-KNW-001 |
| Knowledge Set ID | VCA-AUC-001-KNW-SET-001 |
| Evidence Contract ID | VCA-AUC-001-EVD-001 |
| Status | Confirmed against Recommendation Contract |
| Version | 1.1.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Backing Task | T-027; T-029 confirmation |

---

## Purpose

Registrar acciones sugeridas, justificadas y priorizadas a partir del Knowledge Set confirmado de AUC-001.

Este Recommendation Set convierte conocimiento trazable en acciones evaluables.

Este artefacto queda confirmado contra `VCA-AUC-001-REC-001` como salida trazable de Recomendaciones para AUC-001.

Este artefacto no crea evidencia nueva.

Este artefacto no reescribe conclusiones.

Este artefacto no construye el informe final ni define formato de presentacion.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-027; T-029 |
| Task | T-027: Implementar la capa de recomendaciones del caso AUC-001; T-029: Implementar el Recommendation Set de AUC-001 |
| Specifications | SPEC-001 Analytical Lifecycle; SPEC-002 Component Boundaries |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | El flujo convierte el conocimiento en acciones sugeridas, justificadas y priorizadas; existe un Recommendation Set con acciones priorizadas, justificacion y trazabilidad a la evidencia y al conocimiento |
| Implementation basis | T-026 confirmed Knowledge Set; T-025 Knowledge Contract; T-028 Recommendation Contract |

---

## Recommendation Scope

| Field | Value |
|---|---|
| knowledge_contract_id | VCA-AUC-001-KNW-001 |
| knowledge_set_id | VCA-AUC-001-KNW-SET-001 |
| period | 2026-06-01 to 2026-06-30 |
| source_model | `ad_quality_spend_model` |
| recommendation_boundary | Suggested actions only; no execution, no presentation artifact, no new evidence |
| uncertainty_policy | Propagate UNC-001 through UNC-005 and avoid unsupported quantitative impact or effort claims |

---

## Prioritization Criteria

| Criterion | Description |
|---|---|
| Evidence traceability | Recommendation must link to knowledge IDs and evidence-backed conclusions |
| Risk control | Recommendation should reduce a documented risk or protect downstream interpretation |
| Decision usefulness | Recommendation should improve how AUC-001 can support lead quality and spend decisions |
| Scope compliance | Recommendation must remain inside the corrected model and documented uncertainty |
| Execution clarity | Recommendation must be stated as an action that can be reviewed or assigned later |

---

## Suggested Actions

### REC-001 - Use matched ad-level evidence as the primary basis for efficiency-oriented decisions

| Field | Value |
|---|---|
| Suggested action | Base any near-term efficiency discussion on matched ad-level evidence first, especially the 8 matched ad references where both lead quality and commercial spend are present. |
| Justification | PRI-001 identifies matched ad-level evidence as the strongest reasoning base because it contains both lead quality and commercial spend. CON-001 confirms AUC-001 has sufficient ad-level evidence within the corrected model. |
| Priority | P1 |
| Expected impact | High qualitative impact on decision reliability, because it avoids mixing lead-only or spend-only rows into efficiency claims. |
| Effort | Low to medium; requires using the existing Recommendation/Presentation flow with coverage filtering. |
| Dependencies | Confirmed Knowledge Set; preservation of `coverage_status`; no requery required. |
| Risks | May underuse lead-only quality evidence if treated as the only valid lens. |
| Confidence | High within corrected model scope. |
| Traceability | CON-001; PRI-001; INS-001; HYP-001; EVD-001; EVD-003 |

### REC-002 - Treat RTG lead-only evidence as a separate quality reading, not as matched spend efficiency

| Field | Value |
|---|---|
| Suggested action | Report and reason about RTG lead-only evidence separately from matched commercial-spend efficiency evidence. |
| Justification | INS-002 and HYP-002 show that the RTG campaign/adset appears as lead-only in the approved model; PRI-002 requires treating lead-only evidence as quality evidence without matched commercial spend. |
| Priority | P1 |
| Expected impact | High qualitative impact on methodological correctness, because it prevents unsupported cost-efficiency statements for lead-only rows. |
| Effort | Low; requires separate grouping or labeling in downstream recommendation and presentation artifacts. |
| Dependencies | `coverage_status = lead_only`; Knowledge Contract limitations on campaign/adset spend attribution. |
| Risks | Stakeholders may still expect spend comparison for RTG; this must be marked unavailable from the corrected model. |
| Confidence | High for separation requirement; low for any spend interpretation outside the model. |
| Traceability | INS-002; HYP-002; PRI-002; CON-002; UNC-005; EVD-004 |

### REC-003 - Validate or document campaign/adset spend mapping before making campaign-level spend recommendations

| Field | Value |
|---|---|
| Suggested action | Before issuing campaign-level spend recommendations, either validate an approved campaign/adset spend mapping or explicitly keep campaign/adset spend recommendations out of scope. |
| Justification | CON-002 states campaign/adset reasoning is only partially supported; RSK-002 identifies unsupported campaign/adset spend interpretation as a risk. |
| Priority | P2 |
| Expected impact | Medium to high qualitative impact by preventing unsupported campaign/adset budget or efficiency conclusions. |
| Effort | UNKNOWN; depends on whether an approved mapping or expanded source table is available. |
| Dependencies | Source-table decision or future data-contract revision if campaign/adset spend attribution is required. |
| Risks | Delays campaign-level recommendations if mapping is unavailable. |
| Confidence | High for the need to validate; UNKNOWN for implementation effort. |
| Traceability | CON-002; PRI-003; RSK-002; UNC-002; EVD-004 |

### REC-004 - Keep creative recommendations at ad-reference level unless creative asset metadata is added

| Field | Value |
|---|---|
| Suggested action | Frame any creative-related recommendation at `ad_id_norm` / `ad_name` reference level only, and avoid claims about media, format or asset attributes. |
| Justification | RSK-003 warns against turning ad-reference concentration into creative causality; UNC-004 states creative asset metadata is unavailable. |
| Priority | P2 |
| Expected impact | Medium qualitative impact by reducing overinterpretation risk in creative discussion. |
| Effort | Low for wording discipline; UNKNOWN if asset-level recommendations are required later. |
| Dependencies | Preservation of ad-reference naming and explicit creative metadata limitation. |
| Risks | Limits creative production guidance until richer creative metadata exists. |
| Confidence | High for current scope; UNKNOWN for future asset-level analysis. |
| Traceability | INS-001; HYP-001; RSK-003; UNC-004; EVD-003 |

### REC-005 - Preserve duplicate/test-record uncertainty in downstream decisions and final output

| Field | Value |
|---|---|
| Suggested action | Carry the duplicate/test-record limitation into downstream recommendation and presentation artifacts, and avoid overstating lead-count certainty. |
| Justification | UNC-001 and RSK-005 state that duplicate/test-record flags are not explicitly mapped and that ignoring this uncertainty could overstate certainty. |
| Priority | P2 |
| Expected impact | Medium qualitative impact by improving auditability and reducing certainty overstatement. |
| Effort | Low for documentation; UNKNOWN for data remediation. |
| Dependencies | No immediate data change required; future source mapping required for resolution. |
| Risks | If omitted, downstream recommendations may appear more certain than the evidence supports. |
| Confidence | High for propagation requirement. |
| Traceability | UNC-001; RSK-005; Evidence Contract uncertainty notes |

### REC-006 - Exclude impressions, clicks and CTR from recommendations unless source scope is expanded

| Field | Value |
|---|---|
| Suggested action | Do not make recommendations based on impressions, clicks or CTR in the current AUC-001 output; mark them unavailable unless a future approved source expansion provides them. |
| Justification | UNC-003 states impressions, clicks and CTR are unavailable; PRI-004 requires propagating missing evidence families instead of filling gaps by assumption. |
| Priority | P3 |
| Expected impact | Medium qualitative impact by keeping recommendations aligned with available evidence. |
| Effort | Low for current output; UNKNOWN if source expansion is requested. |
| Dependencies | Future source-table decision if funnel-entry metrics are required. |
| Risks | Output may be less complete for stakeholders expecting full funnel metrics. |
| Confidence | High for exclusion in current scope. |
| Traceability | PRI-004; UNC-003; CON-001; Evidence Contract limitations |

---

## Recommendation Priority Summary

| Priority | Recommendations | Rationale |
|---|---|---|
| P1 | REC-001; REC-002 | Highest need to preserve correct efficiency and quality reading from the confirmed Knowledge Set |
| P2 | REC-003; REC-004; REC-005 | Important controls for campaign/adset, creative and data-quality uncertainty |
| P3 | REC-006 | Scope guardrail for unavailable funnel-entry metrics |

---

## Dependency Summary

| Dependency | Affected Recommendations | Handling |
|---|---|---|
| Confirmed Knowledge Set | REC-001 through REC-006 | Required input; no re-opening of reasoning |
| Coverage status preservation | REC-001; REC-002 | Must remain visible in downstream artifacts |
| Campaign/adset spend mapping | REC-003 | UNKNOWN; requires future source-table decision if needed |
| Creative asset metadata | REC-004 | UNKNOWN; keep at ad-reference level |
| Duplicate/test-record mapping | REC-005 | UNKNOWN; propagate uncertainty |
| Impressions/clicks/CTR source expansion | REC-006 | Not authorized in current scope |

---

## Risk And Confidence Summary

| Recommendation | Main Risk | Confidence |
|---|---|---|
| REC-001 | Over-narrowing decisions to matched rows only | High within corrected model scope |
| REC-002 | Stakeholder expectation of RTG spend comparison | High for separation requirement |
| REC-003 | Mapping unavailable or outside current scope | High for validation need; effort UNKNOWN |
| REC-004 | Stakeholder expectation of asset-level creative guidance | High for current scope boundary |
| REC-005 | Downstream certainty overstatement | High for propagation requirement |
| REC-006 | Incomplete funnel narrative | High for current exclusion |

---

## Contract Confirmation

| Check | Result | Evidence |
|---|---|---|
| Recommendation Contract dependency | Pass | `VCA-AUC-001-REC-001` formalizes this Recommendation Set |
| Action coverage | Pass | REC-001 through REC-006 are present |
| Priority coverage | Pass | P1, P2 and P3 are present and aligned with contract |
| Justification coverage | Pass | Every recommendation has a documented justification |
| Impact coverage | Pass | Expected impact is qualitative, not unsupported quantitative impact |
| Effort coverage | Pass | Effort is low, low-to-medium or UNKNOWN according to documented support |
| Dependency coverage | Pass | Dependencies and source-scope constraints are present |
| Risk coverage | Pass | Each recommendation has a stated risk |
| Confidence coverage | Pass | Confidence is documented for each recommendation |
| Uncertainty propagation | Pass | UNC-001 through UNC-005 are propagated through recommendations |
| Presentation boundary | Pass | No final report, executive narrative or presentation format is introduced |

## Confirmed Recommendation Inventory

| Priority | Recommendation IDs | Status |
|---|---|---|
| P1 | REC-001, REC-002 | Confirmed |
| P2 | REC-003, REC-004, REC-005 | Confirmed |
| P3 | REC-006 | Confirmed |

## Knowledge And Evidence Traceability Matrix

| Recommendation ID | Knowledge Links | Evidence Or Limitation Links | Traceability Status |
|---|---|---|---|
| REC-001 | CON-001; PRI-001; INS-001; HYP-001 | EVD-001; EVD-003 | Complete |
| REC-002 | INS-002; HYP-002; PRI-002; CON-002; UNC-005 | EVD-004 | Complete |
| REC-003 | CON-002; PRI-003; RSK-002; UNC-002 | EVD-004; campaign/adset limitation | Complete |
| REC-004 | INS-001; HYP-001; RSK-003; UNC-004 | EVD-003; creative metadata limitation | Complete |
| REC-005 | UNC-001; RSK-005 | Evidence Contract uncertainty notes | Complete |
| REC-006 | PRI-004; UNC-003; CON-001 | Evidence Contract source-scope limitation | Complete |

---
## Boundary Compliance

| Rule | Result | Evidence |
|---|---|---|
| Knowledge dependency | Pass | Consumes `VCA-AUC-001-KNW-001` and confirmed Knowledge Set |
| Action traceability | Pass | Every recommendation links to knowledge IDs and evidence limits |
| No new evidence | Pass | No new metrics, source queries or observed facts are introduced |
| No conclusion rewrite | Pass | Recommendations preserve CON-001 and CON-002 scope limits |
| Uncertainty propagation | Pass | UNC-001 through UNC-005 are reflected in actions and dependencies |
| No presentation artifact | Pass | This is not an executive report or presentation contract |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-027 Recommendation Layer | Completed | Recommendation Set has been produced from the confirmed Knowledge Set |
| T-029 Recommendation Set confirmation | Completed | Recommendation Set has been confirmed against the Recommendation Contract |
| T-028 Recommendation Contract | Completed | Recommendations have been formalized contractually |
| T-029 Recommendation Set | Completed | Recommendation Set is aligned with the Recommendation Contract |
| T-030 Presentation Contract | Completed | Presentation Contract consumes confirmed recommendations without new interpretation |

---

## Traceability

- [T-027 in docs/tasks.md](../tasks.md)
- [T-029 in docs/tasks.md](../tasks.md)
- [AUC-001 Recommendation Contract](auc-001-recommendation-contract.md)
- [AUC-001 Knowledge Set](auc-001-knowledge-set.md)
- [AUC-001 Knowledge Contract](auc-001-knowledge-contract.md)
- [AUC-001 Evidence Contract](auc-001-evidence-contract.md)
- [VCA-REC-001 Base Recommendation Contract](../contracts/recommendation.contract.md)
- [SPEC-001 Analytical Lifecycle](../../specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](../../specs/spec-002-component-boundaries.md)
- [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md)

---

## Completion Statement

T-027 and T-029 are complete.

The Recommendation Set converts the confirmed AUC-001 Knowledge Set into six traceable suggested actions with priority, justification, expected impact, effort, dependencies, risks and confidence. It has been confirmed against `VCA-AUC-001-REC-001`.

T-030 has defined the Presentation Contract for consuming these confirmed recommendations without adding evidence, reasoning or new recommendations. T-031 may now construct the executive output artifact under that contract.