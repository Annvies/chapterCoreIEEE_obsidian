---
type: endpoint
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/controllers/auth.controller.ts
actualizado: 2026-10-30
aliases:
  - "POST /auth/links/inspect"
tags:
  - chaptercore
  - modulo-1
  - endpoint
---

# M1 - POST auth › links › inspect

[[M1 - API]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Endpoint
> `POST /auth/links/inspect` · acceso: Público (sin sesión).

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/auth/links/inspect` |
| Acceso | Público (sin sesión) |
| Controlador | `backendChapterCoreIEEE/src/auth/controllers/auth.controller.ts` → `inspectLink()` |
| Respuesta | `OK` |

### Entradas

- Cuerpo → `InspectLinkDto`

### Lógica que invoca

- `AuthService.inspectLink()`

### Consumido por el frontend

- [[M1 - Cliente API auth]]

## Enlaces

- [[M1 - auth.service]]
- [[M1 - DTO InspectLinkDto]]
- [[M1 - Cliente API auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
