---
type: tabla
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts
  - backendChapterCoreIEEE/src/forms/entities/form-submission.entity.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - tabla
---

# M5 - Tabla form_submissions

[[M5 - Base de datos]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Tabla
> Tabla `form_submissions` de PostgreSQL (12 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `uuid NOT NULL DEFAULT gen_random_uuid()` |
| `form_id` | `uuid NOT NULL` |
| `form_version_id` | `uuid NOT NULL` |
| `submitted_by` | `uuid` |
| `respondent_email` | `citext NOT NULL` |
| `data` | `jsonb NOT NULL` |
| `status` | `varchar(20) NOT NULL DEFAULT 'received'` |
| `reviewed_by` | `uuid` |
| `reviewed_at` | `timestamptz` |
| `review_notes` | `text` |
| `created_at` | `timestamptz NOT NULL DEFAULT now()` |
| `updated_at` | `timestamptz NOT NULL DEFAULT now()` |

### Restricciones

- `CONSTRAINT "pk_form_submissions" PRIMARY KEY ("id")`
- `CONSTRAINT "ck_form_submissions_status" CHECK ( "status" IN ('received','reviewed','accepted','rejected') )`
- `CONSTRAINT "ck_form_submissions_data" CHECK (jsonb_typeof("data") = 'object')`
- `CONSTRAINT "ck_form_submissions_email" CHECK (length(trim("respondent_email"::text)) > 3)`
- `CONSTRAINT "fk_form_submissions_form" FOREIGN KEY ("form_id") REFERENCES "forms"("id") ON DELETE RESTRICT ON UPDATE NO ACTION`
- `CONSTRAINT "fk_form_submissions_version" FOREIGN KEY ("form_version_id") REFERENCES "form_versions"("id") ON DELETE RESTRICT ON UPDATE NO ACTION`

### Índices

- `ix_form_submissions_form_created`: ("form_id", "created_at" DESC)
- `ix_form_submissions_form_status`: ("form_id", "status")
- `ix_form_submissions_version`: ("form_version_id")
- `ix_form_submissions_data_gin`: USING gin ("data" jsonb_path_ops)
- `ix_form_submissions_email`: ("respondent_email")

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts`
- `backendChapterCoreIEEE/src/forms/entities/form-submission.entity.ts`

## Enlaces

- [[M5 - Estados de una respuesta]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
