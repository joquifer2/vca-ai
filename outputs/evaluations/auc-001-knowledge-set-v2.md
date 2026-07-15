# AUC-001 Knowledge Set v2

## Finding 1 - The account is buying volume, but quality is stable rather than improving

Evidence:

- Leads increased from 179 in partial April to 369 in May and 773 in June.
- Qualified A/B leads increased from 54 to 111 to 229.
- Qualified rate stayed almost flat: 30.17%, 30.08%, 29.62%.

Interpretation:

The June scale-up produced more qualified leads in absolute terms, but did not improve the quality mix. The system bought more of the same distribution, not a materially better lead profile.

Confidence: high.

Limitations:

- April is partial from 2026-04-18.
- No impressions/clicks/CTR are available.

Business implication:

Optimization should not be judged by lead volume alone. Future budget increases should be gated by cost per A/B lead and ticket-ready rate, not by raw CPL.

## Finding 2 - Only about three in ten leads are FARO-qualified

Evidence:

- 1321 leads through cutoff.
- 57 Tier A and 337 Tier B leads.
- 394 A/B qualified leads, or 29.83%.
- 927 leads are non A/B or unknown.

Interpretation:

The current Meta lead intake is still dominated by lower-quality or unknown-quality leads. FARO creates enough signal to distinguish useful leads, but the media system is not yet concentrated around qualified demand.

Confidence: high.

Limitations:

- The analysis relies on `lead_tier` as the official FARO quality signal.
- Downstream sales outcomes are not available in the authorized evidence.

Business implication:

The primary optimization language should be A/B qualified leads and ticket readiness, not form submissions.

## Finding 3 - Commercial spend is the main useful spend universe, but not the whole spend universe

Evidence:

- Total spend: 1406.23 EUR.
- COMMERCIAL spend: 875.83 EUR, 62.28% of spend.
- ATTENTION + ACTIVATION spend: 530.40 EUR, 37.72% of spend.
- Normalized commercial ads account for 1179 leads and 341 A/B leads.

Interpretation:

Most leads and qualified leads are tied to ads that also appear in the commercial spend universe, but more than one third of spend sits outside COMMERCIAL. Those non-commercial signals may be legitimate upper/mid-funnel investment, but they should not be evaluated with the same success metric as commercial capture.

Confidence: medium-high.

Limitations:

- Campaign signal is available only from spend-side evidence.
- `dim_campaign_signal` is not allowlisted for independent signal validation.

Business implication:

Budget review should separate commercial capture from attention/activation rather than blending all spend into one CPL.

## Finding 4 - Normalizing ad IDs changes the coverage conclusion completely

Evidence:

- Raw join: matched 0, lead_only 13, spend_only 23.
- Normalized join after removing `ag:` from lead `ad_id`: matched 13, lead_only 0, spend_only 10.

Interpretation:

The data is analytically joinable, but only if the lead-side `ad_id` format is normalized. Without that normalization, the analysis would falsely conclude that spend and leads do not connect.

Confidence: high.

Limitations:

- Normalization is an analytical transformation in the query, not a source-model correction.

Business implication:

Any operational reporting or future automated recommendation logic must normalize ad IDs consistently before calculating cost-quality efficiency.

## Finding 5 - Retargeting has a better quality mix but much lower volume

Evidence:

- Captacion ABO: 1179 leads, 341 A/B, 28.92% A/B rate.
- RTG CBO: 142 leads, 53 A/B, 37.32% A/B rate.
- Ticket-ready rate: 12.98% for Captacion, 15.49% for RTG.

Interpretation:

Retargeting appears more selective, with better A/B and ticket-ready concentration, but its volume is small compared with capture.

Confidence: medium-high.

Limitations:

- Spend by campaign could not be robustly joined in one approved query; campaign spend allocation is inferred only from allowed spend/ad cuts.

Business implication:

RTG should be protected as a quality lever, while capture needs stronger filtering or creative/targeting refinement.

## Finding 6 - Two commercial ads carry most volume and qualified output

Evidence:

- ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1: 640 leads, 187 A/B, 76 ticket-ready, 468.06 EUR spend.
- ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1: 359 leads, 101 A/B, 41 ticket-ready, 245.84 EUR spend.
- Together: 999 leads and 288 A/B leads, 73.76% of all leads and 73.10% of all A/B leads.

Interpretation:

The current commercial engine is concentrated in two creatives. They produce volume and qualified leads at similar quality rates, but concentration risk is high.

Confidence: high for volume and quality; medium for efficiency because cost is traced from separate approved spend query.

Limitations:

- Creative asset metadata is unavailable.
- The ad-level cost-quality table query was rejected in one combined form, so efficiency is assembled from independently approved lead and spend cuts.

Business implication:

Scaling decisions should test controlled variants around these two winning concepts rather than spreading budget evenly across all assets.

## Finding 7 - Some lower-volume filter-oriented ads show stronger quality concentration

Evidence:

- FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1: 53 leads, 19 A/B, 35.85%.
- FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1 in RTG: 118 leads, 42 A/B, 35.59%.
- FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1 in Captacion: 19 leads, 10 A/B, 52.63%.

Interpretation:

Filter-oriented messaging appears to increase quality concentration, especially when tied to scarcity or self-segmentation. The evidence is promising but not uniformly high-volume.

Confidence: medium.

Limitations:

- Smaller samples, especially the 19-lead capture variant.
- No click/impression denominator.

Business implication:

The best next experiments should borrow filter mechanics from these ads while preserving enough reach to avoid shrinking the qualified lead pool.

## Finding 8 - BoriWine creative underperforms on quality concentration

Evidence:

- ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1: 67 leads, 8 A/B, 11.94%.
- Spend: 50.01 EUR in COMMERCIAL.

Interpretation:

This creative produces volume but a weak qualified mix relative to the account average of 29.83%.

Confidence: medium-high.

Limitations:

- Downstream sales value is unavailable.
- The creative could still serve brand or product discovery goals, but it should not be treated as strong commercial lead-quality evidence.

Business implication:

It should not receive incremental commercial budget without a revised filter, offer, or audience hypothesis.
