---
type: endpoint
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/controllers/users.controller.ts
actualizado: 2026-10-30
aliases:
  - "PATCH /users/:id/status"
tags:
  - chaptercore
  - modulo-1
  - endpoint
---

# M1 - PATCH users › {id} › status

[[M1 - API]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Endpoint
> `PATCH /users/:id/status` · acceso: Usuarios · Total.

| Campo | Valor |
|---|---|
| Método | `PATCH` |
| Ruta | `/users/:id/status` |
| Acceso | Usuarios · Total |
| Controlador | `backendChapterCoreIEEE/src/auth/controllers/users.controller.ts` → `setStatus()` |

### Entradas

- Parámetro de ruta `id` (UUID)
- Cuerpo → `UpdateUserStatusDto`
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `UsersService.setStatus()`

### Consumido por el frontend

- [[M1 - Cliente API auth]]

## Enlaces

- [[M1 - users.service]]
- [[M1 - DTO UpdateUserStatusDto]]
- [[M1 - Cliente API auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
