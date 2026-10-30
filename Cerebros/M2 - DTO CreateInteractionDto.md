---
type: dto
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/dto/create-interaction.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-2
  - dto
---

# M2 - DTO CreateInteractionDto

[[M2 - DTO y validaciones]] · [[Cerebro 2 - Contactos]]

> [!abstract] Dto
> Contrato de datos `CreateInteractionDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `tipo` | `InteractionType` | no | `@IsIn(INTERACTION_TYPES, { message: 'El tipo de registro no es válido.' })` |
| `descripcion` | `string` | no | `@Trim()`, `@IsString()`, `@Length(1, CONTACT_LIMITS.interaccion, { message: `La descripción debe tener entre 1 y ${C…` |
| `fecha` | `string` | sí | `@IsOptional()`, `@Matches(/^\d{4}-\d{2}-\d{2}$/, { message: 'La fecha debe tener formato aaaa-mm-dd.' })` |

## Enlaces

- [[M2 - contact]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
