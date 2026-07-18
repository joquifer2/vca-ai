# Specification

## Metadata

### Spec ID

SPEC-012

### Title

AUC-001 Canonical Cost-Quality Model

### Status

Approved and executed for AUC-001-PCI-001

### Owner

Equipo VCA / Specification Agent

### Last Updated

2026-07-18

### Classification

Post-closure evolution of AUC-001

### Parent Analytical Use Case

AUC-001 - Meta Lead Quality Analysis

### Previous Cycle

Original AUC-001 experimental cycle: Closed (`READY FOR CLOSURE`, 2026-07-16)

### Post-Closure Iteration

`AUC-001 Post-Closure Iteration 1` (`AUC-001-PCI-001`)

### Entry Gate

[`AUC-001-PCI-001-GATE-ENTRY`](/gates/auc-001-pci-001-entry-gate.md)

### Exit Gate

[`AUC-001-PCI-001-GATE-EXIT`](/gates/auc-001-pci-001-exit-gate.md)

---

## 1. Purpose

Definir una specification AUC-local, implementable, verificable y trazable para `auc_001_canonical_cost_quality_model`.

Esta specification traduce a requisitos normativos la decision arquitectonica `VCA-AUC-001-ARCH-004` sin reabrir la alternativa seleccionada.

Esta specification no implementa el modelo, no adquiere evidencia, no genera informes y no modifica AIF Foundation.

---

## 2. Contexto

AUC-001 analiza calidad de leads de Meta Ads, scoring FARO y eficiencia economica dentro de `vca-ai`.

El repositorio ya contiene un modelo historico denominado `ad_quality_spend_model`, handoffs de preparacion/evidencia y contratos AUC-001. La decision arquitectonica `VCA-AUC-001-ARCH-004` estabiliza ese trabajo en un modelo canonico mas preciso:

```text
auc_001_canonical_cost_quality_model
```

El modelo canonico debe separar:

- reglas permanentes;
- cifras historicas diagnosticas;
- resultados recalculados por ejecucion.

Las cifras historicas existentes no son expected values ni valores contractuales.

---

## 2.1 Gobernanza Post-Cierre

SPEC-012 se clasifica como una evolucion post-cierre de AUC-001. No reabre el ciclo experimental original, no invalida su cierre y no modifica retroactivamente sus salidas historicas.

| Campo | Definicion |
|---|---|
| Parent AUC | `AUC-001` |
| Iteration label | `AUC-001 Post-Closure Iteration 1` |
| Iteration ID | `AUC-001-PCI-001` |
| Status | Approved; implemented locally; executed and validated under Exit Gate `PASS WITH CONDITIONS` |
| Entry gate | [`AUC-001-PCI-001-GATE-ENTRY`](/gates/auc-001-pci-001-entry-gate.md): Reviewer readiness of SPEC-012, ARCH-004, MCP-only acquisition constraints, source authorization, concrete output namespace, output immutability and no Foundation promotion |
| Exit gate | [`AUC-001-PCI-001-GATE-EXIT`](/gates/auc-001-pci-001-exit-gate.md): validation of execution evidence, canonical metrics, coverage states, blockers/warnings, traceability and non-overwrite of historical outputs |
| Relation to prior closure | Separate successor validation track; not continuation of the closed experimental cycle |

La razon de esta clasificacion es preservar el producto analitico cerrado de AUC-001 y permitir una validacion posterior del modelo coste-calidad canonico con sus propios criterios de entrada, salida, aceptacion y trazabilidad.

Los outputs derivados de esta specification deben persistirse bajo el namespace oficial definido en la seccion 2.2. No pueden sobrescribir `outputs/auc-001/2026-06-30/`, ni presentarse como correccion silenciosa, continuacion operativa o reapertura de AUC-001.

Cualquier Knowledge, Recommendation, Presentation o Evidence Set futuro debera declarar si pertenece al ciclo original cerrado o a `AUC-001-PCI-001`.

## 2.2 Namespace oficial de outputs

El namespace oficial de persistencia para la primera iteracion post-cierre es:

```text
outputs/auc-001/pci-001/2026-06-30/
```

La estructura canonica documentada dentro de ese namespace es:

```text
execution/
evidence/
knowledge/
recommendations/
presentation/
analytical-report/
executive-report/
```

No debe utilizarse `outputs/auc-001-pci-001/`. La continuidad jerarquica del caso de uso se preserva bajo `outputs/auc-001/`, y el identificador `pci-001` delimita la iteracion metodologica post-cierre.

Politica de persistencia:

- `outputs/auc-001/2026-06-30/` corresponde al ciclo experimental original y es inmutable.
- `AUC-001-PCI-001` nunca sobrescribe outputs anteriores.
- Toda nueva ejecucion post-cierre genera un namespace propio.
- La fecha identifica la ejecucion concreta.
- El identificador PCI identifica la iteracion metodologica.
- Futuras iteraciones usaran el patron `outputs/auc-001/pci-00N/<execution-date>/`.

Politica de lectura:

- queda prohibido leer outputs historicos como expected values;
- queda prohibido reutilizar Knowledge anterior como fuente;
- queda prohibido reutilizar Recommendations anteriores;
- queda prohibido regenerar informes mezclando versiones;
- los outputs historicos solo pueden usarse como referencia documental cuando el contexto lo permita expresamente.

Gobernanza:

- el namespace forma parte de la gobernanza de `AUC-001-PCI-001`;
- el Entry Gate requiere que exista un namespace definido antes de autorizar ejecucion;
- el Exit Gate valida unicamente artefactos contenidos dentro del namespace correspondiente;
- el namespace constituye la frontera documental entre iteraciones post-cierre.

---

## 3. Problema

AUC-001 puede producir metricas inconsistentes si mezcla universos economicos, fuentes lead-side, estados de cobertura o granularidades.

Los riesgos principales son:

- sumar `marts.fct_lead_enriched` e `intermediate.int_faro_lead_scoring`;
- usar `ad_name` como clave;
- tratar `lead_only` como captacion gratuita;
- tratar `spend_only` como anuncios con cero leads reales;
- mezclar `COMMERCIAL`, `ATTENTION` y `ACTIVATION` en eficiencia comercial;
- convertir cifras historicas en resultados esperados;
- publicar CPL o CPQL sin universo, cobertura y denominador validos.

---

## 4. Objetivo

Formalizar los requisitos necesarios para implementar, ejecutar y validar `auc_001_canonical_cost_quality_model` como modelo canonico experimental de coste-calidad de AUC-001.

El resultado permitio planificar, implementar, ejecutar y validar la iteracion post-cierre sin reabrir la arquitectura.

---

## 5. Alcance

### Included

- fuentes autorizadas y roles canonicos;
- adquisicion MCP separada;
- preparacion independiente por fuente;
- normalizacion `ad_id_norm`;
- reconciliacion full outer join;
- coverage states;
- universos economicos;
- metricas permitidas y prohibidas;
- precision economica;
- invariantes;
- validacion entre fuentes de leads;
- ranking experimental por anuncio;
- UNKNOWNs;
- criterios de bloqueo;
- trazabilidad;
- impacto contractual;
- plan de pruebas;
- gate de autorizacion de implementacion.

---

## 6. Fuera de alcance

- modificar AIF Foundation;
- promover una capacidad reusable al framework;
- crear un mart materializado nuevo en BigQuery;
- modificar Tier A/B/C/D;
- redefinir FARO scoring;
- generar Knowledge, Recommendations o Presentation;
- generar informes;
- adquirir evidencia nueva;
- introducir una fuente alternativa de datos;
- atribuir causalidad creativa cuando solo existe `ad_name`;
- resolver el modelo de ventas o estados comerciales;
- reabrir SPEC-010 o SPEC-011;
- modificar contracts, Runbook o Checklist en esta specification.

---

## 7. Decisiones arquitectonicas heredadas

Esta specification asume como cerradas:

| Decision | Regla heredada |
|---|---|
| Provider | BigQuery MCP Server es la unica via autorizada para evidencia nueva. |
| Arquitectura | Alternativa B: adquisicion separada e integracion determinista en runtime. |
| Lead source | `marts.fct_lead_enriched` es la fuente canonica de conteo y calidad. |
| Validation source | `intermediate.int_faro_lead_scoring` valida, no se suma. |
| Spend source | `marts.fct_spend` es fuente canonica de inversion. |
| Integration key | `ad_id_norm`. |
| Lead normalization | Eliminacion estricta del prefijo inicial `ag:`. |
| Label | `ad_name` es descriptivo, nunca clave. |
| Coverage | `matched`, `lead_only`, `spend_only`, `UNKNOWN`. |
| Main CPL | `cpl_commercial_matched = matched_commercial_spend / matched_leads`. |
| Main A/B cost | `cost_per_ab_commercial_matched = matched_commercial_spend / matched_ab_leads`. |
| Diagnostic metric | `commercial_spend_per_matched_lead_observed` es diagnostica, no KPI principal. |
| Historical figures | Diagnosticas, no contractuales. |

---

## 8. Definiciones y terminologia

| Termino | Definicion normativa |
|---|---|
| Modelo canonico | Reglas estables de fuentes, transformaciones, universos, metricas, invariantes y blockers. |
| Evidence Set ejecutado | Instancia concreta del modelo para un periodo, ejecucion, datos, resultados y trazabilidad. |
| `ad_id_norm` | Clave canonica obtenida desde lead-side eliminando solo el prefijo inicial `ag:`; en spend-side equivale a `ad_id`. |
| `matched` | Existe agregado lead-side y spend `COMMERCIAL` para el mismo `ad_id_norm`. |
| `lead_only` | Existe agregado lead-side sin spend `COMMERCIAL` emparejado. |
| `spend_only` | Existe spend `COMMERCIAL` sin agregado lead-side emparejado. |
| `UNKNOWN` | Estado o valor no fiable por ID invalido, colision, duplicidad, periodo incompatible, fuente no validada, estructura incompleta u otra condicion bloqueante. |
| A/B lead | Lead con `lead_tier IN ('A', 'B')`. |

---

## 9. Fuentes

| Fuente | Rol normativo | Uso permitido |
|---|---|---|
| `marts.fct_lead_enriched` | Fuente canonica lead-side | Conteo de leads, calidad, tiers, `lead_id`, `ad_id`, `ad_name`, referencias campaign/adset/ad y FARO score si esta disponible. |
| `intermediate.int_faro_lead_scoring` | Fuente de validacion/fallback controlado | Validar equivalencia de conteos y calidad. No puede sumarse ni sustituir automaticamente la fuente canonica. |
| `marts.fct_spend` | Fuente canonica spend-side | Inversion, `campaign_signal`, periodo, `ad_id`, `ad_name` si esta disponible. |
| `marts.dim_campaign_signal` | Fuente de dominio | Validar dominio de `campaign_signal` cuando este disponible y allowlisted. |

No se autorizan nuevas fuentes por esta specification.

---

## 10. Modelo canonico

El modelo canonico se compone de:

- agregado lead-side adquirido mediante MCP y preparado desde `marts.fct_lead_enriched`;
- agregado spend-side adquirido mediante MCP y preparado desde `marts.fct_spend`;
- validacion lead-side contra `intermediate.int_faro_lead_scoring`;
- full outer join determinista por `ad_id_norm`;
- asignacion de `coverage_status`;
- calculo de universos, metricas permitidas e invariantes.

El modelo canonico no contiene resultados fijos. Sus valores se recalculan por ejecucion.

---

## 11. Modelo ejecutado

Un Evidence Set ejecutado debe declarar:

| Campo | Requisito |
|---|---|
| execution_id | Obligatorio. |
| period_start / period_end | Periodo cerrado e identico entre fuentes. |
| specification_version | `SPEC-012` y version/fecha usada. |
| analytical_contract_version | Version del contrato AUC-001 aplicable. |
| evidence_contract_version | Version del contrato AUC-001 aplicable. |
| provider | BigQuery MCP Server. |
| source_tables | Tablas allowlisted efectivamente usadas. |
| thresholds_config | Configuracion de umbrales de ranking usada en la ejecucion. |
| blockers / warnings | Resultado de validaciones. |

El periodo debe formar parte de la clave de cualquier persistencia historica del modelo ejecutado junto con `execution_id` y `ad_id_norm`.

---

## 12. Workflow por fases

| Fase | Responsabilidad normativa | Prohibiciones |
|---|---|---|
| Evidence Acquisition | Adquirir agregados lead-side y spend-side mediante BigQuery MCP, en consultas separadas y autorizadas. | No unir fuentes, no calcular coverage reconciliado, no interpretar. |
| Analytical Preparation | Limpiar, normalizar, validar y agregar cada fuente de forma independiente; validar fuente lead canonica; comprobar grano, unicidad y periodo. | No producir Evidence Set reconciliado ni findings. |
| Evidence Set Construction | Ejecutar full outer join, asignar coverage states, reconciliar totales, calcular invariantes, construir modelo observable y metricas permitidas. | No generar Knowledge, Recommendations ni Presentation. |

Ninguna transformacion puede quedar situada ambiguamente entre fases.

---

## 13. Grano y claves

El grano canonico del Evidence Set es una fila logica por:

```text
execution_id + period_start + period_end + ad_id_norm
```

Cada fila debe tener un unico `coverage_status`.

`ad_name`, `campaign_name`, `adset_name` y campos equivalentes son labels descriptivos. No forman parte de la clave de integracion.

---

## 14. Normalizacion

Regla lead-side:

```text
ad_id_norm = remove_prefix(ad_id, "ag:") only when "ag:" is the initial prefix
```

Regla spend-side:

```text
ad_id_norm = ad_id
```

Controles obligatorios:

- `ad_id` nulo;
- `ad_id` vacio;
- valores no normalizables;
- prefijos inesperados;
- duplicados por fuente;
- multiples raw IDs colapsando en el mismo `ad_id_norm`;
- multiples `ad_name` para el mismo `ad_id_norm`;
- cobertura raw antes de normalizar;
- cobertura normalized despues de normalizar.

Queda prohibido normalizar nombres, usar coincidencia parcial, usar `ad_name` como fallback o inferir IDs por similitud textual.

---

## 15. Coverage states

| Estado | Condicion exacta | Metricas soportadas |
|---|---|---|
| `matched` | Existe agregado lead-side valido y spend `COMMERCIAL` valido para el mismo `ad_id_norm`. | CPL matched, coste A/B matched, tasa A/B matched, metricas descriptivas por anuncio si cumple umbrales. |
| `lead_only` | Existe agregado lead-side valido y no existe spend `COMMERCIAL` emparejado. | Volumen lead-side, calidad lead-side, tasa A/B lead-only. Sin CPL/CPQL. |
| `spend_only` | Existe spend `COMMERCIAL` valido y no existe agregado lead-side emparejado. | Inversion y share spend-only. Sin lead quality, CPL ni CPQL. |
| `UNKNOWN` | Existe condicion que impide clasificacion fiable. | Solo trazabilidad, limitacion y bloqueo o exclusion segun alcance. |

`lead_only` no representa captacion gratuita.

`spend_only` no representa automaticamente ineficiencia ni anuncios con cero leads reales.

---

## 16. Universos economicos

| Universo | Fuente | Filtro | Grano | Cobertura | Metricas compatibles |
|---|---|---|---|---|---|
| `total_spend_all_signals` | `marts.fct_spend` | Ninguno | periodo + ad/signal | Spend-side | `spend_share_by_signal`; no CPL comercial. |
| `commercial_spend` | `marts.fct_spend` | `campaign_signal = 'COMMERCIAL'` | periodo + `ad_id_norm` | matched + spend_only | Reconciliacion y shares. |
| `matched_commercial_spend` | Modelo reconciliado | `coverage_status = 'matched'` | `ad_id_norm` | matched | CPL/coste calidad canonicos. |
| `spend_only_commercial_spend` | Modelo reconciliado | `coverage_status = 'spend_only'` | `ad_id_norm` | spend_only | Coverage/reconciliacion. |
| `total_leads` | `marts.fct_lead_enriched` | periodo valido | `ad_id_norm` | matched + lead_only | volumen/calidad global. |
| `matched_leads` | Modelo reconciliado | `coverage_status = 'matched'` | `ad_id_norm` | matched | CPL matched, tasa matched. |
| `lead_only_leads` | Modelo reconciliado | `coverage_status = 'lead_only'` | `ad_id_norm` | lead_only | calidad descriptiva sin coste. |
| `total_ab_leads` | `marts.fct_lead_enriched` | `lead_tier IN ('A','B')` | `ad_id_norm` | matched + lead_only | tasa A/B global. |
| `matched_ab_leads` | Modelo reconciliado | A/B + matched | `ad_id_norm` | matched | `cost_per_ab_commercial_matched`. |
| `lead_only_ab_leads` | Modelo reconciliado | A/B + lead_only | `ad_id_norm` | lead_only | tasa A/B lead-only. |
| `tier_a_total` | `marts.fct_lead_enriched` | `lead_tier = 'A'` | `ad_id_norm` | matched + lead_only | calidad Tier A. |
| `tier_a_matched` | Modelo reconciliado | Tier A + matched | `ad_id_norm` | matched | `cost_per_tier_a_commercial_matched`. |
| `tier_b_total` | `marts.fct_lead_enriched` | `lead_tier = 'B'` | `ad_id_norm` | matched + lead_only | calidad Tier B. |
| `tier_b_matched` | Modelo reconciliado | Tier B + matched | `ad_id_norm` | matched | coste Tier B si se autoriza posteriormente. |

---

## 17. Metricas permitidas

| Metrica | Formula | Tipo | Publicacion |
|---|---|---|---|
| `cpl_commercial_matched` | `matched_commercial_spend / matched_leads` | Canonica | Solo matched; denominador > 0. |
| `qualified_rate_ab_global` | `total_ab_leads / total_leads` | Descriptiva | Lead-side validado; denominador > 0. |
| `qualified_rate_ab_matched` | `matched_ab_leads / matched_leads` | Canonica | Solo matched; denominador > 0. |
| `cost_per_ab_commercial_matched` | `matched_commercial_spend / matched_ab_leads` | Canonica | Solo matched; denominador > 0. |
| `cost_per_tier_a_commercial_matched` | `matched_commercial_spend / matched_tier_a` | Canonica condicionada | Solo matched; sensible a bajo volumen. |
| `spend_share_by_signal` | `spend_by_signal / total_spend_all_signals` | Descriptiva | Spend-side; no implica calidad. |
| `spend_share_matched` | `matched_commercial_spend / commercial_spend` | Reconciliacion | Mide cobertura, no eficiencia. |
| `lead_share_matched` | `matched_leads / total_leads` | Reconciliacion | Mide cobertura lead-side. |
| `ab_share_matched` | `matched_ab_leads / total_ab_leads` | Reconciliacion | Mide cobertura de calidad. |
| `commercial_spend_per_matched_lead_observed` | `commercial_spend / matched_leads` | Diagnostica | No es CPL canonico ni KPI principal. |

Ante denominador cero, la metrica debe ser `NULL`. Ante inputs desconocidos, debe ser `NULL` o `UNKNOWN` explicito.

---

## 18. Metricas prohibidas

Debe bloquearse:

- `CPL` sin universo;
- `CPQL` sin universo, señal y cobertura;
- CPL o CPQL sobre `lead_only`;
- CPL o CPQL sobre `spend_only`;
- coste-calidad mezclando señales;
- rankings por `ad_name`;
- rankings por asset, formato o creatividad sin evidencia suficiente;
- eficiencia campaign/adset sin mapping autorizado;
- cualquier ratio con denominador cero convertido a cero;
- cualquier metrica que use cifras historicas como expected value.

---

## 19. Precision economica

| Regla | Requisito |
|---|---|
| Moneda | EUR. |
| Tipo recomendado | `NUMERIC`. |
| Redondeo intermedio | No permitido. |
| Persistencia | Conservar precision suficiente para recomputar y auditar. |
| Presentacion monetaria | 2 decimales. |
| Tolerancia | 0.01 EUR. |
| Denominador cero | `NULL`, nunca 0. |
| Desconocido | `NULL` o `UNKNOWN` explicito. |

La tolerancia monetaria aplica por fila reconciliada y por agregado. Cualquier incumplimiento superior a 0.01 EUR debe clasificarse segun la tabla de blockers.

---

## 20. Invariantes

```text
commercial_spend = matched_spend + spend_only_spend
lead_total = matched_leads + lead_only_leads
ab_total = matched_ab_leads + lead_only_ab_leads
tier_a_total = matched_tier_a + lead_only_tier_a
tier_b_total = matched_tier_b + lead_only_tier_b
prepared_ad_count = matched_ad_count + lead_only_ad_count + spend_only_ad_count
```

Nivel de evaluacion:

- por ejecucion completa;
- por periodo;
- por coverage aggregate;
- por fila cuando aplique reconciliacion monetaria.

Incumplir una identidad obligatoria bloquea la publicacion del Evidence Set o de la metrica afectada segun alcance.

---

## 21. Validacion de fuentes

La validacion entre `marts.fct_lead_enriched` e `intermediate.int_faro_lead_scoring` debe ejecutarse al mismo periodo y grano `ad_id_norm`.

| Dimension | Comparacion requerida | Tolerancia |
|---|---|---|
| Row count | absoluta y relativa | Pendiente de validacion experimental. |
| Distinct leads | absoluta y relativa | Pendiente de validacion experimental. |
| `lead_id` coverage | nulos, vacios, cobertura relativa | Pendiente de validacion experimental. |
| `ad_id` coverage | raw coverage | Pendiente de validacion experimental. |
| `ad_id_norm` coverage | normalized coverage | Pendiente de validacion experimental. |
| Tier A | conteo por `ad_id_norm` | Pendiente de validacion experimental. |
| Tier B | conteo por `ad_id_norm` | Pendiente de validacion experimental. |
| Tier A/B | conteo por `ad_id_norm` | Pendiente de validacion experimental. |
| Tier C | conteo por `ad_id_norm` si existe | Pendiente de validacion experimental. |
| Tier D | conteo por `ad_id_norm` si existe | Pendiente de validacion experimental. |
| FARO score | distribucion y diferencias si existe | Pendiente de validacion experimental. |
| Distribucion por anuncio | diferencias absolutas y relativas | Pendiente de validacion experimental. |

No se fija una tolerancia numerica definitiva porque la evidencia disponible no justifica promoverla a norma. Hasta validarla experimentalmente, cualquier discrepancia no explicada debe bloquear publicacion final de metricas coste-calidad.

No hay fallback automatico. Sustituir la fuente canonica requiere decision posterior explicita.

---

## 22. Politica de rankings

Politica experimental AUC-local:

| Uso | Umbral minimo | Resultado permitido |
|---|---:|---|
| Metrica descriptiva | 1 lead matched y spend matched | Observacion descriptiva. |
| Ranking | 10 leads matched | Ranking comparativo con limitaciones. |
| Recomendacion fuerte | 20 leads matched y 5 leads A/B matched | Recomendacion posible si Knowledge/Recommendations lo soportan. |

Los umbrales son configurables por ejecucion y deben registrarse en `thresholds_config`.

Por debajo del umbral debe etiquetarse `sample_insufficient`. No se permite recomendacion de inversion.

Queda prohibida cualquier conclusion causal sobre creatividad, asset, formato o media cuando solo existe `ad_name`.

---

## 23. UNKNOWNs

Debe usarse `UNKNOWN` cuando:

- falta ID;
- el ID es invalido;
- hay colision de `ad_id_norm`;
- hay duplicidad no resuelta;
- hay periodo incompatible;
- la señal es invalida;
- la fuente canonica no esta validada;
- falta estructura obligatoria;
- la metrica depende de denominador cero o valor desconocido.

UNKNOWN no puede sustituirse por 0 ni por inferencia narrativa.

---

## 24. Criterios de bloqueo

| Condicion | Clasificacion | Alcance |
|---|---|---|
| Invariante incumplida | Blocking error | Evidence Set completo o bloque afectado. |
| Colision de `ad_id_norm` | Blocking error | Dimension/anuncio y metricas dependientes. |
| Duplicados no resueltos | Blocking error | Fuente o dimension afectada. |
| Fuente canonica no validada | Blocking error | Metricas coste-calidad. |
| Periodos incompatibles | Blocking error | Ratios economicos y Evidence Set reconciliado. |
| Señal invalida | Blocking error | Eficiencia comercial. |
| Mezcla de señales | Blocking error | Metrica afectada. |
| Discrepancia monetaria > 0.01 EUR | Blocking error | Reconciliacion economica. |
| Denominador cero | Blocking error para la metrica | Metrica concreta; publicar `NULL`. |
| Uso de `ad_name` como clave | Blocking error | Join/ranking/agregacion afectada. |
| `lead_only` con coste cero | Blocking error | Metrica o narrativa. |
| `spend_only` como cero leads reales | Warning; blocking si sustenta recomendacion | Narrativa o recomendacion. |
| Muestra insuficiente | Presentation limitation | Ranking/recomendacion. |
| Historicos como expected values | Blocking error | Validacion y publicacion. |
| Ausencia de trazabilidad MCP | Blocking error | Evidence Acquisition y Evidence Set. |

---

## 25. Trazabilidad

Cada ejecucion debe conservar:

- periodo canonicalizado;
- execution_id y timestamp;
- SQL;
- request IDs;
- trace IDs;
- execution context;
- Data Provider;
- tablas;
- filtros;
- reglas de normalizacion;
- coverage raw y normalized;
- invariantes;
- warnings;
- blockers;
- version de specification;
- version del Analytical Contract;
- version del Evidence Contract;
- configuracion de umbrales;
- evidencia de allowlist.

---

## 26. Impacto contractual

Esta specification identifica cambios futuros, pero no los aplica.

| Artefacto | Cambio futuro requerido |
|---|---|
| Analytical Contract AUC-001 | Declarar `auc_001_canonical_cost_quality_model`, fuentes, frontera runtime, metricas, precision, blockers. |
| Data Contract AUC-001 | Formalizar adquisicion MCP separada, allowlist, agregados requeridos y trazabilidad MCP. |
| Evidence Contract AUC-001 | Incluir universos, coverage states, full outer join, invariantes, UNKNOWNs y metricas derivadas permitidas. |
| Runbook | Ajustar fases 07/08 para separar adquisicion, preparacion y Evidence Set Construction. |
| Checklist | Agregar checks de fuente canonica, `ad_id_norm`, precision, CPQL, blockers y ranking. |
| SKILL | Revisar solo si el Runbook actualizado requiere exponer nuevas reglas de activacion o DoD. |
| Tests | Agregar pruebas unitarias, contractuales, documentales, integracion y QA gate. |
| Herramientas de validacion | Validar SQL MCP, invariantes, precision y trazabilidad. |
| Plantillas Evidence Set | Exponer modelo canonico frente a instancia ejecutada. |
| Salidas persistentes | Evitar que historicos se lean como expected values. |

---

## 27. Plan de pruebas

| Tipo | Casos minimos |
|---|---|
| Unitarias | `ag:` removido; IDs sin prefijo no modificados; nulos; invalidos; duplicados; colisiones; multiples nombres; denominador cero; NULL; precision sin redondeo intermedio. |
| Contractuales | fuentes allowlisted; MCP-only; agregados lead/spend; fuente canonica; validacion source; rechazo de doble conteo; metricas permitidas/prohibidas. |
| Documentales | historicos no contractuales; `ad_name` no clave; coverage visible; `lead_only`/`spend_only` interpretados correctamente; SPEC-010/011 no reabiertas. |
| Integracion | raw join vs normalized join; full outer join; matched; lead_only; spend_only; UNKNOWN; reconciliacion monetaria y de leads. |
| QA Gate | trazabilidad MCP completa; invariantes pass; blockers resueltos o ejecucion detenida; ranking con umbrales; salida lista para downstream. |

---

## 28. Criterios de aceptacion

### AC-001

La specification no reabre la alternativa B.

### AC-002

`marts.fct_lead_enriched` queda fijada como fuente canonica y `intermediate.int_faro_lead_scoring` como validacion.

### AC-003

La frontera Evidence Acquisition / Analytical Preparation / Evidence Set Construction queda cerrada.

### AC-004

`ad_id_norm`, normalizacion `ag:` y prohibicion de `ad_name` como clave quedan formalizados.

### AC-005

Los cuatro coverage states quedan definidos con metricas soportadas y limitaciones.

### AC-006

Los universos economicos y metricas quedan nombrados sin ambiguedad.

### AC-007

`commercial_spend_per_matched_lead_observed` queda clasificada como diagnostica.

### AC-008

Precision, invariantes, blockers, trazabilidad y plan de pruebas quedan definidos.

### AC-009

La specification distingue modelo canonico de Evidence Set ejecutado.

### AC-010

El artefacto puede entregarse al Tasks Planner Agent para planificar la iteracion post-cierre separada.

---

## 29. Riesgos

| Risk | Impact | Mitigacion |
|---|---|---|
| Contratos antiguos contradicen el modelo canonico | Alto | Tratar handoffs antiguos como antecedentes a alinear, no como norma vigente. |
| Tolerancias lead-source no cerradas | Alto | Mantener como parametro experimental y bloquear produccion final sin validacion. |
| Ranking con muestras bajas | Medio | Aplicar umbrales y `sample_insufficient`. |
| Confundir diagnostico con KPI | Alto | Clasificar `commercial_spend_per_matched_lead_observed` como diagnostico. |
| Sobreleer `ad_name` como creatividad causal | Alto | Prohibir causalidad creativa sin metadata suficiente. |

---

## 30. Dependencias

- `docs/decisions/auc-001/auc-001-canonical-cost-quality-model-architectural-decision.md`;
- `analytical_use_cases/auc-001/analytical-contract.md`;
- `docs/contracts/data.contract.md`;
- `docs/contracts/evidence.contract.md`;
- `docs/contracts/context.contract.md`;
- `docs/contracts/presentation.contract.md`;
- `.github/skills/meta-lead-quality-analysis/SKILL.md`;
- `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`;
- `.github/skills/meta-lead-quality-analysis/CHECKLIST.md`;
- `.github/skills/meta-lead-quality-analysis/ANALYTICAL_PROFILE.md`;
- `docs/handoffs/auc-001-analytical-preparation.md`;
- `docs/handoffs/auc-001-evidence-acquisition.md`;
- `docs/handoffs/auc-001-evidence-set.md`;
- `specs/spec-010-presentation-projection-selection.md`;
- `specs/spec-011-communication-context-representation-transformation.md`.

---

## 31. Gate de implementacion

La implementacion solo puede autorizarse cuando:

- esta specification haya sido revisada por Reviewer Agent como evolucion post-cierre;
- Tasks Planner Agent haya creado tareas trazables;
- los cambios documentales requeridos esten planificados;
- exista configuracion documentada de umbrales;
- la tolerancia de validacion lead-source este validada o marcada como blocker;
- QA Gate Agent pueda verificar MCP-only, invariantes, precision, blockers y no modificacion de Foundation.

---

## 32. Siguiente paso SDD

Siguiente agente recomendado: **Reviewer Agent**.

Instruccion recomendada:

```text
Trabaja en `vca-ai` sobre la rama `auc-001-doc-restructuring`. Usa el Reviewer Agent para revisar `specs/spec-012-auc-001-canonical-cost-quality-model.md`. Verifica que no reabre la alternativa B, que no modifica AIF Foundation, que formaliza fuente canonica, frontera runtime, metricas, invariantes, blockers, trazabilidad y plan de pruebas, y que puede pasar al Tasks Planner Agent sin implementar ni generar informe.
```

---

## Cross-Artifact Impact Analysis

| Artefacto | Impacto detectado | Accion propuesta |
|---|---|---|
| Project Brief | Sin cambio requerido. | Mantener. |
| README | Puede requerir referencia futura si SPEC-012 se vuelve capacidad activa de AUC-001. | Diferir. |
| Context References | Debe incorporar SPEC-012 y ARCH-004 como decision/spec vigente de AUC-001. | Planificar en implementacion documental. |
| SPEC-010 / SPEC-011 | Compatibles; no se reabren. | Mantener sin cambios. |
| AUC-001 Analytical Contract | Requiere alineacion. | Planificar. |
| AUC-001 Data Contract | Requiere alineacion MCP-only y agregados separados. | Planificar. |
| AUC-001 Evidence Contract | Requiere actualizar universos, metrics, UNKNOWNs e invariantes. | Planificar. |
| Runbook / Checklist | Requieren checks nuevos. | Planificar. |
| Agents / Skills | Specification Agent usado; Skill puede requerir ajuste solo si cambia el Runbook. | Revisar en tarea posterior. |
| Glossary | Puede requerir terminos `ad_id_norm`, coverage states y modelo canonico. | Diferir a Documentation Agent. |

---

## Open Questions

- Tolerancias numericas definitivas para validacion entre `marts.fct_lead_enriched` e `intermediate.int_faro_lead_scoring`.
- Ubicacion final de `thresholds_config` para rankings experimentales.
- Namespace de persistencia de outputs post-cierre: resuelto como `outputs/auc-001/pci-001/2026-06-30/`.

Estas preguntas no reabren la arquitectura. Bloquean produccion final o implementacion completa cuando afecten a readiness.

---

## Future Considerations

- Evaluar si el modelo debe materializarse como mart BigQuery solo despues de validacion experimental.
- Evaluar si los umbrales de ranking pueden generalizarse fuera de AUC-001.
- Evaluar si aparece metadata creativa suficiente para soportar analisis de asset/formato sin depender de `ad_name`.

---

## Related Artifacts

| Artifact | Relationship |
|---|---|
| `VCA-AUC-001-ARCH-004` | Decision arquitectonica fuente. |
| `ad_quality_spend_model` handoffs | Antecedente historico a alinear. |
| BigQuery MCP discover_metadata Contract | Control de Data Provider MCP. |
| SPEC-001 | Lifecycle. |
| SPEC-002 | Boundaries. |
| SPEC-004 | Contracts. |
| SPEC-010 / SPEC-011 | Compatibilidad de Presentation posterior. |

---

## Definition of Done

Esta specification esta completa cuando:

- objetivo, alcance y exclusiones estan definidos;
- fuentes, workflow, grano, normalizacion y coverage states estan definidos;
- universos, metricas, precision, invariantes y blockers son verificables;
- trazabilidad y pruebas estan especificadas;
- impacto documental esta identificado;
- no se implementa nada;
- no se modifica AIF Foundation;
- queda lista para Reviewer Agent y despues Tasks Planner Agent.
