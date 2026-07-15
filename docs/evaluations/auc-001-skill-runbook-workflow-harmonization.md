# AUC-001 Skill Runbook Workflow Harmonization

## Purpose

Document the harmonization between `.github/skills/meta-lead-quality-analysis/SKILL.md` and `.github/skills/meta-lead-quality-analysis/RUNBOOK.md` after detecting duplicated and contradictory workflow definitions.

## Problems Corrected

- `SKILL.md` contained two incompatible execution orders: startup instructions loaded context before canonicalization, while its workflow list canonicalized before context loading.
- `SKILL.md` exposed a 6-phase workflow while `RUNBOOK.md` exposed an 8-phase workflow.
- Data Provider Validation and Canonical Content Validation were not explicit phases in `SKILL.md`.
- Evidence Acquisition and Evidence Set Construction were blended.
- Context Definition was called stable before provider-dependent fields, such as the real start date, could be resolved.
- `RUNBOOK.md` ended at handoff to Presentation Layer and did not fully define Presentation Materialization or Final Checklist.
- Invariants were duplicated across both documents, increasing drift risk.

## Decisions Taken

- `SKILL.md` now acts as activation, orchestration, modes, global invariants, blocking rules, high-level Definition of Done and references.
- `RUNBOOK.md` is the single canonical operational procedure.
- `SKILL.md` no longer contains a second numbered operational workflow.
- `RUNBOOK.md` now separates Provisional Context Definition from Stabilized Context Definition.
- Official Context Loading now precedes final Execution Context Canonicalization.
- Data Provider Validation, Context Definition Stabilization, Evidence Acquisition, Evidence Set Construction, Canonical Content Validation, Presentation Materialization and Final Checklist are explicit phases.
- The previously added BigQuery MCP SQL safety conventions were preserved in the Data Provider Validation phase.

## Files Modified

- `.github/skills/meta-lead-quality-analysis/SKILL.md`
- `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`

## Before / After Workflow

Before:

```text
SKILL.md:
Execution Context Canonicalization
-> Context Loading
-> Evidence Acquisition
-> Knowledge Generation
-> Recommendation Generation
-> Presentation

RUNBOOK.md:
Resolver Execution Context
-> Cargar contexto oficial
-> Validar Data Provider
-> Adquirir Evidence Set
-> Construir Knowledge Set
-> Construir Recommendation Set
-> Validar contenido canonico
-> Entregar a Presentation Layer
```

After:

```text
RUNBOOK.md:
1. Skill Activation and Execution Mode Resolution.
2. Preliminary Request Resolution.
3. Official Context Loading.
4. Execution Context Canonicalization.
5. Data Provider Validation.
6. Context Definition Stabilization.
7. Evidence Acquisition.
8. Evidence Set Construction and Stabilization.
9. Knowledge Generation and Stabilization.
10. Recommendation Generation and Stabilization.
11. Canonical Content Validation Gate.
12. Presentation Materialization.
13. Final Checklist and Delivery.
```

`SKILL.md` now contains only a conceptual chain:

```text
Context -> Evidence -> Knowledge -> Recommendations -> Presentation
```

## Precedence Rules

The harmonized rule is:

```text
Contracts prevail over SKILL.md, RUNBOOK.md, CHECKLIST.md and profiles.
SKILL.md defines activation, scope, modes and invariants.
RUNBOOK.md defines the operational order.
CHECKLIST.md validates delivery.
Profiles specialize concrete phases.
```

## Validations Performed

- Reviewed both updated documents completely.
- Confirmed `SKILL.md` has no numbered operational workflow.
- Confirmed the single numbered operational workflow is in `RUNBOOK.md`.
- Confirmed Context Loading precedes final Execution Context Canonicalization.
- Confirmed Data Provider Validation is explicit.
- Confirmed Canonical Content Validation Gate is explicit.
- Confirmed Evidence Acquisition is separated from Evidence Set Construction and Stabilization.
- Confirmed Presentation Materialization includes Projection, Communication Context, Representation Constraints, Presentation Policy, no-data-access, no-new-evidence, no-new-knowledge and no-new-recommendations rules.
- Confirmed Final Checklist and Delivery includes `CHECKLIST.md`, source declaration, MCP-only confirmation when applicable, consumed artifacts, projection, policy, historical isolation, traceability, limitations and UNKNOWNs.
- Confirmed no Specifications, contracts, AIF Foundation files, BigQuery MCP Server files, workspace, allowlist, FARO definitions or profiles were modified.
- No repository-level documentation lint configuration was found (`package.json`, `pyproject.toml`, `.markdownlint*`, `Makefile`, `justfile` were absent for this purpose); validation was performed through deterministic textual checks.

## Residual Risks

- `CHECKLIST.md` still contains its existing detailed checks and was not harmonized in this change beyond previous SQL-safety additions.
- Some historical evaluation or handoff artifacts may still describe older workflow forms. They remain historical records and were not modified.
- The Runbook is now more explicit; future edits should avoid reintroducing workflow steps into `SKILL.md`.

## Result

```yaml
status: pass
single_operational_source: RUNBOOK.md
skill_role: activation_orchestration_invariants
runbook_role: operational_procedure
framework_change: false
spec_change: false
ready_for_natural_language_test: true
```