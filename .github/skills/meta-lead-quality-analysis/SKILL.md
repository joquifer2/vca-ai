---
name: meta-lead-quality-analysis
description: Ejecuta AUC-001 para analizar la calidad de leads de Meta Ads utilizando el contexto oficial, el workflow aprobado y BigQuery MCP Server como Data Provider autorizado.
id: SDD-SKILL-006
user-invocable: true
disable-model-invocation: false
---

# Skill - Meta Lead Quality Analysis

## Proposito

Ejecutar el caso de uso analitico AUC-001 para producir informes trazables sobre la calidad, evolucion y eficiencia de los leads captados mediante Meta Ads.

Esta skill actua como punto de activacion y orquestador. No implementa el procedimiento operativo fase a fase.

El orden operativo canonico se define exclusivamente en `RUNBOOK.md`.

Referencias de ejecucion:

- `RUNBOOK.md` define el procedimiento operativo.
- `references.md` define las fuentes obligatorias del caso.
- `CHECKLIST.md` valida la entrega.

Esta skill no sustituye las Specifications, los contratos ni las decisiones arquitectonicas del proyecto.

## Cuándo utilizar esta skill

Activar esta skill cuando la solicitud este relacionada con:

- calidad de leads de Meta Ads;
- volumen y evolucion de la captacion;
- eficiencia economica;
- campanas, conjuntos o anuncios;
- scoring o tiers de calidad;
- informes analiticos de lead quality;
- informes ejecutivos para Direccion;
- ejecucion del caso de uso AUC-001.

La solicitud puede formularse en lenguaje natural. El usuario no necesita mencionar la skill, AUC-001, los contratos ni las Specifications aplicables.

## Precedencia documental

- Los contratos prevalecen sobre esta skill, el Runbook, el Checklist y los perfiles.
- `SKILL.md` define activacion, alcance, modos e invariantes.
- `RUNBOOK.md` define el orden operativo.
- `CHECKLIST.md` valida la entrega.
- Los perfiles especializan fases concretas.

Si aparece una contradiccion entre activacion e implementacion operativa, usar `RUNBOOK.md` para el orden de ejecucion y los contratos para el alcance.

## Instrucciones obligatorias de inicio

No iniciar la ejecucion mediante una busqueda global del repositorio.

No utilizar `rg`, busquedas globales ni exploracion abierta del repositorio para descubrir fuentes analiticas, salvo que `references.md` contenga una ruta rota que deba localizarse.

Antes de adquirir evidencia o materializar una salida:

1. Leer `RUNBOOK.md`.
2. Resolver el modo de ejecucion conforme a la Fase 01 del Runbook.
3. Leer `references.md` y cargar los artefactos obligatorios cuando lo indique el orden operativo.
4. Seguir exclusivamente la secuencia definida en `RUNBOOK.md`.
5. Confirmar el Data Contract vigente.
6. Verificar la autorizacion de las fuentes.
7. Confirmar BigQuery MCP Server cuando el modo requiera evidencia nueva y se alcance la fase de Data Provider Validation.

No iniciar la adquisicion de evidencia si alguno de estos pasos no puede completarse.

## Data Provider y mecanismo de acceso

La evidencia debera adquirirse exclusivamente desde las fuentes autorizadas por:

- el Data Contract vigente;
- la configuracion publicada del workspace;
- las referencias oficiales del caso de uso.

El Data Provider se resolvera desde `configs/workspaces.json`.

Ese archivo define el workspace que debe utilizarse, el proyecto autorizado, los recursos permitidos y el mecanismo de acceso.

Una vez resuelto el workspace, la adquisicion de evidencia debera realizarse utilizando el BigQuery MCP Server asociado.

Antes de ejecutar cualquier consulta debera verificarse que las fuentes necesarias pertenecen al Data Contract y al workspace seleccionado.

La disponibilidad tecnica de una tabla no implica autorizacion metodologica.

Queda prohibido:

- consultar fuentes fuera del alcance aprobado;
- ampliar silenciosamente el conjunto de tablas;
- utilizar un mecanismo distinto al definido por el workspace;
- introducir acceso directo a BigQuery cuando el workspace exige MCP;
- continuar cuando no pueda verificarse la autorizacion de una fuente.

## Marco canónico vigente de AUC-001

Para ejecuciones AUC-001 posteriores a P04, la cadena operativa vigente incorpora tres contratos específicos sin cambiar la semántica del lifecycle base:

- `SPEC-014 - AUC-001 Analytical Product Contract`: define cobertura de preguntas de negocio, Common Product Core, preservación de coverage states, `UNKNOWN`, limitaciones y recomendaciones trazadas.
- `SPEC-015 - AUC-001 Canonical Projection Consolidation`: exige un `Canonical Projection Source` previo a cualquier informe; analytical y executive son proyecciones hermanas derivadas del mismo núcleo, no de prompts independientes ni una de otra.
- `SPEC-016 - AUC-001 Operational Acceptance Package Contract`: define preflight MCP, registro completo de llamadas MCP, estrategia de consultas independientes por tabla con reconciliación local controlada, manifest, fingerprints, trazabilidad física, higiene de namespace y handoff verificable.

Estos contratos son dependencias vigentes de la skill. No autorizan ampliar fuentes, reinterpretar SPEC-014/SPEC-015, modificar el servidor BigQuery MCP ni reutilizar outputs históricos como evidencia nueva.
## Modos de ejecucion

AUC-001 admite dos modos.

**Ejecucion completa**

Construye una nueva ejecucion desde contexto oficial, valida el Data Provider, adquiere evidencia desde BigQuery MCP Server y estabiliza Context Definition, Evidence Set, Knowledge Set, Recommendation Set y Presentation.

Este modo requiere obligatoriamente acceso a BigQuery MCP Server.

**Representacion de un Evidence Set existente**

Se usa solo cuando el usuario solicita trabajar sobre un Evidence Set previamente estabilizado y autorizado, sin adquirir ni actualizar evidencia.

En este modo:

- no se consulta BigQuery MCP Server;
- no se adquiere nueva evidencia;
- se reutiliza unicamente el Evidence Set indicado;
- se reconstruyen Knowledge Set, Recommendation Set y Presentation para la solicitud actual si el alcance lo permite.

Fuera de este modo, BigQuery MCP Server es obligatorio.

## Solicitud "desde cero"

Interpretar "desde cero" como:

- volver a adquirir la evidencia autorizada;
- reconstruir los artefactos canonicos;
- generar una nueva representacion.

No significa:

- ignorar la skill;
- ignorar el contexto oficial;
- ignorar los contratos;
- consultar cualquier tabla disponible;
- utilizar informes anteriores como fuente;
- omitir el workflow metodologico.

## Cadena canonica conceptual

La ejecucion preserva esta cadena conceptual:

```text
Context -> Evidence -> Knowledge -> Recommendations -> Common Product Core -> Canonical Projection Source -> Presentation
```

La secuencia operativa detallada de esa cadena vive solo en `RUNBOOK.md`.

Antes de iniciar Presentation deben existir y estar estabilizados:

- Context Definition;
- Evidence Set;
- Knowledge Set;
- Recommendation Set;
- Common Product Core conforme a SPEC-014;
- Canonical Projection Source conforme a SPEC-015.

Presentation Layer no puede reconstruir estos artefactos ni volver a razonar directamente desde los datos.

Coverage states, limitaciones, UNKNOWNs, prioridades y trazabilidad deben preservarse durante toda la ejecucion.

## Profundidad analitica del Knowledge Set

La calidad de AUC-001 depende de que Knowledge Generation ejecute un programa explicito de investigacion analitica antes de estabilizar conocimiento.

Ese programa no crea una nueva fase metodologica, no modifica los contratos y no sustituye el lifecycle canonico. Opera dentro de Knowledge Generation como disciplina interna de razonamiento.

Antes de producir el Knowledge Set, la ejecucion debe:

- recorrer la evidencia mediante preguntas de negocio adaptadas a la cobertura disponible;
- aplicar operaciones analiticas como segmentacion, comparacion, ranking multicriterio, analisis temporal, analisis relacional, concentracion, trade-offs, robustez y contraste de explicaciones alternativas cuando la evidencia lo permita;
- construir findings intermedios trazables, con observacion, soporte, importancia, incertidumbre y relacion con otros findings;
- descartar observaciones que solo repitan metricas o que no cambien la comprension del problema;
- consolidar los findings relacionados en insights, hipotesis, conclusiones, prioridades, riesgos e incertidumbres;
- mantener Recommendations fuera del Knowledge Set.

El objetivo no es aumentar la longitud del informe ni reproducir prompts historicos. El objetivo es recuperar el comportamiento analitico: descubrir patrones, relaciones, tensiones, anomalias y limites de interpretacion antes de sintetizar conocimiento.

Si la evidencia disponible no permite ejecutar alguna operacion esperada, debe registrarse la limitacion y no sustituirse por inferencia.

## Analytical Narrative / Strategic Interpretation

AUC-001 debe producir una lectura integrada del fenomeno observado, no solo un conjunto de insights independientes.

La Analytical Narrative es una operacion experimental de sintesis dentro del cierre de Knowledge Generation. No introduce una nueva fase arquitectonica, no modifica los contratos y no sustituye Presentation Layer.

Su funcion es transformar el Knowledge Set ya estabilizado en una explicacion breve, densa y trazable del fenomeno principal. Debe integrar varios elementos del Knowledge Set para responder:

- cual es el fenomeno principal que explica la mayor parte de la evidencia;
- que elementos del Knowledge Set estan relacionados entre si;
- que findings son estructurales y cuales son secundarios;
- que trade-off principal aparece;
- que riesgo o limitacion condiciona mas la lectura;
- que implicacion estrategica emerge del conjunto;
- que idea deberia recordar el lector una semana despues.

La Analytical Narrative solo puede usar Context Definition, Knowledge Set estabilizado, limitaciones, UNKNOWNs, coverage states y niveles de confianza ya registrados.

No puede consultar BigQuery, Evidence Set bruto, tablas, outputs historicos, Recommendation Set ni informes anteriores.

No puede producir nuevos findings, nuevo Knowledge, recomendaciones encubiertas ni adaptacion comunicativa propia de Presentation.

Su salida debe construir una tesis integrada, no repetir una lista de insights.
## Aislamiento entre ejecuciones

Los artefactos persistidos documentan ejecuciones anteriores. No representan el estado logico de la ejecucion actual ni sustituyen el workflow.

Pueden utilizarse solo para recuperar contexto funcional, comparar resultados entre ejecuciones, validar consistencia, auditoria y trazabilidad. No pueden sustituir la adquisicion de nueva evidencia, el Evidence Set, el Knowledge Set, el Recommendation Set ni construir directamente la Presentation Layer.

Solo pueden ser la base principal cuando el usuario solicite explicitamente trabajar sobre una ejecucion anterior ya estabilizada o comparar resultados historicos.

Los artefactos canonicos requeridos por este workflow deben construirse o estabilizarse dentro de la ejecucion actual.

Queda prohibido utilizar como input analitico de una nueva ejecucion:

- Knowledge Sets anteriores;
- Recommendation Sets anteriores;
- Presentations o informes anteriores;
- conclusiones, hipotesis o recomendaciones de ejecuciones historicas.

Un Evidence Set anterior solo podra reutilizarse cuando:

- el usuario solicite explicitamente trabajar sobre evidencia ya adquirida;
- coincidan Execution Context, periodo, alcance y version contractual;
- quede registrada expresamente su reutilizacion;
- no se presente como evidencia adquirida de nuevo.

Un Knowledge Set o Recommendation Set anterior solo podra reutilizarse cuando la solicitud consista exclusivamente en volver a representar el mismo contenido canonico mediante otra Presentation Projection o Presentation Policy.

Para una nueva solicitud analitica, Knowledge y Recommendations deben generarse de nuevo desde la evidencia autorizada de la ejecucion actual.

## Invariantes globales

La ejecucion no podra:

- consultar fuentes fuera del Data Contract o del workspace autorizado;
- usar mecanismos no autorizados por el workspace;
- generar evidencia desde informes anteriores;
- mezclar Evidence, Knowledge y Recommendations;
- introducir recomendaciones no derivadas del Knowledge Set;
- ocultar limitaciones materiales o UNKNOWNs;
- alterar coverage states durante Presentation;
- derivar una proyeccion desde otra proyeccion;
- introducir conocimiento nuevo en Presentation;
- romper la equivalencia semantica entre artefactos canonicos y representacion.

## Criterios de bloqueo

Detener la ejecucion cuando:

- el modo de ejecucion no pueda resolverse;
- falte contexto obligatorio;
- `references.md` no pueda resolverse;
- el Data Contract no pueda identificarse;
- el runtime no pueda acceder a BigQuery MCP Server durante una ejecucion completa;
- no pueda verificarse que las fuentes pertenecen al Data Contract;
- una fuente necesaria no este autorizada;
- se detecte una fuente fuera del Data Contract;
- el Context Definition, Evidence Set, Knowledge Set o Recommendation Set no pueda estabilizarse;
- falte algun artefacto canonico, Common Product Core o Canonical Projection Source antes de Presentation Layer;
- la representacion requiera modificar el contenido canonico;
- no pueda garantizarse la equivalencia semantica.

En caso de bloqueo:

- no improvisar;
- no ampliar silenciosamente las fuentes;
- no sustituir BigQuery MCP Server por handoffs, Knowledge Sets, Recommendation Sets, informes o evaluaciones anteriores;
- no completar mediante inferencias;
- registrar la causa exacta del bloqueo;
- solicitar aclaracion o revision cuando corresponda.

## Definition of Done

La ejecucion se considera completada cuando:

- el modo de ejecucion esta resuelto;
- el orden operativo de `RUNBOOK.md` ha sido seguido;
- el contexto oficial ha sido consultado;
- el Data Contract vigente se ha aplicado;
- las fuentes utilizadas estan autorizadas;
- BigQuery MCP Server ha sido el unico Data Provider cuando se adquirio evidencia nueva;
- Context Definition, Evidence Set, Knowledge Set y Recommendation Set estan estabilizados;
- Common Product Core y Canonical Projection Source existen antes de cualquier informe cuando aplique SPEC-014/SPEC-015;
- las recomendaciones estan trazadas al conocimiento;
- Presentation Layer consume los artefactos canonicos sin volver a derivarlos;
- la proyeccion y el contexto comunicativo estan resueltos;
- la politica aplicada esta identificada, cuando exista;
- las limitaciones y UNKNOWNs permanecen visibles;
- la equivalencia semantica esta preservada;
- cuando se persiste un execution package, manifest, fingerprints, trazabilidad fisica, registro de llamadas MCP, higiene de namespace y handoff cumplen SPEC-016;
- el estado `READY_FOR_REVALIDATION` no se declara como aceptacion final sin gate QA fisico;
- `CHECKLIST.md` esta completado;
- no se han introducido hechos, interpretaciones ni recomendaciones no aprobados.