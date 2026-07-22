# AUC-001 P03 Executive Report - Revision

## Mensaje principal

Meta no parece estar fallando por coste ni por falta de volumen. El reto es desplazar el mix hacia leads con intencion clara sin perder la escala que ya funciona.

La senal que mas separa calidad es la intencion declarada: billetes o estado equivalente. La estructura actual da volumen y coste matched controlado, pero depende de pocos activos y la cobertura parcial impide tomar decisiones economicas definitivas sobre todo el sistema.

## Lectura para Direccion

La decision prudente no es mover presupuesto de forma agresiva. Es proteger la base dominante, probar pre-cualificacion por intencion, auditar los huecos `lead_only` y `spend_only`, y diversificar mensajes con control.

## Senales que explican la calidad

| Senal | Que indica | Uso recomendado | Limite |
| --- | --- | --- | --- |
| Intencion/billetes | Separa calidad con claridad. | Base para experimento de pre-cualificacion. | Asociacion, no causalidad ni venta. |
| Matched cost-quality | El coste observado esta controlado en el universo matched. | Referencia economica principal. | No extrapolar a `lead_only` o `spend_only`. |
| Concentracion de activos | Pocos anuncios y estructuras sostienen escala. | Diversificar con tests pequenos. | No declara ganador creativo. |
| Temporalidad lead-side | No hay deterioro claro de calidad. | Monitorizar, no sobrerreaccionar. | Coste temporal parcial. |

## Recomendaciones y criterio de exito

| Recomendacion | Tipo | Criterio de exito |
| --- | --- | --- |
| Test de pre-cualificacion por intencion/billetes. | Experimento medible | Mejorar tasa A/B con muestra matched suficiente y sin empeorar materialmente coste por A/B matched. |
| Auditar `lead_only` y `spend_only`. | Accion verificable | Cada caso no matched queda clasificado con causa o `UNKNOWN` explicito. |
| Diversificar creatividades/mensajes con tracking por `ad_id_norm`. | Experimento medible | Un activo no dominante alcanza muestra suficiente con calidad comparable o mejor y coste aceptable. |
| Mantener julio como hipotesis, no conclusion. | Hipotesis no accionable | Solo promover si un periodo completo y comparable valida la mejora. |

## Limites que siguen abiertos

- No hay revenue/CRM reconciliado.
- No hay causalidad creativa validada.
- No hay metadata creativa adicional mas alla de `ad_name`.
- La temporalidad coste-calidad sigue limitada por proveedor.

## Idea para recordar

El coste esta bajo control en el universo matched; el valor esta en ensenar a Meta a comprar mas intencion, no simplemente mas formularios.
