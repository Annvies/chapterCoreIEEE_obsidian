---
type: concepto
modulo: 5
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts
  - backendChapterCoreIEEE/src/forms/form-submissions.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - concepto
---

# M5 - Estados de una respuesta

[[M5 - Respuestas y versiones]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Qué es
> Tabla `form_submissions`: cada envío y su revisión.

> [!info] Confirmado en el código
> - Estados: `received`, `reviewed`, `accepted` y `rejected`.
> - Correo de quien responde obligatorio; respuestas en JSON.
> - Revisión con `reviewed_by`, `reviewed_at` y notas.
> - Exportación de hasta 10.000 filas.

## Enlaces

- Forma parte de [[M5 - Respuestas y versiones]].
- Relacionada con [[M5 - Versionado de formularios]].

## Fuentes

- `backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts`
- `backendChapterCoreIEEE/src/forms/form-submissions.service.ts`
