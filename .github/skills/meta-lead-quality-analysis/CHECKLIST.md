# Execution Checklist — Meta Lead Quality Analysis

## Propósito

Este checklist debe ejecutarse inmediatamente antes de iniciar Presentation Layer.

No sustituye la Skill.

No sustituye el Runbook.

No sustituye los contratos.

Su única responsabilidad es verificar que el contenido canónico está completo y que la ejecución puede materializarse de forma segura.

---

# 1. Execution Context

- [ ] El objetivo del análisis está resuelto.
- [ ] El periodo y fecha de corte están canonicalizados.
- [ ] Si la solicitud contiene `hasta [fecha]` sin fecha inicial, la fecha indicada se trató como fecha de corte.
- [ ] El inicio del periodo se resolvió como primera evidencia disponible dentro de las fuentes autorizadas.
- [ ] No se reutilizó automáticamente un mes natural ni el periodo de una ejecución anterior.
- [ ] La solicitud original, el periodo resuelto y la regla de canonicalización aplicada están registrados.
- [ ] Cualquier divergencia entre la solicitud y el alcance final está justificada explícitamente.
- [ ] El alcance está definido.
- [ ] La audiencia está identificada.
- [ ] El tipo de salida está resuelto.

---

# 2. Contexto oficial

- [ ] Se ha consultado `references.md`.
- [ ] Se ha consultado `docs/context_refs.md`.
- [ ] Se han cargado las definiciones oficiales aplicables.
- [ ] El Data Contract vigente ha sido identificado.
- [ ] El Presentation Contract aplicable ha sido identificado.

---

# 3. Data Provider

- [ ] El Data Provider utilizado corresponde al autorizado por el Data Contract.
- [ ] Se ha consultado `docs/contracts/bigquery-mcp-discover-metadata.contract.md`.
- [ ] `discover_metadata` se ejecuto con selector canonico antes de adquirir evidencia.
- [ ] No se ejecutaron reintentos exploratorios de selector.
- [ ] No se usaron selectores con prefijo de proyecto, valores legacy plurales de `scope_request` ni nombres logicos inferidos como selector de discovery.
- [ ] El resultado de Fase 05 esta registrado como `PASS`, `PASS WITH OBSERVATION` o `FAIL`.
- [ ] `ERR_AUTH_REQUIRED`, `ERR_SELECTOR_INVALID`, `ERR_SCOPE_TOO_BROAD` y `ERR_RESOURCE_NOT_ALLOWLISTED` se interpretaron segun el contrato canonico.
- [ ] La validacion alternativa con `query_read_only`, si existio, se uso solo ante un codigo funcional explicito publicado por el servidor; actualmente no hay codigo oficial observado que active esa ruta.
- [ ] Todas las tablas consultadas pertenecen al Data Contract.
- [ ] Todas las fuentes consultadas han podido verificarse.
- [ ] No se ha utilizado ninguna fuente fuera del alcance autorizado.
- [ ] Las consultas BigQuery MCP no usan `AS rows` como alias.
- [ ] Las consultas BigQuery MCP no reutilizan nombres de CTE como aliases de columna.
- [ ] Las consultas BigQuery MCP no usan joins implicitos con coma.
- [ ] Cada `query_read_only.execution_context` contiene exactamente `project_id`, `dataset_id` y `max_bytes_billed`.
- [ ] No se incluyen campos descriptivos o no soportados dentro de `execution_context`.
- [ ] El `dataset_id` enviado en `execution_context` corresponde al alcance principal de cada consulta.
- [ ] Cualquier `ERR_DRY_RUN_FAILED` se ha tratado como evidencia no utilizable hasta revisar sintaxis, tipos, aliases y ambiguedades.
---

# 4. Evidence Set

- [ ] Existe un Evidence Set explícito.
- [ ] Toda la evidencia mantiene trazabilidad.
- [ ] Las fuentes están autorizadas.
- [ ] Los UNKNOWNs están registrados.
- [ ] Las limitaciones materiales están documentadas.

---

## 4.1 AUC-001-PCI-001 Canonical Cost-Quality Model

- [ ] Si la ejecucion pertenece a `AUC-001-PCI-001`, el modelo usado esta identificado como `auc_001_canonical_cost_quality_model`.
- [ ] La adquisicion lead-side y spend-side se ha mantenido separada antes de la construccion del Evidence Set.
- [ ] `marts.fct_lead_enriched` se usa como fuente lead canonica y `intermediate.int_faro_lead_scoring` solo como validacion/fallback controlado por decision explicita.
- [ ] `ad_id_norm` se calcula removiendo solo el prefijo inicial `ag:` en lead-side.
- [ ] `ad_name` no se ha usado como clave de join, ranking o fallback.
- [ ] `matched`, `lead_only`, `spend_only` y `UNKNOWN` permanecen visibles.
- [ ] `lead_only` no se interpreta como captacion gratuita.
- [ ] `spend_only` no se interpreta como anuncio con cero leads reales.
- [ ] Las metricas economicas declaran universo, senal y coverage; no se publica `CPQL` ambiguo.
- [ ] Denominadores cero producen `NULL`, nunca 0.
- [ ] Los umbrales de ranking estan registrados en `thresholds_config`.
- [ ] No se han usado outputs historicos, incluido `outputs/auc-001/2026-06-30/`, como expected values.

---

# 5. Knowledge Set

- [ ] Existe un Knowledge Set estabilizado.
- [ ] Se ha aplicado `.github/skills/meta-lead-quality-analysis/ANALYTICAL_PROFILE.md` como guia de preguntas y criterios de calidad analitica.
- [ ] Se ha aplicado `.github/skills/meta-lead-quality-analysis/knowledge-construction-profile.md` como guia interna solo durante Knowledge Generation.
- [ ] Existe un Analytical Investigation Record interno previo al Knowledge Set.
- [ ] Los findings intermedios estan trazados al Evidence Set.
- [ ] Cada finding intermedio declara observacion, soporte, importancia e incertidumbre.
- [ ] Se han aplicado operaciones analiticas relevantes segun la evidencia disponible: segmentacion, comparacion, ranking multicriterio, temporalidad, relaciones, combinaciones, cobertura, robustez, trade-offs o contraste de explicaciones alternativas.
- [ ] Las observaciones sin materialidad, robustez o utilidad para decision fueron descartadas o marcadas como limitadas.
- [ ] El conocimiento deriva de la evidencia y de la consolidacion de findings intermedios.
- [ ] No se limita a repetir metricas, rankings o tablas.
- [ ] Distingue insights, hipotesis observacionales, conclusiones, prioridades, riesgos e incertidumbres.
- [ ] Los riesgos estan identificados.
- [ ] Las incertidumbres permanecen explicitas.
- [ ] Existe una Analytical Narrative / Strategic Interpretation estabilizada antes de Recommendation Generation.
- [ ] La Analytical Narrative conecta varios Knowledge items y no se limita a repetir insights.
- [ ] La Analytical Narrative identifica fenomeno principal, trade-off, riesgo o limitacion dominante e implicacion estrategica.
- [ ] La Analytical Narrative diferencia hallazgos estructurales de hallazgos secundarios.
- [ ] La Analytical Narrative declara una idea central memorable para el lector.
- [ ] La Analytical Narrative puede rastrearse completamente al Knowledge Set estabilizado.
- [ ] La Analytical Narrative no introduce evidencia nueva, Knowledge nuevo ni recomendaciones.

---

# 6. Recommendation Set

- [ ] Existe un Recommendation Set estabilizado.
- [ ] Todas las recomendaciones derivan del Knowledge Set.
- [ ] Las prioridades están definidas.
- [ ] No existen recomendaciones sin justificación.

---

# 7. Canonical Projection Source

- [ ] Existe Coverage Matrix conforme a SPEC-014 cuando el alcance requiere producto analítico completo.
- [ ] Existe Common Product Core conforme a SPEC-014 antes de Presentation.
- [ ] Existe Canonical Projection Source conforme a SPEC-015 antes de cualquier informe.
- [ ] El Canonical Projection Source deriva del núcleo canónico, Knowledge y Recommendation Sets aprobados.
- [ ] Analytical report y executive report, si ambos existen, derivan del mismo Canonical Projection Source.
- [ ] Ninguna proyección deriva de otra proyección.
- [ ] Las variaciones entre analytical y executive son de selección, densidad, orden, énfasis, formato o audiencia, no de contenido semántico nuevo.
- [ ] Limitaciones, `UNKNOWN`, `partial`, `not_available`, coverage states y prioridades permanecen presentes y equivalentes.
- [ ] Presentation no introduce nueva evidencia, nuevo Knowledge, nuevas recomendaciones ni valoración comparativa externa.

---

# 8. Presentation

- [ ] Los cuatro artefactos canónicos existen antes de Presentation Layer.
- [ ] Puede demostrarse que Evidence quedó estabilizada antes de Presentation Layer.
- [ ] Puede demostrarse que Knowledge deriva exclusivamente de Evidence.
- [ ] Puede demostrarse que Recommendations derivan exclusivamente de Knowledge y de la priorizacion ya contenida en el Knowledge Set, sin usar la Analytical Narrative como fuente de recomendaciones nuevas.
- [ ] Evidence, Knowledge y Recommendations no aparecen por primera vez dentro del informe final.
- [ ] Presentation Layer consume esos estados cerrados y no los reconstruye.
- [ ] Las limitaciones, UNKNOWNs y coverage states fueron preservados antes de representar.
- [ ] La Presentation Projection está resuelta.
- [ ] El Communication Context está resuelto.
- [ ] La Presentation Policy está identificada, cuando corresponda.
- [ ] Presentation Layer no ha reconstruido conocimiento ni ha creado una Analytical Narrative nueva.
- [ ] Presentation Layer no ha generado recomendaciones nuevas.

---

# 9. Execution Package y validación física

- [ ] Si se persiste paquete físico, existe preflight MCP obligatorio antes de adquirir evidencia.
- [ ] Si se persiste paquete físico, existe Evidence Acquisition Record completo con SQL, `execution_context`, datasets, tablas, periodo, filtros, granularidad, dry run, control de coste, resultado o error, `request_id`, `trace_reference`, bytes cuando estén disponibles y estado de uso como evidencia.
- [ ] Las llamadas MCP rechazadas, descartadas o diagnósticas se registran y no se usan como Evidence.
- [ ] La estrategia MCP usa consultas independientes por tabla autorizada y reconciliación local controlada hasta que el gap multi-tabla sea resuelto formalmente.
- [ ] El grano adquirido permite cumplir SPEC-014; si no lo permite, la ejecución queda bloqueada o declara insuficiencia antes de Presentation.
- [ ] Existen manifest, artifact fingerprints y physical traceability reproducibles.
- [ ] El namespace no contiene `__pycache__`, `.pyc` ni residuos no contractuales.
- [ ] El handoff declara comandos ejecutados, resultados, limitaciones y desviaciones.
- [ ] `READY_FOR_REVALIDATION` no se declara como aceptación final sin gate QA físico.

---

# 10. Validación final

- [ ] La equivalencia semántica se mantiene.
- [ ] Los coverage states permanecen visibles.
- [ ] Las limitaciones materiales permanecen visibles.
- [ ] Las prioridades no han cambiado.
- [ ] La representación puede reconstruirse desde los artefactos canónicos.
- [ ] No se han utilizado informes anteriores como fuente.

---

# Resultado

La ejecución solo podrá darse por completada cuando todos los puntos anteriores estén verificados.

Si cualquier comprobación falla, la ejecución deberá detenerse antes de generar la representación final.
