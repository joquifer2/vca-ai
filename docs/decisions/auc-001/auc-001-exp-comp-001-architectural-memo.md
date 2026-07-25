# AUC-001-EXP-COMP-001 - Memo Arquitectonico

## Metadata

| Campo | Valor |
|---|---|
| Artifact ID | AUC-001-EXP-COMP-001-ARCH-MEMO |
| Iteracion | AUC-001-EXP-COMP-001 |
| Tipo | Memo arquitectonico aprobado |
| Estado | Approved for experimental specification |
| Fecha | 2026-07-24 |
| Agente origen | Architect Agent |
| Alcance | AUC-001 local |
| Decision | EXPERIMENT FIRST |

## Proposito

Documentar la clasificacion arquitectonica aprobada para la gobernanza de comparaciones entre universos estrategicos no equivalentes en AUC-001.

Este memo no abre una nueva SPEC Foundation, no modifica Strategic Context, no implementa codigo y no reabre la iteracion Strategic Context ya aceptada.

## Resumen Ejecutivo

El problema existe, pero no es un fallo de carga de contexto ni de trazabilidad. El CCD, el Strategic Context Profile, `ccd_constraint_ref` y `strategic_context_constraints` ya llegan hasta Common Product Core, Canonical Projection Source, proyecciones e informes.

El defecto arquitectonico residual es que una comparacion descriptiva entre campanas de universos FARO distintos puede ser numericamente correcta y aun asi inducir una lectura inferencial o economica no autorizada. La ejecucion aceptada evita declarar un ganador economico universal, pero el framework local todavia no gobierna con suficiente granularidad la comparacion como unidad semantica.

Decision aprobada: solucion hibrida minima, validada primero en `vca-ai`.

Estado recomendado: `EXPERIMENT FIRST`.

## Evidencia Revisada

La revision arquitectonica considero como fuentes principales:

- `knowledge/client/ccd.md`
- `analytical_use_cases/auc-001/faro-strategic-context-profile.json`
- `.github/skills/meta-lead-quality-analysis/SKILL.md`
- `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`
- `.github/skills/meta-lead-quality-analysis/references.md`
- `analytical_use_cases/auc-001/analytical-contract.md`
- `specs/spec-014-auc-001-analytical-product-contract.md`
- `specs/spec-015-auc-001-canonical-projection-consolidation.md`
- `specs/spec-016-auc-001-operational-acceptance-package-contract.md`
- `outputs/auc-001/exec-2026-07-24-strategic-context-full-rerun-retry-2026-06-30/product-core/common-product-core.json`
- `outputs/auc-001/exec-2026-07-24-strategic-context-full-rerun-retry-2026-06-30/product-core/canonical-projection-source.json`
- `outputs/auc-001/exec-2026-07-24-strategic-context-full-rerun-retry-2026-06-30/reports/analytical-report.md`
- `outputs/auc-001/exec-2026-07-24-strategic-context-full-rerun-retry-2026-06-30/reports/executive-report.md`
- `outputs/auc-001/exec-2026-07-24-strategic-context-full-rerun-retry-2026-06-30/validations/exit-gate-strategic-context-validation.json`

## Definicion Precisa Del Problema

Hay cuatro niveles que no deben confundirse:

| Nivel | Clasificacion |
|---|---|
| Validez de datos | Valida. Las metricas de leads, A/B, Tier A, spend y `commercial_matched` estan trazadas. |
| Comparabilidad estrategica | Condicionada. `COMMERCIAL`, `ACTIVATION` y `ATTENTION` no son universos equivalentes. |
| Validez inferencial | Limitada. Puede describirse diferencia de volumen/calidad, pero no inferir superioridad economica cross-layer. |
| Seguridad comunicativa | Incompleta. La proximidad narrativa entre cifras puede inducir lectura de ranking aunque exista declaracion de no equivalencia. |

La unidad problematica no es la metrica aislada, sino la comparacion o claim que usa metricas de entidades con universos estrategicos distintos.

## Clasificacion Arquitectonica

No es principalmente adquisicion, modelado de evidencia ni conocimiento base.

Es una combinacion de:

- Strategic Context, que ya contiene la regla semantica.
- Analytical Reasoning, que debe clasificar el tipo de comparacion y su alcance inferencial.
- Common Product Core y Canonical Projection Source, que deben transportar esa clasificacion de forma consumible.
- Projection y Presentation, que deben presentar la comparacion sin transformarla en ranking implicito.

Clasificacion: extension local de capacidades existentes, con potencial reusable todavia no validado.

## Relacion Con Capacidades Existentes

Strategic Context ya cubre parte del problema: el perfil FARO prohibe `universal_kpi_ranking_across_layers` y exige `ccd_constraint_ref`.

SPEC-014 cubre nomenclatura economica y universos explicitos.

SPEC-015 cubre Canonical Projection Source, proyecciones hermanas y equivalencia semantica.

SPEC-010 y SPEC-011 cubren seleccion de proyeccion y transformacion comunicativa.

Lo que no esta suficientemente cubierto es una gobernanza explicita de comparabilidad por claim/comparison: origen, destino, proposito, tipo, equivalencia, KPI family, inferencia permitida y riesgo de interpretacion.

## Opciones Consideradas

| Opcion | Evaluacion |
|---|---|
| A - Regla local AUC-001 | Minima y rapida; recomendada como experimento local. |
| B - Extension de Strategic Context | Util solo para declarar equivalencia entre universos; no debe absorber reglas de Presentation. |
| C - Extension de Presentation Projection | Util como guardrail de materializacion, pero llega tarde si el claim ya nacio ambiguo. |
| D - Nueva capacidad de gobernanza del razonamiento | Conceptualmente limpia pero prematura para AIF Foundation. |
| E - Solucion hibrida | Recomendada: separa responsabilidades sin crear una capability nueva. |

## Decision Recomendada

Aplicar la Opcion E primero como experimento local en `vca-ai`.

No abrir una nueva SPEC Foundation. No reabrir Strategic Context. No corregir solo wording de informes.

La siguiente iteracion debe probar una regla local de gobernanza de comparaciones:

- Strategic Context declara universos y equivalencias.
- Analytical Reasoning clasifica cada comparacion.
- Common Product Core y Canonical Projection Source transportan esa clasificacion.
- Projection adapta visibilidad segun audiencia.
- Presentation impide ranking implicito o inferencia economica no autorizada.

## Frontera De Responsabilidad

| Capa | Responsabilidad |
|---|---|
| Strategic Context | Define universos, funciones estrategicas, KPIs permitidos/prohibidos y no equivalencias. |
| Analytical Reasoning | Decide si una comparacion es descriptiva, normalizada, benchmark, ranking, inferencial o prohibida. |
| Knowledge | Conserva claims con tipo de comparacion y limite inferencial. |
| Common Product Core | Estabiliza metricas, claims, limitaciones y estados de cobertura. |
| Projection | Decide cuanta visibilidad necesita la restriccion segun informe analitico o ejecutivo. |
| Presentation | Comunica sin convertir comparacion descriptiva en jerarquia economica. |

## Riesgos De Sobrediseno

No formalizar todavia:

- taxonomia universal cerrada;
- nueva SPEC Foundation;
- contrato generico para todos los dominios;
- reglas rigidas que prohiban toda comparacion cross-layer;
- duplicacion normativa del CCD dentro de varios artefactos.

## Estado Recomendado

`EXPERIMENT FIRST`

Hay suficiente evidencia para actuar localmente, pero no suficiente validacion para elevarlo aun a AIF Foundation.

## Siguiente Actuacion Recomendada

Persistir y someter a Entry Gate una especificacion experimental local AUC-001 para gobernanza de comparaciones.

## Trazabilidad Cruzada

| Artefacto | Ruta |
|---|---|
| Especificacion experimental final | `docs/evaluations/auc-001/experiments/auc-001-exp-comp-001-final-experimental-specification.md` |
| Revision Reviewer | `docs/evaluations/auc-001/validations/auc-001-exp-comp-001-reviewer-review.md` |
| Registro de resolucion | `docs/evaluations/auc-001/validations/auc-001-exp-comp-001-five-change-resolution-record.md` |

## Definition Of Done Documental

- El memo registra la decision `EXPERIMENT FIRST`.
- El memo preserva el alcance local AUC-001.
- El memo no abre SPEC Foundation ni modifica Strategic Context.
- El memo queda enlazado desde los indices AUC-001 para reevaluacion de Entry Gate.