---
type: endpoint
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/public-forms.controller.ts
actualizado: 2026-10-29
aliases:
  - "POST /public/forms/:slug/submissions"
tags:
  - chaptercore
  - modulo-5
  - endpoint
---

# M5 - POST public › forms › {slug} › submissions

[[M5 - API]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Endpoint
> `POST /public/forms/:slug/submissions` · acceso: Público (sin sesión).

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/public/forms/:slug/submissions` |
| Acceso | Público (sin sesión) |
| Controlador | `backendChapterCoreIEEE/src/forms/public-forms.controller.ts` → `submit()` |

### Entradas

- Parámetro de ruta `slug`
- Cuerpo → `Record`

### Lógica que invoca

- `FormSubmissionsService.createPublic()`

> [!note] Comentario del controlador
> Formularios abiertos desde un QR: no requieren sesión.

### Consumido por el frontend

- [[M5 - lib api]]

## Enlaces

- [[M5 - form-submissions.service]]
- [[M5 - lib api]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
