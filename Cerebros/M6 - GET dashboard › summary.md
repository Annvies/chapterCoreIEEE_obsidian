---
type: endpoint
modulo: 6
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/dashboard/dashboard.controller.ts
actualizado: 2026-10-30
aliases:
  - "GET /dashboard/summary"
tags:
  - chaptercore
  - modulo-6
  - endpoint
---

# M6 - GET dashboard › summary

[[M6 - API]] · [[Cerebro 6 - Feedback y KPIs]]

> [!abstract] Endpoint
> `GET /dashboard/summary` · acceso: Dashboard · Ver.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/dashboard/summary` |
| Acceso | Dashboard · Ver |
| Controlador | `backendChapterCoreIEEE/src/dashboard/dashboard.controller.ts` → `summary()` |

### Entradas

- Query  → `DashboardQueryDto`
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `DashboardService.summary()`

### Consumido por el frontend

- [[M6 - Cliente API dashboard]]

## Enlaces

- [[M6 - dashboard.service]]
- [[M6 - DTO DashboardQueryDto]]
- [[M6 - Cliente API dashboard]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
