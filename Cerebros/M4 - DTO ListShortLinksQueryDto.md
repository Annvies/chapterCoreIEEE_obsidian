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

# M4 - DTO ListShortLinksQueryDto

[[M4 - DTO y validaciones]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Dto
> Contrato de datos `ListShortLinksQueryDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `tipo` | `ShortLinkType` | sí | `@IsOptional()`, `@IsEnum(ShortLinkType)` |
| `estado` | `ShortLinkStatus` | sí | `@IsOptional()`, `@IsEnum(ShortLinkStatus)` |

## Enlaces

- [[Cerebro 4 - Difusión y QR]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
