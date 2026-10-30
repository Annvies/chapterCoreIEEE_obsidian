---
type: migración
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792972800000-CreateOpportunitySearchHistory.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - migración
---

# M3 - Migración CreateOpportunitySearchHistory

[[M3 - Base de datos]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Migración
> Spec 002 (Módulo 3): historial de búsquedas en fuentes oficiales IEEE por persona (data-model.md). Depende de users (Módulo 1). Guarda como máximo 20 resultados por búsqueda; la poda a las 50 búsquedas más recientes la hace SearchHistoryService. Ciclo 2 (T047, C1): el enum incluye busqueda_sitio y catalogo, y la marca de tiempo es posterior a las migraciones de main (1792886400000, CreateExpensesModule) porque esta aún no está en producción.

| Campo | Valor |
|---|---|
| Archivo | `1792972800000-CreateOpportunitySearchHistory.ts` |
| Marca de tiempo | `1792972800000` (orden de ejecución) |
| Reversible | sí, tiene `down()` |

### Qué hace

- Extensión `pgcrypto`
- Tipo enumerado `discovery_strategy`
- Crea la tabla `opportunity_searches`
- Índice `opportunity_searches_user_created_idx` en `opportunity_searches`

## Enlaces

- [[M3 - Tabla opportunity_searches]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
