# AUC-001-EXP-COMP-001 - Especificacion Experimental Final

## Metadata

```yaml
id: AUC-001-EXP-COMP-001
titulo: Clasificacion explicita de comparaciones entre universos estrategicos no equivalentes
tipo: especificacion experimental minima
estado: READY FOR ENTRY GATE REVIEW
alcance: AUC-001 local
decision_previa_aplicada: EXPERIMENT FIRST
solucion_autorizada: hibrida local para AUC-001
fecha: 2026-07-24
agente: Specification Agent
modo: read-only documental
evidencia_nueva: no
```

## Proposito

Definir el contrato experimental minimo para que AUC-001 identifique, clasifique, transporte y presente comparaciones o claims entre universos estrategicos no equivalentes sin convertir contrastes descriptivos utiles en inferencias economicas, causalidades, recomendaciones de optimizacion o jerarquias implicitas.

La especificacion no reabre arquitectura, no modifica Strategic Context, no crea una taxonomia universal y no disena implementacion.

## Hipotesis

Si Analytical Reasoning clasifica explicitamente cada comparacion entre universos estrategicos no equivalentes, y esa clasificacion se preserva hasta Common Product Core (CPC), Canonical Projection Source (CPS), Presentation y QA, entonces las salidas de AUC-001 reduciran inferencias economicas o jerarquias implicitas sin eliminar comparaciones descriptivas utiles.

## Alcance

In-scope:

- AUC-001 exclusivamente.
- Comparaciones, contrastes, rankings o claims entre universos estrategicos equivalentes, no equivalentes o de equivalencia desconocida.
- Clasificacion dentro de Analytical Reasoning.
- Transporte obligatorio de clasificacion hasta CPC y CPS.
- Adaptacion de Presentation segun audiencia analitica o ejecutiva.
- Validacion experimental por QA.

Out-of-scope:

- Modificar Strategic Context.
- Abrir SPEC Foundation.
- Crear taxonomia transversal o universal.
- Disenar runtime, codigo, prompts finales o tareas tecnicas.
- Adquirir evidencia nueva.
- Reinterpretar outputs historicos como evidencia.
- Modificar SPEC-014, SPEC-015 o SPEC-016.

## Dependencias

- AUC-001 Meta Lead Quality Analysis.
- SPEC-014 Analytical Product Contract.
- SPEC-015 Canonical Projection Consolidation.
- SPEC-016 Operational Acceptance Package Contract.
- Presentation Projection Architecture vigente.
- Communication Context Representation Transformation.
- Perfil local de restricciones estrategicas AUC-001.
- Memo arquitectonico aprobado con decision `EXPERIMENT FIRST`.

## Contrato Minimo De Clasificacion

```yaml
comparison_classification:
  comparison_id: string
  source_artifact: analytical_reasoning | knowledge_set | recommendation_set
  provisional_claim_ref:
    type: textual_excerpt | provisional_anchor
    value: string
    status: provisional_until_knowledge_stabilization
  stabilized_claim_refs:
    knowledge_refs: list
    recommendation_refs: list
    reconciliation_status: reconciled | not_applicable | blocked
  compared_universes:
    - universe_id: string
      universe_label: string
      strategic_equivalence: equivalent | non_equivalent | unknown
  comparison_type:
    cardinality: multiple_allowed
    values:
      - descriptive_contrast
      - economic_efficiency_claim
      - strategic_hierarchy_claim
      - causal_or_optimization_claim
  restrictive_type_priority:
    - causal_or_optimization_claim
    - economic_efficiency_claim
    - strategic_hierarchy_claim
    - descriptive_contrast
  governance_status:
    - allowed
    - allowed_with_limitation
    - presentation_restricted
    - blocked
  required_limitation_or_disclaimer_semantics: string | null
  allowed_projection_behavior:
    analytical: preserve_full_context | preserve_with_limitation | suppress_claim
    executive: simplify_with_limitation | downgrade_to_descriptive | suppress_claim
  traceability:
    evidence_refs: list
    knowledge_refs: list
    recommendation_refs: list
  qa_expected_check: string
```

`comparison_type` admite multiples valores. Cuando un claim tenga varios tipos, prevalece el tipo mas restrictivo segun `restrictive_type_priority` para determinar `governance_status`.

`required_limitation_or_disclaimer_semantics` prescribe la semantica obligatoria que debe conservar Presentation. No prescribe wording literal, estructura narrativa ni texto final.

## Reglas Minimas

- Toda comparacion debe tener `comparison_id`.
- Durante Analytical Reasoning puede existir `provisional_claim_ref` textual o provisional.
- Al estabilizar Knowledge, `provisional_claim_ref` debe reconciliarse contra `knowledge_refs`; si no puede reconciliarse y el claim es material, debe bloquearse.
- `recommendation_refs` solo pueden existir despues de Recommendation Set estabilizado.
- Si `strategic_equivalence = non_equivalent`, no puede emitirse jerarquia estrategica sin limitacion explicita.
- Si `strategic_equivalence = unknown` y el claim es economico, jerarquico, causal u orientado a optimizacion, debe degradarse, restringirse o bloquearse salvo justificacion explicita; no puede emitir decision economica concluyente.
- Si el claim implica eficiencia economica entre universos no equivalentes o desconocidos, debe declararse como `allowed_with_limitation` o `presentation_restricted`, salvo normalizacion aprobada.
- Si el claim implica causalidad, optimizacion o reasignacion entre universos no equivalentes sin soporte contractual, debe quedar `blocked`.
- Las comparaciones descriptivas pueden mantenerse si no inducen ranking, causalidad ni recomendacion economica.

## Reglas Por Fase

### Analytical Reasoning

- Detecta comparaciones explicitas e implicitas.
- Clasifica cada comparacion antes de estabilizar Knowledge.
- Distingue contraste descriptivo de claim economico, jerarquico, causal u orientado a optimizacion.
- Usa `provisional_claim_ref` mientras el claim no este reconciliado.
- Marca `unknown` cuando no pueda determinar equivalencia estrategica.

### Knowledge Set

- Reconciliara `provisional_claim_ref` contra `knowledge_refs`.
- Puede conservar comparaciones descriptivas permitidas.
- Debe transportar limitaciones asociadas.
- No puede convertir diferencia observada en superioridad estrategica si la clasificacion lo restringe.

### Recommendation Set

- No puede derivar recomendaciones desde claims `blocked`.
- No puede emitir reasignacion, optimizacion o priorizacion economica concluyente desde claims con equivalencia `unknown`.
- Debe referenciar la clasificacion cuando use conocimiento comparativo.

### Common Product Core (CPC)

- Incluye la clasificacion de comparaciones como contenido canonico.
- Preserva `governance_status`, semantica de limitacion y trazabilidad.
- No suaviza ni elimina restricciones para Presentation.

### Canonical Projection Source (CPS)

- Transporta la clasificacion desde CPC.
- Declara comportamiento permitido por proyeccion.
- Impide divergencia semantica entre analytical y executive.

### Presentation

- Audiencia analitica: puede mostrar comparacion completa con limitacion visible y trazabilidad.
- Audiencia ejecutiva: debe evitar lenguaje de ranking, eficiencia u optimizacion si el claim no esta autorizado.
- Ninguna proyeccion puede convertir `allowed_with_limitation` en claim concluyente.
- Ninguna proyeccion puede presentar un claim `blocked`.

### QA

- Valida presencia, transporte y uso correcto de clasificacion.
- Verifica prioridad restrictiva cuando haya multiples `comparison_type`.
- Verifica reconciliacion de `provisional_claim_ref` al estabilizar Knowledge.
- Confirma que comparaciones descriptivas utiles no desaparecen.
- Confirma que jerarquias o inferencias economicas no autorizadas quedan bloqueadas o degradadas.

## Criterios De Aceptacion

- Todas las comparaciones relevantes tienen clasificacion explicita.
- `comparison_type` multiple se resuelve por tipo mas restrictivo.
- Claims con `strategic_equivalence = unknown` no emiten decision economica concluyente.
- `provisional_claim_ref` queda reconciliado antes de Knowledge estabilizado.
- CPC y CPS preservan clasificacion sin perdida semantica.
- Presentation adapta lenguaje sin alterar contenido canonico.
- QA puede verificar el comportamiento sin evidencia nueva.

## Criterios De Bloqueo

- No se identifican los universos comparados.
- La equivalencia estrategica queda ambigua y el claim requiere decision economica concluyente.
- La clasificacion no llega hasta CPC o CPS.
- `provisional_claim_ref` no puede reconciliarse para un claim material.
- Presentation necesita inventar contexto para adaptar el claim.
- Una recomendacion depende de un claim bloqueado.
- El experimento requiere modificar Strategic Context o abrir SPEC Foundation.

## Evidencia Esperada Para QA

- Muestra controlada de comparaciones clasificadas.
- Matriz `comparison_id -> comparison_type -> governance_status -> CPC -> CPS -> projection`.
- Caso con multiples `comparison_type` resuelto por prioridad restrictiva.
- Caso `strategic_equivalence = unknown` degradado, restringido o bloqueado.
- Registro de reconciliacion `provisional_claim_ref -> knowledge_refs`.
- Ejemplo analitico donde una comparacion descriptiva se conserva.
- Ejemplo ejecutivo donde una jerarquia implicita se degrada o bloquea.
- Verificacion de que no se adquirio evidencia nueva ni se modificaron Strategic Context, SPEC-014, SPEC-015 o SPEC-016.

## Riesgos Y No-Goals

Riesgos:

- Clasificacion excesiva que elimine contraste util.
- Clasificacion debil que permita rankings implicitos.
- Uso de `unknown` como via para emitir claims concluyentes.
- Confundir semantica obligatoria de limitacion con wording literal.
- Crear una taxonomia transversal de facto.

No-goals:

- Resolver comparabilidad estrategica universal.
- Definir normalizacion economica universal.
- Autorizar recomendaciones de inversion.
- Cambiar contratos existentes.
- Crear implementacion o plan tecnico.
- Reabrir decisiones arquitectonicas aprobadas.

## Readiness Para Entry Gate

Estado: `READY FOR ENTRY GATE REVIEW`.

La especificacion incorpora los hallazgos del Reviewer Agent, mantiene alcance local AUC-001, conserva verificabilidad QA y no introduce implementacion, arquitectura nueva, Strategic Context ni SPEC Foundation.

## Trazabilidad Cruzada

| Artefacto | Ruta |
|---|---|
| Memo arquitectonico aprobado | `docs/decisions/auc-001/auc-001-exp-comp-001-architectural-memo.md` |
| Revision Reviewer | `docs/evaluations/auc-001/validations/auc-001-exp-comp-001-reviewer-review.md` |
| Registro de resolucion | `docs/evaluations/auc-001/validations/auc-001-exp-comp-001-five-change-resolution-record.md` |