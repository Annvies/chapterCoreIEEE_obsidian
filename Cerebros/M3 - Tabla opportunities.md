---
type: tabla
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792368000000-CreateOpportunities.ts
  - backendChapterCoreIEEE/src/database/migrations/1792454400000-UniqueOpportunityEnlace.ts
  - backendChapterCoreIEEE/src/opportunities/entities/opportunity.entity.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - tabla
---

# M3 - Tabla opportunities

[[M3 - Base de datos]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Tabla
> Tabla `opportunities` de PostgreSQL (15 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `uuid PRIMARY KEY DEFAULT gen_random_uuid()` |
| `titulo` | `text NOT NULL CHECK (char_length(btrim(titulo)) BETWEEN 1 AND 300)` |
| `tipo` | `opportunity_type NOT NULL` — valores: 'beca', 'concurso', 'voluntariado' |
| `fecha_limite` | `date` |
| `elegibilidad` | `text[] NOT NULL DEFAULT '{}' CHECK (cardinality(elegibilidad) <= 50 AND array_position(elegibilidad, NULL) IS NULL)` |
| `beneficio` | `text CHECK (beneficio IS NULL OR char_length(beneficio) <= 2000)` |
| `enlace` | `text NOT NULL CHECK (enlace ~ '^https://' AND char_length(enlace) <= 2048)` |
| `society_id` | `smallint REFERENCES ieee_societies(id) ON DELETE RESTRICT` |
| `fuente_url` | `text NOT NULL CHECK (fuente_url ~ '^https://' AND char_length(fuente_url) <= 2048)` |
| `fuente_consultada_at` | `timestamptz NOT NULL DEFAULT now()` |
| `estado` | `opportunity_status NOT NULL DEFAULT 'borrador'` — valores: 'borrador', 'publicada' |
| `published_at` | `timestamptz` |
| `created_at` | `timestamptz NOT NULL DEFAULT now()` |
| `updated_at` | `timestamptz NOT NULL DEFAULT now()` |
| `deleted_at` | `timestamptz` |

### Restricciones

- `CONSTRAINT published_at_coherente CHECK ((estado = 'publicada') = (published_at IS NOT NULL))`

### Índices

- `opportunities_society_id_idx`: (society_id)
- `opportunities_publicadas_fecha_idx`: (fecha_limite)  WHERE estado =
- único `opportunities_enlace_publicada_uq`: (enlace)  WHERE estado =

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1792368000000-CreateOpportunities.ts`
- `backendChapterCoreIEEE/src/database/migrations/1792454400000-UniqueOpportunityEnlace.ts`
- `backendChapterCoreIEEE/src/opportunities/entities/opportunity.entity.ts`

## Enlaces

- [[M3 - Modelo de datos opportunities]]
- [[M3 - Migración CreateOpportunities]]
- [[M3 - Migración UniqueOpportunityEnlace]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
