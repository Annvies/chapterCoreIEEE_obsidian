---
type: dto
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/dto/contact.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-2
  - dto
---

# M2 - DTO ContactInputDto

[[M2 - DTO y validaciones]] · [[Cerebro 2 - Contactos]]

> [!abstract] Dto
> Alta y edición comparten el mismo cuerpo: la edición reemplaza todos los campos.

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `tipo` | `ContactType` | no | `@IsIn(CONTACT_TYPES, { message: 'El tipo debe ser empresa, alumni, conferencista o autorid…` |
| `nombre` | `string` | no | `@Trim()`, `@IsString()`, `@Length(1, CONTACT_LIMITS.nombre, { message: `El nombre debe tener entre 1 y ${CONTACT_LIM…` |
| `organizacion` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@IsString()`, `@MaxLength(CONTACT_LIMITS.organizacion)` |
| `contactoNombre` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@IsString()`, `@MaxLength(CONTACT_LIMITS.contactoNombre)` |
| `cargo` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@IsString()`, `@MaxLength(CONTACT_LIMITS.cargo)` |
| `correo` | `string \| null` | sí | `@OptionalEmail()`, `@IsOptional()`, `@IsEmail({}, { message: 'Ingresa un correo válido.' })`, `@MaxLength(CONTACT_LIMITS.correo)` |
| `telefono` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@IsString()`, `@MaxLength(CONTACT_LIMITS.telefono)` |
| `sector` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@IsString()`, `@MaxLength(CONTACT_LIMITS.sector)` |
| `ciudad` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@IsString()`, `@MaxLength(CONTACT_LIMITS.ciudad)` |
| `estado` | `RelationshipStatus \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@IsIn(RELATIONSHIP_STATUSES, { message: 'El estado no es válido.' })` |
| `convenio` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@IsString()`, `@MaxLength(CONTACT_LIMITS.convenio)` |
| `convenioVence` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@Matches(ISO_DATE, { message: 'La fecha de vencimiento debe tener formato aaaa-mm-dd.' })` |
| `chapterId` | `number \| null` | sí | `@IsOptional()`, `@IsInt()`, `@Min(1)` |
| `notas` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@IsString()`, `@MaxLength(CONTACT_LIMITS.notas)` |

## Enlaces

- [[M2 - contact]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
