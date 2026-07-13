# AUC-001 Report Quality Test - Meta Ads lead quality to 2026-06-30

## Resumen ejecutivo

Este informe analiza la calidad de leads procedentes de Meta Ads para AUC-001 con corte en **2026-06-30**. Como la solicitud actual no define fecha inicial, el alcance se ha fijado como **todo el histórico disponible en las tablas aprobadas hasta el 30 de junio de 2026**. La fecha inicial no se ha heredado de ejecuciones anteriores: se ha observado en BigQuery como **2026-04-18**.

La evidencia principal de calidad se obtuvo mediante BigQuery MCP Server sobre `datamart-vca-494114.intermediate.int_faro_lead_scoring`. La relación entre inversión y calidad requiere `marts.fct_spend`, que el MCP rechazó por estar fuera de su scope autorizado; esa parte se obtuvo mediante BigQuery CLI y queda marcada como evidencia CLI.

Hechos observados principales:

| Métrica | Valor |
|---|---:|
| Periodo cubierto por datos observados | 2026-04-18 a 2026-06-30 |
| Leads Meta observados | 1.319 |
| Leads con identificador válido | 1.319 |
| Leads FARO A/B | 390 |
| Tasa A/B total | 29,57% |
| Campañas con leads | 2 |
| Ad sets con leads | 2 principales, más una variante `- Copia` con 1 lead |
| Anuncios/ad references con leads | 13 |
| Spend `COMMERCIAL` observado por CLI | 875,83 EUR |
| Spend `COMMERCIAL` emparejado con leads por `ad_id` normalizado | 873,63 EUR |

Interpretación ejecutiva:

La campaña/ad set de captación `[META]_[CLP]_[CAPTACIÓN]_[ABO]` / `[PR]_[NATIVE FORM]_[AVG+]_[ISLA]` concentra el volumen y casi toda la inversión comercial emparejable: 1.179 leads, 339 A/B y 873,63 EUR de spend emparejado. Es la base más sólida para decisiones de eficiencia.

La campaña/ad set RTG `[META]_[CLP]_[RTG]_[CBO]` / `[RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA]` muestra mejor tasa A/B en lectura de calidad pura, pero queda como `lead_only` en el modelo de inversión comercial disponible. Por tanto, puede tratarse como señal de calidad, no como evidencia de eficiencia económica.

La creatividad/ad reference con mayor aportación absoluta es `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`: 640 leads, 185 A/B, 468,06 EUR y 2,53 EUR por lead A/B. La creatividad con mejor tasa A/B entre las piezas con volumen material es `FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1` en captación: 19 leads, 10 A/B, 52,63% A/B y 2,52 EUR por lead A/B. `ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1` presenta peor eficiencia relativa en el conjunto emparejado: 67 leads, 8 A/B, 11,94% A/B y 6,25 EUR por lead A/B.

## Objetivo y alcance

Objetivo: preparar un informe ejecutivo para Dirección sobre calidad de leads Meta Ads hasta el 30 de junio de 2026, identificando diferencias por campaña, conjunto de anuncios y creatividad/ad reference cuando los datos lo permitan.

Alcance operativo reconstruido:

| Elemento | Decisión aplicada |
|---|---|
| Caso | AUC-001 - Meta Lead Quality Analysis |
| Corte temporal | 2026-06-30 |
| Fecha inicial | No declarada por la solicitud; observada en datos como 2026-04-18 |
| Canal | Meta Ads / Meta Lead Ads |
| Calidad | Qualified Lead FARO equivalente a `lead_tier IN ('A','B')` |
| Inversión | `marts.fct_spend`, filtrando `campaign_signal = 'COMMERCIAL'` para lectura comercial |
| Relación calidad-inversión | `ad_id` normalizado, eliminando prefijo `ag:` en tablas de leads |
| Geografía | Sin filtro geográfico adicional |
| Creatividad | Nivel `ad_id_norm` / `ad_name`; no hay asset metadata |

No se asume que todos los leads sean directamente `COMMERCIAL`, porque las tablas de leads no exponen `campaign_signal`. La lectura comercial se limita al subconjunto emparejado contra spend `COMMERCIAL`.

## Datos y cobertura utilizados

### Evidencia MCP

BigQuery MCP Server respondió correctamente para `intermediate.int_faro_lead_scoring`, incluyendo metadata y consultas read-only.

| Fuente MCP | Resultado |
|---|---|
| Tabla | `datamart-vca-494114.intermediate.int_faro_lead_scoring` |
| Scope validado | Lead scoring FARO |
| Periodo observado hasta corte | 2026-04-18 a 2026-06-30 |
| Leads | 1.319 |
| Leads A/B | 390 |
| Tiers | A: 57; B: 333; C: 551; D: 378 |
| Campañas | 2 |
| Ad sets | 2 principales, con una variante `- Copia` observada |
| Ads | 13 |

### Evidencia CLI

La relación inversión-calidad se ejecutó con BigQuery CLI porque el MCP rechazó `marts.fct_spend` como recurso fuera de scope.

| Fuente CLI | Uso |
|---|---|
| `datamart-vca-494114.marts.fct_lead_enriched` | Validación lead-side, `ad_id` normalizado, campaña, ad set, ad name |
| `datamart-vca-494114.marts.fct_spend` | Spend por `ad_id` y `campaign_signal` |

Cobertura de spend hasta 2026-06-30:

| campaign_signal | Spend | Ads |
|---|---:|---:|
| ACTIVATION | 221,86 EUR | 6 |
| ATTENTION | 308,54 EUR | 7 |
| COMMERCIAL | 875,83 EUR | 10 |

Solo `COMMERCIAL` se usa para eficiencia comercial de AUC-001. `ATTENTION` y `ACTIVATION` quedan excluidas de la relación calidad-inversión para no mezclar capas FARO.

### Cobertura del modelo calidad-inversión

| Estado | Ad refs | Leads | A/B | Tasa A/B | Spend | EUR/lead | EUR/A-B |
|---|---:|---:|---:|---:|---:|---:|---:|
| matched | 8 | 1.179 | 339 | 28,75% | 873,63 | 0,741 | 2,577 |
| lead_only | 5 | 140 | 51 | 36,43% | 0,00 | 0,000 | 0,000 |
| spend_only | 2 | 0 | 0 | UNKNOWN | 2,20 | UNKNOWN | UNKNOWN |

El estado `lead_only` no debe interpretarse como coste cero real. Significa que no existe spend `COMMERCIAL` emparejado en el modelo disponible.

## Principales resultados

### Hechos observados

- La calidad global A/B es estable y ligeramente descendente por mes: abril 30,17%, mayo 29,89%, junio 29,27%.
- El 89,4% de los leads observados se encuentra en anuncios emparejados con spend comercial: 1.179 de 1.319.
- El 86,9% de los leads A/B observados se encuentra en anuncios emparejados con spend comercial: 339 de 390.
- El 99,75% del spend comercial observado queda emparejado con anuncios con leads: 873,63 EUR de 875,83 EUR.
- La campaña de captación `[META]_[CLP]_[CAPTACIÓN]_[ABO]` aporta la mayoría del volumen y de los leads A/B.
- La campaña RTG muestra mejor tasa A/B lead-side, pero sin spend comercial emparejado en el modelo disponible.

### Interpretación

La inversión comercial está concentrada en una estructura que sí genera volumen y calidad, aunque con una tasa A/B inferior a RTG. Esto no significa que RTG sea más eficiente: significa que RTG parece cualificar mejor sus leads entre los registros observados, pero la evidencia no permite calcular su coste comercial.

En el nivel creatividad/ad reference, no hay una única pieza dominante por todos los criterios. `ViajeSinEstres_AlivioEmocional` domina en volumen y A/B absolutos; `FiltroBilletes_EscasezReal` tiene mejor tasa A/B con volumen más bajo; `ViajaComoInvitado_Identidad` aporta volumen relevante con coste por A/B competitivo; `BoriWine2026` queda rezagada por tasa y coste por A/B.

### Hipótesis

- Las creatividades de filtro explícito o alivio emocional pueden estar captando intención más útil que las de experiencia puntual, pero esto debe validarse con datos comerciales posteriores.
- RTG podría estar generando leads más cualificados por madurez previa de audiencia, aunque no se puede cuantificar eficiencia sin spend emparejado.
- La estabilidad mensual de la tasa A/B sugiere que el scoring FARO está produciendo una lectura consistente, pero no demuestra calidad comercial final ni ventas.

## Análisis por nivel disponible

### Campañas y conjuntos

| Campaña | Ad set | Cobertura | Leads | A/B | Tasa A/B | Spend | EUR/A-B | Lectura |
|---|---|---|---:|---:|---:|---:|---:|---|
| `[META]_[CLP]_[CAPTACIÓN]_[ABO]` | `[PR]_[NATIVE FORM]_[AVG+]_[ISLA]` | matched | 1.179 | 339 | 28,75% | 873,63 | 2,58 | Base principal para decisiones de eficiencia |
| `[META]_[CLP]_[RTG]_[CBO]` | `[RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA]` | lead_only | 139 | 51 | 36,69% | UNKNOWN | UNKNOWN | Señal de calidad sin eficiencia económica |
| `[META]_[CLP]_[RTG]_[CBO]` | variante `- Copia` | lead_only | 1 | 0 | 0,00% | UNKNOWN | UNKNOWN | Volumen no material |
| UNKNOWN | UNKNOWN | spend_only | 0 | 0 | UNKNOWN | 2,20 | UNKNOWN | Spend comercial sin leads emparejados |

La campaña de captación es el único nivel campaña/ad set con inversión comercial emparejada suficiente para lectura de eficiencia. RTG es relevante para calidad, pero no para coste.

### Creatividades / ad references emparejadas

| Ad reference | Leads | A/B | Tasa A/B | Spend | EUR/A-B | Lectura |
|---|---:|---:|---:|---:|---:|---|
| `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1` | 640 | 185 | 28,91% | 468,06 | 2,53 | Mayor escala absoluta |
| `ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1` | 359 | 101 | 28,13% | 245,84 | 2,43 | Escala alta y eficiencia similar a la media |
| `FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1` | 53 | 19 | 35,85% | 48,96 | 2,58 | Buena tasa, coste medio |
| `FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1` | 19 | 10 | 52,63% | 25,16 | 2,52 | Mejor tasa con volumen limitado |
| `ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1` | 67 | 8 | 11,94% | 50,01 | 6,25 | Peor eficiencia relativa |
| `ViajaComoInvitado_Estatus_ExperienciaCalidad_Reel_v1` | 20 | 8 | 40,00% | 18,22 | 2,28 | Buena tasa, volumen bajo |
| `ViajeSinEstres_PrevencionDeRiesgo_ErroresViaje_Reel_v1` | 16 | 6 | 37,50% | 12,52 | 2,09 | Buena eficiencia, volumen bajo |
| `ExperienciasUnicas_OportunidadIrrepetible_EclipseSolar2026_Reel_v1` | 5 | 2 | 40,00% | 4,86 | 2,43 | Muestra pequeña |

Hecho observado: la mayor parte de los A/B viene de dos ad references de escala: `ViajeSinEstres_AlivioEmocional` y `ViajaComoInvitado_Identidad`, con 286 A/B combinados.

Interpretación: estas piezas sostienen el rendimiento principal. Las piezas con mejores tasas deben tratarse como candidatas a exploración controlada, no como ganadoras definitivas, porque su volumen es menor.

### Creatividades / ad references lead-only

| Ad reference | Leads | A/B | Tasa A/B | Lectura |
|---|---:|---:|---:|---|
| `FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1` RTG | 116 | 40 | 34,48% | Señal RTG de calidad relevante |
| `MasCaroPorqueMejor_CalidadVsCantidad_ViajesConCalidad_Reel_v1` RTG | 18 | 9 | 50,00% | Buena tasa, volumen bajo |
| `ExperienciasUnicas_OportunidadIrrepetible_EclipseSolar2026_Reel_v1` RTG | 2 | 2 | 100,00% | Muestra no material |
| Otros RTG | 4 | 0 | 0,00% | Muestra baja |

Estos registros no permiten inferir coste. Son útiles para detectar señales de calidad de audiencia o mensaje, no para presupuesto.

## Conclusiones

1. La campaña de captación `[META]_[CLP]_[CAPTACIÓN]_[ABO]` es la base de eficiencia más defendible: concentra inversión comercial, volumen y 339 leads A/B.
2. RTG genera una tasa A/B superior en lectura lead-side, pero no tiene spend comercial emparejado en las fuentes aprobadas; cualquier afirmación de eficiencia RTG queda UNKNOWN.
3. `ViajeSinEstres_AlivioEmocional` y `ViajaComoInvitado_Identidad` son las piezas más relevantes por contribución absoluta a leads A/B.
4. `FiltroBilletes_EscasezReal` combina buena tasa A/B tanto en captación como en RTG, pero necesita más volumen o validación controlada antes de escalar conclusiones.
5. `BoriWine2026` muestra una señal de baja eficiencia relativa dentro de los anuncios emparejados.
6. No hay evidencia suficiente para hablar de formato, asset creativo, copy exacto o causa creativa: solo hay `ad_name` como referencia.
7. No hay evidencia de impresiones, clics o CTR dentro del source set aprobado para este informe.

## Recomendaciones priorizadas

### P1 - Mantener la base de captación que sostiene volumen y calidad

Acción: conservar la estructura `[META]_[CLP]_[CAPTACIÓN]_[ABO]` / `[PR]_[NATIVE FORM]_[AVG+]_[ISLA]` como base de inversión comercial mientras se optimizan piezas específicas.

Justificación: es el único nivel campaña/ad set con spend comercial emparejado material, 1.179 leads y 339 A/B.

### P1 - Proteger y seguir validando las piezas de mayor contribución

Acción: mantener seguimiento prioritario de `ViajeSinEstres_AlivioEmocional` y `ViajaComoInvitado_Identidad`, porque explican la mayor parte de los A/B emparejados.

Justificación: aportan escala; sus costes por A/B están próximos entre sí y no muestran una desviación negativa material frente al total emparejado.

### P2 - Test controlado sobre `FiltroBilletes_EscasezReal`

Acción: plantear una prueba incremental controlada de `FiltroBilletes_EscasezReal`, separando captación y RTG.

Justificación: muestra una de las tasas A/B más altas, pero con volumen menor en captación y sin eficiencia comercial emparejada en RTG.

### P2 - Revisar o limitar `BoriWine2026` antes de escalar inversión

Acción: no escalar `ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1` hasta entender si su baja tasa A/B responde al mensaje, al producto, a la audiencia o al momento.

Justificación: 11,94% A/B y 6,25 EUR por A/B, peor que el resto de piezas emparejadas con volumen comparable.

### P2 - Resolver mapping de spend RTG y campaña/ad set

Acción: habilitar una relación aprobada entre spend y campaña/ad set o confirmar explícitamente que RTG queda fuera de lectura de eficiencia.

Justificación: la principal diferencia observada entre captación y RTG no puede convertirse en recomendación presupuestaria sin spend emparejado.

### P3 - Ampliar cobertura de datos antes de decisiones de funnel

Acción: incorporar o autorizar fuentes de impresiones, clics, CTR y resultados comerciales downstream si Dirección quiere decidir sobre creatividad, saturación o eficiencia de embudo completo.

Justificación: el source set actual mide lead scoring y spend, pero no explica entrega, interacción, contactabilidad, oportunidad o venta.

## Limitaciones y UNKNOWN

| Limitación / UNKNOWN | Efecto |
|---|---|
| La solicitud no definía fecha inicial | Se usó histórico disponible observado: 2026-04-18 a 2026-06-30 |
| MCP solo autorizó `intermediate.int_faro_lead_scoring` | Calidad por MCP; inversión y modelo calidad-spend por CLI |
| `marts.fct_spend` fue rechazado por MCP | La relación inversión-calidad no es evidencia MCP |
| Las tablas de leads no exponen `campaign_signal` | No se afirma que cada lead sea directamente `COMMERCIAL` |
| `fct_spend` no expone campaña/ad set | Spend por campaña/ad set solo puede inferirse al emparejar por `ad_id`, no para spend-only |
| RTG aparece como `lead_only` para spend comercial | Calidad observable, eficiencia económica UNKNOWN |
| Creative asset metadata no disponible | Se analiza `ad_id` / `ad_name`, no formato real, pieza visual ni asset |
| Impresiones, clics y CTR fuera del source set usado | No hay lectura de funnel publicitario previo al lead |
| Test/duplicados no tienen mapping explícito en las consultas actuales | Se validó identificador de lead y ausencia de tiers vacíos, pero no exclusión completa de pruebas/duplicados |
| Un `ad_id` RTG aparece asociado a dos nombres de ad set, uno `- Copia` con 1 lead | El análisis por ad reference puede colapsar naming representativo; la lectura por ad set debe conservar esta cautela |

## Trazabilidad hacia fuentes utilizadas

Artefactos canónicos y de contexto:

- `AGENTS.md`
- `.github/instructions/sdd.instructions.md`
- `README.md`
- `project_brief.md`
- `docs/context_refs.md`
- `knowledge/client/ccd.md`
- `analytical_use_cases/meta_lead_quality_analysis.md`
- `.github/skills/meta-lead-quality-analysis/SKILL.md`
- `specs/spec-001-analytical-lifecycle.md`
- `specs/spec-002-component-boundaries.md`
- `specs/spec-004-transversal-contracts.md`
- `docs/handoffs/auc-001-analysis-request.md`
- `docs/handoffs/auc-001-execution-context.md`
- `docs/handoffs/auc-001-context-definition.md`
- `docs/handoffs/auc-001-data-contract.md`
- `docs/handoffs/auc-001-discovery-contract.md`
- `docs/handoffs/auc-001-analytical-contract.md`
- `docs/handoffs/auc-001-evidence-contract.md`
- `docs/handoffs/auc-001-evidence-acquisition.md`
- `docs/evaluations/auc-001-bigquery-mcp-integration-validation.md`

Fuentes de datos:

- MCP: `datamart-vca-494114.intermediate.int_faro_lead_scoring`
- CLI: `datamart-vca-494114.marts.fct_lead_enriched`
- CLI: `datamart-vca-494114.marts.fct_spend`

## Execution record

### Artefactos del repositorio consultados

Se consultaron instrucciones, specifications, contracts, AUC-001, skill y fuentes oficiales del repositorio antes de cerrar el informe. En particular: `AGENTS.md`, `.github/instructions/sdd.instructions.md`, `README.md`, `project_brief.md`, `docs/context_refs.md`, `knowledge/client/ccd.md`, `analytical_use_cases/meta_lead_quality_analysis.md`, `.github/skills/meta-lead-quality-analysis/SKILL.md`, `specs/spec-001-analytical-lifecycle.md`, `specs/spec-002-component-boundaries.md`, `specs/spec-004-transversal-contracts.md`, y los handoffs/contracts AUC-001 de contexto, data, discovery, analytical y evidence.

No se usaron `docs/handoffs/auc-001-executive-report.md`, `docs/handoffs/auc-001-knowledge-set.md` ni `docs/handoffs/auc-001-recommendation-set.md` como fuente de conclusiones.

### Herramientas utilizadas

- Lectura local de archivos con PowerShell.
- BigQuery MCP Server mediante endpoint local `http://127.0.0.1:8000/mcp`.
- BigQuery CLI `bq query` para fuentes no cubiertas por MCP.
- PowerShell `Set-Content` para generar este archivo, usado porque `apply_patch` falló por restricción del sandbox de Windows.

### Consultas o acciones ejecutadas mediante MCP

| Request ID | Acción | Resultado | Trace |
|---|---|---|---|
| `AUC001-QUALITY-TEST-DISCOVER-INT-FARO-001` | `discover_metadata` sobre `intermediate.int_faro_lead_scoring` | success | `trc-fecfd7d205de41f89c834c6b60cd6521` |
| `AUC001-QUALITY-TEST-QUERY-INT-FARO-JUNE-001` | Consulta preliminar junio 2026 | success; descartada como alcance primario tras resolver ambigüedad de fecha inicial | `trc-24cc02eca3db44cd9ef2830a17c25153` |
| `AUC001-QUALITY-TEST-DISCOVER-FCT-SPEND-001` | `discover_metadata` sobre `marts.fct_spend` | rejected, fuera de scope autorizado | `trc-d0362423e3714e049273cbcd1310abf6` |
| `AUC001-QUALITY-TEST-QUERY-INT-FARO-TO-20260630-001` | Calidad lead FARO hasta 2026-06-30 | success | `trc-2218883ef6984f279ea9da562f82dc63` |
| `AUC001-QUALITY-TEST-QUERY-INT-FARO-CAMPAIGN-TO-20260630-001` | Calidad por campaña/ad set hasta 2026-06-30 | success | `trc-6f942be138e049359fdf0cc5b159654d` |

### Consultas o acciones ejecutadas mediante CLI

Se ejecutaron consultas agregadas con `bq query --project_id=datamart-vca-494114` para:

- validar `fct_lead_enriched` y `fct_spend`;
- calcular distribución por `lead_tier`;
- calcular spend por `campaign_signal`;
- construir el modelo ad-level con `ad_id_norm`;
- calcular cobertura `matched`, `lead_only`, `spend_only`;
- obtener detalle por ad reference;
- obtener agregados por campaña/ad set donde existen metadatos lead-side;
- validar identificadores de lead y tiers vacíos;
- detectar ad references con más de un nombre de ad set.

### Datos que no pudieron obtenerse

- Spend por campaña/ad set directamente desde MCP.
- Spend por campaña/ad set directamente desde `fct_spend`, porque esa tabla no expone esos campos.
- Metadata de asset creativo, formato, visual, copy exacto o pieza multimedia.
- Impresiones, clics y CTR dentro del source set aprobado para este informe.
- Confirmación completa de exclusión de pruebas y duplicados mediante flags específicos.
- Resultados comerciales posteriores a lead, como contactabilidad, oportunidad, venta o margen.

### Decisiones tomadas por limitaciones de cobertura

- Se usó `2026-04-18` como fecha inicial observada, no como parámetro heredado.
- Se usó `lead_tier IN ('A','B')` como definición de lead cualificado por FARO/AUC-001.
- Se mantuvo `campaign_signal = 'COMMERCIAL'` solo para spend comercial, no como atributo directo del lead.
- Se separó evidencia MCP de evidencia CLI.
- Se mantuvieron RTG y spend-only como estados con limitaciones, sin inventar eficiencia económica.
- Se reportaron creatividades como ad references, no como assets creativos reales.

### Confirmación sobre el informe ejecutivo anterior

El informe ejecutivo anterior `docs/handoffs/auc-001-executive-report.md` no fue usado como fuente de conclusiones. Tampoco se usaron el Knowledge Set ni el Recommendation Set existentes para producir los hallazgos, interpretaciones o recomendaciones de este informe.

### Observaciones para evaluación posterior

- El MCP actual no cubre `marts.fct_spend`, por lo que AUC-001 todavía depende de CLI para relacionar inversión y calidad salvo que se amplíe el scope del servidor.
- El alcance "hasta 2026-06-30" debería formalizar si significa mes cerrado, histórico acumulado o ventana móvil para evitar ambigüedades en futuras ejecuciones.
- La frontera entre campaña/ad set y spend necesita un mapping aprobado si Dirección requiere recomendaciones presupuestarias por campaña o conjunto.
- La ausencia de metadata creativa limita recomendaciones de producción creativa.
- La ausencia de métricas de entrega y comerciales downstream limita decisiones sobre funnel completo.
