---
type: dto
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/dto/extract-opportunity.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - dto
---

# M3 - DTO ExtractOpportunityDto

[[M3 - DTO y validaciones]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dto
> Contrato de datos `ExtractOpportunityDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `url` | `string` | no | `@Transform(({ value }: { value: unknown }) => (typeof value === 'string' ? value.trim() :…`, `@IsString()`, `@MaxLength(2048)`, `@IsOfficialIeeeUrl()` |

## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
