# RUNBOOK — Meta Lead Quality Analysis

## Propósito

Este documento describe el procedimiento operativo para ejecutar AUC-001.

Debe utilizarse únicamente después de que la skill haya sido activada.

No define arquitectura.

No sustituye Specifications.

No redefine contratos.

Su responsabilidad consiste únicamente en ejecutar correctamente el caso de uso.

---

# Workflow

1. Resolver Execution Context
2. Cargar contexto oficial
3. Validar Data Provider
4. Adquirir Evidence Set
5. Construir Knowledge Set
6. Construir Recommendation Set
7. Validar contenido canónico
8. Entregar a Presentation Layer

---

# 1. Resolver Execution Context

Objetivo:

Materializar un Context Definition estable antes de acceder a los datos.

Debe resolverse:

- objetivo;
- periodo;
- fecha de corte;
- alcance;
- definición de calidad;
- audiencia;
- tipo de salida;
- restricciones.

No reutilizar automáticamente contexto de ejecuciones anteriores.

Cuando la solicitud utilice la forma `hasta [fecha]` y no incluya una fecha inicial:

- interpretar la fecha indicada como fecha de corte;
- resolver el inicio como la primera evidencia disponible dentro de las fuentes autorizadas;
- no sustituir el periodo por el mes natural de la fecha de corte;
- no reutilizar el periodo de una ejecución histórica anterior.

Solo podrá utilizarse un mes natural cuando:

- el usuario solicite explícitamente `mes`, `mensual`, `junio`, `durante junio` o una formulación equivalente; o
- exista una restricción contractual aplicable que obligue a ello.

Cuando exista una restricción contractual que cambie el alcance solicitado:

- registrar la divergencia;
- justificarla explícitamente;
- solicitar aclaración si modifica materialmente el significado de la petición.

Si la primera fecha disponible todavía no se conoce durante Context Resolution:

- registrar temporalmente `PENDING_START_FROM_PROVIDER_COVERAGE`;
- resolverla al validar la cobertura temporal del Data Provider;
- cerrar el periodo antes de construir el Evidence Set.

Solicitar aclaración únicamente cuando cambie materialmente la ejecución.

Definition of Done

Existe un Context Definition explícito y estable.

Deben quedar registrados:

- solicitud original;
- patrón temporal detectado;
- fecha de corte;
- fecha inicial resuelta;
- regla aplicada;
- justificación de cualquier divergencia.

---

# 2. Cargar contexto oficial

Consultar:

- docs/context_refs.md
- Analytical Use Case
- Data Contract
- Presentation Contract
- CCD
- FARO
- CLARO
- KPIs oficiales
- project_brief.md (cuando aplique)

Las definiciones oficiales prevalecen sobre inferencias realizadas desde el modelo de datos.

Definition of Done

Las fuentes obligatorias han sido cargadas.

---

# 3. Validar Data Provider

Confirmar que el runtime puede acceder al Data Provider autorizado por el Data Contract.

Verificar:

- proyecto;
- datasets;
- tablas;
- campos;
- cobertura temporal.

Antes de ejecutar cualquier consulta deberá comprobarse que todas las fuentes pertenecen al Data Contract vigente.

Si una fuente no puede verificarse, detener la ejecución.

Definition of Done

Todas las fuentes consultadas pertenecen al Data Contract.

---

# 4. Construir Evidence Set

Adquirir únicamente evidencia verificable.

Separar:

- hechos;
- métricas derivadas;
- coverage states;
- limitaciones;
- UNKNOWNs.

Cada elemento debe mantener:

- fuente;
- periodo;
- alcance;
- referencia contractual.

No interpretar todavía.

Definition of Done

Existe un Evidence Set trazable.

Debe poder demostrarse que Evidence quedó estabilizada antes de iniciar Presentation Layer, con limitaciones, UNKNOWNs y coverage states preservados.

---

# 5. Construir Knowledge Set

Transformar la evidencia en conocimiento.

El objetivo no es repetir cifras.

Debe responder preguntas como:

- ¿Qué patrones aparecen?
- ¿Qué está cambiando?
- ¿Qué explica mejor el rendimiento?
- ¿Qué anomalías existen?
- ¿Qué riesgos aparecen?
- ¿Qué incertidumbres permanecen?

Para cada insight indicar:

- evidencia utilizada;
- interpretación autorizada;
- limitaciones.

No formular todavía recomendaciones.

Knowledge debe derivar exclusivamente de Evidence y no puede reconstruir evidencia ni modificar coverage states, limitaciones o UNKNOWNs.

Definition of Done

Existe un Knowledge Set consolidado que explica el comportamiento observado.

Debe poder demostrarse que Knowledge quedó estabilizado antes de iniciar Presentation Layer y que deriva exclusivamente de Evidence.

---

# 6. Construir Recommendation Set

Cada recomendación debe derivar del Knowledge Set.

Para cada recomendación registrar:

- prioridad;
- acción;
- justificación;
- conocimiento asociado;
- riesgo;
- criterio posterior de validación.

No introducir recomendaciones nuevas durante Presentation Layer.

Recommendations deben derivar exclusivamente de Knowledge y preservar sus limitaciones, UNKNOWNs y coverage states.

Definition of Done

Existe un Recommendation Set priorizado y trazable.

Debe poder demostrarse que Recommendations quedaron estabilizadas antes de iniciar Presentation Layer y que derivan exclusivamente de Knowledge.

---

# 7. Validar contenido canónico

Antes de Presentation comprobar:

- Context Definition;
- Evidence Set;
- Knowledge Set;
- Recommendation Set.

Verificar:

- consistencia;
- trazabilidad;
- prioridades;
- coverage states;
- limitaciones;
- equivalencia semántica.

Antes de iniciar Presentation Layer deberá poder verificarse que:

1. la evidencia está cerrada y no contiene interpretación;
2. el conocimiento está cerrado y deriva únicamente de la evidencia;
3. las recomendaciones están cerradas y derivan únicamente del conocimiento;
4. ninguno de estos estados será reconstruido durante la representación.

No basta con que Evidence, Knowledge y Recommendations aparezcan mezclados por primera vez dentro del informe final.

Este requisito exige la existencia y cierre verificable de los estados lógicos, independientemente de su implementación. No exige archivos físicos separados, IDs físicos, rutas concretas ni formatos concretos.

Definition of Done

Los cuatro conjuntos están estabilizados como estados lógicos verificables.

---

# 8. Entregar a Presentation Layer

Presentation Layer recibe únicamente:

- Context Definition;
- Evidence Set;
- Knowledge Set;
- Recommendation Set.

Presentation Layer podrá modificar únicamente:

- organización;
- densidad;
- vocabulario;
- abstracción;
- narrativa;
- precisión de presentación.

Nunca podrá:

- consultar datos;
- reconstruir conocimiento;
- generar recomendaciones;
- alterar prioridades;
- modificar cobertura;
- cambiar el contenido canónico.

Definition of Done

El contenido canónico queda preparado para cualquier Presentation Policy compatible.