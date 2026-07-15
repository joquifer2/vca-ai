# Knowledge Construction Profile v0.2

## Purpose

Indica al modelo como razonar durante Knowledge Generation para AUC-001.

Su objetivo es mejorar el siguiente Knowledge Set mediante razonamiento explicito, disciplinado y trazable, sin redisenar el workflow ni crear una capability reusable.

## Reasoning Principles

- Prioriza la explicacion sobre la descripcion: explica que significa el patron, no solo que muestra la tabla.
- Parte de la fuerza de la evidencia y manten visible la trazabilidad a bloques concretos.
- Compara antes de concluir y evalua robustez antes que confianza.
- Separa concentracion, asociacion, correlacion y causalidad.
- Respeta los coverage states: matched, lead_only y spend_only no sostienen la misma lectura.
- Propaga la incertidumbre cuando falten datos, metadata o coverage.
- Considera explicaciones alternativas antes de estabilizar una conclusion.
- Mantiene la frontera entre knowledge y recommendation.

## Analytical Questions

- Que patron es el mas fuerte en la evidencia, y que lo hace mas solido?
- Que cambia de forma material entre segmentos, coverage states o referencias?
- Que variables separan la evidencia de alta calidad de la de baja calidad?
- Que observaciones se mantienen estables en mas de un slice?
- Donde se concentra la evidencia, y esa concentracion es informativa o accidental?
- Que trade-off aparece entre volumen, calidad y coste?
- Que cambia al leer por coverage state en lugar de por total?
- Que explicacion encaja mejor y que alternativa sigue siendo plausible?
- Que no puede concluirse porque la evidencia es incompleta, parcial o faltante?
- Que resultado sigue siendo demasiado debil para convertirse en Finding?
- Que se volveria enganoso si se presentara sin su limitacion?

## Analytical Operations

Usa estas operaciones cuando ayuden a aclarar la evidencia.

### Distribution Analysis

Inspecciona distribuciones de valores, tiers o conteos para distinguir senales concentradas de senales repartidas.

### Comparative Analysis

Compara segmentos, referencias, campanas o estados para identificar que cambia, que permanece y que diferencia importa mas.

### Segmentation

Divide la evidencia por coverage state, referencia, periodo o senal de calidad cuando una vista agregada oculte el patron real.

### Concentration Analysis

Detecta si pocas entidades explican la mayor parte de la senal, sin convertir concentracion en superioridad o causalidad.

### Trend Analysis

Inspecciona cambios en el tiempo para distinguir subida, bajada, estabilidad o volatilidad.

### Cost Efficiency Analysis

Relaciona gasto con calidad cuando la pregunta sea si la calidad se obtiene de forma eficiente o solo barata.

### Coverage Analysis

Verifica que puede sostener cada bloque de evidencia, especialmente entre matched, lead_only y spend_only.

### Robustness Evaluation

Comprueba si una observacion sobrevive a cambios de slice, umbral o agrupacion, y si el volumen o alcance la distorsionan.

### Variable Explanatory Assessment

Evalua que variable explica mejor la diferencia observada cuando varios campos sean plausibles.

### Thresholding

Separa senales fuertes y debiles mediante una regla declarada cuando haga falta un limite explicito.

### Ranking

Ordena observaciones, segmentos o referencias por fuerza, relevancia o peso de evidencia.

## Composition Patterns

No trates las operaciones como movimientos aislados. Componlas cuando la evidencia lo soporte.

### Pattern 1: Compare, segment, test robustness

Comparative Analysis -> Segmentation -> Robustness Evaluation -> Finding

Usalo cuando una diferencia parezca importante pero pueda explicarse solo por un slice.

### Pattern 2: Distribute, threshold, consolidate

Distribution Analysis -> Thresholding -> Knowledge Consolidation

Usalo cuando la evidencia deba convertirse en una distincion de calidad como senal de lead mas fuerte o mas debil.

### Pattern 3: Segment, compare, explain

Segmentation -> Comparative Analysis -> Variable Explanatory Assessment -> Finding

Usalo cuando la pregunta sea que variable explica mejor la diferencia observada.

### Pattern 4: Concentrate, check limits, qualify

Concentration Analysis -> Coverage Analysis -> Robustness Evaluation -> Finding o Hypothesis

Usalo cuando una referencia domine los datos y exista riesgo de sobreinterpretar el resultado.

### Pattern 5: Cost, quality, trade-off

Cost Efficiency Analysis -> Segmentation -> Comparative Analysis -> Finding

Usalo cuando el analisis deba equilibrar gasto y calidad en lugar de leer solo el coste.

### Pattern 6: Evidence, uncertainty, conclusion

Coverage Analysis -> Robustness Evaluation -> Knowledge Consolidation -> Conclusion

Usalo cuando la evidencia sea incompleta y la conclusion deba permanecer limitada a lo soportado.

## Finding Construction

Una observacion en bruto solo se convierte en Finding cuando:

- cambia la interpretacion de la evidencia;
- esta vinculada a evidencia identificable;
- supera una simple lectura de tabla o metricas;
- sobrevive a un chequeo de sentido, comparacion o limite;
- es especifica sin convertirse en detalle aislado;
- distingue lo importante de lo que solo esta presente.

No conviertas una observacion en Finding cuando solo repite un numero, no cambia la lectura, depende de contexto faltante, no ha sido contrastada o no supera un chequeo de coverage o robustez.

Todo Finding debe tener trazabilidad a la evidencia, afirmacion interpretativa clara, limite, razon de importancia y relacion con al menos otro Finding o hipotesis.

## Knowledge Consolidation

Despues de formar Findings, consolidalos en un Knowledge Set coherente.

- Insights: interpretaciones directamente respaldadas por la evidencia, cerca de sus limites.
- Hypotheses: explicaciones plausibles que todavia necesitan cautela o validacion.
- Conclusions: afirmaciones acotadas cuando la evidencia converge lo suficiente.
- Priorities: orden de atencion por peso de evidencia, riesgo o relevancia; no prescripcion operativa.
- Risks: peligros interpretativos enlazados a la restriccion de evidencia que los genera.
- Uncertainties: informacion faltante, incompleta o no verificable que debe propagarse al Knowledge Set final.

Al consolidar, confirma los Findings mas solidos, separa interpretaciones respaldadas de explicaciones tentativas, identifica lo desconocido, registra riesgos de lectura erronea y preserva la frontera entre knowledge y recommendation.

## Anti-patterns

- Listar metricas sin interpretarlas.
- Repetir numeros sin aportar significado.
- Tratar un valor grande como relevante por si solo.
- Confundir concentracion con superioridad.
- Convertir correlacion, asociacion o concentracion en causalidad.
- Ignorar coverage states o leer spend_only y lead_only como matched.
- Ocultar incertidumbre porque complica la narrativa.
- Usar volumen o CPL por si solos como prueba de calidad o rendimiento.
- Hacer recommendations antes de estabilizar el knowledge.
- Colapsar varios Findings en un resumen vago.
- Sobreajustarse a una unica referencia dominante.
- Inventar contexto faltante.
- Presentar una hipotesis como conclusion.
- Presentar una conclusion sin limite.