# AUC-001 P02 Analytical Report

## Estado

Producto analítico conforme con SPEC-014 para el periodo `2026-04-18` a `2026-07-17`.

La ejecución usa evidencia real adquirida exclusivamente mediante BigQuery MCP Server. El periodo se cerró en `2026-07-17` porque es la última fecha común entre `marts.fct_lead_enriched` y `marts.fct_spend`.

## Lectura Principal

Meta está generando volumen suficiente y coste observado bajo en el universo comercial matched, pero la calidad alta es selectiva. De 1.549 leads, 469 son A/B y 67 son Tier A. En el universo matched, 1.362 leads sostienen métricas coste-calidad canónicas: `cpl_commercial_matched` de 0,78 EUR y `cost_per_ab_commercial_matched` de 2,70 EUR.

La pregunta de negocio no es si hay volumen, sino cómo mover el mix hacia intención cualificada sin romper la eficiencia ni ocultar cobertura parcial.

## Evidencia Base

| Métrica | Valor |
| --- | ---: |
| Leads totales | 1.549 |
| Tier A | 67 |
| Tier B | 402 |
| A/B | 469 |
| A/B global | 30,28% |
| Tier A global | 4,33% |
| Matched leads | 1.362 |
| Matched A/B | 396 |
| Matched commercial spend | 1.069,05 EUR |
| `cpl_commercial_matched` | 0,78 EUR |
| `cost_per_ab_commercial_matched` | 2,70 EUR |
| `cost_per_tier_a_commercial_matched` | 19,44 EUR |

## Coverage

| Estado | Ads | Leads | A/B | Spend comercial |
| --- | ---: | ---: | ---: | ---: |
| matched | 12 | 1.362 | 396 | 1.069,05 EUR |
| lead_only | 5 | 187 | 73 | 0,00 EUR |
| spend_only | 2 | 0 | 0 | 2,20 EUR |

`lead_only` no significa captación gratuita. `spend_only` no significa cero leads reales. Ambos estados condicionan cualquier decisión económica.

## Calidad Y Señales

La señal más fuerte es la intención asociada a billetes/status. Los leads con `tiene_billetes = true` tienen 195 A/B de 218 leads, un 89,45%. Los leads sin billetes tienen 274 A/B de 1.331, un 20,59%.

Por `ticket_status`, `solo_mirando` concentra volumen pero baja calidad: 53 A/B de 955 leads. `en_proceso` tiene 221 A/B de 376. `tiene_billetes` tiene 195 A/B de 218. Esta lectura es asociativa y no prueba conversión comercial.

## Campaña, Adset Y Ads

La estructura principal de captación aporta 1.267 leads y 370 A/B. También concentra la mayor parte del spend matched derivado por anuncio. RTG/DIASPORA muestra una tasa A/B mayor en lead-side, pero queda como `lead_only` para spend comercial matched en esta ejecución, por lo que no sostiene una comparación económica completa.

Los dos anuncios con más volumen aportan 1.002 leads. Esto permite lectura descriptiva robusta de concentración, pero no causalidad creativa. `ad_name` se usa solo como etiqueta interpretativa; la clave técnica es `ad_id_norm`.

## Temporalidad

La calidad mensual es estable: abril parcial 30,98% A/B, mayo 30,08%, junio 29,51%, julio parcial 32,73%. No hay evidencia de deterioro material. La lectura semanal y el coste-calidad temporal quedan `partial` porque hay semanas parciales y las consultas de spend temporal fueron rechazadas por política de coste.

## Knowledge Estabilizado

1. VCA compra escala, pero la calidad alta es minoritaria.
2. El coste-calidad matched es eficiente, siempre que no se mezcle con `lead_only` o `spend_only`.
3. La intención declarada o status equivalente separa calidad mucho más que el volumen agregado.
4. Hay dependencia de pocas estructuras y anuncios.
5. Hay posible calidad fuera de la base dominante, pero con cobertura económica parcial.
6. La calidad lead-side no muestra deterioro temporal claro.

## Recomendaciones

| ID | Tipo | Prioridad | Acción |
| --- | --- | --- | --- |
| REC-001 | measurable_experiment | Alta | Test controlado de pre-cualificación por intención/billetes. |
| REC-002 | verifiable_action | Alta | Revisar y documentar causas de `lead_only` y `spend_only`. |
| REC-003 | measurable_experiment | Media-alta | Diversificar mensajes/creativos con tracking por `ad_id_norm`. |
| REC-004 | non_actionable_hypothesis | Media | Tratar la mejora parcial de julio como hipótesis pendiente. |

No se recomienda redistribución presupuestaria inmediata, ganador creativo ni optimización por revenue porque la evidencia no alcanza esos claims.

## Matriz SPEC-014

Las preguntas obligatorias AQ-001, AQ-002, AQ-003, AQ-006, AQ-007, AQ-008, AQ-010 y AQ-011 quedan `complete`. AQ-004, AQ-005 y AQ-009 quedan `partial` por límites de campaign/adset economics, causalidad creativa y temporalidad coste-calidad. Las condicionales quedan `partial`, `not_available` o `not_applicable` según la matriz física.

## Limitaciones

- Spend temporal rechazado por política de coste; no se usa como evidencia.
- La consulta combinada de reconciliación fue rechazada por scope; la reconciliación se construyó desde agregados separados.
- No hay revenue ni conversión comercial reconciliada.
- No hay metadata creativa más allá de `ad_name`.
- No hay causalidad validada.

