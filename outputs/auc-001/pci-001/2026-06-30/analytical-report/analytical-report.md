# Analytical Report

## Scope

This report represents AUC-001-PCI-001 as a separated post-closure execution. It uses BigQuery MCP Server as the only data provider and persists only under `outputs/auc-001/pci-001/2026-06-30/`.

## Method

1. Validate allowlisted sources through MCP metadata discovery.
2. Resolve provider coverage for the execution period.
3. Acquire lead-side, scoring-side and spend-side evidence through separate MCP reads.
4. Construct the canonical cost-quality model by `ad_id_norm`.
5. Validate invariants, coverage states, blockers and warnings.
6. Generate Knowledge and Recommendations only from the stabilized Evidence Set.

## Result

| Area | Result |
|---|---|
| Data Provider Validation | PASS |
| Source validation | PASS |
| Evidence Set Construction | PASS |
| Blocking errors | None |
| Historical namespace touched | No |
| Historical expected values used | No |

## Main Evidence

- Period: 2026-04-18 to 2026-06-30.
- Total leads: 1329.
- Total A/B leads: 399.
- Total spend across signals: 1406.25 EUR.
- Commercial spend: 875.85 EUR.
- Matched commercial spend: 873.65 EUR.
- Matched leads: 1187.
- Matched A/B leads: 346.
- Matched cost per A/B lead: 2.53 EUR.

## Interpretation

The canonical model produces a stable commercial matched baseline. It also shows that quality volume outside matched commercial coverage is material enough to keep visible, while spend-only commercial residual is not economically material in this execution.

## Limitations

- No sales conversion or revenue outcome is included.
- No creative causality is inferred.
- No historical output is used as a benchmark.
- Future PCI executions must use their own namespace.
