---
type: endpoint
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/form-submissions.controller.ts
actualizado: 2026-10-30
aliases:
  - "PATCH /forms/:formId/submissions/:id/review"
tags:
  - chaptercore
  - modulo-5
  - endpoint
---

# M5 - PATCH forms › {formId} › submissions › {id} › review

[[M5 - API]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Endpoint
> `PATCH /forms/:formId/submissions/:id/review` · acceso: Formularios · Editar.

| Campo | Valor |
|---|---|
| Método | `PATCH` |
| Ruta | `/forms/:formId/submissions/:id/review` |
| Acceso | Formularios · Editar |
| Controlador | `backendChapterCoreIEEE/src/forms/form-submissions.controller.ts` → `review()` |

### Entradas

- Parámetro de ruta `formId` (UUID)
- Parámetro de ruta `id` (UUID)
- Cuerpo → `UpdateSubmissionReviewDto`
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `FormSubmissionsService.review()`

### Consumido por el frontend

- [[M5 - lib api]]

## Enlaces

- [[M5 - form-submissions.service]]
- [[M5 - DTO UpdateSubmissionReviewDto]]
- [[M5 - lib api]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
