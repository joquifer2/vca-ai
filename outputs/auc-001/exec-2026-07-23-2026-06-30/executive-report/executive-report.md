# Informe ejecutivo - Calidad de leads Meta Ads

## Contexto de ejecucion

| Campo | Valor |
|---|---|
| Caso | AUC-001 - Meta Lead Quality Analysis |
| Solicitud original | Genera el informe ejecutivo de calidad de los leads hasta el 30 de junio de 2026. |
| Modo | Ejecucion completa con evidencia nueva via BigQuery MCP Server |
| Periodo resuelto | 2026-04-18 a 2026-06-30 |
| Fecha de corte | 2026-06-30 |
| Audiencia | Direccion / decision ejecutiva |
| Proyeccion | Executive decision support |
| Estado de entrega | READY_FOR_REVALIDATION; no constituye aceptacion QA final |

## Resumen ejecutivo

Meta genero 1.329 leads entre el 18 de abril y el 30 de junio de 2026. El volumen se acelero claramente en junio, que concentro 776 leads, el 58,4% del total del periodo. La lectura de calidad no acompana esa escala con la misma fuerza: los leads Tier A fueron 58, el 4,4% del total, y los leads A/B fueron 397, el 29,9%.

La tesis ejecutiva es clara: Meta esta comprando volumen con una base cualificada estable pero limitada. El sistema genera senal suficiente para optimizar, pero la mayor parte de la captacion sigue en Tier C/D o en estados de baja intencion. La decision no deberia ser "invertir mas o menos" de forma agregada, sino proteger el volumen que ya produce aprendizaje y desplazar la optimizacion hacia combinaciones, anuncios y respuestas que elevan la proporcion A/B.

La eficiencia economica canonicamente comparable existe solo en el universo comercial emparejado. En ese universo, 1.187 leads estan asociados a 873,65 euros de spend comercial, con un coste por lead matched de 0,74 euros y un coste por lead A/B matched de 2,54 euros. Estos costes son bajos, pero no deben leerse como eficiencia completa si se ignora que solo 344 de los 1.187 leads matched fueron A/B.

## Mensajes clave

1. El crecimiento de junio es real, pero no transforma la calidad.
   Junio aporta 776 leads, frente a 184 en abril parcial y 369 en mayo. La tasa A/B mensual baja suavemente de 31,0% en abril parcial a 30,1% en mayo y 29,5% en junio. El volumen escala, la calidad relativa permanece practicamente plana.

2. La calidad se concentra en una minoria operativa.
   Tier A representa 58 leads y Tier B 339. En conjunto, A/B son 397 leads. El resto, 932 leads, queda en Tier C/D. La implicacion es que Meta entrega suficiente senal util, pero todavia compra mucho volumen de baja calidad relativa.

3. El coste comercial matched es eficiente en terminos unitarios, pero el indicador de decision es coste-calidad, no CPL generico.
   El universo matched muestra 873,65 euros de inversion comercial para 1.187 leads, con 344 A/B. La metrica ejecutiva relevante es `cost_per_ab_commercial_matched` = 2,54 euros, no un CPL sin cobertura.

4. La campana de captacion explica casi todo el volumen, pero el retargeting aporta mejor tasa A/B en menor escala.
   La campana `[META]_[CLP]_[CAPTACION]_[ABO]` concentra 1.187 leads y 344 A/B, con tasa A/B de 29,0%. La linea `[META]_[CLP]_[RTG]_[CBO]` aporta 141 leads y 53 A/B, con tasa A/B de 37,6%. Es una senal de calidad interesante, pero con menor volumen y sin coste comercial matched comparable en esta ejecucion.

5. Dos anuncios sostienen gran parte del sistema.
   `ViajeSinEstres_AlivioEmocional...` genera 643 leads y 187 A/B. `ViajaComoInvitado_Identidad...` genera 359 leads y 101 A/B. Juntos concentran 1.002 leads, el 75,4% del total, y 288 leads A/B, el 72,5% del total A/B. Esta concentracion da escala, pero crea dependencia.

6. Las respuestas de formulario separan con mucha fuerza la calidad.
   Combinaciones con "estoy en proceso de compra", ventana de viaje definida y organizacion completa alcanzan 100% A/B en varios grupos con al menos 10 leads. En el extremo contrario, "no solo estoy mirando" con fecha no clara y valoracion de opciones produce grupos grandes con 0% A/B. La calidad observada esta muy ligada a intencion declarada y claridad del viaje.

## Indicadores principales

| Indicador | Valor |
|---|---:|
| Leads totales | 1.329 |
| Leads Tier A | 58 |
| Leads Tier B | 339 |
| Leads A/B | 397 |
| Tasa A/B global | 29,9% |
| Score medio FARO | 49,80 |
| Leads con billetes | 177 |
| Spend total todas las senales | 1.406,25 EUR |
| Spend comercial | 875,85 EUR |
| Spend comercial matched | 873,65 EUR |
| Spend comercial spend_only | 2,20 EUR |
| Leads matched | 1.187 |
| Leads lead_only | 142 |
| Coste por lead matched | 0,74 EUR |
| Coste por lead A/B matched | 2,54 EUR |

## Evolucion temporal

| Mes | Leads | Leads A/B | Tasa A/B | Score medio |
|---|---:|---:|---:|---:|
| Abril parcial | 184 | 57 | 31,0% | 50,71 |
| Mayo | 369 | 111 | 30,1% | 49,27 |
| Junio | 776 | 229 | 29,5% | 49,84 |

La evolucion mensual sugiere estabilidad de calidad relativa y aumento de volumen. La lectura semanal es parcial: existen semanas incompletas o con volumen bajo, por lo que no debe usarse como base concluyente para cambios tacticos finos. Aun asi, la semana iniciada el 15 de junio muestra una tasa A/B destacada de 38,7% sobre 194 leads, mientras que la semana iniciada el 29 de junio es parcial y no comparable.

## Lectura por inversion y activos

| Activo / linea | Leads | A/B | Tasa A/B | Spend comercial matched | Lectura ejecutiva |
|---|---:|---:|---:|---:|---|
| ViajeSinEstres_AlivioEmocional... | 643 | 187 | 29,1% | 468,06 EUR | Principal motor de escala; eficiencia baja por coste unitario, calidad relativa media. |
| ViajaComoInvitado_Identidad... | 359 | 101 | 28,1% | 245,84 EUR | Segundo motor de volumen; muy dependiente de escala, no mejora la tasa A/B. |
| FiltroBilletes_EscasezReal_3Tips... RTG | 118 | 42 | 35,6% | not_available | Mejor tasa entre activos con volumen relevante, pero sin spend comercial matched para coste-calidad. |
| FiltroBilletes_AutoSegmentacion... | 58 | 22 | 37,9% | 48,96 EUR | Mejor equilibrio matched entre calidad y coste con volumen moderado. |
| ExperienciasUnicas_BoriWine2026... | 67 | 8 | 11,9% | 50,03 EUR | Volumen moderado con baja calidad relativa; candidato a revision. |

La comparacion debe leerse con cautela: los rankings por anuncio son robustos para los dos grandes motores de volumen, pero varias referencias tienen muestras pequenas. `ad_name` se usa solo como etiqueta interpretativa, no como clave tecnica ni prueba causal de creatividad.

## Senales que explican la calidad

El componente FARO mas discriminante es la intencion de compra del viaje, especialmente billetes y fecha. Los Tier A promedian 86,98 puntos; Tier B 67,99; Tier C 48,83; Tier D 29,21. La separacion entre tiers no depende de una sola metrica aislada, pero las mayores diferencias aparecen en billetes, fecha de viaje y tipo de experiencia.

`ticket_status` esta disponible como dimension post-lead descriptiva: `tiene_billetes` alcanza 88,7% A/B, `en_proceso` 61,2% A/B y `solo_mirando` 5,7% A/B. Esta dimension refuerza la lectura de intencion, pero no debe convertirse en conversion comercial ni revenue porque la fuente CRM/revenue reconciliada no forma parte del alcance autorizado de esta ejecucion.

Facebook aporta 894 leads con 31,1% A/B; Instagram aporta 435 leads con 27,4% A/B. La diferencia es util como senal descriptiva, pero no autoriza causalidad de plataforma ni reasignacion automatica sin coste/calidad por superficie.

## Decisiones recomendadas

| Prioridad | Recomendacion | Tipo | Criterio de exito |
|---|---|---|---|
| Alta | Reasignar pruebas hacia combinaciones de formulario con intencion fuerte: billetes en proceso o comprados, ventana definida y organizacion completa. | Experimento medible | Subir tasa A/B matched sin reducir materialmente el volumen semanal util; guardrail: mantener coste por A/B matched en rango comparable. |
| Alta | Proteger los dos anuncios de mayor volumen, pero no escalar presupuesto solo por volumen. Exigir mejora o estabilidad de tasa A/B como condicion de escala. | Accion verificable | Mantener volumen y evitar deterioro de tasa A/B mensual por debajo del nivel observado del periodo. |
| Media-alta | Revisar `ExperienciasUnicas_BoriWine2026...` antes de ampliarlo: tiene spend matched y volumen moderado, pero baja tasa A/B. | Experimento medible | Mejorar tasa A/B del activo o reducir exposicion si no converge tras una ventana definida. |
| Media | Tratar el retargeting como fuente de calidad prometedora, no como ganador economico cerrado. | Hipotesis no accionable aun | Resolver coste-calidad matched o clasificar su spend por universo comparable antes de escalar por eficiencia. |
| Media | Mantener visible la brecha CRM/revenue antes de decisiones de negocio finales. | Accion verificable | Incorporar fuente comercial reconciliada o declarar formalmente que la decision se basa solo en scoring FARO y señales de intencion. |

## Riesgos y limitaciones

1. Revenue, ventas o conversion comercial reconciliada: `not_available`.
   La ejecucion contiene candidatos offline de `QualifiedLead`, pero no prueba revenue ni cierre comercial. Las decisiones deben basarse en calidad FARO e intencion, no en ventas.

2. Causalidad creativa: `UNKNOWN`.
   `ad_name` ayuda a leer etiquetas y mensajes, pero no demuestra que una creatividad cause mejor calidad.

3. Temporalidad semanal: `partial`.
   El periodo empieza el 18 de abril y termina el 30 de junio. Algunas semanas son parciales o de bajo volumen, por lo que la comparabilidad semanal completa no queda cerrada.

4. Coste-calidad por retargeting: `partial`.
   Hay leads de retargeting con buena tasa A/B, pero no spend comercial matched comparable para esa linea en la evidencia reconciliada.

5. Dependencia de pocos activos.
   Dos anuncios concentran la mayor parte de leads y A/B. Esto facilita aprendizaje, pero aumenta fragilidad ante fatiga creativa o cambios de entrega.

## Coverage ejecutivo

| Pregunta | Estado | Justificacion |
|---|---|---|
| AQ-001 Volumen y evolucion | complete | Leads totales, periodo y evolucion mensual disponibles. |
| AQ-002 Calidad FARO | complete | Tiers A/B/C/D y denominadores disponibles. |
| AQ-003 Coste-calidad reconciliada | complete | Universo matched, lead_only y spend_only preservado. |
| AQ-004 Campana/adset | partial | Lead-side disponible; coste por campana/adset no esta plenamente reconciliado. |
| AQ-005 Anuncio/creatividad | partial | `ad_id_norm` y `ad_name` disponibles; causalidad creativa no autorizada. |
| AQ-006 Senales explicativas | complete | Componentes FARO y combinaciones de formulario disponibles. |
| AQ-007 Trade-off volumen/calidad/coste | complete | Se observa tension entre escala, tasa A/B y coste matched. |
| AQ-008 Concentracion/dependencia | complete | Concentracion por anuncio cuantificada. |
| AQ-009 Temporalidad | partial | Mensual comparable; semanal parcial. |
| AQ-010 Oportunidades | complete | Recomendaciones trazadas a Knowledge estabilizado. |
| AQ-011 Limites | complete | UNKNOWN, partial y not_available declarados. |
| CQ-001 Plataforma | partial | Plataforma disponible lead-side; sin coste por superficie. |
| CQ-002 Post-lead / ticket_status | partial | `ticket_status` disponible; no equivale a CRM/revenue reconciliado. |
| CQ-006 Conversion/revenue | not_available | No hay fuente comercial reconciliada autorizada en esta ejecucion. |

## Trazabilidad MCP

Todas las cifras proceden de BigQuery MCP Server. No se uso `bq`, CLI, clientes directos, informes historicos ni Evidence Sets previos como fuente analitica.

Consultas principales: `auc001_exec_20260630_q_leads_summary`, `auc001_exec_20260630_q_leads_monthly`, `auc001_exec_20260630_q_leads_weekly`, `auc001_exec_20260630_q_leads_platform`, `auc001_exec_20260630_q_spend_signal`, `auc001_exec_20260630_q_spend_monthly_signal`, `auc001_exec_20260630_q_leads_by_ad`, `auc001_exec_20260630_q_spend_commercial_by_ad`, `auc001_exec_20260630_q_leads_by_campaign_adset`, `auc001_exec_20260630_q_leads_signals_form`, `auc001_exec_20260630_q_faro_components`, `auc001_exec_20260630_q_ticket_status`, `auc001_exec_20260630_q_offline_candidates`, `auc001_exec_20260630_q_mapping_quality`.

