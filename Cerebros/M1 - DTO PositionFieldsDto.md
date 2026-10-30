---
type: dto
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/dto/invite-user.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - dto
---

# M1 - DTO PositionFieldsDto

[[M1 - DTO y validaciones]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dto
> La coherencia cargo/ámbito/capítulo se valida en UsersService (normalizePosition).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `cargo` | `Cargo \| null` | sí | `@IsOptional()`, `@IsIn(CARGOS, { message: 'El cargo no es válido.' })` |
| `ambito` | `Ambito \| null` | sí | `@IsOptional()`, `@IsIn(AMBITOS, { message: 'El ámbito debe ser rama o capitulo.' })` |
| `chapterId` | `number \| null` | sí | `@IsOptional()`, `@IsInt()`, `@Min(1)` |
| `ieeeMemberNumber` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@Matches(/^\d{6,12}$/, { message: 'El número de membresía IEEE debe tener entre 6 y 12 díg…` |

## Enlaces

- [[M1 - position]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
