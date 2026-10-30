---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/auth/dto/update-ieee-profile.dto.ts
  - backendChapterCoreIEEE/src/auth/dto/access-link.dto.ts
  - backendChapterCoreIEEE/src/auth/dto/list-users-query.dto.ts
  - backendChapterCoreIEEE/src/auth/dto/invite-user.dto.ts
  - frontendChapterCoreIEEE/src/types/auth.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Contratos del perfil IEEE

[[M1 - Permisos compartidos]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué es
> Los DTO y endpoints que agregó el perfil IEEE, con sus validaciones y el permiso
> que exige cada uno. El `ValidationPipe` global rechaza campos desconocidos.

> [!info] Endpoints nuevos o ampliados
> | Método y ruta | Permiso | Cuerpo / consulta | Respuesta |
> |---|---|---|---|
> | `PATCH /auth/me/ieee` | Sesión | `UpdateIeeeProfileDto` | Perfil propio |
> | `POST /users/:id/ieee/verify` | Usuarios · Total | — | Usuario verificado y aceptado (200) |
> | `GET /access/societies` | Sesión | — | Catálogo `ieee_societies` |
> | `GET /users?pending=true` | Usuarios · Total | `ListUsersQueryDto.pending` | Solicitudes + `pendingCount` |
> | `POST /auth/links/password` | Público | `SetPasswordDto.ieeeMemberNumber` | Sesión o `{ pendingApproval: true }` |

> [!success] Validaciones de los DTO
> - **`UpdateIeeeProfileDto`**: `ieeeMemberNumber` 6–12 dígitos; `grade` uno de los 7
>   grados; `expiresAt` `aaaa-mm-dd` válido; `societyIds` arreglo de enteros ≥ 1, sin
>   repetir, máximo 20. Los campos omitidos no cambian; `''` se convierte en `null`.
> - **`SetPasswordDto.ieeeMemberNumber`**: opcional en el DTO, pero el servicio lo
>   exige al activar una invitación.
> - **`ListUsersQueryDto.pending`**: solo la cadena `"true"` activa el filtro.
> - **`InviteUserDto` / `UpdateUserDto`**: `ieeeMemberNumber` se acepta por
>   compatibilidad, pero se **ignora** (lo registra la propia persona).

> [!tip] En el frontend
> Los tipos `IeeeProfile`, `IeeeStatus`, `IeeeGrade`, `PendingApproval` y
> `UpdateIeeeProfileInput` están en `types/auth.ts`; las llamadas, en `api/auth.ts`
> (`updateMyIeeeProfile`, `verifyUserIeee`, `fetchIeeeSocieties`).

## Enlaces

- DTO: [[M1 - DTO UpdateIeeeProfileDto]], [[M1 - DTO SetPasswordDto]],
  [[M1 - DTO ListUsersQueryDto]], [[M1 - DTO InviteUserDto]].
- Endpoints: [[M1 - PATCH auth › me › ieee]], [[M1 - POST users › {id} › ieee › verify]],
  [[M1 - GET access › societies]], [[M1 - GET users]], [[M1 - POST auth › links › password]].
- Frontend: [[M1 - Tipos auth]], [[M1 - Cliente API auth]].
- Grupos técnicos: [[M1 - API]], [[M1 - DTO y validaciones]].

## Fuentes

- `backendChapterCoreIEEE/src/auth/dto/update-ieee-profile.dto.ts`
- `backendChapterCoreIEEE/src/auth/dto/access-link.dto.ts`
- `backendChapterCoreIEEE/src/auth/dto/list-users-query.dto.ts`
- `backendChapterCoreIEEE/src/auth/dto/invite-user.dto.ts`
- `frontendChapterCoreIEEE/src/types/auth.ts`, `frontendChapterCoreIEEE/src/api/auth.ts`
