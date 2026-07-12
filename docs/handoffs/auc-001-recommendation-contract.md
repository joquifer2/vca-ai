# AUC-001 Recommendation Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-AUC-001-REC-001 |
| Contract Name | AUC-001 Recommendation Contract |
| Contract Category | Recommendation Contract |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Related Base Contract | VCA-REC-001 |
| Recommendation Set ID | VCA-AUC-001-REC-SET-001 |
| Knowledge Contract ID | VCA-AUC-001-KNW-001 |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Backing Task | T-028 |

---

## Purpose

Formalizar el Recommendation Set de AUC-001 como handoff contractual desde la fase de Recomendaciones hacia la validacion y la futura capa de presentacion.

Este contract estructura acciones sugeridas, justificacion, prioridad, impacto esperado, esfuerzo, dependencias, riesgos, confianza y trazabilidad.

Este contract no crea evidencia nueva.

Este contract no reescribe conclusiones.

Este contract no construye el artefacto final de presentacion.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-028 |
| Task | Implementar el Recommendation Contract del caso AUC-001 |
| Specifications | SPEC-001 Analytical Lifecycle; SPEC-002 Component Boundaries; SPEC-004 Transversal Contracts |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | Existe un Recommendation Contract con acciones sugeridas, justificacion, prioridad y trazabilidad explicita |
| Implementation basis | T-027 Recommendation Set |

---

## Producer And Consumer

| Role | Value |
|---|---|
| Producer | Reasoning Layer / Phase 5 Recommendations |
| Consumer | Framework and future Presentation Layer |
| Framework role | Validate readiness before Presentation Contract |
| Downstream artifact | T-029 Recommendation Set confirmation; T-030 Presentation Contract |

---

## Inputs

| Input | Artifact | Status |
|---|---|---|
| Context Definition | [AUC-001 Context Definition](auc-001-context-definition.md) | Validated |
| Knowledge Contract | [AUC-001 Knowledge Contract](auc-001-knowledge-contract.md) | Completed |
| Knowledge Set | [AUC-001 Knowledge Set](auc-001-knowledge-set.md) | Confirmed |
| Recommendation Set | [AUC-001 Recommendation Set](auc-001-recommendation-set.md) | Completed |
| AUC-001 | [Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md) | Available |
| Skill | [meta-lead-quality-analysis](../../.github/skills/meta-lead-quality-analysis/SKILL.md) | Available |

---

## Recommendation Scope

| Field | Value |
|---|---|
| recommendation_set_id | VCA-AUC-001-REC-SET-001 |
| knowledge_contract_id | VCA-AUC-001-KNW-001 |
| knowledge_set_id | VCA-AUC-001-KNW-SET-001 |
| context_contract_id | VCA-AUC-001-CTX-DEF-2026-06 |
| period | 2026-06-01 to 2026-06-30 |
| source_model | `ad_quality_spend_model` |
| recommendation_count | 6 |
| recommendation_ids | REC-001, REC-002, REC-003, REC-004, REC-005, REC-006 |
| recommendation_boundary | Contract formalization only; no execution and no presentation artifact |

---

## Contracted Recommendations

| Recommendation ID | Priority | Suggested Action Summary | Knowledge Links | Status |
|---|---|---|---|---|
| REC-001 | P1 | Use matched ad-level evidence as the primary basis for efficiency-oriented decisions | CON-001; PRI-001; INS-001; HYP-001 | Contracted |
| REC-002 | P1 | Treat RTG lead-only evidence as a separate quality reading, not matched spend efficiency | INS-002; HYP-002; PRI-002; CON-002; UNC-005 | Contracted |
| REC-003 | P2 | Validate or document campaign/adset spend mapping before campaign-level spend recommendations | CON-002; PRI-003; RSK-002; UNC-002 | Contracted |
| REC-004 | P2 | Keep creative recommendations at ad-reference level unless creative asset metadata is added | INS-001; HYP-001; RSK-003; UNC-004 | Contracted |
| REC-005 | P2 | Preserve duplicate/test-record uncertainty in downstream decisions and final output | UNC-001; RSK-005 | Contracted |
| REC-006 | P3 | Exclude impressions, clicks and CTR from recommendations unless source scope is expanded | PRI-004; UNC-003; CON-001 | Contracted |

---

## Suggested Actions

| Recommendation ID | Suggested Action | Priority |
|---|---|---|
| REC-001 | Base any near-term efficiency discussion on matched ad-level evidence first, especially the 8 matched ad references where both lead quality and commercial spend are present. | P1 |
| REC-002 | Report and reason about RTG lead-only evidence separately from matched commercial-spend efficiency evidence. | P1 |
| REC-003 | Before issuing campaign-level spend recommendations, either validate an approved campaign/adset spend mapping or explicitly keep campaign/adset spend recommendations out of scope. | P2 |
| REC-004 | Frame any creative-related recommendation at `ad_id_norm` / `ad_name` reference level only, and avoid claims about media, format or asset attributes. | P2 |
| REC-005 | Carry the duplicate/test-record limitation into downstream recommendation and presentation artifacts, and avoid overstating lead-count certainty. | P2 |
| REC-006 | Do not make recommendations based on impressions, clicks or CTR in the current AUC-001 output; mark them unavailable unless a future approved source expansion provides them. | P3 |

---

## Justification And Impact

| Recommendation ID | Justification | Expected Impact |
|---|---|---|
| REC-001 | Matched rows contain both lead quality and commercial spend, and CON-001 supports ad-level reasoning inside the corrected model. | High qualitative impact on decision reliability |
| REC-002 | RTG appears as lead-only evidence and PRI-002 requires separation from matched commercial-spend efficiency. | High qualitative impact on methodological correctness |
| REC-003 | Campaign/adset spend reasoning is only partially supported, and unsupported attribution is a documented risk. | Medium to high qualitative impact by preventing unsupported campaign/adset conclusions |
| REC-004 | Creative asset metadata is unavailable, and ad-reference concentration must not become creative causality. | Medium qualitative impact by reducing overinterpretation risk |
| REC-005 | Duplicate/test-record uncertainty remains unresolved and must not be hidden in downstream decisions. | Medium qualitative impact by improving auditability |
| REC-006 | Impressions, clicks and CTR are unavailable in the corrected source set. | Medium qualitative impact by keeping recommendations evidence-aligned |

---

## Effort, Dependencies, Risks And Confidence

| Recommendation ID | Effort | Dependencies | Risks | Confidence |
|---|---|---|---|---|
| REC-001 | Low to medium | Confirmed Knowledge Set; preservation of `coverage_status` | May underuse lead-only quality evidence if treated as the only valid lens | High within corrected model scope |
| REC-002 | Low | `coverage_status = lead_only`; campaign/adset spend attribution limitation | Stakeholders may expect RTG spend comparison | High for separation requirement; low for spend interpretation outside model |
| REC-003 | UNKNOWN | Source-table decision or future data-contract revision if campaign/adset spend attribution is required | Delays campaign-level recommendations if mapping is unavailable | High for validation need; effort UNKNOWN |
| REC-004 | Low for wording discipline; UNKNOWN for asset-level analysis | Ad-reference naming; explicit creative metadata limitation | Limits creative production guidance until richer creative metadata exists | High for current scope; UNKNOWN for asset-level analysis |
| REC-005 | Low for documentation; UNKNOWN for data remediation | Future source mapping required for full resolution | Downstream recommendations may appear more certain than evidence supports if omitted | High for propagation requirement |
| REC-006 | Low for current output; UNKNOWN if source expansion is requested | Future source-table decision for funnel-entry metrics | Output may be less complete for stakeholders expecting full funnel metrics | High for current exclusion |

---

## Priority Contract

| Priority | Recommendation IDs | Contracted Rationale |
|---|---|---|
| P1 | REC-001; REC-002 | Highest need to preserve correct efficiency and quality reading from confirmed knowledge |
| P2 | REC-003; REC-004; REC-005 | Important controls for campaign/adset, creative and data-quality uncertainty |
| P3 | REC-006 | Scope guardrail for unavailable funnel-entry metrics |

---

## Uncertainty Propagation

| Uncertainty | Affected Recommendations | Contracted Handling |
|---|---|---|
| UNC-001 duplicate/test-record flags not explicitly mapped | REC-005 | Preserve limitation in downstream artifacts |
| UNC-002 spend-only campaign/adset metadata UNKNOWN | REC-003 | Do not issue campaign/adset spend recommendations without mapping |
| UNC-003 impressions/clicks/CTR unavailable | REC-006 | Exclude from current recommendations unless source scope expands |
| UNC-004 creative asset metadata unavailable | REC-004 | Keep creative recommendations at ad-reference level |
| UNC-005 `campaign_signal` spend-side only | REC-002 | Do not treat lead rows as directly commercial |

---

## Critical Fields

| Field | Status | Notes |
|---|---|---|
| contract_id | Present | `VCA-AUC-001-REC-001` |
| context_contract_id | Present | `VCA-AUC-001-CTX-DEF-2026-06` |
| knowledge_contract_id | Present | `VCA-AUC-001-KNW-001` |
| recommendation_scope | Present | AUC-001 recommendations from confirmed Knowledge Set |
| suggested_actions | Present | REC-001 through REC-006 |
| justification | Present | Contracted for each recommendation |
| priority | Present | P1 through P3 |
| expected_impact | Present | Qualitative only, no unsupported quantitative impact |
| effort | Present | Low, low-to-medium, or UNKNOWN as supported |
| dependencies | Present | Contracted for each recommendation |
| risks | Present | Contracted for each recommendation |
| confidence | Present | Contracted for each recommendation |
| traceability_links | Present | Knowledge, evidence and source artifacts listed below |
| transition_status | Present | T-029 ready to start after T-028 completion |

---

## Validation Rules Applied

| Rule | Result | Evidence |
|---|---|---|
| Knowledge dependency | Pass | Contract consumes `VCA-AUC-001-KNW-001` |
| Recommendation Set dependency | Pass | Contract formalizes `VCA-AUC-001-REC-SET-001` |
| Action traceability | Pass | Every action links to knowledge IDs and uncertainty notes |
| Justification required | Pass | Each recommendation has justification |
| Priority required | Pass | Each recommendation has P1, P2 or P3 |
| Uncertainty propagation | Pass | UNC-001 through UNC-005 are mapped to affected recommendations |
| No new evidence | Pass | Contract does not introduce new observations or metrics |
| No presentation rewrite | Pass | Contract does not create an output artifact or executive narrative |
| Scope alignment | Pass | Recommendations remain inside corrected AUC-001 model and limitations |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-028 Recommendation Contract | Completed | Recommendation Set is formalized with required metadata and traceability |
| T-029 Recommendation Set | Completed | Recommendation Set has been confirmed against this contract |
| T-030 Presentation Contract | Completed | Presentation Contract consumes this recommendation contract and confirmed Recommendation Set |
| T-031 Executive Output Artifact | Ready to start | Requires consuming the Presentation Contract without new evidence or interpretation |

---

## Traceability

- [T-028 in docs/tasks.md](../tasks.md)
- [AUC-001 Recommendation Set](auc-001-recommendation-set.md)
- [AUC-001 Knowledge Contract](auc-001-knowledge-contract.md)
- [AUC-001 Knowledge Set](auc-001-knowledge-set.md)
- [AUC-001 Evidence Contract](auc-001-evidence-contract.md)
- [VCA-REC-001 Base Recommendation Contract](../contracts/recommendation.contract.md)
- [SPEC-001 Analytical Lifecycle](../../specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](../../specs/spec-002-component-boundaries.md)
- [SPEC-004 Transversal Contracts](../../specs/spec-004-transversal-contracts.md)
- [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md)

---

## Completion Statement

T-028 is complete.

The Recommendation Contract formalizes six AUC-001 recommendations with priority, justification, qualitative impact, effort, dependencies, risks, confidence and explicit traceability to the Knowledge Contract.

T-029 has confirmed the Recommendation Set against this contract. T-030 has defined the Presentation Contract, so T-031 may now construct the executive output artifact under presentation constraints.