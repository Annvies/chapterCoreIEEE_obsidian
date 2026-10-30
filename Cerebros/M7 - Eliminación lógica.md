---
type: concepto
modulo: 7
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/expenses/controllers/expenses.controller.ts
  - backendChapterCoreIEEE/src/expenses/repositories/expenses.repository.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - concepto
---

# M7 - Eliminación lógica

[[M7 - Alcance y permisos]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Qué es
> Eliminar un gasto no borra la fila: la marca como eliminada para conservar quién y cuándo.

> [!info] Confirmado en el código
> - `DELETE /expenses/:id` exige acceso **Total** (solo Mesa Directiva) y responde `204`.
> - El repositorio guarda `deleted_at = now()` y `deleted_by` con la persona que elimina,
>   solo si el gasto seguía vigente; si no existe o ya estaba eliminado responde «El gasto
>   no existe.» (`404`).
> - Todas las consultas filtran `deleted_at IS NULL`: el gasto deja de listarse y de sumar.
> - En la interfaz, el botón de eliminar solo aparece con `can('expenses', 'total')`.

> [!tip] Corregir un error
> Como no hay edición, un Director que registró un gasto por error debe pedir a la Mesa
> Directiva que lo elimine y registrarlo de nuevo.

## Enlaces

- Forma parte de [[M7 - Alcance y permisos]].
- Relacionada con [[M7 - Modelo de datos expenses]], [[M7 - Total gastado por periodo]].

## Fuentes

- `backendChapterCoreIEEE/src/expenses/controllers/expenses.controller.ts`
- `backendChapterCoreIEEE/src/expenses/repositories/expenses.repository.ts`
- `frontendChapterCoreIEEE/src/features/expenses/ExpensesPage.tsx`
