# Common Input Manifest

## Evaluation

- Evaluation category: Controlled Comparative Evaluation
- Freeze commit: `41a8c31acf16568bbfa66f094ea8b8fe326d4d27`
- Actual repository commit used: `41a8c31acf16568bbfa66f094ea8b8fe326d4d27`
- AUC: AUC-001 - Meta Lead Quality Analysis
- Period: 2026-06-01 to 2026-06-30

## Authorized Common Inputs

The following files form the common input package used by all three conditions:

1. `analytical_use_cases/meta_lead_quality_analysis.md`
2. `.github/skills/meta-lead-quality-analysis/SKILL.md`
3. `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`
4. `.github/skills/meta-lead-quality-analysis/CHECKLIST.md`
5. `docs/handoffs/auc-001-execution-context.md`
6. `docs/handoffs/auc-001-evidence-contract.md`
7. `docs/handoffs/auc-001-evidence-set.md`
8. `docs/handoffs/auc-001-knowledge-contract.md`
9. `docs/handoffs/auc-001-recommendation-contract.md`
10. `docs/handoffs/auc-001-presentation-contract.md`
11. `.github/presentation_policies/executive-decision-support.md`
12. `outputs/evaluations/auc-001-knowledge-construction-validation/common-input/common-instruction.md`

## Condition-Specific Reasoning Inputs

These files are not part of the common package and are only available to the named condition:

- Condition A: none.
- Condition B: `docs/experiments/knowledge-construction-profile-v0.1.md`.
- Condition C: `docs/experiments/knowledge-construction-profile-v0.2.md`.

## Excluded Inputs

The execution must not read, use or incorporate:

- `docs/evaluations/auc-001-analytical-scaffold-controlled-experiment.md`
- `docs/evaluations/auc-001-evidence-to-knowledge-independent-research.md`
- `docs/evaluations/auc-001-knowledge-construction-comparative-analysis.md`
- `docs/evaluations/auc-001-knowledge-methodology-investigation.md`
- `docs/evaluations/corpus/`
- `docs/evaluations/knowledge-construction-architectural-investigation.md`
- `docs/evaluations/knowledge-construction-profile-validation-execution-blocker.md`
- `docs/experiments/auc-001-knowledge-construction-profile-design.md`
- `docs/experiments/knowledge-construction-blueprint-conceptual-model.md`
- `docs/handoffs/auc-001-knowledge-set.md`
- `docs/handoffs/auc-001-recommendation-set.md`
- `docs/handoffs/auc-001-executive-report.md`

## Controls

- No BigQuery execution.
- No external sources.
- No new evidence.
- No reuse of outputs across conditions.
- No modification of canonical inputs.
- Outputs must be written only inside the assigned condition folder.
