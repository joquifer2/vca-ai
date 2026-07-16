# AUC-001 Analytical Contract

## Metadata

| Field | Value |
|---|---|
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Contract Type | Analytical operating contract |
| Status | Active |
| Scope | What AUC-001 must be able to answer and what it needs to do so |

El caso de uso base permanece activo y validado en [analytical_use_cases/meta_lead_quality_analysis.md](../meta_lead_quality_analysis.md); este contrato fija la articulacion operativa vigente del caso de uso.

## 1. Propósito

AUC-001 existe para producir una lectura analitica estable sobre la calidad de leads en Meta Ads, la eficiencia de la inversion y las implicaciones de negocio derivadas de esa lectura.

El caso de uso debe convertir evidencia trazable en conocimiento util para negocio, preservando separacion entre observacion, interpretacion, recomendacion y presentacion.

## 2. Preguntas analíticas

La lista canonica de preguntas que AUC-001 debe responder es la siguiente:

1. Cuanto volumen de captacion existe y como evoluciona?
2. Que parte del volumen es calidad y como se separan niveles de calidad alta, media y baja?
3. Que tan eficiente es la inversion?
4. Que campañas o conjuntos generan la mejor combinacion de volumen, calidad y coste?
5. Que creatividades o anuncios concentran valor o desperdicio?
6. Que señales explican mejor la calidad observada?
7. Que trade-offs existen entre volumen, calidad y coste?
8. Donde se concentra el valor y cuanta dependencia hay de pocos activos?
9. Como se relacionan las variables entre si?
10. Como cambia la calidad en el tiempo?
11. Hay diferencias por plataforma o superficie?
12. Que impacto esperado tiene esto sobre Meta y su optimizacion?
13. Que oportunidades de optimizacion aparecen?

## 3. Knowledge esperado

| Pregunta | Knowledge esperado |
|---|---|
| Volumen | Dimension del embudo, lectura de escala y comportamiento por periodo |
| Calidad | Gradiente operativo de calidad y separacion entre categorias relevantes |
| Eficiencia | Lectura economica de coste-calidad y coste por nivel de resultado |
| Campañas y conjuntos | Comparacion de rendimiento por estructura de media |
| Creatividades y anuncios | Concentracion y eficiencia por activo publicitario |
| Senales explicativas | Variables o respuestas que distinguen mejor la calidad observada |
| Trade-offs | Tension entre volumen, calidad y coste |
| Concentracion | Dependencia de pocos activos y peso relativo del top performer |
| Relaciones entre variables | Asociaciones observables entre variables sin afirmar causalidad no validada |
| Evolucion temporal | Tendencia, estabilidad, deterioro o mejora |
| Plataforma | Diferencias por canal, superficie o segmento cuando exista la dimension |
| Impacto sobre Meta | Implicaciones sobre aprendizaje, senales y optimizacion |
| Oportunidades | Priorizacion de donde hay mayor potencial de mejora |

## 4. Findings necesarios

| Knowledge | Findings necesarios |
|---|---|
| Volumen | Totales por periodo, variacion, distribucion por segmento y brechas entre universo total y universo utilizable |
| Calidad | Distribucion de score o tier, umbral operativo, diferencias entre categorias y presencia o ausencia de high quality |
| Eficiencia | Spend, CPL, CPQL, CPHQL o equivalentes, y coste por segmento |
| Campañas y conjuntos | Ranking por campaign y adset, calidad vs coste por estructura y separacion de coverage states |
| Creatividades y anuncios | Ranking de anuncios o creatividades, concentracion del resultado y comparacion entre activos top y long tail |
| Senales explicativas | Cruces de variables, thresholds, diferenciales entre categorias y combinacion de senales |
| Trade-offs | Casos donde volumen, calidad y coste entran en tension |
| Concentracion | Shares de contribucion, dependencia del top asset y lectura top-heavy |
| Relaciones entre variables | Tablas cruzadas, patrones combinados, interacciones y co-ocurrencias relevantes |
| Evolucion temporal | Series comparables, ventanas periodicas y cambios en eficiencia o calidad |
| Plataforma | Comparaciones entre plataformas, superficies o segmentos |
| Impacto sobre Meta | Mapping entre calidad, eventos, aprendizaje y cobertura de senales |
| Oportunidades | Identificacion de activos, segmentos o coberturas con mayor potencial |

## 5. Capacidades analíticas requeridas

AUC-001 debe ser capaz de:

- agrupar observaciones por unidad de inversion;
- ordenar observaciones temporalmente;
- distinguir niveles de calidad;
- distribuir observaciones por superficie o segmento;
- identificar activos publicitarios relevantes;
- medir eficiencia economica;
- detectar concentracion;
- analizar relaciones entre variables;
- evaluar trade-offs entre volumen, calidad y coste;
- identificar anomalías o comportamientos atipicos;
- separar coverage states no equivalentes;
- conservar limites de interpretacion cuando la evidencia es parcial.

## 6. Representación actual

Las capacidades anteriores se satisfacen actualmente en AUC-001 mediante estas representaciones contingentes. Esta tabla describe materializaciones actuales; no redefine el contrato analitico, que se expresa en las capacidades de las secciones anteriores.

| Capacidad analitica | Representacion actual |
|---|---|
| Agrupar observaciones por unidad de inversion | campaign_id, adset_id |
| Ordenar observaciones temporalmente | week, date o granularidad temporal equivalente |
| Distinguir niveles de calidad | lead_tier, qualified AB y high quality donde exista |
| Distribuir observaciones por superficie o segmento | platform, audience segment o dimension equivalente |
| Identificar activos publicitarios | ad reference o identificador de anuncio equivalente |
| Medir eficiencia economica | spend y ratios derivados sobre universos emparejados |
| Detectar concentracion | ranking y shares por campaign, adset o ad reference |
| Analizar relaciones entre variables | cruces y comparaciones entre senales, categorias y resultados |
| Evaluar trade-offs | lectura conjunta de volumen, calidad y coste |
| Identificar anomalías | flags de validez, coverage states y excepciones observables |
| Separar coverage states | matched, lead_only y spend_only |
| Conservar limites de interpretacion | UNKNOWNs, limitaciones y notas de cobertura |

Estas representaciones son contingentes y pueden cambiar sin modificar el contrato analitico.

## 7. Cobertura del contrato

### Capacidades plenamente cubiertas

- medir volumen por periodo;
- distinguir calidad observable en el universo disponible;
- medir eficiencia economica en los casos emparejados;
- comparar campaign y adset cuando exista cobertura;
- identificar concentracion por activo o estructura;
- preservar coverage states y limites de interpretacion.

### Capacidades parcialmente cubiertas

- lectura de creatividades, porque la representacion actual es util pero no expresa toda la metadata de asset;
- analisis de señales explicativas, porque solo parte de las variables necesarias esta materializada;
- evolucion temporal, porque no todas las preguntas tienen la misma profundidad de cobertura;
- lectura por plataforma o superficie, porque la dimension no siempre esta disponible de forma completa;
- impacto sobre Meta, porque depende de mapping de senales y de evidencia parcial.

### Capacidades fuera del contrato actual

- causalidad validada;
- planes de ejecucion;
- recomendaciones operativas como parte del contrato analitico;
- uso de fuentes no trazadas;
- ampliacion del alcance mediante supuestos no verificados.

## 8. Límites del contrato

El contrato de AUC-001 acepta como limites actuales:

- la separacion entre matched, lead_only y spend_only;
- la imposibilidad de mezclar coberturas como si fueran equivalentes;
- la falta de equivalencia total entre ad reference y metadata creativa completa;
- la dependencia de algunas lecturas respecto de variables explicativas que no estan siempre materializadas;
- la cobertura temporal y de plataforma solo cuando existan en la evidencia disponible;
- la ausencia de causalidad demostrada para asociaciones observadas;
- la necesidad de declarar UNKNOWN cuando la evidencia no alcanza.

## Referencias de soporte

Este contrato consolida conocimiento validado en:

- [docs/evaluations/auc-001/investigations/auc-001-knowledge-construction-comparative-analysis.md](/docs/evaluations/auc-001/investigations/auc-001-knowledge-construction-comparative-analysis.md)
- [docs/evaluations/auc-001/investigations/auc-001-analytical-investigation-analysis.md](/docs/evaluations/auc-001/investigations/auc-001-analytical-investigation-analysis.md)
- [docs/evaluations/auc-001/validations/auc-001-knowledge-depth-recovery-validation.md](/docs/evaluations/auc-001/validations/auc-001-knowledge-depth-recovery-validation.md)
- [docs/evaluations/auc-001/investigations/auc-001-minimum-evidence-contract-analysis.md](/docs/evaluations/auc-001/investigations/auc-001-minimum-evidence-contract-analysis.md)

La lectura del contrato debe hacerse junto con [analytical_use_cases/meta_lead_quality_analysis.md](../meta_lead_quality_analysis.md) como documento base del caso de uso.