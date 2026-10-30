---
type: dto
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/dto/list-users-query.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - dto
---

# M1 - DTO ListUsersQueryDto

[[M1 - DTO y validaciones]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dto
> Contrato de datos `ListUsersQueryDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `search` | `string` | sí | `@IsOptional()`, `@IsString()`, `@MaxLength(120)` |
| `level` | `AccessLevel` | sí | `@IsOptional()`, `@IsIn(ACCESS_LEVELS)` |
| `page` | `number` | sí | `@IsOptional()`, `@Type(() => Number)`, `@IsInt()`, `@Min(1)` |
| `limit` | `number` | sí | `@IsOptional()`, `@Type(() => Number)`, `@IsInt()`, `@Min(1)`, `@Max(100)` |

## Enlaces

- [[M1 - permissions]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
