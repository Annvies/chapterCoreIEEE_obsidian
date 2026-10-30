---
type: tabla
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792540800000-CreateDifusionModule.ts
  - backendChapterCoreIEEE/src/difusion/entities/short-link.entity.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - tabla
---

# M4 - Tabla short_links

[[M4 - Base de datos]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Tabla
> Tabla `short_links` de PostgreSQL (9 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `uuid PRIMARY KEY DEFAULT gen_random_uuid()` |
| `codigo` | `text NOT NULL` |
| `nombre` | `text NOT NULL` |
| `destino_url` | `text NOT NULL` |
| `tipo` | `short_link_type NOT NULL` — valores: 'qr_dinamico', 'enlace_oficial' |
| `estado` | `short_link_status NOT NULL DEFAULT 'activo'` — valores: 'activo', 'pausado' |
| `estilo` | `qr_style NOT NULL DEFAULT 'azul'` — valores: 'azul', 'navy', 'cian' |
| `created_at` | `timestamptz NOT NULL DEFAULT now()` |
| `updated_at` | `timestamptz NOT NULL DEFAULT now()` |

### Restricciones

- `CONSTRAINT short_links_codigo_key UNIQUE (codigo)`
- `CONSTRAINT short_links_codigo_check CHECK (codigo ~ '^[a-z0-9]+(-[a-z0-9]+)*$' AND char_length(codigo) BETWEEN 3 AND 40)`
- `CONSTRAINT short_links_nombre_check CHECK (char_length(btrim(nombre)) BETWEEN 1 AND 120)`
- `CONSTRAINT short_links_destino_url_check CHECK (destino_url ~ '^https?://' AND char_length(destino_url) <= 2048)`

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1792540800000-CreateDifusionModule.ts`
- `backendChapterCoreIEEE/src/difusion/entities/short-link.entity.ts`

## Enlaces

- [[M4 - Modelo short_links y link_visits]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
