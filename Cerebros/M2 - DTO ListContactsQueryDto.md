---
type: dto
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/dto/list-contacts-query.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-2
  - dto
---

# M2 - DTO ListContactsQueryDto

[[M2 - DTO y validaciones]] · [[Cerebro 2 - Contactos]]

> [!abstract] Dto
> Contrato de datos `ListContactsQueryDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `tipo` | `ContactType` | sí | `@IsOptional()`, `@IsIn(CONTACT_TYPES)` |
| `search` | `string` | sí | `@IsOptional()`, `@IsString()`, `@MaxLength(120)` |
| `estado` | `RelationshipStatus` | sí | `@IsOptional()`, `@IsIn(RELATIONSHIP_STATUSES)` |
| `sector` | `string` | sí | `@IsOptional()`, `@IsString()`, `@MaxLength(80)` |
| `chapterId` | `number` | sí | `@IsOptional()`, `@Type(() => Number)`, `@IsInt()`, `@Min(1)` |
| `lastContact` | `LastContactFilter` | sí | `@IsOptional()`, `@IsIn(LAST_CONTACT_FILTERS)` |
| `page` | `number` | sí | `@IsOptional()`, `@Type(() => Number)`, `@IsInt()`, `@Min(1)` |
| `limit` | `number` | sí | `@IsOptional()`, `@Type(() => Number)`, `@IsInt()`, `@Min(1)`, `@Max(100)` |

## Enlaces

- [[M2 - contact]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
