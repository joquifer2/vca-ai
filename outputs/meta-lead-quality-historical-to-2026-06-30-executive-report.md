# Informe ejecutivo - Calidad de leads Meta Ads hasta 2026-06-30

## Validacion de alcance

La solicitud actual queda canonicalizada como analisis historico completo disponible hasta el 30 de junio de 2026.

No se reutiliza el periodo de la ejecucion mensual previa. El inicio del periodo se resuelve desde la evidencia disponible en BigQuery.

| Campo | Valor aplicado |
|---|---|
| Periodo analizado | 2026-04-18 a 2026-06-30 |
| Canal | Meta Ads / Meta Lead Ads |
| Leads incluidos | `source_system = 'meta_lead_ads'`, `is_organic = false`, `lead_id` valido, `ad_id` valido |
| Gasto incluido | `source_system = 'meta_ads'`, `campaign_signal = 'COMMERCIAL'` |
| Definicion de lead cualificado | Lead Tier A o B, segun criterio FARO usado por AUC-001 |
| Audiencia | Direccion |
| Fuente principal | BigQuery: `datamart-vca-494114.marts.fct_lead_enriched` y `datamart-vca-494114.marts.fct_spend` |

## Resumen ejecutivo

Entre el 18 de abril y el 30 de junio de 2026, Meta Lead Ads genero 1.319 leads validos en el modelo analizado. De ellos, 390 fueron cualificados A/B, lo que supone una tasa de cualificacion del 29,6%.

El gasto comercial emparejado en el modelo asciende a 875,83 EUR. El coste medio preparado por lead es 0,66 EUR y el coste por lead cualificado A/B es 2,25 EUR. Estos importes deben leerse dentro del modelo de cobertura aprobado, no como una atribucion universal fuera de las tablas consultadas.

La senal de calidad esta concentrada: dos referencias de anuncio explican 286 leads cualificados A/B, el 73,3% del total cualificado historico. La referencia principal, `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`, concentra 640 leads, 185 cualificados A/B y 468,06 EUR de gasto.

La lectura por campana debe mantenerse separada por cobertura. CAPTACION/ABO aparece como evidencia `matched`, con gasto y calidad emparejados. RTG/CBO aparece como `lead_only`, con calidad de lead pero sin gasto comercial emparejado en el modelo aprobado. Esto no prueba ausencia de gasto fuera del modelo; solo limita la lectura economica disponible.

## Evidencia principal

### Totales por cobertura

| Cobertura | Anuncios | Leads | Cualificados A/B | Tasa A/B | Gasto | Coste por cualificado A/B |
|---|---:|---:|---:|---:|---:|---:|
| Total modelo | 15 | 1.319 | 390 | 29,6% | 875,83 EUR | 2,25 EUR |
| Matched | 8 | 1.179 | 339 | 28,8% | 873,63 EUR | 2,58 EUR |
| Lead only | 5 | 140 | 51 | 36,4% | 0,00 EUR | No interpretable como eficiencia |
| Spend only | 2 | 0 | 0 | No aplica | 2,20 EUR | No aplica |

### Evolucion mensual

| Mes | Cobertura | Leads | Cualificados A/B | Tasa A/B | Gasto | Coste por cualificado A/B |
|---|---|---:|---:|---:|---:|---:|
| 2026-04 | Matched | 179 | 54 | 30,2% | 146,29 EUR | 2,71 EUR |
| 2026-05 | Matched | 320 | 94 | 29,4% | 232,98 EUR | 2,48 EUR |
| 2026-05 | Lead only | 48 | 16 | 33,3% | 0,00 EUR | No interpretable como eficiencia |
| 2026-06 | Matched | 680 | 191 | 28,1% | 494,36 EUR | 2,59 EUR |
| 2026-06 | Lead only | 92 | 35 | 38,0% | 0,00 EUR | No interpretable como eficiencia |
| 2026-06 | Spend only | 0 | 0 | No aplica | 2,20 EUR | No aplica |

### Campanas y conjuntos

| Campana | Conjunto | Cobertura | Leads | Cualificados A/B | Tasa A/B | Gasto | Coste por cualificado A/B |
|---|---|---|---:|---:|---:|---:|---:|
| `[META]_[CLP]_[CAPTACION]_[ABO]` | `[PR]_[NATIVE FORM]_[AVG+]_[ISLA]` | matched | 1.179 | 339 | 28,8% | 873,63 EUR | 2,58 EUR |
| `[META]_[CLP]_[RTG]_[CBO]` | `[RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA]` | lead_only | 140 | 51 | 36,4% | 0,00 EUR | No interpretable como eficiencia |
| UNKNOWN | UNKNOWN | spend_only | 0 | 0 | No aplica | 2,20 EUR | No aplica |

### Principales referencias de anuncio

| Referencia de anuncio | Cobertura | Leads | Cualificados A/B | Tasa A/B | Gasto | Coste por cualificado A/B |
|---|---|---:|---:|---:|---:|---:|
| `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1` | matched | 640 | 185 | 28,9% | 468,06 EUR | 2,53 EUR |
| `ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1` | matched | 359 | 101 | 28,1% | 245,84 EUR | 2,43 EUR |
| `FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1` | lead_only | 116 | 40 | 34,5% | 0,00 EUR | No interpretable como eficiencia |
| `FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1` | matched | 53 | 19 | 35,8% | 48,96 EUR | 2,58 EUR |
| `FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1` | matched | 19 | 10 | 52,6% | 25,16 EUR | 2,52 EUR |

## Lectura ejecutiva

### Hechos observables

- El historico disponible empieza el 18 de abril de 2026 y llega hasta el 30 de junio de 2026.
- La captacion total modelada es de 1.319 leads validos, todos procedentes de Meta Lead Ads no organico.
- El 29,6% de los leads quedan clasificados como A/B.
- El 84,6% de los leads estan en cobertura `matched`, donde existe tanto evidencia de lead como gasto comercial emparejado.
- El 10,6% de los leads estan en `lead_only`; aportan lectura de calidad, pero no lectura economica emparejada.
- El gasto `spend_only` es pequeno, 2,20 EUR, pero debe mantenerse visible por trazabilidad.

### Interpretacion

La calidad global es estable en torno al 29%-30% cuando se observa la evidencia `matched` por mes. Junio aporta mas volumen, pero no mejora la tasa de cualificacion frente a abril y mayo; el incremento parece venir principalmente por escala de captacion, no por una mejora clara de calidad relativa.

La mayor parte del valor historico esta concentrada en pocas referencias de anuncio. Esto simplifica la lectura ejecutiva, pero tambien crea dependencia: si los mejores anuncios pierden rendimiento, el sistema podria resentirse rapidamente.

RTG/CBO muestra una tasa A/B superior en `lead_only`, pero no debe compararse economicamente contra CAPTACION/ABO porque el gasto no esta emparejado en el modelo. La senal es prometedora como calidad de leads, no como eficiencia economica demostrada.

Facebook muestra una tasa A/B superior a Instagram en leads agregados, 31,0% frente a 26,6%. Esta diferencia es util como senal de lectura, aunque no debe convertirse por si sola en una recomendacion de presupuesto sin cruzarla con gasto y cobertura.

La variable `ticket_status` confirma que el criterio FARO esta alineado con intencion declarada: los leads con `tiene_billetes` alcanzan 89,0% de cualificacion A/B, los de `en_proceso` 60,8%, y `solo_mirando` 5,7%.

## Recomendaciones para Direccion

1. Mantener la lectura de eficiencia principalmente sobre la cobertura `matched`.
   La base mas robusta para decisiones economicas es CAPTACION/ABO, donde existen leads, calidad y gasto emparejados.

2. Proteger y monitorizar las dos referencias que concentran la mayor parte del resultado.
   `ViajeSinEstres_AlivioEmocional` y `ViajaComoInvitado_Identidad` explican el 73,3% de los cualificados A/B historicos. Conviene tratarlas como activos criticos de aprendizaje y no solo como piezas tacticas.

3. Analizar RTG/CBO como senal de calidad separada, no como eficiencia de gasto.
   Sus 140 leads y 51 cualificados A/B son relevantes, pero la falta de gasto emparejado impide concluir coste por cualificado o rentabilidad.

4. Revisar la cobertura de atribucion por campana/conjunto antes de elevar decisiones presupuestarias.
   El modelo permite buen razonamiento a nivel `ad_id`, pero la atribucion economica por campana/conjunto sigue condicionada por la disponibilidad de metadata en gasto.

5. Priorizar aprendizajes sobre intencion declarada del viajero.
   La diferencia entre `tiene_billetes`, `en_proceso` y `solo_mirando` es muy marcada. Direccion deberia usar esta lectura para separar volumen barato de demanda comercialmente util.

6. No basar decisiones de Direccion en CTR, impresiones o clicks en esta ejecucion.
   Esas metricas no forman parte del modelo historico validado para este informe.

## Limitaciones

- La evidencia no incluye impresiones, clicks, CTR ni metadata creativa visual.
- La calidad se calcula con `lead_tier IN ('A','B')`; no se usa una columna independiente de `qualified_leads`.
- `campaign_signal = COMMERCIAL` aplica al lado de gasto, no directamente a cada fila de lead.
- Las filas `lead_only` no deben interpretarse como gasto cero real, sino como ausencia de gasto emparejado en el modelo.
- Las filas `spend_only` no permiten calcular coste por lead ni tasa de calidad.
- La exclusion de duplicados y registros de prueba no esta explicitamente mapeada como campo en la consulta; se conserva la restriccion de `lead_id` valido.

## Trazabilidad

Contexto consultado:

- `analytical_use_cases/meta_lead_quality_analysis.md`
- `docs/context_refs.md`
- `knowledge/client/ccd.md`
- `.github/skills/meta-lead-quality-analysis/SKILL.md`
- `docs/handoffs/auc-001-data-contract.md`
- `docs/handoffs/auc-001-analytical-contract.md`
- `docs/handoffs/auc-001-evidence-set.md`

Consultas ejecutadas:

- Validacion de esquema en `marts.INFORMATION_SCHEMA.COLUMNS`.
- Validacion de rango disponible en `marts.fct_lead_enriched` y `marts.fct_spend`.
- Agregacion historica por cobertura `matched`, `lead_only`, `spend_only`.
- Agregacion mensual.
- Agregacion por campana/conjunto.
- Agregacion por referencia de anuncio.
- Agregacion auxiliar por plataforma y `ticket_status`.

Fecha de preparacion: 2026-07-13.
