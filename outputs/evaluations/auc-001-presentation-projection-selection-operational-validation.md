# Validacion operativa de Presentation Projection Selection - AUC-001

## Estado

| Campo | Valor |
| --- | --- |
| Validation ID | VCA-AUC-001-EVAL-PPS-001 |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Capability under validation | Presentation Projection Selection |
| Architecture reference | VCA-AUC-001-ARCH-002 |
| Specification reference | SPEC-010 |
| Execution date | 2026-07-13 |
| Status | Completed |
| Selected presentation mode | Executive |
| Selected presentation projection | Executive Report |
| Output artifact | This file |

---

## 1. Reconstruccion del estado actual del repositorio

La ejecucion se reconstruyo exclusivamente desde artefactos canonicos vigentes del repositorio.

### Artefactos canonicos consultados

| Artifact | Role in execution |
| --- | --- |
| `docs/context_refs.md` | Registry canonico de contexto, decisiones, runtime sources y reusable knowledge |
| `specs/spec-010-presentation-projection-selection.md` | Specification vigente de seleccion de proyeccion de presentacion |
| `docs/architecture/adr-001-execution-scope-canonicalization.md` | Regla canonica de Execution Scope Canonicalization |
| `docs/architecture/adr-002-presentation-projection-boundary.md` | Decision arquitectonica sobre boundary de proyecciones de presentacion |
| `docs/contracts/context.contract.md` | Context Contract base alineado con canonicalizacion y presentation projection readiness |
| `docs/contracts/presentation.contract.md` | Presentation Contract base alineado con Selected Presentation Projection |
| `docs/handoffs/auc-001-context-definition.md` | Context Definition canonica para AUC-001 |
| `docs/handoffs/auc-001-presentation-contract.md` | Presentation Contract canonico especifico de AUC-001 |
| `docs/handoffs/auc-001-evidence-contract.md` | Evidence Set aprobado para AUC-001 |
| `docs/handoffs/auc-001-knowledge-contract.md` | Knowledge Set aprobado para AUC-001 |
| `docs/handoffs/auc-001-recommendation-contract.md` | Recommendation Set aprobado para AUC-001 |
| `docs/handoffs/auc-001-executive-report.md` | Selected Presentation Projection canonica ya alineada para AUC-001 |
| `docs/evaluations/auc-001-documentary-alignment-decision.md` | Decision de alineacion documental autorizada |
| `docs/evaluations/auc-001-base-contracts-alignment-record.md` | Registro de alineacion T-044 |
| `docs/evaluations/auc-001-presentation-artifacts-alignment-record.md` | Registro de alineacion T-045 |
| `docs/evaluations/auc-001-context-references-alignment-record.md` | Registro de alineacion T-046 |
| `docs/evaluations/auc-001-presentation-projection-readiness-evaluation.md` | Readiness posterior a T-044/T-045/T-046 |

### Estado canonico reconstruido

| Dimension | Estado observado |
| --- | --- |
| Development status | Development Authorized segun `docs/context_refs.md` |
| Relevant capability | Presentation Projection Selection definida por SPEC-010 |
| Architectural rule | La proyeccion se selecciona desde Execution Context canonicalizado; Presentation Layer no decide ad hoc |
| Presentation boundary | Analytical Report y Executive Report son proyecciones hermanas del mismo contenido aprobado |
| Current AUC-001 output request | Informe ejecutivo trazable |
| Current AUC-001 presentation mode | Executive |
| Current AUC-001 selected projection | Executive Report |
| Current approved content base | Evidence Set, Knowledge Set y Recommendation Set aprobados para AUC-001 |
| Readiness | PASS WITH OBSERVATIONS en `auc-001-presentation-projection-readiness-evaluation.md` |

---

## 2. Execution Scope Canonicalization

### Current human request

Validar experimentalmente la capacidad definida por `VCA-AUC-001-ARCH-002` y `SPEC-010`, resolver el Execution Context con Execution Scope Canonicalization, determinar la proyeccion correspondiente y generar solo despues el artefacto correspondiente.

### Canonicalized Execution Context

| Field | Canonicalized value | Source / rule |
| --- | --- | --- |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis | Context Definition / context registry |
| Execution purpose | Validacion operativa de Presentation Projection Selection | Current user request |
| Execution type | Presentation projection selection and materialization validation | SPEC-010 / ARCH-002 |
| Scope status | Sufficiently defined | ARCH-001 canonicalization rule |
| Time period | 2026-06-01 to 2026-06-30 | AUC-001 Context Definition |
| Operational scope | Meta Lead Ads campaigns, ad sets and ad references with spend or leads in scope | AUC-001 Context Definition |
| Output request | Informe ejecutivo trazable | AUC-001 Context Definition and AUC-001 Presentation Contract |
| Audience | Analista de negocio, direccion, responsable de Marketing, especialistas de Meta Ads y equipo Comercial | AUC-001 Presentation Contract |
| Decision type | Executive/business decision support over approved analytical content | AUC-001 Presentation Contract / SPEC-010 |
| Evidence policy | No new evidence generation | Current user request and contracts |
| Reasoning policy | No new reasoning beyond approved Knowledge Set | Current user request and contracts |
| Recommendation policy | No new recommendations and no priority modification | Current user request and Recommendation Contract boundary |
| Presentation Layer role | Materialize selected projection only | SPEC-010 / ARCH-002 |
| Ambiguity status | No material ambiguity detected | ARCH-001 rule: inherited canonical context resolves missing parameters |

### Canonicalization decision

No material ambiguity was detected. The current request does not redefine audience, period, evidence basis or recommendation policy. Under ARCH-001, those parameters are inherited from the current canonical AUC-001 context and contracts. Therefore execution can continue without asking for clarification.

---

## 3. Presentation Projection Selection

| Selection field | Value |
| --- | --- |
| Presentation Mode | Executive |
| Selected Presentation Projection | Executive Report |
| Projection source | Canonicalized Execution Context, Output Request and AUC-001 Presentation Contract |
| Relationship to other projections | Sibling projection from the same approved content; not derived from an analytical report |
| Boundary status | No new evidence, no new interpretation, no new recommendations and no priority rewrite |

### Why this projection was selected

The canonicalized Execution Context contains an `output_request` of `Informe ejecutivo trazable`, an audience that includes `direccion` and business stakeholders, and a decision-support purpose. SPEC-010 states that projection selection is derived from the canonicalized Execution Context using audience, purpose and decision type. ARCH-002 states that Presentation Layer only materializes the selected projection and must not choose ad hoc.

Therefore, the applicable projection is `Executive Report` under `Presentation Mode = Executive`.

---

# Artefacto generado: Executive Report Projection

This section materializes the selected projection using only approved contract content from the canonical AUC-001 Evidence Set, Knowledge Set, Recommendation Set and Presentation Contract. It does not introduce new data, new reasoning, new priorities or new recommendations.

## Resumen ejecutivo

Durante junio de 2026, el caso AUC-001 analiza la calidad de leads procedentes de Meta Lead Ads usando el modelo preparado `ad_quality_spend_model`, con grano primario `ad_id_norm` y definicion de `Qualified Lead` como Lead Tier A o B.

El modelo preparado contiene 15 referencias de anuncio, 772 leads, 226 qualified leads, inversion total de 496.5600089999987 y una tasa global de leads cualificados de 0.2927461139896373. El spend per qualified lead global es 2.197168181415923.

La cobertura corregida distingue tres grupos materiales:

| Coverage group | Ad refs | Leads | Qualified leads | Spend |
| --- | ---: | ---: | ---: | ---: |
| matched | 8 | 680 | 191 | 494.3600089999987 |
| lead_only | 5 | 92 | 35 | 0.0 |
| spend_only | 2 | 0 | 0 | 2.200000000000001 |

La lectura aprobada es que el modelo permite razonar sobre calidad de leads y spend comercial a nivel de anuncio dentro de la cobertura corregida. La interpretacion a nivel campaign/adset queda condicionada por problemas de cobertura y por la imposibilidad de reconstruir de forma fiable spend por campaign/adset desde las claves disponibles.

## Objetivo y alcance

| Campo | Valor aprobado |
| --- | --- |
| Periodo | 2026-06-01 to 2026-06-30 |
| Alcance operativo | Todas las campanas, conjuntos y creatividades de Meta Lead Ads con spend o leads en el periodo |
| Filtros | `campaign_signal = COMMERCIAL`; exclusion de test records, duplicados y leads sin id valido; sin filtro geografico adicional |
| Definicion de calidad | Qualified Lead FARO = Tier A/B |
| Audiencia | Analista de negocio, direccion, responsable de Marketing, especialistas de Meta Ads y equipo Comercial |
| Output request | Informe ejecutivo trazable |
| Presentation Mode | Executive |
| Selected Presentation Projection | Executive Report |

## Datos y cobertura utilizados

| Source artifact | Approved role |
| --- | --- |
| Evidence Contract | Contiene evidencia numerica aprobada para AUC-001 |
| Knowledge Contract | Contiene interpretaciones, hipotesis y conclusiones aprobadas |
| Recommendation Contract | Contiene recomendaciones priorizadas aprobadas |
| Presentation Contract | Define audiencia, forma de salida y boundaries de presentacion |

### Cobertura aprobada

| Evidence ID | Observation |
| --- | --- |
| EVD-001 | La cobertura se divide en matched, lead_only y spend_only; no debe colapsarse sin preservar coverage status |
| EVD-002 | El modelo preparado contiene 15 ad refs, 772 leads, 226 qualified leads y spend 496.5600089999987 |
| EVD-003 | La mayor referencia matched por volumen es `120245828603090721` / `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`, con 519 leads, 152 qualified leads y spend 374.79000799999875 |
| EVD-004 | La agregacion campaign/adset es coverage-qualified y contiene UNKNOWN materiales en spend-side |

## Principales resultados

1. La evidencia aprobada muestra que la mayor parte del volumen y del spend se concentra en el grupo `matched`.
2. Existen 5 referencias `lead_only` con 92 leads y 35 qualified leads sin spend asociado en el modelo corregido.
3. Existen 2 referencias `spend_only` con 2.200000000000001 de spend sin leads asociados.
4. La referencia matched de mayor volumen aporta 519 leads, 152 qualified leads y 374.79000799999875 de spend, pero no permite atribuir causalmente calidad al asset creativo.
5. Las lecturas por campaign/adset deben mantenerse como coverage-qualified y no deben usarse para recomendaciones de eficiencia de spend sin validacion adicional.

## Analisis por nivel disponible

### Nivel anuncio / ad reference

La lectura aprobada considera el nivel `ad_id_norm` como el grano primario del modelo preparado. En este nivel se puede comparar calidad de leads y spend dentro de la cobertura corregida, siempre conservando `coverage_status`.

La referencia matched de mayor volumen es `120245828603090721` / `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`, con 519 leads, 152 qualified leads y 374.79000799999875 de spend. Esta observacion describe volumen y calidad observada, no causalidad creativa.

### Nivel campaign / adset

El nivel campaign/adset existe solo como lectura condicionada por cobertura. La evidencia aprobada conserva UNKNOWN materiales en spend-side y no valida una relacion completa entre spend y calidad a ese nivel.

Por ello, las decisiones de redistribucion por campaign/adset requieren validacion previa de mapping de spend y no deben derivarse directamente de ratios incompletos.

### Nivel creative / asset

No hay metadata completa de assets creativos ni variables de impresiones, clicks o CTR. La evidencia permite hablar de referencias de anuncio y nombres observados, pero no permite concluir rendimiento causal de creatividades, formatos o mensajes.

## Conclusiones aprobadas

| Conclusion ID | Conclusion |
| --- | --- |
| CON-001 | AUC-001 puede producir un reporte ejecutivo trazable sobre calidad de leads y spend comercial a nivel de anuncio dentro del modelo corregido. |
| CON-002 | La lectura campaign/adset debe mantenerse coverage-qualified hasta resolver problemas de spend-side mapping y cobertura. |

## Recomendaciones priorizadas

| Priority | Recommendation ID | Recommendation |
| --- | --- | --- |
| P1 | REC-001 | Usar el nivel matched ad reference como base primaria para decisiones operativas inmediatas. |
| P1 | REC-002 | Tratar RTG lead-only como segmento separado hasta resolver su cobertura de spend. |
| P2 | REC-003 | Validar y documentar el mapping de spend por campaign/adset antes de emitir recomendaciones de redistribucion a esos niveles. |
| P2 | REC-004 | Mantener las recomendaciones de creative performance a nivel ad reference y evitar inferencias causales sobre assets. |
| P2 | REC-005 | Arrastrar explicitamente la incertidumbre por duplicados y test-record flags en cualquier entrega ejecutiva. |
| P3 | REC-006 | No introducir recomendaciones basadas en impresiones, clicks, CTR o ratios de funnel no disponibles. |

## Limitaciones y UNKNOWN

| Limitation / UNKNOWN | Impact |
| --- | --- |
| Duplicate/test-record flags not fully mapped | La calidad puede estar afectada por registros excluidos o no verificables |
| Spend-only campaign/adset UNKNOWN | Limita la lectura de eficiencia por campaign/adset |
| Impressions, clicks and CTR unavailable | Impide analisis de funnel superior y performance media |
| Creative asset metadata unavailable | Impide concluir causalidad por pieza creativa o formato |
| `campaign_signal` spend-side only | Limita consistencia entre lead-side y spend-side |
| Lead-only spend zero by alignment | No equivale a spend real cero; es ausencia de match en el modelo |
| Spend-only ratios UNKNOWN | No deben usarse para calidad de leads |
| Campaign/adset values include lead-side metadata constraints | Lectura agregada debe mantenerse coverage-qualified |

## Trazabilidad

| Output section | Approved source |
| --- | --- |
| Resumen ejecutivo | `docs/handoffs/auc-001-executive-report.md`; Evidence Contract; Knowledge Contract |
| Objetivo y alcance | AUC-001 Context Definition; AUC-001 Presentation Contract |
| Datos y cobertura | AUC-001 Evidence Contract |
| Principales resultados | AUC-001 Evidence Contract and Knowledge Contract |
| Analisis por nivel disponible | AUC-001 Knowledge Contract; Presentation Contract boundary |
| Conclusiones aprobadas | AUC-001 Knowledge Contract |
| Recomendaciones priorizadas | AUC-001 Recommendation Contract |
| Limitaciones y UNKNOWN | AUC-001 Evidence/Knowledge/Presentation Contracts |
| Projection selection | SPEC-010; ARCH-001; ARCH-002; Context Contract; Presentation Contract |

---

## Boundary compliance

| Constraint | Compliance |
| --- | --- |
| No new evidence | Compliant. No MCP, BigQuery or CLI data queries were executed for analytical evidence. |
| No new reasoning | Compliant. Interpretations are limited to approved Knowledge Contract / Executive Report content. |
| No new recommendations | Compliant. Recommendations are copied from approved Recommendation Contract content. |
| No priority changes | Compliant. Priorities P1/P2/P3 are preserved. |
| Projection not ad hoc | Compliant. Selection is derived from canonicalized Execution Context. |
| Sibling projection rule | Compliant. Executive Report is treated as sibling projection, not derived from analytical projection. |

---

## Execution record

### Artefactos del repositorio consultados

- `docs/context_refs.md`
- `specs/spec-010-presentation-projection-selection.md`
- `docs/architecture/adr-001-execution-scope-canonicalization.md`
- `docs/architecture/adr-002-presentation-projection-boundary.md`
- `docs/contracts/context.contract.md`
- `docs/contracts/presentation.contract.md`
- `docs/handoffs/auc-001-context-definition.md`
- `docs/handoffs/auc-001-presentation-contract.md`
- `docs/handoffs/auc-001-evidence-contract.md`
- `docs/handoffs/auc-001-knowledge-contract.md`
- `docs/handoffs/auc-001-recommendation-contract.md`
- `docs/handoffs/auc-001-executive-report.md`
- `docs/evaluations/auc-001-documentary-alignment-decision.md`
- `docs/evaluations/auc-001-base-contracts-alignment-record.md`
- `docs/evaluations/auc-001-presentation-artifacts-alignment-record.md`
- `docs/evaluations/auc-001-context-references-alignment-record.md`
- `docs/evaluations/auc-001-presentation-projection-readiness-evaluation.md`

### Herramientas utilizadas

- Repository file reads through shell commands.
- Repository file write to create this output artifact.

### Consultas o acciones ejecutadas mediante MCP

None. The current execution explicitly prohibited new evidence generation. BigQuery MCP was therefore not used.

### Datos que no pudieron obtenerse

No additional data was requested or obtained. Missing analytical data remains the same as in the approved contracts: impressions, clicks, CTR, full creative asset metadata, fully resolved duplicate/test-record flags and reliable campaign/adset spend mapping.

### Decisiones tomadas por limitaciones de cobertura

- Campaign/adset analysis is preserved as coverage-qualified.
- Creative analysis is limited to ad reference naming and cannot be interpreted as causal creative performance.
- Lead-only and spend-only records are kept separate and not collapsed into matched performance ratios.
- No recommendation was generated from impressions, clicks, CTR or unavailable funnel metrics.

### Confirmacion sobre uso de informes previos

The previously generated executive report was consulted only as a canonical, aligned presentation artifact registered in the current repository state. It was not used to create new conclusions. The content in this validation is constrained to approved Evidence, Knowledge, Recommendation and Presentation contracts.

### Observaciones para evaluacion posterior

- The readiness evaluation records residual generic wording around `Output Artifact` in legacy/generic contract text. No correction was implemented in this execution.
- This validation creates an experimental output artifact but does not update Tasks, contracts, handoffs, specifications or evaluations.
