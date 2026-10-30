---
type: cliente API
modulo: 7
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/api/expenses.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - cliente-API
---

# M7 - Cliente API expenses

[[M7 - Interfaz]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Cliente API
> Cliente api del frontend (`frontendChapterCoreIEEE/src/api/expenses.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `listExpenses` | function | — |
| `fetchExpenseSummary` | function | — |
| `createExpense` | function | — |
| `deleteExpense` | function | — |

### Llamadas a la API

| Función | Método | Ruta |
|---|---|---|
| `listExpenses()` | `GET` | `/expenses` |
| `fetchExpenseSummary()` | `GET` | `/expenses/summary` |
| `createExpense()` | `POST` | `/expenses` |
| `deleteExpense()` | `DELETE` | `/expenses/:p` |


## Enlaces

- [[M7 - Tipos expenses]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
