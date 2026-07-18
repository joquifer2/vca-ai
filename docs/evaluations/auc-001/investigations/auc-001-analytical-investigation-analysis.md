# AUC-001 Analytical Investigation Analysis

## 1. Pregunta de investigación

¿Qué constituye realmente una investigación analítica entre Evidence y Knowledge en AUC-001?

La pregunta no es cómo construir Knowledge ni cómo cambiar el lifecycle. La pregunta es qué sucede intelectual y metodológicamente en el tramo intermedio que convierte evidencia en conocimiento estabilizado.

Esta investigación no propone una nueva Specification, no modifica el workflow y no introduce nuevas capacidades. Solo intenta comprender la forma real de la investigación analítica a partir del corpus ya disponible.

## 2. Método utilizado

El método aplicado es inverso y reconstructivo.

En lugar de partir de operaciones identificadas y avanzar hacia Knowledge, se parte de Knowledge relevantes y se reconstruye hacia atrás:

```text
Knowledge
↓
¿Qué findings tuvieron que existir?
↓
¿Qué razonamiento conectó esos findings?
↓
¿Qué preguntas provocaron ese razonamiento?
↓
¿Qué evidencia respondió esas preguntas?
```

La reconstrucción se apoya únicamente en:

- [docs/evaluations/auc-001/investigations/auc-001-knowledge-construction-comparative-analysis.md](/docs/evaluations/auc-001/investigations/auc-001-knowledge-construction-comparative-analysis.md);
- el mismo corpus documental utilizado en esa investigación;
- Knowledge Set, Evidence Set, Recommendation Set e informe histórico ya presentes en el repositorio;
- el prompt histórico archivado y los outputs históricos referenciados por ese corpus.

No se incorporó nueva evidencia.

## 3. Reconstrucción inversa de varios Knowledge Sets

### 3.1 Knowledge histórico: la calidad no se explica por volumen bruto

Knowledge reconstruido:

El canal compra volumen barato, no calidad homogénea.

Reconstrucción inversa:

- Findings necesarios:
  - el volumen total es suficiente para observar patrones;
  - la proporción de leads cualificados es minoritaria;
  - el volumen y la calidad no están alineados de forma automática.
- Razonamiento que conecta esos findings:
  - un volumen alto no garantiza valor comercial;
  - la calidad debe leerse separadamente del simple envío de formularios;
  - la señal de negocio está en la calidad y no en el conteo bruto.
- Preguntas que provocan ese razonamiento:
  - ¿estamos captando suficiente volumen?
  - ¿estamos captando calidad?
  - ¿puede el volumen barato ser engañoso?
- Evidencia que responde esas preguntas:
  - los informes históricos muestran diferencia clara entre leads totales, qualified y high quality;
  - la calidad no crece al mismo ritmo que el volumen.

Lectura de la investigación:

Antes de llegar a ese Knowledge, el sistema tuvo que investigar la separación entre volumen observado y calidad observable. Esa investigación no es solo ordenar datos; es descubrir que el volumen por sí solo no resuelve la pregunta de negocio.

### 3.2 Knowledge histórico: la creatividad puede concentrar valor

Knowledge reconstruido:

El valor aparece concentrado en pocas piezas de mayor volumen.

Reconstrucción inversa:

- Findings necesarios:
  - unas pocas creatividades concentran la mayor parte del volumen y de los cualificados observados;
  - no todas las piezas aportan el mismo balance coste/calidad;
  - algunas piezas muestran trade-offs favorables y otras no.
- Razonamiento que conecta esos findings:
  - no basta con saber qué creatividades generan leads;
  - hay que comparar volumen, calidad y coste simultáneamente;
  - la concentración indica dependencia de activos críticos.
- Preguntas que provocan ese razonamiento:
  - ¿qué creatividades generan más volumen?
  - ¿qué creatividades generan mejor calidad?
  - ¿el valor está disperso o concentrado?
- Evidencia que responde esas preguntas:
  - la matriz histórica por creatividad muestra diferencias visibles de CPL, CPQL, CPHQL, score y cualificación.

Lectura de la investigación:

La investigación analítica aquí no empieza con el ranking. Empieza con la sospecha de que algunas piezas pueden explicar más que otras y termina verificando que el comportamiento está concentrado. El conocimiento no sale del ranking aislado, sino del contraste entre piezas, costes y calidad.

### 3.3 Knowledge actual: la disponibilidad de billetes marca una diferencia observada de calidad

Knowledge reconstruido:

La disponibilidad de billetes es la señal observada con mayor diferencia de calidad entre categorías.

Reconstrucción inversa:

- Findings necesarios:
  - quienes solo están mirando muestran una cualificación mucho menor;
  - quienes están en proceso de compra mejoran de forma marcada;
  - quienes ya tienen billetes muestran la mejor proporción de quality dentro del conjunto observado.
- Razonamiento que conecta esos findings:
  - la intención declarada no vale igual en todas sus etapas;
  - la señal de viaje progresa por estados observables;
  - la diferencia entre categorías es más importante que el total agregado.
- Preguntas que provocan ese razonamiento:
  - ¿qué variable se asocia con mayor diferencia de calidad?
  - ¿qué categoría separa mejor la intención?
  - ¿hay una gradiente de señal observable?
- Evidencia que responde esas preguntas:
  - la tabla histórica de billetes de avión muestra diferencias claras entre “solo mirando”, “en proceso de compra” y “sí, ya los tengo”.

Lectura de la investigación:

Aquí la investigación analítica no consiste en “descubrir la variable ganadora” en sentido predictivo. Consiste en comprobar que la evidencia permite un gradiente de lectura suficientemente fuerte como para distinguir categorías de intención.

### 3.4 Knowledge actual: las señales combinadas pesan más que las aisladas

Knowledge reconstruido:

La combinación de señales presenta una asociación más fuerte con la calidad que las variables aisladas.

Reconstrucción inversa:

- Findings necesarios:
  - billetes, fecha prevista y experiencia no actúan igual por separado que en conjunto;
  - la acumulación de señales refuerza la lectura de intención;
  - la variable aislada explica menos que el conjunto de señales.
- Razonamiento que conecta esos findings:
  - la intención no es monocausal;
  - el patrón relevante aparece cuando varias señales convergen;
  - una lectura univariada pierde parte del fenómeno.
- Preguntas que provocan ese razonamiento:
  - ¿qué combinaciones de señales elevan la calidad?
  - ¿cuál es la relación entre señales aisladas y señal acumulada?
  - ¿la lectura de negocio cambia si se combinan variables?
- Evidencia que responde esas preguntas:
  - las tablas históricas y actuales muestran que billetes, fecha, experiencia y otras variables informadas generan diferencias más claras cuando se leen juntas.

Lectura de la investigación:

La investigación analítica no es solo segmentar. Es investigar si las categorías aisladas se explican mejor dentro de una estructura de señales combinadas. El Knowledge emerge cuando el sistema descubre que la explicación más útil no es una variable, sino una constelación de señales.

### 3.5 Knowledge actual: la cobertura limita lo que puede afirmarse

Knowledge reconstruido:

La separación entre coverage states limita el tipo de inferencia permitida.

Reconstrucción inversa:

- Findings necesarios:
  - matched, lead_only y spend_only no admiten la misma interpretación;
  - no todo lead-side evidence tiene equivalencia de spend;
  - algunas inferencias serían inválidas si se mezclan coberturas.
- Razonamiento que conecta esos findings:
  - la investigación analítica también investiga qué no puede afirmarse;
  - la robustez no depende solo de patrones, sino de cobertura y atribución;
  - la limitación es parte del conocimiento, no un residuo externo.
- Preguntas que provocan ese razonamiento:
  - ¿qué parte del fenómeno está emparejada?
  - ¿qué parte no tiene spend atribuible?
  - ¿qué conclusiones son válidas por cobertura y cuáles no?
- Evidencia que responde esas preguntas:
  - el Evidence Set actual separa matched, lead_only y spend_only;
  - el Knowledge Set actual propaga incertidumbre y límites de lectura.

Lectura de la investigación:

Parte de investigar analíticamente es aprender a bloquear inferencias falsas. La investigación no solo extrae significado; también disciplina el significado posible.

## 4. Posibles niveles del proceso intelectual

La clasificación A/B/C es útil, pero no completa por sí sola. La evidencia sugiere al menos cinco niveles funcionales:

### Nivel A - Trabajo sobre evidencia

Incluye:

- segmentar;
- ordenar;
- comparar;
- agregar;
- filtrar;
- agrupar;
- medir diferencias observables.

Este nivel manipula la evidencia sin pretender todavía explicar el fenómeno.

### Nivel B - Trabajo intelectual

Incluye:

- buscar explicación;
- resolver contradicciones;
- evaluar trade-offs;
- formular hipótesis;
- decidir si un patrón es robusto;
- diferenciar señal de ruido;
- detectar qué evidencia no permite inferir.

Este nivel no crea Knowledge todavía, pero sí organiza la investigación que lo hará posible.

### Nivel C - Construcción de conocimiento

Incluye:

- sintetizar;
- consolidar;
- estabilizar interpretaciones;
- declarar prioridades;
- formalizar incertidumbres;
- convertir findings en Knowledge.

Este nivel ya no explora solamente; estabiliza una lectura útil del fenómeno.

### Nivel D - Disciplina de frontera

Incluye:

- separar conocimiento de recomendación;
- evitar causalidad no demostrada;
- impedir que una interpretación se vista como acción;
- conservar límites y UNKNOWN.

Este nivel aparece como guardrail metodológico recurrente y es parte real de la investigación.

### Nivel E - Traducción de negocio

Incluye:

- expresar implicaciones;
- decidir relevancia práctica;
- conectar lectura analítica con efectos potenciales.

Este nivel todavía no es Recommendation, pero ya deja ver hacia dónde podría ir el conocimiento.

Conclusión provisional sobre la clasificación:

La clasificación A/B/C es correcta como abstracción parcial, pero insuficiente para describir la investigación analítica observada. La evidencia muestra al menos dos capas adicionales: disciplina de frontera y traducción de negocio.

## 5. Hipótesis alternativas

### H1 - La investigación es una secuencia fija de operaciones

Evidencia a favor:

- los artefactos históricos repiten comparación, segmentación, ranking, robustez e interpretación;
- las cadenas reconstruidas muestran una cierta recurrencia estructural;
- la profundidad aparece cuando estas operaciones se encadenan.

Evidencia en contra:

- el orden cambia según la pregunta;
- algunas investigaciones empiezan por una anomalía, otras por una variable, otras por un trade-off;
- la secuencia fija no explica bien la adaptación al dominio.

Valoración: parcialmente cierta, pero insuficiente.

### H2 - La investigación está guiada por preguntas

Evidencia a favor:

- las cadenas históricas nacen de preguntas explícitas;
- las preguntas orientan qué evidencia mirar;
- las preguntas cambian el tipo de conocimiento obtenido.

Evidencia en contra:

- una pregunta sola no basta sin operaciones y sin razonamiento;
- la misma pregunta puede conducir a distintos Knowledge según cómo se investigue.

Valoración: muy bien soportada, pero incompleta sola.

### H3 - La investigación es un proceso iterativo de generación y contraste de hipótesis

Evidencia a favor:

- el razonamiento histórico compara alternativas, no solo resume;
- algunas conclusiones nacen de tensión entre posibles explicaciones;
- la robustez aparece como criterio de contraste.

Evidencia en contra:

- no todo el proceso queda descrito como iteración explícita;
- parte de la investigación parece proceder por lectura directa de patrones.

Valoración: fuertemente plausible como componente central.

### H4 - La investigación depende principalmente del contexto de negocio

Evidencia a favor:

- el contexto determina qué señales importan;
- el objetivo de negocio cambia la relevancia de un patrón;
- la misma evidencia puede producir distintas prioridades según el caso.

Evidencia en contra:

- el contexto no sustituye la investigación;
- sin operaciones y contraste, el contexto no produce conocimiento.

Valoración: necesaria, pero no suficiente.

### H5 - La investigación combina preguntas, operaciones y razonamiento iterativo

Evidencia a favor:

- la reconstrucción inversa muestra preguntas que activan operaciones y producen hipótesis;
- los Knowledge observados surgen de encadenar lectura, contraste, explicación y consolidación;
- la frontera entre evidencia, investigación y conocimiento es gradual, no única.

Evidencia en contra:

- la combinación todavía no está formalizada como secuencia universal;
- diferentes informes muestran distinto peso relativo de cada componente.

Valoración: la hipótesis mejor soportada.

## 6. Evidencia a favor y en contra

### A favor de que sí existe una investigación analítica explícita

- Los Knowledge históricos no aparecen como resumen plano; aparecen como salida de una secuencia de contraste.
- Los informes muestran repetición de comparación, segmentación, robustez, trade-off y lectura de negocio.
- El Knowledge actual conserva límites, incertidumbre y separación de cobertura.
- Los outputs históricos indican que antes de consolidar conocimiento hubo razonamiento intermedio visible.

### En contra de una secuencia rígida única

- No todas las cadenas empiezan por la misma unidad.
- No toda investigación necesita un mismo orden de operaciones.
- El contexto y el dominio alteran el peso de cada paso.
- La evidencia no demuestra todavía una fórmula universal cerrada.

### A favor de que el nivel B importa tanto como el A

- La diferencia entre dos analistas con la misma evidencia no se explica solo por capacidad de ordenar datos.
- Hay que explicar, contrastar, seleccionar y excluir hipótesis.
- La superficie de evidencia es insuficiente si no se investiga su significado.

### En contra de que el nivel C sea independiente del resto

- El Knowledge final depende de qué preguntas se hicieron.
- También depende de qué operaciones se consideraron relevantes.
- Y depende de qué límites se respetaron al consolidar.

## 7. Hallazgos

1. La investigación analítica no empieza únicamente con una operación.
2. Tampoco empieza solo con una pregunta.
3. Empieza cuando una pregunta activa una búsqueda de explicación sobre evidencia insuficiente por sí sola.
4. La unidad mínima de la investigación no es una métrica ni un ranking; es una tensión interpretativa entre evidencia y significado.
5. Las operaciones son necesarias, pero no explican solas el proceso.
6. Los findings suelen aparecer como puentes entre observación e interpretación, antes de consolidarse como Knowledge.
7. La diferencia entre superficial y profunda está en la calidad del contraste, la robustez de la lectura y la capacidad de excluir explicaciones débiles.
8. Dos analistas pueden producir distinto Knowledge con la misma evidencia porque seleccionan preguntas distintas, conectan findings de forma distinta y toleran distinto nivel de incertidumbre.

## 8. Incertidumbres

- No existe una traza completa de la actividad mental o procedimental del modelo entre Evidence y Knowledge.
- La reconstrucción inversa depende de artefactos escritos, no de observación directa del proceso interno.
- No se ha probado la hipótesis en otro caso de uso no relacionado con Meta Ads.
- La clasificación A/B/C parece útil, pero puede no capturar todas las capas reales.
- Finding sigue siendo un término puente documental, no un pilar fundacional cerrado.

## 9. Conclusión experimental

La investigación analítica parece ser un proceso compuesto, no una sola acción.

Con la evidencia disponible, la mejor definición provisional es esta:

Una investigación analítica es la secuencia, generalmente iterativa, mediante la cual una pregunta de negocio o una anomalía observada activa operaciones sobre evidencia, esas operaciones generan findings intermedios, los findings se contraponen con hipótesis o explicaciones posibles, y el conjunto resultante se estabiliza como Knowledge trazable, limitado y útil para fases posteriores.

Por tanto:

- no comienza solo con una pregunta;
- no comienza solo con una operación;
- no comienza solo con una anomalía;
- no comienza solo con el objetivo de negocio;
- comienza cuando alguno de esos disparadores activa una búsqueda de explicación que obliga a distinguir evidencia, interpretación y límite.

La hipótesis H5 es la más sólida: preguntas, operaciones y razonamiento iterativo combinados con disciplina de frontera.

## 10. Próximo experimento recomendado

El próximo experimento debería probar si distintas formas de disparar la investigación producen Knowledge diferente sobre la misma evidencia.

Un protocolo útil sería comparar, sobre el mismo corpus congelado:

1. Disparo por pregunta explícita.
2. Disparo por anomalía observable.
3. Disparo por objetivo de negocio.
4. Disparo por hipótesis previa.

Y medir:

- cuántos findings intermedios aparecen;
- qué tipo de operaciones se activan;
- cuánto contraste interpretativo se produce;
- qué nivel de incertidumbre permanece;
- qué tan distinto es el Knowledge final entre disparadores.

Ese experimento no debe diseñar una solución. Debe servir para comprender si la investigación analítica tiene un disparador dominante o si emerge de la interacción entre varios.
