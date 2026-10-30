---
type: endpoint
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/difusion/difusion.controller.ts
actualizado: 2026-10-30
aliases:
  - "PATCH /difusion/enlaces/:id"
tags:
  - chaptercore
  - modulo-4
  - endpoint
---

# M4 - PATCH difusion › enlaces › {id}

[[M4 - API]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Endpoint
> `PATCH /difusion/enlaces/:id` · acceso: Difusión · Editar.

| Campo | Valor |
|---|---|
| Método | `PATCH` |
| Ruta | `/difusion/enlaces/:id` |
| Acceso | Difusión · Editar |
| Controlador | `backendChapterCoreIEEE/src/difusion/difusion.controller.ts` → `update()` |
| Devuelve | `Promise<ShortLinkView>` |

### Entradas

- Parámetro de ruta `id` (UUID)
- Cuerpo → `UpdateShortLinkDto`

### Lógica que invoca

- `DifusionService.update()`

> [!note] Comentario del controlador
> Administración de QR y enlaces oficiales (mockup 06). Permisos de la matriz del Módulo 1: ver lista y escaneos exige Ver; crear y editar exige Editar.

### Consumido por el frontend

- [[M4 - Cliente API difusion]]

## Enlaces

- [[M4 - difusion.service]]
- [[M4 - DTO UpdateShortLinkDto]]
- [[M4 - Cliente API difusion]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
