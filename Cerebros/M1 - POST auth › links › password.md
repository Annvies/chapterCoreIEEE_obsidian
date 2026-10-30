---
type: endpoint
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/controllers/auth.controller.ts
actualizado: 2026-10-29
aliases:
  - "POST /auth/links/password"
tags:
  - chaptercore
  - modulo-1
  - endpoint
---

# M1 - POST auth › links › password

[[M1 - API]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Endpoint
> `POST /auth/links/password` · acceso: Público (sin sesión).

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/auth/links/password` |
| Acceso | Público (sin sesión) |
| Controlador | `backendChapterCoreIEEE/src/auth/controllers/auth.controller.ts` → `setPassword()` |
| Respuesta | `OK` |

### Entradas

- Cuerpo → `SetPasswordDto`

### Lógica que invoca

- `AuthService.setPasswordWithLink()`

### Consumido por el frontend

- [[M1 - Cliente API auth]]

## Enlaces

- [[M1 - auth.service]]
- [[M1 - DTO SetPasswordDto]]
- [[M1 - Cliente API auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
