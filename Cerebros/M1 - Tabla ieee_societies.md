---
type: tabla
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792368000000-CreateOpportunities.ts
  - backendChapterCoreIEEE/src/opportunities/entities/ieee-society.entity.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - tabla
---

# M1 - Tabla ieee_societies

[[M1 - Base de datos]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Tabla
> Tabla `ieee_societies` de PostgreSQL (6 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `smallint GENERATED ALWAYS AS IDENTITY PRIMARY KEY` |
| `sigla` | `text NOT NULL UNIQUE` |
| `nombre_oficial` | `text NOT NULL UNIQUE` |
| `tipo` | `text NOT NULL CHECK (tipo IN ('sociedad', 'grupo_afinidad'))` |
| `sitio_oficial` | `text NOT NULL CHECK (sitio_oficial ~ '^https://')` |
| `created_at` | `timestamptz NOT NULL DEFAULT now()` |

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1792368000000-CreateOpportunities.ts`
- `backendChapterCoreIEEE/src/opportunities/entities/ieee-society.entity.ts`

## Enlaces

- [[M1 - Catálogo ieee_societies]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
