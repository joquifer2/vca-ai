# AUC-001 Context Definition v2

## Execution context canonicalization

Request: analyze Meta Ads lead quality using all authorized evidence available up to 2026-06-30.

Canonical interpretation:

- Analysis cutoff: 2026-06-30.
- Start date: first evidence available in authorized MCP sources, resolved from data as 2026-04-18.
- Real analyzed period: 2026-04-18 to 2026-06-30.
- Workspace: `vca`.
- BigQuery project: `datamart-vca-494114`.
- Location: `EU`.
- Projection: `analytical-review`.
- Audience: analytical/business reviewer.
- Lead quality definition: FARO qualified lead = `lead_tier` A or B.
- Channel scope: Meta Ads / Meta Lead Ads evidence available in authorized tables.

The request says "hasta el 30 de junio de 2026" and does not provide a start date. Following the Runbook rule, the start date was not assumed to be 2026-06-01; it was resolved from provider coverage.

## Loaded governing artifacts

- `.github/skills/meta-lead-quality-analysis/SKILL.md`
- `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`
- `.github/skills/meta-lead-quality-analysis/references.md`
- `.github/skills/meta-lead-quality-analysis/CHECKLIST.md`
- `.github/skills/meta-lead-quality-analysis/ANALYTICAL_PROFILE.md`
- `.github/skills/meta-lead-quality-analysis/knowledge-construction-profile.md`
- `analytical_use_cases/meta_lead_quality_analysis.md`
- `docs/context_refs.md`
- `project_brief.md`
- `knowledge/client/ccd.md`
- `docs/contracts/data.contract.md`
- `docs/contracts/context.contract.md`
- `docs/contracts/presentation.contract.md`
- `docs/handoffs/auc-001-data-contract.md`
- `docs/handoffs/auc-001-presentation-contract.md`
- `configs/workspaces.json`

## Workspace and source resolution

Workspace `vca` authorizes:

- `datamart-vca-494114.intermediate.int_faro_lead_scoring`
- `datamart-vca-494114.marts.fct_lead_enriched`
- `datamart-vca-494114.marts.fct_spend`

The broader AUC/Data Contract context mentions `marts.fct_performance_daily` and `marts.dim_campaign_signal`, but those tables are not in the current MCP allowlist. They were not queried or used.

Intersection used for this run:

| Table | Role | Used |
| --- | --- | --- |
| `intermediate.int_faro_lead_scoring` | FARO scoring, tier, lead-level quality, campaign/ad lead attribution | Yes |
| `marts.fct_lead_enriched` | lead coverage validation | Yes |
| `marts.fct_spend` | spend, campaign signal, ad spend attribution | Yes |

## MCP-only execution

All metadata and metrics came from BigQuery MCP Server tools:

- `discover_metadata`
- `query_read_only`

No `gcloud`, `bq`, direct BigQuery client, fallback, historical report, previous Knowledge Set, previous Recommendation Set, previous Presentation, or previous evaluation was used as an analytical source.

## Deviations and unavailable references

- The analytical Presentation Policy canonical route is `.github/presentation_policies/analytical-review.md`. The run used the requested `analytical-review` projection, base Presentation Contract, and explicit user requirements.
- `docs/experiments/knowledge-construction-profile-v0.2.md` was referenced by `CHECKLIST.md` but was not present. The available Skill file `.github/skills/meta-lead-quality-analysis/knowledge-construction-profile.md`, titled Knowledge Construction Profile v0.2, was used.
