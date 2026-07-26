# AUC-001 Lead Quality Analysis - cutoff 2026-06-30

## Scope

Period: 2026-04-18 to 2026-06-30. Evidence acquired only through BigQuery MCP Server from allowlisted tables.

## Executive Reading

VCA is generating scale: 1,329 Meta leads by the cutoff. The quality picture is mixed: 397 leads are A/B (29.9%) and only 58 are Tier A (4.4%). That means the system is buying useful qualified volume, but most captured volume is still C/D noise.

The main explanatory signal is not the ad alone. Declared travel maturity is the strongest separator: leads with tickets already bought produce 157 A/B from 177 leads and 47 Tier A leads, while solo-looking leads produce only 48 A/B from 838 leads and no Tier A.

## Cost-Quality

Commercial matched spend is 873.65. On the commercial matched universe, CPL is 0.74, cost per A/B lead is 2.54 and cost per Tier A lead is 18.20.

Observed activation matched spend is 221.18 for 142 leads, 53 A/B and 10 Tier A. Activation has better quality density than cold capture, but with lower scale and higher observed cost per A/B lead. Under FARO, this should be read as activation/retargeting behavior, not as a universal KPI race against commercial capture.

## Concentration

Two commercial ads dominate the system:

- ViajeSinEstres_AlivioEmocional: 643 leads, 187 A/B, 23 Tier A, 468.06 spend.
- ViajaComoInvitado_Identidad: 359 leads, 101 A/B, 17 Tier A, 245.84 spend.

Together they generate 75.4% of all leads and 72.5% of A/B leads. This is useful scale, but it creates dependency.

FiltroBilletes variants show stronger quality density in smaller samples. The RTG FiltroBilletes ad produced 118 leads, 42 A/B and 9 Tier A. The cold commercial FiltroBilletes AutoSegmentacion ad produced 58 leads, 22 A/B and 3 Tier A. These are promising signals, not definitive creative winners.

## Temporal Pattern

Volume rose sharply into June: 184 leads in April partial coverage, 369 in May, 776 in June. Quality share did not rise with volume: A/B rate was about 31.0% in April, 30.1% in May and 29.5% in June. Tier A stayed small: 8, 19 and 31 respectively.

Weekly interpretation is partial because boundary weeks and some May weeks are incomplete. The week of 2026-06-15 had the strongest full-week A/B count in the evidence: 75 A/B from 194 leads.

## Recommendations

1. Test increased exposure to high-intent filters (tickets and near-term travel) while preserving a volume guardrail. Success metric: A/B rate and cost_per_ab_commercial_matched.
2. Run a separate FiltroBilletes/mature-intent experiment by FARO layer, without comparing ATTENTION, ACTIVATION and COMMERCIAL as a single KPI ranking.
3. Add a recurring matched/lead_only/spend_only evidence view by normalized ad_id and campaign signal.
4. Keep CRM/revenue claims as not_available until GIAV or another governed commercial source is authorized and reconciled.

## Limitations

No revenue, CRM opportunity or sales conversion evidence was available in the authorized scope. Creative causality remains UNKNOWN. Weekly trend is partial. Attention spend is not evaluated as direct lead efficiency under FARO constraints.
