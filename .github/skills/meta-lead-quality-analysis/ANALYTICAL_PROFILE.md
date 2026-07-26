# Analytical Profile - Lead Quality Analysis

## Estado

| Campo | Valor |
| --- | --- |
| Nombre | Lead Quality Analytical Profile |
| Version | 0.1.0 |
| Estado | Draft |
| Alcance inicial | Calidad de leads, scoring y eficiencia de inversion en Meta Lead Ads |
| Uso previsto | Guia reusable para formular buenos analisis de calidad de leads |

---

## Proposito

Este perfil define las preguntas, principios y criterios de razonamiento que debe intentar responder un analisis excelente de calidad de leads.

No es una plantilla de informe.

No es un prompt operativo.

No fija una estructura de presentacion.

Su funcion es preservar el conocimiento analitico implicito que antes estaba concentrado en un prompt monolitico, convirtiendolo en una guia reusable para evaluar volumen, calidad, eficiencia economica, madurez de optimizacion y oportunidades de decision.

---

## Pregunta central

Un buen analisis de calidad de leads no debe limitarse a responder cuantos leads se han captado.

Debe responder:

> Estamos comprando volumen, calidad o ruido, y que deberiamos cambiar para invertir mejor?

Todas las preguntas del perfil derivan de esta pregunta central.

---

## Principios analiticos

### 1. Calidad antes que volumen

El volumen solo es valioso si puede conectarse con calidad, potencial comercial o avance posterior en el embudo.

Preguntas clave:

- Cuantos leads se han captado?
- Que porcentaje tiene calidad suficiente?
- Que parte del volumen parece poco accionable?
- Hay crecimiento de volumen acompanado de deterioro de calidad?
- Hay pocos leads pero con calidad suficientemente alta como para justificar la inversion?

### 2. Eficiencia economica basada en calidad

El CPL por si solo no representa eficiencia real. Un lead barato puede ser irrelevante si no cumple los criterios minimos de calidad.

Preguntas clave:

- Cuanto cuesta captar un lead?
- Cuanto cuesta captar un lead cualificado?
- Cuanto cuesta captar un lead de alta calidad?
- Que campanas o anuncios tienen buen CPL pero mala calidad?
- Que campanas o anuncios parecen caros al leer CPL, pero eficientes al leer calidad?
- Donde se esta invirtiendo sin generar senal comercial util?

### 3. Scoring como lenguaje de decision

El scoring debe convertir senales dispersas en una lectura operativa de calidad.

Preguntas clave:

- Existe un score formal o debe derivarse desde variables disponibles?
- Que criterios distinguen calidad alta, media y baja?
- Que umbrales se han usado y por que?
- El score representa potencial comercial o solo completitud de datos?
- Que variables empujan el score hacia arriba o hacia abajo?
- Que limitaciones tiene el scoring actual?

### 4. Explicacion de la calidad

El analisis debe buscar que variables explican la diferencia entre leads mejores y peores.

Preguntas clave:

- Que atributos se asocian con mayor calidad?
- Que respuestas de formulario, segmentos, campanas, creatividades o periodos separan mejor los leads buenos de los malos?
- Que variables tienen senal fuerte y cuales solo parecen relevantes por volumen?
- Que patrones se mantienen al cambiar el nivel de lectura?
- Que relaciones son robustas y cuales son fragiles?

### 5. Lectura por unidades de inversion

La calidad debe analizarse donde se toman decisiones de inversion: campana, conjunto, anuncio, creatividad, plataforma, periodo o segmento.

Preguntas clave:

- Que campanas producen mas calidad?
- Que anuncios concentran leads cualificados?
- Que creatividades parecen atraer mejores leads?
- Que unidades combinan volumen, calidad y coste de forma equilibrada?
- Que unidades generan coste sin calidad suficiente?
- Que unidades requieren escala, optimizacion, revision o pausa?

### 6. Separacion entre evidencia y decision

El analisis debe distinguir datos observables, interpretaciones, hipotesis, conclusiones y recomendaciones.

Preguntas clave:

- Que hechos estan directamente soportados por los datos?
- Que metricas son derivadas?
- Que interpretaciones son plausibles pero no demostradas?
- Que conclusiones tienen evidencia suficiente?
- Que recomendaciones dependen de supuestos o informacion incompleta?
- Que no se puede concluir todavia?

### 7. Madurez de optimizacion

La calidad de leads no solo depende de campanas. Tambien depende de si las plataformas reciben senales utiles para optimizar.

Preguntas clave:

- Que eventos o senales de calidad se estan capturando?
- Que senales se envian a Meta u otros sistemas de optimizacion?
- Existe diferencia entre capturar un lead y enviar un evento de calidad?
- Las campanas optimizan por volumen, por lead cualificado o por senales posteriores?
- Que parte de la estrategia de Conversion API es tecnica y que parte es realmente estrategica?
- Que hito permitiria pasar de optimizacion por cantidad a optimizacion por calidad?

---

## Dimensiones minimas de analisis

Un analisis completo debe intentar cubrir estas dimensiones cuando la evidencia exista.

| Dimension | Pregunta que debe responder |
| --- | --- |
| Volumen | Hay suficiente captacion para sostener aprendizaje y decision? |
| Calidad | Que proporcion de leads cumple criterios de valor? |
| Coste | Cuanto cuesta cada nivel de calidad? |
| Campana | Que lineas de inversion explican los mejores y peores resultados? |
| Anuncio o creatividad | Que piezas o referencias atraen mejor calidad? |
| Plataforma | Hay diferencias materiales entre Facebook, Instagram u otros placements? |
| Tiempo | La calidad y el coste mejoran, empeoran o fluctuan? |
| Segmento | Que combinaciones de atributos concentran mejor calidad? |
| Funnel posterior | Los leads avanzan despues de captarse? |
| Senales de optimizacion | Que informacion vuelve a los sistemas de adquisicion? |

---

## Metricas preferentes

El analisis debe priorizar metricas que conecten coste con calidad.

| Categoria | Metricas recomendadas |
| --- | --- |
| Volumen | Leads, leads validos, leads por periodo |
| Calidad | Score medio, distribucion por score, qualified leads, high quality leads |
| Ratios | Porcentaje qualified, porcentaje high quality, conversion posterior si existe |
| Coste | Spend, CPL, coste por qualified lead, coste por high quality lead |
| Comparacion | Ranking por calidad, ranking por coste-calidad, dispersion entre unidades |
| Robustez | Cobertura de datos, volumen minimo, estabilidad por periodo o segmento |

El CPL debe tratarse como metrica incompleta si no se acompana de calidad.

Para AUC-001, cuando el analisis trate eficiencia coste-calidad bajo SPEC-017, debe priorizar metricas canonicas con universo y coverage declarados:

- `matched_commercial_spend`;
- `cost_per_ab_commercial_matched`;
- `cost_per_tier_a_commercial_matched` cuando el denominador sea suficiente;
- denominador usado en cada tasa o coste;
- coverage state aplicable;
- suficiencia de muestra.

Un CPL generico o aislado no sostiene una conclusion de eficiencia si no queda anclado a estas metricas canonicas o a una equivalencia documentada con universo, denominador y coverage.

---

## Operaciones analiticas esperadas

### Inspeccion y normalizacion

Antes de interpretar resultados, el analisis debe identificar fuentes, campos equivalentes, claves de union, granularidad y limitaciones.

Debe preguntar:

- Que datasets existen?
- Que representa cada campo?
- Que columnas son equivalentes aunque tengan nombres distintos?
- Que claves permiten integrar leads, coste, campanas, anuncios, scoring o CRM?
- Que duplicidades o diferencias de granularidad pueden distorsionar costes o conteos?

### Distribucion

Debe observar como se reparte la calidad.

Debe preguntar:

- La calidad esta concentrada en pocos anuncios o repartida?
- Predominan leads de baja, media o alta calidad?
- Hay colas, outliers o grupos pequenos con comportamiento extremo?

### Comparacion

Debe comparar entidades equivalentes antes de concluir.

Debe preguntar:

- Que cambia entre campanas, anuncios, plataformas, periodos o segmentos?
- La diferencia es grande, estable y accionable?
- Que comparacion contradice la lectura agregada?

### Relacion coste-calidad

Debe conectar inversion con valor, no solo con volumen.

Debe preguntar:

- Donde coincide bajo coste con alta calidad?
- Donde el coste alto esta justificado por calidad?
- Donde el coste alto no esta generando valor?
- Donde el bajo coste puede estar ocultando mala calidad?

### Robustez

Debe evaluar si una observacion resiste cambios de lectura.

Debe preguntar:

- El patron se mantiene al segmentar?
- El volumen es suficiente para sostener la conclusion?
- La observacion depende de una sola entidad dominante?
- Que pasaria si se excluye un outlier?

---

## Matriz de lectura estrategica

El perfil debe ayudar a clasificar unidades de decision segun calidad y coste.

| Calidad | Coste | Lectura analitica | Decision probable |
| --- | --- | --- | --- |
| Alta | Bajo | Eficiencia fuerte | Escalar con control |
| Alta | Alto | Valor potencial, eficiencia mejorable | Optimizar antes de escalar agresivamente |
| Baja | Bajo | Volumen barato pero dudoso | Revisar segmentacion, creatividad o criterio de scoring |
| Baja | Alto | Ineficiencia clara | Pausar, redisenar o excluir |
| Incierta | Cualquiera | Evidencia insuficiente | Ampliar datos antes de decidir |

La decision probable no debe presentarse como recomendacion final si no existe evidencia suficiente.

Esta matriz solo orienta la lectura diagnostica. Puede reconocer que una recomendacion futura deberia ser evaluable, pero la accion, prioridad, impacto, metrica de exito, guardrail, confianza y condicion de revision pertenecen a Recommendation Generation y deben derivar del Knowledge Set estabilizado.

---

## Preguntas ejecutivas que el analisis debe poder responder

### Rendimiento global

- Estamos captando suficiente volumen?
- Ese volumen tiene calidad real?
- El coste total esta generando valor proporcional?
- Que KPI resume mejor el estado actual: leads, CPL, CPQL, CPHQL, score medio o conversion posterior?

### Calidad

- Que define un lead bueno en este contexto?
- Cuantos leads cumplen esa definicion?
- Que variables explican mejor la calidad?
- La calidad observada es estable o depende de un segmento puntual?

### Inversion

- Donde se concentra el gasto?
- Donde se concentra la calidad?
- Gasto y calidad estan alineados?
- Que parte de la inversion parece infrautilizada?

### Campanas y anuncios

- Que campanas merecen mas atencion?
- Que anuncios combinan calidad y eficiencia?
- Que anuncios generan volumen sin calidad?
- Que anuncios parecen prometedores pero necesitan mas evidencia?

### Creatividad y mensaje

- Que referencias creativas atraen mejor calidad?
- La creatividad explica calidad o solo concentra volumen?
- Hay senales para ajustar mensajes, claims, formatos o audiencias?
- Falta metadata creativa para sostener una conclusion mas fuerte?

### Evolucion temporal

- La eficiencia mejora o empeora con el tiempo?
- La calidad cambia por semana, dia o fase de campana?
- Hay aprendizaje visible tras cambios de campana, presupuesto o creatividad?
- Existen ventanas temporales anormales que distorsionan la lectura?

### Conversion API y senales

- Que senales de calidad se estan enviando a Meta?
- Se optimiza por lead o por calidad de lead?
- Hay eventos suficientes para entrenar optimizacion basada en calidad?
- Que eventos no deben recomendarse porque ya existen?
- Que siguiente senal tendria mayor impacto estrategico?

### Riesgos y limites

- Que datos faltan para una lectura completa?
- Que conclusion seria enganosa con la evidencia actual?
- Que costes pueden estar duplicados o mal atribuidos?
- Que segmentos tienen volumen insuficiente?
- Que decisiones deberian esperar validacion adicional?

---

## Proceso de razonamiento analítico

Responder preguntas no es suficiente.

Para cada pregunta de negocio, el análisis debe seguir un proceso de razonamiento antes de generar un hallazgo.

### Paso 1. Comprender el patrón

No limitarse a describir la métrica.

Preguntarse:

- ¿Qué está ocurriendo realmente?
- ¿Es un patrón o un hecho aislado?

### Paso 2. Buscar explicaciones

Antes de aceptar una explicación:

- considerar explicaciones alternativas;
- identificar la variable que mejor explica el comportamiento observado;
- separar asociación, correlación y causalidad.

### Paso 3. Evaluar la robustez

Preguntarse:

- ¿El patrón se mantiene al segmentar?
- ¿Depende de un único anuncio, campaña o periodo?
- ¿Existe volumen suficiente?

### Paso 4. Valorar su importancia

No todos los patrones merecen convertirse en hallazgo.

Preguntarse:

- ¿Cambia realmente la comprensión del negocio?
- ¿Modificaría una decisión?
- ¿Sorprendería a un analista experimentado?

Si la respuesta es negativa, probablemente no merece formar parte del informe principal.

### Paso 5. Integrar el hallazgo

Antes de cerrar un hallazgo, comprobar:

- ¿Se relaciona con otros hallazgos?
- ¿Confirma o contradice otra evidencia?
- ¿Ayuda a construir una explicación más completa?

El objetivo no es producir observaciones independientes, sino construir una explicación coherente del comportamiento observado.

---

## Construcción de Insights

El objetivo del análisis no es acumular observaciones, sino construir conocimiento útil para la toma de decisiones.

Un Insight excelente no responde únicamente a la pregunta:

> ¿Qué muestran los datos?

Debe responder además:

> ¿Por qué este resultado cambia nuestra comprensión del problema?

Todo Insight debe cumplir las siguientes condiciones:

- responde a una pregunta relevante de negocio;
- está respaldado por evidencia identificable;
- explica una diferencia, concentración, tensión, relación o cambio significativo;
- conecta varias evidencias cuando ello mejora la comprensión del problema;
- distingue hechos, interpretaciones e hipótesis;
- declara explícitamente su límite de validez;
- evita convertir asociación o correlación en causalidad;
- ayuda a comprender mejor el problema o a orientar una decisión posterior.

Antes de incorporar un Insight al informe, el analista debe preguntarse:

- ¿Este Insight aporta algo que no era evidente leyendo la tabla?
- ¿Cambia realmente la comprensión del problema?
- ¿Se sostiene cuando se consideran explicaciones alternativas?
- ¿Está conectado con otros hallazgos del análisis?
- ¿Su importancia justifica ocupar espacio en el informe principal?

No debe considerarse un Insight:

- una métrica aislada sin interpretación;
- un ranking sin lectura analítica;
- una diferencia sin evaluar volumen, cobertura o robustez;
- una afirmación no trazable a la evidencia;
- una recomendación disfrazada de conclusión;
- una conclusión basada únicamente en CPL u otra métrica aislada;
- una simple descripción de datos que el lector podría obtener directamente de una tabla.

---

## Priorización analítica

No todos los hallazgos tienen el mismo valor.

El informe debe identificar explícitamente:

- cuáles son los descubrimientos más importantes;
- cuáles son secundarios;
- cuáles son únicamente observaciones;
- cuáles son hipótesis que requieren validación.

El espacio dedicado a cada hallazgo debe reflejar su importancia para la toma de decisiones.

---

## Síntesis analítica

El análisis no debe limitarse a producir una colección de hallazgos independientes.

Después de construir los Insights, el analista debe integrarlos para responder:

- ¿Cuál es la explicación más probable del comportamiento observado?
- ¿Qué factores parecen explicar la mayor parte del resultado?
- ¿Qué hallazgos son estructurales y cuáles circunstanciales?
- ¿Qué relaciones existen entre los distintos Insights?
- ¿Qué descubrimientos merecen realmente la atención del lector?

El informe debe priorizar la comprensión del problema por encima de la enumeración de resultados.

---

## Antipatrones

El analisis debe evitar:

- celebrar volumen sin revisar calidad;
- optimizar por CPL como si fuera eficiencia completa;
- concluir eficiencia desde CPL, coste o volumen sin `matched_commercial_spend`, denominador, coverage y muestra;
- mezclar costes de granularidades distintas sin control;
- comparar campanas con coberturas de datos diferentes como si fueran equivalentes;
- inferir causalidad creativa sin metadata suficiente;
- convertir asociaciones temporales, de creatividad o de inversion en causalidad;
- ocultar ausencia de CRM, conversion posterior o eventos de calidad;
- recomendar eventos de Conversion API ya implementados;
- inventar score, umbrales o categorias sin explicar la logica;
- presentar hipotesis como conclusiones;
- presentar recomendaciones no soportadas por datos;
- formular acciones dentro de Knowledge Generation;
- usar outputs historicos como evidencia de una ejecucion actual.

---

## Construcción de la narrativa analítica

El informe no debe limitarse a responder preguntas de forma independiente.

Debe construir una explicación coherente que permita comprender:

1. Qué está ocurriendo.
2. Por qué está ocurriendo.
3. Qué evidencia lo respalda.
4. Qué implicaciones tiene.
5. Qué incertidumbres permanecen.

Cada sección debe conectar con la anterior.

El análisis debe leerse como una explicación, no como una colección de respuestas.

---

## Relacion con artefactos SDD

Este perfil debe operar subordinado a los artefactos metodologicos del proyecto.

| Artefacto | Relacion |
| --- | --- |
| Analytical Use Case | Define el problema y el alcance del caso |
| SPEC-017 Diagnostico Analitico Multicapa | Especializa la profundidad diagnostica minima local de AUC-001 |
| Data Contract | Declara fuentes disponibles, cobertura y limitaciones |
| Discovery Contract | Identifica entidades, dimensiones, metricas y relaciones |
| Analytical Contract | Formaliza el modelo preparado para analisis |
| Evidence Set | Contiene observaciones y metricas trazables |
| Knowledge Set | Convierte evidencia en insights, hipotesis, conclusiones, riesgos e incertidumbres |
| Recommendation Set | Formula acciones sugeridas desde conocimiento confirmado |
| Presentation Layer | Materializa la salida final sin alterar el contenido canonico |

El perfil no sustituye ninguno de estos artefactos.

---

## Condiciones de suficiencia

Un analisis puede considerarse suficientemente completo cuando puede responder, con evidencia o con limitacion explicita:

1. Que volumen se ha generado.
2. Que calidad tiene ese volumen.
3. Cuanto cuesta la calidad, no solo el lead.
4. Que unidades explican los mejores y peores resultados.
5. Que variables parecen explicar diferencias de calidad.
6. Que limitaciones impiden una conclusion mas fuerte.
7. Que senales deberian orientar la optimizacion futura.
8. Que decisiones son razonables ahora y cuales requieren mas evidencia.

---

## Principio rector

Un analisis excelente de calidad de leads debe dejar a Direccion con una lectura clara:

- que esta funcionando;
- que parece funcionar pero aun no esta demostrado;
- que esta consumiendo inversion sin calidad suficiente;
- que falta para optimizar por valor real;
- que decisiones pueden tomarse con confianza y cuales deben esperar.

Si el analisis no mejora la calidad de decision, solo ha descrito datos.
