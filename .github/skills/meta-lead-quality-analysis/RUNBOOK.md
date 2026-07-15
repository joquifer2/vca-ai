# RUNBOOK - Meta Lead Quality Analysis

## Proposito
Ejecutar AUC-001 despues de activar la skill.

---

# Workflow
1. Resolver Execution Context
2. Cargar contexto oficial
3. Validar Data Provider
4. Adquirir Evidence Set
5. Construir Knowledge Set
6. Construir Recommendation Set
7. Validar contenido canonico
8. Entregar a Presentation Layer

---

# 1. Resolver Execution Context
Materializar un Context Definition estable antes de acceder a los datos.

Resolver: objetivo, periodo, fecha de corte, alcance, definicion de calidad, audiencia, tipo de salida y restricciones.

Cuando la solicitud use `hasta [fecha]` sin fecha inicial:
- interpretar la fecha indicada como fecha de corte;
- resolver el inicio como la primera evidencia disponible en las fuentes autorizadas;
- no sustituir el periodo por el mes natural de la fecha de corte;
- no reutilizar el periodo de una ejecucion historica anterior.

Usar un mes natural solo cuando el usuario solicite explicitamente `mes`, `mensual`, `junio`, `durante junio` o equivalente, o cuando exista una restriccion contractual aplicable.

Si una restriccion contractual cambia el alcance solicitado, registrar la divergencia, justificarla y solicitar aclaracion si modifica materialmente la peticion.

Si la primera fecha disponible no se conoce durante Context Resolution:
- registrar temporalmente `PENDING_START_FROM_PROVIDER_COVERAGE`;
- resolverla al validar la cobertura temporal del Data Provider;
- cerrar el periodo antes de construir el Evidence Set.

Solicitar aclaracion unicamente cuando cambie materialmente la ejecucion.

Definition of Done

Existe un Context Definition explicito y estable.

Deben quedar registrados: solicitud original, patron temporal detectado, fecha de corte, fecha inicial resuelta, regla aplicada y justificacion de cualquier divergencia.

---

# 2. Cargar contexto oficial
Cargar las fuentes oficiales aplicables: docs/context_refs.md, Analytical Use Case, Data Contract, Presentation Contract, CCD, FARO, CLARO, KPIs oficiales y project_brief.md cuando aplique.

Aplicar las definiciones oficiales por encima de inferencias realizadas desde el modelo de datos.

Definition of Done

Las fuentes obligatorias han sido cargadas.

---

# 3. Validar Data Provider
Confirmar que el runtime puede acceder al Data Provider autorizado por el Data Contract.

Verificar proyecto, datasets, tablas, campos y cobertura temporal.

Antes de ejecutar cualquier consulta, comprobar que todas las fuentes pertenecen al Data Contract vigente. Si una fuente no puede verificarse, detener la ejecucion.

Definition of Done

Todas las fuentes consultadas pertenecen al Data Contract.

---

# 4. Construir Evidence Set
Adquirir unicamente evidencia verificable.

Separar hechos, metricas derivadas, coverage states, limitaciones y UNKNOWNs.

Mantener en cada elemento: fuente, periodo, alcance y referencia contractual.

No interpretar todavia.

Definition of Done

Existe un Evidence Set trazable.

Debe poder demostrarse que Evidence quedo estabilizada antes de iniciar Presentation Layer, con limitaciones, UNKNOWNs y coverage states preservados.

---

# 5. Construir Knowledge Set
Construir el Knowledge Set exclusivamente desde el Evidence Set estabilizado durante la ejecucion actual.

Durante esta fase:
1. Aplicar `analytical_profile.md`.
2. Aplicar `knowledge-construction-profile.md`.
3. Construir el Knowledge Set.

Transformar evidencia estabilizada en conocimiento util para la toma de decisiones, sin limitarse a repetir metricas o describir tablas.

Explicar patrones, relaciones relevantes, factores que explican el comportamiento observado, anomalias, oportunidades, riesgos e incertidumbres abiertas.

Conservar por cada elemento: evidencia utilizada, interpretacion autorizada, limitaciones y grado de incertidumbre cuando corresponda.

No formular todavia recomendaciones.

Definition of Done

Existe un Knowledge Set consolidado que explica el comportamiento observado.

Debe poder demostrarse que: el Analytical Profile fue utilizado durante la construccion del analisis; el Knowledge Construction Profile fue aplicado durante la construccion del conocimiento; ambos artefactos se utilizaron unicamente dentro de esta fase; el Knowledge Set deriva exclusivamente del Evidence Set; el Knowledge quedo estabilizado antes de iniciar Recommendation Generation.

---

# 6. Construir Recommendation Set
Construir el Recommendation Set exclusivamente desde el Knowledge Set generado durante la ejecucion actual.

Registrar por cada recomendacion: prioridad, accion, justificacion, conocimiento asociado, riesgo y criterio posterior de validacion.

No introducir recomendaciones nuevas durante Presentation Layer.

Definition of Done

Existe un Recommendation Set priorizado y trazable.

Debe poder demostrarse que Recommendations quedaron estabilizadas antes de iniciar Presentation Layer y que derivan exclusivamente de Knowledge.

---

# 7. Validar contenido canonico
Comprobar Context Definition, Evidence Set, Knowledge Set y Recommendation Set antes de Presentation.

Verificar consistencia, trazabilidad, prioridades, coverage states, limitaciones y equivalencia semantica.

Confirmar que la evidencia esta cerrada y no contiene interpretacion; el conocimiento esta cerrado y deriva unicamente de la evidencia; las recomendaciones estan cerradas y derivan unicamente del conocimiento; ninguno de estos estados sera reconstruido durante la representacion.

No corregir inconsistencias durante esta fase. Si la validacion falla, detener la ejecucion.

Definition of Done

Los cuatro conjuntos estan estabilizados como estados logicos verificables.

---

# 8. Entregar a Presentation Layer
Entregar a Presentation Layer el contenido canonico estabilizado.

Definition of Done

El contenido canonico queda preparado para cualquier Presentation Policy compatible.