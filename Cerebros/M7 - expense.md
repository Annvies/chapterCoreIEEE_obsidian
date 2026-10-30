---
type: dominio
modulo: 7
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/expenses/domain/expense.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - dominio
---

# M7 - expense

[[M7 - Lógica del backend]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Dominio
> Módulo 7 · Control de gastos y tesorería (specs/009-modulo-7-gastos-tesoreria). Reglas puras: sin Nest ni TypeORM, para probarlas sin base de datos.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ExpenseCategory` | enum | — |
| `EXPENSE_CATEGORIES` | const | — |
| `EXPENSE_LIMITS` | const | — |
| `MAX_MONTO` | const | Máximo de la columna numeric(12,2). |
| `DEFAULT_PAGE_SIZE` | const | — |
| `MAX_PAGE_SIZE` | const | — |
| `RAMA_SCOPE` | const | Valor del filtro `alcance` para los gastos sin capítulo. |
| `RequestedScope` | type | Alcance pedido: sin filtro, la Rama o el id de un capítulo. |
| `ExpenseScope` | type | — |
| `parseRequestedScope` | function | `alcance` ya validado por el DTO ('rama' o un entero positivo). |
| `resolveExpenseScope` | function | Alcance efectivo de una consulta o registro. Si la celda de la matriz es "chapterOnly" (Director de capítulo), la persona queda limitada a su capítulo. |


## Enlaces

- [[Cerebro 7 - Tesorería y Gastos]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
