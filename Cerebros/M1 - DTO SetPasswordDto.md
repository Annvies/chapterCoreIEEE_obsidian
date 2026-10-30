---
type: dto
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/dto/access-link.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - dto
---

# M1 - DTO SetPasswordDto

[[M1 - DTO y validaciones]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dto
> Contrato de datos `SetPasswordDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

Hereda de `InspectLinkDto`.

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `password` | `string` | no | `@IsString()`, `@Length(PASSWORD_MIN_LENGTH, 72, { message: PASSWORD_POLICY_MESSAGE })`, `@Matches(PASSWORD_PATTERN, { message: PASSWORD_POLICY_MESSAGE })` |
| `ieeeMemberNumber` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@Matches(/^\d{6,12}$/, { message: 'El número de membresía IEEE debe tener entre 6 y 12 díg…` |

## Enlaces

- [[M1 - DTO InspectLinkDto]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
