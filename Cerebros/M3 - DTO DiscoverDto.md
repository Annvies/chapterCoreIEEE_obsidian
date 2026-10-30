---
type: dto
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/dto/discover.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - dto
---

# M3 - DTO DiscoverDto

[[M3 - DTO y validaciones]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dto
> Cuerpo de POST /opportunities/discover (contracts/api-rest.md).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `q` | `string` | no | `@Transform(({ value }: { value: unknown }) => (typeof value === 'string' ? value.trim() :…`, `@IsString()`, `@Length(1, 200)` |
| `estrategia` | `StrategyName` | sí | `@IsOptional()`, `@IsIn(STRATEGY_NAMES)` |

## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
