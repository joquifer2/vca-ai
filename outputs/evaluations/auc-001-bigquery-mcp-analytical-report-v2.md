# AUC-001 BigQuery MCP Analytical Report v2

## Executive answer

From the authorized MCP evidence available through 2026-06-30, Meta Ads is buying meaningful lead volume, but not yet a clearly improving quality mix. The account produced 1321 leads from 2026-04-18 to 2026-06-30. Of those, 394 were FARO-qualified A/B leads, a 29.83% qualified rate.

Volume scaled strongly into June, but quality stayed flat around 30%. This means the current media system is scaling quantity more than it is improving lead quality. The strongest business reading is: keep buying the volume that produces A/B leads, but govern optimization by qualified lead economics and ticket readiness, not form submissions.

No historical reports, prior Knowledge Sets, Recommendation Sets, Presentations, or evaluations were used as analytical sources.

## What was analyzed

- Period: 2026-04-18 to 2026-06-30.
- Cutoff: 2026-06-30.
- Tables:
  - `datamart-vca-494114.intermediate.int_faro_lead_scoring`
  - `datamart-vca-494114.marts.fct_lead_enriched`
  - `datamart-vca-494114.marts.fct_spend`
- Qualified lead definition: `lead_tier IN ('A','B')`.
- Execution path: BigQuery MCP Server only.

## Core evidence

| Metric | Value |
| --- | ---: |
| Leads | 1321 |
| A/B qualified leads | 394 |
| Qualified rate | 29.83% |
| Tier A | 57 |
| Tier B | 337 |
| Non A/B or unknown | 927 |
| Ticket-ready leads | 175 |
| Ticket-ready rate | 13.25% |
| Total spend | 1406.23 EUR |
| COMMERCIAL spend | 875.83 EUR |
| ATTENTION + ACTIVATION spend | 530.40 EUR |

Monthly movement:

| Month | Leads | A/B leads | A/B rate | Spend EUR |
| --- | ---: | ---: | ---: | ---: |
| Apr 2026 partial from 04-18 | 179 | 54 | 30.17% | 209.19 |
| May 2026 | 369 | 111 | 30.08% | 389.98 |
| Jun 2026 | 773 | 229 | 29.62% | 807.06 |

The volume doubled from May to June, and qualified leads also doubled. However, the quality rate did not improve. June bought more qualified leads because it bought more leads overall.

## Coverage and join quality

The raw `ad_id` fields do not join directly:

| Join state | Raw ad_id | Normalized ad_id |
| --- | ---: | ---: |
| matched | 0 | 13 |
| lead_only | 13 | 0 |
| spend_only | 23 | 10 |

The mismatch is caused by the lead-side `ad_id` prefix `ag:`. After normalizing that prefix away, all lead ad IDs match spend ad IDs, while 10 spend-side ads remain spend-only.

This matters: without normalization, the analysis would incorrectly say spend and leads cannot be connected.

## Spend by signal

| Signal | Spend EUR | Share |
| --- | ---: | ---: |
| COMMERCIAL | 875.83 | 62.28% |
| ATTENTION | 308.54 | 21.94% |
| ACTIVATION | 221.86 | 15.78% |

Commercial spend is the main lead-quality universe. Attention and activation spend should be reviewed separately because those signals do not represent the same business intent.

On normalized commercial spend ads:

- Leads: 1179.
- A/B qualified leads: 341.
- Share of all leads: 89.25%.
- Share of all A/B leads: 86.55%.
- Commercial CPL on this matched commercial universe: 0.74 EUR.
- Commercial cost per A/B lead: 2.57 EUR.

## Campaign reading

| Campaign | Leads | A/B leads | A/B rate | Ticket-ready | Ticket-ready rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| `[META]_[CLP]_[CAPTACIÓN]_[ABO]` | 1179 | 341 | 28.92% | 153 | 12.98% |
| `[META]_[CLP]_[RTG]_[CBO]` | 142 | 53 | 37.32% | 22 | 15.49% |

Capture produces most qualified volume. Retargeting produces a better quality mix, but with much smaller scale. The right action is not to move everything to RTG; it is to protect RTG as a quality lever and improve capture filtering.

## Ad-level reading

The two largest lead producers are also the two main commercial spend ads:

| Ad | Leads | A/B leads | A/B rate | Ticket-ready | Spend EUR |
| --- | ---: | ---: | ---: | ---: | ---: |
| ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1 | 640 | 187 | 29.22% | 76 | 468.06 |
| ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1 | 359 | 101 | 28.13% | 41 | 245.84 |

Together, they produce 999 leads and 288 A/B leads: 73.76% of all leads and 73.10% of all A/B leads. They are the current commercial engine, but they do not outperform the account quality rate by much. They are good volume bases, not yet decisive quality breakthroughs.

Promising filter-oriented assets:

| Ad | Leads | A/B leads | A/B rate | Note |
| --- | ---: | ---: | ---: | --- |
| FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1 | 53 | 19 | 35.85% | stronger quality, modest volume |
| FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1, RTG | 118 | 42 | 35.59% | stronger quality, RTG |
| FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1, Captacion | 19 | 10 | 52.63% | very small base |

Underperforming commercial quality asset:

| Ad | Leads | A/B leads | A/B rate | Spend EUR |
| --- | ---: | ---: | ---: | ---: |
| ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1 | 67 | 8 | 11.94% | 50.01 |

## Interpretation

The current system is not just noise: 394 A/B leads and 175 ticket-ready leads are real commercial signal. But 70.17% of leads are not A/B or are unknown, so raw volume still contains a lot of weak demand.

The strongest pattern is quality concentration in filter-oriented messaging. Ads that force the user to self-select around tickets, scarcity, or travel readiness show better A/B rates than the largest emotional/identity volume ads. The account should therefore treat filter mechanics as the next optimization frontier.

## Recommendations

1. Govern performance by A/B qualified leads and ticket-ready leads, not raw lead count.
2. Keep COMMERCIAL spend separated from ATTENTION and ACTIVATION in reporting.
3. Normalize `ad_id` before any cost-quality join.
4. Protect RTG as a quality lever and scale it cautiously.
5. Keep the two high-volume commercial winners live while testing variants.
6. Add stronger filter mechanics to capture creatives.
7. Do not scale BoriWine as a commercial-quality winner without a revised hypothesis.

## Limitations

- No impressions, clicks, CTR, CPC, CPM, or reach were available because `fct_performance_daily` is not allowlisted.
- `dim_campaign_signal` is not allowlisted, so campaign signal is taken only from `fct_spend`.
- Spend-only ads have no observable lead quality in the authorized lead tables.
- Creative asset metadata is unavailable.
- Several alternate query shapes failed MCP dry-run validation; only successful query outputs were used as metrics.
- Downstream CRM/sales outcomes are not available in the authorized tables.

## Final classification

`PASS WITH OBSERVATIONS`

The AUC-001 run completed end to end through BigQuery MCP with canonical artifacts and traceable evidence. The observations are due to missing referenced presentation policy files, allowlist-limited tables, and rejected alternate query shapes during MCP dry-run validation.
