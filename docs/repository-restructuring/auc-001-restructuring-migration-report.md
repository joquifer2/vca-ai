# AUC-001 Restructuring Migration Report

## Metadata

| Field | Value |
|---|---|
| Artifact type | migration report |
| Scope | AUC-001 repository documentation restructuring |
| Status | Completed |
| Branch | auc-001-doc-restructuring |
| Date | 2026-07-16 |
| Responsible agent | Documentation Agent |

## 1. Movimientos realizados

Se ejecutó la propuesta aprobada de forma conservadora.

### Decisiones

Movidas a `docs/decisions/auc-001/`:

- `auc-001-execution-scope-canonicalization-architectural-decision.md`
- `auc-001-presentation-projection-architectural-decision.md`
- `auc-001-communication-context-representation-transformation-architectural-decision.md`
- `auc-001-documentary-alignment-decision.md`

### Evaluaciones AUC-001

Reclasificadas bajo:

- `docs/evaluations/auc-001/investigations/`
- `docs/evaluations/auc-001/experiments/`
- `docs/evaluations/auc-001/validations/`
- `docs/evaluations/auc-001/diagnostics/`
- `docs/evaluations/auc-001/historical/`

### Evaluaciones SPEC-011

Reclasificadas bajo:

- `docs/evaluations/spec-011/investigations/`
- `docs/evaluations/spec-011/experiments/`
- `docs/evaluations/spec-011/validations/`
- `docs/evaluations/spec-011/historical/`

### Evaluaciones transversales

Reclasificadas bajo:

- `docs/evaluations/transversal/investigations/`
- `docs/evaluations/transversal/experiments/`
- `docs/evaluations/transversal/validations/`
- `docs/evaluations/transversal/diagnostics/`
- `docs/evaluations/transversal/historical/`

### Corpus

Movido desde `docs/evaluations/corpus/` a `docs/corpus/auc-001/`.

### Output analítico final

Movido desde `docs/handoffs/auc-001-analytical-report-2026-06-30.md` a:

`outputs/auc-001/2026-06-30/analytical-report.md`

Esta queda como única ruta canónica del producto analítico validado de esa ejecución.

## 2. Renombrados

- El gate canónico de cierre queda como `gates/auc-001-experimental-closure-gate.md`.
- No se conservaron copias con nombres anteriores.
- Metadata normalizada: `Gate ID` pasa a `VCA-AUC-001-GATE-CLOSURE-001` y `Gate Type` queda `Experimental Closure Gate`.

## 3. Documentos clasificados como históricos

Se usó `historical/`, no `archive/`, para:

- closure reconciliation previo al closure gate;
- assessments sustituidos por records;
- planes experimentales ejecutados o superados;
- reviews o versiones preliminares sin vigencia operativa.

## 4. Índices creados

- `analytical_use_cases/README.md`
- `analytical_use_cases/auc-001/README.md`
- `docs/evaluations/README.md`
- `gates/README.md`

## 5. Enlaces actualizados

Se actualizaron referencias en:

- `README.md`
- `docs/context_refs.md`
- `docs/tasks.md`
- `analytical_use_cases/auc-001/analytical-contract.md`
- `gates/auc-001-experimental-closure-gate.md`
- documentos movidos bajo `docs/evaluations/`
- contracts y handoffs que enlazaban decisiones movidas

Los enlaces Markdown fueron normalizados a rutas desde raíz (`/docs/...`, `/outputs/...`) cuando el cambio de profundidad podía romper rutas relativas.

## 6. Estado final de AUC-001

`analytical_use_cases/meta_lead_quality_analysis.md` queda con:

```yaml
status: Active
validation_status: Validated
experimental_cycle: Closed
```

La decisión responde a la aprobación del closure gate y evita la contradicción previa entre caso base, Analytical Contract y `READY FOR CLOSURE`.

## 7. Ubicación canónica del producto final

`outputs/auc-001/2026-06-30/analytical-report.md`

El informe ejecutivo permanece como handoff documentado en `docs/handoffs/auc-001-executive-report.md`.

## 8. Desviaciones respecto a la propuesta inicial

- Se sustituyó `archive/` por `historical/`, según aprobación del usuario.
- No se renombró `analytical_use_cases/meta_lead_quality_analysis.md` a `definition.md`.
- No se clasificaron decisiones por subcategorías internas.
- No se creó una política completa de outputs futuros.
- No se eliminó ni fusionó ningún documento histórico.

## 9. Notas sobre Git

Los movimientos se realizaron mediante operaciones de filesystem dentro del workspace. Git debería detectar renombrados por similitud en `git diff --find-renames`; los cambios no han sido staged.

## 10. Correcciones residuales posteriores a revisión independiente

Tras la revisión independiente se aplicaron correcciones puntuales sin cambiar metodología, veredicto ni estructura:

- corregido en `analytical_use_cases/auc-001/README.md` el enlace visible `../../docs/docs/evaluations/README.md` a `../../docs/evaluations/README.md`;
- actualizado `gates/auc-001-experimental-closure-gate.md` para declarar `outputs/auc-001/2026-06-30/analytical-report.md` como producto analítico final validado;
- mantenido `docs/evaluations/auc-001/validations/auc-001-analytical-narrative-validation.md` como evidencia de validación, no como ubicación canónica del informe final;
- eliminada del texto visible del gate la antigua ruta `docs/handoffs/auc-001-analytical-report-2026-06-30.md`.

## 11. Correcciones finales previas al merge

Se aplicaron correcciones editoriales y de gobernanza documental sin cambiar metodología, veredicto ni estructura aprobada:

- normalización ortográfica de tildes en documentos principales de la reestructuración;
- cambio en `README.md` de `Version estable: v1.0.0` a `Versión documental: v1.0.0`, sin introducir una política nueva de versionado;
- actualización de `project_brief.md` para reflejar el estado vigente `Development Authorized`;
- actualización de referencias al SDD Readiness Assessment como evidencia histórica en `docs/evaluations/transversal/historical/sdd_readiness_assessment.md`, respetando la reubicación ya realizada por el usuario;
- conversión de pseudo-enlaces Markdown a outputs históricos no existentes en referencias de código para mantener `BROKEN_COUNT=0`.
