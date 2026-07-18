# AUC-001 Canonical Cost-Quality Model Architectural Decision

## 1. Contexto

| Campo | Valor |
|---|---|
| Decision ID | VCA-AUC-001-ARCH-004 |
| Decision Type | Architectural Decision |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Status | Approved and validated for AUC-001-PCI-001 |
| Owner | Architect Agent |
| Scope | Modelo canonico reproducible de coste-calidad para AUC-001 |
| Branch source of truth | `auc-001-doc-restructuring` |

AUC-001 esta activo como caso experimental de `vca-ai` para analizar calidad de leads de Meta Ads, scoring FARO y eficiencia economica mediante SDD. El caso ya dispone de Context, Data, Analytical, Evidence, Knowledge, Recommendation y Presentation contracts, un Runbook canonico de 13 fases, validaciones de BigQuery MCP y salidas historicas.

La revision arquitectonica detecta un bloqueo residual: no existe una definicion unica, inequívoca y reproducible del universo coste-calidad. Como consecuencia, CPL, coste por A/B y metricas por anuncio pueden variar segun la ejecucion, el periodo o el universo economico usado.

Esta decision no implementa la solucion, no genera nuevo informe analitico y no modifica AIF Foundation.

## 2. Problema

Actualmente conviven al menos cuatro lecturas economicas distintas:

- inversion total de todas las señales de `fct_spend`;
- inversion `COMMERCIAL`;
- inversion del modelo preparado `ad_quality_spend_model`;
- inversion `matched` entre leads y spend.

Tambien conviven diferentes universos de leads:

- leads totales en tablas de lead/scoring;
- leads dentro de anuncios emparejados con inversion comercial;
- leads `lead_only`;
- leads A/B totales;
- leads A/B emparejados.

El problema no es que estos universos existan. El problema es que no hay una regla canonica que declare cuales son comparables, cuales son subconjuntos y que nombre debe recibir cada metrica para impedir una lectura mezclada.

## 3. Evidencia Revisada

Artefactos revisados:

- `.github/skills/meta-lead-quality-analysis/SKILL.md`, `RUNBOOK.md`, `CHECKLIST.md`, `ANALYTICAL_PROFILE.md` y `knowledge-construction-profile.md`.
- `docs/context_refs.md` y `analytical_use_cases/meta_lead_quality_analysis.md`.
- Contracts base: Context, Data, Analytical, Evidence, Knowledge, Recommendation y Presentation.
- `analytical_use_cases/auc-001/analytical-contract.md`.
- Handoffs AUC-001: Context Definition, Execution Context, Data, Discovery, Source Table Review, Analytical Preparation, Analytical Contract, Evidence Acquisition, Evidence Set, Evidence Contract, Knowledge Set, Recommendation Set y Presentation Contract.
- Informe persistido `outputs/auc-001/2026-06-30/analytical-report.md`, usado solo como antecedente documental y nivel esperado de producto, no como evidencia analitica nueva.
- Evaluaciones y diagnosticos MCP: integration validation, end-to-end validation, end-to-end validation v2, runtime diagnosis, execution-context remediation, dry-run diagnostic, SQL conventions check y discover_metadata contract migration validation.
- Specs 010 y 011, y decisiones arquitectonicas previas ARCH-001, ARCH-002, ARCH-003 y documentary alignment decision.
- Herramientas y pruebas MCP: `configs/workspaces.json`, `tools/vca_mcp_contract.py`, `tools/vca_mcp_smoke.py`, `tests/evals/auc_001_discover_metadata_contract_tests.ps1`.

Hallazgos documentales relevantes:

- El Data Contract y el workspace autorizan `intermediate.int_faro_lead_scoring`, `marts.fct_lead_enriched`, `marts.fct_spend` y `marts.dim_campaign_signal`.
- La Discovery corregida aprueba `fct_spend`, `int_faro_lead_scoring` y `fct_lead_enriched` como base principal del modelo coste-calidad.
- La preparacion corregida define `ad_quality_spend_model` con grano `ad_id_norm`, normalizando `ad_id` lead-side mediante eliminacion del prefijo `ag:`.
- El Evidence Set canonico de junio 2026 preserva `matched`, `lead_only` y `spend_only`.
- La ejecucion MCP v2 demuestra que la normalizacion cambia la cobertura de forma material: raw join sin normalizar produce 0 matches; join normalizado produce matches.
- Los diagnosticos de dry run muestran que los rechazos MCP se debieron principalmente a SQL invalida generada por el agente (`AS rows`, colisiones de alias, comma joins), no a un defecto demostrado del proveedor.
- El Runbook vigente permite consultas `query_read_only` solo con `execution_context` cerrado: `project_id`, `dataset_id`, `max_bytes_billed`.

Separacion normativa:

| Tipo de contenido | Rol en esta decision | Regla |
|---|---|---|
| Reglas canonicas permanentes | Definen fuentes, clave, cobertura, frontera runtime, invariantes, precision, metricas y blockers. | Son normativas para la Specification AUC-local mientras esta decision siga vigente. |
| Cifras historicas observadas | Documentan diagnosticos previos y ayudan a entender el problema. | Son diagnosticas, no contractuales, no fijan umbrales ni valores esperados. |
| Metricas recalculadas por ejecucion | Resultado de cada ejecucion AUC-001 sobre su periodo canonicalizado. | Deben recalcularse desde evidencia MCP nueva; no pueden heredarse de informes, handoffs ni evaluaciones anteriores. |
## 4. Universos Economicos Encontrados

| Universo | Periodo observado | Fuentes | Filtro `campaign_signal` | Grano | Inclusion / exclusion | Cobertura | Inversion | Leads | Leads A/B | Metricas derivadas | Limitaciones |
|---|---|---|---|---|---|---|---:|---:|---:|---|---|
| Total spend all signals | 2026-04-18 a 2026-06-30 en v2; junio 2026 en handoffs | `marts.fct_spend` | Ninguno | `spend_period`, `ad_id`, señal | Todos los spend rows autorizados | Spend-only posible | 1406.23 en v2; 807.06 en junio v2 | No aplica | No aplica | share por señal | No mide calidad; no debe usarse como CPL/CPQL de leads |
| Spend `COMMERCIAL` | 2026-04-18 a 2026-06-30 en v2; junio 2026 en handoffs | `marts.fct_spend` | `COMMERCIAL` | `ad_id` / periodo | Solo inversion comercial | Puede incluir spend sin leads | 875.83 en v2; 496.56 en junio | No directo | No directo | commercial spend share | La señal vive en spend, no en lead rows |
| Prepared model total | Junio 2026 handoffs | `fct_lead_enriched`, `int_faro_lead_scoring`, `fct_spend` | Spend `COMMERCIAL` | `ad_id_norm` | Full outer alignment; conserva coverage states | `matched`, `lead_only`, `spend_only` | 496.56 | 772 | 226 | CPL preparado, coste/A-B preparado, tasa A/B | Total mezcla coberturas; util solo si conserva coverage states |
| Commercial matched | Junio 2026 handoffs; v2 como periodo extendido | Lead source + `fct_spend` | `COMMERCIAL` | `ad_id_norm` | Solo ads con leads y spend comercial | `matched` | 494.36 en junio | 680 | 191 | CPL comercial matched, coste/A-B commercial matched, ratios por anuncio | No convierte lead rows en directamente `COMMERCIAL`; campaign/adset spend parcial |
| Commercial spend-only | Junio 2026 handoffs | `fct_spend` | `COMMERCIAL` | `ad_id_norm` | Ads con spend comercial sin leads | `spend_only` | 2.20 en junio | 0 | 0 | share de spend-only | No tiene CPL, tasa A/B ni CPQL; no es gasto cero |
| Lead total | Junio 2026 handoffs; v2 periodo extendido | `fct_lead_enriched` / `int_faro_lead_scoring` | No disponible en lead table | lead / `ad_id_norm` | Leads con identificador valido segun evidencia disponible | Incluye matched y lead_only | No directo | 772 junio; 1321/1322 v2 segun fuente | 226 junio; 394/395 v2 segun fuente | tasa A/B global | No todos los leads pueden calificarse como comerciales |
| Lead-only | Junio 2026 handoffs | Lead source | No disponible en lead table | `ad_id_norm` | Leads sin spend comercial emparejado | `lead_only` | 0 por alineacion, no gasto real cero | 92 | 35 | tasa A/B lead-only | No soporta CPL/CPQL ni ausencia real de gasto |
| Commercial performance aggregate | Junio 2026 T-018 historical CLI | `marts.fct_performance_daily` | `COMMERCIAL` | dia / concept / version / angle | Performance comercial agregado | No equivalente a ad_id_norm | 439.49 | 638 | UNKNOWN | CPL agregado | Ya no es base primaria corregida; grano incompatible para coste-calidad por anuncio |

Compatibilidad:

- `Commercial matched`, `commercial spend-only` y `lead-only` son subconjuntos de cobertura dentro del modelo preparado.
- `Prepared model total` es una suma orientativa de esos estados, pero no debe usarse para conclusiones de eficiencia sin descomponer cobertura.
- `Spend COMMERCIAL` es comparable con `commercial matched + commercial spend-only`, no con leads totales sin declaracion de cobertura.
- `Total spend all signals` no es comparable con CPL/CPQL comercial porque mezcla `COMMERCIAL`, `ATTENTION` y `ACTIVATION`.
- `Commercial performance aggregate` no debe compararse directamente con el modelo `ad_id_norm`; usa otra granularidad.

Mecanismos de atribucion:

- `Total spend all signals`: atribucion spend-side por señal y periodo; no atribuye calidad.
- `Spend COMMERCIAL`: atribucion spend-side por `campaign_signal = 'COMMERCIAL'`; no atribuye por si sola leads.
- `Prepared model total`: reconciliacion full outer por `ad_id_norm`; sirve para cobertura, no para eficiencia sin separar estados.
- `Commercial matched`: atribucion determinista por `ad_id_norm` cuando existen lead quality y spend comercial.
- `Commercial spend-only`: atribucion spend-side sin lead quality emparejada.
- `Lead total` y `Lead-only`: atribucion lead-side por fuente de lead/scoring; no hereda spend ni señal comercial.

## 5. Diagnostico De La Integracion

| Dimension | Diagnostico |
|---|---|
| Formato original lead-side | `ad_id` puede venir prefijado como `ag:<numeric_meta_ad_id>` en tablas de lead/scoring. |
| Formato original spend-side | `fct_spend.ad_id` usa el identificador numerico sin prefijo `ag:`. |
| Normalizacion aplicada | `ad_id_norm = REGEXP_REPLACE(ad_id, r'^ag:', '')` o equivalente estrictamente prefijado. |
| Cobertura sin normalizar | El raw join puede producir 0 matches y falsos `lead_only`/`spend_only`. |
| Cobertura con normalizacion | La cobertura mejora materialmente; en junio 2026 se documentaron 8 commercial-spend ads matched, 5 lead_only y 2 spend_only; en v2 periodo extendido se documentaron 13 matched y 10 spend_only. |
| Unicidad | El grano analitico debe ser agregado por `ad_id_norm` antes del join; la unicidad debe validarse por fuente y periodo. |
| Duplicidades | `fct_lead_enriched` e `int_faro_lead_scoring` son fuentes equivalentes de lead quality para el periodo validado; usarlas simultaneamente como lead base duplicaria leads. |
| Colisiones | No se ha documentado colision de `ad_id_norm`, pero debe existir control obligatorio: un `ad_id_norm` no puede mapear a multiples `ad_name` conflictivos sin registrarlo. |
| Nulos / invalidos | Deben excluirse o marcarse como UNKNOWN antes de agregacion; no pueden entrar en ratios economicos. |
| `ad_name` | Es etiqueta descriptiva, no clave. Puede repetirse entre anuncios distintos y puede variar entre fuentes; usarlo como join canonico queda prohibido. |
| Lead-only | Conserva calidad lead-side, no eficiencia economica. No prueba gasto real cero. |
| Spend-only | Conserva inversion, no calidad ni CPL. No debe ocultarse ni imputarse a cero leads como fallo de calidad. |

Decision sobre clave:

`ad_id_norm` puede declararse como clave canonica de integracion para AUC-001, condicionada a estos controles:

- normalizacion prefijada y documentada;
- agregacion previa por fuente al mismo periodo;
- validacion de nulos, duplicados y colisiones;
- preservacion de `ad_name` solo como label;
- clasificacion obligatoria de `matched`, `lead_only`, `spend_only` y UNKNOWN;
- trazabilidad de la cobertura antes y despues de normalizar.

## 6. Alternativas

### Alternativa A - Join dentro de una consulta MCP

Adquirir leads, scoring e inversion mediante una consulta multi-tabla ejecutada por BigQuery MCP.

| Criterio | Evaluacion |
|---|---|
| Data Contract | Compatible si usa solo tablas allowlisted y selectors canonicos. |
| BigQuery MCP | Parcialmente compatible; el MCP acepta SQL read-only y joins validos, pero historicamente ha rechazado formas combinadas por policy o SQL invalida. |
| Seguridad | Buena si pasa policy y dry run. |
| Reproducibilidad | Sensible a forma SQL, aliases, dataset context y parser de policy. |
| Trazabilidad | Menor granularidad de auditoria si toda la adquisicion queda en una consulta compleja. |
| Mantenibilidad | Fragil ante cambios de campos, policy o formas de join. |
| Riesgo de duplicacion | Bajo si la query esta bien agregada; alto si mezcla lead sources. |
| Testabilidad | Mas dificil: una consulta concentra normalizacion, agregacion, join, coverage y metricas. |
| Impacto workflow | Mantiene Evidence Acquisition como punto fuerte, pero hace menos visible Evidence Set Construction. |
| Impacto contracts | Exige formalizar la SQL como parte fuerte del Analytical Contract. |
| Dependencias externas | Solo MCP y tablas autorizadas. |
| Validacion experimental | Posible, pero no recomendada como canon inicial por fragilidad observada. |

### Alternativa B - Adquisicion separada e integracion determinista en runtime

Adquirir mediante MCP dos agregados autorizados: lead quality por `ad_id_norm` y commercial spend por `ad_id_norm`; despues unirlos deterministamente segun una frontera runtime cerrada: Evidence Acquisition adquiere datos, Analytical Preparation normaliza y agrega cada fuente de forma independiente, y Evidence Set Construction construye el full outer join, los coverage states, los invariantes y el modelo observable.

| Criterio | Evaluacion |
|---|---|
| Data Contract | Compatible: las dos adquisiciones proceden del mismo Data Provider autorizado y de tablas allowlisted. |
| BigQuery MCP | Alta compatibilidad: reduce queries complejas, evita cross-dataset query fragil y conserva dry-run por dataset. |
| Seguridad | Alta: no amplia fuentes ni usa fallback; el join posterior no consulta datos externos. |
| Reproducibilidad | Alta si los agregados tienen schema cerrado, periodo identico, `request_id`, trace, SQL y hash/snapshot de resultado. |
| Trazabilidad | Alta: cada lado del modelo tiene evidencia y cobertura propia antes de reconciliacion. |
| Mantenibilidad | Alta: normalizacion, agregacion y reconciliacion quedan como pasos explicitos. |
| Riesgo de duplicacion | Controlable mediante una unica lead base canonica y validacion contra la otra si aplica. |
| Testabilidad | Alta: se pueden probar agregados, normalizacion, full outer join, invariantes y metricas por separado. |
| Impacto workflow | Encaja en Evidence Set Construction como integracion determinista posterior a Evidence Acquisition. |
| Impacto contracts | Exige precisar Analytical Contract, Evidence Contract, Runbook y Checklist para el modelo coste-calidad. |
| Dependencias externas | No introduce proveedor alternativo; sigue siendo MCP-only para adquisicion. |
| Validacion experimental | Recomendable dentro de AUC-001 antes de promover cualquier capacidad reusable. |

Esta alternativa no constituye un Data Provider alternativo. Si ambos datasets son adquiridos por BigQuery MCP desde fuentes autorizadas y la union posterior es determinista, declarada, trazable y limitada a la frontera runtime definida en esta decision, forma parte del workflow AUC-001.

### Alternativa C - Modelo preparado materializado en BigQuery

Consumir una tabla o mart canonica que ya contenga coste-calidad.

| Criterio | Evaluacion |
|---|---|
| Data Contract | No compatible hoy salvo nueva tabla allowlisted y contract revision. |
| BigQuery MCP | Compatible tecnicamente si se allowlistea; no autorizado actualmente. |
| Seguridad | Buena cuando exista governance; no aceptable como atajo actual. |
| Reproducibilidad | Potencialmente alta, si el mart versiona reglas y lineage. |
| Trazabilidad | Alta si el mart documenta fuentes, periodo, normalizacion, coverage e invariantes. |
| Mantenibilidad | Alta a largo plazo; costosa antes de estabilizar reglas. |
| Riesgo de duplicacion | Bajo para consumidores; medio si el mart replica logica experimental prematura. |
| Testabilidad | Buena con pruebas de mart, pero depende de otro repositorio/capa de datos. |
| Impacto workflow | Simplifica Evidence Acquisition, pero oculta parte de Evidence Set Construction si no hay lineage. |
| Impacto contracts | Exige modificar Data Contract y posiblemente Analytical Contract. |
| Dependencias externas | Alta: requiere trabajo en BigQuery/data mart y gobierno de allowlist. |
| Validacion experimental | Debe venir despues de validar B en AUC-001. |

## 7. Decision

Seleccionar la **Alternativa B - Adquisicion separada e integracion determinista en runtime** como arquitectura canonica experimental para AUC-001.

Razones:

- mantiene BigQuery MCP Server como unico Data Provider de adquisicion;
- evita depender de una query multi-tabla monolitica que ya mostro fragilidad por policy, aliases y dry run;
- hace visibles los universos economicos antes de calcular ratios;
- permite declarar `matched`, `lead_only`, `spend_only` y UNKNOWN como parte estructural del Evidence Set;
- facilita pruebas unitarias/documentales de normalizacion, cobertura, reconciliacion e invariantes;
- resuelve el problema dentro de AUC-001 sin modificar AIF Foundation.

Alternativas descartadas:

- A queda descartada como canon inicial, aunque puede seguir siendo una optimizacion futura si las queries multi-tabla se validan con suficiente robustez.
- C queda diferida hasta que AUC-001 valide experimentalmente el modelo y exista una necesidad clara de materializarlo como mart.

## 7.1 Gobernanza Post-Cierre

Esta decision se clasifica como una **evolucion post-cierre de AUC-001**.

El ciclo experimental original de AUC-001 permanece cerrado con su closure gate `READY FOR CLOSURE` de fecha 2026-07-16. ARCH-004 no reabre ese ciclo, no invalida su producto analitico final, no sobrescribe sus outputs y no convierte resultados historicos en incorrectos retrospectivamente.

La validacion futura del modelo `auc_001_canonical_cost_quality_model` debe realizarse en una iteracion separada:

| Campo | Decision |
|---|---|
| Iteration label | `AUC-001 Post-Closure Iteration 1` |
| Iteration ID | `AUC-001-PCI-001` |
| Classification | Post-closure evolution of AUC-001 |
| Parent analytical use case | AUC-001 - Meta Lead Quality Analysis |
| Previous cycle | Original experimental cycle, `Closed` |
| Current status | Implemented locally; executed and validated under `AUC-001-PCI-001-GATE-EXIT` with `PASS WITH CONDITIONS` |
| Entry gate ID | [`AUC-001-PCI-001-GATE-ENTRY`](/gates/auc-001-pci-001-entry-gate.md) |
| Exit gate ID | [`AUC-001-PCI-001-GATE-EXIT`](/gates/auc-001-pci-001-exit-gate.md) |
| Entry gate | [Post-closure iteration entry gate](/gates/auc-001-pci-001-entry-gate.md) confirming SPEC-012 review, MCP-only acquisition constraints, source authorization, output immutability and no Foundation promotion |
| Exit gate | [Post-closure iteration exit gate](/gates/auc-001-pci-001-exit-gate.md) validating canonical model execution, evidence construction, blockers, traceability, immutable historical outputs and reviewer approval |
| Acceptance basis | SPEC-012, this ADR, updated AUC contracts, Runbook/Checklist alignment and QA gate evidence |
| Relation to previous closure | Successor validation track; not continuation of the closed experiment |

Governance rules:

- the original AUC-001 experimental cycle remains closed;
- this decision does not reopen or amend the previous closure gate;
- historical outputs under the closed cycle remain immutable;
- new outputs must be persisted under `outputs/auc-001/pci-001/2026-06-30/` for the first post-closure execution of `AUC-001-PCI-001`;
- a new execution cannot be presented as a continuation of the same closed cycle;
- all new evidence, Knowledge, Recommendations and Presentation produced in this evolution must identify the post-closure iteration;
- future promotion to AIF Foundation remains out of scope until the post-closure iteration is separately validated and reviewed.
### Namespace De Persistencia Post-Cierre

La primera ejecucion de `AUC-001-PCI-001`, cuando sea autorizada, debe persistir sus salidas bajo:

```text
outputs/auc-001/pci-001/2026-06-30/
```

Estructura canonica minima:

```text
execution/
evidence/
knowledge/
recommendations/
presentation/
analytical-report/
executive-report/
```

No se permite `outputs/auc-001-pci-001/`, porque separa la iteracion de la jerarquia documental del caso de uso. Futuras iteraciones deben seguir `outputs/auc-001/pci-00N/<execution-date>/`.

La fecha identifica la ejecucion; el identificador PCI identifica la iteracion metodologica. El namespace es frontera documental de gobernanza: Entry Gate exige que este definido, Exit Gate valida solamente artefactos dentro del namespace de la iteracion y ninguna iteracion post-cierre puede sobrescribir `outputs/auc-001/2026-06-30/`.

Politica de lectura: los outputs historicos no son expected values; Knowledge, Recommendations e informes anteriores no pueden reutilizarse como fuente ni mezclarse con nuevas versiones. Solo pueden citarse como referencia documental cuando el contexto lo permita expresamente.
## 8. Definicion Del Modelo Canonico

| Campo | Definicion |
|---|---|
| Nombre | `auc_001_canonical_cost_quality_model` |
| Alias historico compatible | `ad_quality_spend_model` |
| Proposito | Relacionar calidad de leads Meta Ads con inversion comercial sin mezclar universos economicos ni coverage states. |
| Fuente lead canonica | `marts.fct_lead_enriched` para conteo de leads, `lead_id`, `lead_tier`, `qualified_ab` derivado, FARO score si esta disponible, y referencias campaign/adset/ad. |
| Fuente lead de validacion/fallback | `intermediate.int_faro_lead_scoring`; no puede sumarse a `marts.fct_lead_enriched` ni sustituirla sin decision explicita si la validacion falla. |
| Fuente spend canonica | `marts.fct_spend` para inversion, periodo, `ad_id` y `campaign_signal`. |
| Fuente de dominio | `marts.dim_campaign_signal` solo para validar dominio cuando este disponible y allowlisted. |
| Periodo | El periodo canonicalizado por Execution Context. Para solicitudes `hasta [fecha]`, inicio resuelto desde cobertura del provider, no desde ejecuciones anteriores. |
| Grano | Un registro por `ad_id_norm` y `coverage_status`; agregados por periodo cerrado. |
| Clave canonica | `ad_id_norm`. |
| Regla de normalizacion | En fuentes lead-side, eliminar estrictamente prefijo inicial `ag:`; en spend-side usar `ad_id` como `ad_id_norm`. No normalizar nombres. |
| Filtro de señal | `campaign_signal = 'COMMERCIAL'` solo para spend comercial. Leads no heredan `COMMERCIAL` como atributo directo. |
| Estados de cobertura | `matched`, `lead_only`, `spend_only`, `UNKNOWN`. |
| Calidad | Qualified A/B = `lead_tier IN ('A', 'B')`; Tier A, B, C, D no cambian de significado. |
| Reconciliacion | Full outer join determinista entre agregado lead quality y agregado spend commercial por `ad_id_norm`. |
| UNKNOWNs | Nulos, IDs invalidos, colisiones, campaign/adset spend ausente, creative asset metadata ausente y ratios no definidos deben permanecer visibles. |

### Politica De Fuente Canonica De Leads

AUC-001 debe contar y cualificar leads desde una unica fuente canonica: `marts.fct_lead_enriched`. La evidencia documental existente la identifica como mart-level enriched lead fact con FARO scores, tiers y referencias campaign/adset/ad; por tanto cierra la ambiguedad entre fuentes lead-side.

`intermediate.int_faro_lead_scoring` queda reservado para validacion y fallback controlado. La validacion minima entre ambas fuentes debe comparar, al mismo periodo y grano `ad_id_norm`:

- row count / lead row count;
- distinct `lead_id`;
- cobertura de `ad_id_norm`;
- conteos por `lead_tier` A/B y, cuando aplique, A, B, C, D;
- `qualified_ab` derivado;
- FARO score o distribucion de score cuando el campo este disponible en ambas fuentes.

Si hay discrepancias por encima de la tolerancia documentada, discrepancias no explicadas o ausencia de validacion obligatoria, la publicacion queda bloqueada. `marts.fct_lead_enriched` prevalece solo cuando la validacion pasa; si no pasa, no se publican metricas coste-calidad y debe abrirse una decision especifica de source table.

### Frontera Exacta Del Runtime

| Fase | Responsabilidad permitida | Salida |
|---|---|---|
| Evidence Acquisition | Adquirir evidencia mediante BigQuery MCP en consultas separadas y autorizadas. | Agregado lead-side y agregado spend-side trazables, con SQL, request IDs, periodo y execution context. |
| Analytical Preparation | Normalizar, limpiar, validar y agregar cada fuente de forma independiente. No une fuentes para razonar ni publicar resultados. | Agregados preparados por `ad_id_norm`, checks de fuente, dominios, nulos, duplicados y equivalencia lead source. |
| Evidence Set Construction | Ejecutar full outer join determinista por `ad_id_norm`, asignar `coverage_status`, reconciliar totales, calcular invariantes y construir el modelo observable. | Evidence Set coste-calidad con coverage states, metricas derivadas y limitaciones visibles. |

Esta frontera respeta los contratos AUC-001 porque la adquisicion solo expone datos autorizados, la preparacion convierte fuentes en agregados comparables sin razonamiento, y Evidence Set Construction construye evidencia observable, estados de cobertura y metricas derivadas sin producir Knowledge, Recommendations ni Presentation.

Tratamiento de cobertura:

| Estado | Tratamiento canonico |
|---|---|
| `matched` | Puede soportar lectura coste-calidad, CPL comercial matched, coste por A/B matched y metricas descriptivas por anuncio. |
| `lead_only` | Puede soportar volumen y tasa A/B lead-side. No puede soportar CPL/CPQL. No representa adquisicion gratuita; indica ausencia de spend comercial emparejado, posible diferencia temporal, cobertura incompleta o problema de matching. |
| `spend_only` | Puede soportar inversion y share de inversion no emparejada. No puede soportar lead quality, CPL ni CPQL. No representa automaticamente ineficiencia ni anuncios con cero leads reales; indica spend sin lead quality emparejada en el universo observado. |
| `UNKNOWN` | Bloquea metricas dependientes hasta resolucion; no se imputa por inferencia. |

Distinciones obligatorias:

| Identidad | Formula conceptual |
|---|---|
| Inversion total | `SUM(spend_amount)` de todas las señales autorizadas. |
| Inversion `COMMERCIAL` | `SUM(spend_amount)` donde `campaign_signal = 'COMMERCIAL'`. |
| Inversion comercial emparejada | `SUM(spend_amount)` donde `coverage_status = 'matched'`. |
| Inversion `spend_only` | `SUM(spend_amount)` donde `coverage_status = 'spend_only'`. |
| Leads totales | Leads de `marts.fct_lead_enriched` en el periodo, tras validacion contra `intermediate.int_faro_lead_scoring`. |
| Leads emparejados | Leads donde `coverage_status = 'matched'`. |
| Leads `lead_only` | Leads donde `coverage_status = 'lead_only'`. |
| Leads A/B | Leads con `lead_tier IN ('A','B')`. |
| Leads A/B emparejados | Leads A/B donde `coverage_status = 'matched'`. |

Reglas para evitar doble conteo:

- no sumar `int_faro_lead_scoring` y `fct_lead_enriched` como dos bases de leads;
- no sumar `fct_performance_daily` con `fct_spend` para inversion del modelo canonico;
- no mezclar `ATTENTION` y `ACTIVATION` en metricas de eficiencia comercial;
- no convertir `lead_only` en spend cero para eficiencia;
- no convertir `spend_only` en cero leads como metrica de mala calidad.
## 9. Metricas Permitidas

La metrica economica primaria del modelo canonico es `cpl_commercial_matched = matched_commercial_spend / matched_leads`. Cualquier metrica que use spend comercial total con denominador matched es diagnostica de reconciliacion, no CPL canonico.

| Metrica recomendada | Numerador | Denominador | Universo | Cobertura | Limitaciones |
|---|---|---|---|---|---|
| `cpl_global_all_signals_observed` | Inversion total all signals | Leads totales | Orientacion global | Mixed | Solo orientativo; no es eficiencia comercial. |
| `commercial_spend_per_matched_lead_observed` | Inversion `COMMERCIAL` total, incluyendo `spend_only` | Leads emparejados con ads de spend comercial | Diagnostico de reconciliacion | `matched` denominator + `spend_only` numerator visible | No es CPL canonico; debe etiquetarse como observed diagnostic y mostrar `spend_only_spend`. |
| `cpl_commercial_matched` | Inversion comercial emparejada | Leads emparejados | Coste-calidad canonico | `matched` | Canonica para eficiencia lead-cost en AUC-001. |
| `qualified_rate_ab_global` | Leads A/B totales | Leads totales | Lead quality global | Lead-side | No incluye gasto. |
| `qualified_rate_ab_matched` | Leads A/B emparejados | Leads emparejados | Coste-calidad canonico | `matched` | No extrapolar a lead_only. |
| `cost_per_ab_commercial_matched` | Inversion comercial emparejada | Leads A/B emparejados | Coste-calidad canonico | `matched` | Nombre preferido frente a `CPQL` ambiguo. |
| `cost_per_tier_a_commercial_matched` | Inversion comercial emparejada | Leads Tier A emparejados | Coste-calidad canonico | `matched` | Sensible a denominadores bajos. |
| `spend_share_by_signal` | Spend por señal | Spend total | Spend all signals | Spend-only capable | No implica calidad. |
| `spend_share_matched` | Spend matched | Spend commercial | Comercial | Coverage split | Mide cobertura, no eficiencia. |
| `lead_share_matched` | Leads matched | Leads totales | Lead-side reconciliado | Coverage split | Mide cobertura, no coste. |
| `ab_share_matched` | Leads A/B matched | Leads A/B totales | Lead-side reconciliado | Coverage split | Mide cobertura de calidad en matched. |
| `ad_cost_quality_metrics_matched` | Spend, leads, A/B, Tier A por `ad_id_norm` | Denominadores por anuncio | Anuncio | `matched` | Requiere volumen minimo y no causalidad creativa. |
| `lead_only_quality_metrics` | Leads A/B lead_only | Leads lead_only | Lead-only | `lead_only` | Sin coste; no implica adquisicion gratuita. |
| `spend_only_spend_metrics` | Spend spend_only | Spend commercial | Spend-only | `spend_only` | Sin calidad; no implica automaticamente ineficiencia. |

Regla de naming:

No se permite publicar una metrica llamada simplemente `CPQL`. Debe nombrarse con universo y cobertura, por ejemplo `cost_per_ab_commercial_matched` o `cpql_ab_commercial_matched`.

Metricas no permitidas:

- `CPQL` sin universo, señal y coverage.
- `cpl_commercial_observed` como metrica primaria o equivalente a CPL canonico.
- `CPL` por anuncio que use `lead_only` como gasto cero.
- `CPQL` o coste por Tier A en `spend_only`.
- coste-calidad mezclando `COMMERCIAL`, `ATTENTION` y `ACTIVATION`.
- eficiencia por campaign/adset cuando el spend procede de `fct_spend` sin mapping autorizado a campaign/adset.
- ranking creativo por asset, formato o media cuando solo existe `ad_name`.
- metrica por nombre de anuncio como si `ad_name` fuera clave estable.

### Politica De Ranking Por Anuncio

| Uso | Umbral minimo | Tratamiento |
|---|---:|---|
| Metrica descriptiva por anuncio | 1 lead matched y spend matched existente | Puede mostrarse como observacion descriptiva con cobertura visible. |
| Ranking comparativo | 10 leads matched | Puede ordenarse, pero sin recomendacion fuerte si no supera el umbral de recomendacion. |
| Recomendacion fuerte de inversion | 20 leads matched y 5 leads A/B matched | Puede alimentar recomendaciones, siempre con periodo, coverage y limitaciones. |
| Por debajo del umbral aplicable | No aplica | Marcar muestra insuficiente; no emitir recomendacion de inversion. |

Estos umbrales son experimentales y configurables dentro de AUC-001. Deben validarse antes de cada informe final y no pueden promoverse a Foundation sin nueva decision. Las conclusiones por anuncio son de referencia de anuncio (`ad_id_norm` / `ad_name`), no de causalidad creativa; no se permite afirmar que un asset, formato o pieza visual causa la calidad si solo existe `ad_name` como etiqueta.
## 10. Invariantes

Identidades de reconciliacion obligatorias:

```text
commercial_spend = matched_spend + spend_only_spend
lead_total = matched_leads + lead_only_leads
ab_total = matched_ab_leads + lead_only_ab_leads
tier_a_total = matched_tier_a + lead_only_tier_a
tier_b_total = matched_tier_b + lead_only_tier_b
prepared_ad_count = matched_ad_count + lead_only_ad_count + spend_only_ad_count
```

Identidades de no comparacion:

```text
total_spend_all_signals != commercial_spend
commercial_spend != matched_spend when spend_only_spend > 0
lead_only_spend is not real zero spend
spend_only_leads are UNKNOWN for quality interpretation, not failed leads
ad_name is not an integration key
```

Controles de calidad minimos:

- validar cobertura temporal de cada fuente antes de adquirir evidencia;
- validar dominio de `campaign_signal` cuando `dim_campaign_signal` este autorizado y disponible;
- registrar raw `ad_id` coverage y normalized `ad_id_norm` coverage;
- validar nulos e invalidos de `ad_id` y `ad_id_norm`;
- detectar multiples `ad_name` por `ad_id_norm`;
- detectar multiples raw IDs que colapsan en un `ad_id_norm`;
- validar equivalencia entre `fct_lead_enriched` e `int_faro_lead_scoring` antes de publicar metricas;
- registrar queries rechazadas como no utilizables;
- conservar trace IDs, SQL, request IDs, execution context y bytes/cost policy.

## 11. Precision Economica

| Regla | Decision |
|---|---|
| Moneda | EUR. |
| Tipo recomendado | `NUMERIC` para importes, ratios economicos y agregados monetarios. |
| Redondeo interno | Prohibido redondear en pasos intermedios. |
| Presentacion | 2 decimales para importes y ratios monetarios. |
| Tolerancia monetaria de reconciliacion | 0.01 EUR. |
| Denominador cero | Resultado `NULL`, nunca 0. |
| Valor desconocido | `NULL` o `UNKNOWN` explicito; no se permite imputacion silenciosa. |

## 12. Criterios De Bloqueo Y Limitacion

| Condicion | Clasificacion | Efecto |
|---|---|---|
| Falla una identidad de reconciliacion obligatoria | Blocking error | No publicar Evidence Set ni metricas derivadas. |
| Colision no resuelta de `ad_id_norm` | Blocking error | No publicar metricas por anuncio ni agregados dependientes. |
| Fuente lead canonica no validada contra `intermediate.int_faro_lead_scoring` cuando la validacion es obligatoria | Blocking error | No publicar metricas coste-calidad. |
| Periodo lead-side y spend-side no coincide | Blocking error | No publicar ratios economicos. |
| Denominador cero en metrica economica | Blocking error para esa metrica | Publicar `NULL` y bloquear cualquier narrativa que lo convierta en 0. |
| Senal economica no identificada o dominio `campaign_signal` invalido | Blocking error | No publicar eficiencia comercial. |
| Cobertura matched insuficiente para el objetivo del informe | Blocking error o warning segun alcance aprobado | Bloquear recomendaciones si afecta ranking/inversion; permitir solo cobertura descriptiva si el alcance lo permite. |
| Discrepancia monetaria superior a 0.01 EUR | Blocking error | No publicar reconciliacion economica. |
| Mezcla de señales economicas en una metrica comercial | Blocking error | Rechazar la metrica. |
| Uso de `ad_name` como clave | Blocking error | Rechazar join, ranking o agregacion. |
| `lead_only` mostrado con coste cero | Blocking error | Rechazar metrica o narrativa. |
| `spend_only` interpretado como anuncio con cero leads reales | Warning si es texto corregible; Blocking error si sustenta recomendacion | Corregir narrativa y mostrar como cobertura/reconciliacion. |
| Muestra por anuncio bajo umbral | Presentation limitation | Mostrar muestra insuficiente; no recomendar inversion. |
| Cifras historicas usadas como expected values | Blocking error | Recalcular desde evidencia de la ejecucion. |

## 13. Impacto Contractual

| Artefacto | Impacto |
|---|---|
| AUC-001 Specification local | Debe formalizar fuente lead canonica, frontera runtime, metricas normativas, precision economica, invariantes, blockers, umbrales de muestra y trazabilidad. |
| AUC-001 Analytical Contract | Debe declarar `auc_001_canonical_cost_quality_model`, alternativa B, `marts.fct_lead_enriched` como fuente lead canonica, validacion contra `intermediate.int_faro_lead_scoring`, metricas permitidas/no permitidas y precision. |
| AUC-001 Data Contract | Debe precisar fuentes autorizadas, rol de `dim_campaign_signal`, adquisicion MCP separada, no introduccion de nuevas fuentes y prohibicion de fallback. |
| AUC-001 Evidence Contract | Debe ampliar Evidence Set con universos economicos, coverage states, full outer join, invariantes, blockers, metricas derivadas y trazabilidad SQL/request/execution context. |
| Runbook | Debe ajustar Evidence Acquisition, Analytical Preparation y Evidence Set Construction con la frontera exacta definida aqui. |
| Checklist | Debe incorporar checks de fuente lead canonica, `ad_id_norm`, coverage, precision, naming CPQL, blockers, umbrales de ranking y ausencia de `ad_name` como clave. |
| Tests documentales/locales | Deben cubrir normalizacion, invariantes, denominadores cero, precision monetaria, coverage states, prohibicion de metricas ambiguas y criterios de bloqueo. |
| Context Contract base | No requiere cambio inmediato. |
| Presentation Contract base | No requiere cambio inmediato; debe preservar limitaciones y coverage states cuando se ejecute el informe. |
| SPEC-010 / SPEC-011 | Sin cambio. Son de Presentation y no deben reabrirse por un problema de modelo analitico. |
| AIF Foundation | Sin cambio. La capacidad reusable potencial debe validarse primero dentro de AUC-001. |

Nueva specification:

Se recomienda una specification AUC-local para formalizar el modelo canonico coste-calidad antes de implementar. No debe ser una specification de Foundation.

## 14. Riesgos

| Riesgo | Severidad | Mitigacion |
|---|---|---|
| Confundir integracion determinista con Data Provider alternativo | Important | Declarar que toda adquisicion proviene de BigQuery MCP y que la union posterior es Evidence Set Construction. |
| Publicar `CPQL` sin universo | Important | Checklist debe bloquear metricas economicas sin nombre de universo y coverage. |
| Sobreleer `matched` como clasificacion comercial lead-side | Important | Documentar que `campaign_signal` vive en spend-side. |
| Ocultar `lead_only` o `spend_only` por comodidad ejecutiva | Important | Presentation Contract debe exigir coverage visible cuando afecte eficiencia. |
| Usar `ad_name` como join por coincidencia aparente | Important | Prohibicion explicita en Analytical Contract y tests. |
| Introducir mart BigQuery prematuro | Medium | Diferir C hasta validar B. |
| Denominadores pequenos por anuncio | Medium | Aplicar umbrales descriptivo/ranking/recomendacion. |
| Diferencias entre periodo junio y periodo `hasta cutoff` | Medium | Toda metrica debe declarar periodo canonicalizado exacto. |

## 15. Plan De Validacion

1. Specification Agent crea una specification AUC-local para `auc_001_canonical_cost_quality_model`.
2. Tasks Planner Agent descompone actualizaciones documentales: Analytical Contract, Data Contract, Evidence Contract, Runbook, Checklist y tests.
3. Implementation Agent aplica solo cambios documentales y pruebas locales, sin generar informe.
4. QA Gate Agent valida que:
   - no se modifica AIF Foundation;
   - no se adquiere evidencia fuera de BigQuery MCP;
   - los agregados separados son MCP-only;
   - `marts.fct_lead_enriched` es la unica fuente lead canonica;
   - `intermediate.int_faro_lead_scoring` solo valida o actua como fallback por decision explicita;
   - la integracion posterior es determinista;
   - se cumplen invariantes de reconciliacion y precision;
   - ninguna metrica ambigua `CPQL` queda permitida;
   - no se publica ranking/recomendacion por anuncio sin umbrales suficientes.
5. Solo despues de esa validacion se autoriza una ejecucion de `AUC-001-PCI-001` como iteracion post-cierre separada para producir Evidence, Knowledge, Recommendation y Presentation diferenciados, sin reabrir ni sobrescribir el ciclo experimental original.

Validaciones experimentales requeridas:

- raw vs normalized `ad_id` coverage;
- colisiones y duplicidades de `ad_id_norm`;
- equivalencia lead source contra scoring source;
- reconciliacion de spend commercial, matched spend y spend_only spend;
- reconciliacion de leads totales, matched leads y lead_only leads;
- metrica por anuncio solo en `matched`;
- tratamiento de UNKNOWNs;
- denominadores cero como `NULL`;
- precision y tolerancia monetaria;
- umbrales de ranking por anuncio;
- rechazo documental de metricas sin universo.

## 16. Criterios De Aceptacion

La implementacion futura solo puede autorizarse cuando:

- exista specification AUC-local aprobada;
- el Analytical Contract declare el modelo canonico, fuente lead canonica y metricas permitidas;
- el Data Contract preserve BigQuery MCP como unica via de adquisicion;
- el Evidence Contract contenga universos, coverage states, frontera runtime, precision e invariantes;
- Runbook y Checklist bloqueen `CPQL` ambiguo;
- `ad_id_norm` sea validado como clave mediante controles de nulos, duplicados, colisiones y cobertura;
- `ad_name` quede explicitamente prohibido como clave;
- `COMMERCIAL`, `ATTENTION` y `ACTIVATION` no se mezclen en eficiencia comercial;
- `lead_only` y `spend_only` permanezcan visibles con su interpretacion correcta;
- las cifras historicas queden etiquetadas como diagnosticas y no contractuales;
- los umbrales de ranking por anuncio esten documentados y validados;
- no se modifique AIF Foundation;
- no se genere informe hasta que la cadena Context -> Evidence -> Knowledge -> Recommendations -> Presentation vuelva a ejecutarse.

## 17. Siguiente Paso SDD

Siguiente agente recomendado: **Specification Agent**.

Instruccion concreta:

```text
Trabaja en `vca-ai` sobre la rama `auc-001-doc-restructuring`. Usa el Specification Agent para crear una specification AUC-local que formalice `auc_001_canonical_cost_quality_model` conforme a `docs/decisions/auc-001/auc-001-canonical-cost-quality-model-architectural-decision.md`. No implementes el modelo ni generes informe. La specification debe fijar `marts.fct_lead_enriched` como fuente lead canonica, `intermediate.int_faro_lead_scoring` como fuente de validacion/fallback controlado, BigQuery MCP como unica adquisicion, la frontera Evidence Acquisition / Analytical Preparation / Evidence Set Construction, `ad_id_norm`, normalizacion `ag:`, coverage states, universos economicos, metricas permitidas/no permitidas, precision economica, invariantes de reconciliacion, blockers de publicacion, umbrales de muestra por anuncio, checks de calidad y cambios documentales requeridos en Analytical Contract, Data Contract, Evidence Contract, Runbook, Checklist y tests. No conviertas cifras historicas en valores contractuales.
```

## Decision Summary

La decision estabiliza AUC-001 alrededor de un modelo canonico de coste-calidad que separa adquisicion MCP de reconciliacion determinista. La arquitectura seleccionada permite calcular eficiencia economica solo cuando el universo y la cobertura lo soportan, evitando que CPL, CPQL o rankings por anuncio dependan de ejecuciones, nombres de anuncios, cifras historicas o mezclas de señales.
