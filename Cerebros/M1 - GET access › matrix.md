---
type: endpoint
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/controllers/access.controller.ts
actualizado: 2026-10-30
aliases:
  - "GET /access/matrix"
tags:
  - chaptercore
  - modulo-1
  - endpoint
---

# M1 - GET access › matrix

[[M1 - API]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Endpoint
> Matriz de permisos vigente (cualquier persona con sesión).

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/access/matrix` |
| Acceso | Sesión iniciada |
| Controlador | `backendChapterCoreIEEE/src/auth/controllers/access.controller.ts` → `matrix()` |

### Lógica que invoca

- `AccessService.matrix()`

### Consumido por el frontend

- [[M1 - Cliente API auth]]

## Enlaces

- [[M1 - access.service]]
- [[M1 - Cliente API auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
