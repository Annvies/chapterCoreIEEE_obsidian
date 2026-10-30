---
type: tabla
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792627200000-CreateContactsModule.ts
  - backendChapterCoreIEEE/src/contacts/entities/contact-interaction.entity.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-2
  - tabla
---

# M2 - Tabla contact_interactions

[[M2 - Base de datos]] · [[Cerebro 2 - Contactos]]

> [!abstract] Tabla
> Tabla `contact_interactions` de PostgreSQL (7 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `uuid PRIMARY KEY DEFAULT gen_random_uuid()` |
| `contact_id` | `uuid NOT NULL REFERENCES contacts(id) ON DELETE CASCADE` |
| `tipo` | `text NOT NULL CHECK (tipo IN ('llamada', 'correo', 'reunion', 'evento', 'nota'))` |
| `descripcion` | `text NOT NULL CHECK (char_length(btrim(descripcion)) BETWEEN 1 AND 1000)` |
| `fecha` | `date NOT NULL` |
| `created_by` | `uuid REFERENCES users(id) ON DELETE SET NULL` |
| `created_at` | `timestamptz NOT NULL DEFAULT now()` |

### Índices

- `contact_interactions_contact_fecha_idx`: (contact_id, fecha DESC, created_at DESC)

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1792627200000-CreateContactsModule.ts`
- `backendChapterCoreIEEE/src/contacts/entities/contact-interaction.entity.ts`

## Enlaces

- [[M2 - Historial de interacciones]]
- [[M2 - Migración CreateContactsModule]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
