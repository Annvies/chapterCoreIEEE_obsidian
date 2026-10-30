---
type: dto
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/dto/list-submissions-query.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-5
  - dto
---

# M5 - DTO ListSubmissionsQueryDto

[[M5 - DTO y validaciones]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Dto
> Contrato de datos `ListSubmissionsQueryDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

Hereda de `PaginationQueryDto`.

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `status` | `SubmissionStatus` | sí | `@IsOptional()`, `@IsIn(SUBMISSION_STATUSES)` |
| `search` | `string` | sí | `@IsOptional()`, `@IsString()`, `@MaxLength(320)` |
| `from` | `string` | sí | `@IsOptional()`, `@IsISO8601()` |
| `to` | `string` | sí | `@IsOptional()`, `@IsISO8601()` |

## Enlaces

- [[M5 - DTO PaginationQueryDto]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
