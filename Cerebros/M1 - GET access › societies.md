---
type: endpoint
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/controllers/access.controller.ts
actualizado: 2026-10-30
aliases:
  - "GET /access/societies"
tags:
  - chaptercore
  - modulo-1
  - endpoint
---

# M1 - GET access › societies

[[M1 - API]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Endpoint
> Mismo catálogo público, para que cualquier persona elija sus sociedades IEEE.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/access/societies` |
| Acceso | Sesión iniciada |
| Controlador | `backendChapterCoreIEEE/src/auth/controllers/access.controller.ts` → `societies()` |

### Lógica que invoca

- `AccessService.listChapters()`

### Consumido por el frontend

- [[M1 - Cliente API auth]]

## Enlaces

- [[M1 - access.service]]
- [[M1 - Cliente API auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
