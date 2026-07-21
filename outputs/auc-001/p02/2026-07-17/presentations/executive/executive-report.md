# AUC-001 P02 Executive Report

## Mensaje Principal

Meta está generando volumen a coste observado bajo, pero el valor real depende de mover el mix hacia leads con intención clara. El coste no parece el problema principal en el universo matched; el reto es comprar más calidad sin perder escala.

## Cifras Clave

- Periodo: `2026-04-18` a `2026-07-17`.
- Leads: 1.549.
- Leads A/B: 469, un 30,28%.
- Tier A: 67, un 4,33%.
- Universo matched: 1.362 leads y 1.069,05 EUR de spend comercial.
- Coste por lead A/B matched: 2,70 EUR.

## Lo Que Más Importa

La señal de intención separa mucho la calidad: los leads con billetes alcanzan 89,45% A/B, frente a 20,59% en los que no tienen billetes. Esta diferencia no debe leerse como causalidad, pero sí como una señal fuerte para orientar tests.

La captación está concentrada. Una estructura principal y pocos anuncios sostienen la mayoría del volumen. Eso da escala, pero también crea dependencia.

## Decisiones Recomendadas

1. Ejecutar un experimento medible de pre-cualificación por intención o billetes.
2. Auditar los casos `lead_only` y `spend_only` antes de tomar decisiones económicas sobre esos grupos.
3. Probar diversificación creativa controlada, usando `ad_id_norm` como trazabilidad.
4. Mantener la mejora parcial de julio como hipótesis, no como conclusión.

## Límites Para Dirección

No hay revenue o ventas reconciliadas. No hay causalidad creativa. La lectura temporal de coste-calidad es parcial porque las consultas de spend temporal fueron rechazadas por política del proveedor. `lead_only` no significa gratis y `spend_only` no significa cero leads.

## Idea Para Recordar

El coste parece controlado; el valor está en desplazar el mix hacia intención cualificada, no en celebrar volumen bruto.
