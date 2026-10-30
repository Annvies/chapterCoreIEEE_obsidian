---
type: dto
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/dto/list-forms-query.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - dto
---

# M5 - DTO ListFormsQueryDto

[[M5 - DTO y validaciones]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Dto
> Contrato de datos `ListFormsQueryDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

Hereda de `PaginationQueryDto`.

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `status` | `FormStatus` | sí | `@IsOptional()`, `@IsIn(FORM_STATUSES)` |
| `search` | `string` | sí | `@IsOptional()`, `@IsString()`, `@MaxLength(120)` |

## Enlaces

- [[M5 - DTO PaginationQueryDto]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
