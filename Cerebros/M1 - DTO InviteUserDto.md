---
type: dto
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/dto/invite-user.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - dto
---

# M1 - DTO InviteUserDto

[[M1 - DTO y validaciones]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dto
> Contrato de datos `InviteUserDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

Hereda de `PositionFieldsDto`.

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `email` | `string` | no | `@NormalizeEmail()`, `@IsEmail({}, { message: 'Ingresa un correo válido.' })`, `@MaxLength(254)` |
| `fullName` | `string` | no | `@Trim()`, `@IsString()`, `@Length(1, 120, { message: 'El nombre debe tener entre 1 y 120 caracteres.' })` |

## Enlaces

- [[M1 - DTO PositionFieldsDto]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
