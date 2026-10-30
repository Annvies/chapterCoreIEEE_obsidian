---
type: módulo
modulo: 7
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/expenses/expense-schema.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - módulo
---

# M7 - expense-schema

[[M7 - Interfaz]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Módulo
> Mismas reglas que ExpenseInputDto del backend; el servidor sigue siendo quien decide.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ExpenseFormValues` | interface | Estado del modal: los inputs entregan texto. |
| `ExpenseFormErrors` | type | — |
| `buildExpenseSchema` | function | — |
| `validateExpense` | function | — |
| `currentMonthRange` | function | Periodo por defecto de la pantalla: el mes en curso, en la hora local. |


## Enlaces

- [[M7 - Tipos expenses]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
