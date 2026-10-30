---
type: tabla
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792972800000-CreateOpportunitySearchHistory.ts
  - backendChapterCoreIEEE/src/opportunities/discovery/entities/opportunity-search.entity.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - tabla
---

# M3 - Tabla opportunity_searches

[[M3 - Base de datos]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Tabla
> Tabla `opportunity_searches` de PostgreSQL (8 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `uuid PRIMARY KEY DEFAULT gen_random_uuid()` |
| `user_id` | `uuid NOT NULL` |
| `consulta` | `text NOT NULL` |
| `estrategia` | `discovery_strategy` — valores: 'busqueda_sitio', 'estaticas', 'navegador', 'catalogo' |
| `forzada` | `boolean NOT NULL DEFAULT false` |
| `intentos` | `jsonb NOT NULL` |
| `resultados` | `jsonb NOT NULL` |
| `created_at` | `timestamptz NOT NULL DEFAULT now()` |

### Restricciones

- `CONSTRAINT opportunity_searches_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE`
- `CONSTRAINT opportunity_searches_consulta_check CHECK (char_length(btrim(consulta)) BETWEEN 1 AND 200)`
- `CONSTRAINT opportunity_searches_intentos_check CHECK (jsonb_typeof(intentos) = 'array')`
- `CONSTRAINT opportunity_searches_resultados_check CHECK (jsonb_typeof(resultados) = 'array' AND jsonb_array_length(resultados) <= 20)`

### Índices

- `opportunity_searches_user_created_idx`: (user_id, created_at)

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1792972800000-CreateOpportunitySearchHistory.ts`
- `backendChapterCoreIEEE/src/opportunities/discovery/entities/opportunity-search.entity.ts`

## Enlaces

- [[M3 - Historial de búsquedas]]
- [[M3 - Migración CreateOpportunitySearchHistory]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
