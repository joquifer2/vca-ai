---
name: meta-lead-quality-analysis
description: Ejecuta AUC-001 para analizar la calidad de leads de Meta Ads utilizando el contexto oficial, el workflow aprobado y BigQuery MCP Server como Data Provider autorizado.
id: SDD-SKILL-006
user-invocable: true
disable-model-invocation: false
---

# Skill — Meta Lead Quality Analysis

## Propósito

Ejecutar el caso de uso analítico AUC-001 para producir informes trazables sobre la calidad, evolución y eficiencia de los leads captados mediante Meta Ads.

Esta skill actúa como punto de entrada y orquestador del caso de uso.

El procedimiento detallado de ejecución se encuentra en:

- `RUNBOOK.md`

Las referencias obligatorias del caso se encuentran en:

- `references.md`

La validación previa a la entrega se encuentra en:

- `CHECKLIST.md`

Esta skill no sustituye las Specifications, los contratos ni las decisiones arquitectónicas del proyecto.

---

# Cuándo utilizar esta skill

Activar esta skill cuando la solicitud esté relacionada con:

- calidad de leads de Meta Ads;
- volumen y evolución de la captación;
- eficiencia económica;
- campañas, conjuntos o anuncios;
- scoring o tiers de calidad;
- informes analíticos de lead quality;
- informes ejecutivos para Dirección;
- ejecución del caso de uso AUC-001.

La solicitud puede formularse en lenguaje natural.

El usuario no necesita mencionar la skill, AUC-001, los contratos ni las Specifications aplicables.

---

# Instrucciones obligatorias de inicio

No iniciar la ejecución mediante una búsqueda global del repositorio.

No utilizar `rg`, búsquedas globales ni exploración abierta del repositorio para descubrir fuentes analíticas, salvo que `references.md` contenga una ruta rota que deba localizarse.

Antes de analizar o consultar datos:

1. Leer `RUNBOOK.md`.
2. Leer `references.md`.
3. Cargar los artefactos obligatorios indicados en `references.md`.
4. Canonicalizar el Execution Context de la solicitud actual.
5. Confirmar el Data Contract vigente.
6. Confirmar que BigQuery MCP Server está disponible.
7. Verificar que las fuentes necesarias están autorizadas.

No iniciar la adquisición de evidencia si alguno de estos pasos no puede completarse.

---

## Data Provider y mecanismo de acceso

La evidencia deberá adquirirse exclusivamente desde las fuentes autorizadas por:

- el Data Contract vigente;
- la configuración publicada del workspace;
- las referencias oficiales del caso de uso.

El Data Provider se resolverá desde:

- `configs/workspaces.json`

Este archivo define el workspace que debe utilizarse, el proyecto autorizado, los recursos permitidos y el mecanismo de acceso.

Una vez resuelto el workspace, la adquisición de evidencia deberá realizarse utilizando el BigQuery MCP Server asociado.

Antes de ejecutar cualquier consulta deberá verificarse que las fuentes necesarias pertenecen al Data Contract y al workspace seleccionado.

La disponibilidad técnica de una tabla no implica autorización metodológica.

Si el workspace no puede resolverse o el BigQuery MCP Server no está disponible, la ejecución deberá detenerse y registrar el bloqueo.

Queda prohibido:

- consultar fuentes fuera del alcance aprobado;
- ampliar silenciosamente el conjunto de tablas;
- utilizar un mecanismo distinto al definido por el workspace;
- continuar cuando no pueda verificarse la autorización de una fuente.


## Solicitud “desde cero”

Interpretar “desde cero” como:

- volver a adquirir la evidencia autorizada;
- reconstruir los artefactos canónicos;
- generar una nueva representación.

No significa:

- ignorar la skill;
- ignorar el contexto oficial;
- ignorar los contratos;
- consultar cualquier tabla disponible;
- utilizar informes anteriores como fuente;
- omitir el workflow metodológico.

---

# Workflow obligatorio

Ejecutar el caso siguiendo este orden:

1. Execution Context Canonicalization.
2. Context Loading.
3. Evidence Acquisition.
4. Knowledge Generation.
5. Recommendation Generation.
6. Presentation.

No redactar el informe mientras se adquiere o analiza evidencia.

No saltar directamente desde BigQuery a la representación final.

---

# Artefactos canónicos

Antes de iniciar Presentation Layer deben existir y estar estabilizados:

- Context Definition;
- Evidence Set;
- Knowledge Set;
- Recommendation Set.

La ejecución debe seguir las instrucciones de `RUNBOOK.md` para construirlos.

El Knowledge Set debe consolidar conocimiento y no limitarse a repetir métricas o describir tablas.

El Recommendation Set debe derivar exclusivamente del Knowledge Set.

Presentation Layer no puede reconstruir estos artefactos ni volver a razonar directamente desde los datos.

La cadena canonica obligatoria es: Context Definition -> Evidence Set -> Knowledge Set -> Recommendation Set -> Presentation.

Coverage states, limitaciones, UNKNOWNs, prioridades y trazabilidad deben preservarse durante toda la ejecucion. Ninguna fase posterior puede reconstruir evidencia, alterar coverage states, modificar limitaciones, resolver UNKNOWNs por inferencia o cambiar prioridades estabilizadas.

---

## Aislamiento entre ejecuciones

Los artefactos persistidos documentan ejecuciones anteriores. No representan el estado lógico de la ejecución actual ni sustituyen el workflow.

Pueden utilizarse solo para recuperar contexto funcional, comparar resultados entre ejecuciones, validar consistencia, auditoría y trazabilidad. No pueden sustituir la adquisición de nueva evidencia, el Evidence Set, el Knowledge Set, el Recommendation Set ni construir directamente la Presentation Layer.

Solo pueden ser la base principal cuando el usuario solicite explícitamente trabajar sobre una ejecución anterior ya estabilizada o comparar resultados históricos.

Los artefactos canónicos requeridos por este workflow deben construirse o estabilizarse dentro de la ejecución actual.

Los artefactos persistentes procedentes de ejecuciones anteriores no pueden utilizarse como fuente para construir una nueva ejecución.

Queda prohibido utilizar como input analítico de una nueva ejecución:

- Knowledge Sets anteriores;
- Recommendation Sets anteriores;
- Presentations o informes anteriores;
- conclusiones, hipótesis o recomendaciones de ejecuciones históricas.

Un Evidence Set anterior solo podrá reutilizarse cuando:

- el usuario solicite explícitamente trabajar sobre evidencia ya adquirida;
- coincidan Execution Context, periodo, alcance y versión contractual;
- quede registrada expresamente su reutilización;
- no se presente como evidencia adquirida de nuevo.

Un Knowledge Set o Recommendation Set anterior solo podrá reutilizarse cuando la solicitud consista exclusivamente en volver a representar el mismo contenido canónico mediante otra Presentation Projection o Presentation Policy.

Para una nueva solicitud analítica, Knowledge y Recommendations deben generarse de nuevo desde la evidencia autorizada de la ejecución actual.

---

# Materialización de la salida

Presentation Layer deberá consumir únicamente los artefactos canónicos estabilizados.

La salida deberá resolver:

- Presentation Projection;
- Communication Context;
- Representation Constraints;
- Presentation Policy aplicable, cuando exista.

Para una salida analítica podrá utilizarse:

- `analytical-review`

Para una salida orientada a Dirección podrá utilizarse:

- `executive-decision-support`

Las proyecciones analítica y ejecutiva son representaciones hermanas.

Ninguna representación anterior puede utilizarse como fuente de otra.

---

# Invariantes de presentación

La representación final no podrá:

- consultar nuevas fuentes;
- crear evidencia;
- generar nuevo conocimiento;
- crear recomendaciones;
- cambiar prioridades;
- alterar coverage states;
- ocultar limitaciones materiales;
- modificar conclusiones aprobadas;
- romper la equivalencia semántica.

Las Presentation Policies solo pueden especializar la forma de comunicar el contenido canónico.

---

# Criterios de bloqueo

AUC-001 admite dos modos de ejecución:

**1. Ejecución completa (modo normal)**

Construye un nuevo Context Definition, adquiere evidencia desde BigQuery MCP Server y genera un nuevo Evidence Set, Knowledge Set, Recommendation Set y Presentation.

Este modo requiere obligatoriamente acceso a BigQuery MCP Server.

**2. Representación de un Evidence Set existente**

El usuario solicita trabajar sobre un Evidence Set previamente estabilizado y autorizado, sin adquirir ni actualizar evidencia.

En este modo:

- no se consulta BigQuery MCP Server;
- no se adquiere nueva evidencia;
- se reutiliza únicamente el Evidence Set indicado;
- se reconstruyen el Knowledge Set, el Recommendation Set y la Presentation para la solicitud actual.

Fuera de este modo, BigQuery MCP Server es obligatorio.

---

Detener la ejecución cuando:

- el Execution Context no pueda canonicalizarse;
- falte contexto obligatorio;
- `references.md` no pueda resolverse;
- el runtime no pueda acceder a BigQuery MCP Server durante una ejecución completa;
- no pueda verificarse que las fuentes pertenecen al Data Contract;
- una fuente necesaria no esté autorizada;
- se detecte una fuente fuera del Data Contract;
- el Evidence Set no pueda estabilizarse;
- el Knowledge Set no aporte conocimiento consolidado;
- el Recommendation Set no derive del Knowledge Set;
- falte algún artefacto canónico antes de Presentation Layer;
- la representación requiera modificar el contenido canónico;
- no pueda garantizarse la equivalencia semántica.

---

En caso de bloqueo:

- no improvisar;
- no ampliar silenciosamente las fuentes;
- no sustituir BigQuery MCP Server por handoffs, Knowledge Sets, Recommendation Sets, informes o evaluaciones anteriores;
- no utilizar artefactos de ejecuciones previas como fuente para construir una nueva ejecución;
- no completar mediante inferencias;
- registrar la causa exacta del bloqueo;
- solicitar aclaración o revisión cuando corresponda.

---

# Validación final

Antes de entregar cualquier informe:

1. Ejecutar `CHECKLIST.md`.
2. Confirmar que solo se utilizó BigQuery MCP Server.
3. Declarar las fuentes y artefactos consumidos.
4. Identificar la Presentation Projection aplicada.
5. Identificar la Presentation Policy aplicada, cuando exista.
6. Confirmar que no se utilizaron informes anteriores como fuente.
7. Confirmar que la salida conserva el contenido canónico y su trazabilidad.

---

# Definition of Done

La ejecución se considera completada cuando:

- el Execution Context está canonicalizado;
- el contexto oficial ha sido consultado;
- las fuentes utilizadas están autorizadas;
- BigQuery MCP Server ha sido el único Data Provider;
- Context Definition, Evidence Set, Knowledge Set y Recommendation Set están estabilizados;
- las recomendaciones están trazadas al conocimiento;
- Presentation Layer consume los artefactos canónicos sin volver a derivarlos;
- la proyección y el contexto comunicativo están resueltos;
- la política aplicada está identificada, cuando exista;
- las limitaciones y UNKNOWNs permanecen visibles;
- la equivalencia semántica está preservada;
- `CHECKLIST.md` está completado;
- no se han introducido hechos, interpretaciones ni recomendaciones no aprobados.