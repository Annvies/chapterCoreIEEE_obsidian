---
type: tabla
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts
  - backendChapterCoreIEEE/src/forms/entities/form-version.entity.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - tabla
---

# M5 - Tabla form_versions

[[M5 - Base de datos]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Tabla
> Tabla `form_versions` de PostgreSQL (8 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `uuid NOT NULL DEFAULT gen_random_uuid()` |
| `form_id` | `uuid NOT NULL` |
| `version` | `integer NOT NULL` |
| `schema` | `jsonb NOT NULL` |
| `status` | `varchar(20) NOT NULL DEFAULT 'draft'` |
| `published_at` | `timestamptz` |
| `created_by` | `uuid` |
| `created_at` | `timestamptz NOT NULL DEFAULT now()` |

### Restricciones

- `CONSTRAINT "pk_form_versions" PRIMARY KEY ("id")`
- `CONSTRAINT "uq_form_versions_form_version" UNIQUE ("form_id", "version")`
- `CONSTRAINT "ck_form_versions_version" CHECK ("version" > 0)`
- `CONSTRAINT "ck_form_versions_schema" CHECK (jsonb_typeof("schema") = 'object')`
- `CONSTRAINT "ck_form_versions_status" CHECK ("status" IN ('draft','published','archived'))`
- `CONSTRAINT "ck_form_versions_published_at" CHECK ( ("status" = 'published' AND "published_at" IS NOT NULL) OR "status" <> 'published' )`
- `CONSTRAINT "fk_form_versions_form" FOREIGN KEY ("form_id") REFERENCES "forms"("id") ON DELETE CASCADE ON UPDATE NO ACTION`

### Índices

- `ix_form_versions_schema_gin`: USING gin ("schema" jsonb_path_ops)
- único `uq_form_versions_one_draft`: ("form_id") WHERE "status" = \
- único `uq_form_versions_one_published`: ("form_id") WHERE "status" = \

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts`
- `backendChapterCoreIEEE/src/forms/entities/form-version.entity.ts`

## Enlaces

- [[M5 - Versionado de formularios]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
