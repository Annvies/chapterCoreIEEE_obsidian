---
type: tabla
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792713600000-AddIeeeMembershipToUsers.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - tabla
---

# M1 - Tabla user_ieee_societies

[[M1 - Base de datos]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Tabla
> Tabla `user_ieee_societies` de PostgreSQL (3 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `user_id` | `uuid NOT NULL REFERENCES users(id) ON DELETE CASCADE` |
| `society_id` | `smallint NOT NULL REFERENCES ieee_societies(id) ON DELETE RESTRICT` |
| `PRIMARY` | `KEY (user_id, society_id)` |

### Índices

- `user_ieee_societies_society_id_idx`: (society_id)

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1792713600000-AddIeeeMembershipToUsers.ts`

## Enlaces

- [[M1 - Migración AddIeeeMembershipToUsers]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
