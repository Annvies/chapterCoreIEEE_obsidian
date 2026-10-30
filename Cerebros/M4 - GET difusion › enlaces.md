---
type: endpoint
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/difusion/difusion.controller.ts
actualizado: 2026-10-29
aliases:
  - "GET /difusion/enlaces"
tags:
  - chaptercore
  - modulo-4
  - endpoint
---

# M4 - GET difusion › enlaces

[[M4 - API]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Endpoint
> `GET /difusion/enlaces` · acceso: Difusión · Ver.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/difusion/enlaces` |
| Acceso | Difusión · Ver |
| Controlador | `backendChapterCoreIEEE/src/difusion/difusion.controller.ts` → `list()` |
| Devuelve | `Promise<ShortLinkView[]>` |

### Entradas

- Query  → `ListShortLinksQueryDto`

### Lógica que invoca

- `DifusionService.list()`

> [!note] Comentario del controlador
> Administración de QR y enlaces oficiales (mockup 06). Permisos de la matriz del Módulo 1: ver lista y escaneos exige Ver; crear y editar exige Editar.

### Consumido por el frontend

- [[M4 - Cliente API difusion]]

## Enlaces

- [[M4 - difusion.service]]
- [[M4 - DTO ListShortLinksQueryDto]]
- [[M4 - Cliente API difusion]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
