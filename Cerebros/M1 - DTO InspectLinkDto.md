---
type: dto
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/dto/access-link.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - dto
---

# M1 - DTO InspectLinkDto

[[M1 - DTO y validaciones]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dto
> Los tokens viajan en el cuerpo (no en la URL) para que no queden en logs de acceso.

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `token` | `string` | no | `@IsString()`, `@Length(20, 200)` |

## Enlaces

- [[M1 - password-policy]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
