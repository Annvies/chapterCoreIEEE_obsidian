---
type: dto
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/dto/update-user.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - dto
---

# M1 - DTO UpdateUserStatusDto

[[M1 - DTO y validaciones]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dto
> Contrato de datos `UpdateUserStatusDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `status` | `UserStatus.Active \| UserStatus.Disabled` | no | `@IsIn([UserStatus.Active, UserStatus.Disabled], { message: 'El estado debe ser active o di…` |

## Enlaces

- [[Cerebro 1 - Base institucional]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
