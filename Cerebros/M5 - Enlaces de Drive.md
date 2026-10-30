---
type: concepto
modulo: 5
estado: propuesto
fuentes:
  - backendChapterCoreIEEE/src/forms/schema/form-schema.types.ts
  - backendChapterCoreIEEE/src/forms/schema/form-schema.zod.ts
  - backendChapterCoreIEEE/src/forms/public-forms.controller.ts
  - backendChapterCoreIEEE/src/forms/form-submissions.service.ts
  - frontendChapterCoreIEEE/src/features/public/DynamicForm.tsx
  - frontendChapterCoreIEEE/src/features/responses/SubmissionDetail.tsx
  - frontendChapterCoreIEEE/src/lib/form-schema-helpers.ts
  - specs/007-modulo-5-drive-links/spec.md
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-5
  - concepto
---

# M5 - Enlaces de Drive

[[M5 - Datos y privacidad]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Qué es
> Campo `drive_link` («Enlace de Drive») que reemplaza la carga de archivos en los
> formularios públicos: quien responde pega un enlace de Google Drive en lugar de subir
> un archivo al servidor.

> [!info] En el código (PR #27, en `main` con el PR #29)
> - Solo se acepta una URL absoluta `https`, sin usuario ni contraseña y con host
>   exactamente `drive.google.com` o `docs.google.com` (`isGoogleDriveUrl` en
>   `forms/schema/form-schema.types.ts`; validación en `forms/schema/form-schema.zod.ts`).
> - El constructor ofrece «Enlace de Drive» y deja de ofrecer «Subir archivo»
>   (`features/forms/FieldPalette.tsx`).
> - Un campo `file` de una versión ya publicada se muestra como entrada de enlace, sin
>   migración de datos (`lib/form-schema-helpers.ts`, `features/public/DynamicForm.tsx`).
> - Los envíos nuevos van como JSON: no se guardan archivos ni se crean registros en
>   `form_uploads` (`forms/public-forms.controller.ts`, `forms/form-submissions.service.ts`).
> - El detalle de la respuesta muestra el enlace y conserva la descarga de adjuntos
>   antiguos (`features/responses/SubmissionDetail.tsx`).

> [!success] Qué resuelve
> El almacenamiento local de archivos no garantizaba persistencia en despliegues
> efímeros. Con enlaces, el archivo vive en Google Drive y su acceso lo controla Drive.
> Se conservan las respuestas, los metadatos y los archivos históricos.

> [!warning] Límites
> No se sigue ni se verifica el enlace: el sistema no comprueba si el documento existe
> ni si está compartido con quien revisa. Cambiar permisos de Drive queda fuera de
> alcance (`specs/007-modulo-5-drive-links/spec.md`).

## Enlaces

- Forma parte de [[M5 - Datos y privacidad]].
- Sustituye, para los envíos nuevos, a [[M5 - Archivos adjuntos]].
- Relacionada con [[M5 - Tipos de campo]].

## Fuentes

- PR #27 de `marianZamorano/chapterCoreIEEE` (commit `3169b49`), integrado en `dev` (`8c81834`) y en `main` con el PR #29 (`cdc4abf`).
- `specs/007-modulo-5-drive-links/spec.md`
