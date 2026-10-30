---
type: endpoint
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/controllers/auth.controller.ts
actualizado: 2026-10-30
aliases:
  - "PATCH /auth/me/ieee"
tags:
  - chaptercore
  - modulo-1
  - endpoint
---

# M1 - PATCH auth › me › ieee

[[M1 - API]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Endpoint
> Solo requiere sesión: cada persona edita su propio perfil IEEE.

| Campo | Valor |
|---|---|
| Método | `PATCH` |
| Ruta | `/auth/me/ieee` |
| Acceso | Sesión iniciada |
| Controlador | `backendChapterCoreIEEE/src/auth/controllers/auth.controller.ts` → `updateMyIeeeProfile()` |

### Entradas

- Cuerpo → `UpdateIeeeProfileDto`
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `AuthService.profile()`
- `UsersService.updateIeeeProfile()`

### Consumido por el frontend

- [[M1 - Cliente API auth]]

## Enlaces

- [[M1 - auth.service]]
- [[M1 - users.service]]
- [[M1 - DTO UpdateIeeeProfileDto]]
- [[M1 - Cliente API auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
