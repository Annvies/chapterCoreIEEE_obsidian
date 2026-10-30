---
type: dto
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/dto/search-opportunities-query.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - dto
---

# M3 - DTO SearchOpportunitiesQueryDto

[[M3 - DTO y validaciones]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dto
> Contrato de datos `SearchOpportunitiesQueryDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `q` | `string` | sí | `@IsOptional()`, `@IsString()`, `@MaxLength(200)` |
| `tipo` | `OpportunityType` | sí | `@IsOptional()`, `@IsEnum(OpportunityType)` |
| `capitulo` | `string` | sí | `@IsOptional()`, `@IsString()`, `@MaxLength(20)` |
| `limit` | `number` | sí | `@IsOptional()`, `@Type(() => Number)`, `@IsInt()`, `@Min(1)`, `@Max(100)` |

## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
