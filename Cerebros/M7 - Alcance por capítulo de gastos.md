---
type: concepto
modulo: 7
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/expenses/domain/expense.ts
  - backendChapterCoreIEEE/src/expenses/dto/expense-summary-query.dto.ts
  - frontendChapterCoreIEEE/src/features/expenses/ExpensesPage.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - concepto
---

# M7 - Alcance por capítulo de gastos

[[M7 - Alcance y permisos]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Qué es
> Cómo decide el servidor qué gastos ve o registra cada persona. Lo resuelve
> `resolveExpenseScope` leyendo la marca `chapterOnly` de la matriz, el mismo patrón que
> usa el dashboard del [[Cerebro 6 - Feedback y KPIs]].

> [!info] Confirmado en el código
> - El filtro `alcance` acepta `rama` (gastos sin capítulo) o el id de un capítulo
>   (`^(rama|[1-9]\d{0,4})$`); sin filtro se ven todos.
> - **Director de capítulo** (`chapterOnly`): queda limitado a su capítulo aunque no envíe
>   filtro. Si pide otro alcance recibe «Solo puedes gestionar los gastos de tu
>   capítulo.» y, si su cargo no tiene capítulo, «Tu cargo no tiene un capítulo
>   asignado.» (ambos `403`).
> - La interfaz carga el selector de capítulos con `GET /contacts/chapters` del
>   [[Cerebro 2 - Contactos]]; para el Director no hace esa llamada
>   (`ExpensesPage.test.tsx`).

## Enlaces

- Forma parte de [[M7 - Alcance y permisos]].
- Relacionada con [[M7 - Categorías y validaciones]], [[M7 - Total gastado por periodo]].

## Fuentes

- `backendChapterCoreIEEE/src/expenses/domain/expense.ts`
- `backendChapterCoreIEEE/src/expenses/dto/expense-summary-query.dto.ts`
- `frontendChapterCoreIEEE/src/features/expenses/ExpensesPage.tsx`
