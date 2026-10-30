---
type: dto
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/dto/list-sectors-query.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-2
  - dto
---

# M2 - DTO ListSectorsQueryDto

[[M2 - DTO y validaciones]] · [[Cerebro 2 - Contactos]]

> [!abstract] Dto
> Contrato de datos `ListSectorsQueryDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `tipo` | `ContactType` | sí | `@IsOptional()`, `@IsIn(CONTACT_TYPES)` |

## Enlaces

- [[M2 - contact]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
