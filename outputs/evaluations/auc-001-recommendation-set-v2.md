# AUC-001 Recommendation Set v2

## Recommendation 1 - Govern spend by qualified lead economics, not raw lead volume

Supporting findings: 1, 2.

Action:

Use A/B qualified leads as the primary commercial optimization metric. Track raw leads only as a volume input, not as the success metric.

Expected impact:

Budget movement becomes aligned with lead usefulness instead of form fill volume.

Priority: high.

Risk:

Short-term apparent CPL may worsen if lower-quality cheap leads are deprioritized.

Next validation:

Continue comparing qualified rate, ticket-ready rate, commercial CPL, and commercial cost per A/B lead in the next reporting window.

## Recommendation 2 - Keep commercial and non-commercial spend separated in reviews

Supporting finding: 3.

Action:

Evaluate COMMERCIAL spend using lead quality and cost per A/B lead. Evaluate ATTENTION and ACTIVATION with their own funnel intent, not as if they were capture campaigns.

Expected impact:

Prevents upper/mid-funnel spend from distorting commercial lead efficiency.

Priority: high.

Risk:

Requires discipline in reporting because the allowlist does not expose `dim_campaign_signal`.

Next validation:

Request or validate a future MCP-safe signal dimension only through governance; do not widen scope during this AUC run.

## Recommendation 3 - Standardize ad_id normalization in analytical logic

Supporting finding: 4.

Action:

For analysis, normalize lead-side `ad_id` by removing `ag:` before joining to spend-side `ad_id`.

Expected impact:

Avoids false `lead_only`/`spend_only` conclusions and enables cost-quality analysis.

Priority: high.

Risk:

If other prefixes appear later, the transformation may need a more general canonical ID rule.

Next validation:

Track raw and normalized coverage states in each AUC-001 rerun.

## Recommendation 4 - Protect retargeting as a quality lever, but scale cautiously

Supporting finding: 5.

Action:

Maintain RTG/CBO presence and test incremental budget only in controlled steps, because the quality rate is higher but the volume base is smaller.

Expected impact:

Improves qualified concentration without assuming RTG can absorb capture-level volume.

Priority: medium-high.

Risk:

Over-scaling retargeting may saturate the audience and degrade quality.

Next validation:

Compare RTG qualified rate and ticket-ready rate after each budget change.

## Recommendation 5 - Build next creative tests from the two high-volume commercial winners

Supporting finding: 6.

Action:

Use `ViajeSinEstres_AlivioEmocional` and `ViajaComoInvitado_Identidad` as base concepts for controlled variants. Keep the original winners live while testing variants.

Expected impact:

Preserves current qualified volume while searching for better quality mix.

Priority: high.

Risk:

Creative fatigue or audience overlap could reduce performance if variants are too similar.

Next validation:

Measure qualified rate, ticket-ready rate, and cost per A/B lead at ad level after normalization.

## Recommendation 6 - Introduce stronger filters into capture creatives

Supporting finding: 7.

Action:

Translate the stronger filter mechanics from `FiltroBilletes` creatives into capture variants: ticket readiness, travel timing, group size, and experience intent.

Expected impact:

May increase qualified concentration while retaining capture scale.

Priority: medium-high.

Risk:

Filtering can reduce raw lead volume; success should be judged on A/B and ticket-ready economics.

Next validation:

Run a controlled creative test against current capture winners and compare A/B rate plus cost per A/B lead.

## Recommendation 7 - Do not scale BoriWine as a commercial quality winner yet

Supporting finding: 8.

Action:

Hold or redesign the BoriWine creative before giving it incremental commercial budget.

Expected impact:

Reduces spend leakage into low-quality commercial lead intake.

Priority: medium.

Risk:

The creative may have product-specific strategic value not visible in the authorized data.

Next validation:

If product strategy requires BoriWine, test a stronger qualification hook and compare against account A/B rate.
