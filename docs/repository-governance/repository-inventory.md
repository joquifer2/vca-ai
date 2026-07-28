# Repository Inventory

## Metadata

| Campo | Valor |
|---|---|
| Artifact type | Repository Inventory |
| Iteration | Project Consolidation |
| Iteration ID | VCA-IA-PC-001 |
| Status | QA refreshed physical inventory - human validation pending |
| Date | 2026-07-28 |
| Source | Filesystem inventory generated after Project Consolidation QA Gate persistence |

## Scope

This inventory records repository artifacts for documentary consolidation. It does not read analytical outputs as evidence, does not acquire data and does not modify AUC-001.

Exclusions: `.git/`, `.codex/` and `.env.local` are excluded. `.env.local` is treated as local sensitive configuration and is not governed by content inventory.

The complete row-level inventory is stored in:

`docs/repository-governance/repository-inventory.csv`

## Summary

Total inventoried files: 466

## By Preliminary Category

| Category | File count |
|---|---:|
| archivable_candidate | 2 |
| documentary_evidence | 93 |
| experimental_closed | 3 |
| historical | 3 |
| historical_output | 166 |
| normative_current | 75 |
| normative_current_candidate | 6 |
| operational_current | 34 |
| supporting | 84 |

## By Top-Level Area

| Area | File count |
|---|---:|
| .github | 20 |
| .gitignore | 1 |
| AGENTS.md | 1 |
| analytical_use_cases | 5 |
| Borradores | 2 |
| configs | 1 |
| docs | 164 |
| gates | 35 |
| knowledge | 2 |
| memory | 1 |
| outputs | 166 |
| project_brief.md | 1 |
| README.md | 1 |
| specs | 19 |
| tasks | 10 |
| tests | 12 |
| tools | 23 |
| workflows | 2 |

## Classification Fields

The CSV uses these fields:

- path
- area
- artifact_type
- preliminary_category
- existing_class_mapping
- local_evaluation_category
- primary_consumer
- ownership_status
- proposed_action
- notes

## WS-0 Closure Status

This inventory has been refreshed after QA Gate persistence. WS-0 still requires human review of conceptual duplication and ambiguous ownership before repository governance can be promoted from candidate/draft to definitive baseline.
