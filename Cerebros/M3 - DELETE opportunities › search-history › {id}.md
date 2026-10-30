---
type: endpoint
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/discovery.controller.ts
actualizado: 2026-10-30
aliases:
  - "DELETE /opportunities/search-history/:id"
tags:
  - chaptercore
  - modulo-3
  - endpoint
---

# M3 - DELETE opportunities › search-history › {id}

[[M3 - API]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Endpoint
> `DELETE /opportunities/search-history/:id` · acceso: Oportunidades · Ver.

| Campo | Valor |
|---|---|
| Método | `DELETE` |
| Ruta | `/opportunities/search-history/:id` |
| Acceso | Oportunidades · Ver |
| Controlador | `backendChapterCoreIEEE/src/opportunities/discovery/discovery.controller.ts` → `removeEntry()` |
| Respuesta | `NO_CONTENT` |
| Devuelve | `Promise<void>` |

### Entradas

- Parámetro de ruta `id` (UUID)
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `SearchHistoryService.remove()`

> [!note] Comentario del controlador
> Búsqueda en fuentes oficiales IEEE e historial (spec 002, contracts/api-rest.md). Cualquier persona con sesión (nivel Ver, RF-315); «Extraer ficha» y «Publicar» siguen exigiendo Editar.

### Consumido por el frontend

- [[M3 - Cliente API opportunities]]

## Enlaces

- [[M3 - search-history.service]]
- [[M3 - Cliente API opportunities]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
