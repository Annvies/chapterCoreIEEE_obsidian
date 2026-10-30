---
type: dto
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/dto/login.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - dto
---

# M1 - DTO LoginDto

[[M1 - DTO y validaciones]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dto
> Contrato de datos `LoginDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `email` | `string` | no | `@NormalizeEmail()`, `@IsEmail({}, { message: 'Ingresa un correo válido.' })`, `@MaxLength(254)` |
| `password` | `string` | no | `@IsString()`, `@MinLength(1, { message: 'Ingresa tu contraseña.' })`, `@MaxLength(200)` |
| `remember` | `boolean` | sí | `@IsOptional()`, `@IsBoolean()` |

## Enlaces

- [[M1 - transforms]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
