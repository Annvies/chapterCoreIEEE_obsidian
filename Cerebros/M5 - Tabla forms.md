---
type: tabla
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts
  - backendChapterCoreIEEE/src/forms/entities/form.entity.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-5
  - tabla
---

# M5 - Tabla forms

[[M5 - Base de datos]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Tabla
> Tabla `forms` de PostgreSQL (9 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `uuid NOT NULL DEFAULT gen_random_uuid()` |
| `slug` | `varchar(140) NOT NULL` |
| `title` | `varchar(200) NOT NULL` |
| `description` | `text` |
| `status` | `varchar(20) NOT NULL DEFAULT 'draft'` |
| `created_by` | `uuid` |
| `created_at` | `timestamptz NOT NULL DEFAULT now()` |
| `updated_at` | `timestamptz NOT NULL DEFAULT now()` |
| `deleted_at` | `timestamptz` |

### Restricciones

- `CONSTRAINT "pk_forms" PRIMARY KEY ("id")`
- `CONSTRAINT "ck_forms_status" CHECK ("status" IN ('draft','published','archived'))`
- `CONSTRAINT "ck_forms_slug" CHECK ("slug" ~ '^[a-z0-9]+(?:-[a-z0-9]+)*$')`

### Índices

- único `uq_forms_slug_active`: ("slug") WHERE "deleted_at" IS NULL
- `ix_forms_status`: ("status") WHERE "deleted_at" IS NULL

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts`
- `backendChapterCoreIEEE/src/forms/entities/form.entity.ts`

## Enlaces

- [[M5 - Estados del formulario]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
