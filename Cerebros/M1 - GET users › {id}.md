---
type: endpoint
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/controllers/users.controller.ts
actualizado: 2026-10-30
aliases:
  - "GET /users/:id"
tags:
  - chaptercore
  - modulo-1
  - endpoint
---

# M1 - GET users › {id}

[[M1 - API]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Endpoint
> `GET /users/:id` · acceso: Usuarios · Total.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/users/:id` |
| Acceso | Usuarios · Total |
| Controlador | `backendChapterCoreIEEE/src/auth/controllers/users.controller.ts` → `findOne()` |

### Entradas

- Parámetro de ruta `id` (UUID)

### Lógica que invoca

- `UsersService.findOne()`

> [!question] Sin llamada directa en el frontend
> No se encontró una llamada a esta ruta en `frontendChapterCoreIEEE/src`. Puede usarse con una
> URL que devuelve el servidor, desde fuera de la app (p. ej. un QR) o no usarse todavía.

## Enlaces

- [[M1 - users.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
