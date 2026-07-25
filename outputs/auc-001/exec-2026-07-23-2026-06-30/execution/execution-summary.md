# Execution Summary - AUC-001 executive report 2026-06-30

## Estado

Entrega generada: `READY_FOR_REVALIDATION`.

No constituye aceptacion final de QA Gate.

## Context Definition estabilizado

| Campo | Valor |
|---|---|
| Objetivo | Generar informe ejecutivo de calidad de leads Meta Ads |
| Modo | Ejecucion completa |
| Periodo | 2026-04-18 a 2026-06-30 |
| Cutoff | 2026-06-30 |
| Regla temporal | La solicitud indicaba solo fecha de corte; el inicio se resolvio desde cobertura MCP autorizada |
| Audiencia | Direccion / decision ejecutiva |
| Data Provider | BigQuery MCP Server |
| Workspace | vca |
| Project ID | datamart-vca-494114 |
| Fuentes autorizadas | marts.fct_lead_enriched; intermediate.int_faro_lead_scoring; marts.fct_spend; marts.dim_campaign_signal |

## Data Provider Validation

Resultado: `PASS`.

Selectores canonicos ejecutados:

- `workspace:vca`
- `dataset:intermediate`
- `dataset:marts`
- `table:intermediate.int_faro_lead_scoring`
- `table:marts.fct_spend`
- `table:marts.fct_lead_enriched`
- `table:marts.dim_campaign_signal`

No se usaron selectores alternativos, prefijos de proyecto, CLI, `bq`, informes historicos ni Evidence Sets previos.

## Evidence Set estabilizado

Metricas principales:

| Campo | Valor |
|---|---:|
| total_leads | 1329 |
| distinct_leads | 1329 |
| tier_a | 58 |
| tier_b | 339 |
| tier_c | 554 |
| tier_d | 378 |
| ab_leads | 397 |
| avg_score | 49.8029 |
| total_spend_all_signals | 1406.250006 |
| commercial_spend | 875.850006 |
| matched_commercial_spend | 873.650006 |
| spend_only_commercial_spend | 2.2 |
| matched_leads | 1187 |
| lead_only_leads | 142 |
| matched_ab_leads | 344 |
| lead_only_ab_leads | 53 |

Coverage reconciliation:

| Estado | Ads | Leads | A/B | Tier A | Spend comercial |
|---|---:|---:|---:|---:|---:|
| matched | 8 | 1187 | 344 | 48 | 873.650006 |
| lead_only | 5 | 142 | 53 | 10 | 0 |
| spend_only | 2 | 0 | 0 | 0 | 2.2 |
| UNKNOWN | 0 | 0 | 0 | 0 | 0 |

Invariantes:

- `commercial_spend = matched_commercial_spend + spend_only_commercial_spend`: PASS.
- `total_leads = matched_leads + lead_only_leads + unknown_leads`: PASS.
- `total_ab_leads = matched_ab_leads + lead_only_ab_leads + unknown_ab_leads`: PASS.
- `tier_a_total = matched_tier_a + lead_only_tier_a + unknown_tier_a`: PASS.

## Knowledge Set estabilizado

1. El volumen escala principalmente en junio, pero la tasa A/B permanece estable cerca del 30%.
2. La calidad se concentra en una minoria A/B; Tier A es reducido y requiere cautela por denominador.
3. La eficiencia matched es baja en coste unitario, pero la decision debe basarse en coste por A/B matched y no en CPL generico.
4. La captacion ABO explica casi todo el volumen; RTG muestra mejor tasa A/B lead-side, pero sin coste comercial matched comparable.
5. Dos anuncios concentran la mayor parte del volumen y de los A/B, creando dependencia operacional.
6. Las respuestas de formulario sobre billetes, fecha e intencion explican mejor la separacion de calidad que la lectura agregada por anuncio.
7. La evidencia permite orientar experimentos de calidad, no afirmar causalidad creativa ni revenue.

Analytical Narrative:

El fenomeno dominante es una tension entre escala y cualificacion: Meta ya compra mucho volumen a coste bajo, pero la calidad incremental no mejora al mismo ritmo que la captacion. La explicacion mas fuerte no esta en una metrica aislada de coste, sino en la combinacion de intencion declarada, claridad de viaje y dependencia de pocos activos de alto volumen. La implicacion estrategica es mover la optimizacion desde "mas leads baratos" hacia "mas senal A/B dentro del volumen existente", manteniendo visibles los limites de revenue, causalidad creativa y comparabilidad semanal.

## Recommendation Set estabilizado

1. Prioridad alta: experimentar con combinaciones de formulario de intencion fuerte.
2. Prioridad alta: proteger activos de volumen, pero condicionar escala a calidad A/B.
3. Prioridad media-alta: revisar activos con spend matched y baja tasa A/B, especialmente BoriWine2026.
4. Prioridad media: tratar RTG como hipotesis prometedora hasta cerrar coste-calidad comparable.
5. Prioridad media: resolver o declarar formalmente el gap CRM/revenue antes de decisiones finales de negocio.

## Presentation

Artefacto materializado:

- `outputs/auc-001/exec-2026-07-23-2026-06-30/executive-report/executive-report.md`

La proyeccion ejecutiva consume el contenido canonico anterior y no introduce evidencia, Knowledge ni recomendaciones nuevas.

