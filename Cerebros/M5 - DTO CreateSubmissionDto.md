---
type: dto
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/dto/create-submission.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - dto
---

# M5 - DTO CreateSubmissionDto

[[M5 - DTO y validaciones]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Dto
> Contrato de datos `CreateSubmissionDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `respondentEmail` | `string` | no | `@IsEmail()`, `@MaxLength(320)` |
| `data` | `Record<string, unknown>` | no | `@IsObject()` |
| `submittedBy` | `string` | sí | `@IsOptional()`, `@IsUUID()` |

## Enlaces

- [[Cerebro 5 - Secretaría y formularios]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
