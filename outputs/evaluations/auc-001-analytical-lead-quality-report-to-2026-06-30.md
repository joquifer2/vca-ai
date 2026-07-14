# Informe analitico - Calidad de leads Meta Ads hasta 2026-06-30

## Metadata

| Campo | Valor |
| --- | --- |
| Artifact ID | VCA-AUC-001-ANL-REPORT-2026-06-30-FRESH |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Tipo de salida | Informe analitico trazable |
| Fecha de generacion | 2026-07-13 |
| Solicitud | Generar informe analitico de calidad de leads hasta el 30 de junio empezando de cero |
| Periodo observado disponible | 2026-04-18 to 2026-06-30 |
| Canal | Meta Ads / Meta Lead Ads |
| Fuente principal de datos | BigQuery CLI sobre tablas publicadas del Data Contract |
| Estado | Generado como nueva ejecucion analitica; no usa resultados anteriores como fuente |

---

## 1. Alcance y criterio de ejecucion

La solicitud actual pide un informe analitico de calidad de leads hasta el 30 de junio y que la ejecucion empiece de cero. Para esta corrida se ha usado el contexto canonico de AUC-001 solo para reconstruir metodologia, tablas, definicion de calidad y restricciones; no se han usado informes anteriores ni Evidence Sets previos como fuente de resultados.

La comprobacion directa de disponibilidad en BigQuery muestra que las tablas relevantes contienen datos desde `2026-04-18` hasta `2026-06-30`. Por tanto, el periodo analitico de esta ejecucion es:

```text
2026-04-18 to 2026-06-30
```

La fecha `2026-06-30` se interpreta como 30 de junio de 2026 por el contexto vigente del repositorio y por la fecha actual de ejecucion.

### Fuentes canonicas usadas para metodologia

| Fuente | Uso |
| --- | --- |
| `docs/context_refs.md` | Identificar fuentes oficiales, proyecto BigQuery y tablas publicadas |
| `.github/instructions/sdd.instructions.md` | Mantener trazabilidad y separacion metodologica |
| `analytical_use_cases/meta_lead_quality_analysis.md` | Reconstruir objetivo, alcance y salidas esperadas de AUC-001 |
| `.github/skills/meta-lead-quality-analysis/SKILL.md` | Reconstruir workflow analitico |
| `docs/handoffs/auc-001-analysis-request.md` | Confirmar parametros de ejecucion aplicables |
| `docs/handoffs/auc-001-execution-context.md` | Confirmar scope Meta Ads, filtros y definicion de lead de calidad |
| `docs/handoffs/auc-001-data-contract.md` | Confirmar tablas y frontera del Data Provider |
| `docs/handoffs/auc-001-analytical-contract.md` | Confirmar transformaciones y modelo por `ad_id_norm` |

---

## 2. Datos utilizados y preparacion

### Tablas consultadas

| Tabla | Rol |
| --- | --- |
| `datamart-vca-494114.marts.fct_lead_enriched` | Leads, metadata de campana/conjunto/anuncio y `lead_tier` |
| `datamart-vca-494114.intermediate.int_faro_lead_scoring` | Validacion cruzada de scoring FARO |
| `datamart-vca-494114.marts.fct_spend` | Inversion comercial con `campaign_signal = 'COMMERCIAL'` |

### Reglas de preparacion aplicadas

| Regla | Aplicacion |
| --- | --- |
| Periodo | `2026-04-18 <= fecha <= 2026-06-30` |
| Leads validos | `lead_id IS NOT NULL` |
| Trafico organico | Excluido mediante `is_organic = false` |
| Lead de calidad | `lead_tier IN ('A','B')` |
| Spend comercial | `campaign_signal = 'COMMERCIAL'` en `fct_spend` |
| Grano de analisis | `ad_id_norm`, normalizando `ad_id` lead-side con `REGEXP_REPLACE(ad_id, r'^ag:', '')` |
| Union lead/spend | Full outer join por `ad_id_norm` |
| Estados de cobertura | `matched`, `lead_only`, `spend_only` |

### Validacion de cobertura de fechas

| Fuente | min_date | max_date | Filas hasta 2026-06-30 |
| --- | --- | --- | ---: |
| `fct_lead_enriched` | 2026-04-18 | 2026-06-30 | 1319 |
| `int_faro_lead_scoring` | 2026-04-18 | 2026-06-30 | 1319 |
| `fct_spend` | 2026-04-18 | 2026-06-30 | 7332 |

### Validacion lead-side vs FARO scoring

| Metrica | Valor |
| --- | ---: |
| ad_refs comparadas | 13 |
| ad_refs coincidentes | 13 |
| ad_refs con mismatch | 0 |
| filas en `fct_lead_enriched` | 1319 |
| filas en `int_faro_lead_scoring` | 1319 |
| qualified A/B en `fct_lead_enriched` | 390 |
| qualified A/B en `int_faro_lead_scoring` | 390 |

Lectura: para esta ejecucion, la tabla enriquecida y la tabla FARO coinciden en volumen y calidad A/B por referencia de anuncio lead-side.

---

## 3. Resultados globales

### Totales del modelo reconstruido

| Metrica | Valor |
| --- | ---: |
| Referencias de anuncio | 15 |
| Leads | 1319 |
| Leads distintos | 1319 |
| Leads cualificados A/B | 390 |
| Lead Tier A | 57 |
| Lead Tier B | 333 |
| Inversion comercial | 875.8300059999967 |
| Tasa de cualificacion A/B | 0.29567854435178165 |
| Inversion por lead | 0.6640106186504903 |
| Inversion por lead cualificado A/B | 2.2457179641025555 |

### Cobertura por estado

| coverage_status | ad_refs | leads | qualified A/B | spend | qualified_rate_ab | spend/lead | spend/qualified A/B |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| matched | 8 | 1179 | 339 | 873.6300059999967 | 0.2875318066157761 | 0.7409923715012694 | 2.5770796637168045 |
| lead_only | 5 | 140 | 51 | 0.0 | 0.36428571428571427 | 0.0 | 0.0 |
| spend_only | 2 | 0 | 0 | 2.200000000000001 | UNKNOWN | UNKNOWN | UNKNOWN |

### Lectura analitica global

- El 89.39% de los leads observados estan en referencias `matched` y, por tanto, pueden analizarse junto con inversion comercial emparejada.
- El 86.92% de los leads cualificados A/B estan en `matched`.
- `lead_only` tiene una tasa A/B mayor que `matched` en la evidencia observada, pero no tiene spend emparejado; no debe compararse como eficiencia economica.
- `spend_only` es pequeno en importe, pero prueba que la cobertura no es completa y debe mantenerse separada.

---

## 4. Evolucion temporal

| Mes | Leads | Qualified A/B | Lead Tier A | Lead Tier B | Spend | Qualified rate A/B | Spend/qualified A/B |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2026-04 | 179 | 54 | 7 | 47 | 146.2900000000005 | 0.3016759776536313 | 2.7090740740740835 |
| 2026-05 | 368 | 110 | 19 | 91 | 232.979997 | 0.29891304347826086 | 2.1179999727272727 |
| 2026-06 | 772 | 226 | 31 | 195 | 496.56000899999043 | 0.2927461139896373 | 2.1971681814158868 |

### Interpretacion temporal

El volumen crece de abril a junio: 179 leads en abril parcial, 368 en mayo y 772 en junio. La tasa de cualificacion A/B se mantiene relativamente estable, con una ligera reduccion desde 0.3016759776536313 en abril a 0.2927461139896373 en junio. La inversion por lead cualificado mejora de abril a mayo y empeora ligeramente en junio frente a mayo, aunque sigue por debajo de abril.

Esta lectura temporal debe considerar que abril es un mes parcial desde el dia 18.

---

## 5. Analisis por campana y conjunto

| Campaign | Adset | Coverage | Refs | Leads | Qualified A/B | Spend | Qualified rate | Spend/qualified A/B |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [META]_[CLP]_[CAPTACION]_[ABO] | [PR]_[NATIVE FORM]_[AVG+]_[ISLA] | matched | 8 | 1179 | 339 | 873.6300059999967 | 0.2875318066157761 | 2.5770796637168045 |
| [META]_[CLP]_[RTG]_[CBO] | [RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA] | lead_only | 5 | 140 | 51 | 0.0 | 0.36428571428571427 | 0.0 |
| UNKNOWN | UNKNOWN | spend_only | 2 | 0 | 0 | 2.200000000000001 | UNKNOWN | UNKNOWN |

### Interpretacion por campana/conjunto

- `[META]_[CLP]_[CAPTACION]_[ABO]` es el unico bloque con cobertura `matched`; es la base principal para analizar relacion calidad-inversion.
- `[META]_[CLP]_[RTG]_[CBO]` aporta 51 leads A/B y una tasa A/B observada superior a matched, pero su spend no esta emparejado en el modelo. Debe leerse como calidad lead-side, no como eficiencia de inversion.
- Las filas `UNKNOWN` son spend sin leads emparejados; no permiten atribucion de calidad ni analisis campaign/adset.

---

## 6. Analisis por referencia de anuncio

### Referencias matched con mayor valor analitico

| ad_id_norm | ad_name | Leads | Qualified A/B | Spend | Qualified rate | Spend/qualified A/B | Lectura |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 120245828603090721 | ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1 | 640 | 185 | 468.06000799999686 | 0.2890625 | 2.5300540972972803 | Principal generador por volumen y qualified A/B |
| 120245829545180721 | ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1 | 359 | 101 | 245.8399969999997 | 0.28133704735376047 | 2.4340593762376206 | Segundo gran contribuidor; coste por A/B similar al principal |
| 120245407987450721 | FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1 | 53 | 19 | 48.96000000000012 | 0.3584905660377358 | 2.5768421052631645 | Mejor tasa que los dos mayores, con volumen medio |
| 120245407987440721 | FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1 | 19 | 10 | 25.160000000000068 | 0.5263157894736842 | 2.5160000000000067 | Tasa alta, pero muestra pequena |
| 120251257513780721 | ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1 | 67 | 8 | 50.009999999999984 | 0.11940298507462686 | 6.251249999999998 | Tasa y coste por A/B menos favorables dentro de matched con volumen relevante |
| 120245829746630721 | ViajaComoInvitado_Estatus_ExperienciaCalidad_Reel_v1 | 20 | 8 | 18.22000099999993 | 0.4 | 2.277500124999991 | Buena tasa observada con muestra pequena |
| 120245829115590721 | ViajeSinEstres_PrevencionDeRiesgo_ErroresViaje_Reel_v1 | 16 | 6 | 12.519999999999936 | 0.375 | 2.086666666666656 | Buen coste por A/B, muestra pequena |
| 120251254823190721 | ExperienciasUnicas_OportunidadIrrepetible_EclipseSolar2026_Reel_v1 | 5 | 2 | 4.859999999999992 | 0.4 | 2.429999999999996 | Muestra demasiado pequena para extrapolar |

### Referencias lead_only

| ad_id_norm | ad_name | Leads | Qualified A/B | Qualified rate | Lectura |
| --- | --- | ---: | ---: | ---: | --- |
| 120247352473020721 | FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1 | 116 | 40 | 0.3448275862068966 | Principal fuente RTG lead-only |
| 120245823087500721 | MasCaroPorqueMejor_CalidadVsCantidad_ViajesConCalidad_Reel_v1 | 18 | 9 | 0.5 | Buena tasa, volumen pequeno |
| 120251255543170721 | ExperienciasUnicas_OportunidadIrrepetible_EclipseSolar2026_Reel_v1 | 2 | 2 | 1.0 | Muestra minima, no extrapolable |
| 120245823087510721 | FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1 | 3 | 0 | 0.0 | Sin A/B observados |
| 120251255543160721 | ExperienciasUnicas_LugaresSorprendentes_CamposLavanda_Reel_v1 | 1 | 0 | 0.0 | Muestra minima |

### Referencias spend_only

| ad_id_norm | ad_name | Spend | Lectura |
| --- | --- | ---: | --- |
| 120251249759480721 | ExperienciasUnicas_LugaresSorprendentes_CamposLavanda_Reel_v1 | 1.2000000000000006 | Spend sin leads emparejados |
| 120251252180570721 | ExperienciasUnicas_ErroresPlanificacion_EclipseSolar2026_Reel_v1 | 1.0000000000000004 | Spend sin leads emparejados |

---

## 7. Respuesta a las preguntas analiticas

### Que elementos generan leads de mayor calidad

Hecho observado: por tasa A/B, algunas referencias de bajo volumen muestran tasas altas, como `120245407987440721` con 0.5263157894736842 y `120245829746630721` con 0.4. Sin embargo, por volumen absoluto de qualified A/B, destacan `120245828603090721` con 185 y `120245829545180721` con 101.

Interpretacion: para decisiones robustas, la calidad debe ponderarse por volumen y cobertura. Los dos mayores anuncios matched son los principales generadores de qualified leads. Las referencias de tasa alta y muestra pequena son candidatas a revision, no conclusiones fuertes.

### Como se relacionan calidad e inversion

Hecho observado: en `matched`, 873.6300059999967 de inversion generan 1179 leads y 339 qualified A/B, con coste por qualified A/B de 2.5770796637168045. En `lead_only`, hay 51 qualified A/B sin spend emparejado. En `spend_only`, hay 2.200000000000001 de spend sin leads.

Interpretacion: la relacion calidad-inversion solo es defendible en `matched`. `lead_only` puede informar calidad, pero no eficiencia economica. `spend_only` informa cobertura incompleta, no rendimiento.

### Diferencias relevantes

- Diferencia por cobertura: `matched` soporta eficiencia; `lead_only` soporta calidad sin spend; `spend_only` no soporta calidad.
- Diferencia por campana/conjunto: CAPTACION/ABO concentra la evidencia matched; RTG/CBO concentra evidencia lead-only.
- Diferencia por anuncio: los mayores contribuidores por qualified A/B no son necesariamente los de mayor tasa; las tasas mas altas tienen muestras mas pequenas.
- Diferencia temporal: el volumen crece hasta junio, mientras la tasa A/B se mantiene cerca de 0.29-0.30.

---

## 8. Conclusiones

1. El periodo disponible hasta 2026-06-30 cubre desde 2026-04-18 y contiene 1.319 leads, 390 qualified A/B y 875.8300059999967 de inversion comercial.
2. La evidencia mas accionable esta en 8 referencias `matched`, que explican 1.179 leads, 339 qualified A/B y casi toda la inversion comercial.
3. Los principales generadores por volumen de qualified A/B son `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1` y `ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1`.
4. Algunas referencias con muestra pequena muestran tasas A/B superiores, pero no deben convertirse automaticamente en ganadores sin validar estabilidad con mas volumen.
5. RTG/CBO muestra calidad lead-side relevante, pero no eficiencia economica porque no tiene spend emparejado en el modelo reconstruido.
6. La lectura por campana, conjunto y creatividad sigue limitada por cobertura y por falta de metadata completa de asset creativo.

---

## 9. Recomendaciones priorizadas

| Prioridad | Recomendacion | Justificacion | Tipo |
| --- | --- | --- | --- |
| P1 | Usar `matched` como base primaria para decisiones de eficiencia hasta resolver cobertura restante. | Es el unico grupo con leads, qualified A/B y spend emparejados. | Decision analitica inmediata |
| P1 | Separar RTG/CBO lead-only en una lectura propia de calidad, sin compararlo como eficiencia de spend. | Tiene 51 qualified A/B y tasa 0.36428571428571427, pero sin spend emparejado. | Control metodologico |
| P1 | Revisar los dos anuncios matched que concentran mas qualified A/B antes de redistribuir inversion. | Aportan 286 qualified A/B de 339 en matched. | Priorizacion de revision |
| P2 | Investigar por que `ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1` tiene coste por qualified A/B de 6.251249999999998 y tasa 0.11940298507462686. | Es el caso menos favorable entre matched con volumen relevante. | Optimizacion candidata |
| P2 | Validar mapping de spend por campana/conjunto si se quieren decisiones a nivel campaign/adset. | El modelo solo atribuye campaign/adset desde metadata lead-side. | Mejora de cobertura |
| P2 | Tratar anuncios con tasas altas y muestras pequenas como candidatos a test, no como ganadores definitivos. | Sus tasas pueden ser inestables por bajo volumen. | Control de inferencia |
| P3 | No usar impresiones, clicks, CTR ni claims de asset creativo en decisiones actuales. | Esas variables no estan disponibles en el scope reconstruido. | Guardrail de alcance |

---

## 10. Limitaciones y UNKNOWN

| Limitacion / UNKNOWN | Efecto |
| --- | --- |
| No hay campos completos de duplicado/test-record en la consulta reconstruida | Los conteos usan `lead_id IS NOT NULL`, pero no prueban exclusion completa de duplicados/test |
| `campaign_signal` existe en spend-side, no como atributo directo del lead | No debe afirmarse que cada lead es comercial por si mismo |
| `lead_only` tiene spend 0 por ausencia de match, no por prueba de inversion real cero | Impide calcular eficiencia economica para RTG/CBO |
| `spend_only` no tiene leads ni campaign/adset lead-side | Impide calidad, CPL y atribucion campaign/adset |
| No hay impresiones, clicks ni CTR en el modelo usado | No se puede evaluar funnel superior ni eficiencia de clics |
| No hay metadata completa de asset creativo | No se puede atribuir causalidad por formato, pieza, visual o copy |
| Abril es parcial desde 2026-04-18 | Las comparaciones mensuales deben considerar distinta cobertura temporal |
| Valores monetarios se conservan con precision BigQuery | No se aplica redondeo para preservar trazabilidad |

---

## 11. Trazabilidad de evidencia

| Bloque | Procedencia |
| --- | --- |
| Alcance metodologico | Artefactos canonicos del repositorio listados en seccion 1 |
| Schema y columnas | BigQuery CLI: `INFORMATION_SCHEMA.COLUMNS` en `marts` e `intermediate` |
| Ventana temporal | BigQuery CLI sobre `fct_lead_enriched`, `int_faro_lead_scoring`, `fct_spend` |
| Modelo por coverage | BigQuery CLI reconstruyendo `lead_agg`, `spend_agg` y full outer join por `ad_id_norm` |
| Detalle de anuncios | BigQuery CLI sobre modelo reconstruido por `ad_id_norm` |
| Campana/conjunto | BigQuery CLI sobre modelo reconstruido con metadata lead-side |
| Evolucion mensual | BigQuery CLI agregando leads y spend por mes |
| Validacion FARO | BigQuery CLI comparando `fct_lead_enriched` contra `int_faro_lead_scoring` |

---

## Execution record

### Artefactos consultados

- `docs/context_refs.md`
- `.github/instructions/sdd.instructions.md`
- `analytical_use_cases/meta_lead_quality_analysis.md`
- `.github/skills/meta-lead-quality-analysis/SKILL.md`
- `docs/handoffs/auc-001-analysis-request.md`
- `docs/handoffs/auc-001-execution-context.md`
- `docs/handoffs/auc-001-data-contract.md`
- `docs/handoffs/auc-001-analytical-contract.md`

No se usaron informes anteriores ni outputs previamente generados como fuente de conclusiones.

### Herramientas utilizadas

- Shell local para lectura de artefactos canonicos.
- BigQuery CLI (`bq query`) para evidencia de datos.
- Escritura de archivo Markdown en `outputs/evaluations`.

### Consultas ejecutadas

1. Consulta de columnas en `marts.INFORMATION_SCHEMA.COLUMNS`.
2. Consulta de columnas en `intermediate.INFORMATION_SCHEMA.COLUMNS` para `int_faro_lead_scoring`.
3. Consulta de disponibilidad temporal y filas hasta `2026-06-30`.
4. Consulta de plataforma / organicidad en leads.
5. Consulta de coverage summary reconstruyendo modelo por `ad_id_norm`.
6. Consulta de totales globales del modelo reconstruido.
7. Consulta de detalle por referencia de anuncio.
8. Consulta de agregados campaign/adset.
9. Consulta de agregados mensuales.
10. Consulta de validacion cruzada `fct_lead_enriched` vs `int_faro_lead_scoring`.

### Incidencias de ejecucion

- La primera consulta BigQuery fallo porque el CLI intento crear el job en el proyecto por defecto `datamart-393217`, sin permisos. Se corrigio fijando `--project_id=datamart-vca-494114`.
- No se uso BigQuery MCP porque no hay herramienta MCP de BigQuery expuesta en este turno. La evidencia nueva se obtuvo mediante BigQuery CLI y queda etiquetada como tal.

### Datos no obtenidos

- Impresiones.
- Clicks.
- CTR.
- Metadata completa de assets creativos.
- Mapping completo de spend por campaign/adset fuera de la metadata lead-side.
- Flags completos de duplicados/test records.

### Decisiones por cobertura

- Usar `2026-04-18 to 2026-06-30` como periodo disponible observado hasta el 30 de junio.
- Mantener separados `matched`, `lead_only` y `spend_only`.
- Usar `ad_id_norm` como grano primario.
- Tratar campaign/adset como lectura condicionada por metadata lead-side.
- No introducir conclusiones de creatividad causal, CTR ni funnel superior.
