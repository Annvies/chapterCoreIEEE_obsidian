---
type: migración
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792368000000-CreateOpportunities.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - migración
---

# M3 - Migración CreateOpportunities

[[M3 - Base de datos]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Migración
> Tablas del módulo de oportunidades (CONTEXTO.md §7, mockup 05). La allowlist de dominios de fuente_url/enlace se valida en NestJS: varios sitios oficiales verificados no están bajo ieee.org (p. ej. computer.org, comsoc.org).

| Campo | Valor |
|---|---|
| Archivo | `1792368000000-CreateOpportunities.ts` |
| Marca de tiempo | `1792368000000` (orden de ejecución) |
| Reversible | sí, tiene `down()` |

### Qué hace

- Tipo enumerado `opportunity_type`
- Tipo enumerado `opportunity_status`
- Crea la tabla `ieee_societies`
- Crea la tabla `opportunities`
- Índice `opportunities_society_id_idx` en `opportunities`
- Índice `opportunities_publicadas_fecha_idx` en `opportunities`
- Inserta datos iniciales en `ieee_societies`

## Enlaces

- [[M3 - Tabla opportunities]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
