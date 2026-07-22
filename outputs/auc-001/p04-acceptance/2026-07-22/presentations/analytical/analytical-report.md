# AUC-001 P04 Acceptance Analytical Report

Canonical Projection Source: `AUC-001-P04-ACCEPTANCE-CANONICAL-PROJECTION-SOURCE`
CPS fingerprint: `79368d267dbe47d297338db1bbf84067694b4181ac0cba8e8874f8434abc5c22`

## Scope And Coverage

Derived from `cps.period`, `cps.sources` and `EVD-001`. Leads cover 2026-04-18 to 2026-07-22; spend covers 2026-04-18 to 2026-07-17.

## Quality Base

Derived from `KNW-001` and `EVD-002`. Leads: 1632. FARO A/B: 504 (30.9%). Tier A: 76 (4.7%).

## Cost-Quality Reconciliation

Derived from `KNW-002`, `EVD-003` and `EVD-004`. Commercial matched universe: 12 ads, 1458 leads, 1069.05001 matched commercial spend. Cost per A/B in matched commercial universe: 2.5095. Coverage states remain explicit: lead_only 5 ads and spend_only 2 ads.

## Signals And Combinations

Derived from `cps.integrated_view.combinations`. The shared explanatory combinations are ticket/form qualification signals, commercial matched ad quality-cost metrics, and temporal source coverage. They explain observed associations, not causal effects.

## Temporal Pattern

Derived from `KNW-004` and `EVD-005`. Monthly evidence is available. Weekly evidence is partial because provider spend stops before the lead source and edge weeks are incomplete.

## Recommendations

Derived from `cps.recommendations`.

| Recommendation | Category | Success criterion |
|---|---|---|
| REC-001 | measurable_experiment | PASS if A/B rate increases versus control while cost_per_ab_commercial_matched is stable or lower over two comparable weeks. |
| REC-002 | verifiable_action | all current lead_only and spend_only rows have a declared reason code |
| REC-003 | measurable_experiment | PASS if qualified-share lift is observed with stable lead volume and no increase in unmapped responses. |
| REC-004 | non_actionable_hypothesis | promote only when future evidence is authorized and reconciled |

## Limitations And UNKNOWN

- Revenue/CRM: not_available.
- Creative causality: UNKNOWN / not_applicable.
- Additional creative metadata: not_available.
- Temporal comparability: partial under provider limits.
