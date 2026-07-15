# Common Generation Instruction

Generate AUC-001 outputs from the frozen common input package only.

Read the common inputs in this order:

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

Rules:

- Do not execute BigQuery.
- Do not consult external sources.
- Do not add evidence.
- Do not use prior outputs, prior reports, corpus material or excluded documents.
- Do not read outputs from other conditions.
- Do not modify canonical inputs, profiles, protocol, contracts, handoffs, AUC, Skill, Runbook or Checklist.
- Preserve the separation between knowledge, recommendations and presentation.
- Produce exactly these files in the assigned run folder:
  - `knowledge-set.md`
  - `recommendation-set.md`
  - `presentation.md`
- Do not create `execution-record.md`; it will be created after all conditions complete.
- Do not include the condition name, profile version or any blinding-revealing identifier in generated outputs.
