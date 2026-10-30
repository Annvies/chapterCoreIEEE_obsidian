---
type: dto
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/dto/create-opportunity.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - dto
---

# M3 - DTO CreateOpportunityDto

[[M3 - DTO y validaciones]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dto
> PRUEBA DE HOOK Ficha revisada por una persona en la vista previa (mockup 05). Los nombres siguen la ficha de CONTEXTO.md §7. estado/published_at no se reciben: los fija el servidor.

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `titulo` | `string` | no | `@Transform(trim)`, `@IsString()`, `@IsNotEmpty()`, `@MaxLength(300)` |
| `tipo` | `OpportunityType` | no | `@IsEnum(OpportunityType)` |
| `fecha_limite` | `string \| null` | sí | `@IsOptional()`, `@IsDateString({ strict: true })` |
| `elegibilidad` | `string[]` | sí | `@IsOptional()`, `@Transform(({ value }: { value: unknown }) => Array.isArray(value) ? value.map((item) => (…`, `@IsArray()`, `@ArrayMaxSize(50)`, `@IsString({ each: true })`, `@MaxLength(500, { each: true })` |
| `beneficio` | `string \| null` | sí | `@IsOptional()`, `@Transform(trim)`, `@IsString()`, `@MaxLength(2000)` |
| `enlace` | `string` | no | `@IsOfficialIeeeUrl()`, `@MaxLength(2048)` |
| `capitulo` | `string \| null` | sí | `@IsOptional()`, `@IsString()`, `@MaxLength(20)` |
| `fuente_url` | `string` | no | `@IsOfficialIeeeUrl()`, `@MaxLength(2048)` |

## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
