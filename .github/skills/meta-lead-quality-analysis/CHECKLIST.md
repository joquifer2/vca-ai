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
- [ ] Todas las tablas consultadas pertenecen al Data Contract.
- [ ] Todas las fuentes consultadas han podido verificarse.
- [ ] No se ha utilizado ninguna fuente fuera del alcance autorizado.
- [ ] Las consultas BigQuery MCP no usan `AS rows` como alias.
- [ ] Las consultas BigQuery MCP no reutilizan nombres de CTE como aliases de columna.
- [ ] Las consultas BigQuery MCP no usan joins implicitos con coma.
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

# 5. Knowledge Set

- [ ] Existe un Knowledge Set estabilizado.
- [ ] Se ha aplicado `docs/experiments/knowledge-construction-profile-v0.2.md` como guia interna solo durante Knowledge Generation.
- [ ] El conocimiento deriva de la evidencia.
- [ ] No se limita a repetir métricas.
- [ ] Los riesgos están identificados.
- [ ] Las incertidumbres permanecen explícitas.

---

# 6. Recommendation Set

- [ ] Existe un Recommendation Set estabilizado.
- [ ] Todas las recomendaciones derivan del Knowledge Set.
- [ ] Las prioridades están definidas.
- [ ] No existen recomendaciones sin justificación.

---

# 7. Presentation

- [ ] Los cuatro artefactos canónicos existen antes de Presentation Layer.
- [ ] Puede demostrarse que Evidence quedó estabilizada antes de Presentation Layer.
- [ ] Puede demostrarse que Knowledge deriva exclusivamente de Evidence.
- [ ] Puede demostrarse que Recommendations derivan exclusivamente de Knowledge.
- [ ] Evidence, Knowledge y Recommendations no aparecen por primera vez dentro del informe final.
- [ ] Presentation Layer consume esos estados cerrados y no los reconstruye.
- [ ] Las limitaciones, UNKNOWNs y coverage states fueron preservados antes de representar.
- [ ] La Presentation Projection está resuelta.
- [ ] El Communication Context está resuelto.
- [ ] La Presentation Policy está identificada, cuando corresponda.
- [ ] Presentation Layer no ha reconstruido conocimiento.
- [ ] Presentation Layer no ha generado recomendaciones nuevas.

---

# 8. Validación final

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