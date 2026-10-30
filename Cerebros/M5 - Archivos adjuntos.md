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

# M5 - Archivos adjuntos

[[M5 - Datos y privacidad]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Qué es
> Tabla `form_uploads`: archivos subidos en campos `file`.

> [!info] Confirmado en el código
> - Guarda nombre original, tipo MIME, tamaño y clave de almacenamiento única.
> - Tamaño máximo configurable con `MAX_UPLOAD_MB` (20 MB por defecto).
> - Si se borra la respuesta, se borran sus adjuntos (`ON DELETE CASCADE`).

> [!info] Cambio en `main` (PR #27, integrado con el PR #29)
> Los envíos nuevos ya no crean registros en `form_uploads`: se reemplazan por
> [[M5 - Enlaces de Drive]]. La tabla, sus archivos y la descarga autenticada se
> conservan para las respuestas históricas.

> [!warning] Datos personales
> Los adjuntos pueden contener datos personales: revisar quién los descarga y cuánto tiempo se conservan.

## Enlaces

- Forma parte de [[M5 - Datos y privacidad]].

## Fuentes

- `backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts`
- `backendChapterCoreIEEE/src/forms/form-submissions.service.ts`
