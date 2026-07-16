# AUC-001 Minimum Evidence Contract Analysis

## Metadata

| Field | Value |
|---|---|
| Evaluation ID | VCA-AUC-001-EVAL-MEC-001 |
| Evaluation Type | Analytical contract reconstruction |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Status | Documented |
| Date | 2026-07-16 |
| Scope | Reconstruct the minimum evidence contract needed to answer the analytical questions AUC-001 must be able to answer |

## 1. Objetivo

Determinar cual es el contrato minimo de evidencia necesario para que AUC-001 pueda responder todas las preguntas analiticas que el caso debe soportar.

This analysis does not modify the Evidence Contract, BigQuery, Dataform, the Evidence Set or the current AUC. It only specifies what evidence is minimally required from the analytical need, not how to obtain it.

## 2. Metodo

El metodo parte exclusivamente de las preguntas de negocio.

Para cada pregunta se reconstruye la siguiente cadena:

```text
Pregunta de negocio
↓
Knowledge esperado
↓
Findings necesarios
↓
Evidencia minima
```

No se parte de las tablas existentes ni del modelo fisico. La evidencia minima se deriva de la necesidad analitica, no de la disponibilidad tecnica actual.

## 3. Preguntas analiticas minimas

La reconstruccion minima del caso AUC-001 requiere responder al menos estas preguntas:

| # | Pregunta de negocio | Knowledge esperado | Findings necesarios | Evidencia minima requerida |
|---|---|---|---|---|
| 1 | Cuanto volumen de captacion existe y como evoluciona? | Dimension del embudo y lectura de escala | Totales por periodo, variacion, distribucion por segmento | E-01, E-02, E-10, E-13 |
| 2 | Que parte del volumen es calidad y como se separa la calidad alta, media y baja? | Gradiente de calidad util para negocio | Distribucion de score o tier, diferencia entre categorias, tasa de calidad | E-01, E-04, E-11, E-13 |
| 3 | Que tan eficiente es la inversion? | Lectura economica de coste-calidad | Spend, CPL, CPQL, CPHQL o equivalentes, coste por segmento | E-03, E-04, E-05, E-13 |
| 4 | Que campañas o conjuntos generan mejor combinacion de volumen, calidad y coste? | Comparacion de rendimiento por estructura de media | Ranking por campaña, conjunto y cobertura | E-02, E-03, E-05, E-08, E-13 |
| 5 | Que creatividades o anuncios concentran valor o desperdicio? | Concentracion y eficiencia por activo | Ranking multicriterio por ad reference, creative pattern y coste | E-03, E-06, E-07, E-13 |
| 6 | Que señales explican mejor la calidad? | Variables explicativas y gradientes de intencion | Cruces de variables, thresholds, diferenciales entre categorias | E-09, E-11, E-14 |
| 7 | Que trade-offs existen entre volumen, calidad y coste? | Lectura de equilibrio y tension entre metricas | Parejas de metricas, comparacion multi-criterio, casos extremos | E-02, E-03, E-04, E-05, E-06, E-13 |
| 8 | Donde se concentra el valor y cuanta dependencia hay de pocos activos? | Concentracion y fragilidad estructural | Shares, Pareto-like concentration, top-heavy contribution | E-02, E-03, E-05, E-06, E-13 |
| 9 | Como se relacionan las variables entre si? | Relaciones observables y asociaciones no causales | Tablas cruzadas, patrones combinados, interacciones, co-ocurrencias | E-02, E-04, E-05, E-06, E-09, E-13 |
| 10 | Como cambia la calidad en el tiempo? | Tendencia, estabilidad, fatiga o mejora | Series temporales, ventanas comparables, cambios por cohorte | E-02, E-03, E-04, E-08, E-10 |
| 11 | Hay diferencias por plataforma? | Lectura por canal de distribucion | Comparaciones entre Facebook, Instagram u otras superficies | E-02, E-03, E-04, E-08, E-10 |
| 12 | Que impacto esperado tiene esto sobre Meta y su optimizacion? | Implicacion de negocio y de aprendizaje del algoritmo | Mapeo entre calidad, eventos, aprendizaje y cobertura de senales | E-01, E-04, E-11, E-12, E-13 |
| 13 | Que oportunidades de optimizacion aparecen? | Priorizacion de oportunidades y limites | Identificacion de activos, señales, segmentos o coberturas con mejor potencial | E-03, E-04, E-05, E-06, E-09, E-10, E-11, E-12, E-13 |

## 4. Knowledge esperado, findings y evidencia minima por pregunta

### 4.1 Volumen de captacion

Knowledge esperado:

El caso debe poder explicar si el volumen es suficiente, si crece o cae y si esta concentrado o distribuido.

Findings necesarios:

- totales por periodo;
- tendencias;
- volumen por segmento;
- brechas entre universo total y universo utilizable.

Evidencia minima:

- Obligatorio: E-01, E-02, E-10, E-13.
- Muy recomendable: E-08.
- Opcional: E-11, E-12.
- Fuera del alcance: datos macroeconómicos externos.

### 4.2 Calidad del lead

Knowledge esperado:

El caso debe distinguir calidad alta, media y baja y mostrar un gradiente claro de intencion o valor comercial.

Findings necesarios:

- distribucion de calidad;
- umbral operativo de calidad;
- diferencias entre categorias;
- presencia o ausencia de high quality.

Evidencia minima:

- Obligatorio: E-01, E-04, E-11, E-13.
- Muy recomendable: E-09.
- Opcional: E-12.
- Fuera del alcance: opiniones comerciales no trazadas.

### 4.3 Eficiencia economica

Knowledge esperado:

El caso debe saber que coste se paga por lead, qualified lead y high quality, y donde se pierde eficiencia.

Findings necesarios:

- spend;
- CPL/CPQL/CPHQL o equivalentes;
- diferencia entre volumen y coste;
- coste por segmento.

Evidencia minima:

- Obligatorio: E-03, E-04, E-05, E-13.
- Muy recomendable: E-10, E-11.
- Opcional: E-12.
- Fuera del alcance: ROAS si no hay revenue.

### 4.4 Campanas y conjuntos

Knowledge esperado:

El caso debe comparar rendimiento por campaign y adset sin mezclar coverage states.

Findings necesarios:

- ranking por campaign/adset;
- calidad vs coste por estructura;
- separacion de matched y lead_only;
- lectura de spend attribution solo donde exista.

Evidencia minima:

- Obligatorio: E-05, E-03, E-13.
- Muy recomendable: E-02, E-08, E-10.
- Opcional: E-12.
- Fuera del alcance: attribution de spend sin fields disponibles.

### 4.5 Creatividades y anuncios

Knowledge esperado:

El caso debe identificar que activos concentran rendimiento y cuales se quedan como volumen barato o calidad debil.

Findings necesarios:

- ranking de anuncios/creatividades;
- concentracion del resultado;
- trade-offs entre volumen y calidad;
- compare de activos top y long tail.

Evidencia minima:

- Obligatorio: E-06, E-03, E-13.
- Muy recomendable: E-07, E-10.
- Opcional: E-08, E-11.
- Fuera del alcance: metadata creativa de asset si no esta materializada.

### 4.6 Senales explicativas

Knowledge esperado:

El caso debe poder decir que variables o respuestas explican mejor la calidad observada.

Findings necesarios:

- gradiente entre categorias de una variable;
- combinacion de senales;
- separacion entre variables aisladas y patrones conjuntos.

Evidencia minima:

- Obligatorio: E-09, E-11, E-14.
- Muy recomendable: E-02, E-04, E-13.
- Opcional: E-12.
- Fuera del alcance: texto libre no codificado.

### 4.7 Trade-offs

Knowledge esperado:

El caso debe mostrar donde el volumen choca con la calidad o donde la calidad exige sacrificar escala.

Findings necesarios:

- activos top-heavy;
- pequenos con mejor tasa pero poca robustez;
- volumen barato con calidad debil;
- coste vs calidad.

Evidencia minima:

- Obligatorio: E-02, E-03, E-04, E-05, E-06, E-13.
- Muy recomendable: E-10, E-11.
- Opcional: E-12.
- Fuera del alcance: trade-offs externos al canal.

### 4.8 Concentracion

Knowledge esperado:

El caso debe identificar dependencia de pocos activos y el peso relativo del top performer.

Findings necesarios:

- shares de contribucion;
- Pareto-like contribution;
- dependencia del top asset;
- fragilidad ante degradacion del top asset.

Evidencia minima:

- Obligatorio: E-02, E-03, E-05, E-06, E-13.
- Muy recomendable: E-10.
- Opcional: E-11.
- Fuera del alcance: causalidad de asset.

### 4.9 Relaciones entre variables

Knowledge esperado:

El caso debe poder leer asociaciones entre variables sin afirmar causalidad no demostrada.

Findings necesarios:

- cruces de variables;
- patrones combinados;
- interacciones;
- co-ocurrencias relevantes.

Evidencia minima:

- Obligatorio: E-04, E-05, E-06, E-09, E-13.
- Muy recomendable: E-10, E-11.
- Opcional: E-12.
- Fuera del alcance: correlaciones no codificadas.

### 4.10 Evolucion temporal

Knowledge esperado:

El caso debe detectar tendencia, estabilidad, deterioro o mejora.

Findings necesarios:

- series comparables;
- ventanas periodicas;
- cambios en eficiencia o calidad;
- posibles efectos de fatiga o aprendizaje.

Evidencia minima:

- Obligatorio: E-02, E-03, E-04, E-10, E-13.
- Muy recomendable: E-08.
- Opcional: E-11.
- Fuera del alcance: series de sistemas no publicadas.

### 4.11 Plataforma

Knowledge esperado:

El caso debe comparar diferencias por plataforma si el dato existe.

Findings necesarios:

- comparacion entre plataformas;
- impacto en calidad y coste;
- lectura por placement o superficie cuando aplique.

Evidencia minima:

- Obligatorio: E-08, E-02, E-03, E-04, E-10.
- Muy recomendable: E-09.
- Opcional: E-12.
- Fuera del alcance: plataformas no medidas.

### 4.12 Impacto esperado sobre Meta

Knowledge esperado:

El caso debe poder explicar que senales debe aprender Meta y como cambia la lectura de optimizacion.

Findings necesarios:

- mapping de eventos y senales;
- calidad observada frente a senal enviada;
- cobertura de learning signals;
- limites de la optimizacion actual.

Evidencia minima:

- Obligatorio: E-04, E-11, E-12, E-13.
- Muy recomendable: E-09, E-10.
- Opcional: E-08.
- Fuera del alcance: configuracion tecnica no documentada.

### 4.13 Oportunidades de optimizacion

Knowledge esperado:

El caso debe priorizar donde hay valor potencial sin confundir oportunidad con solucion.

Findings necesarios:

- activos con mejor senal relativa;
- activos con volumen pero baja calidad;
- segmentos o coberturas con mayor potencial;
- riesgos de escala prematura.

Evidencia minima:

- Obligatorio: E-03, E-04, E-05, E-06, E-09, E-10, E-13.
- Muy recomendable: E-11, E-12.
- Opcional: E-08.
- Fuera del alcance: planes de ejecucion.

## 5. Inventario minimo de evidencia y clasificacion de obligatoriedad

| ID | Elemento de evidencia | Clasificacion | Por que es necesario |
|---|---|---|---|
| E-01 | Contexto oficial, objetivo, alcance y definiciones | Obligatorio | Sin definicion de negocio no hay lectura analitica correcta |
| E-02 | Volumen por periodo y por segmento | Obligatorio | Permite dimensionar escala, concentracion y comparacion |
| E-03 | Spend y metricas de coste | Obligatorio | Sin coste no hay eficiencia economica |
| E-04 | Regla de calidad, score o tier operativo | Obligatorio | Sin criterio de calidad no se puede distinguir volumen de valor |
| E-05 | Campaign y adset identifiers | Obligatorio | Necesarios para comparar estructura de media |
| E-06 | Ad reference / ad name | Obligatorio | Necesario para lectura a nivel anuncio |
| E-07 | Creative asset metadata | Muy recomendable | Aumenta profundidad en creatividad y permite distinguir assets reales |
| E-08 | Plataforma / placement / audience segment | Muy recomendable | Permite explicar diferencias de rendimiento por canal o segmento |
| E-09 | Variables explicativas de formulario o senales de intencion | Obligatorio | Necesarias para responder preguntas sobre explicacion de calidad |
| E-10 | Fecha, semana o mes con granularidad estable | Obligatorio | Sin temporalidad no hay evolucion ni estabilidad |
| E-11 | CRM / post-lead / outcome signal | Muy recomendable | Mejora la lectura de calidad real e impacto de negocio |
| E-12 | Conversion API / event mapping | Muy recomendable | Necesario para impacto esperado sobre Meta y lectura de learning signals |
| E-13 | Coverage states y reglas de emparejamiento | Obligatorio | Sin cobertura no se pueden separar universos ni ratios válidos |
| E-14 | Duplicate / test / validity flags | Obligatorio | Sin control de validez no hay contrato de evidencia confiable |
| E-15 | High quality definition o equivalente | Muy recomendable | Mejora la exactitud de calidad y trade-offs |

### Lectura de la clasificacion

- Obligatorio: sin este elemento, una o varias preguntas no pueden responderse.
- Muy recomendable: mejora significativamente la calidad y profundidad del analisis.
- Opcional: aporta profundidad adicional, pero no cambia la conclusion principal.
- Fuera del alcance: informacion interesante, pero no necesaria para el objetivo actual de AUC-001.

## 6. Comparacion con el contrato vigente

El Evidence Contract vigente es correcto como armazon formal: exige trazabilidad, UNKNOWN, limitaciones, alcance y separacion frente a Razonamiento.

Sin embargo, frente al contrato minimo reconstruido, su cobertura es solo parcial o aproximada en varias preguntas clave.

| Pregunta de negocio | Estado frente al contrato vigente | Justificacion |
|---|---|---|
| Volumen | Parcialmente cubierto | El contrato puede contener volumen, pero el set actual no cubre toda la granularidad historica (p. ej. impresiones/clicks/conversions) |
| Calidad | Parcialmente cubierto | Hay lead_tier A/B y ratios, pero faltan high quality, post-lead y señales explicativas completas |
| Eficiencia economica | Cubierto mediante aproximacion | Spend y ratios derivados existen para matched, pero no para todos los universos ni todos los niveles |
| Campañas | Parcialmente cubierto | Campaign/adset existen donde hay metadata de lead-side, pero spend attribution no es completa |
| Creatividades | Cubierto mediante aproximacion | La lectura por ad reference existe, pero no hay metadata de asset creativa |
| Anuncios | Cubierto por otra dimension equivalente | El ad reference funciona como dimension util para lectura analitica |
| Senales explicativas | No cubierto | Faltan variables de formulario y señales de intencion codificadas |
| Trade-offs | Parcialmente cubierto | Solo puede leerse en el subconjunto con spend y quality emparejados |
| Concentracion | Cubierto | El current Evidence Set soporta lectura top-heavy |
| Relaciones entre variables | Parcialmente cubierto | Hay algunas relaciones estructurales, pero no todas las necesarias |
| Evolucion temporal | No cubierto | No hay cobertura temporal suficiente para todas las preguntas |
| Plataforma | No cubierto | La dimension no esta materializada en el Evidence Set actual |
| Impacto esperado sobre Meta | Parcialmente cubierto | Puede inferirse de forma limitada, pero faltan event mappings y quality depth |
| Oportunidades de optimizacion | Parcialmente cubierto | Hay base para priorizar, pero no para una evaluacion completa |

### Lectura de comparacion

El contrato vigente cubre bien la trazabilidad formal y la disciplina de UNKNOWN, pero no materializa todavia todas las familias de evidencia necesarias para el repertorio analitico minimo completo de AUC-001.

## 7. Gaps identificados

### Evidence gaps

- variables explicativas de formulario;
- temporalidad suficiente;
- plataforma;
- high quality;
- CRM / post-lead outcomes;
- CAPI / event mapping;
- creative asset metadata real;
- impressions, clicks y conversiones por periodo cuando hagan falta para la pregunta.

### Contract gaps

- El Evidence Contract es estructuralmente correcto, pero demasiado generico para declarar por si solo toda la cobertura analitica minima.
- Algunas preguntas quedan cubiertas solo por aproximacion o por una dimension equivalente.

### Question gaps

- Las preguntas sobre explicacion, evolucion, plataforma e impacto sobre Meta no pueden cerrarse solo con el repertorio de evidencia actualmente materializado.

## 8. Riesgos

- Confundir cobertura formal con cobertura analitica real.
- Tratar ad reference como sustituto completo de creative asset metadata.
- Inferir calidad explicativa sin variables explicativas.
- Mezclar evidencia emparejada con evidencias lead-only o spend-only.
- Presentar como concluyente lo que solo es aproximacion o lectura parcial.
- Construir preguntas de optimizacion sin la evidencia que las sostenga.

## 9. Conclusión

La informacion que AUC-001 necesita realmente para generar el informe analitico correcto es mas amplia que la que el contrato vigente materializa hoy.

El contrato minimo reconstruido requiere, como minimo, evidencia sobre:

- volumen y calidad por periodo;
- coste y eficiencia economica;
- campaign / adset / ad reference;
- cobertura y emparejamiento de spend vs lead;
- variables explicativas de calidad;
- evolucion temporal;
- plataforma;
- high quality o equivalente;
- impacto de senales sobre Meta y sus eventos;
- control de validez de datos.

El Evidence Contract actual preserva la estructura correcta para razonar sobre evidencia, pero solo cubre de forma plena algunas de estas familias y cubre otras mediante aproximacion o por otra dimension equivalente.

Por tanto, el contrato minimo de evidencia para AUC-001 no es solo un contenedor de hallazgos observables. Es el conjunto minimo de familias de evidencia que permiten responder volumen, calidad, eficiencia, trade-offs, concentracion, relaciones, evolucion, plataforma y oportunidad de optimizacion sin reintroducir supuestos no verificados.