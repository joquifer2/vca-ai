# AUC-001 SPEC-016 - MCP Multi-table Query Gap

## Estado

Open - provider/runtime behavior gap, not blocking SPEC-016.

## Fecha

2026-07-22

## Contexto

Durante la prueba real end-to-end de aceptacion AUC-001 post-P04 se registraron intentos de consulta MCP multi-tabla que terminaron en `ERR_SCOPE_DENIED`.

Las tablas individuales estaban dentro del alcance autorizado, pero la forma de consulta multi-tabla no produjo evidencia utilizable.

## Decision

SPEC-016 no intenta resolver este comportamiento modificando el servidor, el Data Contract, el allowlist o las fuentes.

La estrategia canonica de AUC-001 pasa a ser:

* consultas MCP independientes por tabla autorizada;
* reconciliacion local controlada;
* preservacion explicita de `matched`, `lead_only` y `spend_only`;
* registro de cualquier intento multi-tabla como rechazado, descartado o diagnostico no-evidencial;
* prohibicion de usar consultas rechazadas como Evidence.

## Gap

No existe todavia una decision tecnica documentada del proveedor MCP que garantice semantica de autorizacion para consultas multi-tabla.

Hasta que exista esa garantia, AUC-001 no debe depender de consultas multi-tabla MCP para generar Evidence.

## Condicion de cierre futura

El gap podra cerrarse solo si:

* el BigQuery MCP Server documenta oficialmente soporte y limites de consultas multi-tabla;
* el Data Contract autoriza explicitamente esa forma;
* el preflight MCP puede verificar la forma antes de adquirir evidencia;
* las validaciones de SPEC-016 demuestran que el resultado no rompe grano, coverage ni reconciliacion.

## Relacion contractual

Este gap no modifica:

* SPEC-014;
* SPEC-015;
* fuentes autorizadas;
* outputs historicos;
* BigQuery MCP Server.

