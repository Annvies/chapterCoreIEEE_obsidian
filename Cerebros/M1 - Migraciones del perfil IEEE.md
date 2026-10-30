---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792713600000-AddIeeeMembershipToUsers.ts
  - backendChapterCoreIEEE/src/database/migrations/1792800000000-AddPendingApprovalToUsers.ts
  - .github/workflows/deploy-vercel-prod.yml
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Migraciones del perfil IEEE

[[M1 - Base de datos]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué son
> Dos migraciones de TypeORM, **aditivas y reversibles**, que agregan el perfil IEEE y
> la aprobación de invitaciones sin modificar los datos existentes.

> [!info] Contenido
> **`1792713600000-AddIeeeMembershipToUsers`**
> - `users`: `ieee_membership_grade` (con CHECK de los 7 grados),
>   `ieee_membership_expires_at` (date), `ieee_verified_at` (timestamptz) e
>   `ieee_verified_by` (FK a `users`, `ON DELETE SET NULL`). Todas aceptan nulo.
> - Tabla nueva `user_ieee_societies (user_id, society_id)`: PK compuesta, FK `CASCADE`
>   a `users`, `RESTRICT` a `ieee_societies` e índice por `society_id`.
>
> **`1792800000000-AddPendingApprovalToUsers`**
> - `users.pending_approval boolean NOT NULL DEFAULT false`. En PostgreSQL 11+ una
>   columna con default constante no reescribe la tabla.

> [!success] Seguridad para el deploy
> - Compatibles hacia atrás: el código anterior sigue funcionando con el esquema nuevo.
> - Las cuentas existentes quedan con `pending_approval = false`: siguen entrando.
> - El workflow `deploy-vercel-prod` las aplica en Neon **antes** de desplegar el
>   backend; cada migración corre en transacción.
> - Probadas en PostgreSQL 18 local (2026-10-30): desde cero, sobre un usuario
>   existente, `revert` y otra vez `run`. El CI solo ejecuta `migration:show`.

> [!todo] Pendiente de confirmar
> La ejecución en la base de producción (Neon) tras el merge a `main` no se revisó en
> esta auditoría: confirmar en GitHub Actions → `deploy-vercel-prod` → paso de migraciones.

## Enlaces

- Tablas: [[M1 - Tabla users]], [[M1 - Tabla user_ieee_societies]], [[M1 - Tabla ieee_societies]].
- Explica el almacenamiento de [[M1 - Perfil de membresía IEEE]] y [[M1 - Aprobación de invitaciones]].
- Despliegue: [[CC - Producción en Neon y Vercel]].

## Fuentes

- `backendChapterCoreIEEE/src/database/migrations/1792713600000-AddIeeeMembershipToUsers.ts`
- `backendChapterCoreIEEE/src/database/migrations/1792800000000-AddPendingApprovalToUsers.ts`
- `.github/workflows/deploy-vercel-prod.yml` y `.github/workflows/backend-ci.yml`
