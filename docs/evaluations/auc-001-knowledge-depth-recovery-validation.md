# AUC-001 Knowledge Depth Recovery QA

## Metadata

| Field | Value |
|---|---|
| Evaluation ID | VCA-AUC-001-EVAL-KDR-001 |
| Evaluation Type | Controlled validation / Knowledge depth recovery |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Status | Validated |
| Date | 2026-07-16 |
| Scope | Validate the updated AUC-001 skill artifacts against the June 2026 Evidence Set |

## 1. Alcance revisado

Esta QA revisa si la recuperación de profundidad analítica en AUC-001 es real o solo documental.

La revisión se limita a los artefactos autorizados por la solicitud actual y a la evidencia canónica ya estabilizada. No se ejecutaron consultas nuevas ni se corrigió la implementación.

### Cambios atribuibles a la implementación revisada de AUC-001

- [.github/skills/meta-lead-quality-analysis/SKILL.md](../../.github/skills/meta-lead-quality-analysis/SKILL.md)
- [.github/skills/meta-lead-quality-analysis/RUNBOOK.md](../../.github/skills/meta-lead-quality-analysis/RUNBOOK.md)
- [.github/skills/meta-lead-quality-analysis/CHECKLIST.md](../../.github/skills/meta-lead-quality-analysis/CHECKLIST.md)
- [.github/skills/meta-lead-quality-analysis/references.md](../../.github/skills/meta-lead-quality-analysis/references.md)

### Artefactos de validación producidos por el cambio

- [docs/evaluations/auc-001-knowledge-depth-recovery-validation.md](auc-001-knowledge-depth-recovery-validation.md)
- [docs/evaluations/auc-001-analytical-investigation-analysis.md](auc-001-analytical-investigation-analysis.md)
- [docs/evaluations/auc-001-knowledge-construction-comparative-analysis.md](auc-001-knowledge-construction-comparative-analysis.md)

### Evidencia y corpus de comparación utilizados

- [docs/handoffs/auc-001-evidence-set.md](../../docs/handoffs/auc-001-evidence-set.md)
- [docs/handoffs/auc-001-knowledge-set.md](../../docs/handoffs/auc-001-knowledge-set.md)
- [docs/handoffs/auc-001-recommendation-set.md](../../docs/handoffs/auc-001-recommendation-set.md)
- [docs/evaluations/corpus/informe_calidad_leads_scoring_20260701.md](corpus/informe_calidad_leads_scoring_20260701.md)
- [docs/evaluations/corpus/prompt_historico_monolitico.md](corpus/prompt_historico_monolitico.md)

### Modificaciones detectadas en el working tree, pero no atribuidas a esta implementación

Las siguientes rutas aparecen en el diff del workspace y se registran solo como estado observado, no como cambios atribuidos a la recuperación de profundidad:

- [AGENTS.md](../../AGENTS.md)
- [README.md](../../README.md)
- [docs/context_refs.md](../../docs/context_refs.md)
- [specs/spec-011-communication-context-representation-transformation.md](../../specs/spec-011-communication-context-representation-transformation.md)
- [docs/contracts/presentation.contract.md](../../docs/contracts/presentation.contract.md)
- [docs/contracts/knowledge.contract.md](../../docs/contracts/knowledge.contract.md)
- [docs/evaluations/auc-001-codex-routing-remediation.md](auc-001-codex-routing-remediation.md)
- [docs/evaluations/auc-001-mcp-execution-context-remediation.md](auc-001-mcp-execution-context-remediation.md)

Estas rutas existen en el workspace, pero no se usan para atribuir el resultado de la recuperación de profundidad de AUC-001 en esta QA.

## 2. Preservación del lifecycle

La secuencia vigente sigue siendo:

```text
Context Definition
→ Evidence Set
→ Analytical Investigation / Findings
→ Knowledge Set
→ Recommendation Set
→ Presentation
```

### Verificación

- El Evidence Set sigue siendo la fuente de entrada para Knowledge Generation.
- No se adquiere nueva evidencia durante Knowledge Generation.
- Presentation no reconstruye findings ni Knowledge desde cero.
- Recommendations derivan del Knowledge Set y no vuelven a consultar Evidence de forma directa.
- El RUNBOOK no reintroduce el prompt monolítico; incorpora un programa de investigacion analitica dentro de Knowledge Generation sin crear una nueva fase.

### Juicio

Lifecycle preservado: **Pass**.

## 3. Analytical Investigation Record

El Analytical Investigation Record no es ceremonial. Contiene preguntas investigadas, operaciones, findings, materialidad, cobertura, incertidumbres y explicaciones alternativas.

### Señales de profundidad real

- formula preguntas de investigación antes de consolidar Knowledge;
- reconstruye Knowledge hacia atrás desde findings;
- distingue niveles A/B/C/D/E del proceso intelectual;
- separa disciplina de frontera y traducción de negocio;
- explicita hipótesis alternativas y evidencia a favor/en contra;
- no convierte el registro en una tabla decorativa para superar el checklist.

### Límite observado

El record es profundo para el Evidence Set actual, pero no puede cubrir familias de evidencia que ese Evidence Set no contiene.

## 4. Validación de findings

### Muestra representativa revisada

| Cadena | Evidencia | Operación | Finding | Knowledge | Juicio |
|---|---|---|---|---|---|
| R-01 | 1.339 leads, 396 qualified, 65 high quality, 29,6% y 4,9% | Descriptivo + síntesis | El volumen es suficiente pero la calidad es minoritaria | El canal compra volumen barato, no calidad homogénea | Válido y trazable |
| R-02 | Matriz histórica por creatividad | Concentración + comparativo | Pocas piezas concentran la mayor parte del resultado | El valor aparece concentrado en pocas piezas de mayor volumen | Válido y no prescriptivo |
| R-03 | Billetes de avión: mirar / proceso / sí | Relacional + comparativo | Existe una diferencia marcada por categoría de intención | La disponibilidad de billetes es la señal observada con mayor diferencia de calidad entre categorías | Válido, no predictivo |
| R-07 | Cruce de billetes, fecha y experiencia | Relacional + síntesis | Las señales se acumulan y refuerzan entre sí | La combinación de señales presenta una asociación más fuerte con la calidad que las variables aisladas | Válido, pero no causal |
| FND-07 | `lead_only` vs `matched` | Coverage classification | No pueden mezclarse como si fueran equivalentes | La separación de coverage states limita la inferencia permitida | Válido y metodológicamente crítico |

### Criterios verificados

- Cada finding añade observación derivada, no una simple métrica.
- Cada finding mantiene trazabilidad a Evidence.
- Ningún finding contiene recomendaciones.
- Los coverage states y UNKNOWNs se preservan.
- Las asociaciones no se presentan como causalidad validada.

## 5. Comparación entre Knowledge Set anterior y nuevo

### Evaluación general

El Knowledge Set nuevo es más profundo que el anterior porque ya no solo resume, sino que investiga: pregunta, contrasta, descarta explicaciones débiles y consolida conocimiento a partir de findings intermedios.

El Knowledge Set anterior era correcto, pero más compacto y más dependiente de la lectura documental de la evidencia. El nuevo incorpora una capa de investigación explícita previa al conocimiento.

### Comparación por criterio

| Criterio | Knowledge Set anterior | Knowledge Set nuevo | Juicio |
|---|---|---|---|
| Profundidad | Correcto pero descriptivo | Más exploratorio y razonado | Mejora real |
| Diversidad de preguntas | Limitada | Explícita y variada | Mejora real |
| Concentración | Presente | Mejor investigada | Mejora real |
| Comparaciones | Presentes | Más encadenadas | Mejora real |
| Trade-offs | Presencia parcial | Más claros | Mejora real |
| Anomalías | Coverage states | Coverage y anomalías metodológicas | Mejora real |
| Robustez | Declarada | Operacionalizada en findings | Mejora real |
| Relaciones entre findings | Débil | Explícita | Mejora real |
| Implicaciones de negocio | Moderadas | Más controladas | Mejora real |
| Redundancia | Baja | Controlada | Sin regresión |
| Sobreinterpretación | Baja | Más controlada aún | Mejora real |

### Conclusión comparativa

La recuperación de profundidad es real, pero solo dentro del conjunto de evidencia disponible.

## 6. Matriz histórica de capacidades

| Capacidad analítica histórica | Disponible en Evidence Set actual | Ejecutada por el nuevo método | Resultado | Clasificación |
|---|---|---|---|---|
| Distribución de calidad | Parcial: A/B y coverage states | Sí | Recuperada para la evidencia disponible | RECOVERED |
| Variables explicativas | No | No | No puede recuperarse con el evidence set actual | EVIDENCE GAP |
| Combinaciones de señales | No como variables históricas de formulario | Parcial, solo como lectura general | No comparable a la capacidad histórica | NOT COMPARABLE |
| Campañas | Sí, a nivel CAPTACION / RTG | Sí | Recuperada | RECOVERED |
| Creatividades | Parcial, a nivel de ad reference; no asset metadata | Parcial | Existe lectura, pero no equivalencia histórica | CONTRACT GAP |
| Eficiencia económica | Sí, en matched | Sí | Recuperada con cobertura declarada | RECOVERED |
| Temporalidad | No | No | No recuperada | EVIDENCE GAP |
| Plataforma | No | No | No recuperada | EVIDENCE GAP |
| High Quality | No como métrica equivalente en el Evidence Set actual | No | No recuperada | EVIDENCE GAP |
| CAPI | No | No | No recuperada | EVIDENCE GAP |

### Lectura de la matriz

- `RECOVERED`: el nuevo método alcanza profundidad equivalente o superior dentro de la evidencia que sí existe.
- `EVIDENCE GAP`: la información no está en el Evidence Set actual.
- `CONTRACT GAP`: la información no se materializa en el contrato o en la estructura actual aunque exista contexto aguas arriba.
- `NOT COMPARABLE`: la capacidad histórica dependía de evidencia o supuestos que no son válidos aquí.

## 7. Gaps de método, evidencia y contrato

### Method gap

No se observa un `method gap` crítico para la recuperación de profundidad dentro del Evidence Set actual. El nuevo método sí investiga, sí formula preguntas y sí consolida findings.

### Evidence gap

Persisten gaps claros en:

- variables explicativas de formulario;
- high quality;
- temporalidad;
- plataforma;
- CAPI;
- ventas o CRM;
- metadata creativa real.

### Contract gap

El caso más claro es creatividad: el modelo actual permite lectura por ad reference y naming, pero no materializa metadata de asset creativa suficiente para replicar la profundidad histórica sin ambigüedad.

### Resultado de fondo

La diferencia residual frente al histórico se debe principalmente a una cobertura de evidencia inferior, no a una ausencia de método.

## 8. Riesgos de sobreinterpretación

- Tratar concentración como causalidad.
- Tratar calidad lead-side como eficiencia económica.
- Mezclar `matched`, `lead_only` y `spend_only`.
- Inferir variable explicativa cuando la evidencia no la expone.
- Convertir implicación de negocio en recomendación encubierta.
- Reintroducir high quality, temporalidad o CAPI como si estuvieran cubiertos por el Evidence Set actual.

## 9. Informe mínimo aceptable

### A. Método

**Respuesta:** Sí.

El nuevo método produce un análisis suficientemente profundo sobre la evidencia que recibe. No es un resumen lineal: genera preguntas, findings intermedios, contraste de explicaciones y disciplina de frontera.

### B. Cobertura

**Respuesta:** No.

El Evidence Set actual no contiene toda la información necesaria para responder las preguntas mínimas históricas de AUC-001. Faltan variables explicativas, temporalidad, plataforma, high quality, CAPI y CRM.

### C. Producto final

**Respuesta:** Sí, con limitación explícita.

El informe analítico resultante ya puede considerarse el informe mínimo aceptable para AUC-001 sobre la evidencia actualmente autorizada. No es equivalente al informe histórico, pero sí es un mínimo robusto, trazable y no ceremonial.

## 10. Cierre oficial del experimento

```text
AUC-001
Experiment: Knowledge Depth Recovery

Status: Validated

Outcome: PASS WITH CONDITIONS

Conclusion: The analytical workflow recovers sufficient analytical depth for the current Evidence Contract. Remaining differences with the historical report are primarily explained by Evidence Contract limitations rather than deficiencies in the analytical workflow.
```

### Lectura operativa

- El experimento queda cerrado de forma explícita.
- La discusión no debe reabrirse salvo que cambie el Evidence Set autorizado o se solicite una nueva validación comparativa.
- El resultado no equivale a recuperar el informe histórico completo; equivale a recuperar la profundidad suficiente para la evidencia actual.

## 11. Veredicto

**PASS WITH CONDITIONS — method recovered, evidence coverage remains insufficient**

**MINIMUM REPORT ACCEPTABLE**

### Interpretación del veredicto

- La profundidad analítica se ha recuperado para la evidencia disponible.
- La diferencia con el informe histórico se explica principalmente por cobertura de evidencia inferior.
- No se alcanza equivalencia histórica completa porque el Evidence Set actual no contiene varias dimensiones analíticas que el informe histórico sí utilizaba.

## 12. Siguiente acción recomendada

No ampliar todavía el Evidence Set.

La siguiente acción recomendada es realizar una validación comparativa controlada sobre el mismo Evidence Set congelado, manteniendo la nueva disciplina de investigación analítica, para confirmar estabilidad y evitar sobreinterpretación antes de cualquier extensión futura.