# AUC-001 Base Contracts Alignment Assessment

## Metadata

| Field | Value |
|---|---|
| Evaluation ID | VCA-AUC-001-EVAL-040 |
| Evaluation Name | Base Contracts Alignment Assessment |
| Evaluation Type | Validation / Review |
| Backing Task | T-040 |
| Status | Completed |
| Decision | PASS WITH JUSTIFIED FOLLOW-UP CHANGES |
| Evaluation Date | 2026-07-13 |
| Owner | Reviewer Agent |
| Scope | Impact of SPEC-010, VCA-AUC-001-ARCH-001 and VCA-AUC-001-ARCH-002 on base Context and Presentation Contracts |

---

## Purpose

Evaluate whether the new presentation projection capability documented in SPEC-010 and supported by VCA-AUC-001-ARCH-001 / VCA-AUC-001-ARCH-002 requires explicit specialization of the base contracts:

- `docs/contracts/context.contract.md` (`VCA-CTX-001`);
- `docs/contracts/presentation.contract.md` (`VCA-PRS-001`).

This assessment does not modify the evaluated contracts.

This assessment does not update AUC-001 handoffs.

This assessment does not implement Presentation Layer behavior.

---

## Sources Consulted

| Source | Role In Assessment |
|---|---|
| `docs/contracts/context.contract.md` | Base Context Contract under review |
| `docs/contracts/presentation.contract.md` | Base Presentation Contract under review |
| `docs/contracts.md` | Contract inventory and status |
| `specs/spec-001-analytical-lifecycle.md` | Lifecycle rules for context and presentation phases |
| `specs/spec-002-component-boundaries.md` | Component and Presentation Layer boundaries |
| `specs/spec-004-transversal-contracts.md` | Contract category and metadata rules |
| `specs/spec-010-presentation-projection-selection.md` | New projection selection capability under assessment |
| `docs/decisions/auc-001/auc-001-execution-scope-canonicalization-architectural-decision.md` | VCA-AUC-001-ARCH-001 |
| `docs/decisions/auc-001/auc-001-presentation-projection-architectural-decision.md` | VCA-AUC-001-ARCH-002 |
| `docs/context_refs.md` | Official context index and decision trace |
| `docs/tasks.md` | T-040 definition and acceptance criteria |

---

## Assessment Criteria

| Criterion | Basis |
|---|---|
| Boundary compliance | SPEC-001, SPEC-002, SPEC-004 |
| Projection selection support | SPEC-010 FR-001 through FR-005 and BR-001 through BR-003 |
| Execution scope canonicalization support | VCA-AUC-001-ARCH-001 |
| Presentation projection support | VCA-AUC-001-ARCH-002 |
| Contract stability | SPEC-004 stability rules |
| Change necessity | T-040 result must distinguish no-change from justified-change |

---

## Context Contract Assessment

### Observed Coverage

`VCA-CTX-001` already covers core context responsibilities required by SPEC-001 and SPEC-004:

| Requirement Area | Evidence In Contract | Assessment |
|---|---|---|
| Analysis objective | `analysis_objective` critical field | Covered |
| Supported decision | `supported_decision` critical field | Covered |
| Analysis scope | `analysis_scope` critical field and Operational Scope input | Covered |
| Official context sources | `official_context_sources` critical field | Covered |
| Constraints and assumptions | Critical fields and validation rules | Covered |
| UNKNOWN handling | Unknown Handling section | Covered |
| Boundary compliance | Contract explicitly forbids evidence, interpretation, conclusions and recommendations | Covered |

### Gaps Against New Capability

| Gap ID | Gap | Evidence | Impact |
|---|---|---|---|
| CTX-GAP-001 | The base contract does not explicitly name `Execution Scope Canonicalization` as a required precondition or output. | VCA-AUC-001-ARCH-001 identifies this as the reusable responsibility between human request and frozen Execution Context. | A future execution could still treat canonicalization as implicit, increasing risk of inherited scope leakage. |
| CTX-GAP-002 | The base contract does not require a canonicalization result distinguishing execution parameters from methodological parameters. | VCA-AUC-001-ARCH-001 defines these categories and their default handling. | The contract can delimit scope, but does not yet prove the scope was canonicalized under the new rule. |
| CTX-GAP-003 | The base contract does not explicitly carry selected presentation projection or the fields needed to determine it. | SPEC-010 requires projection selection from canonicalized Execution Context using audience, purpose and decision type. | Projection selection may remain downstream or ad hoc unless the context boundary exposes enough structured information. |
| CTX-GAP-004 | `Output Request` appears indirectly in inputs but is not a critical field of `VCA-CTX-001`. | SPEC-010 lists `Output Request` as an input and requires blocking if projection cannot be determined. | Ambiguous output requests may not be handled as first-class blocking context defects. |

### Decision For Context Contract

`VCA-CTX-001` remains valid for the existing lifecycle and AUC-001 execution records, but **changes are justified** if the repository incorporates SPEC-010 as an active capability.

Recommended future change scope:

- add explicit support for `Execution Scope Canonicalization` as a context readiness requirement;
- add canonicalization result fields or equivalent critical fields;
- distinguish execution parameters from inherited methodological parameters;
- promote `Output Request` / presentation projection determinability into critical context validation when presentation selection is in scope;
- preserve the contract's current prohibition against evidence, interpretation and recommendations.

No immediate edit is performed in T-040.

---

## Presentation Contract Assessment

### Observed Coverage

`VCA-PRS-001` already contains strong boundary controls aligned with SPEC-001, SPEC-002 and SPEC-004:

| Requirement Area | Evidence In Contract | Assessment |
|---|---|---|
| Approved content scope | `Presentation Content Scope` output | Covered |
| Knowledge dependency | Knowledge Set / Knowledge Contract inputs and validation rules | Covered |
| Recommendation dependency | Recommendation Set / Recommendation Contract inputs and validation rules | Covered |
| Evidence references | `Evidence References` input and source reference output | Covered |
| Required limitations | `Required Limitations` output and limitation visibility rule | Covered |
| No new evidence | Validation rule | Covered |
| No reinterpretation | Validation rule | Covered |
| No priority rewrite | Validation rule | Covered |
| Format containment | Validation rule | Covered |

### Gaps Against New Capability

| Gap ID | Gap | Evidence | Impact |
|---|---|---|---|
| PRS-GAP-001 | The contract still frames the destination as a generic `Output Artifact`. | SPEC-010 introduces selected presentation projections: Analytical or Executive. | The contract can authorize content, but does not yet distinguish projection type. |
| PRS-GAP-002 | The contract does not require `Presentation Mode` or `Selected Presentation Projection`. | SPEC-010 outputs include Presentation Mode and Selected Presentation Projection. | Presentation Layer could remain compliant on content while still lacking explicit projection-selection traceability. |
| PRS-GAP-003 | The contract does not state that analytical and executive projections are sibling representations of the same canonical content. | VCA-AUC-001-ARCH-002 and SPEC-010 BR-003 require no sequential derivation between projections. | A future artifact could incorrectly derive Executive Report from analytical projection. |
| PRS-GAP-004 | `presentation_constraints` currently covers format/audience generally, but does not block projection ambiguity. | SPEC-010 BR-002 requires blocking or clarification when projection cannot be determined. | Ambiguous projection requests may be handled as formatting concerns instead of readiness blockers. |

### Decision For Presentation Contract

`VCA-PRS-001` remains boundary-compliant and sufficient for preventing new evidence, reinterpretation and priority changes. However, **changes are justified** if SPEC-010 becomes active for projection selection.

Recommended future change scope:

- replace or qualify generic `Output Artifact` language with `Selected Presentation Projection` where applicable;
- add `Presentation Mode` / projection selection as a critical field for projection-aware instances;
- state that Analytical Projection and Executive Report consume the same approved canonical content and must not be derived sequentially from each other;
- add a validation rule requiring block or clarification when projection selection is ambiguous;
- preserve existing no-new-evidence, no-reinterpretation, no-priority-rewrite and limitation-visibility rules.

No immediate edit is performed in T-040.

---

## Cross-Contract Findings

| Finding ID | Finding | Severity | Treatment |
|---|---|---|---|
| FND-040-001 | Both contracts remain valid under SPEC-001, SPEC-002 and SPEC-004. | Low | No emergency correction needed. |
| FND-040-002 | The new capability introduces a real alignment need, mostly around explicit canonicalization and projection selection fields. | Medium | Changes are justified but should be implemented only after T-043 or the corresponding documentary decision task. |
| FND-040-003 | The Presentation Contract already protects against content drift; it needs projection traceability more than content-boundary repair. | Medium | Future changes should be narrow and additive. |
| FND-040-004 | The Context Contract is the stronger location for preventing scope leakage before projection selection. | Medium | Future changes should avoid pushing canonicalization responsibility into Presentation Layer. |

---

## Decision Summary

| Contract | Current Status | T-040 Decision | Rationale |
|---|---|---|---|
| `VCA-CTX-001` Context Contract | Valid but incomplete for SPEC-010 capability | Changes justified | Needs explicit Execution Scope Canonicalization and projection determinability support. |
| `VCA-PRS-001` Presentation Contract | Boundary-compliant but projection-generic | Changes justified | Needs selected projection fields and sibling-projection rules while preserving current content controls. |

Overall decision: **PASS WITH JUSTIFIED FOLLOW-UP CHANGES**.

The evaluated contracts do not require emergency correction to remain valid, but both have real, documentable alignment gaps relative to SPEC-010 and the two architectural decisions.

---

## Non-Changes Confirmed

T-040 does not require and does not perform:

- direct edits to `docs/contracts/context.contract.md`;
- direct edits to `docs/contracts/presentation.contract.md`;
- changes to AUC-001 Presentation Contract;
- changes to AUC-001 Executive Report;
- changes to SPEC-010;
- implementation of a runtime selector;
- creation of analytical or executive output artifacts.

---

## Recommended Next Step

Proceed to T-041 using this assessment as input.

T-041 should evaluate whether the AUC-001 presentation handoffs already preserve the current terminology and scope:

- `docs/handoffs/auc-001-presentation-contract.md`;
- `docs/handoffs/auc-001-executive-report.md`.

T-043 should later consolidate whether the justified changes identified here should be implemented, deferred, or rejected.

---

## Traceability

- `docs/tasks.md` / T-040
- `docs/contracts/context.contract.md`
- `docs/contracts/presentation.contract.md`
- `docs/contracts.md`
- `specs/spec-001-analytical-lifecycle.md`
- `specs/spec-002-component-boundaries.md`
- `specs/spec-004-transversal-contracts.md`
- `specs/spec-010-presentation-projection-selection.md`
- `docs/decisions/auc-001/auc-001-execution-scope-canonicalization-architectural-decision.md`
- `docs/decisions/auc-001/auc-001-presentation-projection-architectural-decision.md`
- `docs/context_refs.md`

---

## Completion Statement

T-040 is complete.

The base Context and Presentation Contracts were assessed against SPEC-010, VCA-AUC-001-ARCH-001 and VCA-AUC-001-ARCH-002.

The assessment concludes that both contracts remain valid but require justified follow-up alignment if the new projection-selection capability is incorporated into the active documentary model.
