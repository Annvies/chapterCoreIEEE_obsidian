---
type: endpoint
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/difusion/difusion.controller.ts
actualizado: 2026-10-30
aliases:
  - "POST /difusion/enlaces"
tags:
  - chaptercore
  - modulo-4
  - endpoint
---

# M4 - POST difusion › enlaces

[[M4 - API]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Endpoint
> `POST /difusion/enlaces` · acceso: Difusión · Editar.

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/difusion/enlaces` |
| Acceso | Difusión · Editar |
| Controlador | `backendChapterCoreIEEE/src/difusion/difusion.controller.ts` → `create()` |
| Límite | 20 peticiones por 60 s |
| Devuelve | `Promise<ShortLinkView>` |

### Entradas

- Cuerpo → `CreateShortLinkDto`

### Lógica que invoca

- `DifusionService.create()`

> [!note] Comentario del controlador
> Administración de QR y enlaces oficiales (mockup 06). Permisos de la matriz del Módulo 1: ver lista y escaneos exige Ver; crear y editar exige Editar.

### Consumido por el frontend

- [[M4 - Cliente API difusion]]

## Enlaces

- [[M4 - difusion.service]]
- [[M4 - DTO CreateShortLinkDto]]
- [[M4 - Cliente API difusion]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
