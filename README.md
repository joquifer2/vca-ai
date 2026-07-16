# VCA IA

## Plataforma Analitica basada en IA

Version estable: v1.0.0

Estado del proyecto: Development Authorized.

VCA IA es la plataforma de analisis asistido por IA de VCA para transformar contexto, datos y conocimiento del negocio en analisis trazables, conclusiones fundamentadas y recomendaciones reutilizables.

El proyecto se apoya en AIF Foundation como dependencia metodologica reutilizable. El objeto funcional de este repositorio es VCA IA.

---

## Proposito

El repositorio gobierna y documenta la Plataforma Analitica basada en IA de VCA.

Su funcion principal es mantener trazabilidad entre:

- contexto;
- evidencia;
- conocimiento;
- recomendaciones;
- outputs;
- decisiones y gates documentales.

El objetivo no es automatizar informes aislados, sino sostener un sistema analitico coherente, auditable y reutilizable.

---

## Estado actual

- Fase SDD: Development Authorized.
- Phase Gate: [gates/spec-008-development-entry-phase-gate.md](/gates/spec-008-development-entry-phase-gate.md).
- Primer caso analitico: [AUC-001 - Meta Lead Quality Analysis](/analytical_use_cases/auc-001/README.md).
- Cierre experimental AUC-001: [gates/auc-001-experimental-closure-gate.md](/gates/auc-001-experimental-closure-gate.md), decision `READY FOR CLOSURE`.
- Producto analitico validado: [outputs/auc-001/2026-06-30/analytical-report.md](/outputs/auc-001/2026-06-30/analytical-report.md).

---

## Capacidades principales

- Definir y ejecutar casos de uso analiticos trazables.
- Separar contexto, evidencia, conocimiento, recomendaciones y presentacion.
- Validar avance mediante gates documentales.
- Mantener decisiones y evaluaciones separadas.
- Reutilizar capacidades analiticas sin acoplar el sistema a una ejecucion puntual.

---

## Estructura del repositorio

| Area | Proposito |
|---|---|
| [project_brief.md](/project_brief.md) | Definicion del proyecto, alcance y criterios de exito |
| [docs/context_refs.md](/docs/context_refs.md) | Indice detallado de contexto, trazabilidad y fuentes |
| [specs/](/specs/) | Specifications del marco analitico |
| [analytical_use_cases/](/analytical_use_cases/) | Casos de uso analiticos e indices por caso |
| [.github/skills/](/.github/skills/) | Skills operativas asociadas a casos de uso |
| [docs/contracts/](/docs/contracts/) | Contratos transversales |
| [docs/decisions/](/docs/decisions/) | Decisiones estabilizadas |
| [docs/evaluations/](/docs/evaluations/) | Investigaciones, experimentos, validaciones y diagnosticos |
| [docs/corpus/](/docs/corpus/) | Corpus historico usado como referencia experimental |
| [outputs/](/outputs/) | Productos analiticos validados por ejecucion |
| [gates/](/gates/) | Phase, QA y closure gates |
| [docs/tasks.md](/docs/tasks.md) | Backlog documental y gobernanza de trabajo |

---

## Source of Truth minima

| Fuente | Proposito |
|---|---|
| [project_brief.md](/project_brief.md) | Proposito y alcance del proyecto |
| [docs/context_refs.md](/docs/context_refs.md) | Trazabilidad detallada y contexto oficial |
| [specs/](/specs/) | Lifecycle, boundaries, extensibilidad y gates |
| [analytical_use_cases/](/analytical_use_cases/) | Casos analiticos y estado por caso |
| [.github/skills/](/.github/skills/) | Ejecucion operativa de skills |
| [docs/contracts/](/docs/contracts/) | Contratos metodologicos y documentales |
| [gates/](/gates/) | Decisiones de avance y cierre |
| [docs/tasks.md](/docs/tasks.md) | Trabajo aprobado y trazable |

---

## Punto de entrada AUC-001

Para comprender AUC-001, leer primero:

1. [analytical_use_cases/auc-001/README.md](/analytical_use_cases/auc-001/README.md)
2. [analytical_use_cases/meta_lead_quality_analysis.md](/analytical_use_cases/meta_lead_quality_analysis.md)
3. [.github/skills/meta-lead-quality-analysis/SKILL.md](/.github/skills/meta-lead-quality-analysis/SKILL.md)
4. [gates/auc-001-experimental-closure-gate.md](/gates/auc-001-experimental-closure-gate.md)
5. [outputs/auc-001/2026-06-30/analytical-report.md](/outputs/auc-001/2026-06-30/analytical-report.md)

---

## Forma de trabajo esperada

- Mantener separacion entre metodologia, gobernanza, evaluacion y outputs.
- No convertir evaluaciones historicas en fuentes canonicas.
- No duplicar decisiones estabilizadas dentro de evaluations.
- Registrar nuevas rutas relevantes en [docs/context_refs.md](/docs/context_refs.md).
- Tratar AIF Foundation como dependencia metodologica reutilizable, no como producto funcional del repositorio.