---
type: dto
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/dto/update-submission-review.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - dto
---

# M5 - DTO UpdateSubmissionReviewDto

[[M5 - DTO y validaciones]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Dto
> Contrato de datos `UpdateSubmissionReviewDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `status` | `SubmissionStatus` | no | `@IsIn(SUBMISSION_STATUSES)` |
| `notes` | `string` | sí | `@IsOptional()`, `@IsString()`, `@MaxLength(2000)` |

## Enlaces

- [[Cerebro 5 - Secretaría y formularios]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
