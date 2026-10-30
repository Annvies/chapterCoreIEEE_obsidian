---
type: endpoint
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/controllers/users.controller.ts
actualizado: 2026-10-30
aliases:
  - "POST /users/:id/access-link"
tags:
  - chaptercore
  - modulo-1
  - endpoint
---

# M1 - POST users › {id} › access-link

[[M1 - API]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Endpoint
> `POST /users/:id/access-link` · acceso: Usuarios · Total.

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/users/:id/access-link` |
| Acceso | Usuarios · Total |
| Controlador | `backendChapterCoreIEEE/src/auth/controllers/users.controller.ts` → `issueAccessLink()` |
| Respuesta | `OK` |

### Entradas

- Parámetro de ruta `id` (UUID)
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `UsersService.issueAccessLink()`

### Consumido por el frontend

- [[M1 - Cliente API auth]]

## Enlaces

- [[M1 - users.service]]
- [[M1 - Cliente API auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
