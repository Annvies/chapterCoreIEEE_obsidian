---
type: tabla
modulo: 7
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792886400000-CreateExpensesModule.ts
  - backendChapterCoreIEEE/src/expenses/entities/expense.entity.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - tabla
---

# M7 - Tabla expenses

[[M7 - Base de datos]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Tabla
> Tabla `expenses` de PostgreSQL (13 columnas).

### Columnas

| Columna | Definición |
|---|---|
| `id` | `uuid PRIMARY KEY DEFAULT gen_random_uuid()` |
| `concepto` | `text NOT NULL CHECK (char_length(btrim(concepto)) BETWEEN 1 AND 200)` |
| `categoria` | `text NOT NULL CHECK (categoria IN ('evento', 'material', 'transporte', 'alimentacion', 'servicios', 'otro'))` |
| `monto` | `numeric(12,2) NOT NULL CHECK (monto > 0)` |
| `fecha` | `date NOT NULL` |
| `chapter_id` | `smallint REFERENCES ieee_societies(id) ON DELETE RESTRICT` |
| `comprobante_url` | `text CHECK (comprobante_url ~ '^https://' AND char_length(comprobante_url) <= 500)` |
| `notas` | `text CHECK (char_length(notas) <= 1000)` |
| `created_by` | `uuid REFERENCES users(id) ON DELETE SET NULL` |
| `deleted_at` | `timestamptz` |
| `deleted_by` | `uuid REFERENCES users(id) ON DELETE SET NULL` |
| `created_at` | `timestamptz NOT NULL DEFAULT now()` |
| `updated_at` | `timestamptz NOT NULL DEFAULT now()` |

### Índices

- `expenses_fecha_idx`: (fecha DESC, created_at DESC) WHERE deleted_at IS NULL
- `expenses_chapter_fecha_idx`: (chapter_id, fecha DESC) WHERE deleted_at IS NULL

### Origen

- `backendChapterCoreIEEE/src/database/migrations/1792886400000-CreateExpensesModule.ts`
- `backendChapterCoreIEEE/src/expenses/entities/expense.entity.ts`

## Enlaces

- [[M7 - Modelo de datos expenses]]
- [[M7 - Migración CreateExpensesModule]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
