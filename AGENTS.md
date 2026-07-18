# AGENTS.md

## Propósito

Este documento describe los agentes metodológicos que forman parte de JQF SDD Foundation.

Su función es gobernar, documentar, revisar y validar la evolución de proyectos construidos mediante Specification Driven Development (SDD).

Estos agentes forman parte del SDD Harness.

No representan capacidades funcionales de negocio.

No forman un sistema multiagente operativo.

No ejecutan procesos productivos.

---

## Relación con el SDD Harness

Los agentes metodológicos son componentes especializados del SDD Harness.

Su responsabilidad es ayudar a mantener:

* coherencia documental;
* trazabilidad;
* control de alcance;
* readiness;
* validación;
* evolución controlada.

Los agentes metodológicos no sustituyen la validación humana.

Todas las decisiones relevantes permanecen bajo responsabilidad humana.

---

## Clasificación de agentes

### Agentes de definición

Responsables de transformar contexto y necesidades en artefactos estructurados.

* Specification Agent
* Architect Agent

---

### Agentes de planificación

Responsables de transformar definiciones en trabajo estructurado.

* Tasks Planner Agent

---

### Agentes de revisión

Responsables de revisar calidad y coherencia.

* Reviewer Agent
* Documentation Agent

---

### Agentes de validación

Responsables de verificar readiness y criterios de avance.

* QA Gate Agent

---

### Agentes de transición

Responsables de supervisar el paso desde Structure hacia Development.

* Implementation Agent

---

## Catálogo de agentes

| Agente                | Responsabilidad principal                                        |
| --------------------- | ---------------------------------------------------------------- |
| Specification Agent   | Crear y revisar specifications                                   |
| Architect Agent       | Diseñar estructura documental y arquitectura conceptual          |
| Tasks Planner Agent   | Transformar specifications en tareas trazables                   |
| Reviewer Agent        | Revisar coherencia, alcance y calidad documental                 |
| Documentation Agent   | Mantener documentación consistente y actualizada, distinguiendo entre Foundation y Proyecto Derivado para evitar crear instancias reales dentro de repositorios Foundation. |
| QA Gate Agent         | Validar readiness y cumplimiento de criterios de fase            |
| Implementation Agent  | Supervisar la transición controlada hacia Development            |

---

## Flujo metodológico recomendado

```text
Project Brief
        ↓
Specification Agent
        ↓
Architect Agent
        ↓
Tasks Planner Agent
        ↓
Reviewer Agent
        ↓
Documentation Agent
        ↓
QA Gate Agent
        ↓
Implementation Agent
```

La secuencia puede variar según el proyecto.

El objetivo es garantizar que la implementación nunca preceda a la definición.


## Routing obligatorio para AUC-001

Para solicitudes que coincidan con AUC-001, este routing debe aplicarse antes de cualquier comportamiento generico de exploracion del repositorio.

Cuando la solicitud este relacionada con cualquiera de estos temas:

* calidad de leads de Meta Ads;
* Meta Lead Ads;
* volumen o evolucion de leads de Meta;
* scoring FARO;
* tiers A/B;
* eficiencia economica de campanas Meta;
* campanas, conjuntos o anuncios de Meta;
* informes analiticos o ejecutivos de lead quality;
* AUC-001.

Codex debe:

1. Leer primero `.github/skills/meta-lead-quality-analysis/SKILL.md`.
2. Activar esa Skill como punto de entrada.
3. Leer `.github/skills/meta-lead-quality-analysis/RUNBOOK.md` y `.github/skills/meta-lead-quality-analysis/references.md`.
4. Seguir `RUNBOOK.md` como unica fuente del orden operativo.
5. No realizar antes `rg --files`, busquedas globales, exploracion abierta del repositorio, lectura de informes historicos, lectura de evaluaciones anteriores, consultas BigQuery ni acceso por CLI.
6. No utilizar `bq`, `gcloud`, clientes directos de BigQuery, informes historicos como fuente analitica, Evidence Sets anteriores salvo solicitud expresa del usuario, ni fallback.
7. Cuando la ejecucion requiera nueva evidencia, utilizar exclusivamente el BigQuery MCP Server definido por el workspace.
8. Si el MCP no esta disponible o falla una precondicion obligatoria, detener la ejecucion, registrar el bloqueo y no continuar con datos historicos ni mecanismos alternativos.

---

## Recuperación de autenticación del BigQuery MCP Server

Cuando una ejecución AUC-001 falle durante `Data Provider Validation` con:

```text
ERR_AUTH_REQUIRED
A valid read-only service identity is required
```

Codex debe interpretar el error como una posible expiración o invalidez de las ADC impersonadas utilizadas por el proceso local del BigQuery MCP Server.

La identidad esperada es:

```text
bq-mcp-reader@datamart-vca-494114.iam.gserviceaccount.com
```

La cuenta autorizada para renovar las ADC es:

```text
jordi@viajaconalvaro.com
```

Procedimiento obligatorio:

1. Detener la ejecución AUC-001.
2. No utilizar `bq`, clientes directos, informes históricos, Evidence Sets previos ni fallback.
3. Informar al usuario de que debe renovarse la autenticación local.
4. Solicitar autorización explícita antes de ejecutar cualquier comando que modifique ADC o credenciales locales.
5. Tras recibir autorización:

   * renovar las ADC impersonadas;
   * reiniciar el proceso del BigQuery MCP Server;
   * validar `discover_metadata` mediante MCP;
   * reanudar la solicitud como una nueva ejecución completa.
6. Si la renovación requiere autenticación interactiva que Codex no puede completar, mostrar el comando exacto al usuario y detenerse hasta que confirme que ha finalizado.
7. No modificar IAM, workspace, allowlist, contratos ni código del servidor como parte de esta recuperación.

La renovación de ADC es una acción de mantenimiento del runtime local, no una vía alternativa de acceso a BigQuery.

---

## Relación con proyectos derivados

Los proyectos derivados pueden incorporar agentes operativos propios.

Ejemplos:

* agentes de reporting;
* agentes de forecasting;
* agentes analíticos;
* agentes de automatización;
* asistentes especializados.

Los agentes operativos no forman parte de esta Foundation.

Deben documentarse dentro del repositorio correspondiente.

---

## Principios comunes

Todos los agentes metodológicos deben:

* respetar la metodología SDD;
* respetar la precedencia documental;
* evitar implementación prematura;
* mantener trazabilidad;
* priorizar claridad sobre complejidad;
* favorecer la revisión humana;
* evitar duplicación documental.

---

## Fuera de alcance

Los agentes metodológicos no deben:

* implementar runtime;
* seleccionar tecnologías definitivas;
* crear herramientas reales;
* ejecutar integraciones;
* crear automatizaciones productivas;
* sustituir decisiones humanas.

Estas responsabilidades pertenecen a fases posteriores y a repositorios derivados.
