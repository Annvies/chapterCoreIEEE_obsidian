---
type: concepto
modulo: 7
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/expenses/services/expenses.service.ts
  - backendChapterCoreIEEE/src/expenses/repositories/expenses.repository.ts
  - frontendChapterCoreIEEE/src/features/expenses/ExpensesPage.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - concepto
---

# M7 - Total gastado por periodo

[[M7 - Totales y filtros]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Qué es
> El resumen que devuelve `GET /expenses/summary`: total, cantidad de gastos y desglose
> por categoría, con los mismos filtros de periodo y alcance que el listado.

> [!info] Confirmado en el código
> - Suma en SQL: `COALESCE(SUM(monto), 0)` como `numeric(14,2)` convertido a texto, y el
>   desglose por categoría ordenado de mayor a menor total.
> - `desde` y `hasta` son opcionales (`aaaa-mm-dd`); si `desde` es posterior a `hasta`
>   responde «La fecha inicial no puede ser posterior a la final.» (`400`).
> - La respuesta repite `desde` y `hasta` (o `null`) para que la interfaz muestre el
>   periodo calculado.
> - La interfaz arranca con el mes en curso (`currentMonthRange`) y muestra «Sin gastos en
>   el periodo.» cuando no hay datos.

## Enlaces

- Forma parte de [[M7 - Totales y filtros]].
- Relacionada con [[M7 - Moneda y montos]], [[M7 - Alcance por capítulo de gastos]].

## Fuentes

- `backendChapterCoreIEEE/src/expenses/services/expenses.service.ts`
- `backendChapterCoreIEEE/src/expenses/repositories/expenses.repository.ts`
- `frontendChapterCoreIEEE/src/features/expenses/ExpensesPage.tsx`
