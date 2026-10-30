---
type: migración
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-5
  - migración
---

# M5 - Migración CreateFormsModule

[[M5 - Base de datos]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Migración
> Migración TypeORM `1730000000000-CreateFormsModule.ts`.

| Campo | Valor |
|---|---|
| Archivo | `1730000000000-CreateFormsModule.ts` |
| Marca de tiempo | `1730000000000` (orden de ejecución) |
| Reversible | sí, tiene `down()` |

### Qué hace

- Extensión `pgcrypto`
- Extensión `citext`
- Crea la tabla `forms`
- Crea la tabla `form_versions`
- Crea la tabla `form_submissions`
- Crea la tabla `form_uploads`
- Índice único `uq_forms_slug_active` en `forms`
- Índice `ix_forms_status` en `forms`
- Índice `ix_form_versions_schema_gin` en `form_versions`
- Índice único `uq_form_versions_one_draft` en `form_versions`
- Índice único `uq_form_versions_one_published` en `form_versions`
- Índice `ix_form_submissions_form_created` en `form_submissions`
- Índice `ix_form_submissions_form_status` en `form_submissions`
- Índice `ix_form_submissions_version` en `form_submissions`
- Índice `ix_form_submissions_data_gin` en `form_submissions`
- Índice `ix_form_submissions_email` en `form_submissions`
- Índice `ix_form_uploads_submission` en `form_uploads`

## Enlaces

- [[M5 - Tabla forms]]
- [[M5 - Tabla form_versions]]
- [[M5 - Tabla form_submissions]]
- [[M5 - Tabla form_uploads]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
