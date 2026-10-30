---
type: tabla
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts
  - backendChapterCoreIEEE/src/forms/entities/form-upload.entity.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - tabla
---

# M5 - Tabla form_uploads

[[M5 - Base de datos]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Tabla
> Tabla `form_uploads` de PostgreSQL (8 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `uuid NOT NULL DEFAULT gen_random_uuid()` |
| `submission_id` | `uuid NOT NULL` |
| `field_id` | `varchar(80) NOT NULL` |
| `original_name` | `text NOT NULL` |
| `mime_type` | `varchar(150) NOT NULL` |
| `size_bytes` | `bigint NOT NULL` |
| `storage_key` | `text NOT NULL` |
| `created_at` | `timestamptz NOT NULL DEFAULT now()` |

### Restricciones

- `CONSTRAINT "pk_form_uploads" PRIMARY KEY ("id")`
- `CONSTRAINT "uq_form_uploads_storage_key" UNIQUE ("storage_key")`
- `CONSTRAINT "ck_form_uploads_size" CHECK ("size_bytes" > 0)`
- `CONSTRAINT "fk_form_uploads_submission" FOREIGN KEY ("submission_id") REFERENCES "form_submissions"("id") ON DELETE CASCADE ON UPDATE NO ACTION`

### Índices

- `ix_form_uploads_submission`: ("submission_id")

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts`
- `backendChapterCoreIEEE/src/forms/entities/form-upload.entity.ts`

## Enlaces

- [[M5 - Archivos adjuntos]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
