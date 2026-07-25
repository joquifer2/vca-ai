# AUC-001-EXP-COMP-001 Implementation Handoff

## Estado

IMPLEMENTED FOR EXPERIMENTAL REVIEW.

## Alcance aplicado

Se implemento un contrato local experimental para gobernanza de comparaciones en AUC-001, sin modificar Strategic Context, sin abrir SPEC Foundation y sin introducir una taxonomia universal.

La implementacion queda limitada a `vca-ai` y a los helpers runtime locales del contrato analitico AUC-001.

## Artefactos de referencia

- Especificacion experimental: `docs/evaluations/auc-001/experiments/auc-001-exp-comp-001-final-experimental-specification.md`
- Entry Gate: `gates/auc-001-exp-comp-001-entry-gate.md`
- Plan autorizado: `tasks/auc-001-exp-comp-001-comparison-governance-task-plan.md`

## Cambios implementados

- `tools/auc_001_analytical_product_contract.py`
  - Anade constantes locales para tipos de comparacion, equivalencia estrategica y estados de gobernanza experimental.
  - Anade `ComparisonClassification` como estructura local opcional.
  - Valida clasificaciones declaradas por Analytical Reasoning.
  - Transporta `comparison_classifications` desde CPC hacia CPS y desde CPS hacia proyecciones.
  - Valida que recomendaciones no dependan de comparaciones bloqueadas.
  - Valida que Presentation no diverja de CPS ni presente referencias a comparaciones bloqueadas.
  - Permite referencias estructuradas a comparaciones en secciones de Presentation.

- `tests/evals/auc_001_comparison_governance_tests.ps1`
  - Cubre fixtures sinteticos para multi-label, equivalencia desconocida, comportamiento bloqueado, recomendacion con comparacion bloqueada, transporte CPC -> CPS -> proyeccion y bloqueo en Presentation.

## Validacion ejecutada

- `python -m py_compile tools/auc_001_analytical_product_contract.py` -> PASS
- `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_comparison_governance_tests.ps1` -> PASS
- `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_analytical_product_contract_tests.ps1` -> PASS, 14 checks
- `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_canonical_projection_source_tests.ps1` -> PASS, 4 checks

## Restricciones preservadas

- No se consulto BigQuery.
- No se adquirio evidencia nueva.
- No se modificaron outputs analiticos.
- No se modifico Strategic Context.
- No se modificaron SPEC Foundation, SPEC-014, SPEC-015 ni SPEC-016.
- No se abrio una nueva SPEC.

## Resultado

La implementacion esta lista para revision experimental. El contrato minimo permite validar si la clasificacion explicita de comparaciones reduce inferencias economicas o jerarquias implicitas sin eliminar comparaciones descriptivas utiles.
## Correccion Posterior A Revision

Estado: REVIEWER FOLLOW-UP IMPLEMENTED.

- `CHG-003: fully implemented`.
- `unknown-equivalence recommendation restriction: implemented`.

### Cambios adicionales aplicados

- `validate_comparison_classification()` distingue explicitamente entre claim provisional previo a Knowledge y claim material con Knowledge Set estabilizado mediante `knowledge_set_stabilized` y `knowledge_items`.
- Las comparaciones materiales con Knowledge estabilizado requieren `stabilized_claim_refs.knowledge_refs` no vacias y `reconciliation_status = reconciled`.
- Los estados `not_applicable`, `pending`, `missing`, `unresolved`, `unknown` o vacios producen issue bloqueante cuando el claim material ya alcanzo Knowledge.
- Las `knowledge_refs` declaradas se resuelven contra identidades reales del Knowledge Set cuando este esta disponible.
- `validate_recommendation_comparison_refs()` considera conjuntamente `comparison_type`, `strategic_equivalence`, `governance_status`, categoria de recomendacion y contenido semantico.
- Las recomendaciones economicas, jerarquicas, de priorizacion, superioridad u optimizacion basadas en equivalencia `unknown` quedan bloqueadas.
- Se preservan como validas las hipotesis no accionables, experimentos medibles y acciones verificables orientadas a resolver o reconciliar la incertidumbre.

### Fixtures nuevos anadidos

- Provisional claim con Knowledge estabilizado, `knowledge_refs` vacias y `reconciliation_status = not_applicable` -> PASS esperado: falla con issue bloqueante.
- `knowledge_refs` presentes pero inexistentes en Knowledge Set -> PASS esperado: falla con issue bloqueante.
- Claim todavia provisional anterior a Knowledge -> PASS esperado: valido.
- Recomendacion economica concluyente sobre comparacion `unknown` -> PASS esperado: falla.
- Recomendacion jerarquica/priorizacion sobre comparacion `unknown` -> PASS esperado: falla.
- Hipotesis no accionable para resolver `unknown` -> PASS esperado: valida.
- Experimento medible para resolver `unknown` -> PASS esperado: valido.
- Recomendacion basada en comparacion equivalente y gobernada -> PASS esperado: valida.

### Validacion posterior ejecutada

- `python -m py_compile tools/auc_001_analytical_product_contract.py` -> PASS
- `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_comparison_governance_tests.ps1` -> PASS
- `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_analytical_product_contract_tests.ps1` -> PASS, 14 checks
- `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_canonical_projection_source_tests.ps1` -> PASS, 4 checks
- `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_operational_acceptance_package_tests.ps1` -> PASS, 4 checks

### Observaciones arquitectonicas no bloqueantes

El modulo `tools/auc_001_analytical_product_contract.py` concentra modelos contractuales, validadores de Strategic Context, gobernanza de comparaciones, validacion de Knowledge/Recommendations, CPC, CPS y Presentation. Esta concentracion se mantiene aceptada para el experimento local.

Si la capacidad se valida experimentalmente y se propone para AIF Foundation, Architect Agent deberia evaluar una separacion de responsabilidades entre modelos de comparacion, validadores de reconciliacion, reglas de Strategic Context, gobernanza de recomendaciones y gobernanza de proyecciones.

No se implementa esa separacion ahora porque ampliaria el alcance experimental, aumentaria riesgo de regresion y aun no existe evidencia suficiente para definir una arquitectura reusable definitiva.

### Confirmacion de alcance

- No se generalizo la solucion a AIF Foundation.
- No se modifico Strategic Context.
- No se abrio nueva SPEC Foundation.
- No se introdujo evidencia nueva.
- No se modificaron outputs analiticos.
- No se realizo refactorizacion amplia del modulo.

## Correccion Segunda Revision Reviewer

Estado: REVIEWER FOLLOW-UP FINAL ADJUSTMENT IMPLEMENTED.

### Ajustes aplicados

- Las `knowledge_refs` se validan siempre contra el Knowledge Set disponible cuando `knowledge_set_stabilized=True`, incluso si el Knowledge Set esta vacio.
- Un Knowledge Set estabilizado vacio ya no permite que `knowledge_refs` declaradas pasen como reconciliadas.
- La deteccion de decisiones concluyentes sobre equivalencia `unknown` cubre tambien patrones basicos como `redistribuir presupuesto`, `mejor eficiencia`, `eficiencia comparada` y `priorizar`.

### Fixtures adicionales de cierre

- `CMP-REF-AGAINST-EMPTY-KS`: `knowledge_refs` contra Knowledge Set estabilizado vacio -> falla con `COMPARISON_KNOWLEDGE_REF_UNRESOLVED`.
- `REC-REDISTRIBUIR-PRESUPUESTO`: recomendacion `Redistribuir presupuesto ... por mejor eficiencia` sobre comparacion economica con equivalencia `unknown` -> falla con `RECOMMENDATION_UNKNOWN_COMPARISON_CONCLUSIVE`.

### Validacion posterior ejecutada

- `python -m py_compile tools/auc_001_analytical_product_contract.py` -> PASS
- `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_comparison_governance_tests.ps1` -> PASS
- `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_analytical_product_contract_tests.ps1` -> PASS, 14 checks
- `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_canonical_projection_source_tests.ps1` -> PASS, 4 checks
- `powershell -NoProfile -ExecutionPolicy Bypass -File tests/evals/auc_001_operational_acceptance_package_tests.ps1` -> PASS, 4 checks

### Confirmacion de alcance

- No se modifico la especificacion experimental.
- No se generalizo la solucion a AIF Foundation.
- No se modifico Strategic Context.
- No se introdujo evidencia nueva.
- No se modificaron outputs analiticos.
