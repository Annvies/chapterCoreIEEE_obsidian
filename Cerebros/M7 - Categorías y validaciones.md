---
type: concepto
modulo: 7
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/expenses/domain/expense.ts
  - backendChapterCoreIEEE/src/expenses/dto/expense-input.dto.ts
  - backendChapterCoreIEEE/src/expenses/services/expenses.service.ts
  - frontendChapterCoreIEEE/src/features/expenses/expense-schema.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - concepto
---

# M7 - Categorías y validaciones

[[M7 - Registro de gastos]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Qué es
> Las reglas que debe cumplir un gasto antes de guardarse. Las reglas puras viven en
> `expenses/domain/expense.ts`, sin Nest ni TypeORM, para probarlas sin base de datos.

> [!info] Confirmado en el código
> - **Categorías** (`ExpenseCategory`): `evento`, `material`, `transporte`,
>   `alimentacion`, `servicios`, `otro`.
> - **Límites** (`EXPENSE_LIMITS`): concepto 200, notas 1000 y comprobante 500 caracteres.
> - **Monto:** de 0,01 a `MAX_MONTO` = 9 999 999 999,99 (máximo de `numeric(12,2)`).
> - **Fecha:** formato `aaaa-mm-dd`; el servicio rechaza fechas inválidas («La fecha no es
>   válida.») y futuras («La fecha no puede ser futura.»).
> - **Capítulo:** si se indica, debe existir («El capítulo seleccionado no existe.»).
> - **Comprobante:** solo un enlace `https`; ChapterCore no lo abre ni lo verifica.
> - Los campos opcionales vacíos se guardan como `null` (`@EmptyToNull()`).

## Enlaces

- Forma parte de [[M7 - Registro de gastos]].
- Relacionada con [[M7 - Modelo de datos expenses]], [[M7 - Alcance por capítulo de gastos]].

## Fuentes

- `backendChapterCoreIEEE/src/expenses/domain/expense.ts`
- `backendChapterCoreIEEE/src/expenses/dto/expense-input.dto.ts`
- `backendChapterCoreIEEE/src/expenses/services/expenses.service.ts`
- `frontendChapterCoreIEEE/src/features/expenses/expense-schema.ts`
