# AUC-001 P03 Analytical Report - Revision de producto

## Estado

Revision autorizada de representacion posterior a AUC-001-P03.

Este paquete no adquiere nueva evidencia, no modifica SPEC-014, no altera el paquete cerrado `outputs/auc-001/p02/2026-07-17/` y no usa outputs historicos como expected values.

La revision consume exclusivamente el producto canonico P02:

- `outputs/auc-001/p02/2026-07-17/product-core/common-product-core.json`
- `outputs/auc-001/p02/2026-07-17/evidence/evidence-set.json`
- `outputs/auc-001/p02/2026-07-17/knowledge/knowledge-set.json`
- `outputs/auc-001/p02/2026-07-17/recommendations/recommendation-set.json`
- `outputs/auc-001/p02/2026-07-17/coverage-matrix/coverage-matrix.json`

## Lectura principal reforzada

El fenomeno principal no es una falta de volumen ni una ineficiencia evidente del coste observado. VCA ya tiene una base de captacion amplia y economicamente controlada en el universo comercial matched. La tension real esta en la composicion del mix: una parte relevante del volumen cumple A/B, pero la calidad mas alta sigue siendo selectiva y aparece asociada a senales de intencion concretas.

La lectura integrada es que Meta esta aprendiendo sobre una base concentrada: pocas estructuras y pocos anuncios sostienen gran parte de la escala, mientras las senales de intencion, especialmente `ticket_status` y `tiene_billetes`, separan mejor la calidad que el volumen agregado. Por eso el problema de decision no es "comprar mas barato", sino desplazar el aprendizaje hacia intencion cualificada sin perder escala ni convertir cobertura parcial en certeza economica.

La restriccion dominante sigue siendo la cobertura. `matched`, `lead_only` y `spend_only` no son universos equivalentes; la temporalidad coste-calidad es parcial; y la lectura creativa permanece descriptiva. Estas limitaciones no bloquean el producto, pero condicionan el tipo de accion permitida: experimentos medibles y acciones verificables, no redistribuciones presupuestarias definitivas ni ganadores creativos.

## Vista integrada de senales y combinaciones

| Dimension integrada | Lectura desde P02 | Relacion con calidad | Implicacion analitica | Limite preservado |
| --- | --- | --- | --- | --- |
| Escala y calidad FARO | El nucleo comun declara 1.549 leads, 469 A/B y 67 Tier A. | Hay volumen suficiente y una base A/B relevante, pero Tier A es minoritario. | La optimizacion debe mejorar mix, no solo volumen. | FARO es proxy autorizado; revenue no esta disponible. |
| Coste-calidad matched | El universo matched contiene 1.362 leads, 396 A/B y coste A/B matched canonico. | La eficiencia observada es buena dentro de matched. | Las decisiones economicas deben apoyarse en metricas canonicas con coverage explicito. | No extrapolar a `lead_only` ni `spend_only`. |
| Intencion declarada | `tiene_billetes = true` y `ticket_status` separan calidad con mucha fuerza. | Es la senal explicativa mas clara del Knowledge Set. | La pre-cualificacion por intencion es la via mas prometedora para mejorar mix. | Asociacion observada; no causalidad ni venta cerrada. |
| Formulario/producto | DIASPORA/RTG muestra mayor calidad lead-side que la base dominante. | Sugiere calidad potencial fuera de captacion principal. | Puede explorarse como expansion controlada. | Parte de esa lectura queda `lead_only` para economia matched. |
| Campana/adset | La estructura principal concentra la escala y el spend matched derivado. | Sostiene el aprendizaje actual. | Proteger la base dominante antes de mover presupuesto. | Economics de campaign/adset son derivados desde ad-level. |
| Anuncios | Dos anuncios dominan volumen; otros mensajes muestran senales exploratorias. | Concentracion fuerte y posible dependencia. | Diversificar con tests pequenos y trazabilidad por `ad_id_norm`. | `ad_name` es etiqueta interpretativa; causalidad creativa UNKNOWN. |
| Plataforma | Facebook muestra mayor volumen y calidad observada moderadamente superior. | Diferencia asociativa, no suficiente para presupuesto. | Usar como diagnostico secundario. | Spend por plataforma no disponible en evidencia adquirida. |
| Temporalidad | Calidad mensual estable y julio parcial algo superior. | No hay deterioro claro lead-side. | Monitorizar calidad, no inferir tendencia economica completa. | Semanas parciales y spend temporal rechazado por proveedor. |

### Combinacion explicativa principal

La combinacion que mejor explica la calidad disponible en P02 es:

1. base de escala concentrada en la estructura principal;
2. eficiencia economica solo dentro del universo matched;
3. separacion fuerte por senales de intencion;
4. oportunidad exploratoria en grupos de mayor calidad lead-side;
5. limites de cobertura que impiden convertir esas oportunidades en decisiones economicas definitivas.

Esta combinacion conecta `KNW-001`, `KNW-002`, `KNW-003`, `KNW-004`, `KNW-005` y `KNW-006` sin introducir conocimiento nuevo.

## Patrones de decision

| Patron | Soporte canonico | Que permite decidir | Que no permite decidir |
| --- | --- | --- | --- |
| Escala con calidad selectiva | `KNW-001`, `FND-001` | Priorizar calidad del mix frente a volumen bruto. | No permite afirmar rentabilidad final. |
| Coste controlado en matched | `KNW-002`, `FND-002`, `FND-003` | Usar metricas matched como referencia economica aprobada. | No permite publicar CPL/CPQL genericos globales. |
| Intencion como separador | `KNW-003`, `FND-004` | Disenar experimento de pre-cualificacion. | No prueba causalidad ni conversion comercial. |
| Dependencia de pocos activos | `KNW-004`, `FND-005` | Justifica diversificacion controlada. | No declara ganadores creativos. |
| Upside parcial fuera de la base dominante | `KNW-005`, `FND-006` | Explorar RTG/DIASPORA o trafico alineado a intencion. | No autoriza reasignacion fuerte de presupuesto. |
| Calidad temporal estable | `KNW-006`, `FND-007` | Evita tratar la situacion como emergencia. | No sostiene tendencia coste-calidad completa. |

## Recomendaciones con criterio de exito visible

| ID | Tipo | Prioridad | Accion | Criterio de exito o cierre | Guardrail / limite |
| --- | --- | --- | --- | --- | --- |
| REC-001 | `measurable_experiment` | Alta | Test controlado de pre-cualificacion por intencion o billetes. | La tasa A/B mejora con muestra matched suficiente y sin deterioro material de `cost_per_ab_commercial_matched`. | Revisar si la muestra queda baja, cae la cobertura matched o empeora el coste por A/B. |
| REC-002 | `verifiable_action` | Alta | Revisar y documentar causas de `lead_only` y `spend_only`. | Cada `ad_id_norm` no matched queda clasificado como esperado, latencia, gap de mapping o `UNKNOWN` explicito. | Sin esta revision, los grupos `lead_only` no pueden leerse economicamente. |
| REC-003 | `measurable_experiment` | Media-alta | Test pequeno de diversificacion creativa/mensaje con trazabilidad por `ad_id_norm`. | Al menos un anuncio no dominante alcanza muestra suficiente con tasa A/B comparable o mejor y coste A/B aceptable. | No usar `ad_name` como clave ni declarar causalidad creativa. |
| REC-004 | `non_actionable_hypothesis` | Media | Mantener la mejora parcial de julio como hipotesis pendiente. | Promocionar solo si un periodo comparable completo valida el cambio con evidencia temporal autorizada. | Julio parcial y coste temporal incompleto impiden conclusion durable. |

## Gaps declarados que permanecen abiertos

Estos gaps se mantienen deliberadamente como limitaciones, no como objetivos de resolucion en P03:

- Revenue/CRM o conversion comercial reconciliada: `not_available`.
- Causalidad creativa: `UNKNOWN`.
- Metadata creativa adicional mas alla de `ad_name`: `not_available`.
- Temporalidad coste-calidad completa: `partial` por limites del proveedor.

## Resultado de la revision

Las condiciones internas de P03 quedan resueltas como mejora de representacion:

- la vista integrada de senales y combinaciones queda explicitada;
- la narrativa analitica queda reforzada desde Knowledge existente;
- los criterios de exito de recomendaciones quedan visibles en el informe;
- se preservan coverage states, UNKNOWNs, limitaciones y separacion de capas.

Decision preparada para revalidacion experimental: `READY FOR EXPERIMENTAL REVALIDATION`.
