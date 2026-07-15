# Knowledge Construction Experimental Package

## Experimental Scope

This package freezes the documentary inputs required to validate whether a Knowledge Construction Profile improves Knowledge Generation for AUC-001.

The experiment compares three conditions:

- Condition A: current workflow without Knowledge Construction Profile.
- Condition B: current workflow with Knowledge Construction Profile v0.1 during Knowledge Generation only.
- Condition C: current workflow with Knowledge Construction Profile v0.2 during Knowledge Generation only.

The package validates reasoning behavior during Knowledge Generation. It does not validate BigQuery access, data acquisition, profile design, Foundation architecture, contract design or presentation policy design.

## Frozen Inputs

| Artifact | Path | Status | Version | Dependency | In Package |
|---|---|---|---|---|---|
| AUC-001 | `analytical_use_cases/meta_lead_quality_analysis.md` | Proposed / validated as AUC entrypoint | Not declared | Root analytical use case | Yes |
| Skill | `.github/skills/meta-lead-quality-analysis/SKILL.md` | Active skill | `SDD-SKILL-006` | AUC-001, Runbook, references, Checklist | Yes |
| Runbook | `.github/skills/meta-lead-quality-analysis/RUNBOOK.md` | Active procedural workflow | Not declared | Skill | Yes |
| Checklist | `.github/skills/meta-lead-quality-analysis/CHECKLIST.md` | Active pre-presentation checklist | Not declared | Skill, Runbook | Yes |
| Presentation Policy | `.github/presentation_policies/executive-decision-support.md` | Selected policy for executive output | Not declared | Presentation Layer, Presentation Contract | Yes |
| Execution Context | `docs/handoffs/auc-001-execution-context.md` | Validated | `1.0.0` | Analysis Request, AUC-001 | Yes |
| Evidence Set | `docs/handoffs/auc-001-evidence-set.md` | Documented | `1.0.0` | Analytical Contract, Execution Context | Yes |
| Evidence Contract | `docs/handoffs/auc-001-evidence-contract.md` | Documented | `1.0.0` | Evidence Set | Yes |
| Knowledge Contract | `docs/handoffs/auc-001-knowledge-contract.md` | Documented | `1.0.0` | Evidence Contract, Knowledge Set | Yes |
| Recommendation Contract | `docs/handoffs/auc-001-recommendation-contract.md` | Documented | `1.0.0` | Knowledge Contract, Recommendation Set | Yes |
| Presentation Contract | `docs/handoffs/auc-001-presentation-contract.md` | Documented | `1.1.0` | Recommendation Contract, Presentation Layer | Yes |
| Knowledge Construction Profile v0.1 | `docs/experiments/knowledge-construction-profile-v0.1.md` | Experimental baseline profile | `v0.1` | AUC-001 Knowledge Generation | Yes |
| Knowledge Construction Profile v0.2 | `docs/experiments/knowledge-construction-profile-v0.2.md` | Experimental reduced profile | `v0.2` | v0.1 review, AUC-001 Knowledge Generation | Yes |
| Validation Protocol | `docs/evaluations/knowledge-construction-profile-validation-protocol.md` | Canonical remediated protocol | `1.0.0-remediated` | This package | Yes |

Frozen evidence blocks:

- EVD-001 - Model Coverage By Status.
- EVD-002 - Prepared Model Totals.
- EVD-003 - Ad Reference Evidence.
- EVD-004 - Campaign And Adset Evidence Where Available.

Frozen period:

- 2026-06-01 to 2026-06-30.

Frozen AUC:

- AUC-001 - Meta Lead Quality Analysis.

## Frozen Outputs

The future experiment must produce outputs only under:

`outputs/evaluations/auc-001-knowledge-construction-validation/`

Each condition must produce:

- `knowledge-set.md`
- `recommendation-set.md`
- `presentation.md`
- `execution-record.md`
- `prompt-used.md`

Blind review must produce:

- `blind-review/output-x/knowledge-set.md`
- `blind-review/output-x/recommendation-set.md`
- `blind-review/output-x/presentation.md`
- `blind-review/output-y/knowledge-set.md`
- `blind-review/output-y/recommendation-set.md`
- `blind-review/output-y/presentation.md`
- `blind-review/output-z/knowledge-set.md`
- `blind-review/output-z/recommendation-set.md`
- `blind-review/output-z/presentation.md`
- `blind-review/blinding-key.md`
- `blind-review/evaluation-form.md`

No canonical handoff may be overwritten by experimental outputs.

## Experimental Variables

### Independent variable

The Knowledge Generation reasoning mechanism:

- no profile for Condition A;
- Knowledge Construction Profile v0.1 for Condition B;
- Knowledge Construction Profile v0.2 for Condition C.

### Controlled variables

- AUC-001.
- Execution Context.
- Period.
- Evidence Set.
- Evidence blocks.
- Evidence Contract.
- Knowledge Contract.
- Recommendation Contract.
- Presentation Contract.
- Presentation Policy.
- Skill.
- Runbook.
- Checklist.
- Output schema.
- Prompt structure, except for the declared reasoning profile difference.
- No BigQuery execution.
- No external sources.
- No new evidence.
- No reuse of outputs across conditions.

### Non-controllable variables

The current environment may not expose or allow fixed control of:

- exact model version string;
- temperature;
- sampling parameters;
- seed;
- deterministic replay;
- full isolation guarantees equivalent to separate clean runtime processes.

These variables must be recorded explicitly in each execution record. The experiment must not claim strict determinism unless the execution environment exposes and fixes those controls.

## Reproducibility Constraints

### What can be reproduced

- The frozen documentary input package.
- The AUC, period, Evidence Set and Contracts used by all conditions.
- The prompt text used for each condition.
- The output schema.
- The evaluation rubric.
- The blind review mapping and evaluation package.
- The absence of new BigQuery queries if execution records confirm it.

### What cannot be guaranteed in the current environment

- Bit-for-bit regeneration of model outputs.
- Deterministic equality across repeated runs.
- Fixed seed behavior.
- Full control over temperature and sampling if not exposed.
- Full isolation proof if the runtime does not expose independent clean contexts.

### What must be declared explicitly

- Model identity exposed by the environment.
- Model version if available.
- Temperature if configurable; otherwise `not exposed / not configurable`.
- Sampling parameters if configurable; otherwise `not exposed / not configurable`.
- Seed or deterministic setting if available; otherwise `not guaranteed`.
- Actual order of condition execution.
- Any isolation limitation.
- Any deviation from the package manifest.

## Repository State

Recommended execution commit:

- The first repository commit created after this remediation that includes this manifest, the canonical protocol, the remediation report, Knowledge Construction Profile v0.1 and Knowledge Construction Profile v0.2.

Base commit inspected during remediation:

- `b78c35138fdc4d6b4c0cc0b3e0908df47f49a587`

Files modified by this remediation:

- `docs/evaluations/knowledge-construction-profile-validation-protocol.md`

Files created by this remediation:

- `docs/evaluations/knowledge-construction-experimental-package.md`
- `docs/evaluations/knowledge-construction-remediation-report.md`

Experimental files that must be present in the recommended execution commit:

- `docs/evaluations/knowledge-construction-profile-validation-protocol.md`
- `docs/evaluations/knowledge-construction-experimental-package.md`
- `docs/evaluations/knowledge-construction-remediation-report.md`
- `docs/experiments/knowledge-construction-profile-v0.1.md`
- `docs/experiments/knowledge-construction-profile-v0.2.md`

## Preconditions

Before executing the experiment:

1. Commit or otherwise freeze all files listed in this package.
2. Confirm the protocol contains only one canonical protocol body.
3. Confirm v0.1 and v0.2 have no pending unintended edits.
4. Confirm all frozen input paths exist.
5. Confirm no canonical contracts or handoffs changed after package freeze.
6. Define all three prompts before running any condition.
7. Declare the available model configuration.
8. Decide and record the execution order.
9. Confirm that no BigQuery queries or external sources will be executed.
10. Confirm that outputs will be written only under `outputs/evaluations/auc-001-knowledge-construction-validation/`.

## Blocking Conditions

Block the experiment if any of the following occurs:

- The package manifest is missing or stale.
- The protocol again contains multiple competing versions.
- Any frozen input is missing.
- Any frozen input changed without refreezing the package.
- The conditions cannot use the same Execution Context, Evidence Set, period, AUC, Contracts, Presentation Policy, Skill or Runbook.
- A condition requires new BigQuery execution.
- A condition requires evidence not present in the Evidence Set.
- The execution cannot record non-controllable model variables.
- Prompts cannot be defined before condition execution.
- Outputs from one condition would be visible as input to another condition.
- Blind review files reveal condition identity.

## Experiment Classification

Final category: B. Controlled Comparative Evaluation.

This is not a Strict Reproducible Experiment because the current environment does not expose full control over seed, temperature, sampling parameters, deterministic replay or exact model version guarantees.

This is stronger than an Exploratory Evaluation because the repository provides a frozen AUC, Execution Context, Evidence Set, Contracts, Presentation Policy, Skill, Runbook, profiles, output schema and rubric. The independent variable is explicit and the documentary package can be held constant across conditions.