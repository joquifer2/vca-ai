# AUC-001 CCD/FARO Strategic Context Constraints Task Plan

## Metadata

| Field | Value |
| --- | --- |
| Artifact ID | TASK-PLAN-AUC-001-CCD-FARO-STRATEGIC-CONTEXT-CONSTRAINTS |
| Use Case | AUC-001 - Meta Lead Quality Analysis |
| Classification | Local controlled post-acceptance evolution |
| Agent | Tasks Planner Agent |
| Created | 2026-07-23 |
| Source decision | Architect Agent memo and Reviewer Agent PASS in conversation, 2026-07-23 |
| Canonical business source | `knowledge/client/ccd.md` |
| Specification policy | No new Specification required |
| Reopened specifications | None |
| Historical outputs | Protected; no mutation authorized |
| BigQuery | Not required for this plan |
| Implementation | Not executed by this plan |
| Status | Ready for controlled Entry Gate review |

---

## 1. Objective

Plan the minimum local correction required so AUC-001 applies the strategic business context from `knowledge/client/ccd.md` as verifiable analytical constraints when interpreting `campaign_signal`.

The correction must ensure that FARO layers are interpreted according to their own objectives, KPIs and decision criteria:

- `ATTENTION` is not evaluated by direct leads, CPL or qualified CPL.
- `ACTIVATION` is interpreted as retargeting / prior-interest activation, separating direct cost from complete or assisted cost.
- `COMMERCIAL` is interpreted as direct acquisition and cost-quality analysis only within the authorized commercial universe.
- FARO layers are not compared by a universal KPI.
- Evidence, Knowledge, Recommendations, CPS and Presentation preserve traceability to the CCD when interpreting `campaign_signal`.
- QA can detect violations of the strategic context.

---

## 2. Source Artifacts

| Type | Artifact | Role |
| --- | --- | --- |
| Canonical business context | `knowledge/client/ccd.md` | Normative source for FARO layer semantics. |
| Skill | `.github/skills/meta-lead-quality-analysis/SKILL.md` | Activation and AUC-001 invariants. |
| Runbook | `.github/skills/meta-lead-quality-analysis/RUNBOOK.md` | Operational phase order. |
| References | `.github/skills/meta-lead-quality-analysis/references.md` | Official dependency registry. |
| Context refs | `docs/context_refs.md` | Official context entrypoint. |
| Evidence contract | `docs/contracts/evidence.contract.md` | Evidence structure and interpretation boundary. |
| Knowledge contract | `docs/contracts/knowledge.contract.md` | Knowledge derivation constraints. |
| Recommendation contract | `docs/contracts/recommendation.contract.md` | Recommendation traceability constraints. |
| Presentation contract | `docs/contracts/presentation.contract.md` | Presentation boundary. |
| Runtime | `tools/auc_001_canonical_cost_quality_model.py` | Structured cost-quality and signal reconciliation. |
| Product validator | `tools/auc_001_analytical_product_contract.py` | CPS, common core and projection validation. |
| Package validator | `tools/auc_001_operational_acceptance_package.py` | Physical package acceptance validation. |
| Tests | `tests/evals/auc_001_*_tests.ps1` | Local regression and adversarial checks. |

---

## 3. Planning Decision

```text
LOCAL CONTROLLED EVOLUTION UNDER EXISTING AUC-001 CONTRACTS
```

Rationale:

- `knowledge/client/ccd.md` already contains the required business semantics.
- The incident is a propagation and validation gap, not a missing business definition.
- SPEC-014, SPEC-015 and SPEC-016 remain valid and do not need to be reopened.
- The correction can be implemented by making CCD-derived constraints explicit, structured and verifiable inside the current AUC-001 chain.
- Historical outputs and closed gates must remain preserved as historical evidence, not retrofitted.

Rejected options:

| Option | Decision | Reason |
| --- | --- | --- |
| Create a new Specification | Rejected | No new product scope, evidence source, artifact family or reusable Foundation capability is required. |
| Duplicate CCD rules in a new normative document | Rejected | `knowledge/client/ccd.md` remains the canonical source. The correction transports references and constraints derived from it. |
| Fix only report wording | Rejected | The issue would remain possible in Knowledge, Recommendations, CPS and validators. |
| Reopen SPEC-014/SPEC-015/SPEC-016 | Rejected | Existing specifications can host the local hardening without changing approved scope. |

---

## 4. Boundary

In scope:

- make `knowledge/client/ccd.md` an explicit mandatory business context source for AUC-001 execution;
- define a structured `strategic_context_constraints` block derived from CCD references;
- propagate this block through Context Definition, Evidence, Knowledge, Recommendations, Common Product Core, CPS and Presentation lineage;
- add semantic validation for FARO layer interpretation;
- add adversarial tests that do not depend only on literal blocked phrases;
- update Skill, Runbook, references, local contracts, runtime and validators as needed;
- preserve existing data provider restrictions and MCP-only policy for future evidence acquisition.

Out of scope:

- modifying `knowledge/client/ccd.md` as part of implementation unless Reviewer or QA later identifies a broken reference;
- copying CCD normative content into a parallel source of truth;
- changing BigQuery MCP Server, IAM, allowlist or data sources;
- acquiring new evidence;
- regenerating analytical or executive reports;
- modifying or backfilling closed outputs;
- reopening SPEC-014, SPEC-015, SPEC-016, P04 acceptance or IC-001 closure;
- creating a reusable Foundation-level context-governance capability.

---

## 5. Required Constraint Model

The implementation should introduce a structured block equivalent to:

```text
strategic_context_constraints
  source_artifact: knowledge/client/ccd.md
  source_refs:
    - campaign_signal official values
    - FARO interpretation principles
    - multicapa reading principles
  constraints:
    ATTENTION:
      required_interpretation: attention / useful interest
      forbidden_kpi_families: direct_leads, cpl, qualified_cpl, direct_commercial_efficiency
    ACTIVATION:
      required_interpretation: retargeting / prior-interest activation
      required_separation: direct_cost vs complete_or_assisted_cost
      forbidden_interpretations: mixed_with_cold_traffic, universal_cpl_efficiency
    COMMERCIAL:
      required_interpretation: direct acquisition
      allowed_cost_quality_universe: commercial_matched
      forbidden_primary_kpi_families: video_consumption, attention_only
    ALL:
      forbidden_comparison: universal_kpi_ranking_across_layers
      required_traceability: ccd_constraint_ref for campaign_signal interpretation
```

This block is a transport and validation mechanism. It is not a new normative source.

---

## 6. Task Register

| ID | Task | Type | Owner | Depends On | Expected Result | Completion Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| CCD-FARO-T001 | Prepare controlled Entry Gate handoff | Governance | Tasks Planner Agent | This plan | QA receives scope, constraints, boundary and blocking criteria | Handoff or gate request references this task plan |
| CCD-FARO-T002 | Evaluate Entry Gate for local correction | Validation | QA Gate Agent | CCD-FARO-T001 | QA decides whether implementation may start | Entry Gate PASS or explicit equivalent authorization |
| CCD-FARO-T003 | Make CCD activation explicit in AUC-001 references | Documentation / Governance | Implementation Agent | CCD-FARO-T002 PASS | `references.md` and related routing name `knowledge/client/ccd.md` as mandatory for AUC-001 business interpretation | Diff plus route validation |
| CCD-FARO-T004 | Update Skill and Runbook propagation points | Documentation / Governance | Implementation Agent | CCD-FARO-T002 PASS | Runbook phases 03, 04, 06, 08, 09, 10, 11, 12 and 13 preserve CCD-derived constraints | Diff plus reviewer check |
| CCD-FARO-T005 | Extend local contracts for strategic constraints | Contract / Governance | Implementation Agent | CCD-FARO-T003, CCD-FARO-T004 | Evidence, Knowledge, Recommendation and Presentation contracts require CCD traceability for `campaign_signal` interpretation | Contract diff and contract validation |
| CCD-FARO-T006 | Add `strategic_context_constraints` to runtime output model | Development | Implementation Agent | CCD-FARO-T005 | Runtime output exposes CCD-derived constraints and source refs without duplicating CCD as a new canon | Unit tests and schema fixture |
| CCD-FARO-T007 | Preserve constraints in Evidence Set construction | Development | Implementation Agent | CCD-FARO-T006 | Evidence carries constraints as context/lineage while remaining free of interpretation | Evidence fixture validation |
| CCD-FARO-T008 | Enforce constraints during Knowledge construction | Development / Analytical governance | Implementation Agent | CCD-FARO-T007 | Knowledge claims involving `campaign_signal` include `ccd_constraint_ref`, `signal_layer`, `kpi_family` and allowed interpretation | Product contract tests |
| CCD-FARO-T009 | Enforce constraints during Recommendation construction | Development / Governance | Implementation Agent | CCD-FARO-T008 | Recommendations do not use universal KPI rankings or forbidden layer interpretations | Recommendation fixture tests |
| CCD-FARO-T010 | Preserve constraints in Common Product Core and CPS | Development / Product contract | Implementation Agent | CCD-FARO-T008, CCD-FARO-T009 | CPS contains strategic constraints and lineage required by Presentation | CPS schema and validation tests |
| CCD-FARO-T011 | Adapt Presentation validation to consume structured constraints | Development / QA | Implementation Agent | CCD-FARO-T010 | Analytical and executive projections fail if they alter or omit material CCD-dependent interpretation | Projection validation tests |
| CCD-FARO-T012 | Add semantic validators for FARO layer rules | Development / QA | Implementation Agent | CCD-FARO-T010 | Validators check structured claims, KPI families, signal layers and CCD refs, not only literal phrases | Positive and negative fixtures |
| CCD-FARO-T013 | Add adversarial tests for `ATTENTION` | Tests | Implementation Agent | CCD-FARO-T012 | Tests fail when `ATTENTION` is evaluated by direct leads, CPL, qualified CPL or direct acquisition efficiency | Local test PASS after implementation |
| CCD-FARO-T014 | Add adversarial tests for `ACTIVATION` | Tests | Implementation Agent | CCD-FARO-T012 | Tests fail when `ACTIVATION` is not treated as retargeting or omits direct/full cost separation | Local test PASS after implementation |
| CCD-FARO-T015 | Add adversarial tests for `COMMERCIAL` | Tests | Implementation Agent | CCD-FARO-T012 | Tests fail when `COMMERCIAL` is interpreted primarily by attention/video-consumption KPIs | Local test PASS after implementation |
| CCD-FARO-T016 | Add adversarial tests for universal KPI ranking | Tests | Implementation Agent | CCD-FARO-T012 | Tests fail when layers are ranked together by a single cost-quality KPI | Local test PASS after implementation |
| CCD-FARO-T017 | Add package-level QA checks | Development / QA | Implementation Agent | CCD-FARO-T012 to CCD-FARO-T016 | Physical package validation detects missing strategic constraints and missing CCD lineage | Package validator tests |
| CCD-FARO-T018 | Run local validation suite | Validation | Implementation Agent | CCD-FARO-T003 to CCD-FARO-T017 | AUC-001 tests pass and new adversarial tests prove the incident is blocked | Test results recorded |
| CCD-FARO-T019 | Prepare Reviewer handoff | Handoff | Implementation Agent | CCD-FARO-T018 PASS | Reviewer receives changed artifacts, scope, tests, risks and no-reopen statement | Handoff artifact |
| CCD-FARO-T020 | Review local correction | Review | Reviewer Agent | CCD-FARO-T019 | Reviewer validates contract alignment and absence of CCD duplication | Reviewer decision |
| CCD-FARO-T021 | QA closure validation | Validation | QA Gate Agent | CCD-FARO-T020 PASS | QA validates semantic constraints, tests and no mutation of closed outputs | QA closure gate |
| CCD-FARO-T022 | Index final accepted correction | Documentation | Documentation Agent | CCD-FARO-T021 PASS | AUC-001 indexes and task backlog reflect accepted correction | Documentation diff after QA PASS |

---

## 7. Recommended Execution Order

1. Prepare and run Entry Gate: CCD-FARO-T001 to CCD-FARO-T002.
2. Harden official context activation and propagation: CCD-FARO-T003 to CCD-FARO-T005.
3. Implement structured transport through runtime and canonical artifacts: CCD-FARO-T006 to CCD-FARO-T010.
4. Implement semantic validators: CCD-FARO-T011 to CCD-FARO-T012.
5. Add adversarial tests for all required FARO rules: CCD-FARO-T013 to CCD-FARO-T017.
6. Run local validation and prepare handoff: CCD-FARO-T018 to CCD-FARO-T019.
7. Close with Reviewer and QA: CCD-FARO-T020 to CCD-FARO-T021.
8. Index only after QA PASS: CCD-FARO-T022.

---

## 8. Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC-CCD-FARO-001 | `knowledge/client/ccd.md` is explicitly required for AUC-001 business interpretation and remains the canonical source. |
| AC-CCD-FARO-002 | `strategic_context_constraints` exists as structured transport with CCD source refs. |
| AC-CCD-FARO-003 | Evidence carries CCD-derived constraints as context/lineage without generating interpretation. |
| AC-CCD-FARO-004 | Knowledge claims involving `campaign_signal` include traceability to the applicable CCD constraint. |
| AC-CCD-FARO-005 | Recommendations involving `campaign_signal` derive from Knowledge that already satisfies CCD constraints. |
| AC-CCD-FARO-006 | Common Product Core and CPS preserve the strategic constraints before Presentation. |
| AC-CCD-FARO-007 | Presentation consumes and preserves CCD-dependent interpretation without adding new strategic claims. |
| AC-CCD-FARO-008 | `ATTENTION` cannot be evaluated by direct leads, CPL, qualified CPL or direct commercial efficiency. |
| AC-CCD-FARO-009 | `ACTIVATION` must be interpreted as retargeting / prior-interest activation and must separate direct cost from complete or assisted cost when cost is discussed. |
| AC-CCD-FARO-010 | `COMMERCIAL` cost-quality analysis remains restricted to direct acquisition and the authorized commercial matched universe. |
| AC-CCD-FARO-011 | Cross-layer comparison by a universal KPI is blocked. |
| AC-CCD-FARO-012 | Validators operate on structured fields, typed claims, KPI families, signal layers and CCD refs; literal blocked phrases are only a supplemental guardrail. |
| AC-CCD-FARO-013 | SPEC-014, SPEC-015 and SPEC-016 are not reopened or semantically changed. |
| AC-CCD-FARO-014 | Closed outputs and accepted packages are not modified or regenerated by this correction. |

---

## 9. Required Tests

| Test ID | Test | Minimum Expected Result |
| --- | --- | --- |
| TST-CCD-FARO-001 | Missing `strategic_context_constraints` in CPS | Validation fails. |
| TST-CCD-FARO-002 | Missing CCD source reference for `campaign_signal` interpretation | Validation fails. |
| TST-CCD-FARO-003 | `ATTENTION` claim uses direct leads, CPL or qualified CPL as success metric | Validation fails. |
| TST-CCD-FARO-004 | `ACTIVATION` claim omits retargeting / prior-interest interpretation | Validation fails. |
| TST-CCD-FARO-005 | `ACTIVATION` cost claim does not separate direct and complete/assisted cost | Validation fails unless declared not applicable with reason. |
| TST-CCD-FARO-006 | `COMMERCIAL` claim uses attention/video consumption as primary KPI | Validation fails. |
| TST-CCD-FARO-007 | Cross-layer ranking uses one universal cost-quality KPI | Validation fails. |
| TST-CCD-FARO-008 | Projection drops or rewrites CCD-dependent interpretation from CPS | Validation fails. |
| TST-CCD-FARO-009 | Valid layer-specific interpretation with CCD refs | Validation passes. |
| TST-CCD-FARO-010 | Existing valid commercial matched cost-quality metric | Validation still passes. |
| TST-CCD-FARO-011 | Closed output namespace mutation check | Validation confirms protected outputs unchanged. |

---

## 10. Blocking Conditions

Implementation must stop if:

- Entry Gate is absent or not PASS / equivalent authorization;
- the correction requires changing CCD normative meaning;
- the correction duplicates CCD as a new canonical business document;
- the correction requires new evidence, BigQuery, MCP calls, IAM changes or source expansion;
- implementation attempts to reopen SPEC-014, SPEC-015, SPEC-016, P04 acceptance or IC-001;
- implementation attempts to modify historical or accepted output namespaces;
- validators cannot inspect structured claims and would rely only on literal text scanning;
- Knowledge, Recommendations or Presentation need to invent new business definitions not present in CCD.

---

## 11. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Duplicating CCD content into a parallel norm | Future drift between CCD and AUC-001 constraints | Store source refs and derived constraint IDs; keep CCD canonical. |
| Overfitting validators to Spanish phrases | False negatives when wording changes | Validate typed claims, KPI families, signal layers and refs. |
| Breaking valid SPEC-012 commercial metrics | Regression in cost-quality model | Preserve current `COMMERCIAL` matched metric rules and add positive tests. |
| Turning Evidence into interpretation | Lifecycle boundary violation | Evidence may carry constraints as context, but findings remain in Knowledge. |
| Reopening closed outputs | Governance breach | Add protected namespace checks and explicit no-regeneration boundary. |
| Treating `ACTIVATION` as full attribution without evidence | Overclaiming assisted impact | Require direct vs complete/assisted cost separation and UNKNOWN/not_available where evidence is absent. |

---

## 12. Definition of Done

This plan is complete when:

- the correction is classified as local controlled evolution;
- no new Specification is required;
- `knowledge/client/ccd.md` remains canonical;
- affected artifacts are identified;
- tasks, dependencies, acceptance criteria, tests and blockers are explicit;
- implementation is not started by this plan;
- BigQuery is not used by this plan;
- closed outputs remain protected;
- the next agent is identified.

---

## 13. Next Agent

Next required agent: **QA Gate Agent** for Entry Gate review.

Recommended instruction:

```text
Actua como QA Gate Agent de vca-ai. Evalua el Entry Gate para implementar la evolucion local AUC-001 CCD/FARO Strategic Context Constraints segun `tasks/auc-001-ccd-faro-strategic-context-constraints-task-plan.md`. No ejecutes BigQuery, no modifiques outputs cerrados, no reabras SPEC-014, SPEC-015 ni SPEC-016, y decide si Implementation Agent puede iniciar la correccion local controlada.
```

Readiness decision:

```text
READY FOR CONTROLLED ENTRY GATE REVIEW
```
