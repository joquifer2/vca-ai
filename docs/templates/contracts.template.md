# Contracts Template

## Propósito

Este documento describe los contratos funcionales y técnicos existentes dentro del sistema.

Su objetivo es identificar interfaces estables entre componentes para permitir evolución controlada sin romper dependencias existentes.

Un contrato define:

- qué produce un componente;
- qué consume otro componente;
- qué estructura se espera;
- qué comportamiento debe mantenerse estable.

No pretende documentar implementaciones internas.

No pretende documentar lógica de negocio completa.

No pretende documentar arquitectura.

Para ello existen otros artefactos especializados.

---

# Información General

| Campo | Valor |
|---|---|
| Project Name | |
| Repository | |
| Last Updated | |
| Owner | |

---

# Resumen Ejecutivo

Describir brevemente:

- qué contratos existen;
- qué componentes dependen de ellos;
- cuáles son críticos para la operación del sistema.

---

# Contratos Identificados

| Contract ID | Nombre | Categoria Fundacional | Estado |
|---|---|---|---|
| | | | |

Estado:

- Documented
- Inferred
- Missing
- Unknown

---

# Contract Detail

## Contract ID

### Nombre

### Categoria Fundacional

- Context Contract
- Data Contract
- Discovery Contract
- Analytical Contract
- Evidence Contract
- Knowledge Contract
- Recommendation Contract
- Presentation Contract
- Extension Contract
- Unknown

### Tipo

- API
- Webhook
- Dataset
- Table
- dbt Model
- Event
- Message
- File
- Unknown

### Producer

Componente que genera el contrato.

### Consumer

Componente que consume el contrato.

### Propósito

Descripción funcional.

### Input

Datos esperados.

### Output

Datos producidos.

### Campos Críticos

| Campo | Obligatorio | Descripción |
|---|---|---|
| | | |

### Reglas de Validación

| Regla | Descripción |
|---|---|
| | | |

### Trazabilidad

Referencias a evidencia, conocimiento, specs u otros artefactos que justifican el contenido del contrato.

### Unknown Handling

Documentar huecos, limitaciones o estados UNKNOWN que afecten al contrato.

### Reglas de Idempotencia

Documentar mecanismos de deduplicación o control de repetición.

### Dependencias

| Dependencia | Tipo |
|---|---|
| | |

### Evidencia

Referencias observadas en el sistema.

### Riesgos

Riesgos asociados al contrato.

---

# Contratos de Datos

Documentar contratos basados en datos.

| Producer | Consumer | Objeto | Estado |
|---|---|---|---|
| | | | |

Ejemplos:

- BigQuery Table
- dbt Model
- Dataset
- CSV Export

---

# Contratos de Integración

Documentar contratos API o Webhook.

| Producer | Consumer | Endpoint / Event | Estado |
|---|---|---|---|
| | | | |

---

# Contratos de Eventos

Documentar eventos utilizados por el sistema.

| Event | Producer | Consumer | Estado |
|---|---|---|---|
| | | | |

---

# Contratos Críticos

Documentar contratos cuya ruptura tendría alto impacto.

| Contrato | Impacto | Evidencia |
|---|---|---|
| | | |

---

# Riesgos de Contratos

| Riesgo | Severidad | Impacto | Evidencia |
|---|---|---|---|
| | | | |

Severidad:

- Critical
- Important
- Minor

---

# Unknowns

| Unknown | Impacto | Validación requerida |
|---|---|---|
| | | |

---

# Artefactos Relacionados

- system_overview.md
- architecture_as_is.md
- data_lineage.md
- retrospective_spec.md
- sdd_readiness_assessment.md

---

# Definition of Done

Este documento está completo cuando permite responder:

1. ¿Qué contratos existen?
2. ¿Quién produce cada contrato?
3. ¿Quién consume cada contrato?
4. ¿Qué campos son críticos?
5. ¿Qué validaciones existen?
6. ¿Qué reglas de idempotencia existen?
7. ¿Qué contratos son críticos?
8. ¿Qué riesgos existen?
9. ¿Qué información sigue siendo desconocida?

---

# Notas

Este documento debe centrarse en interfaces estables.

Las implementaciones internas deben documentarse en otros artefactos.
