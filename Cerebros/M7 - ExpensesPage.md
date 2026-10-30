---
type: página
modulo: 7
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/expenses/ExpensesPage.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - página
---

# M7 - ExpensesPage

[[M7 - Interfaz]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Página
> Página del frontend (`frontendChapterCoreIEEE/src/features/expenses/ExpensesPage.tsx`).

Página de la aplicación. Ruta y permiso en [[M7 - Interfaz]].

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ExpensesPage` | function | Módulo 7 · Control de gastos y tesorería (specs/009-modulo-7-gastos-tesoreria). |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `summary` | sí | `ExpenseSummary \| null` |
| `isLoading` | sí | `boolean` |
| `error` | sí | `string \| null` |
| `onRetry` | sí | `): void` |


## Enlaces

- [[M7 - Cliente API expenses]]
- [[M7 - Tipos expenses]]
- [[M7 - expense-labels]]
- [[M7 - expense-schema]]
- [[M7 - ExpenseDialog]]
- [[M7 - ExpensesTable]]
- [[M7 - useExpenses]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
