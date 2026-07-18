# VCA IA

## Plataforma Analítica basada en IA

Versión documental: v1.0.0

Estado del proyecto: Development Authorized.

VCA IA es la plataforma de análisis asistido por IA de VCA para transformar contexto, datos y conocimiento del negocio en análisis trazables, conclusiones fundamentadas y recomendaciones reutilizables.

El proyecto se apoya en AIF Foundation como dependencia metodológica reutilizable. El objeto funcional de este repositorio es VCA IA.

---

## Propósito

El repositorio gobierna y documenta la Plataforma Analítica basada en IA de VCA.

Su función principal es mantener trazabilidad entre:

- contexto;
- evidencia;
- conocimiento;
- recomendaciones;
- outputs;
- decisiones y gates documentales.

El objetivo no es automatizar informes aislados, sino sostener un sistema analítico coherente, auditable y reutilizable.

---

## Estado actual

- Fase SDD: Development Authorized.
- Phase Gate: [gates/spec-008-development-entry-phase-gate.md](/gates/spec-008-development-entry-phase-gate.md).
- Primer caso analítico: [AUC-001 - Meta Lead Quality Analysis](/analytical_use_cases/auc-001/README.md).
- Cierre experimental AUC-001: [gates/auc-001-experimental-closure-gate.md](/gates/auc-001-experimental-closure-gate.md), decisión `READY FOR CLOSURE`.
- Producto analítico validado: [outputs/auc-001/2026-06-30/analytical-report.md](/outputs/auc-001/2026-06-30/analytical-report.md).

---

## Capacidades principales

- Definir y ejecutar casos de uso analíticos trazables.
- Separar contexto, evidencia, conocimiento, recomendaciones y presentación.
- Validar avance mediante gates documentales.
- Mantener decisiones y evaluaciones separadas.
- Reutilizar capacidades analíticas sin acoplar el sistema a una ejecución puntual.

---

## Estructura del repositorio

| Área | Propósito |
|---|---|
| [project_brief.md](/project_brief.md) | Definición del proyecto, alcance y criterios de éxito |
| [docs/context_refs.md](/docs/context_refs.md) | Índice detallado de contexto, trazabilidad y fuentes |
| [specs/](/specs/) | Specifications del marco analítico |
| [analytical_use_cases/](/analytical_use_cases/) | Casos de uso analíticos e índices por caso |
| [.github/skills/](/.github/skills/) | Skills operativas asociadas a casos de uso |
| [docs/contracts/](/docs/contracts/) | Contratos transversales |
| [docs/decisions/](/docs/decisions/) | Decisiones estabilizadas |
| [docs/evaluations/](/docs/evaluations/) | Investigaciones, experimentos, validaciones y diagnósticos |
| [docs/corpus/](/docs/corpus/) | Corpus histórico usado como referencia experimental |
| [outputs/](/outputs/) | Productos analíticos validados por ejecución |
| [gates/](/gates/) | Phase, QA y closure gates |
| [docs/tasks.md](/docs/tasks.md) | Backlog documental y gobernanza de trabajo |

---

## Source of Truth mínima

| Fuente | Propósito |
|---|---|
| [project_brief.md](/project_brief.md) | Propósito y alcance del proyecto |
| [docs/context_refs.md](/docs/context_refs.md) | Trazabilidad detallada y contexto oficial |
| [specs/](/specs/) | Lifecycle, boundaries, extensibilidad y gates |
| [analytical_use_cases/](/analytical_use_cases/) | Casos analíticos y estado por caso |
| [.github/skills/](/.github/skills/) | Ejecución operativa de skills |
| [docs/contracts/](/docs/contracts/) | Contratos metodológicos y documentales |
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

- Mantener separación entre metodología, gobernanza, evaluación y outputs.
- No convertir evaluaciones históricas en fuentes canónicas.
- No duplicar decisiones estabilizadas dentro de evaluations.
- Registrar nuevas rutas relevantes en [docs/context_refs.md](/docs/context_refs.md).
- Tratar AIF Foundation como dependencia metodológica reutilizable, no como producto funcional del repositorio.