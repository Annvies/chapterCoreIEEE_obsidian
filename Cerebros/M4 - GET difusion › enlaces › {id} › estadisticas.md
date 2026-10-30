---
type: endpoint
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/difusion/difusion.controller.ts
actualizado: 2026-10-30
aliases:
  - "GET /difusion/enlaces/:id/estadisticas"
tags:
  - chaptercore
  - modulo-4
  - endpoint
---

# M4 - GET difusion › enlaces › {id} › estadisticas

[[M4 - API]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Endpoint
> `GET /difusion/enlaces/:id/estadisticas` · acceso: Difusión · Ver.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/difusion/enlaces/:id/estadisticas` |
| Acceso | Difusión · Ver |
| Controlador | `backendChapterCoreIEEE/src/difusion/difusion.controller.ts` → `stats()` |
| Devuelve | `Promise<LinkStatsView>` |

### Entradas

- Parámetro de ruta `id` (UUID)
- Query  → `LinkStatsQueryDto`

### Lógica que invoca

- `DifusionService.stats()`

> [!note] Comentario del controlador
> Administración de QR y enlaces oficiales (mockup 06). Permisos de la matriz del Módulo 1: ver lista y escaneos exige Ver; crear y editar exige Editar.

### Consumido por el frontend

- [[M4 - Cliente API difusion]]

## Enlaces

- [[M4 - difusion.service]]
- [[M4 - DTO LinkStatsQueryDto]]
- [[M4 - Cliente API difusion]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
