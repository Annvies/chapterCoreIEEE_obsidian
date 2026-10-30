---
type: dto
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/dto/pagination.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - dto
---

# M5 - DTO PaginationQueryDto

[[M5 - DTO y validaciones]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Dto
> Contrato de datos `PaginationQueryDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `page` | `number = 1` | sí | `@IsOptional()`, `@Type(() => Number)`, `@IsInt()`, `@Min(1)` |
| `limit` | `number = 20` | sí | `@IsOptional()`, `@Type(() => Number)`, `@IsInt()`, `@Min(1)`, `@Max(100)` |

## Enlaces

- [[Cerebro 5 - Secretaría y formularios]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
