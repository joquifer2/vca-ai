# Specification

## Metadata

### Spec ID

SPEC-013

### Title

AUC-001 Structured Reconciliation Output

### Status

Accepted - Exit Gate PASS WITH CONDITIONS; PCI-002 Entry Gate pending QA Gate Agent

### Owner

Equipo VCA / Specification Agent

### Last Updated

2026-07-19

### Classification

Post-closure evolution of AUC-001; output schema hardening

### Parent Analytical Use Case

AUC-001 - Meta Lead Quality Analysis

### Source Input

Architect Agent memo and architectural pre-review: reconciliation of total investment, commercial investment and coverage states for AUC-001.

### Related Specification

[`SPEC-012 - AUC-001 Canonical Cost-Quality Model`](/specs/spec-012-auc-001-canonical-cost-quality-model.md)

### Historical Execution

`AUC-001-PCI-001-2026-06-30`

### Historical Output Namespace

`outputs/auc-001/pci-001/2026-06-30/`

---

## 1. Purpose

Close the structured exposure gap detected after the `AUC-001-PCI-001` execution.

This specification requires future AUC-001 executions to persist investment and coverage reconciliation in a structured format consumable by analytical and executive reports without recalculating reconciliations, reinterpreting names, mixing signals, inferring coverage states or consulting Markdown artifacts to complete `runtime-output.json`.

This specification does not redesign the canonical model defined by SPEC-012.

---

## 2. Problem Or Need

SPEC-012 correctly defines the canonical cost-quality model and the historical execution `AUC-001-PCI-001-2026-06-30` demonstrated that the core economic and coverage identities hold:

```text
commercial_spend = matched_commercial_spend + spend_only_commercial_spend
total_leads = matched_leads + lead_only_leads
total_ab_leads = matched_ab_leads + lead_only_ab_leads
```

The remaining gap is not a model or calculation gap. It is a consumability gap: total spend by signal, canonical naming and some reconciliation guarantees are available for validation, but are not yet exposed as a complete structured runtime output contract for future analytical products.

---

## 3. Scope

### Included

- future structured schema for `runtime-output.json`;
- `spend_reconciliation` block;
- `coverage_reconciliation` block;
- canonical names `matched_commercial_spend` and `spend_only_commercial_spend`;
- controlled deprecated aliases for `matched_spend` and `spend_only_spend`;
- explicit consumer guarantees;
- formal invariant record schema;
- output schema family and versioning;
- allowed and prohibited metric consumption rules;
- required tests;
- future documentation update of state in README and AUC-001 index;
- Reviewer Agent and Entry Gate conditions.

### Out Of Scope

- modifying SPEC-012 unless a contradiction is demonstrated;
- redesigning the canonical model;
- consulting BigQuery;
- recalculating the historical execution;
- modifying closed outputs;
- regenerating reports;
- defining the analytical product contract;
- starting transversal contract refactoring;
- promoting capabilities to AIF Foundation;
- modifying `outputs/auc-001/pci-001/2026-06-30/`.

---

## 4. AUC-Specific Rules And Reusable Responsibilities

This specification remains AUC-local. It explicitly separates concepts that belong to AUC-001 from responsibilities that may later be evaluated as reusable methodological capabilities.

### 4.1 AUC-001 Specific Rules

| Element | Scope |
|---|---|
| `COMMERCIAL` | AUC-001 spend signal used for commercial efficiency. |
| `matched_commercial_spend` | AUC-001 canonical matched commercial investment field. |
| `spend_only_commercial_spend` | AUC-001 canonical spend-only commercial investment field. |
| `matched`, `lead_only`, `spend_only`, `unknown` | AUC-001 coverage states inherited from SPEC-012. |
| CPL, CPQL and cost-per-quality restrictions | AUC-001 economic metric policy inherited from SPEC-012. |

### 4.2 Potentially Reusable Responsibilities

These responsibilities are generic in shape, but are not promoted to AIF Foundation by this specification:

| Responsibility | Reuse hypothesis |
|---|---|
| `coverage_reconciliation` | Structured coverage state publication may be useful for other AUCs. |
| `output_schema_version` and `schema_family` | Versioned output schemas may be useful across analytical outputs. |
| invariant validation records | PASS/FAIL identity records may be reusable for governed outputs. |
| deprecated alias control | Temporary schema compatibility may be reusable during migrations. |
| structured output consumption | Analytical products should consume structured artifacts rather than Markdown tables. |

Future promotion to AIF Foundation requires separate evidence, architectural review and approval. SPEC-013 only reinforces AUC-001.

---

## 5. Historical Compatibility

The historical namespace:

```text
outputs/auc-001/pci-001/2026-06-30/
```

remains immutable.

This specification applies only to future AUC-001 executions after `AUC-001-PCI-001-2026-06-30`.

Consumers must be able to identify the structured schema family and version through stable fields:

```json
{
  "schema_family": "auc_001_reconciliation_output",
  "output_schema_version": "auc_001_reconciliation_output.v1"
}
```

Compatibility with previous names may exist only if:

- it is declared as temporary;
- it is documented inside the output;
- aliases are not an independent source of truth;
- automated validation proves exact equivalence.

---

## 6. Structured Spend Reconciliation

Future versions of `runtime-output.json` must include a structured block equivalent to:

```json
{
  "spend_reconciliation": {
    "total_spend_all_signals": null,
    "spend_by_signal": {},
    "commercial_spend": null,
    "matched_commercial_spend": null,
    "spend_only_commercial_spend": null,
    "non_commercial_spend": null,
    "non_commercial_spend_by_signal": {},
    "invariants": []
  }
}
```

### 6.1 Field Semantics

| Field | Meaning |
|---|---|
| `total_spend_all_signals` | Sum of spend across all authorized signals in `marts.fct_spend` for the execution period. |
| `spend_by_signal` | Spend map by `campaign_signal`, including at minimum `COMMERCIAL` and any observed non-commercial signal. |
| `commercial_spend` | Spend where `campaign_signal = 'COMMERCIAL'`. |
| `matched_commercial_spend` | Commercial spend with `matched` coverage. |
| `spend_only_commercial_spend` | Commercial spend with `spend_only` coverage. |
| `non_commercial_spend` | Total spend for signals other than `COMMERCIAL`. |
| `non_commercial_spend_by_signal` | Spend map by non-commercial signal. |
| `invariants` | Structured validation records for spend identities. |

### 6.2 Monetary Rules

| Rule | Requirement |
|---|---|
| Currency | EUR. |
| Numeric representation | Decimal string or numeric type with no intermediate rounding. |
| Precision | Sufficient to recompute identities; presentation may round to 2 decimals. |
| Tolerance | 0.01 EUR for published aggregate reconciliation. |
| Missing values | `null` only when the source value is unavailable or blocked; never infer as 0. |
| Unknown values | `null` plus explicit UNKNOWN state or blocker explaining why the value is not reliable. |

### 6.3 Required Spend Identities

Each future output must persist identity results as PASS/FAIL, not only the values.

```text
total_spend_all_signals = commercial_spend + non_commercial_spend
commercial_spend = matched_commercial_spend + spend_only_commercial_spend
non_commercial_spend = sum(non_commercial_spend_by_signal)
total_spend_all_signals = sum(spend_by_signal)
```

Failure of any required spend identity is a blocking error for the affected Evidence Set or metric.

---

## 7. Structured Coverage Reconciliation

Future versions of `runtime-output.json` must include a structured block equivalent to:

```json
{
  "coverage_reconciliation": {
    "matched": {},
    "lead_only": {},
    "spend_only": {},
    "unknown": {},
    "invariants": []
  }
}
```

### 7.1 Required Coverage Fields

The block must include, at minimum:

| Field group | Required values |
|---|---|
| `matched` | `ad_count`, `leads`, `ab_leads`, `tier_a`, `tier_b`, `matched_commercial_spend`. |
| `lead_only` | `ad_count`, `leads`, `ab_leads`, `tier_a`, `tier_b`. |
| `spend_only` | `ad_count`, `spend_only_commercial_spend`. |
| `unknown` | `ad_count`, `leads`, `ab_leads`, `tier_a`, `tier_b`, `commercial_spend`, `reason_codes` or explicit empty array. |
| `invariants` | Array of identity validation objects with name, expression, left value, right value, tolerance where applicable and result. |

UNKNOWN must be explicit even when zero:

```json
{
  "unknown": {
    "ad_count": 0,
    "leads": 0,
    "ab_leads": 0,
    "tier_a": 0,
    "tier_b": 0,
    "commercial_spend": "0",
    "reason_codes": []
  }
}
```

It is not valid to infer UNKNOWN solely from the absence of blockers.

### 7.2 Required Coverage Identities

The `coverage_reconciliation.invariants` array must include PASS/FAIL results for:

```text
total_leads = matched.leads + lead_only.leads + unknown.leads
total_ab_leads = matched.ab_leads + lead_only.ab_leads + unknown.ab_leads
tier_a_total = matched.tier_a + lead_only.tier_a + unknown.tier_a
tier_b_total = matched.tier_b + lead_only.tier_b + unknown.tier_b
commercial_spend = matched.matched_commercial_spend + spend_only.spend_only_commercial_spend + unknown.commercial_spend
prepared_ad_count = matched.ad_count + lead_only.ad_count + spend_only.ad_count + unknown.ad_count
```

If `unknown` values are zero, the identity must still include them explicitly.

---

## 8. Invariant Record Contract

Every invariant object published in `spend_reconciliation.invariants`, `coverage_reconciliation.invariants` or an equivalent future structured block must follow this minimum contract:

```json
{
  "name": "commercial_spend_reconciliation",
  "expression": "commercial_spend = matched_commercial_spend + spend_only_commercial_spend",
  "left_value": "875.85",
  "right_value": "875.85",
  "tolerance": "0.01",
  "result": "PASS"
}
```

| Field | Requirement |
|---|---|
| `name` | Stable machine-readable identifier for the invariant. |
| `expression` | Human-readable identity or expression validated. |
| `left_value` | Observed left side of the identity. |
| `right_value` | Observed right side of the identity. |
| `tolerance` | Monetary or numeric tolerance when applicable; `null` for exact integer identities. |
| `result` | `PASS` or `FAIL`. |

The invariant record may include additional traceability fields in future executions, but these fields are mandatory. `PASS` and `FAIL` are the only allowed result values unless a later specification extends the state machine.

This invariant schema is a reusable pattern candidate, but remains AUC-001-local until separately evaluated.

---

## 9. Consumer Contract

Any consumer of a future `runtime-output.json` conforming to this specification may assume:

- `spend_reconciliation` always exists.
- `coverage_reconciliation` always exists.
- `matched`, `lead_only`, `spend_only` and `unknown` are always present, even when their values are zero.
- every published identity has already been validated.
- each identity result, `PASS` or `FAIL`, is part of the contract.
- canonical spend field names are the source of truth.
- deprecated aliases, if present, are equivalent to canonical names by validation.
- Markdown documents are not required to complete the structured runtime information.

Consumers must reject or quarantine outputs that lack required blocks, lack schema versioning, omit explicit UNKNOWN, contain failing required invariants or expose unsupported aliases.

---

## 10. Canonical Naming And Deprecated Aliases

The canonical field names are:

```text
matched_commercial_spend
spend_only_commercial_spend
```

Temporary compatibility aliases may exist:

```text
matched_spend
spend_only_spend
```

If compatibility aliases are kept, they must be declared as deprecated aliases in a schema metadata block:

```json
{
  "deprecated_aliases": {
    "matched_spend": "matched_commercial_spend",
    "spend_only_spend": "spend_only_commercial_spend"
  }
}
```

Aliases are deprecated compatibility fields. They cannot evolve independently, cannot have different values and cannot be treated as separate sources of truth.

Any mismatch between alias and canonical field is a blocking error.

The name `deprecated_aliases` is required because it makes the temporary and non-authoritative character of these fields explicit. A neutral name such as `compatibility_aliases` could be misread as a permanent supported interface.

---

## 11. Metrics Policy

SPEC-012 remains authoritative for metric validity. This specification hardens output consumption rules.

### 11.1 Allowed

Efficiency metrics may be calculated only over the universe and coverage authorized by SPEC-012:

- `cpl_commercial_matched`;
- `cost_per_ab_commercial_matched`;
- `cost_per_tier_a_commercial_matched` when denominator and threshold conditions hold;
- `qualified_rate_ab_matched`;
- `qualified_rate_ab_global`;
- reconciliation shares such as `spend_share_matched`, `lead_share_matched`, `ab_share_matched`;
- spend-side descriptive shares such as `spend_share_by_signal`.

### 11.2 Prohibited

The output schema and tests must prohibit:

- CPL over `lead_only`;
- CPQL or cost-per-quality over `lead_only`;
- CPL or CPQL over `spend_only`;
- economic efficiency metrics mixing non-commercial signals;
- use of `total_spend_all_signals` as numerator for commercial efficiency;
- denominators of zero converted into 0;
- metrics without explicit signal, universe and coverage;
- any metric where aliases and canonical names disagree.

---

## 12. Output Schema Versioning

Future runtime outputs must declare:

| Field | Requirement |
|---|---|
| `schema_family` | Stable family identifier for this kind of structured output. |
| `output_schema_version` | Stable schema version string. |
| `model_name` | `auc_001_canonical_cost_quality_model`. |
| `specification_versions` | Must include `SPEC-012` and this specification. |
| `deprecated_aliases` | Required if legacy field names are emitted. |
| `schema_status` | `active`, `compatibility`, or `deprecated` as applicable. |

A consumer must be able to reject outputs that lack the structured reconciliation schema or whose schema version is unsupported.

Decision: include `schema_family` now.

Rationale: `output_schema_version` identifies one concrete version, but does not provide a stable grouping for related future versions. `schema_family` allows consumers to recognize that `auc_001_reconciliation_output.v1`, `auc_001_reconciliation_output.v2` or later compatible versions belong to the same conceptual output family. This adds low complexity and helps avoid coupling consumers to a single version string.

This does not create a Foundation-level schema registry. It is an AUC-001-local field that may later inform reusable schema governance if enough evidence appears.

---

## 13. Architectural Reflection On `runtime-output.json`

Current proposal keeps the structured reconciliation inside:

```text
runtime-output.json
```

This is acceptable for the next AUC-001 iteration because the reconciliation is produced by the deterministic runtime boundary defined by SPEC-012 and is directly tied to model execution. Keeping it in `runtime-output.json` avoids creating a new artifact type before the use case has produced enough evidence that a separate structured package contract is needed.

However, the reflection surfaces a future architectural question: analytical products may eventually need a broader structured artifact that contains runtime output, Evidence Set metadata, schema versioning, validation state and consumer-facing guarantees without mixing execution internals with product consumption contracts.

Conclusion: keep `runtime-output.json` as the structured contract for this specification and next implementation step, but require Architect Agent review before generalizing this pattern beyond AUC-001 or before promoting it to AIF Foundation.

This specification does not promote any reusable capability. It only strengthens AUC-001 so future evidence can show whether structured reconciliation output, invariant records, schema families and deprecated alias governance are general enough for the framework.

---

## 14. Proposed Affected Files

This specification proposes future changes to:

| File | Proposed impact |
|---|---|
| `tools/auc_001_canonical_cost_quality_model.py` | Emit structured `spend_reconciliation`, `coverage_reconciliation`, schema metadata, invariant records and canonical spend names. |
| `tests/evals/auc_001_canonical_cost_quality_model_tests.ps1` | Add schema, reconciliation, invariant, deprecated alias, UNKNOWN and metric prohibition tests. |
| `README.md` | Reflect real state: `AUC-001-PCI-001` executed, Exit Gate `PASS WITH CONDITIONS`, model stabilized, structured exposure still pending. |
| `analytical_use_cases/auc-001/README.md` | Reflect real AUC-001 post-closure state and pending structured output hardening. |
| Future output namespaces | Persist the new structured runtime output for future executions only. |

No change is proposed for `outputs/auc-001/pci-001/2026-06-30/`.

---

## 15. Tests Required

Future implementation must include automated tests for:

| ID | Test |
|---|---|
| TST-001 | `runtime-output.json` includes `spend_reconciliation`. |
| TST-002 | `runtime-output.json` includes `coverage_reconciliation`. |
| TST-003 | Spend identities pass within 0.01 EUR tolerance. |
| TST-004 | Lead and quality identities pass exactly for integer counts. |
| TST-005 | UNKNOWN is explicit even when all values are zero. |
| TST-006 | `matched_spend` equals `matched_commercial_spend` while deprecated alias compatibility exists. |
| TST-007 | `spend_only_spend` equals `spend_only_commercial_spend` while deprecated alias compatibility exists. |
| TST-008 | Economic metrics over `lead_only` are rejected or null with blocker/limitation. |
| TST-009 | Quality-cost metrics over `spend_only` are rejected or null with blocker/limitation. |
| TST-010 | Non-commercial signals cannot be mixed into commercial efficiency metrics. |
| TST-011 | `total_spend_all_signals` cannot be used as commercial efficiency numerator. |
| TST-012 | Zero denominators produce `null`, not 0. |
| TST-013 | Every economic metric declares signal, universe and coverage. |
| TST-014 | `output_schema_version` is present and supported. |
| TST-015 | `schema_family` is present and stable for the output family. |
| TST-016 | Every invariant object includes `name`, `expression`, `left_value`, `right_value`, `tolerance` and `result`. |
| TST-017 | Future analytical products can consume reconciliation from structured JSON without reading execution Markdown documents. |

---

## 16. Acceptance Criteria

### AC-001

Future AUC-001 executions persist the full spend reconciliation in structured format.

### AC-002

Future AUC-001 executions persist the full coverage reconciliation in structured format.

### AC-003

Analytical and executive reports can consume reconciliations without recomputing them or reading Markdown artifacts as data inputs.

### AC-004

Required identities are validated automatically and their PASS/FAIL result is persisted.

### AC-005

UNKNOWN is explicit even when zero.

### AC-006

`matched_commercial_spend` and `spend_only_commercial_spend` are the only canonical names for matched and spend-only commercial investment.

### AC-007

Legacy aliases, if emitted, are temporary, declared as deprecated and automatically checked for exact equivalence with canonical names.

### AC-008

No CPL, CPQL or economic efficiency metric can be calculated over invalid universes or mixed signals.

### AC-009

Historical outputs remain intact and are not regenerated.

### AC-010

README and AUC-001 index reflect that `AUC-001-PCI-001` executed with Exit Gate `PASS WITH CONDITIONS`, the canonical model is stabilized, and structured exposure remains pending for later products.

### AC-011

Tests cover schema presence, identities, UNKNOWN, aliases, invalid metrics and schema versioning.

### AC-012

Any future analytical product can consume only the structured output without reading `execution.md`, `evidence-set.md`, `analytical-report.md` or any other Markdown document generated during the execution as a data source.

### AC-013

The output declares `schema_family` and `output_schema_version` so consumers can distinguish the output family from a concrete version.

### AC-014

Invariant objects follow the minimum invariant record contract defined by this specification.

---

## 17. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Consumers continue reading Markdown tables as data | High | Require structured reconciliation in runtime output and schema version checks. |
| Future consumers ignore the structured output and keep using `execution.md`, `evidence-set.md`, `analytical-report.md` or other generated Markdown files as data sources | High | Treat Markdown as presentation/audit material only; require product consumers to read structured JSON for reconciliation data. |
| Alias names become independent metrics | High | Treat aliases as deprecated compatibility fields and block mismatches. |
| `total_spend_all_signals` is mistaken for commercial efficiency spend | High | Separate spend-side shares from matched commercial efficiency metrics. |
| UNKNOWN disappears when zero | Medium | Require explicit `unknown` object in every output. |
| Historical execution is retrofitted | High | Keep `outputs/auc-001/pci-001/2026-06-30/` immutable and apply only to future executions. |
| Documentation overstates closure | Medium | README and AUC index must distinguish stabilized model from pending structured exposure. |
| Schema hardening expands into product contract design | Medium | Keep product analytical contract explicitly out of scope. |
| Runtime output becomes overloaded with product-facing responsibilities | Medium | Keep this placement for AUC-001 only and require Architect Agent review before generalizing. |

---

## 18. Dependencies

- `.github/instructions/sdd.instructions.md`;
- `.github/agents/specification.agent.md`;
- `.github/skills/meta-lead-quality-analysis/SKILL.md`;
- `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`;
- `.github/skills/meta-lead-quality-analysis/references.md`;
- `docs/context_refs.md`;
- `project_brief.md`;
- `analytical_use_cases/meta_lead_quality_analysis.md`;
- `analytical_use_cases/auc-001/analytical-contract.md`;
- `specs/spec-012-auc-001-canonical-cost-quality-model.md`;
- `docs/decisions/auc-001/auc-001-canonical-cost-quality-model-architectural-decision.md`;
- `gates/auc-001-pci-001-entry-gate.md`;
- `gates/auc-001-pci-001-exit-gate.md`.

---

## 19. Cross-Artifact Impact Analysis

| Artifact | Impact | Proposed action |
|---|---|---|
| Project Brief | No direct change required. | Keep unchanged. |
| README | State is stale relative to executed `AUC-001-PCI-001`. | Update after Reviewer/Entry Gate approval. |
| Context References | Does not yet index SPEC-013. | Add SPEC-013 when accepted. |
| SPEC-012 | No redesign required. | Keep as normative model source. |
| Analytical Contract | Metric policy remains compatible. | No immediate change unless Reviewer requests explicit reference. |
| Data Contract | No new provider or source. | Keep unchanged. |
| Evidence Contract | Structured output hardening may later deserve reference. | Defer until implementation planning. |
| Gates | Entry Gate must verify limited implementation scope. | Create or update gate evidence after Reviewer approval. |
| Templates | No template change. | Keep unchanged. |
| Agents and Skills | No role or workflow change. | Keep unchanged. |
| Glossary | May later add `schema_family`, `deprecated_aliases`, `coverage_reconciliation`. | Defer to Documentation Agent if terms become recurrent. |

---

## 20. Historical Reviewer Conditions

These reviewer conditions were used before SPEC-013 moved through implementation validation and Exit Gate. They are retained for traceability.

Reviewer Agent had to verify:

- this specification does not redesign SPEC-012;
- no historical output modification is required or implied;
- no BigQuery acquisition is required;
- no report regeneration is required;
- canonical names and aliases are unambiguous;
- invalid metric universes remain prohibited;
- UNKNOWN remains explicit;
- invariant object schema is complete and verifiable;
- `schema_family` and `output_schema_version` are justified;
- `deprecated_aliases` correctly communicates temporary compatibility;
- Consumer Contract gives clear guarantees without defining product contract scope;
- proposed documentation changes reflect state without closing future work prematurely;
- scope remains AUC-local and does not promote anything to AIF Foundation.

Reviewer Agent review is no longer the next operational step for SPEC-013. The current follow-up is the PCI-002 QA Entry Gate for physical runtime-output persistence.

---

## 21. Conditions For Entry Gate

Entry Gate may authorize future task planning and implementation only when:

- Reviewer Agent accepts this specification;
- the implementation scope is limited to runtime output schema, tests and state documentation;
- historical outputs are protected by explicit no-write rule;
- output schema versioning is included in the task plan;
- `schema_family` is included in the task plan;
- invariant record schema tests are included in the task plan;
- product consumers are prohibited from using execution Markdown as data source for reconciliation;
- tests for all required identities and prohibited metric cases are planned;
- no changes to SPEC-012, transversal contracts, product analytical contract or AIF Foundation are included unless a separate approved specification authorizes them.

Entry Gate must block if:

- implementation proposes recalculating or editing `outputs/auc-001/pci-001/2026-06-30/`;
- aliases can diverge from canonical fields;
- UNKNOWN is represented only by absence;
- metrics can be consumed without signal, universe and coverage;
- non-commercial spend can enter commercial efficiency metrics;
- implementation creates a new structured artifact type without Architect Agent review.

---

## 22. Open Questions

No open question blocks PCI-002 QA Entry Gate review.

Architect Agent should revisit whether `runtime-output.json` remains the right structured consumer contract before this pattern is generalized beyond AUC-001 or proposed for AIF Foundation.

---

## 23. Current Recommended Step

Siguiente agente recomendado: **QA Gate Agent**.

Instruccion recomendada:

```text
Actua como QA Gate Agent de vca-ai. Evalua el Entry Gate de AUC-001-PCI-002 usando `tasks/auc-001-pci-002-runtime-output-persistence-task-plan.md`, `docs/evaluations/auc-001/validations/auc-001-pci-002-entry-gate-handoff-to-qa.md` y `docs/evaluations/auc-001/validations/auc-001-pci-002-planning-review.md`. No implementes codigo, no ejecutes BigQuery y no modifiques outputs.
```

---

## Definition of Done

This specification is complete when:

- it defines structured spend and coverage reconciliation blocks;
- it defines field semantics, precision, UNKNOWN and missing-value handling;
- it separates AUC-001-specific rules from reusable responsibility candidates;
- it defines consumer guarantees;
- it formalizes invariant records;
- it fixes canonical names and deprecated aliases;
- it preserves SPEC-012 allowed/prohibited metric policy;
- it protects historical outputs;
- it identifies proposed affected files;
- it defines required tests;
- it establishes acceptance criteria;
- it declares risks;
- it defines Reviewer and Entry Gate conditions;
- it documents the architectural reflection on `runtime-output.json`;
- it does not implement runtime, output or report changes.