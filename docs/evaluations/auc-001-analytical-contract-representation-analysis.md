# AUC-001 Analytical Contract Representation Analysis

## Metadata

| Field | Value |
|---|---|
| Evaluation ID | VCA-AUC-001-EVAL-ACR-001 |
| Evaluation Type | Experimental representation analysis |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Status | Documented |
| Date | 2026-07-16 |
| Scope | Evaluate whether the analytical contract and the current physical representation are distinct levels |

## 1. Objetivo

Evaluar si el contrato analitico consolidado de AUC-001 y su representacion actual en [analytical_use_cases/auc-001/analytical-contract.md](../../analytical_use_cases/auc-001/analytical-contract.md) describen niveles distintos o si pueden tratarse como la misma cosa.

La investigacion no modifica el contrato, no redefine AUC-001 y no introduce nuevas capacidades. Solo determina si existe suficiente evidencia para justificar una separacion conceptual entre necesidad analitica e implementacion fisica.

## 2. Hipotesis

### H1

El contrato actual es suficiente. No existe un nivel adicional. Las capacidades analiticas pueden vincularse directamente a la implementacion fisica.

### H2

Existe un nivel logico intermedio. El contrato analitico deberia expresarse mediante conceptos analiticos estables y las columnas, dimensiones y tablas actuales serian solo una materializacion contingente.

### H3

La separacion solo aporta valor en algunos tipos de capacidades analiticas. No todo el contrato requiere ese nivel de abstraccion.

## 3. Metodo

El metodo parte exclusivamente de:

- [analytical_use_cases/auc-001/analytical-contract.md](../../analytical_use_cases/auc-001/analytical-contract.md)
- [docs/evaluations/auc-001-knowledge-construction-comparative-analysis.md](auc-001-knowledge-construction-comparative-analysis.md)
- [docs/evaluations/auc-001-analytical-investigation-analysis.md](auc-001-analytical-investigation-analysis.md)
- [docs/evaluations/auc-001-knowledge-depth-recovery-validation.md](auc-001-knowledge-depth-recovery-validation.md)
- [docs/evaluations/auc-001-minimum-evidence-contract-analysis.md](auc-001-minimum-evidence-contract-analysis.md)
- la observacion emitida por el Reviewer Agent sobre la mezcla entre capacidades analiticas y representacion actual.

La investigacion se realiza capacidad por capacidad con estas preguntas:

1. Que necesidad analitica satisface realmente?
2. La implementacion actual es esencial o solo una posible representacion?
3. Existe un concepto logico mas estable que la implementacion actual?
4. Que ocurriria si cambiara completamente el modelo fisico?

## 4. Evidencia revisada

### Evidencia principal

- El contrato analitico establece capacidades, findings y cobertura como niveles conceptuales separados de la materializacion actual.
- La seccion de representacion actual del contrato ya declara que las materializaciones son contingentes y pueden cambiar sin modificar el contrato analitico.
- La QA de recuperacion de profundidad valida que el conocimiento analitico se recupera mejor cuando existe una capa de investigacion previa al Knowledge Set.
- El analisis minimo de evidencia muestra que el contrato debe formularse desde necesidades de negocio y no desde tablas o modelo fisico.

### Evidencia de soporte

- La comparativa de construccion de Knowledge muestra que el workflow mas robusto investiga antes de consolidar.
- La investigacion analitica demuestra que existen niveles distintos entre evidencia, findings, conocimiento y traduccion de negocio.
- La validacion de profundidad concluye que la diferencia residual frente al historico se explica principalmente por cobertura de evidencia, no por una ausencia de metodo.

### Observacion del Reviewer Agent

La tabla actual del contrato mezcla parcialmente dos planos:

- el contrato analitico, que describe que necesita el analisis;
- la representacion actual, que describe como se materializa hoy.

Esa observacion es la base de esta investigacion.

## 5. Analisis por capacidad analitica

### 5.1 Agrupar observaciones por unidad de inversion

Necesidad analitica: comparar rendimiento entre unidades que concentran gasto o esfuerzo de media.

Implementacion actual esencial: no.

Concepto logico estable: unidad de inversion.

Dependencia de implementacion: media. `campaign_id` y `adset_id` son materializaciones utiles, pero no agotan el concepto.

Si cambia el modelo fisico: el contrato sigue siendo valido mientras exista alguna representacion de unidad de inversion comparable.

### 5.2 Ordenar observaciones temporalmente

Necesidad analitica: leer evolucion, estabilidad, cambio o fatiga.

Implementacion actual esencial: no.

Concepto logico estable: periodo, ventana temporal o secuencia analitica.

Dependencia de implementacion: baja. `week` y `date` son solo granularidades posibles.

Si cambia el modelo fisico: el contrato sigue siendo valido si la temporalidad sigue siendo observable, aunque cambie la granularidad.

### 5.3 Distinguir niveles de calidad

Necesidad analitica: separar volumen bruto de valor comercial o calidad observable.

Implementacion actual esencial: no.

Concepto logico estable: nivel de calidad o tier operativo.

Dependencia de implementacion: media. `lead_tier`, `qualified AB` y `high quality` son materializaciones concretas de un concepto analitico mas estable.

Si cambia el modelo fisico: el contrato sigue siendo valido si la calidad puede volver a expresarse en categorias equivalentes.

### 5.4 Distribuir observaciones por superficie o segmento

Necesidad analitica: explicar diferencias de rendimiento por contexto de exposicion o audiencia.

Implementacion actual esencial: no.

Concepto logico estable: superficie, segmento o contexto de distribucion.

Dependencia de implementacion: media-baja. `platform` y `audience segment` representan el concepto, pero no lo agotan.

Si cambia el modelo fisico: el contrato sigue siendo valido si persiste una dimension comparable de distribucion.

### 5.5 Identificar activos publicitarios relevantes

Necesidad analitica: leer rendimiento concentrado por pieza o activo.

Implementacion actual esencial: no.

Concepto logico estable: activo publicitario.

Dependencia de implementacion: media. `ad reference` es una representacion operativa, no el concepto en si.

Si cambia el modelo fisico: el contrato sigue siendo valido si se conserva una clave analitica que identifique activos comparables.

### 5.6 Medir eficiencia economica

Necesidad analitica: relacionar coste con resultado y calidad.

Implementacion actual esencial: no.

Concepto logico estable: eficiencia economica por unidad de resultado.

Dependencia de implementacion: media-baja. `spend` y ratios derivados son una forma de materializacion, pero la necesidad analitica es estable.

Si cambia el modelo fisico: el contrato sigue siendo valido si el coste y el resultado permanecen medibles.

### 5.7 Detectar concentracion

Necesidad analitica: saber si pocos activos concentran la mayor parte del resultado.

Implementacion actual esencial: no.

Concepto logico estable: concentracion, dependencia del top performer y distribucion top-heavy.

Dependencia de implementacion: baja. La forma concreta de medirla puede cambiar sin romper el contrato.

Si cambia el modelo fisico: el contrato sigue siendo valido mientras exista una unidad comparativa de contribucion.

### 5.8 Analizar relaciones entre variables

Necesidad analitica: entender asociaciones entre senales, categorias y resultados.

Implementacion actual esencial: no.

Concepto logico estable: relacion observable, asociacion o co-ocurrencia.

Dependencia de implementacion: baja-media. Las variables pueden cambiar, pero el contrato necesita conservar el concepto de relacion.

Si cambia el modelo fisico: el contrato sigue siendo valido si el analisis puede reconstruir relaciones entre variables equivalentes.

### 5.9 Evaluar trade-offs entre volumen, calidad y coste

Necesidad analitica: reconocer tension entre escala, calidad y gasto.

Implementacion actual esencial: no.

Concepto logico estable: trade-off entre dimensiones analiticas.

Dependencia de implementacion: baja. El contrato no depende de una columna concreta sino de la relacion entre dimensiones.

Si cambia el modelo fisico: el contrato sigue siendo valido si las tres dimensiones siguen existiendo en alguna forma.

### 5.10 Identificar anomalías o comportamientos atipicos

Necesidad analitica: detectar excepciones, outliers o señales que rompen el patron.

Implementacion actual esencial: no.

Concepto logico estable: anomalía o comportamiento atipico.

Dependencia de implementacion: media. Las flags actuales son solo una manera de materializar el control de anomalias.

Si cambia el modelo fisico: el contrato sigue siendo valido si el sistema mantiene algun mecanismo de deteccion o declaracion de excepciones.

### 5.11 Separar coverage states no equivalentes

Necesidad analitica: impedir inferencias invalidas entre universos con distinta cobertura.

Implementacion actual esencial: no.

Concepto logico estable: estado de cobertura.

Dependencia de implementacion: baja. `matched`, `lead_only` y `spend_only` son nombres contingentes de un concepto mas estable.

Si cambia el modelo fisico: el contrato sigue siendo valido si la cobertura sigue distinguiendose en estados comparables.

### 5.12 Conservar limites de interpretacion cuando la evidencia es parcial

Necesidad analitica: evitar causalidad no demostrada y sobreinterpretacion.

Implementacion actual esencial: no.

Concepto logico estable: limite de interpretacion, UNKNOWN y disciplina de frontera.

Dependencia de implementacion: muy baja. Este es uno de los conceptos mas estables del contrato.

Si cambia el modelo fisico: el contrato sigue siendo valido; de hecho, gana valor cuando la cobertura cambia.

## 6. Matriz comparativa

| Capacidad analitica | Concepto logico | Implementacion actual | Dependencia de implementacion | Observaciones |
|---|---|---|---|---|
| Agrupar observaciones por unidad de inversion | Unidad de inversion | campaign_id, adset_id | Media | La implementacion materializa el concepto, pero no lo define |
| Ordenar observaciones temporalmente | Periodo / secuencia analitica | week, date | Baja | La temporalidad es un concepto previo a su granularidad |
| Distinguir niveles de calidad | Nivel de calidad / tier | lead_tier, qualified AB, high quality | Media | El concepto es mas estable que cualquier codificacion puntual |
| Distribuir observaciones por superficie o segmento | Superficie / segmento | platform, audience segment | Media-baja | La dimension analitica puede cambiar sin cambiar el contrato |
| Identificar activos publicitarios relevantes | Activo publicitario | ad reference | Media | La clave concreta es contingente |
| Medir eficiencia economica | Eficiencia por unidad de resultado | spend, ratios derivados | Media-baja | La necesidad analitica no depende de una tabla concreta |
| Detectar concentracion | Concentracion / top-heavy | ranking, shares | Baja | Muy claramente separable del soporte fisico |
| Analizar relaciones entre variables | Asociacion / co-ocurrencia | cruces y comparaciones | Baja-media | El concepto permanece aunque cambien las variables exactas |
| Evaluar trade-offs | Trade-off entre dimensiones | lectura conjunta de volumen, calidad y coste | Baja | Es una propiedad analitica, no una propiedad del modelo |
| Identificar anomalías | Anomalia / comportamiento atipico | flags y excepciones observables | Media | La materializacion puede cambiar, el concepto no |
| Separar coverage states no equivalentes | Estado de cobertura | matched, lead_only, spend_only | Baja | La separacion conceptual es mas estable que sus nombres actuales |
| Conservar limites de interpretacion | Limite de interpretacion / UNKNOWN | limitaciones y notas de cobertura | Muy baja | Esta es una capa metodologica claramente distinta del modelo fisico |

## 7. Beneficios observados

- El contrato gana claridad cuando se expresa en conceptos analiticos y no en nombres de columnas.
- La estabilidad frente a cambios del modelo fisico mejora, porque la parte esencial queda anclada en necesidades y no en materializaciones.
- Se reduce el riesgo de confundir representacion actual con definicion contractual.
- Se refuerza la trazabilidad entre conocimiento validado, cobertura y limites de interpretacion.
- La capa de representacion actual puede evolucionar sin reescribir el contrato cada vez que cambie un campo.

## 8. Costes y riesgos

- Aumenta la longitud del contrato si se intenta explicar siempre el concepto y su materializacion en la misma tabla.
- Puede introducirse redundancia si el concepto logico se escribe con demasiados sinónimos.
- Si la capa logica se vuelve demasiado abstracta, pierde utilidad operativa para revisar cobertura real.
- Existe el riesgo de crear una ontologia artificial para capacidades que ya son suficientemente estables con la descripcion actual.
- Una separacion excesiva puede hacer que el contrato parezca mas academico que accionable.

## 9. Casos donde la separación aporta valor

- Cuando una capacidad depende de una implementacion voluble, como campaign_id, adset_id o ad reference.
- Cuando varias materializaciones podrian satisfacer la misma necesidad analitica.
- Cuando el contrato debe sobrevivir a cambios de granularidad, fuente o naming.
- Cuando la capacidad expresa una propiedad analitica estable, como calidad, cobertura, concentracion o trade-off.
- Cuando hay riesgo de confundir el contrato con el modelo fisico vigente.

## 10. Casos donde no aporta valor

- Cuando la representacion actual ya coincide casi exactamente con el concepto analitico y no existe ambiguedad real.
- Cuando la abstraccion adicional no mejora la estabilidad ni la expresividad.
- Cuando la capacidad es puramente metodologica y se entiende mejor como limite o regla que como entidad intermedia.
- Cuando la tabla ya queda suficientemente clara si separa una sola vez contrato y materializacion, sin introducir un nivel extra de taxonomia.

## 11. Conclusion experimental

La evidencia favorece H2 como hipotesis principal.

El contrato analitico y la implementacion fisica no son el mismo nivel. El contrato expresa necesidades analiticas estables; la representacion actual solo materializa esas necesidades de una forma contingente.

H3 tambien recibe apoyo parcial. La separacion aporta mas valor en capacidades donde la materializacion es volatil, donde hay varias representaciones posibles o donde el riesgo de confundir cobertura con concepto es alto. En capacidades muy proximas al soporte actual, la capa intermedia aporta menos valor y puede quedarse en una separacion simple entre concepto y materializacion.

H1 queda debilitada. La implementacion actual no es suficiente como unico nivel porque el contrato se mantiene valido incluso si cambian columnas, claves, granularidad o naming, siempre que el concepto analitico siga siendo reconocible.

## 12. Recomendacion sobre experimento posterior

Si merece un experimento posterior, pero solo de forma acotada.

La siguiente verificacion deberia probar si una version del contrato que explicite solo conceptos analiticos, sin tabla de representacion actual embebida, mejora la lectura del documento sin perder trazabilidad operativa.

No se recomienda convertir esta conclusion en una nueva Specification ni modificar el contrato vigente con base en esta sola investigacion. La evidencia es suficiente para justificar una experimentacion documental posterior, no para imponer una reescritura inmediata.