---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792454400000-CreateAuthModule.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Modelo de datos users y auth_tokens

[[M1 - Identidad y acceso]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué es
> Tablas que guardan las cuentas y los enlaces de un solo uso.

> [!info] Confirmado en el código
> - `users`: correo único (citext), nombre (1–120), `status`, `cargo`, `ambito`, `chapter_id`, `ieee_member_number` (6–12 dígitos), intentos fallidos, `locked_until`, `token_version`, `invited_by`.
> - Regla `users_position_coherente`: sin cargo → sin ámbito ni capítulo; ámbito `rama` → sin capítulo; ámbito `capitulo` → con capítulo.
> - Una cuenta `active` siempre tiene contraseña.
> - `auth_tokens`: `purpose` (`invitation` o `password_reset`), `token_hash` único, `expires_at`, `used_at`.

## Enlaces

- Forma parte de [[M1 - Identidad y acceso]].
- Relacionada con [[M1 - Ciclo de vida de una cuenta]], [[M1 - Enlaces de un solo uso]], [[M1 - Contraseñas y bloqueo de sesión]].

## Fuentes

- `backendChapterCoreIEEE/src/database/migrations/1792454400000-CreateAuthModule.ts`
