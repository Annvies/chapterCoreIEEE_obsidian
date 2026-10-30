---
type: tabla
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792454400000-CreateAuthModule.ts
  - backendChapterCoreIEEE/src/auth/entities/auth-token.entity.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - tabla
---

# M1 - Tabla auth_tokens

[[M1 - Base de datos]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Tabla
> Tabla `auth_tokens` de PostgreSQL (8 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `uuid PRIMARY KEY DEFAULT gen_random_uuid()` |
| `user_id` | `uuid NOT NULL REFERENCES users(id) ON DELETE CASCADE` |
| `purpose` | `text NOT NULL CHECK (purpose IN ('invitation', 'password_reset'))` |
| `token_hash` | `text NOT NULL UNIQUE` |
| `expires_at` | `timestamptz NOT NULL` |
| `used_at` | `timestamptz` |
| `created_by` | `uuid REFERENCES users(id) ON DELETE SET NULL` |
| `created_at` | `timestamptz NOT NULL DEFAULT now()` |

### Índices

- `auth_tokens_user_id_idx`: (user_id)

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1792454400000-CreateAuthModule.ts`
- `backendChapterCoreIEEE/src/auth/entities/auth-token.entity.ts`

## Enlaces

- [[M1 - Modelo de datos users y auth_tokens]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
