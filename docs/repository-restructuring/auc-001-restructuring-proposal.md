# AUC-001 Repository Restructuring Proposal

## Metadata

| Field | Value |
|---|---|
| Artifact type | restructuring proposal |
| Scope | AUC-001 documentation, SPEC-011 supporting evaluations, transversal evaluation cleanup |
| Status | Draft for user review |
| Branch | auc-001-doc-restructuring |
| Created | 2026-07-16 |
| Responsible agent | Documentation Agent |
| Reviewer role | Reviewer Agent logical review |
| Movement status | Applied |

## 1. Diagnostico

`docs/evaluations/` funciona actualmente como deposito mixto. Contiene validaciones, decisiones arquitectonicas, planes, experimentos, corpus historico, diagnosticos, remediaciones, registros de alineamiento y evaluaciones finales. El problema no es perdida de trazabilidad, sino exceso de responsabilidad en una sola carpeta.

La reestructuracion debe separar:

- gates en `gates/`;
- decisiones estabilizadas en `docs/decisions/`;
- corpus en `docs/corpus/`;
- outputs analiticos en `outputs/`;
- evaluaciones, experimentos, diagnosticos e investigaciones en `docs/evaluations/` por scope y tipo;
- indices navegables en `README.md`, `docs/context_refs.md`, `analytical_use_cases/auc-001/README.md`, `docs/docs/evaluations/README.md` y `gates/README.md`.

## 2. Estructura actual observada

```text
docs/evaluations/
├── *.md                         # 54 documentos de scopes y tipos mezclados
└── corpus/                      # informes y prompt historicos

gates/
├── auc-001-experimental-closure-gate.md
├── spec-008-development-entry-phase-gate.md
├── specs-001-003-qa-gate.md
└── specs-004-007-qa-gate.md

analytical_use_cases/
├── meta_lead_quality_analysis.md
└── auc-001/
    └── analytical-contract.md

docs/handoffs/
└── auc-001-*.md                 # handoffs y outputs historicos/operativos
```

## 3. Estructura propuesta

Crear solo carpetas con contenido inmediato:

```text
analytical_use_cases/
├── README.md
├── meta_lead_quality_analysis.md
└── auc-001/
    ├── README.md
    └── analytical-contract.md

gates/
├── README.md
├── auc-001-experimental-closure-gate.md
├── spec-008-development-entry-phase-gate.md
├── specs-001-003-qa-gate.md
└── specs-004-007-qa-gate.md

docs/
├── decisions/
│   └── auc-001/
├── evaluations/
│   ├── README.md
│   ├── auc-001/
│   │   ├── investigations/
│   │   ├── experiments/
│   │   ├── validations/
│   │   ├── diagnostics/
│   │   └── historical/
│   ├── spec-011/
│   │   ├── investigations/
│   │   ├── experiments/
│   │   ├── validations/
│   │   └── historical/
│   └── transversal/
│       ├── investigations/
│       ├── experiments/
│       ├── validations/
│       ├── diagnostics/
│       └── historical/
├── corpus/
│   └── auc-001/
├── handoffs/
├── repository-restructuring/
└── context_refs.md

outputs/
└── auc-001/
    └── 2026-06-30/
```

## 4. Tabla completa de movimientos propuestos

La tabla completa por documento esta en `docs/repository-restructuring/auc-001-document-inventory.md`. Resumen por bloque:

| Bloque | Accion propuesta |
|---|---|
| `*-architectural-decision.md` estabilizados de AUC-001 | Mover a `docs/decisions/auc-001/` |
| `auc-001-documentary-alignment-decision.md` | Mover a `docs/decisions/auc-001/` |
| Validaciones AUC-001 vigentes | Mover a `docs/evaluations/auc-001/validations/` |
| Investigaciones AUC-001 | Mover a `docs/evaluations/auc-001/investigations/` |
| Experimentos AUC-001 | Mover a `docs/evaluations/auc-001/experiments/` |
| Diagnosticos/remediaciones AUC-001 | Mover a `docs/evaluations/auc-001/diagnostics/` |
| Assessments y planes superados | Mover a `docs/evaluations/auc-001/historical/` o `spec-011/historical/` |
| SPEC-011 docs | Mover bajo `docs/evaluations/spec-011/` segun tipo |
| Knowledge construction transversal | Mover bajo `docs/evaluations/transversal/` segun tipo |
| `docs/corpus/auc-001/` | Mover a `docs/corpus/auc-001/` |
| Informe analitico final 2026-06-30 | Proponer `outputs/auc-001/2026-06-30/analytical-report.md` |

## 5. Artefactos canonicos finales

| Responsabilidad | Artefacto canonico propuesto |
|---|---|
| Entrada general del repo | `README.md` |
| Indice detallado de trazabilidad | `docs/context_refs.md` |
| Definicion AUC-001 | `analytical_use_cases/meta_lead_quality_analysis.md` |
| Indice AUC-001 | `analytical_use_cases/auc-001/README.md` |
| Contrato analitico AUC-001 | `analytical_use_cases/auc-001/analytical-contract.md` |
| Skill | `.github/skills/meta-lead-quality-analysis/SKILL.md` |
| Runbook | `.github/skills/meta-lead-quality-analysis/RUNBOOK.md` |
| Checklist | `.github/skills/meta-lead-quality-analysis/CHECKLIST.md` |
| Gate cierre | `gates/auc-001-experimental-closure-gate.md` |
| Producto analitico final | `outputs/auc-001/2026-06-30/analytical-report.md` o, si se prefiere conservar handoff, `docs/handoffs/auc-001-analytical-report-2026-06-30.md` declarado como canonical output |
| Informe ejecutivo | `docs/handoffs/auc-001-executive-report.md` como handoff/documented executive representation |

Recomendacion: mover el informe analitico final a `outputs/auc-001/2026-06-30/analytical-report.md` y dejar el handoff ejecutivo como representacion/documented handoff. No duplicar dos informes analiticos canonicos.

## 6. Documentos historicos

Quedaran como historicos, sin borrarse:

- corpus historico completo bajo `docs/corpus/auc-001/`;
- plans ya ejecutados bajo `historical/`;
- assessments sustituidos por records bajo `historical/`;
- closure reconciliation review, superado por el closure gate, bajo `historical/`;
- reviews adversariales o versiones experimentales superadas bajo `historical/`.

## 7. Decisiones de naming

| Tema | Decision propuesta |
|---|---|
| Gate AUC-001 | `gates/auc-001-experimental-closure-gate.md` es nombre canonico unico. |
| Gate ID | Cambiar metadata de `VCA-AUC-001-GATE-FINAL-001` a `VCA-AUC-001-GATE-CLOSURE-001`. |
| AUC status | Usar `status: Active`, `validation_status: Validated`, `experimental_cycle: Closed` salvo que prefieras mantener `status: Validated`. |
| Decisions | Usar `docs/decisions/auc-001/` para decisiones estabilizadas. |
| Corpus | Usar `docs/corpus/auc-001/`; nada de corpus bajo evaluations. |
| Outputs | Usar `outputs/auc-001/YYYY-MM-DD/` para futuras ejecuciones. |

Nota: `analytical_use_cases/meta_lead_quality_analysis.md` ya aparece como `status: Validated` en el estado actual de la rama, pero `analytical_use_cases/auc-001/analytical-contract.md` todavia afirma que el caso base permanece `Proposed`. La migracion debe resolver esa contradiccion.

## 8. Impacto sobre enlaces

Los enlaces que deberan actualizarse estan principalmente en:

- `README.md`;
- `docs/context_refs.md`;
- `docs/tasks.md`;
- `analytical_use_cases/auc-001/analytical-contract.md`;
- `gates/auc-001-experimental-closure-gate.md`;
- documentos de `docs/evaluations/` que se enlazan entre si;
- algunos contracts y handoffs que referencian decisiones de presentation/canonicalization.

Estrategia propuesta:

1. aplicar movimientos mediante `git mv`;
2. ejecutar reemplazo de rutas exactas desde el inventario;
3. comprobar referencias antiguas con `rg`;
4. ejecutar QA de enlaces Markdown.

## 9. Riesgos

| Riesgo | Mitigacion |
|---|---|
| Romper enlaces relativos entre documentos movidos | Actualizar enlaces tras movimientos y ejecutar QA de Markdown links. |
| Convertir outputs y validations en dos fuentes canonicas | Elegir una unica ruta canonica para el informe final. |
| Mover a historical un documento que todavia se usa como decision vigente | Mover decisiones estabilizadas a `docs/decisions/`, no a historical. |
| Profundidad excesiva | Crear solo carpetas con contenido inmediato; no crear placeholders vacios. |
| Modificar metodologia por accidente | No tocar SPEC-010, SPEC-011, contratos, Skill, Runbook, Checklist ni policies salvo enlaces si fuera imprescindible. |
| Cambios previos no relacionados en worktree | Mantenerlos visibles en migration report; no revertirlos. |

## 10. Acciones que no se realizaran en esta reestructuracion

- No se eliminara ningun documento historico.
- No se fusionaran evaluaciones ni investigaciones.
- No se modificara metodologia AUC-001.
- No se promovera nada a AIF Foundation.
- No se reejecutara BigQuery ni se generara evidencia analitica nueva.
- No se reescribira el contenido sustantivo de SPEC-010, SPEC-011, contratos, Skill, Runbook, Checklist o Presentation Policies.

## 11. Reviewer Agent logical review

Resultado: PASS WITH CONDITIONS.

| Criterio | Resultado | Observacion |
|---|---|---|
| No se pierde trazabilidad | Pass | Todos los documentos se conservan; los historicos se archivan, no se borran. |
| No se ocultan decisiones vigentes | Pass | Decisiones estabilizadas se promueven a `docs/decisions/`. |
| Ningun gate termina dentro de evaluations | Pass | Gates permanecen en `gates/`. |
| Corpus fuera de evaluations | Pass | `docs/corpus/auc-001/` se mueve a `docs/corpus/auc-001/`. |
| Outputs no se confunden con validations | Pass with condition | Debe elegirse ruta canonica unica para el informe final. Recomendacion: `outputs/auc-001/2026-06-30/analytical-report.md`. |
| Canonicos identificables | Pass with condition | Requiere crear `analytical_use_cases/auc-001/README.md`, `docs/docs/evaluations/README.md`, `gates/README.md`. |
| Estructura no excesivamente profunda | Pass | Maximo scope/tipo; sin carpetas vacias. |
| Nombres consistentes | Pass with condition | Actualizar Gate ID y contradiccion `Proposed` en analytical contract. |

## 12. Recomendacion de aprobacion

Aprobar la propuesta con estas condiciones antes de aplicar movimientos:

1. aceptar `gates/auc-001-experimental-closure-gate.md` como nombre canonico unico;
2. aceptar mover decisiones estabilizadas a `docs/decisions/auc-001/`;
3. aceptar mover corpus a `docs/corpus/auc-001/`;
4. elegir ruta canonica del producto final analitico: recomendada `outputs/auc-001/2026-06-30/analytical-report.md`;
5. aceptar normalizacion de estado AUC-001 a `status: Active`, `validation_status: Validated`, `experimental_cycle: Closed` o confirmar que `status: Validated` debe permanecer.