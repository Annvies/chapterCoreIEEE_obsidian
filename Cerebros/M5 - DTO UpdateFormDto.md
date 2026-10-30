---
type: dto
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/dto/update-form.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-5
  - dto
---

# M5 - DTO UpdateFormDto

[[M5 - DTO y validaciones]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Dto
> Contrato de datos `UpdateFormDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `slug` | `string` | sí | `@IsOptional()`, `@IsString()`, `@MinLength(3)`, `@MaxLength(140)`, `@Matches(SLUG_PATTERN, { message: 'El slug solo admite minusculas, numeros y guiones simpl…` |
| `title` | `string` | sí | `@IsOptional()`, `@IsString()`, `@MinLength(3)`, `@MaxLength(200)` |
| `description` | `string` | sí | `@IsOptional()`, `@IsString()`, `@MaxLength(5000)` |
| `schema` | `FormSchema` | sí | `@IsOptional()`, `@IsObject()` |

## Enlaces

- [[Cerebro 5 - Secretaría y formularios]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
