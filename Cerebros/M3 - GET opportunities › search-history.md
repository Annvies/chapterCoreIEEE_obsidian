---
type: endpoint
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/discovery.controller.ts
actualizado: 2026-10-30
aliases:
  - "GET /opportunities/search-history"
tags:
  - chaptercore
  - modulo-3
  - endpoint
---

# M3 - GET opportunities › search-history

[[M3 - API]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Endpoint
> `GET /opportunities/search-history` · acceso: Oportunidades · Ver.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/opportunities/search-history` |
| Acceso | Oportunidades · Ver |
| Controlador | `backendChapterCoreIEEE/src/opportunities/discovery/discovery.controller.ts` → `listHistory()` |
| Devuelve | `Promise<SearchHistoryEntry[]>` |

### Entradas

- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `SearchHistoryService.list()`

> [!note] Comentario del controlador
> Búsqueda en fuentes oficiales IEEE e historial (spec 002, contracts/api-rest.md). Cualquier persona con sesión (nivel Ver, RF-315); «Extraer ficha» y «Publicar» siguen exigiendo Editar.

### Consumido por el frontend

- [[M3 - Cliente API opportunities]]

## Enlaces

- [[M3 - search-history.service]]
- [[M3 - Cliente API opportunities]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
