---
type: dto
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/difusion/dto/short-link.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-4
  - dto
---

# M4 - DTO LinkStatsQueryDto

[[M4 - DTO y validaciones]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Dto
> Contrato de datos `LinkStatsQueryDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `dias` | `number` | sí | `@IsOptional()`, `@Type(() => Number)`, `@IsInt()`, `@Min(1)`, `@Max(90)` |
| `tz` | `string` | sí | `@IsOptional()`, `@IsString()`, `@MaxLength(64)`, `@Matches(/^[A-Za-z_]+(?:\/[A-Za-z0-9_+-]+)*$/, { message: 'tz debe ser una zona horaria IA…` |

## Enlaces

- [[Cerebro 4 - Difusión y QR]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
