# AUC-001 Recommendation Set

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-REC-SET-001 |
| Artifact Type | Recommendation Set |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Execution ID | VCA-AUC-001-EXEC-2026-06 |
| Knowledge Contract ID | VCA-AUC-001-KNW-001 |
| Status | Stabilized |
| Period | 2026-06-01 to 2026-06-30 |
| Recommendation Count | 6 |

## Purpose

Formalizar acciones sugeridas derivadas exclusivamente del Knowledge Set estabilizado de AUC-001.

Este artefacto no crea evidencia nueva, no reescribe conclusiones y no constituye autorizacion operativa de ejecucion.

## Recommendation Summary

| Recommendation ID | Priority | Suggested Action | Knowledge Links |
|---|---|---|---|
| REC-001 | P1 | Base any near-term efficiency discussion on matched ad-level evidence first, especially the 8 matched ad references where both lead quality and commercial spend are present. | CON-001; PRI-001; INS-001; HYP-001 |
| REC-002 | P1 | Report and reason about RTG lead-only evidence separately from matched commercial-spend efficiency evidence. | INS-002; HYP-002; PRI-002; CON-002; UNC-005 |
| REC-003 | P2 | Before issuing campaign-level spend recommendations, either validate an approved campaign/adset spend mapping or explicitly keep campaign/adset spend recommendations out of scope. | CON-002; PRI-003; RSK-002; UNC-002 |
| REC-004 | P2 | Frame any creative-related recommendation at `ad_id_norm` / `ad_name` reference level only, and avoid claims about media, format or asset attributes. | INS-001; HYP-001; RSK-003; UNC-004 |
| REC-005 | P2 | Carry the duplicate/test-record limitation into downstream recommendation and presentation artifacts, and avoid overstating lead-count certainty. | UNC-001; RSK-005 |
| REC-006 | P3 | Do not make recommendations based on impressions, clicks or CTR in the current AUC-001 output; mark them unavailable unless a future approved source expansion provides them. | PRI-004; UNC-003; CON-001 |

## Recommendation Details

### REC-001 - Use matched ad-level evidence first

| Field | Value |
|---|---|
| Priority | P1 |
| Action | Use matched ad-level evidence as the primary basis for efficiency-oriented decisions. |
| Justification | Matched rows contain both lead quality and commercial spend, and CON-001 supports ad-level reasoning inside the corrected model. |
| Expected Impact | High qualitative impact on decision reliability. |
| Effort | Low to medium. |
| Dependencies | Confirmed Knowledge Set; preservation of `coverage_status`. |
| Risk | May underuse lead-only quality evidence if treated as the only valid lens. |
| Confidence | High within corrected model scope. |
| Validation Criterion | Efficiency-oriented discussion references matched ad-level evidence and preserves lead-only coverage separately. |

### REC-002 - Separate RTG lead-only quality reading

| Field | Value |
|---|---|
| Priority | P1 |
| Action | Treat RTG lead-only evidence as a separate quality reading, not matched spend efficiency. |
| Justification | RTG appears as lead-only evidence and PRI-002 requires separation from matched commercial-spend efficiency. |
| Expected Impact | High qualitative impact on methodological correctness. |
| Effort | Low. |
| Dependencies | `coverage_status = lead_only`; campaign/adset spend attribution limitation. |
| Risk | Stakeholders may expect RTG spend comparison. |
| Confidence | High for separation requirement; low for spend interpretation outside model. |
| Validation Criterion | RTG lead-only evidence is presented without spend-efficiency claims. |

### REC-003 - Validate campaign/adset spend mapping

| Field | Value |
|---|---|
| Priority | P2 |
| Action | Validate or document campaign/adset spend mapping before campaign-level spend recommendations. |
| Justification | Campaign/adset spend reasoning is only partially supported, and unsupported attribution is a documented risk. |
| Expected Impact | Medium to high qualitative impact by preventing unsupported campaign/adset conclusions. |
| Effort | UNKNOWN. |
| Dependencies | Source-table decision or future data-contract revision if campaign/adset spend attribution is required. |
| Risk | Delays campaign-level recommendations if mapping is unavailable. |
| Confidence | High for validation need; effort UNKNOWN. |
| Validation Criterion | Campaign/adset spend recommendations are either backed by approved mapping or explicitly excluded. |

### REC-004 - Keep creative guidance at ad-reference level

| Field | Value |
|---|---|
| Priority | P2 |
| Action | Keep creative recommendations at ad-reference level unless creative asset metadata is added. |
| Justification | Creative asset metadata is unavailable, and ad-reference concentration must not become creative causality. |
| Expected Impact | Medium qualitative impact by reducing overinterpretation risk. |
| Effort | Low for wording discipline; UNKNOWN for asset-level analysis. |
| Dependencies | Ad-reference naming; explicit creative metadata limitation. |
| Risk | Limits creative production guidance until richer creative metadata exists. |
| Confidence | High for current scope; UNKNOWN for asset-level analysis. |
| Validation Criterion | Creative-related statements refer only to `ad_id_norm` / `ad_name` and avoid media, format or asset claims. |

### REC-005 - Preserve duplicate/test-record uncertainty

| Field | Value |
|---|---|
| Priority | P2 |
| Action | Preserve duplicate/test-record uncertainty in downstream decisions and final output. |
| Justification | Duplicate/test-record uncertainty remains unresolved and must not be hidden in downstream decisions. |
| Expected Impact | Medium qualitative impact by improving auditability. |
| Effort | Low for documentation; UNKNOWN for data remediation. |
| Dependencies | Future source mapping required for full resolution. |
| Risk | Downstream recommendations may appear more certain than evidence supports if omitted. |
| Confidence | High for propagation requirement. |
| Validation Criterion | Lead-count statements visibly retain the duplicate/test-record limitation. |

### REC-006 - Exclude unavailable funnel-entry metrics

| Field | Value |
|---|---|
| Priority | P3 |
| Action | Exclude impressions, clicks and CTR from recommendations unless source scope is expanded. |
| Justification | Impressions, clicks and CTR are unavailable in the corrected source set. |
| Expected Impact | Medium qualitative impact by keeping recommendations evidence-aligned. |
| Effort | Low for current output; UNKNOWN if source expansion is requested. |
| Dependencies | Future source-table decision for funnel-entry metrics. |
| Risk | Output may be less complete for stakeholders expecting full funnel metrics. |
| Confidence | High for current exclusion. |
| Validation Criterion | Current recommendations do not use impressions, clicks or CTR. |

## Priority Contract

| Priority | Recommendation IDs | Rationale |
|---|---|---|
| P1 | REC-001; REC-002 | Highest need to preserve correct efficiency and quality reading from confirmed knowledge. |
| P2 | REC-003; REC-004; REC-005 | Important controls for campaign/adset, creative and data-quality uncertainty. |
| P3 | REC-006 | Scope guardrail for unavailable funnel-entry metrics. |

## Uncertainty Propagation

| Uncertainty | Affected Recommendations | Handling |
|---|---|---|
| UNC-001 duplicate/test-record flags not explicitly mapped | REC-005 | Preserve limitation in downstream artifacts. |
| UNC-002 spend-only campaign/adset metadata UNKNOWN | REC-003 | Do not issue campaign/adset spend recommendations without mapping. |
| UNC-003 impressions/clicks/CTR unavailable | REC-006 | Exclude from current recommendations unless source scope expands. |
| UNC-004 creative asset metadata unavailable | REC-004 | Keep creative recommendations at ad-reference level. |
| UNC-005 `campaign_signal` spend-side only | REC-002 | Do not treat lead rows as directly commercial. |

## Stabilization Statement

The Recommendation Set is stabilized for Presentation Layer. All recommendations derive from the Knowledge Set and preserve approved priorities, risks, limitations and UNKNOWNs.
