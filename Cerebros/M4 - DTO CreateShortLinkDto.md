---
type: dto
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/difusion/dto/short-link.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - dto
---

# M4 - DTO CreateShortLinkDto

[[M4 - DTO y validaciones]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Dto
> Formularios «Nuevo QR dinámico» y «Enlaces oficiales» del mockup 06.

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `nombre` | `string` | no | `@Transform(trim)`, `@IsString()`, `@IsNotEmpty()`, `@MaxLength(120)` |
| `destino_url` | `string` | no | `@Transform(url)`, `@IsRedirectableUrl()`, `@MaxLength(2048)` |
| `tipo` | `ShortLinkType` | no | `@IsEnum(ShortLinkType)` |
| `alias` | `string` | sí | `@IsOptional()`, `@Transform(lower)`, `@IsString()`, `@MinLength(CODE_MIN_LENGTH)`, `@MaxLength(CODE_MAX_LENGTH)`, `@Matches(CODE_PATTERN, { message: 'alias solo admite minúsculas, números y guiones (sin gu…` |
| `estilo` | `QrStyle` | sí | `@IsOptional()`, `@IsEnum(QrStyle)` |

## Enlaces

- [[Cerebro 4 - Difusión y QR]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
