---
type: concepto
modulo: 3
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792972800000-CreateOpportunitySearchHistory.ts
  - backendChapterCoreIEEE/src/opportunities/discovery/search-history.service.ts
  - backendChapterCoreIEEE/src/opportunities/discovery/discovery.controller.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - concepto
---

# M3 - Historial de búsquedas

[[M3 - Descubrimiento]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Qué es
> Cada [[M3 - Búsqueda en fuentes oficiales]] se guarda en la tabla
> `opportunity_searches` para que la persona que buscó pueda volver a verla.

> [!info] Confirmado en el código
> - Columnas: `user_id` (borrado en cascada con la persona), `consulta` (1–200
>   caracteres), `estrategia` (`discovery_strategy`), `forzada`, `intentos` y
>   `resultados` (JSON, como máximo 20 resultados) y `created_at`.
> - Se conservan las **50** búsquedas más recientes por persona (`MAX_HISTORY`); la poda
>   la hace `SearchHistoryService`.
> - El texto buscado es **dato personal**: solo lo ve y lo borra quien buscó
>   (`GET /opportunities/search-history`, `DELETE /opportunities/search-history/:id` y
>   `DELETE /opportunities/search-history`).

## Enlaces

- Forma parte de [[M3 - Descubrimiento]].
- Relacionada con [[M3 - Búsqueda en fuentes oficiales]], [[M3 - Modelo de datos opportunities]].

## Fuentes

- `backendChapterCoreIEEE/src/database/migrations/1792972800000-CreateOpportunitySearchHistory.ts`
- `backendChapterCoreIEEE/src/opportunities/discovery/search-history.service.ts`
- `backendChapterCoreIEEE/src/opportunities/discovery/discovery.controller.ts`
