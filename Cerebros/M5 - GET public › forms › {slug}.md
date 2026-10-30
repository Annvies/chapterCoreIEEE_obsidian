---
type: endpoint
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/public-forms.controller.ts
actualizado: 2026-10-29
aliases:
  - "GET /public/forms/:slug"
tags:
  - chaptercore
  - modulo-5
  - endpoint
---

# M5 - GET public › forms › {slug}

[[M5 - API]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Endpoint
> `GET /public/forms/:slug` · acceso: Público (sin sesión).

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/public/forms/:slug` |
| Acceso | Público (sin sesión) |
| Controlador | `backendChapterCoreIEEE/src/forms/public-forms.controller.ts` → `getPublished()` |

### Entradas

- Parámetro de ruta `slug`

### Lógica que invoca

- `FormsService.getPublishedBySlug()`

> [!note] Comentario del controlador
> Formularios abiertos desde un QR: no requieren sesión.

### Consumido por el frontend

- [[M5 - lib api]]

## Enlaces

- [[M5 - forms.service]]
- [[M5 - lib api]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
