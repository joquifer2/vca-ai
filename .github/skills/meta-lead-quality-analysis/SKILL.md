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

El Data Provider autorizado define qué proyectos, datasets, tablas y campos pueden utilizarse.

El mecanismo técnico de acceso será resuelto por el runtime y podrá utilizar las capacidades disponibles en el entorno, siempre que preserve exactamente el alcance autorizado.

Antes de ejecutar cualquier consulta deberá verificarse que cada fuente solicitada está incluida en el Data Contract y en la configuración del workspace.

La disponibilidad técnica de una tabla no implica autorización metodológica.

Queda prohibido:

- consultar fuentes fuera del alcance aprobado;
- ampliar silenciosamente el conjunto de tablas;
- utilizar un mecanismo alternativo para eludir el Data Contract;
- continuar cuando no pueda verificarse la autorización de una fuente.

Si el runtime no puede acceder a las fuentes autorizadas, deberá detener la ejecución y registrar el bloqueo.

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

Detener la ejecución cuando:

- el Execution Context no pueda canonicalizarse;
- falte contexto obligatorio;
- `references.md` no pueda resolverse;
- el runtime no pueda acceder al Data Provider autorizado;
- no pueda verificarse que las fuentes pertenecen al Data Contract.
- una fuente necesaria no esté autorizada;
- se detecte una fuente fuera del Data Contract;
- el Evidence Set no pueda estabilizarse;
- el Knowledge Set no aporte conocimiento consolidado;
- el Recommendation Set no derive del Knowledge Set;
- falte algún artefacto canónico antes de Presentation Layer;
- la representación requiera modificar el contenido canónico;
- no pueda garantizarse la equivalencia semántica.

En caso de bloqueo:

- no improvisar;
- no ampliar silenciosamente las fuentes;
- no completar mediante inferencias;
- registrar la causa;
- solicitar aclaración o revisión.

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