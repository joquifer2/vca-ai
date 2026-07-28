# Repository Governance Guide

Estado: Draft inicial.

Tipo de artefacto: Guia de gobernanza documental.

Estructura: Inferida. No existe template especifico para guia de gobernanza de repositorio en `docs/templates/`.

Fecha: 2026-07-28

Revision requerida: Reviewer Agent y QA Gate Agent.

---

## 1. Proposito

Esta guia inicial describe criterios de mantenimiento documental para `VCA IA`.

No crea reglas de precedencia nuevas. La precedencia documental general debe consultarse exclusivamente en `.github/instructions/sdd.instructions.md`.

---

## 2. Principios de mantenimiento

- Mantener cada documento ligado a una funcion clara.
- Separar decision, explicacion, evaluacion, task plan y output.
- Marcar estados honestos: inicial, draft, candidato, vigente o historico.
- Evitar declarar `PASS`, baseline definitivo o cierre final sin Reviewer/QA.
- Evitar duplicar contenido canonico de specs, contracts, gates o context refs.
- Registrar propuestas futuras como no canonicas hasta decision formal.
- No convertir gobernanza documental en runtime ni automatizacion.

---

## 3. Creacion de documentos

Antes de crear un documento:

1. Revisar `docs/context_refs.md` cuando aplique por tipo de artefacto.
2. Revisar templates en `docs/templates/`.
3. Confirmar si el artefacto ya existe.
4. Definir audiencia, objetivo y alcance.
5. Declarar estado real del documento.

Si no existe template compatible, puede usarse estructura inferida y debe indicarse en el propio documento.

---

## 4. Cambios documentales permitidos

En una iteracion estrictamente documental se permite:

- crear indices, inventarios, guias y taxonomias;
- corregir enlaces, nombres o clasificaciones documentales;
- alinear estados documentales con gates existentes;
- documentar restricciones ya acordadas;
- preparar handoffs o paquetes para revision.

No se permite:

- implementar codigo;
- modificar logica funcional;
- modificar contratos operativos sin autorizacion explicita;
- mover archivos existentes sin autorizacion explicita;
- alterar outputs reales;
- usar outputs historicos como fuente analitica;
- declarar decisiones funcionales nuevas por iniciativa documental.

---

## 5. Evaluaciones y documentos historicos

Las reglas de clasificacion dentro de `docs/evaluations/` son locales a ese arbol. Sirven para ordenar investigations, experiments, validations, diagnostics e historical.

Estas reglas locales no redefinen la precedencia general del repositorio.

---

## 6. Areas protegidas

Las siguientes areas requieren autorizacion explicita y no forman parte de una consolidacion documental transversal ordinaria:

- AUC-001 operativo.
- Contratos AUC-001.
- Runtime.
- BigQuery/MCP.
- Outputs reales.
- `outputs/auc-001/current/`.
- Outputs historicos como fuente analitica.

---

## 7. Propuestas futuras

Las propuestas como `WS-3` deben mantenerse como documentales, futuras, no ejecutables y no canonicas hasta que exista decision formal.

Una propuesta futura no autoriza por si misma:

- crear workflows ejecutables;
- introducir herramientas reales;
- modificar runtime;
- modificar contratos;
- cambiar estado de cierre o QA.

---

## 8. Definition of Done documental

Una actualizacion documental esta lista para revision cuando:

- el objetivo del cambio es claro;
- el estado del artefacto es honesto;
- no hay duplicacion canonica evidente;
- las referencias cruzadas necesarias existen;
- las restricciones aplicables estan visibles;
- el paquete puede ser revisado por Reviewer Agent.

La actualizacion solo puede considerarse cerrada cuando el gate correspondiente lo valide o cuando el responsable humano acepte explicitamente el cierre documental.