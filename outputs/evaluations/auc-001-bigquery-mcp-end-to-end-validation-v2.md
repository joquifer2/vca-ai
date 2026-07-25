# AUC-001 BigQuery MCP End-to-End Validation v2

## Runtime status

| Field | Value |
| --- | --- |
| Server | `bigquery` |
| Endpoint | `http://127.0.0.1:8000/mcp` |
| Tools used | `discover_metadata`, `query_read_only` |
| Effective identity context | ADC impersonated service account previously validated: `bq-mcp-reader@datamart-vca-494114.iam.gserviceaccount.com` |
| Fallback used | false |
| AUC-001 executed | yes |
| AUC-001 direct BigQuery/CLI used | no |

## Workflow completion

| Step | Status |
| --- | --- |
| Execution Context Canonicalization | completed |
| Context Loading | completed |
| Evidence Acquisition | completed |
| Evidence Set stabilization | completed |
| Knowledge Generation | completed |
| Knowledge Set stabilization | completed |
| Recommendation Generation | completed |
| Recommendation Set stabilization | completed |
| Presentation | completed |

## Workspace resolution

Workspace `vca` resolved from `configs/workspaces.json`.

Authorized and used tables:

- `datamart-vca-494114.intermediate.int_faro_lead_scoring`
- `datamart-vca-494114.marts.fct_lead_enriched`
- `datamart-vca-494114.marts.fct_spend`

Not used because not currently in allowlist:

- `datamart-vca-494114.marts.fct_performance_daily`
- `datamart-vca-494114.marts.dim_campaign_signal`

## MCP execution summary

| Category | Count |
| --- | ---: |
| Total MCP calls | 34 |
| Metadata calls | 4 |
| `query_read_only` calls | 30 |
| Successful analytical queries | 15 |
| Rejected alternate/diagnostic queries | 15 |

Primary successful traces:

- Metadata datasets: `trc-bc47b42930454fec9299376cded1d8d0`
- Scoring schema: `trc-77780fee778e430a832f88160076ef59`
- Leads schema: `trc-c39986c2601840728e18440eb13d937f`
- Spend schema: `trc-7aa891c3a35b4044ac7e3877ea3c3b21`
- Scoring coverage: `trc-3b467af730ae40e088a5edda21d5b4b4`
- Marts coverage: `trc-a439a1cd649143f8915e6082debe9c14`
- Spend signal: `trc-6889781df1a74564b73c7d7416bb23ef`
- Tier counts: `trc-93c012b08583417eba1ca54ecd9e4445`
- Ticket readiness: `trc-6cec4aa795254618947dd1ce28c5d33f`
- Monthly leads: `trc-6326771ea1fb43038ca46822814079cc`
- Monthly spend: `trc-bd4307b28da74668980f3f08841f16b3`
- Raw ad coverage: `trc-1e25d1026e0b40868b728b9823e2d8eb`
- Normalized ad coverage: `trc-12c5479993c24c058b3e59d707b8920d`
- Normalized commercial quality: `trc-5e9e04a4a2364750af8ef941b6cc15fc`
- Campaign quality: `trc-ad1c62efd79641babda7f7aa70f22572`

Rejected traces preserved:

- `ERR_DRY_RUN_FAILED`: `trc-09bc75694f18419a9e463bc38a0fd9e6`, `trc-dad161eb94804a709e0fb18ab883daa0`, `trc-72c3e6dcdac34b4fa1e2d3f5a3e31e2c`, `trc-b1fbb991a9204fbbb6c6e4e2ea0cb4ef`, `trc-e1fc0ab2981640c09a35eb933c89eac7`, `trc-008e79f6757f4e8288b902a20945769f`, `trc-c829aa72ad654cc8880796b233cf9150`, `trc-26b197c8342043c0a64bb720da924a48`, `trc-07e4fc70e3e2447095f6f3af0825b808`, `trc-f6dd5c1adbd1406aa8b0d7d1b7987f85`, `trc-4f8ac8a774104d79b174a958f9141dd6`, `trc-7983a05a8eb341dc935ca5091067ea45`, `trc-b896ed5cb8f54307afa29fee14b9cf96`, `trc-823486a0918f411a8fe499802c126ad5`
- `ERR_SCOPE_DENIED`: `trc-043653f090c4451093f81b45be748c5f`

The rejected queries were alternates used to test query shape and coverage. They were not used to compute findings.

## Checklist outcome

| Checklist area | Result |
| --- | --- |
| Skill activated | pass |
| Runbook followed | pass |
| References loaded before global search | pass |
| Execution context canonicalized | pass |
| Workspace resolved | pass |
| Data Contract/allowlist intersection respected | pass |
| BigQuery MCP only | pass |
| No `gcloud`, `bq`, direct client, or fallback | pass |
| Evidence Set created from current-run queries | pass |
| Knowledge Set derives from Evidence Set | pass |
| Recommendation Set derives from Knowledge Set | pass |
| Presentation consumes stabilized artifacts | pass |
| Historical artifacts not used as analytical source | pass |
| Missing/UNKNOWNs declared | pass |
| Presentation policy file available | observation |
| Knowledge profile duplicate path available | observation |

## Deviations

1. The analytical Presentation Policy canonical route is `.github/presentation_policies/analytical-review.md`. The requested `analytical-review` projection was applied through the Presentation Contract, analytical profile, and user instructions.
2. `docs/experiments/knowledge-construction-profile-v0.2.md` was referenced but not found. The Skill-local `knowledge-construction-profile.md`, titled v0.2, was used.
3. `fct_performance_daily` and `dim_campaign_signal` were contract/context references but outside the current allowlist. They were not queried.
4. Some alternate query shapes failed with `ERR_DRY_RUN_FAILED`. Successful equivalent or narrower query shapes were used for evidence where possible.
5. One combined query failed with `ERR_SCOPE_DENIED` and was replaced by a scope-compliant split query.

## Result

`PASS WITH OBSERVATIONS`

The run satisfies the end-to-end AUC-001 workflow and MCP-only evidence requirements. Observations are limited to missing referenced policy/profile paths, allowlist-limited analytical surface, and non-blocking rejected alternate query shapes.
