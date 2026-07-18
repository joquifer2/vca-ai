---
type: analytical-use-case
id: AUC-001
name: Meta Lead Quality Analysis
status: Active
validation_status: Validated
experimental_cycle: Closed
priority: High
---

# Analytical Use Case · Lead Quality Analysis

## Objetivo

Definir el primer caso de uso analítico de VCA IA (AUC-001) que servirá para validar la arquitectura analítica del sistema, el lifecycle definido por AIF Foundation y el BigQuery MCP Server como Data Provider principal.

---

# Problema de negocio

Actualmente el análisis periódico de calidad de leads, scoring y eficiencia de inversión en Meta Ads se realiza mediante un único prompt monolítico.

Aunque el proceso produce resultados satisfactorios, concentra en una única ejecución responsabilidades que deberían permanecer desacopladas, dificultando su reutilización, evolución y trazabilidad.

---

# Objetivo del caso de uso

Construir una capacidad analítica que permita producir contenido analítico canónico estabilizado sobre la calidad de los leads captados mediante Meta Ads, separando claramente:

- contexto;
- obtención de evidencia;
- preparación de datos;
- análisis;
- razonamiento;
- recomendaciones;
- contenido canónico estabilizado.

La materialización posterior del contenido canónico aprobado corresponde a Presentation Layer y se rige por SPEC-010 y SPEC-011.

---

# Delimitación del caso

## Incluye

- análisis de calidad de leads procedentes de Meta Ads;
- revisión de volumen, coste, calidad y eficiencia de inversión;
- consolidación de contexto y evidencia desde las fuentes oficiales del proyecto;
- síntesis analítica con conclusiones y recomendaciones priorizadas;
- trazabilidad entre contexto, evidencia, razonamiento y contenido canónico estabilizado.

## No incluye

- diseño o implementación de runtime productivo;
- definición de nuevas fuentes no publicadas en el repositorio;
- cambios en la arquitectura de la Foundation;
- automatizaciones operativas fuera del alcance documental aprobado;
- decisiones de negocio no sustentadas por evidencia disponible.

## Límites de trabajo

- la skill meta-lead-quality-analysis actua como vehículo de validacion del caso de uso;
- BigQuery MCP Server se mantiene como Data Provider principal para la evidencia;
- cualquier necesidad de ampliar el alcance debe volver a Specification antes de incorporarse al caso de uso.

---

# Usuarios

## Principal

Analista de negocio.

## Secundarios

- Dirección.
- Responsable de Marketing.
- Especialistas de Meta Ads.
- Equipo Comercial.

---

# Contexto requerido

La capacidad analítica deberá utilizar, cuando resulte necesario:

- Client Context Document (CCD).
- FARO.
- CLARO.
- KPIs oficiales.
- Knowledge Base del proyecto.

---

# Inventario minimo de evidencia

## Evidencia base a reunir

| Categoria | Evidencia esperada | Fuente prioritaria | Uso en el caso |
| --- | --- | --- | --- |
| Volumen de captacion | Leads, impresiones, clics y conversiones por periodo | BigQuery MCP Server | Dimensionar la entrada del embudo |
| Calidad del lead | Señales que permitan distinguir calidad alta, media o baja | BigQuery MCP Server + contexto oficial | Evaluar la efectividad real de la captacion |
| Eficiencia economica | Coste, CPA, CPL o metricas equivalentes publicadas | BigQuery MCP Server | Medir eficiencia de inversion |
| Campanas y creatividades | Rendimiento comparado por campaña, conjunto y creatividad | BigQuery MCP Server | Identificar patrones de mejor rendimiento |
| Segmentacion | Diferencias por periodo, audiencia o segmento aplicable | BigQuery MCP Server | Explicar variaciones relevantes |
| Contexto de negocio | Criterios y definiciones oficiales del proyecto | CCD, FARO, CLARO, KPIs oficiales | Evitar interpretaciones no alineadas |

## Evidencia minima obligatoria

- una fuente oficial de contexto consultada antes del analisis;
- una fuente principal de evidencia verificable;
- un criterio operativo para distinguir calidad de lead;
- un periodo de analisis definido;
- un contenido analitico canonico estabilizado con trazabilidad completa;


---

# Flujo de analisis

## Pipeline analitico

## Secuencia base

1. Confirmar objetivo, periodo y alcance operativo.
2. Cargar contexto oficial y verificar definiciones aplicables.
3. Identificar Data Providers y priorizar la evidencia principal.
4. Reunir y estructurar la evidencia minima obligatoria.
5. Separar hechos observables, evidencia derivada e interpretaciones.
6. Construir el razonamiento que conecta evidencia con conclusiones.
7. Formular recomendaciones priorizadas y accionables.

## Salidas esperadas por etapa

| Etapa | Salida esperada |
| --- | --- |
| Confirmacion | Alcance del analisis validado |
| Contexto | Fuentes oficiales identificadas |
| Evidencia | Inventario trazado y verificable |
| Analisis | Hallazgos observables y derivados |
| Razonamiento | Justificacion explicita de conclusiones |
| Recomendaciones | Acciones priorizadas |
| Contenido canonico | Contenido analitico estabilizado y trazable |

## Pipeline de representacion

### Secuencia base

8. Delegar la seleccion de la proyeccion de presentacion a Presentation Layer a partir del contexto canonicalizado, conforme a SPEC-010.
9. Delegar la transformacion de la representacion a Presentation Layer segun el Communication Context correspondiente, conforme a SPEC-011.
10. Materializar la salida final sin alterar el contenido canonico aprobado.

## Salidas esperadas por etapa

| Etapa | Salida esperada |
| --- | --- |
| Proyeccion | Presentation Projection Selection resuelta |
| Contexto de comunicacion | Communication Context aplicado |
| Representacion | Presentation Output trazable |
| Salida | Documento final alineado con la proyeccion seleccionada |

---

# Criterios de validacion

El caso AUC-001 quedara listo para validacion cuando cumpla, como minimo, con estos criterios:

1. Existe un periodo de analisis definido y documentado.
2. Existe al menos una fuente oficial de contexto consultada antes del analisis.
3. La evidencia principal proviene de BigQuery MCP Server o una fuente equivalente explicitamente justificada.
4. El analisis separa hechos observables, evidencia derivada, interpretaciones y recomendaciones.
5. Las conclusiones pueden rastrearse hasta la evidencia usada.
6. Las recomendaciones son accionables y priorizadas.
7. El contenido analitico queda estabilizado antes de cualquier materializacion de presentacion.
8. La proyeccion de presentacion queda determinada por el contexto canonicalizado.
9. Las limitaciones y pendientes quedan explicitados en la salida final.
10. No se introducen supuestos no verificados.

## Señales de validacion exitosa

- el contenido analitico canónico reproduce una lectura coherente del rendimiento de leads;
- la representacion final conserva la equivalencia semantica del contenido canónico aprobado;
- el proceso puede repetirse con la misma estructura sin perder trazabilidad;
- la skill meta-lead-quality-analysis puede operar sin redefinir el alcance del caso;
- el contenido analitico puede materializarse en una salida final coherente con la proyeccion seleccionada;
- la salida resultante es util para revision documental y para consumo ejecutivo.

---

# Data Providers previstos

Como fuente principal de evidencia se utilizará:

- BigQuery MCP Server.

Podrán incorporarse otros Data Providers compatibles cuando resulte necesario.

---

# Resultado esperado

El resultado del análisis será un contenido analítico canonico estabilizado, apto para su posterior materializacion en una salida final que permita comprender:

- volumen de captación;
- calidad de los leads;
- eficiencia económica;
- campañas y creatividades más eficientes;
- oportunidades de optimización;
- recomendaciones priorizadas.

El contenido canónico constituye el unico origen autorizado para cualquier representacion posterior.

La salida final debera conservar equivalencia semantica con el contenido canonico aprobado y ajustarse a la proyeccion de presentacion seleccionada.

---

# Criterios de éxito

El caso de uso se considerará validado cuando la skill meta-lead-quality-analysis sea capaz de producir un contenido analitico canonico equivalente o superior al proceso actual, manteniendo la trazabilidad entre contexto, evidencia, razonamiento y recomendaciones, y permitiendo su posterior materializacion conforme a la proyeccion seleccionada.

El contenido canónico podrá materializarse mediante multiples representaciones preservando la equivalencia semantica.

---

# Próximo paso

Este caso de uso deberá servir como entrada para la skill meta-lead-quality-analysis y para futuras iteraciones de validación del caso de uso dentro de VCA IA.

No constituye una specification ni una implementación.

---

# Evidencia de validación

## Registro

- Fecha: 2026-07-11
- Evidencia: la skill [meta-lead-quality-analysis](/.github/skills/meta-lead-quality-analysis/SKILL.md) queda alineada con este caso de uso y puede utilizarse para ejecutar y validar el primer análisis de VCA IA.
- Resultado: validación documental y trazable del caso de uso AUC-001 como primer caso analítico del proyecto.
- Referencias de soporte:
	- [docs/context_refs.md](/docs/context_refs.md)
	- [project_brief.md](/project_brief.md)
	- [meta-lead-quality-analysis skill](/.github/skills/meta-lead-quality-analysis/SKILL.md)

## Evidencia adicional registrada

- La definicion de criterios de validacion del caso AUC-001 queda registrada en [docs/context_refs.md](/docs/context_refs.md) y en [docs/tasks.md](/docs/tasks.md) como parte del cierre trazable de T-004 y T-005.