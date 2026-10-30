---
type: dto
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/dto/update-user.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - dto
---

# M1 - DTO UpdateUserDto

[[M1 - DTO y validaciones]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dto
> Enviar `cargo` (aunque sea null) reemplaza el cargo, ámbito y capítulo completos.

Hereda de `PositionFieldsDto`.

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `fullName` | `string` | sí | `@Trim()`, `@IsOptional()`, `@IsString()`, `@Length(1, 120, { message: 'El nombre debe tener entre 1 y 120 caracteres.' })` |

## Enlaces

- [[M1 - DTO PositionFieldsDto]]
- [[M1 - transforms]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
