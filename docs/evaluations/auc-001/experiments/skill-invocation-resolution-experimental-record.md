# Skill Invocation Resolution Experimental Record

## Metadata

| Field | Value |
|---|---|
| Document Type | Experimental Record |
| Related Plan | `docs/evaluations/auc-001/historical/skill-invocation-resolution-investigation-plan.md` |
| Execution Date | 2026-07-14 |
| Workspace | `C:\Workspace\VCA\vca-ai` |
| Environment | Same Codex workspace/session; sub-agent executions spawned from the same parent session |
| Plan Modified | No |
| Skill Modified | No |
| Specifications Modified | No |
| Contracts Modified | No |
| Status | Completed as experimental record; records only observed signals |

---

## Control References Used For Observation

| Reference | Use In This Record |
|---|---|
| `docs/evaluations/auc-001/historical/skill-invocation-resolution-investigation-plan.md` | Invocation matrix and controls to record |
| `.github/skills/meta-lead-quality-analysis/SKILL.md` | Skill recognition and canonical workflow reference |
| `docs/handoffs/auc-001-data-contract.md` | Data Contract compliance reference |
| `configs/workspaces.json` | Workspace/provider table scope reference |

---

## Data Contract Scope Used For Objective Checks

Allowed workspace/provider tables observed from `configs/workspaces.json`:

| Dataset | Allowed Tables |
|---|---|
| `datamart-vca-494114.intermediate` | `int_faro_lead_scoring` |
| `datamart-vca-494114.marts` | `fct_spend`; `fct_lead_enriched` |

Data Contract published source exposure in `docs/handoffs/auc-001-data-contract.md`:

| Dataset Reference | Published Tables |
|---|---|
| `datamart-vca-494114.marts` | `fct_lead_enriched`; `fct_performance_daily`; `fct_spend`; `dim_campaign_signal` |

---

## Invocation Execution Register

| ID | Invocation | Agent ID | Completion State | Output Type Observed |
|---|---|---|---|---|
| I-01 | Genera un informe analítico de calidad de los leads hasta el 30 de junio. | `019f619b-61ee-7ca0-888c-2ef276fcabb8` | No completed output within observation window | None observed |
| I-02 | Analiza la calidad de los leads hasta el 30 de junio. | `019f619b-852e-7ac0-a3e3-bab06cde354c` | Completed | Direct analytical answer |
| I-03 | Ejecuta AUC-001 hasta el 30 de junio. | `019f619b-a1cf-7902-ac33-c6a31a0cb842` | No completed output within observation window | None observed |
| I-04 | Utiliza la skill Meta Lead Quality Analysis para generar un informe analítico. | `019f619b-c443-71f2-b96f-a21d063a82b6` | No completed output within observation window | None observed |
| I-05 | Ejecuta el caso de uso AUC-001 siguiendo la skill oficial. | `019f619b-e535-7f21-8177-793ea1f1a30a` | No completed output within observation window | None observed |
| I-06 | Repite el análisis usando el workflow canónico oficial de AUC-001. | `019f619c-0405-7af3-b1c1-0f6dc655341c` | Completed | Interpretive RCA-style answer |
| I-07 | Analiza AUC-001 con la skill oficial y el contexto del repositorio. | `019f61a2-ef6b-76e1-9988-1b45d2179ba3` | Completed | Repository/documentary review answer |
| I-08 | Genera la salida ejecutiva aprobada del caso AUC-001. | `019f61a3-105d-7e61-a5ba-60ae893436ac` | No completed output within observation window | None observed |

---

## Mandatory Control Observations By Invocation

Legend:

- `Yes`: explicit observable signal present in execution output.
- `No`: explicit observable contradiction or absence where output is complete.
- `Not observed`: no objective signal available in completed output.
- `Pending`: invocation still running or not yet observed.
- `N/A`: no completed output to inspect.

| ID | Skill Loaded | Exclusively BigQuery MCP Server | BigQuery CLI Appeared | Tables Consulted | Data Contract Respected | Evidence Set Materialized | Knowledge Set Materialized | Recommendation Set Materialized | Representation Consumed Sets |
|---|---|---|---|---|---|---|---|---|---|
| I-01 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| I-02 | Not observed | Not observed | Not observed | Not observed | Not observed | No | No | No | No |
| I-03 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| I-04 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| I-05 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| I-06 | Yes | Not observed | Not observed | Not observed | Not observed | No | No | No | No |
| I-07 | Yes | Not observed | Not observed | Not observed | Not observed | Yes | Yes | Yes | Yes |
| I-08 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

---

## Per-Invocation Objective Notes

### I-01

No completed output was returned within the observation window used in this experiment.

### I-02

Completed output observed.

Objective signals present:

- Final answer includes analytical metrics for June 2026.
- Final answer mentions AUC-001 only indirectly through the phrase "periodo documentado para AUC-001".
- Final answer mentions `matched`, `lead_only`, and `spend_only`.
- Final answer names one ad: `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`.

Objective signals not present:

- No explicit statement that `meta-lead-quality-analysis` was loaded.
- No explicit BigQuery MCP Server action record.
- No explicit BigQuery CLI action record.
- No table list.
- No Data Contract compliance statement.
- No Evidence Set artifact.
- No Knowledge Set artifact.
- No Recommendation Set artifact.
- No representation consumption record.

### I-03

No completed output was returned within the observation window used in this experiment.

### I-04

No completed output was returned within the observation window used in this experiment.

### I-05

No completed output was returned within the observation window used in this experiment.

### I-06

Completed output observed.

Objective signals present:

- Output explicitly references invocation `I-06`.
- Output references `docs/evaluations/auc-001/historical/skill-invocation-resolution-investigation-plan.md`.
- Output references `.github/skills/meta-lead-quality-analysis/SKILL.md`.
- Output references `.github/prompts/lead_quality_analytical_report.md`.
- Output describes the skill workflow sequence.
- Output states no repository files were modified.

Objective signals not present:

- No explicit BigQuery MCP Server action record.
- No explicit BigQuery CLI action record.
- No table list.
- No Evidence Set artifact.
- No Knowledge Set artifact.
- No Recommendation Set artifact.
- No representation consumption record.

### I-07

Completed output observed.

Objective signals present:

- Output explicitly states use of `meta-lead-quality-analysis` as framework.
- Output references `.github/skills/meta-lead-quality-analysis/SKILL.md`.
- Output references repository context artifacts and handoffs:
  - `docs/handoffs/auc-001-context-definition.md`
  - `docs/handoffs/auc-001-evidence-set.md`
  - `docs/handoffs/auc-001-knowledge-set.md`
  - `docs/handoffs/auc-001-recommendation-set.md`
  - `docs/handoffs/auc-001-executive-report.md`
- Output explicitly names Evidence Set, Knowledge Set and Recommendation Set as existing artifacts.
- Output states that the Executive Report is a selected projection.
- Output states tests were executed:
  - `auc_001_traceability_tests.ps1`: 13/13 PASS
  - `spec011_communication_context_transform_tests.ps1`: 10/10 PASS
- Output states no repository files were modified.

Objective signals not present:

- No explicit BigQuery MCP Server action record for the invocation.
- No explicit BigQuery CLI action record for the invocation.
- No table list consulted during the invocation.
- No explicit Data Contract compliance record produced by the invocation.
- No newly materialized Evidence Set, Knowledge Set or Recommendation Set was reported; existing artifacts were referenced.

### I-08

No completed output was returned within the observation window used in this experiment.

---

## Raw Completed Outputs Captured

### I-02 Raw Output

```text
Asumo el corte **1 al 30 de junio de 2026**, que es el periodo documentado para AUC-001.

La calidad global de leads es **moderada**: se registran **772 leads**, de los cuales **226 son cualificados A/B**, es decir una tasa de cualificación de **29,3%**. Dentro de los cualificados, hay **31 Tier A** y **195 Tier B**, por lo que la calidad existe, pero está muy dominada por Tier B. El coste total asociado al modelo preparado es **496,56**, con **0,64 por lead** y **2,20 por lead cualificado A/B**.

La señal más sólida está en los anuncios con cobertura `matched`, donde hay tanto leads como inversión comercial: **680 leads**, **191 cualificados A/B**, **494,36 de inversión** y una tasa de cualificación de **28,1%**. Ahí debe centrarse cualquier lectura de eficiencia. El anuncio principal, `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`, concentra **519 leads**, **152 cualificados** y **374,79 de inversión**; aporta cerca de dos tercios de los leads cualificados totales, así que el rendimiento de junio depende mucho de esa referencia.

Hay señales interesantes pero con cautela: algunos anuncios pequeños muestran tasas altas, como `ViajaComoInvitado_Estatus_ExperienciaCalidad_Reel_v1` con **50%** de cualificación y coste por cualificado de **1,09**, o `FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1` con **46,2%**. Pero sus volúmenes son bajos, así que no conviene sobredimensionarlos.

El bloque `lead_only`, asociado a RTG/CBO, tiene **92 leads** y **35 cualificados**, con una tasa de **38,0%**, superior al bloque matched. Pero no tiene inversión comercial emparejada en el modelo aprobado, así que sirve para hablar de calidad de lead, no de eficiencia económica. En cambio, `spend_only` es pequeño, **2,20 de inversión**, pero no permite calcular calidad porque no tiene leads asociados.

Conclusión: junio muestra una captación útil, con **calidad razonable pero muy concentrada**. Para decisiones inmediatas, usaría primero la evidencia `matched` a nivel de anuncio; trataría RTG como lectura separada de calidad; y evitaría recomendaciones por campaña, CTR, impresiones o creatividad real hasta ampliar el mapeo de datos.
```

### I-06 Raw Output

```text
Repetido el análisis usando la invocación `I-06`: “Repite el análisis usando el workflow canónico oficial de AUC-001”, definida en [skill-invocation-resolution-investigation-plan.md](/docs/evaluations/auc-001/historical/skill-invocation-resolution-investigation-plan.md).

**Resultado**
La causa mínima más probable sigue siendo una desviación en la resolución/carga efectiva del workflow, pero formulada con más precisión: la regresión no se explica solo por “usar BigQuery CLI”, sino por haber saltado la secuencia canónica obligatoria de AUC-001 antes de producir una salida.

El workflow oficial exige:

1. Canonicalizar contexto de ejecución.
2. Cargar contexto oficial.
3. Identificar Data Providers.
4. Adquirir evidencia verificable.
5. Estabilizar `Knowledge Set`.
6. Estabilizar `Recommendation Set`.
7. Delegar la representación a Presentation Layer.

Ese flujo está definido en [SKILL.md](/.github/skills/meta-lead-quality-analysis/SKILL.md) y reforzado por el prompt oficial, que obliga a revisar artefactos canónicos, reconstruir el workflow y usar BigQuery MCP cuando el scope lo soporte en [lead_quality_analytical_report.md](/.github/prompts/lead_quality_analytical_report.md).

**Lectura corregida**
La ejecución regresiva viola los controles canónicos `C-02` a `C-10`: contexto oficial, MCP, Data Contract, Evidence Set, Knowledge Set, Recommendation Set y representación sobre artefactos estabilizados. Esos controles están explicitados en [skill-invocation-resolution-investigation-plan.md](/docs/evaluations/auc-001/historical/skill-invocation-resolution-investigation-plan.md).

Por tanto:

- No basta con decir que el informe es inválido por usar CLI.
- Es inválido porque no demuestra haber seguido el lifecycle AUC-001/SPEC-001.
- El síntoma visible es CLI + fuente fuera de contrato.
- La ruptura metodológica real es anterior: no se materializa el workflow canónico completo.

**Conclusión**
Usando el workflow canónico oficial, la hipótesis más fuerte queda así:

La regresión se produce porque la invocación o el mecanismo de activación no cargó o no preservó el workflow oficial de AUC-001. El uso de CLI, la omisión de contexto y la ausencia de Evidence/Knowledge/Recommendation estabilizados son consecuencias observables de esa ruptura, no causas independientes suficientes.

No modifiqué archivos del repositorio.
```


### I-07 Raw Output

```text
Usé la skill oficial [meta-lead-quality-analysis](/.github/skills/meta-lead-quality-analysis/SKILL.md) como marco de lectura y la contrasté con el AUC, handoffs, evaluaciones y pruebas del repo.

**Resultado**
AUC-001 está documentariamente cerrado como `Pass with observations`, no bloqueado. La cadena que exige la skill existe y está separada correctamente:

- Context Definition validado: [auc-001-context-definition.md](/docs/handoffs/auc-001-context-definition.md)
- Evidence Set observable: [auc-001-evidence-set.md](/docs/handoffs/auc-001-evidence-set.md)
- Knowledge Set estabilizado: [auc-001-knowledge-set.md](/docs/handoffs/auc-001-knowledge-set.md)
- Recommendation Set priorizado: [auc-001-recommendation-set.md](/docs/handoffs/auc-001-recommendation-set.md)
- Executive Report como proyección seleccionada: [auc-001-executive-report.md](/docs/handoffs/auc-001-executive-report.md)

La skill exige no volver a derivar conocimiento ni recomendaciones durante Presentation Layer; el repo lo respeta explícitamente en el Executive Report y en el Presentation Contract.

**Hallazgos**
La evidencia principal de AUC-001 es suficiente dentro del modelo corregido: 15 ads preparados, 772 leads, 226 leads A/B cualificados y 496.56 de inversión comercial. El núcleo interpretativo fuerte está en el estado `matched`; `lead_only` y `spend_only` están preservados como estados de cobertura, sin forzar eficiencia donde no hay emparejamiento.

Las observaciones activas son reales pero no bloqueantes:

- BigQuery MCP está validado para `intermediate.int_faro_lead_scoring`, pero no reejecuta todo T-018 vía MCP: [auc-001-bigquery-mcp-integration-validation.md](/docs/evaluations/auc-001/validations/auc-001-bigquery-mcp-integration-validation.md)
- Quedan limitaciones de datos: sin impresiones/clicks/CTR, sin metadata creativa, y campaña/adset parcialmente condicionado.
- Hay una tensión menor de gobernanza: el frontmatter del AUC sigue en `status: Proposed` aunque el cierre documental dice `Pass with observations`: [meta_lead_quality_analysis.md](/analytical_use_cases/meta_lead_quality_analysis.md)

**Verificación**
Ejecuté las pruebas relevantes:

- `auc_001_traceability_tests.ps1`: 13/13 PASS
- `spec011_communication_context_transform_tests.ps1`: 10/10 PASS

No modifiqué archivos. Mi lectura: AUC-001 está apto como primer ciclo analítico validado, con deuda residual controlada y trazable; el ajuste más claro sería actualizar el estado documental del AUC para que no siga pareciendo “Proposed”.
```