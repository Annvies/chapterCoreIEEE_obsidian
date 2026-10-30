---
type: dto
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/dto/update-ieee-profile.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - dto
---

# M1 - DTO UpdateIeeeProfileDto

[[M1 - DTO y validaciones]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dto
> Perfil IEEE que edita la propia persona. Los campos omitidos no cambian.

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `ieeeMemberNumber` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@Matches(/^\d{6,12}$/, { message: 'El número de membresía IEEE debe tener entre 6 y 12 díg…` |
| `grade` | `IeeeGrade \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@IsIn(IEEE_GRADES, { message: 'El grado de membresía IEEE no es válido.' })` |
| `expiresAt` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@Matches(/^\d{4}-\d{2}-\d{2}$/, { message: 'La fecha de vencimiento debe ser aaaa-mm-dd.'…`, `@IsDateString({ strict: true }, { message: 'La fecha de vencimiento no es válida.' })` |
| `societyIds` | `number[] \| null` | sí | `@IsOptional()`, `@IsArray()`, `@ArrayMaxSize(20, { message: 'Puedes indicar hasta 20 sociedades.' })`, `@ArrayUnique({ message: 'Hay sociedades repetidas.' })`, `@IsInt({ each: true })`, `@Min(1, { each: true })` |

## Enlaces

- [[M1 - ieee-membership]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
