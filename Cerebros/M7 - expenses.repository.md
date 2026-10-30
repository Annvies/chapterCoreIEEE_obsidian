---
type: repositorio
modulo: 7
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/expenses/repositories/expenses.repository.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - repositorio
---

# M7 - expenses.repository

[[M7 - Lógica del backend]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Repositorio
> Archivo de repositorio del backend (`expenses/repositories/expenses.repository.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ExpenseFilterCriteria` | interface | — |
| `ExpenseSearchCriteria` | interface | — |
| `ExpenseTotals` | interface | — |
| `ExpensesRepository` | class | Acceso a datos de tesorería. Solo lee gastos vigentes (deleted_at IS NULL). |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `findById()` | Promise<Expense \| null> | — |
| `search()` | — | — |
| `summarize()` | Promise<ExpenseTotals> | Sumas en SQL sobre numeric: el total no pasa por coma flotante. |
| `create()` | Expense | — |
| `save()` | Promise<Expense> | — |
| `softDelete()` | Promise<boolean> | Eliminación lógica; false si no existe o ya estaba eliminado. |


## Enlaces

- [[M7 - expense]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
