# AUC-001 Evidence Set v2

## Evidence scope

- Real analyzed period: 2026-04-18 to 2026-06-30.
- Cutoff: 2026-06-30.
- Authorized data only: BigQuery MCP Server.
- Total MCP calls in this execution: 34.
- `discover_metadata` calls: 4.
- `query_read_only` calls: 30.
- Successful analytical queries: 15.
- Rejected diagnostic/alternate query attempts: 15.

Rejected attempts are preserved because they affect coverage and explain why some cuts were not used. No rejected query contributes a metric.

## Metadata discovery

| Request ID | Scope | Resource | Status | Policy | Trace |
| --- | --- | --- | --- | --- | --- |
| `codex-vca-auc001-v2-meta-project-20260715-001` | datasets | `datamart-vca-494114` | success | allow | `trc-bc47b42930454fec9299376cded1d8d0` |
| `codex-vca-auc001-v2-meta-intermediate-schema-20260715-001` | schema | `intermediate.int_faro_lead_scoring` | success | allow | `trc-77780fee778e430a832f88160076ef59` |
| `codex-vca-auc001-v2-meta-leads-schema-20260715-001` | schema | `marts.fct_lead_enriched` | success | allow | `trc-c39986c2601840728e18440eb13d937f` |
| `codex-vca-auc001-v2-meta-spend-schema-20260715-001` | schema | `marts.fct_spend` | success | allow | `trc-7aa891c3a35b4044ac7e3877ea3c3b21` |

Discovered datasets: `intermediate`, `marts`.

## Query log

Execution contexts used:

```yaml
intermediate:
  project_id: datamart-vca-494114
  dataset_id: intermediate
  max_bytes_billed: 1073741824
marts:
  project_id: datamart-vca-494114
  dataset_id: marts
  max_bytes_billed: 1073741824
```

Successful queries used in metrics:

| ID | Purpose | Tables | SQL summary | Status | Bytes | Trace |
| --- | --- | --- | --- | --- | ---: | --- |
| q001 | scoring coverage | `intermediate.int_faro_lead_scoring` | min/max/count lead dates up to cutoff | success | 41801 | `trc-3b467af730ae40e088a5edda21d5b4b4` |
| q002 | marts coverage | `marts.fct_lead_enriched`, `marts.fct_spend` | min/max/count coverage by table | success | 349787 | `trc-a439a1cd649143f8915e6082debe9c14` |
| q004 | spend by signal | `marts.fct_spend` | spend grouped by `campaign_signal` | success | 388507 | `trc-6889781df1a74564b73c7d7416bb23ef` |
| q010 | tier counts | `intermediate.int_faro_lead_scoring` | count tier A, tier B, non A/B or unknown | success | 16500 | `trc-93c012b08583417eba1ca54ecd9e4445` |
| q011 | ticket readiness | `intermediate.int_faro_lead_scoring` | count `tiene_billetes` true/false/unknown | success | 13500 | `trc-6cec4aa795254618947dd1ce28c5d33f` |
| q013 | monthly lead/quality pivot | `intermediate.int_faro_lead_scoring` | Apr/May/Jun leads and A/B leads | success | 16500 | `trc-6326771ea1fb43038ca46822814079cc` |
| q014 | monthly spend pivot | `marts.fct_spend` | Apr/May/Jun spend and commercial/non-commercial spend | success | 205182 | `trc-bd4307b28da74668980f3f08841f16b3` |
| q015 | raw ad_id coverage | `intermediate.int_faro_lead_scoring`, `marts.fct_spend` | raw ad_id full outer join coverage | success | 251824 | `trc-1e25d1026e0b40868b728b9823e2d8eb` |
| q016 | raw commercial ad quality | same | leads on raw commercial spend ads | success | 344178 | `trc-6e7f68958e434b2e95a4dcd543a8c145` |
| q017 | top lead ads | `intermediate.int_faro_lead_scoring` | top ads by leads with A/B and tickets | success | 182387 | `trc-91c61a25783b439bb72749e59edce082` |
| q018 | top spend ads | `marts.fct_spend` | top ads by spend and signal | success | 748602 | `trc-f468cdf2290f47e093629dab1860d12b` |
| q020 | normalized ad_id coverage | same | join after removing `ag:` lead prefix | success | 251824 | `trc-12c5479993c24c058b3e59d707b8920d` |
| q021b | normalized commercial quality | same | leads and A/B leads on commercial spend ads | success | 344178 | `trc-5e9e04a4a2364750af8ef941b6cc15fc` |
| q023 | mapping coverage | `intermediate.int_faro_lead_scoring` | mapped input flags and unmapped reason count | success | 22500 | `trc-f1761bf2df7a4af4a056f4d25f711584` |
| q024 | campaign quality | `intermediate.int_faro_lead_scoring` | leads, A/B, tickets by campaign | success | 100208 | `trc-ad1c62efd79641babda7f7aa70f22572` |

Representative SQL patterns:

```sql
SELECT COUNTIF(lead_tier = 'A') AS tier_a_rows,
       COUNTIF(lead_tier = 'B') AS tier_b_rows,
       COUNTIF(lead_tier NOT IN ('A','B') OR lead_tier IS NULL) AS non_ab_or_unknown_rows
FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring`
WHERE lead_date <= DATE '2026-06-30';
```

```sql
WITH lead_ads AS (
  SELECT DISTINCT REPLACE(ad_id, 'ag:', '') AS ad_id_norm
  FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring`
  WHERE lead_date <= DATE '2026-06-30' AND ad_id IS NOT NULL
),
spend_ads AS (
  SELECT DISTINCT ad_id AS ad_id_norm
  FROM `datamart-vca-494114.marts.fct_spend`
  WHERE spend_period <= DATE '2026-06-30' AND ad_id IS NOT NULL
)
SELECT COUNTIF(lead_ads.ad_id_norm IS NOT NULL AND spend_ads.ad_id_norm IS NOT NULL) AS matched_ad_ids,
       COUNTIF(lead_ads.ad_id_norm IS NOT NULL AND spend_ads.ad_id_norm IS NULL) AS lead_only_ad_ids,
       COUNTIF(lead_ads.ad_id_norm IS NULL AND spend_ads.ad_id_norm IS NOT NULL) AS spend_only_ad_ids
FROM lead_ads FULL OUTER JOIN spend_ads USING (ad_id_norm);
```

Rejected attempts:

| Request IDs | Error | Interpretation |
| --- | --- | --- |
| q003, q003b, q003c, q003d, q003e, q003f, q005, q006, q007, q008, q009, q012, q019, q022 | `ERR_DRY_RUN_FAILED` | Alternate quality/grouping queries failed during cost validation. Metrics were recovered with simpler approved query shapes. |
| q021 | `ERR_SCOPE_DENIED` | A combined scalar/cross-dataset formulation exceeded the accepted scope parser. It was replaced by q021b without widening scope. |

## Coverage

Temporal coverage:

| Source | Min date | Max date in table | Rows total | Rows until cutoff |
| --- | --- | --- | ---: | ---: |
| `intermediate.int_faro_lead_scoring` | 2026-04-18 | 2026-07-15 | 1500 | 1321 |
| `marts.fct_lead_enriched` | 2026-04-18 | 2026-07-15 | 1500 | 1321 |
| `marts.fct_spend` | 2026-04-18 | 2026-07-01 | 7333 | 7332 |

Ad join coverage:

| Method | matched | lead_only | spend_only | UNKNOWN / note |
| --- | ---: | ---: | ---: | --- |
| Raw `ad_id` | 0 | 13 | 23 | Raw lead IDs include `ag:` prefix; spend IDs do not. |
| Normalized lead `ad_id` with `REPLACE(ad_id, 'ag:', '')` | 13 | 0 | 10 | Analytical join is usable after normalization. Spend-only ads remain without lead rows. |

Coverage states preserved:

- `matched`: 13 normalized ad_ids.
- `lead_only`: 0 normalized ad_ids.
- `spend_only`: 10 normalized ad_ids.
- `UNKNOWN`: creative metadata, impressions, clicks, CTR, same-day attribution, and spend-only lead quality.

## Base metrics

Lead volume and quality through 2026-06-30:

| Metric | Value |
| --- | ---: |
| Leads | 1321 |
| Qualified leads A/B | 394 |
| Qualified rate | 29.83% |
| Tier A | 57 |
| Tier B | 337 |
| Non A/B or unknown | 927 |
| Leads with tickets | 175 |
| Ticket-ready rate | 13.25% |

Spend through 2026-06-30:

| Signal | Spend EUR | Rows | Distinct ads |
| --- | ---: | ---: | ---: |
| COMMERCIAL | 875.83 | 7099 | 10 |
| ATTENTION | 308.54 | 141 | 7 |
| ACTIVATION | 221.86 | 92 | 6 |
| Total | 1406.23 | 7332 | 23 |

Monthly movement:

| Month | Leads | Qualified A/B | Qualified rate | Spend EUR |
| --- | ---: | ---: | ---: | ---: |
| 2026-04 partial from 04-18 | 179 | 54 | 30.17% | 209.19 |
| 2026-05 | 369 | 111 | 30.08% | 389.98 |
| 2026-06 | 773 | 229 | 29.62% | 807.06 |

Commercial spend ads after normalized matching:

| Metric | Value |
| --- | ---: |
| Leads on commercial spend ads | 1179 |
| Qualified A/B on commercial spend ads | 341 |
| Share of all leads on commercial spend ads | 89.25% |
| Share of all A/B leads on commercial spend ads | 86.55% |
| Commercial spend EUR | 875.83 |
| Commercial CPL on matched commercial lead universe | 0.74 |
| Commercial cost per A/B qualified lead | 2.57 |

Campaign quality:

| Campaign | Leads | A/B qualified | A/B rate | Ticket-ready | Ticket-ready rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| `[META]_[CLP]_[CAPTACIÓN]_[ABO]` | 1179 | 341 | 28.92% | 153 | 12.98% |
| `[META]_[CLP]_[RTG]_[CBO]` | 142 | 53 | 37.32% | 22 | 15.49% |

Top lead ads:

| Ad | Leads | A/B | A/B rate | Ticket-ready |
| --- | ---: | ---: | ---: | ---: |
| ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1 | 640 | 187 | 29.22% | 76 |
| ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1 | 359 | 101 | 28.13% | 41 |
| FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1, RTG | 118 | 42 | 35.59% | 17 |
| ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1 | 67 | 8 | 11.94% | 4 |
| FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1 | 53 | 19 | 35.85% | 11 |
| FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1, Captacion | 19 | 10 | 52.63% | 10 |

Top spend ads:

| Ad | Signal | Spend EUR |
| --- | --- | ---: |
| ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1 | COMMERCIAL | 468.06 |
| MadridNoGoogle_MiedoAPerdida_OrganizacionViaje_Reel_v1 | ATTENTION | 279.69 |
| ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1 | COMMERCIAL | 245.84 |
| FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1 | ACTIVATION | 155.64 |
| ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1 | COMMERCIAL | 50.01 |
| FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1 | COMMERCIAL | 48.96 |

## Limitations and UNKNOWNs

- Raw `ad_id` fields are not directly joinable because lead IDs include an `ag:` prefix. Normalization resolves coverage but should be documented as an analytical transformation.
- `marts.dim_campaign_signal` is not in the allowlist, so signal validation is limited to `fct_spend.campaign_signal`.
- `marts.fct_performance_daily` is not in the allowlist, so impressions, clicks, CTR, CPM, CPC, and funnel rates are unavailable.
- Creative asset metadata is unavailable.
- Spend-only ads have spend and signal but no lead quality in the authorized lead tables.
- `rows_with_unmapped_reason = 1321` while all mapping flags are true. The semantic meaning of `unmapped_reason` requires data model review; it is not used to penalize quality in this analysis.
- Several alternate query shapes were rejected by MCP dry-run validation. The run used only successful MCP outputs for metrics.
