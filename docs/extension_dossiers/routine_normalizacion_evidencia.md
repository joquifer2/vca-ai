# Dossier de Compatibilidad de Extensiones

## Propósito

Este documento describe la compatibilidad y reutilizabilidad de la rutina de normalización de evidencia en la Foundation.

Su objetivo es registrar, de forma documental y reutilizable, si la rutina puede considerarse compatible con el núcleo metodológico y en qué contextos puede reutilizarse sin alterar la secuencia común.

Este documento no define implementación técnica.

Este documento no aprueba despliegues operativos.

Este documento no sustituye la revisión humana.

---

## Información General

| Campo | Valor |
|---|---|
| Nombre de la extensión | Rutina de Normalización de Evidencia |
| ID de la extensión | ROUTINE-NORMALIZACION-EVIDENCIA-001 |
| Categoría de la extensión | Rutina |
| Repositorio | aif-foundation |
| Última actualización | 2026-07-10 |
| Propietario | Foundation maintainers |
| Revisor | PENDIENTE |

---

## Resumen Ejecutivo

La rutina de normalización de evidencia se evalúa como una candidata razonable para compatibilidad y reutilización porque opera sobre el tratamiento documental de hallazgos, sin imponer dominio, tecnología ni cambios al ciclo fundacional.

El resultado general de esta revisión es preliminarmente favorable, con la condición de que su uso se mantenga limitado a la estructuración de evidencia y no reemplace el razonamiento ni la aprobación documental.

---

## Perfil de la Extensión

### Propósito

Normalizar evidencia observada para hacerla legible, trazable y utilizable por evaluaciones, gates y revisiones documentales.

### Superficie del núcleo

La rutina amplifica la superficie de evidencia y preparación documental dentro del ciclo analítico, especialmente en la transición entre análisis y razonamiento.

### Fases compatibles

Contexto, Discovery, Preparación, Análisis y Razonamiento.

### Impacto en la superficie del sistema

Estructura la evidencia sin introducir reglas nuevas de negocio ni alterar la secuencia metodológica común.

### Propuesta de valor

Facilita que distintos equipos produzcan evidencia comparable, revisable y trazable con menor ambigüedad documental.

---

## Metadata mínima

| Campo | Valor |
|---|---|
| Nombre de la extensión | Rutina de Normalización de Evidencia |
| ID de la extensión | ROUTINE-NORMALIZACION-EVIDENCIA-001 |
| Categoría de la extensión | Routine |
| Superficie del núcleo | Evidencia y preparación documental |
| Propósito | Normalizar evidencia observada para su consumo por evaluaciones y gates |
| Fases compatibles | Contexto, Discovery, Preparación, Análisis, Razonamiento |
| Contracts requeridos | Context Contract, Data Contract, Evidence Contract |
| Contracts producidos | Evidence Contract, Knowledge Contract |
| Dependencias permitidas | Context refs, specs fundacionales, evaluaciones documentales |
| Dependencias prohibidas | Runtime obligatorio, proveedor único, lógica de dominio cerrada |
| Declaración de compatibilidad | Compatible con el núcleo metodológico mientras preserve trazabilidad y no altere fases |
| Declaración de reutilización | Reutilizable en más de un caso de uso de análisis y revisión documental |
| Enlaces de evidencia | [specs/spec-001-analytical-lifecycle.md](../../specs/spec-001-analytical-lifecycle.md); [specs/spec-004-transversal-contracts.md](../../specs/spec-004-transversal-contracts.md); [specs/spec-005-readiness-gates.md](../../specs/spec-005-readiness-gates.md); [specs/spec-006-documentary-evaluations.md](../../specs/spec-006-documentary-evaluations.md); [specs/spec-007-extension-compatibility-reusability.md](../../specs/spec-007-extension-compatibility-reusability.md) |
| Indeterminaciones | Alcance exacto de estandarización por dominio; criterios de versionado futuro |

---

## Perfil de Compatibilidad

### Compatibilidad con el núcleo

La rutina es compatible con el núcleo cuando se limita a organizar evidencia observada y no introduce nuevas fases, decisiones automáticas ni dependencias operativas.

### Responsabilidades que respeta

- respeta la separación entre evidencia y conclusión;
- respeta la responsabilidad del reasoning sobre la interpretación;
- respeta la responsabilidad del reviewer y del QA Gate Agent sobre la aprobación documental.

### Responsabilidades que no reasigna

- no reasigna el rol del Framework;
- no sustituye el razonamiento;
- no sustituye la evaluación humana;
- no sustituye gates ni evaluaciones.

### Dependencias permitidas

- context refs oficiales;
- specs fundacionales;
- contracts transversales;
- evaluaciones documentales.

### Dependencias prohibidas

- runtime productivo obligatorio;
- proveedor único;
- herramienta concreta como requisito fundacional;
- conocimiento de dominio cerrado no documentado.

### Neutralidad tecnológica

La rutina es tecnológicamente neutra porque describe una forma documental de normalizar evidencia, no una implementación.

### Gestión de unknowns

Los huecos de definición futura deben marcarse como UNKNOWN hasta que exista evidencia documental verificable.

---

## Perfil de Reutilización

### Casos de uso plausibles

- normalización de hallazgos en una evaluation documental;
- preparación de evidence sets para gates;
- homogeneización de notas de revisión entre equipos;
- estructuración de evidencia previa a recomendaciones.

### Motivo de reutilización

La rutina resuelve un problema transversal: convertir evidencia heterogénea en material documental comparable y trazable.

### Contextos en los que sí debe reutilizarse

- cuando se necesite reducir ambigüedad documental;
- cuando exista un evidence set con formatos inconsistentes;
- cuando la revisión de gates requiera evidencia homogénea.

### Contextos en los que no debe reutilizarse

- cuando el objetivo sea introducir nueva lógica de dominio;
- cuando la rutina pretenda sustituir el razonamiento;
- cuando se quiera usar como mecanismo operativo de ejecución.

### Abstracción mínima necesaria

La rutina debe permanecer centrada en la forma documental de la evidencia, no en el contenido específico de un dominio.

---

## Requisitos de Revisión

### Revisión de entradas

Verificar que las entradas son observaciones, hallazgos o evidencias documentales y no conclusiones ya cerradas.

### Revisión de salidas

Verificar que las salidas mantienen separada la evidencia de la interpretación.

### Revisión de trazabilidad

Verificar que cada bloque de evidencia puede rastrearse hasta su fuente o artefacto relacionado.

### Revisión de restricciones

Verificar que la rutina no incorpora dependencias operativas, dominio cerrado ni cambios de fase.

### Revisión de riesgos

Verificar que la rutina no se usa para justificar conclusiones sin respaldo documental.

---

## Resumen de Revisión

### Hallazgos

- La rutina encaja con el modelo de extensibilidad de la Foundation.
- La utilidad principal es documental y transversal.
- La dependencia con el núcleo es baja y controlable.

### Huecos

- Falta definir criterios de estandarización por tipo de evidencia.
- Falta definir si existirán variantes específicas por dominio derivado.

### Riesgos

- Convertir la rutina en una regla rígida que reduzca flexibilidad documental.
- Usarla como sustituto del juicio humano.

### Recomendaciones

- Aprobarla como candidata reusable con alcance documental.
- Mantenerla acotada a normalización de evidencia.
- Revisarla de nuevo cuando exista una primera instancia de uso real en un proyecto derivado.

### Decisión documental

Pass with minor conditions

---

## Evidencia

Referencias a specs, gates, evaluaciones, context refs u otros artefactos que justifican la declaración de compatibilidad o reutilización.

---

## Riesgos

| Riesgo | Impacto | Notas |
| --- | --- | --- |
| Usar la rutina como sustituto del razonamiento | Alto | Debilita la metodología común |
| Introducir dependencias operativas | Alto | Rompe el alcance documental |
| Fijar una taxonomía demasiado rígida | Medio | Reduce reutilización entre proyectos derivados |

---

## Preguntas Abiertas

- qué taxonomía mínima de evidencia conviene estandarizar primero;
- si la rutina debe variar según el tipo de contract o gate;
- qué criterio formal se usará para versionar futuras variantes.

---

## Siguiente Paso Recomendado

Seleccionar uno:

- Agente revisor
- Agente de QA Gate
- Agente de documentación
- Agente de especificación

Agente recomendado:

Agente revisor

Motivo:

La rutina ya está suficientemente acotada para revisión documental; conviene validar si la declaración de compatibilidad y reutilización se sostiene sin introducir exceso de alcance.

---

## Definition of Done

El dossier está completo cuando:

- la extensión está identificada;
- la compatibilidad está declarada;
- la reutilización está declarada;
- la metadata mínima está completa;
- las dependencias relevantes están documentadas;
- los unknowns están declarados;
- la trazabilidad está documentada;
- existen criterios claros para la decisión documental.