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

# M4 - DTO UpdateShortLinkDto

[[M4 - DTO y validaciones]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Dto
> «Editar destino» / «Editar» del mockup 06. El código no cambia: ya está impreso.

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `nombre` | `string` | sí | `@IsOmittable()`, `@Transform(trim)`, `@IsString()`, `@IsNotEmpty()`, `@MaxLength(120)` |
| `destino_url` | `string` | sí | `@IsOmittable()`, `@Transform(url)`, `@IsRedirectableUrl()`, `@MaxLength(2048)` |
| `estado` | `ShortLinkStatus` | sí | `@IsOmittable()`, `@IsEnum(ShortLinkStatus)` |
| `estilo` | `QrStyle` | sí | `@IsOmittable()`, `@IsEnum(QrStyle)` |

## Enlaces

- [[Cerebro 4 - Difusión y QR]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
