# Informe ejecutivo - Calidad de leads Meta Ads hasta 2026-06-30

## Metadata

| Campo | Valor |
| --- | --- |
| Artifact ID | VCA-AUC-001-EXEC-REPORT-2026-06-30-FRESH |
| Caso analitico | AUC-001 - Meta Lead Quality Analysis |
| Tipo de salida | Informe ejecutivo trazable |
| Fecha de generacion | 2026-07-13 |
| Solicitud | Generar informe ejecutivo de calidad de leads Meta Ads hasta el 30 de junio de 2026, empezando de cero |
| Periodo disponible observado | 2026-04-18 to 2026-06-30 |
| Canal | Meta Ads / Meta Lead Ads |
| Fuente principal | BigQuery CLI sobre tablas publicadas en el Data Contract |
| Estado | Generado desde una nueva consulta de datos; no usa informes anteriores como fuente |

---

## Resumen ejecutivo

El periodo disponible observado hasta el 30 de junio de 2026 cubre desde el 18 de abril de 2026 hasta el 30 de junio de 2026. En ese periodo se registran 1.319 leads paid de Meta Ads, 390 leads cualificados A/B y 875.8300059999967 de inversion comercial.

La tasa global de cualificacion A/B es 0.29567854435178165 y el coste global por lead cualificado A/B es 2.2457179641025555. Estos valores deben leerse como metricas del modelo reconstruido, no como una afirmacion de cobertura universal fuera de las tablas consultadas.

La base mas solida para relacionar calidad e inversion son las 8 referencias de anuncio `matched`, donde hay simultaneamente leads y spend emparejado. Este grupo concentra 1.179 leads, 339 leads cualificados A/B y 873.6300059999967 de inversion, con coste por lead cualificado A/B de 2.5770796637168045.

Hay un bloque `lead_only` con 5 referencias, 140 leads y 51 leads cualificados A/B. Su tasa de cualificacion es superior a la de `matched`, pero no tiene inversion emparejada en el modelo; por tanto, debe analizarse como calidad observada, no como eficiencia economica.

Los dos anuncios con mayor aportacion absoluta de leads cualificados son `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1` y `ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1`. Juntos aportan 286 leads cualificados A/B dentro de `matched`.

---

## Objetivo y alcance

Este informe sintetiza, para Direccion, la calidad de los leads procedentes de Meta Ads en el periodo disponible hasta el 30 de junio de 2026.

| Dimension | Alcance aplicado |
| --- | --- |
| Periodo | 2026-04-18 to 2026-06-30 |
| Canal | Meta Ads / Meta Lead Ads |
| Lead de calidad | `lead_tier IN ('A','B')` |
| Leads incluidos | `lead_id IS NOT NULL` e `is_organic = false` |
| Spend incluido | `campaign_signal = 'COMMERCIAL'` en `fct_spend` |
| Grano primario | `ad_id_norm` |
| Estados de cobertura | `matched`, `lead_only`, `spend_only` |

---

## Datos y cobertura utilizados

### Fuentes consultadas

| Fuente | Uso |
| --- | --- |
| `datamart-vca-494114.marts.fct_lead_enriched` | Leads, `lead_tier`, plataforma y metadata lead-side de campaign/adset/ad |
| `datamart-vca-494114.intermediate.int_faro_lead_scoring` | Referencia FARO/scoring publicada en contexto tecnico |
| `datamart-vca-494114.marts.fct_spend` | Inversion comercial por anuncio |

### Disponibilidad observada

| Fuente | min_date | max_date | Filas hasta 2026-06-30 |
| --- | --- | --- | ---: |
| `fct_lead_enriched` | 2026-04-18 | 2026-06-30 | 1.319 |
| `int_faro_lead_scoring` | 2026-04-18 | 2026-06-30 | 1.319 |
| `fct_spend` | 2026-04-18 | 2026-06-30 | 7.332 |

### Cobertura analitica

| coverage_status | Referencias | Leads | Qualified A/B | Spend | Tasa A/B | Spend / qualified A/B | Lectura ejecutiva |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| matched | 8 | 1.179 | 339 | 873.6300059999967 | 0.2875318066157761 | 2.5770796637168045 | Base principal para decisiones de eficiencia |
| lead_only | 5 | 140 | 51 | 0.0 | 0.36428571428571427 | 0.0 | Calidad observable sin spend emparejado |
| spend_only | 2 | 0 | 0 | 2.200000000000001 | UNKNOWN | UNKNOWN | Spend sin calidad observable |

---

## Principales resultados

1. El modelo reconstruido contiene 15 referencias de anuncio, 1.319 leads y 390 leads cualificados A/B.
2. El 86.92% de los leads cualificados A/B estan en referencias `matched`, donde tambien se concentra casi toda la inversion comercial.
3. La campana/conjunto `[META]_[CLP]_[CAPTACION]_[ABO]` / `[PR]_[NATIVE FORM]_[AVG+]_[ISLA]` concentra la evidencia matched: 1.179 leads, 339 qualified A/B y 873.6300059999967 de spend.
4. La campana/conjunto `[META]_[CLP]_[RTG]_[CBO]` / `[RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA]` aporta 51 qualified A/B con cobertura `lead_only`; no debe compararse como eficiencia de inversion.
5. En junio se observa el mayor volumen mensual: 772 leads, 226 qualified A/B y 496.56000899999043 de spend.

---

## Analisis por nivel disponible

### Nivel campana / conjunto

| Campana | Conjunto | Coverage | Leads | Qualified A/B | Spend | Tasa A/B | Spend / qualified A/B |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| [META]_[CLP]_[CAPTACION]_[ABO] | [PR]_[NATIVE FORM]_[AVG+]_[ISLA] | matched | 1.179 | 339 | 873.6300059999967 | 0.2875318066157761 | 2.5770796637168045 |
| [META]_[CLP]_[RTG]_[CBO] | [RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA] | lead_only | 140 | 51 | 0.0 | 0.36428571428571427 | 0.0 |
| UNKNOWN | UNKNOWN | spend_only | 0 | 0 | 2.200000000000001 | UNKNOWN | UNKNOWN |

Lectura ejecutiva: CAPTACION/ABO es el unico bloque con relacion calidad-inversion defendible. RTG/CBO muestra calidad de lead, pero sin spend emparejado.

### Nivel anuncio / creatividad referenciada

| Ranking | ad_name | Coverage | Leads | Qualified A/B | Spend | Tasa A/B | Spend / qualified A/B | Lectura |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1 | matched | 640 | 185 | 468.06000799999686 | 0.2890625 | 2.5300540972972803 | Mayor generador absoluto de qualified A/B |
| 2 | ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1 | matched | 359 | 101 | 245.8399969999997 | 0.28133704735376047 | 2.4340593762376206 | Segundo mayor generador; eficiencia similar al lider |
| 3 | FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1 | lead_only | 116 | 40 | 0.0 | 0.3448275862068966 | 0.0 | Principal fuente RTG lead-only; no comparable en spend |
| 4 | FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1 | matched | 53 | 19 | 48.96000000000012 | 0.3584905660377358 | 2.5768421052631645 | Tasa superior con volumen medio |
| 5 | FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1 | matched | 19 | 10 | 25.160000000000068 | 0.5263157894736842 | 2.5160000000000067 | Tasa alta, muestra limitada |
| 6 | ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1 | matched | 67 | 8 | 50.009999999999984 | 0.11940298507462686 | 6.251249999999998 | Menor calidad/eficiencia relativa entre matched con volumen relevante |

Lectura ejecutiva: los dos primeros anuncios explican la mayor parte del volumen cualificado matched. Las tasas altas en muestras pequenas son senales a revisar, no ganadores concluyentes. La peor senal relativa con volumen relevante aparece en `ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1`.

### Evolucion temporal

| Mes | Leads | Qualified A/B | Spend | Tasa A/B | Spend / qualified A/B |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2026-04 | 179 | 54 | 146.2900000000005 | 0.3016759776536313 | 2.7090740740740835 |
| 2026-05 | 368 | 110 | 232.979997 | 0.29891304347826086 | 2.1179999727272727 |
| 2026-06 | 772 | 226 | 496.56000899999043 | 0.2927461139896373 | 2.1971681814158868 |

Lectura ejecutiva: el volumen crece hasta junio. La tasa de cualificacion se mantiene alrededor del 29-30%, con ligera reduccion mensual. Mayo muestra el mejor coste por qualified A/B, aunque abril es parcial desde el dia 18.

---

## Conclusiones

1. El periodo disponible hasta el 30 de junio de 2026 contiene evidencia suficiente para una lectura ejecutiva de calidad de leads a nivel de referencia de anuncio.
2. La relacion entre calidad e inversion solo es solida en el grupo `matched`; fuera de ese grupo, la cobertura limita las conclusiones.
3. CAPTACION/ABO es la base principal para decisiones de eficiencia, porque concentra spend y qualified leads emparejados.
4. RTG/CBO debe conservarse como lectura separada: genera leads cualificados, pero no permite evaluar eficiencia economica con los datos actuales.
5. Los anuncios `ViajeSinEstres_AlivioEmocional...` y `ViajaComoInvitado_Identidad...` son los mayores generadores absolutos de leads cualificados.
6. Las conclusiones creativas deben limitarse a nombres/referencias de anuncio; no hay metadata suficiente para afirmar causalidad por formato, pieza visual o copy.

---

## Recomendaciones priorizadas

| Prioridad | Recomendacion | Motivo |
| --- | --- | --- |
| P1 | Basar las decisiones inmediatas de eficiencia en referencias `matched`, especialmente CAPTACION/ABO. | Es el unico bloque con leads, qualified A/B e inversion emparejada. |
| P1 | Mantener RTG/CBO como lectura separada de calidad lead-side. | Tiene 51 qualified A/B, pero no tiene spend emparejado. |
| P1 | Revisar y proteger el aprendizaje de los dos anuncios matched con mayor volumen de qualified leads. | Juntos aportan 286 qualified A/B dentro de matched. |
| P2 | Auditar `ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1`. | Presenta tasa A/B baja y coste por qualified A/B alto dentro de matched con volumen relevante. |
| P2 | Validar mapping de spend por campana/conjunto antes de redistribuir presupuesto a esos niveles. | La metadata campaign/adset procede del lado lead y no cubre todos los casos spend-side. |
| P2 | Tratar anuncios de tasa alta y bajo volumen como candidatos a test, no como ganadores definitivos. | La muestra limitada puede distorsionar la lectura. |
| P3 | No usar CTR, clicks, impresiones ni claims de asset creativo en la decision actual. | Esas variables no estan disponibles en el scope reconstruido. |

---

## Limitaciones y UNKNOWN

| Limitacion / UNKNOWN | Efecto sobre la conclusion |
| --- | --- |
| El periodo disponible empieza el 2026-04-18 | Abril es parcial y no debe compararse como mes completo |
| `campaign_signal` se aplica en spend-side | No debe afirmarse que cada lead carry directamente esa senal comercial |
| `lead_only` no tiene spend emparejado | No permite eficiencia economica ni CPL real |
| `spend_only` no tiene leads emparejados | No permite calidad, CPL ni attribution campaign/adset |
| No hay impressions/clicks/CTR en el modelo ejecutivo reconstruido | No se puede evaluar funnel superior |
| No hay metadata completa de asset creativo | No se puede atribuir causalidad por pieza, formato, visual o copy |
| Duplicados/test-record flags no quedan plenamente mapeados en esta consulta | Mantener cautela en conteos aunque se exige `lead_id IS NOT NULL` |
| Valores monetarios sin redondeo | Se preserva precision de BigQuery para trazabilidad |

---

## Trazabilidad

| Seccion | Fuente |
| --- | --- |
| Alcance y metodologia | `docs/context_refs.md`, AUC-001, skill `meta-lead-quality-analysis`, Data Contract |
| Disponibilidad temporal | BigQuery CLI sobre `fct_lead_enriched`, `int_faro_lead_scoring`, `fct_spend` |
| Totales y cobertura | BigQuery CLI reconstruyendo modelo lead/spend por `ad_id_norm` |
| Ranking de anuncios | BigQuery CLI sobre modelo reconstruido por referencia de anuncio |
| Campaign/adset | BigQuery CLI con metadata lead-side y spend emparejado |
| Evolucion mensual | BigQuery CLI por mes hasta 2026-06-30 |
| Limitaciones | Data Contract, Analytical Contract y cobertura observada en consulta fresca |

---

## Execution record

### Artefactos consultados

- `docs/context_refs.md`
- `analytical_use_cases/meta_lead_quality_analysis.md`
- `.github/skills/meta-lead-quality-analysis/SKILL.md`
- `docs/handoffs/auc-001-data-contract.md`

### Herramientas utilizadas

- Lectura de artefactos canonicos mediante shell.
- BigQuery CLI (`bq query`) para reconstruir evidencia nueva.
- Escritura de este archivo Markdown en `outputs/evaluations`.

### Consultas ejecutadas mediante BigQuery CLI

1. Disponibilidad temporal y conteo de filas hasta `2026-06-30` en `fct_lead_enriched`, `int_faro_lead_scoring` y `fct_spend`.
2. Validacion de plataforma y organicidad lead-side.
3. Reconstruccion del modelo por `ad_id_norm` con `lead_agg`, `spend_agg` y full outer join.
4. Totales globales del modelo reconstruido.
5. Ranking por referencia de anuncio.
6. Agregado por campana/conjunto.
7. Agregado mensual.

### MCP

No se uso BigQuery MCP Server porque no hay herramienta MCP de BigQuery expuesta en este turno. La evidencia nueva queda identificada como evidencia obtenida mediante BigQuery CLI.

### Confirmacion de independencia

No se utilizaron informes anteriores, outputs previos ni handoffs de resultado como fuente de conclusiones. Los resultados proceden de consultas BigQuery ejecutadas de nuevo en esta corrida y del contexto canonico minimo necesario para reconstruir el workflow.

### Datos no obtenidos

- Impresiones.
- Clicks.
- CTR.
- Metadata completa de assets creativos.
- Mapping completo de spend por campaign/adset fuera de la union por `ad_id_norm`.
- Flags completos de duplicados/test records.
