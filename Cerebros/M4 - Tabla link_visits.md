---
type: tabla
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792540800000-CreateDifusionModule.ts
  - backendChapterCoreIEEE/src/difusion/entities/link-visit.entity.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - tabla
---

# M4 - Tabla link_visits

[[M4 - Base de datos]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Tabla
> Tabla `link_visits` de PostgreSQL (5 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY` |
| `link_id` | `uuid NOT NULL` |
| `visited_at` | `timestamptz NOT NULL DEFAULT now()` |
| `origen` | `text NOT NULL` |
| `es_movil` | `boolean NOT NULL` |

### Restricciones

- `CONSTRAINT link_visits_link_id_fkey FOREIGN KEY (link_id) REFERENCES short_links(id) ON DELETE CASCADE`
- `CONSTRAINT link_visits_origen_check CHECK (origen IN ('qr', 'enlace'))`

### Índices

- `link_visits_link_id_visited_at_idx`: (link_id, visited_at)

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1792540800000-CreateDifusionModule.ts`
- `backendChapterCoreIEEE/src/difusion/entities/link-visit.entity.ts`

## Enlaces

- [[M4 - Modelo short_links y link_visits]]
- [[M4 - Migración CreateDifusionModule]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
