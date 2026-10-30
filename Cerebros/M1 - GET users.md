---
type: endpoint
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/controllers/users.controller.ts
actualizado: 2026-10-30
aliases:
  - "GET /users"
tags:
  - chaptercore
  - modulo-1
  - endpoint
---

# M1 - GET users

[[M1 - API]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Endpoint
> `GET /users` · acceso: Usuarios · Total.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/users` |
| Acceso | Usuarios · Total |
| Controlador | `backendChapterCoreIEEE/src/auth/controllers/users.controller.ts` → `list()` |

### Entradas

- Query  → `ListUsersQueryDto`

### Lógica que invoca

- `UsersService.list()`

### Consumido por el frontend

- [[M1 - Cliente API auth]]

## Enlaces

- [[M1 - users.service]]
- [[M1 - DTO ListUsersQueryDto]]
- [[M1 - Cliente API auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
