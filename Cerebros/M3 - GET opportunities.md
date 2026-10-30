---
type: endpoint
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/opportunities.controller.ts
actualizado: 2026-10-29
aliases:
  - "GET /opportunities"
tags:
  - chaptercore
  - modulo-3
  - endpoint
---

# M3 - GET opportunities

[[M3 - API]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Endpoint
> `GET /opportunities` · acceso: Oportunidades · Ver.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/opportunities` |
| Acceso | Oportunidades · Ver |
| Controlador | `backendChapterCoreIEEE/src/opportunities/opportunities.controller.ts` → `search()` |
| Devuelve | `Promise<OpportunityView[]>` |

### Entradas

- Query  → `SearchOpportunitiesQueryDto`

### Lógica que invoca

- `OpportunitiesService.search()`

> [!note] Comentario del controlador
> Los guards globales del Módulo 1 exigen sesión y permiso; ver es para todos los niveles y extraer/publicar exige Editar (CONTEXTO.md §7). El límite de peticiones se mantiene.

### Consumido por el frontend

- [[M3 - Cliente API opportunities]]

## Enlaces

- [[M3 - opportunities.service]]
- [[M3 - DTO SearchOpportunitiesQueryDto]]
- [[M3 - Cliente API opportunities]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
