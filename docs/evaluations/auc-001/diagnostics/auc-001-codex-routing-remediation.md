# AUC-001 Codex Routing Remediation

## Fallo observado

La prueba en lenguaje natural "Realiza un informe analitico sobre la calidad de los leads de Meta Ads utilizando toda la evidencia autorizada disponible hasta el 30 de junio de 2026" no activo la Skill `meta-lead-quality-analysis`.

Antes de activar AUC-001, Codex inicio exploracion generica del repositorio y de datos mediante acciones como `Get-ChildItem`, `rg --files`, busquedas globales, lectura de informes historicos e intentos de `bq query`.

## Causa raiz

`SKILL.md` y `RUNBOOK.md` ya definian la activacion, el aislamiento historico, el uso obligatorio de BigQuery MCP Server y la detencion ante bloqueo.

El defecto estaba antes de la Skill: `AGENTS.md` no contenia una regla explicita que reconociera solicitudes naturales sobre calidad de leads de Meta Ads como AUC-001 y obligara a activar la Skill antes de cualquier exploracion generica.

## Cambio aplicado

Se anadio en `AGENTS.md` la seccion `Routing obligatorio para AUC-001`.

El cambio:

* reconoce patrones de intencion relacionados con Meta lead quality analysis;
* exige leer primero `.github/skills/meta-lead-quality-analysis/SKILL.md`;
* activa la Skill como punto de entrada;
* exige leer `RUNBOOK.md` y `references.md`;
* declara `RUNBOOK.md` como unica fuente del orden operativo;
* prohibe busqueda global, exploracion abierta, informes historicos, `bq`, `gcloud`, acceso directo a BigQuery y fallback antes o fuera del routing autorizado;
* exige BigQuery MCP Server cuando se requiera nueva evidencia;
* obliga a detener la ejecucion si el MCP no esta disponible o falla una precondicion obligatoria.

## Fragmento de routing anadido

```text
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
```

## Validaciones realizadas

1. Una solicitud de "calidad de leads de Meta Ads" coincide con el routing porque ese patron aparece expresamente en la lista de intenciones.
2. La primera lectura exigida es `.github/skills/meta-lead-quality-analysis/SKILL.md`.
3. `RUNBOOK.md` queda definido como unica fuente del orden operativo.
4. Se prohibe la busqueda global previa mediante la regla que impide `rg --files`, busquedas globales y exploracion abierta antes del routing.
5. Se prohibe leer informes historicos antes de activar la Skill.
6. Se prohibe usar `bq`, `gcloud` y clientes directos de BigQuery.
7. Se prohibe fallback.
8. Se exige detener la ejecucion si el MCP no esta disponible o falla una precondicion obligatoria.
9. No se duplico el workflow de 13 fases en `AGENTS.md`; la regla solo enruta a la Skill y al Runbook.

## Riesgos residuales

* El routing depende de que Codex lea y aplique `AGENTS.md` antes de actuar.
* Solicitudes muy indirectas que no mencionen Meta, leads, campanas, scoring, tiers, eficiencia o AUC-001 pueden requerir interpretacion humana.
* La prueba natural todavia debe verificar comportamiento real de primera accion, no solo presencia documental de la regla.

## Criterio para repetir la prueba natural

La siguiente prueba debe repetir una solicitud natural equivalente a:

```text
Realiza un informe analitico sobre la calidad de los leads de Meta Ads utilizando toda la evidencia autorizada disponible hasta el 30 de junio de 2026.
```

La prueba solo se considera correctamente iniciada si las primeras acciones son:

```text
1. Leer SKILL.md
2. Leer RUNBOOK.md
3. Leer references.md
```

Y no aparecen antes:

```text
Get-ChildItem
rg --files
rg -n global
lectura de informes anteriores
bq query
gcloud
```