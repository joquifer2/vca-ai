# AUC-001 Documentary Alignment Decision

## Metadata

| Field | Value |
|---|---|
| Decision ID | VCA-AUC-001-DOC-043 |
| Decision Name | Documentary Alignment Decision |
| Decision Type | Review / Governance |
| Backing Task | T-043 |
| Status | Completed |
| Decision | PROCEED WITH JUSTIFIED DOCUMENTARY ALIGNMENT |
| Decision Date | 2026-07-13 |
| Owner | Reviewer Agent |
| Scope | Consolidation of T-040, T-041 and T-042 to decide which artifacts remain unchanged and which require documentary alignment |

---

## Purpose

Consolidate the completed alignment assessments for the SPEC-010 presentation projection capability and decide, with traceability, which repository artifacts remain unchanged and which require justified documentary changes.

This decision is not an implementation task.

This decision does not edit contracts, handoffs, specifications or context references.

Any later documentary changes remain subject to the downstream tasks explicitly assigned to those artifacts.

---

## Inputs Consolidated

| Input | Status | Role In Decision |
|---|---|---|
| `docs/evaluations/auc-001-base-contracts-alignment-assessment.md` | Completed | Determines impact on base Context and Presentation Contracts. |
| `docs/evaluations/auc-001-presentation-alignment-assessment.md` | Completed | Determines impact on AUC-001 Presentation Contract and Executive Report. |
| `docs/evaluations/auc-001-context-traceability-alignment-assessment.md` | Completed | Determines impact on `docs/context_refs.md` and official traceability. |
| `specs/spec-010-presentation-projection-selection.md` | Draft | Defines the minimum active capability under review. |
| `docs/evaluations/auc-001-presentation-projection-architectural-decision.md` | Documented | Defines sibling presentation projections and non-derivation. |
| `docs/evaluations/auc-001-execution-scope-canonicalization-architectural-decision.md` | Documented | Defines canonicalized Execution Context dependency. |
| `docs/tasks.md` | Active backlog | Provides T-043 acceptance criteria and downstream task structure. |

---

## Decision Criteria

| Criterion | Meaning |
|---|---|
| Evidence-based change | A change is authorized only if a completed assessment identified a real gap. |
| No emergency correction | Valid existing artifacts should not be rewritten as if defective. |
| Narrow alignment | Authorized changes must target terminology, fields, constraints or traceability needed by SPEC-010. |
| Boundary preservation | No change may introduce new evidence, reasoning, recommendations or priorities. |
| No architecture reopening | T-043 must not redesign SPEC-010, ARCH-001 or ARCH-002. |
| Task separation | This decision authorizes scope; T-044/T-045/T-046 perform any later edits. |

---

## Consolidated Findings

| Finding ID | Finding | Source | Decision Impact |
|---|---|---|---|
| DOC-043-FND-001 | Base contracts remain valid under SPEC-001, SPEC-002 and SPEC-004. | T-040 | No emergency correction. |
| DOC-043-FND-002 | Context Contract lacks explicit Execution Scope Canonicalization and projection determinability support. | T-040 | Authorize narrow Context Contract alignment. |
| DOC-043-FND-003 | Presentation Contract is boundary-compliant but projection-generic. | T-040 | Authorize narrow Presentation Contract alignment. |
| DOC-043-FND-004 | AUC-001 Presentation Contract and Executive Report remain valid for completed AUC-001 output. | T-041 | Preserve existing approved content. |
| DOC-043-FND-005 | AUC-001 handoffs do not yet expose selected projection, sibling-projection and non-derivation terminology. | T-041 | Authorize AUC-001 artifact alignment. |
| DOC-043-FND-006 | `docs/context_refs.md` already exposes SPEC-010 and ARCH-002 but not with sufficient runtime traceability. | T-042 | Authorize context traceability refinement. |
| DOC-043-FND-007 | ARCH-001 is a necessary dependency for projection selection but is not sufficiently visible in context references. | T-042 | Authorize ARCH-001 traceability refinement. |
| DOC-043-FND-008 | No assessment supports adding analytical submodes, new output artifacts, runtime selector implementation or Foundation changes. | T-040, T-041, T-042, SPEC-010 | Explicitly reject those changes in this alignment cycle. |

---

## Artifact Decisions

| Artifact | Decision | Authorized Treatment | Rationale |
|---|---|---|---|
| `docs/contracts/context.contract.md` | Changes justified | Align through T-044. | Needs explicit support for Execution Scope Canonicalization, execution/methodological parameter distinction and projection determinability. |
| `docs/contracts/presentation.contract.md` | Changes justified | Align through T-044. | Needs selected projection / Presentation Mode terminology and sibling-projection constraints while preserving current content boundaries. |
| `docs/handoffs/auc-001-presentation-contract.md` | Changes justified | Align through T-045 after T-044. | Valid AUC handoff, but selected executive projection and non-derivation are implicit rather than explicit. |
| `docs/handoffs/auc-001-executive-report.md` | Changes justified | Align through T-045 after T-044. | Valid executive output, but metadata and traceability should identify it as the selected executive projection. |
| `docs/context_refs.md` | Changes justified | Align through T-046 after T-045. | Needs runtime-source visibility for SPEC-010 / ARCH decisions, qualified handoff references and metadata refresh. |
| `specs/spec-010-presentation-projection-selection.md` | No change in this cycle | Keep unchanged. | T-040/T-041/T-042 assessed artifacts against SPEC-010; no assessed gap requires changing the spec. |
| `docs/evaluations/auc-001-presentation-projection-architectural-decision.md` | No change in this cycle | Keep unchanged. | ARCH-002 remains the accepted decision source. |
| `docs/evaluations/auc-001-execution-scope-canonicalization-architectural-decision.md` | No change in this cycle | Keep unchanged. | ARCH-001 remains the accepted canonicalization decision source. |
| Evidence, Knowledge and Recommendation artifacts for AUC-001 | No change in this cycle | Keep unchanged. | Projection alignment must not reopen approved evidence, reasoning or recommendations. |
| Data, Discovery and Analytical artifacts for AUC-001 | No change in this cycle | Keep unchanged. | No evaluated gap affects upstream acquisition, discovery or analytical model artifacts. |
| AIF Foundation artifacts | No change in this cycle | Keep unchanged. | SPEC-010 explicitly does not modify AIF Foundation. |

---

## Authorized Change Scope

### T-044 Authorized Scope

T-044 may update base contracts only to the extent needed to reflect the approved capability:

- add explicit Context Contract support for Execution Scope Canonicalization;
- distinguish execution parameters from methodological parameters where useful for context readiness;
- expose `Output Request` / projection determinability as context-level validation when presentation selection is in scope;
- add selected projection / Presentation Mode terminology to the Presentation Contract;
- add non-derivation and sibling-projection constraints;
- preserve existing no-evidence, no-reinterpretation and no-priority-rewrite controls.

### T-045 Authorized Scope

T-045 may update AUC-001 presentation artifacts only to the extent needed to reflect the selected executive projection:

- identify the current AUC-001 output as an Executive Report / executive projection;
- add traceability to SPEC-010 and ARCH-002 where appropriate;
- state that the Executive Report is projected from the same approved Evidence, Knowledge and Recommendation Sets;
- state that it is not derived from an analytical projection;
- preserve the existing executive content, evidence references, recommendations, priorities, limitations and UNKNOWN.

### T-046 Authorized Scope

T-046 may update `docs/context_refs.md` only to strengthen official traceability:

- expose SPEC-010 as a discrete runtime source if the capability is active;
- expose ARCH-002 as a discrete runtime or decision source;
- make ARCH-001 visible as a related dependency for projection selection;
- qualify references to AUC-001 handoffs if needed so they are not mistaken for fully aligned sources before T-045;
- add the T-040/T-041/T-042/T-043 chain if accepted as official alignment evidence;
- refresh traceability metadata when editing the context index.

---

## Explicitly Rejected Or Deferred Changes

| Item | Decision | Reason |
|---|---|---|
| Creating an analytical projection artifact now | Rejected for this cycle | No task or evidence requires materializing a new analytical output. |
| Creating a new executive report | Rejected for this cycle | The existing Executive Report remains valid; only metadata/traceability alignment is justified. |
| Rewriting AUC-001 evidence, knowledge or recommendations | Rejected | SPEC-010 forbids new evidence, reasoning, recommendations or priority changes. |
| Adding analytical submodes | Rejected | SPEC-010 explicitly keeps analytical submodes out of current scope. |
| Implementing runtime projection selection | Rejected | The current scope is documentary alignment, not executable implementation. |
| Modifying AIF Foundation | Rejected | SPEC-010 is a vca-ai experimental capability and does not modify Foundation. |
| Changing SPEC-010 | Deferred | No completed assessment demonstrates a need to revise the specification. |
| Changing ARCH-001 or ARCH-002 | Deferred | Both decisions remain valid sources for this alignment cycle. |

---

## Sequencing Decision

The authorized sequence is:

1. T-044: align base contracts.
2. T-045: align AUC-001 presentation artifacts using the updated contract language where applicable.
3. T-046: align context references after artifact-level terminology is stable.
4. T-047: perform final readiness evaluation after T-044, T-045 and T-046 are complete.

This sequencing preserves dependency order and avoids making the context index claim alignment before the underlying artifacts have been updated.

---

## Decision Summary

T-043 accepts the three prior assessments as sufficient evidence for a controlled documentary alignment cycle.

The repository does not require emergency correction, but the evaluated artifacts should not remain permanently unchanged if SPEC-010 is treated as an active project capability.

Decision: **PROCEED WITH JUSTIFIED DOCUMENTARY ALIGNMENT**.

The downstream alignment should be narrow, additive and traceability-focused.

---

## Non-Changes Confirmed

T-043 does not perform:

- edits to `docs/contracts/context.contract.md`;
- edits to `docs/contracts/presentation.contract.md`;
- edits to `docs/handoffs/auc-001-presentation-contract.md`;
- edits to `docs/handoffs/auc-001-executive-report.md`;
- edits to `docs/context_refs.md`;
- edits to SPEC-010;
- implementation of runtime behavior;
- creation of new analytical or executive outputs.

---

## Traceability

- `docs/tasks.md` / T-043
- `docs/evaluations/auc-001-base-contracts-alignment-assessment.md`
- `docs/evaluations/auc-001-presentation-alignment-assessment.md`
- `docs/evaluations/auc-001-context-traceability-alignment-assessment.md`
- `specs/spec-010-presentation-projection-selection.md`
- `docs/evaluations/auc-001-presentation-projection-architectural-decision.md`
- `docs/evaluations/auc-001-execution-scope-canonicalization-architectural-decision.md`

---

## Completion Statement

T-043 is complete.

The documentary alignment decision classifies the reviewed artifacts as either unchanged for this cycle or requiring justified downstream alignment.

The next authorized task is T-044, limited to base contract alignment.