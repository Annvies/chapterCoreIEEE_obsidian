---
type: endpoint
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/controllers/users.controller.ts
actualizado: 2026-10-29
aliases:
  - "POST /users/invitations"
tags:
  - chaptercore
  - modulo-1
  - endpoint
---

# M1 - POST users › invitations

[[M1 - API]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Endpoint
> `POST /users/invitations` · acceso: Usuarios · Total.

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/users/invitations` |
| Acceso | Usuarios · Total |
| Controlador | `backendChapterCoreIEEE/src/auth/controllers/users.controller.ts` → `invite()` |

### Entradas

- Cuerpo → `InviteUserDto`
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `UsersService.invite()`

### Consumido por el frontend

- [[M1 - Cliente API auth]]

## Enlaces

- [[M1 - users.service]]
- [[M1 - DTO InviteUserDto]]
- [[M1 - Cliente API auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
