---
type: concepto
modulo: 7
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792886400000-CreateExpensesModule.ts
  - backendChapterCoreIEEE/src/expenses/entities/expense.entity.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - concepto
---

# M7 - Modelo de datos expenses

[[M7 - Registro de gastos]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Qué es
> Única tabla del Módulo 7. Cada fila es un gasto de la Rama o de un capítulo.

> [!info] Confirmado en la migración
> | Columna | Regla |
> |---|---|
> | `id` | `uuid`, generado con `gen_random_uuid()` |
> | `concepto` | texto de 1 a 200 caracteres (sin contar espacios de los extremos) |
> | `categoria` | una de `evento`, `material`, `transporte`, `alimentacion`, `servicios`, `otro` |
> | `monto` | `numeric(12,2)`, mayor que 0 |
> | `fecha` | `date` (fecha de calendario del gasto) |
> | `chapter_id` | `smallint` hacia `ieee_societies`; vacío = gasto de la Rama; `ON DELETE RESTRICT` |
> | `comprobante_url` | opcional, debe empezar por `https://`, máximo 500 caracteres |
> | `notas` | opcional, máximo 1000 caracteres |
> | `created_by` · `deleted_by` | hacia `users`, `ON DELETE SET NULL` |
> | `deleted_at` | marca de [[M7 - Eliminación lógica]] |
> | `created_at` · `updated_at` | `timestamptz`, por defecto `now()` |
>
> Dos índices parciales (`WHERE deleted_at IS NULL`): por `fecha DESC, created_at DESC` y
> por `chapter_id, fecha DESC`. Las consultas solo leen gastos vigentes.

> [!tip] Relación con otros módulos
> El alcance reutiliza el catálogo `ieee_societies` y la autoría la tabla `users`, ambos del
> [[Cerebro 1 - Base institucional]].

## Enlaces

- Forma parte de [[M7 - Registro de gastos]].
- Relacionada con [[M7 - Categorías y validaciones]], [[M7 - Moneda y montos]].

## Fuentes

- `backendChapterCoreIEEE/src/database/migrations/1792886400000-CreateExpensesModule.ts`
- `backendChapterCoreIEEE/src/expenses/entities/expense.entity.ts`
