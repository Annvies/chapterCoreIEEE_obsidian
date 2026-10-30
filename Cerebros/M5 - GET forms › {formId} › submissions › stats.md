---
type: endpoint
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/form-submissions.controller.ts
actualizado: 2026-10-30
aliases:
  - "GET /forms/:formId/submissions/stats"
tags:
  - chaptercore
  - modulo-5
  - endpoint
---

# M5 - GET forms › {formId} › submissions › stats

[[M5 - API]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Endpoint
> `GET /forms/:formId/submissions/stats` · acceso: Formularios · Editar.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/forms/:formId/submissions/stats` |
| Acceso | Formularios · Editar |
| Controlador | `backendChapterCoreIEEE/src/forms/form-submissions.controller.ts` → `stats()` |

### Entradas

- Parámetro de ruta `formId` (UUID)

### Lógica que invoca

- `FormSubmissionsService.stats()`

### Consumido por el frontend

- [[M5 - lib api]]

## Enlaces

- [[M5 - form-submissions.service]]
- [[M5 - lib api]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
