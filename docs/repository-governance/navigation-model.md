# Navigation Model

Estado: Draft inicial.

Tipo de artefacto: Modelo de navegacion documental.

Estructura: Inferida. No existe template especifico para modelo de navegacion en `docs/templates/`.

Fecha: 2026-07-28

Revision requerida: Reviewer Agent y QA Gate Agent.

---

## 1. Proposito

Este modelo inicial propone rutas de lectura para entender y mantener `VCA IA` sin duplicar contenido canonico.

No sustituye `README.md` ni `docs/context_refs.md`; los complementa como guia de navegacion.

---

## 2. Entrada general

Para comprender el proyecto:

1. `README.md`
2. `project_brief.md`
3. `docs/context_refs.md`

Para resolver conflictos documentales:

1. Consultar la precedencia oficial en `.github/instructions/sdd.instructions.md`.
2. Revisar el artefacto afectado segun su categoria.
3. Registrar cualquier correccion como cambio documental trazable.

---

## 3. Rutas por necesidad

| Necesidad | Ruta recomendada |
|---|---|
| Entender proposito y alcance | `README.md` -> `project_brief.md` |
| Identificar fuentes oficiales | `docs/context_refs.md` |
| Revisar metodologia SDD | `.github/instructions/sdd.instructions.md` -> `.github/agents/` |
| Revisar una capacidad | `specs/` -> `gates/` -> `tasks/` |
| Revisar un caso analitico | `analytical_use_cases/` -> skill aplicable -> gates relacionados |
| Revisar decisiones | `docs/decisions/` |
| Revisar validaciones | `docs/evaluations/` -> scope correspondiente |
| Revisar handoff | `docs/handoffs/` |
| Revisar gobernanza transversal | `docs/repository-governance/` |

---

## 4. Navegacion de AUC-001

AUC-001 tiene routing obligatorio propio para solicitudes operativas o analiticas relacionadas con calidad de leads de Meta, Meta Lead Ads, scoring FARO, tiers A/B, eficiencia economica de campanas Meta y temas equivalentes.

Este modelo no altera ese routing. Para esas solicitudes aplica primero `AGENTS.md` y la skill correspondiente.

En esta iteracion, AUC-001 solo se menciona como area protegida y como ejemplo de caso estable ya documentado.

---

## 5. WS-3

`WS-3` puede tratarse en el futuro como propuesta documental, no ejecutable y no canonica. No forma parte de la navegacion vigente ni autoriza crear workflows, runtime o automatizaciones.

---

## 6. Mantenimiento

Cuando se incorpore un nuevo artefacto transversal:

1. Confirmar si existe template aplicable.
2. Ubicarlo por funcion primaria.
3. Marcar estado real: inicial, draft, candidato, vigente o historico.
4. Evitar duplicar contenido canonico.
5. Añadir referencias cruzadas solo cuando aporten navegacion o trazabilidad.