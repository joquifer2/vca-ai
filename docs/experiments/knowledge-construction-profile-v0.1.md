# Knowledge Construction Profile v0.1

## Proposito

Este perfil indica al modelo como razonar durante Knowledge Generation para AUC-001.

Su objetivo no es describir el workflow, no redisenar el lifecycle y no crear una capability reusable para Foundation.

Su objetivo es mejorar la calidad del siguiente Knowledge Set haciendo el paso de razonamiento mas explicito, mas disciplinado y mas trazable.

Usa este perfil solo cuando trabajes en AUC-001.

## Principios de razonamiento

Al construir conocimiento, piensa como un analista senior que debe defender cada interpretacion.

Aplica estos principios durante todo el paso de razonamiento:

- Prioriza la explicacion sobre la descripcion. No te limites a decir lo que muestra la tabla; explica que significa el patron.
- Parte de la fuerza de la evidencia, no del deseo de negocio. La evidencia mas fuerte debe marcar el recorrido del razonamiento.
- Compara antes de concluir. Si una afirmacion no esta contrastada con una alternativa o una linea base, considerala incompleta.
- Separa concentracion de causalidad. Una referencia dominante es una senal de concentracion, no una prueba de superioridad.
- Respeta los limites de coverage. Trata la evidencia matched, lead_only y spend_only como contextos de razonamiento distintos.
- Propaga la incertidumbre en lugar de ocultarla. Si una conclusion depende de datos faltantes, dilo de forma explicita.
- Prefiere varias explicaciones antes que una sola. Si una explicacion parece dominante, comprueba si otro efecto de coverage o de seleccion tambien explica la observacion.
- Mantiene visible la trazabilidad. Toda interpretacion sustantiva debe poder rastrearse a un bloque concreto de evidencia.
- Evalua robustez antes que confianza. Un patron visto en una fila o en un slice estrecho es un Finding candidato, no una conclusion estable.
- Evita la inflacion causal. Correlacion, asociacion, concentracion y explicacion no son lo mismo.

## Preguntas analiticas

Hazte estas preguntas de forma repetida mientras razonas sobre la evidencia:

- Que patron es el mas fuerte en la evidencia, y que lo hace mas solido que los demas?
- Que cambia de forma material entre segmentos, coverage states o referencias?
- Que variables separan la evidencia de alta calidad de la de baja calidad?
- Que observaciones se mantienen estables en mas de un slice de los datos?
- Donde se concentra la evidencia, y esa concentracion es informativa o solo accidental?
- Que trade-off aparece entre volumen, calidad y coste?
- Que cambia cuando la evidencia se lee por coverage state en lugar de por total?
- Que explicacion encaja mejor con la evidencia y que explicacion alternativa sigue siendo plausible?
- Que no puede concluirse porque la evidencia es incompleta, parcial o faltante?
- Que resultado sigue siendo demasiado debil para convertirse en Finding?
- Que resultado debe seguir como hipotesis hasta superar un chequeo de robustez?
- Que se volveria enganoso si se presentara sin su limitacion?

## Operaciones analiticas

Usa estas operaciones cuando ayuden a aclarar la evidencia.

### Distribution Analysis

Usa esta operacion para inspeccionar como se distribuyen los valores, tiers de calidad o conteos a traves de la evidencia.

Utilizala cuando necesites responder si la senal esta concentrada en pocos buckets o repartida entre muchos.

### Comparative Analysis

Usa esta operacion para comparar dos o mas segmentos, referencias, campanas o estados.

Utilizala cuando necesites responder que cambia, que se mantiene similar y que diferencia importa mas.

### Segmentation

Usa esta operacion para dividir la evidencia por una variable significativa como coverage state, referencia, periodo o senal de calidad.

Utilizala cuando una vista agregada o unica oculte el patron real.

### Concentration Analysis

Usa esta operacion para detectar si un numero pequeno de entidades explica la mayor parte de la senal observada.

Utilizala cuando la evidencia parezca dominada por una o pocas referencias.

### Trend Analysis

Usa esta operacion para inspeccionar el cambio en el tiempo.

Utilizala cuando la pregunta no sea solo que ocurrio, sino si el patron sube, baja, se mantiene estable o es volatil.

### Cost Efficiency Analysis

Usa esta operacion para relacionar gasto con calidad.

Utilizala cuando la pregunta sea si la calidad se obtiene de forma eficiente o solo barata.

### Coverage Analysis

Usa esta operacion para verificar que puede y que no puede sostener cada bloque de evidencia.

Utilizala cuando la evidencia este dividida entre contextos matched, lead_only y spend_only.

### Robustness Evaluation

Usa esta operacion para comprobar si una observacion es lo bastante fuerte como para sobrevivir a un cambio de slice, umbral o agrupacion.

Utilizala cuando un resultado pueda verse distorsionado por poco volumen o por un alcance estrecho.

### Variable Explanatory Assessment

Usa esta operacion para evaluar que variable parece explicar mejor la diferencia observada que las demas.

Utilizala cuando varios campos puedan explicar de forma plausible el mismo comportamiento.

### Thresholding

Usa esta operacion para separar senales mas fuertes de senales mas debiles mediante una regla declarada.

Utilizala cuando la evidencia necesite un limite explicito entre estados que califican y que no califican.

### Ranking

Usa esta operacion para ordenar observaciones, segmentos o referencias por fuerza, relevancia o peso de evidencia.

Utilizala cuando el analisis deba decidir que merece primero la atencion.

## Patrones de composicion

No trates las operaciones como movimientos aislados. Componlas.

Usa los siguientes patrones cuando la evidencia los soporte:

### Patron 1: Comparar, luego segmentar, luego testar robustez

Comparative Analysis

↓

Segmentation

↓

Robustness Evaluation

↓

Finding

Usa este patron cuando una diferencia parezca importante pero pueda explicarse solo por un slice.

### Patron 2: Distribuir, umbralizar y consolidar

Distribution Analysis

↓

Thresholding

↓

Knowledge Consolidation

Usa este patron cuando la evidencia deba convertirse en una distincion de calidad como senal de lead mas fuerte o mas debil.

### Patron 3: Segmentar, comparar y explicar

Segmentation

↓

Comparative Analysis

↓

Variable Explanatory Assessment

↓

Finding

Usa este patron cuando la pregunta sea que variable explica mejor la diferencia observada.

### Patron 4: Concentrar, revisar limite y qualificar

Concentration Analysis

↓

Coverage Analysis

↓

Robustness Evaluation

↓

Finding o Hypothesis

Usa este patron cuando una referencia domine los datos y exista riesgo de sobreinterpretar el resultado.

### Patron 5: Coste, calidad y trade-off

Cost Efficiency Analysis

↓

Segmentation

↓

Comparative Analysis

↓

Finding

Usa este patron cuando el analisis deba equilibrar gasto y calidad en lugar de leer solo el coste.

### Patron 6: Evidencia, incertidumbre y conclusion

Coverage Analysis

↓

Robustness Evaluation

↓

Knowledge Consolidation

↓

Conclusion

Usa este patron cuando la evidencia sea incompleta y la conclusion deba permanecer limitada a lo que realmente esta soportado.

## Construccion de Findings

Una observacion en bruto solo se convierte en Finding cuando cumple todo lo siguiente:

- Cambia la interpretacion de la evidencia, no solo la redaccion.
- Esta vinculada a evidencia identificable, no a una impresion general.
- Es mas fuerte que una simple lectura de tabla o listado de metricas.
- Sobrevive al menos a un chequeo de sentido, comparacion o limite.
- Es lo bastante especifica como para importar, pero no tanto como para convertirse en un detalle aislado.
- Ayuda a distinguir entre lo importante y lo que solo esta presente.

No conviertas una observacion en Finding cuando:

- solo repite un numero ya visible en la evidencia;
- no cambia la lectura de la evidencia;
- depende de contexto faltante que no esta disponible;
- es plausible pero todavia no ha sido contrastada con alternativas;
- parece una conclusion pero no supera un chequeo de coverage o robustez.

Todo Finding debe tener estas propiedades:

- trazabilidad a la evidencia;
- una afirmacion interpretativa clara;
- un limite o limitacion;
- una razon de por que importa;
- una relacion clara con al menos otro Finding o hipotesis.

## Consolidacion de conocimiento

Despues de formar Findings, consolidalos en un Knowledge Set coherente.

### Insights

Usa Insights para interpretaciones directamente respaldadas por la evidencia.

Un insight debe:

- explicar un patron;
- mantenerse cerca de la evidencia;
- evitar excesos causales;
- preservar las limitaciones.

### Hypotheses

Usa Hypotheses para explicaciones plausibles que todavia necesitan cautela o validacion.

Una hipotesis debe:

- explicar por que la observacion puede estar ocurriendo;
- indicar que la respaldaria mas;
- indicar que podria refutarla;
- evitar formularse como conclusion.

### Conclusions

Usa Conclusions solo cuando la evidencia converja lo suficiente como para sostener una afirmacion acotada.

Una conclusion debe:

- resumir lo suficientemente establecido;
- permanecer dentro del alcance de la evidencia;
- evitar convertir evidencia parcial en verdad universal;
- preservar cualquier limitacion no resuelta.

### Priorities

Usa Priorities para expresar que merece mas atencion en el razonamiento, no para prescribir accion.

Una prioridad debe:

- reflejar peso de evidencia, riesgo o relevancia;
- preservar el orden del razonamiento;
- mantenerse distinta de una recomendacion operativa.

### Risks

Usa Risks para los puntos en los que la lectura podria exagerarse, quedar infra-qualificada o usarse mal.

Un riesgo debe:

- nombrar el peligro interpretativo;
- enlazar con la restriccion de evidencia que lo genera;
- seguir visible aguas abajo.

### Uncertainties

Usa Uncertainties para informacion faltante, incompleta o no verificable.

Una incertidumbre debe:

- permanecer explicita;
- propagarse al Knowledge Set final;
- nunca resolverse en silencio por suposicion.

Al consolidar, sigue este orden:

1. Confirma los Findings mas solidos.
2. Separa las interpretaciones respaldadas de las explicaciones tentativas.
3. Identifica que sigue siendo desconocido.
4. Registra los riesgos de lectura erronea.
5. Preserva la frontera entre knowledge y recommendation.

## Quality Gates

Antes de cerrar Knowledge Generation, verifica lo siguiente:

### Profundidad

El razonamiento debe ir mas alla de reportar tablas o metricas aisladas. Debe mostrar que significa la evidencia.

### Trazabilidad

Todo insight, hipotesis, conclusion, prioridad, riesgo e incertidumbre debe apuntar a evidencia identificable.

### Robustez

Ninguna afirmacion principal debe depender de un unico slice debil cuando exista una comparacion o chequeo mas fuerte disponible.

### Disciplina de incertidumbre

Los datos faltantes, la metadata desconocida y el coverage parcial deben seguir visibles y no desaparecer dentro de la narrativa.

### Disciplina de coverage

La evidencia matched, lead_only y spend_only no debe colapsarse en una unica lectura indiferenciada.

### Explicaciones alternativas

Si una explicacion parece fuerte, comprueba si aun existe otra explicacion plausible.

### Disciplina causal

No presentes causalidad cuando la evidencia solo soporte concentracion, asociacion, separacion o correlacion.

### Disciplina de limite

No crees evidencia, no crees recomendaciones y no escribas mas alla de lo que la evidencia soporta.

## Anti-patrones

Evita explicitamente estos comportamientos:

- listar metricas sin interpretarlas;
- repetir el mismo numero en varias formas sin aportar significado;
- tratar un valor grande como un resultado relevante por si solo;
- confundir concentracion con superioridad;
- convertir una correlacion en una afirmacion causal;
- ignorar los coverage states;
- leer evidencia spend-only o lead-only como si fuera matched;
- ocultar la incertidumbre porque complica la narrativa;
- usar el volumen por si solo como prueba de calidad;
- usar el CPL por si solo como prueba de rendimiento;
- hacer recommendations antes de estabilizar el knowledge;
- colapsar varios Findings en un resumen vago;
- sobreajustarse a una unica referencia dominante;
- inventar contexto faltante para que la explicacion quede mas fluida;
- presentar una hipotesis como una conclusion;
- presentar una conclusion sin un limite.

## Como usar este perfil

Cuando el modelo reciba el Evidence Set, debe:

1. Leer la evidencia teniendo en cuenta los limites de coverage.
2. Hacer las preguntas analiticas anteriores antes de escribir cualquier Finding.
3. Aplicar una o mas operaciones de la lista anterior.
4. Combinar operaciones usando los patrones de composicion.
5. Promover solo observaciones estables a Findings.
6. Consolidar los Findings en Insights, Hypotheses, Conclusions, Priorities, Risks y Uncertainties.
7. Mantener las recommendations fuera de este paso.

## Recordatorio de alcance

Este perfil es experimental y local a AUC-001.

No es una capability de Foundation.

No es un metodo general para cualquier caso de uso.

Su proposito es mejorar el siguiente Knowledge Set producido para AUC-001.
