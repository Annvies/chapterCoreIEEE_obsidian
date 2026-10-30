---
type: endpoint
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/controllers/auth.controller.ts
actualizado: 2026-10-29
aliases:
  - "GET /auth/me"
tags:
  - chaptercore
  - modulo-1
  - endpoint
---

# M1 - GET auth › me

[[M1 - API]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Endpoint
> `GET /auth/me` · acceso: Sesión iniciada.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/auth/me` |
| Acceso | Sesión iniciada |
| Controlador | `backendChapterCoreIEEE/src/auth/controllers/auth.controller.ts` → `me()` |

### Entradas

- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `AuthService.profile()`

### Consumido por el frontend

- [[M1 - Cliente API auth]]

## Enlaces

- [[M1 - auth.service]]
- [[M1 - Cliente API auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
