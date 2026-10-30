---
type: endpoint
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/controllers/access.controller.ts
actualizado: 2026-10-29
aliases:
  - "GET /access/chapters"
tags:
  - chaptercore
  - modulo-1
  - endpoint
---

# M1 - GET access › chapters

[[M1 - API]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Endpoint
> Capítulos disponibles para asignar cargos de capítulo.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/access/chapters` |
| Acceso | Usuarios · Total |
| Controlador | `backendChapterCoreIEEE/src/auth/controllers/access.controller.ts` → `chapters()` |

### Lógica que invoca

- `AccessService.listChapters()`

### Consumido por el frontend

- [[M1 - Cliente API auth]]

## Enlaces

- [[M1 - access.service]]
- [[M1 - Cliente API auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
