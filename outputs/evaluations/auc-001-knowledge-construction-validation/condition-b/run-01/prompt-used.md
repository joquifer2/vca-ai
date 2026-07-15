# Prompt Used

You are executing one isolated run of AUC-001 output generation for a controlled comparative evaluation.

## Assigned Output Folder

Write outputs only inside:

`outputs/evaluations/auc-001-knowledge-construction-validation/condition-b/run-01/`

## Input Rules

Use only:

- `outputs/evaluations/auc-001-knowledge-construction-validation/common-input/input-manifest.md`
- `outputs/evaluations/auc-001-knowledge-construction-validation/common-input/common-instruction.md`
- the common input files listed in the manifest and common instruction.
- `docs/experiments/knowledge-construction-profile-v0.1.md`, only during Knowledge Generation.

Do not read:

- `docs/experiments/knowledge-construction-profile-v0.2.md`
- any output from any other condition.
- any excluded document listed in the manifest.

## Reasoning Mechanism

Use the canonical workflow and apply `docs/experiments/knowledge-construction-profile-v0.1.md` only during Knowledge Generation. Do not use it during Recommendation Generation or Presentation generation except through the resulting Knowledge Set.

## Required Outputs

Create exactly:

- `outputs/evaluations/auc-001-knowledge-construction-validation/condition-b/run-01/knowledge-set.md`
- `outputs/evaluations/auc-001-knowledge-construction-validation/condition-b/run-01/recommendation-set.md`
- `outputs/evaluations/auc-001-knowledge-construction-validation/condition-b/run-01/presentation.md`

Do not create or modify any other file.

## Constraints

- Do not execute BigQuery.
- Do not consult external sources.
- Do not add evidence.
- Do not reuse prior outputs.
- Do not evaluate or compare conditions.
- Do not mention condition identity or profile identity in the generated outputs.
