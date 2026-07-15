# Knowledge Construction Profile Design

## 1. Problem Statement

AUC-001 has a persistent gap between methodological correctness and analytical depth. The current lifecycle and contracts preserve traceability and boundary discipline, but they do not explicitly guide how reasoning should be shaped during Knowledge Generation.

The architectural question is whether this gap should be addressed by extending an existing artifact or by introducing a new experimental artifact dedicated to knowledge construction posture.

This document decides that question without changing Foundation, Specifications, Contracts, or the lifecycle.

## 2. Alternatives Considered

### A. Expand the Analytical Use Case

Add reasoning guidance directly to `analytical_use_cases/meta_lead_quality_analysis.md`.

### B. Expand the Skill

Embed the reasoning guidance in `.github/skills/meta-lead-quality-analysis/SKILL.md`.

### C. Expand the Runbook

Add the reasoning guidance to `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`.

### D. Create a new artifact: Knowledge Construction Profile

Create an experimental companion artifact that defines the knowledge construction posture for AUC-001 without changing canonical Foundation artifacts.

### E. Other alternative: use an existing evaluation or experiment note

Reuse a general evaluation file or make the guidance implicit inside an experiment report.

## 3. Architectural Decision

The best architectural option is **D. Create a new artifact: Knowledge Construction Profile**.

This artifact should be an **experimental methodological profile**: a standalone companion document that shapes knowledge construction in AUC-001 while remaining outside the canonical Foundation surface.

It is not a new capability, not a new contract, not a new lifecycle phase, and not a replacement for the Skill or the Runbook.

## 4. Why this artifact and not another?

### Why not expand the Analytical Use Case?

The AUC defines the domain, objective, and expected analytical outcome. It is the right place for scope and problem framing, but it is the wrong place to host experimental knowledge construction guidance.

If the AUC absorbs the profile, domain definition and knowledge construction posture become coupled. That weakens maintainability and makes the AUC less reusable as a stable case-definition artifact.

### Why not expand the Skill?

The Skill is already the operational extension point for AUC-001. Putting the experiment there would contaminate the canonical execution surface with provisional knowledge construction guidance.

That would make the experimental profile look like authoritative workflow behavior rather than an AUC-local test artifact.

### Why not expand the Runbook?

The Runbook is the closest operational layer to Knowledge Generation, but it is still a canonical procedural artifact. Extending it would mix stable execution instructions with provisional knowledge construction guidance.

That would reduce clarity about what is foundational, what is experimental, and what is only relevant to the current investigation.

### Why not reuse an evaluation document?

Evaluations are the right place to record findings about the experiment, not to host the experimental control object itself.

If the guidance lives only inside a report, it becomes descriptive rather than reusable for repeated experimental runs.

### Why this artifact wins

The new artifact is the only option that isolates the experiment while staying below Foundation.

It gives AUC-001 a dedicated knowledge construction overlay without forcing domain, execution, and experimental control into the same document.

## 5. Purpose

The Knowledge Construction Profile is a controlled experimental artifact for AUC-001.

Its purpose is to define the knowledge construction posture used during Knowledge Generation so that the experiment can test whether explicit guidance improves depth without changing the lifecycle or Foundation.

## 6. Scope

The profile applies only to AUC-001 and only to the experimental knowledge construction layer used during Knowledge Generation.

It is limited to:

- knowledge construction posture;
- interpretive framing;
- experimental control boundaries;
- quality expectations for reasoning behavior;
- traceability expectations between evidence and knowledge.

## 7. Out of Scope

The profile does not:

- redefine the lifecycle;
- change contracts;
- alter Foundation responsibilities;
- replace the Skill;
- replace the Runbook;
- define new analytical operations;
- define new rules of reasoning content;
- define new capabilities;
- generalize to other AUCs;
- become a canonical project artifact.

## 8. Responsibilities

The Knowledge Construction Profile is responsible for:

- providing an experimental knowledge construction frame for AUC-001;
- expressing how Knowledge Generation should be guided at a structural level;
- separating the experimental knowledge construction posture from canonical workflow artifacts;
- enabling controlled comparison between baseline reasoning and reasoning under profile guidance;
- preserving the distinction between method experiment and domain specification.

## 9. Non-responsibilities

The Knowledge Construction Profile is not responsible for:

- producing evidence;
- producing recommendations;
- changing the execution workflow;
- governing data acquisition;
- replacing the Skill or Runbook;
- becoming a contract;
- becoming a Specification;
- establishing Foundation-wide rules;
- defining final content for Knowledge Generation.

## 10. Position in the Architecture

The artifact should live as an **experimental companion document** under the AUC-001 experiment area:

`docs/experiments/auc-001-knowledge-construction-profile-design.md`

Architecturally, it sits between stable case definition and experimental knowledge construction guidance.

It is not part of the canonical Foundation core. It is an AUC-local overlay for controlled experimentation.

## 11. Position in the Lifecycle

The artifact does not change the lifecycle.

It is consumed inside the existing Razonamiento / Knowledge Generation context as an experimental guidance layer, but it does not become a lifecycle phase, a handoff, or a contract.

Its role is to influence how reasoning is shaped during the existing phase, not to redefine the phase itself.

## 12. Relationship with AUC

The AUC remains the source of domain framing and analytical intent.

The Knowledge Construction Profile complements the AUC by adding an experimental knowledge construction lens.

Relationship summary:

- AUC defines what is being analyzed;
- the profile defines how knowledge is experimentally constructed for that analysis.

## 13. Relationship with Skill

The Skill remains the operational extension point for AUC-001.

The profile should not replace it. It should be referenced by it, or by the experimental execution context around it, only when the experiment is active.

Relationship summary:

- Skill remains canonical execution behavior;
- the profile is a controlled experimental overlay.

## 14. Relationship with Runbook

The Runbook remains the authoritative procedural document for the current workflow.

The profile should not absorb procedural steps. Instead, it should provide the knowledge construction posture that the Runbook can invoke during the reasoning portion of the workflow.

Relationship summary:

- Runbook says what the workflow does;
- the profile frames how knowledge is experimentally shaped during the workflow.

## 15. Relationship with Contracts

The profile must remain subordinate to existing contracts.

It cannot redefine Evidence, Knowledge, or Recommendation. It can only operate within their boundaries.

Relationship summary:

- Contracts define invariants;
- the profile defines experimental knowledge construction posture inside those invariants.

## 16. Proposed Structure

The artifact should be structured as a lightweight experimental design document, not as a content repository.

Proposed sections:

1. Purpose
2. Experimental framing
3. Knowledge construction boundary
4. Allowed use in AUC-001
5. Disallowed use
6. Interaction model with existing artifacts
7. Experimental status
8. Validation expectations
9. Exit criteria for Foundation consideration

This structure is intentionally high level. It defines the container for future knowledge construction guidance without writing that guidance yet.

## 17. Experimental Status

The artifact is experimental and AUC-001-specific.

It must be treated as provisional until a controlled run demonstrates that it improves reasoning depth without contaminating the canonical workflow.

It should remain outside Foundation until there is cross-case evidence that the same knowledge construction posture works beyond Meta Lead Quality Analysis.

## 18. Risks

- It may duplicate concepts already present in the Skill or Runbook.
- It may be mistaken for a new capability if not clearly labeled experimental.
- It may drift into pseudo-specification if content grows beyond knowledge construction posture.
- It may become hard to maintain if it starts accumulating domain-specific operations.
- It may encourage premature generalization if reused outside AUC-001 too early.

## 19. Evidence Required Before Foundation

Before considering Foundation reuse, the experiment would need evidence that:

- the profile improves analytical depth consistently;
- the same knowledge construction posture works across at least one non-marketing case;
- the profile can be separated from AUC-specific semantics;
- the profile remains compatible with the current lifecycle and contracts;
- the profile adds value not already provided by Skill or Runbook.

## 20. Conclusion

The correct architectural decision is to create a new AUC-local experimental artifact: **Knowledge Construction Profile**.

It is the best container for controlled knowledge construction guidance because it isolates the experiment without changing Foundation, the lifecycle, the contracts, the Skill, or the Runbook.

In short:

- **AUC** defines the domain problem;
- **Skill** defines operational execution;
- **Runbook** defines procedural flow;
- **Contracts** define invariants;
- **Knowledge Construction Profile** defines an experimental knowledge construction posture for AUC-001.

## 21. Architectural Reassessment: Standalone Profile vs Experimental Runbook Section

### 1. Question under review

What does the system lose if the future content of the Knowledge Construction Profile is incorporated as an experimental section inside the Runbook instead of living in an independent document?

The reassessment compares a standalone profile against a Runbook-embedded experimental section and checks whether the extra document is still architecturally justified.

### 2. Options compared

#### Option A - Standalone profile

Keep `docs/experiments/auc-001-knowledge-construction-profile-design.md` as an independent experimental artifact referenced by the Skill or Runbook only when the experiment is active.

#### Option B - Experimental Runbook section

Embed the guidance as a clearly delimited experimental section inside `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`.

#### Option C - Other alternative

No better alternative emerged that improves separation while reducing complexity. A hybrid “section plus extra control file” reintroduces the same split by another name.

### 3. Evaluation criteria

The comparison was judged on:

- cohesion;
- coupling;
- cognitive cost;
- maintainability;
- control experimental;
- future reuse;
- reversibility;
- SDD alignment;
- separation between stable and experimental;
- necessity of the extra artifact.

### 4. Concrete losses if the standalone artifact is removed

If the profile content moves into the Runbook, the system loses these observable properties:

- Independent versioning of the experimental knowledge construction posture disappears. Any change to the profile becomes a change to the canonical procedural file.
- Baseline and variant become harder to distinguish in reviews because the same document now contains both stable workflow and experimental guidance.
- A non-experimental AUC-001 run must inspect a canonical file for gating logic instead of simply ignoring an unreferenced experimental file. This increases the chance of accidental use.
- Retiring or resetting the experiment requires editing a canonical artifact, which makes the removal path noisier and more review-heavy.
- Evaluations lose a single, dedicated reference for the profile and must point to a moving section inside a canonical workflow document.
- The profile becomes harder to treat as a reusable experimental object if later comparisons need to isolate it from procedural workflow edits.

These are concrete losses because they directly affect what an operator sees, what a reviewer diffs, and what a baseline execution reads by default.

### 5. Concrete risks of modifying the Runbook

Modifying the Runbook introduces these observable risks:

- The Runbook is the normal execution path after Skill activation, so experimental text is now closer to default behavior.
- If activation and deactivation conditions are omitted or misread, the experimental guidance can apply to baseline runs by accident.
- Any future maintenance of the Runbook can change the experiment implicitly, because the experiment and the workflow share the same file history.
- Reviewers may treat the experimental section as operational guidance rather than provisional knowledge construction posture because it sits inside the canonical workflow document.
- To avoid contamination, the Runbook would need explicit gating metadata, which adds another control mechanism that itself must be maintained and audited.

### 6. Reversibility analysis

The standalone profile is more reversible.

With a separate file, the experiment can be introduced, tested, referenced, replaced, or removed without editing the canonical workflow artifact. Reversibility is visible and local: delete or update the profile file, then remove the reference.

With a Runbook section, reversibility is weaker because the baseline file must change twice: once to add the experiment and again to remove it. That means the canonical document carries the experiment through its own history, and baseline stability depends on remembering to keep the section gated and inert.

The practical consequence is that the standalone profile preserves a cleaner baseline audit trail.

### 7. Final decision

**A. Maintain the Knowledge Construction Profile as a standalone artifact.**

This is the better architectural choice because the Runbook is the canonical procedural entrypoint, while the profile is a provisional experimental object. Keeping them separate preserves a stable baseline, makes accidental activation less likely, and keeps experiment history inspectable on its own.

### 8. Required next step

Keep the standalone profile document and reference it only when the experiment is explicitly activated.

Do not move the profile into the Runbook unless future evidence shows that the separate file adds no measurable benefit in baseline isolation, reviewability, or reversibility.

If experimentation proceeds, the next step is to populate the standalone profile content while leaving the Runbook unchanged.