---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/auth/entities/user.entity.ts
  - backendChapterCoreIEEE/src/auth/domain/ieee-membership.ts
  - backendChapterCoreIEEE/src/auth/mappers/user.mapper.ts
  - specs/002-m1-perfil-ieee/spec.md
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Perfil de membresía IEEE

[[M1 - Identidad y acceso]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué es
> Los datos de la membresía IEEE de cada persona, guardados en la propia base de
> ChapterCore. IEEE no ofrece «Ingresar con IEEE» ni una API de validación gratuita,
> así que el perfil lo completa la persona y la Mesa Directiva lo verifica a mano
> ([[M1 - Verificación manual en vTools]]).

> [!info] Campos (confirmado en el código)
> | Dato | Dónde se guarda | Regla |
> |---|---|---|
> | Número de miembro | `users.ieee_member_number` | 6 a 12 dígitos (ya existía) |
> | Tipo (grado) | `users.ieee_membership_grade` | `student`, `graduate_student`, `member`, `senior_member`, `fellow`, `life`, `associate` |
> | Vencimiento | `users.ieee_membership_expires_at` | Fecha `aaaa-mm-dd`, opcional |
> | Verificación | `users.ieee_verified_at` / `ieee_verified_by` | Fecha y autor; se borra si cambian los datos |
> | Sociedades | tabla `user_ieee_societies` | Hasta 20, sin repetir, del catálogo `ieee_societies` |
>
> El **estado** no es una columna: se calcula. Ver [[M1 - Estado de la membresía IEEE]].

> [!success] Cómo se usa
> - La persona registra el número al activar su invitación (obligatorio) y completa
>   el resto en **«Mi perfil»** (`/perfil`), con `PATCH /auth/me/ieee`.
> - La API devuelve un bloque `ieee` dentro de cada usuario (`user.mapper.ts`) con
>   tipo, estado, vencimiento, verificación y sociedades.
> - Las sociedades del perfil son **pertenencia**, no el capítulo del cargo
>   (`chapter_id` sigue siendo el capítulo del cargo).

> [!warning] No confundir
> Pertenecer a una sociedad IEEE (perfil) no da permisos. Los permisos dependen solo
> del cargo y el ámbito ([[M1 - Niveles de acceso]]).

## Enlaces

- Código: [[M1 - ieee-membership]], [[M1 - Tabla users]], [[M1 - Tabla user_ieee_societies]],
  [[M1 - DTO UpdateIeeeProfileDto]], [[M1 - PATCH auth › me › ieee]], [[M1 - ProfilePage]].
- Catálogo de sociedades: [[M1 - Catálogo ieee_societies]] · [[M1 - GET access › societies]].
- Relacionada con [[M1 - Aprobación de invitaciones]] y [[M1 - Migraciones del perfil IEEE]].

## Fuentes

- `backendChapterCoreIEEE/src/auth/entities/user.entity.ts`
- `backendChapterCoreIEEE/src/auth/domain/ieee-membership.ts`
- `backendChapterCoreIEEE/src/auth/mappers/user.mapper.ts`
- `specs/002-m1-perfil-ieee/spec.md` (RF-IEEE-01 a RF-IEEE-09)
- `CONTEXTO.md`: hecho verificado el 2026-10-19 sobre la ausencia de OAuth/API de IEEE.
