---
type: tabla
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792627200000-CreateContactsModule.ts
  - backendChapterCoreIEEE/src/contacts/entities/contact.entity.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-2
  - tabla
---

# M2 - Tabla contacts

[[M2 - Base de datos]] · [[Cerebro 2 - Contactos]]

> [!abstract] Tabla
> Tabla `contacts` de PostgreSQL (20 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `uuid PRIMARY KEY DEFAULT gen_random_uuid()` |
| `tipo` | `text NOT NULL CHECK (tipo IN ('empresa', 'alumni', 'conferencista', 'autoridad'))` |
| `nombre` | `text NOT NULL CHECK (char_length(btrim(nombre)) BETWEEN 1 AND 200)` |
| `organizacion` | `text CHECK (char_length(organizacion) <= 200)` |
| `contacto_nombre` | `text CHECK (char_length(contacto_nombre) <= 160)` |
| `cargo` | `text CHECK (char_length(cargo) <= 160)` |
| `correo` | `citext CHECK (correo ~ '^[^@\\s]+@[^@\\s]+$' AND char_length(correo) <= 254)` |
| `telefono` | `text CHECK (char_length(telefono) <= 40)` |
| `sector` | `text CHECK (char_length(sector) <= 80)` |
| `ciudad` | `text CHECK (char_length(ciudad) <= 80)` |
| `estado` | `text CHECK (estado IN ('patrocinador', 'en_negociacion', 'prospecto', 'exaliado'))` |
| `convenio` | `text CHECK (char_length(convenio) <= 200)` |
| `convenio_vence` | `date` |
| `chapter_id` | `smallint REFERENCES ieee_societies(id) ON DELETE RESTRICT` |
| `notas` | `text CHECK (char_length(notas) <= 2000)` |
| `last_interaction_at` | `date` |
| `created_by` | `uuid REFERENCES users(id) ON DELETE SET NULL` |
| `updated_by` | `uuid REFERENCES users(id) ON DELETE SET NULL` |
| `created_at` | `timestamptz NOT NULL DEFAULT now()` |
| `updated_at` | `timestamptz NOT NULL DEFAULT now()` |

### Índices

- `contacts_tipo_nombre_idx`: (tipo, nombre)
- `contacts_chapter_id_idx`: (chapter_id)

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1792627200000-CreateContactsModule.ts`
- `backendChapterCoreIEEE/src/contacts/entities/contact.entity.ts`

## Enlaces

- [[M2 - Modelo de datos contacts]]
- [[M2 - Migración CreateContactsModule]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
