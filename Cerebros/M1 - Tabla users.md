---
type: tabla
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792454400000-CreateAuthModule.ts
  - backendChapterCoreIEEE/src/database/migrations/1792713600000-AddIeeeMembershipToUsers.ts
  - backendChapterCoreIEEE/src/database/migrations/1792800000000-AddPendingApprovalToUsers.ts
  - backendChapterCoreIEEE/src/auth/entities/user.entity.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - tabla
---

# M1 - Tabla users

[[M1 - Base de datos]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Tabla
> Tabla `users` de PostgreSQL (16 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `uuid PRIMARY KEY DEFAULT gen_random_uuid()` |
| `email` | `citext NOT NULL` |
| `full_name` | `text NOT NULL CHECK (char_length(btrim(full_name)) BETWEEN 1 AND 120)` |
| `password_hash` | `text` |
| `status` | `text NOT NULL DEFAULT 'invited' CHECK (status IN ('invited', 'active', 'disabled'))` |
| `cargo` | `text CHECK (cargo IN ('presidente', 'vicepresidente', 'tesorero', 'secretario', 'webmaster'))` |
| `ambito` | `text CHECK (ambito IN ('rama', 'capitulo'))` |
| `chapter_id` | `smallint REFERENCES ieee_societies(id) ON DELETE RESTRICT` |
| `ieee_member_number` | `text CHECK (ieee_member_number ~ '^[0-9]{6,12}$')` |
| `failed_login_attempts` | `smallint NOT NULL DEFAULT 0 CHECK (failed_login_attempts >= 0)` |
| `locked_until` | `timestamptz` |
| `token_version` | `integer NOT NULL DEFAULT 0` |
| `last_login_at` | `timestamptz` |
| `invited_by` | `uuid REFERENCES users(id) ON DELETE SET NULL` |
| `created_at` | `timestamptz NOT NULL DEFAULT now()` |
| `updated_at` | `timestamptz NOT NULL DEFAULT now()` |

### Restricciones

- `CONSTRAINT users_email_unique UNIQUE (email)`
- `CONSTRAINT users_email_format CHECK (email ~ '^[^@\\s]+@[^@\\s]+$')`
- `CONSTRAINT users_position_coherente CHECK ( (cargo IS NULL AND ambito IS NULL AND chapter_id IS NULL) OR (cargo IS NOT NULL AND ambito = 'rama' AND chapter_id IS NULL) OR (cargo IS NOT NULL AND ambito = 'capitulo' AND chapter_id IS NOT NULL) )`
- `CONSTRAINT users_active_has_password CHECK (status <> 'active' OR password_hash IS NOT NULL)`

### Índices

- `users_chapter_id_idx`: (chapter_id)

### Cambios posteriores

- `ADD COLUMN ieee_membership_grade text CHECK (ieee_membership_grade IN (`
- `ADD COLUMN pending_approval boolean NOT NULL DEFAULT false`

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1792454400000-CreateAuthModule.ts`
- `backendChapterCoreIEEE/src/database/migrations/1792713600000-AddIeeeMembershipToUsers.ts`
- `backendChapterCoreIEEE/src/database/migrations/1792800000000-AddPendingApprovalToUsers.ts`
- `backendChapterCoreIEEE/src/auth/entities/user.entity.ts`

## Enlaces

- [[M1 - Modelo de datos users y auth_tokens]]
- [[M1 - Migración CreateAuthModule]]
- [[M1 - Migración AddIeeeMembershipToUsers]]
- [[M1 - Migración AddPendingApprovalToUsers]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
