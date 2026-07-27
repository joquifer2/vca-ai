# AUC-001 Informe analitico canonico enriquecido

## Limite de fuentes

Este informe es una proyeccion de Presentation Layer para AUC-001. Consume solo los artefactos canonicos actuales de este paquete: Evidence Set, Analytical Investigation Record, Findings intermedios, Knowledge Set, Recommendation Set, Common Product Core y Canonical Projection Source. Los outputs historicos no son evidencia, no son valores esperados y no son leidos por este materializador.

La ruta canonica enriquecida es la salida estable de AUC-001: conserva dimensiones, tablas, hipotesis, limites y soporte a decision, y cada valor, UNKNOWN y recomendacion queda limitado por el paquete canonico actual. Fingerprint del Canonical Projection Source: `60fb82e9d268e5c062fea581b453bb23f355236a037299ba1de4fc76b7ec361d`.

## Mapa de cobertura funcional

| Dimension | Estado | Fuente canonica | Consecuencia para decision |
|---|---:|---|---|
| Tiers de calidad | available | lead_tier_total | Se reporta con valores canonicos actuales. |
| Evolucion mensual | available | monthly_tier | Se reporta con valores canonicos actuales. |
| Patron semanal | not_available | not_available en Evidence Set canonico | Se conserva como UNKNOWN; no se usa historico ni inferencia. |
| Plataforma | available | platform | Se reporta con valores canonicos actuales. |
| Senales de intencion | available | ticket_status, travel_window | Se reporta con valores canonicos actuales. |
| Campana | available | campaigns | Se reporta con valores canonicos actuales. |
| Conjunto de anuncios | not_available | not_available en Evidence Set canonico | Se conserva como UNKNOWN; no se usa historico ni inferencia. |
| Anuncio | available | top_ads | Se reporta con valores canonicos actuales. |
| Inversion por senal FARO | available | spend_by_signal, commercial_matched | Se reporta con valores canonicos actuales. |
| Inversion temporal | not_available | not_available en Evidence Set canonico | Se conserva como UNKNOWN; no se usa historico ni inferencia. |
| Inversion por anuncio | not_available | not_available en Evidence Set canonico | Se conserva como UNKNOWN; no se usa historico ni inferencia. |
| Cobertura y UNKNOWNs | available | commercial_matched | Se reporta con valores canonicos actuales. |
| Recomendaciones | available | recommendation-set | Se reporta con valores canonicos actuales. |

## Lectura analitica integrada

La evidencia canonica muestra 1329 leads hasta el 30 de junio de 2026, con 397 leads A/B y 58 Tier A. La lectura principal ya no es una lista de metricas: Meta genera volumen cualificado suficiente para seguir aprendiendo, pero la calidad no mejora por volumen puro. La densidad A/B se mantiene estable mientras junio escala, y el peso C/D sigue siendo material. Por eso la decision no debe premiar solo captacion; debe proteger volumen cualificado y reducir ruido operativo.

El AIR enriquecido identifica como hallazgo estructural la separacion por intencion observable. `tiene_billetes`, `en_proceso` y las ventanas cercanas concentran mucha mas calidad que los buckets exploratorios. Este patron conecta volumen, calidad y accion: Marketing puede formular tests sobre senales de intencion, mientras Direccion puede exigir salvaguardas de volumen A/B y Tier A antes de aprobar cambios de presupuesto.

La lectura economica queda acotada por FARO. COMMERCIAL matched es el unico universo directo coste-calidad. ATTENTION y ACTIVATION se preservan como capas no equivalentes; por tanto, no hay ranking economico universal entre capas. Las dimensiones ausentes se mantienen como not_available o UNKNOWN, sin completarlas desde historicos.

## Estructura de calidad

| Tier | Leads | Peso | Score medio |
|---|---:|---:|---:|
| A | 58 | 4.4% | 86.9828 |
| B | 339 | 25.5% | 67.9912 |
| C | 554 | 41.7% | 48.8285 |
| D | 378 | 28.4% | 29.2143 |

La tabla confirma una tension directiva: hay base cualificada real, pero tambien una masa C/D que puede consumir capacidad comercial. La prioridad analitica es distinguir escala util de escala ruidosa.

## Evolucion mensual

| Mes | Leads | A/B | Tier A | Tasa A/B |
|---|---:|---:|---:|---:|
| 2026-04 | 184 | 57 | 8 | 31.0% |
| 2026-05 | 369 | 111 | 19 | 30.1% |
| 2026-06 | 776 | 229 | 31 | 29.5% |

Junio aporta mas volumen y mas A/B absolutos, pero no prueba mejora estructural de densidad. La implicacion es clara: escalar funciona como crecimiento de pipeline, no todavia como optimizacion de calidad.

## Senales de intencion y scoring

| Senal | Bucket | Leads | A/B | Tier A | Tasa A/B |
|---|---|---:|---:|---:|---:|
| Estado de billete | solo_mirando | 838 | 48 | 0 | 5.7% |
| Estado de billete | en_proceso | 314 | 192 | 11 | 61.1% |
| Estado de billete | tiene_billetes | 177 | 157 | 47 | 88.7% |
| Ventana de viaje | aun_no_claro | 463 | 26 | 0 | 5.6% |
| Ventana de viaje | entre_3_y_6_meses | 342 | 100 | 5 | 29.2% |
| Ventana de viaje | entre_1_y_3_meses | 142 | 94 | 12 | 66.2% |
| Ventana de viaje | menos_de_1_mes | 80 | 74 | 26 | 92.5% |

La intencion es el eje explicativo mas fuerte. Los leads con billetes, proceso de compra o ventana cercana muestran mucha mayor densidad A/B y Tier A. La conclusion sigue siendo observacional: sirve para disenar tests, no para declarar causalidad.

## Plataforma, campana y concentracion por anuncio

| Nivel | Elemento | Leads | A/B | Tier A | Tasa A/B |
|---|---|---:|---:|---:|---:|
| Plataforma | fb | 894 | 278 | 39 | 31.1% |
| Plataforma | ig | 435 | 119 | 19 | 27.4% |
| Campana | [META]_[CLP]_[CAPTACION]_[ABO] | 1187 | 344 | 48 | 29.0% |
| Campana | [META]_[CLP]_[RTG]_[CBO] | 142 | 53 | 10 | 37.3% |
| Anuncio | 120245828603090721 | 643 | 187 | 23 | 29.1% |
| Anuncio | 120245829545180721 | 359 | 101 | 17 | 28.1% |
| Anuncio | 120247352473020721 | 118 | 42 | 9 | 35.6% |

La comparacion por plataforma y campana ayuda a ordenar el trabajo, pero no desplaza el hallazgo de intencion. Retargeting aparece con mayor densidad y adquisicion con mayor volumen cualificado; eso exige diseno de portfolio, no sustitucion simplista. Los anuncios concentrados orientan inspeccion y test, pero no prueban causalidad creativa.

## Coste, calidad y limites FARO

| Capa FARO | Inversion | Leads | A/B | Coste por A/B | Estado de decision |
|---|---:|---:|---:|---:|---|
| COMMERCIAL matched | 873.65 EUR | 1187 | 344 | 2.54 EUR | universo directo coste-calidad |
| ACTIVATION observed | 221.18 EUR | 142 | 53 | 4.17 EUR | capa FARO no equivalente |
| ATTENTION total | 308.54 EUR | UNKNOWN | UNKNOWN | UNKNOWN | solo inversion de capa |
| COMMERCIAL total | 875.85 EUR | UNKNOWN | UNKNOWN | UNKNOWN | solo inversion de capa |
| ACTIVATION total | 221.86 EUR | UNKNOWN | UNKNOWN | UNKNOWN | solo inversion de capa |
| TOTAL total | 1406.25 EUR | UNKNOWN | UNKNOWN | UNKNOWN | solo inversion de capa |

COMMERCIAL matched permite lectura directa: coste por A/B y coste por Tier A dentro de un universo reconciliado. ACTIVATION y ATTENTION no deben tratarse como si compitieran por el mismo KPI de eficiencia. Esta separacion reduce el riesgo de reasignar presupuesto desde una metrica seductora pero estrategicamente no comparable.

## Hipotesis evaluadas

| Hipotesis | Estado | Razonamiento canonico |
|---|---|---|
| El volumen por si solo explica la calidad | Descartada | El AIR muestra que la intencion separa calidad mejor que el volumen bruto. |
| Las senales de intencion explican la separacion A/B y Tier A | Soportada observacionalmente | Ticket status y travel window concentran calidad en buckets de mayor preparacion. |
| Un KPI universal puede rankear todas las capas FARO | Descartada | COMMERCIAL, ATTENTION y ACTIVATION son capas no equivalentes. |
| Los top ads prueban ganador creativo | UNKNOWN | Hay concentracion, pero falta causalidad creativa. |
| La densidad de retargeting justifica sustituir adquisicion | No demostrado | Retargeting aporta densidad; adquisicion aporta volumen cualificado. La decision es de portfolio. |
| Las dimensiones ausentes pueden rellenarse desde historicos | Descartada | Solo se aceptan artefactos canonicos actuales. |

## Conocimiento generado

| ID | Afirmacion | Interpretacion | Limite |
|---|---|---|---|
| K-001 | Meta aporta volumen cualificado material: 397 leads A/B y 58 leads Tier A. | La lectura operativa es que el canal es viable, pero la convivencia de calidad A/B con ruido C/D exige filtros de intencion antes de escalar decisiones. | La calidad de revenue y la conversion CRM permanecen UNKNOWN. |
| K-002 | Junio escala volumen cualificado sin probar una mejora estructural de calidad. | Como la densidad A/B mensual se mantiene cercana entre meses mientras crece el conteo de leads, mejora mas la escala absoluta que la densidad de calidad. | La dinamica semanal esta not_available, por lo que no se declara causalidad intra-mes. |
| K-003 | La intencion explicita de viaje es el separador de calidad mas fuerte observado. | Los buckets de intencion explican mejor la brecha entre demanda exploratoria y concentracion A/B o Tier A que la plataforma o el volumen por si solos. | Es una asociacion observacional, no una prueba causal. |
| K-004 | La interpretacion economica debe mantenerse dentro de los universos FARO gobernados. | COMMERCIAL matched permite lectura directa coste-calidad, mientras ATTENTION y ACTIVATION siguen siendo capas no equivalentes. | Un ranking coste-calidad universal entre capas FARO es invalido. |
| K-005 | Las decisiones de portfolio deben equilibrar escala de adquisicion y densidad de retargeting. | Adquisicion concentra la mayor parte del volumen cualificado, mientras retargeting muestra una bolsa de calidad mas densa pero menor; como los universos difieren, el aprendizaje es balance de portfolio y no sustitucion. | Los cruces por conjunto de anuncios e inversion temporal estan not_available. |
| K-006 | La concentracion por anuncio sirve para priorizar tests, no para declarar ganadores creativos. | Los anuncios principales concentran volumen y leads A/B, lo que justifica prioridad de inspeccion; la causalidad sigue bloqueada sin metadata creativa o tests controlados. | La causalidad creativa permanece UNKNOWN. |
| K-007 | Las dimensiones ausentes son limites de decision, no huecos que rellenar con outputs historicos. | Calidad semanal, segmentacion por conjunto de anuncios, inversion temporal y cruces inversion-anuncio deben seguir como not_available hasta que exista evidencia canonica actual. | Los outputs historicos no son evidencia ni valores esperados. |

La narrativa integrada estabilizada resume la idea central: La tesis integrada es que Meta ya genera volumen cualificado suficiente para seguir invirtiendo aprendizaje, pero la calidad se separa sobre todo por intención observable y no por volumen puro. El hallazgo estructural es la combinación de ruido C/D alto, densidad A/B estable durante la escala de junio y señales de intención muy discriminantes. El trade-off principal es aumentar volumen sin diluir calidad operativa. El riesgo dominante es convertir capas FARO no equivalentes en un ranking económico universal. La implicación estratégica es proteger COMMERCIAL matched como universo de decisión económica y usar intención explícita como hipótesis de test.

Idea memorable: La calidad no esta escondida en mas volumen; esta concentrada en senales de intencion verificables.

## Recomendaciones

| ID | Prioridad | Tipo | Accion o hipotesis | Metrica / salvaguarda | Soporte canonico |
|---|---|---|---|---|---|
| R-001 | high | measurable_experiment | Ejecutar un test controlado en COMMERCIAL matched que enfatice estado de billete e intencion de ventana cercana en copy, formulario o routing. | Tasa de leads A/B y conteo Tier A en COMMERCIAL matched.; salvaguarda: No reducir el volumen cualificado A/B por debajo de la referencia mensual actual. | K-003, K-004 |
| R-002 | high | verifiable_action | Mantener ATTENTION, ACTIVATION y COMMERCIAL en bloques de decision separados en todo informe AUC-001. | Ningun informe contiene un ranking KPI universal entre capas FARO.; salvaguarda: SPEC-017 y los checks de Presentation preservan la separacion de capas. | K-004 |
| R-003 | medium | measurable_experiment | Evaluar adquisicion y retargeting como roles complementarios, no como candidatos de sustitucion. | Volumen A/B y tasa A/B por rol de campana.; salvaguarda: No mover presupuesto solo por densidad sin comprobar volumen absoluto cualificado. | K-005 |
| R-004 | medium | non_actionable_hypothesis | Los clusters principales de ad_id_norm pueden contener encuadres de intencion reutilizables. | Promover solo despues de que un experimento controlado futuro conecte variacion creativa con calidad.; salvaguarda: UNKNOWN | K-006 |
| R-005 | medium | verifiable_action | Mantener calidad semanal, segmentacion por conjunto de anuncios, inversion temporal y cruces inversion-anuncio fuera de decisiones de optimizacion hasta que exista evidencia canonica actual. | Los informes marcan estas dimensiones como not_available o UNKNOWN.; salvaguarda: Una ejecucion futura materializa estas dimensiones mediante evidencia MCP autorizada antes de usarlas. | K-007 |

## Riesgos, UNKNOWNs y limites de decision

| Area | Estado | Consecuencia |
|---|---|---|
| Revenue / CRM | UNKNOWN | No declarar valor comercial final mas alla de calidad de lead. |
| Causalidad creativa | UNKNOWN | Usar top ads para priorizar tests, no para declarar ganadores. |
| Patron semanal | not_available | No inferir dinamica intra-mes. |
| Conjunto de anuncios | not_available | No optimizar ad sets desde este paquete. |
| Inversion temporal o por anuncio | not_available | Mantener coste-calidad en COMMERCIAL matched y capas FARO gobernadas. |
| ATTENTION asistida | UNKNOWN | No atribuir efecto comercial sin evidencia downstream. |

## Uso para Direccion y Marketing

Para Direccion, el paquete permite una decision acotada: mantener Meta como canal con volumen cualificado medible, exigir separacion FARO y aprobar solo experimentos con salvaguardas de A/B, Tier A y volumen cualificado. Para Marketing, el trabajo inmediato es operativo: transformar senales de intencion en hipotesis de copy, formulario, routing o segmentacion, inspeccionar anuncios concentrados como candidatos de test y no tratar C/D exploratorio como demanda comercial equivalente.
