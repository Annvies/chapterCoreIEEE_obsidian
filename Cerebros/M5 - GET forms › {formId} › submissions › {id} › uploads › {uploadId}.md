---
type: endpoint
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/form-submissions.controller.ts
actualizado: 2026-10-29
aliases:
  - "GET /forms/:formId/submissions/:id/uploads/:uploadId"
tags:
  - chaptercore
  - modulo-5
  - endpoint
---

# M5 - GET forms › {formId} › submissions › {id} › uploads › {uploadId}

[[M5 - API]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Endpoint
> `GET /forms/:formId/submissions/:id/uploads/:uploadId` · acceso: Formularios · Editar.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/forms/:formId/submissions/:id/uploads/:uploadId` |
| Acceso | Formularios · Editar |
| Controlador | `backendChapterCoreIEEE/src/forms/form-submissions.controller.ts` → `downloadUpload()` |

### Entradas

- Parámetro de ruta `formId` (UUID)
- Parámetro de ruta `id` (UUID)
- Parámetro de ruta `uploadId` (UUID)

### Lógica que invoca

- `FormSubmissionsService.downloadUpload()`

> [!question] Sin llamada directa en el frontend
> No se encontró una llamada a esta ruta en `frontendChapterCoreIEEE/src`. Puede usarse con una
> URL que devuelve el servidor, desde fuera de la app (p. ej. un QR) o no usarse todavía.

## Enlaces

- [[M5 - form-submissions.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
