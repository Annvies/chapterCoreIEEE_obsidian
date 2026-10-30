---
type: componente
modulo: 7
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/expenses/ExpensesTable.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - componente
---

# M7 - ExpensesTable

[[M7 - Interfaz]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/expenses/ExpensesTable.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ExpensesTable` | function | — |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `data` | sí | `ExpenseList \| null` |
| `isLoading` | sí | `boolean` |
| `error` | sí | `string \| null` |
| `canDelete` | sí | `boolean` |
| `deletingId` | sí | `string \| null` |
| `onDelete` | sí | `expense: Expense): void` |
| `onRetry` | sí | `): void` |
| `onPageChange` | sí | `page: number): void` |


## Enlaces

- [[M7 - Tipos expenses]]
- [[M7 - expense-labels]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
