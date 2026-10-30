---
type: servicio
modulo: 7
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/expenses/services/expenses.service.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - servicio
---

# M7 - expenses.service

[[M7 - Lógica del backend]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Servicio
> Archivo de servicio del backend (`expenses/services/expenses.service.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ExpenseListView` | interface | — |
| `ExpensesService` | class | Tesorería (Módulo 7). El PermissionsGuard aplica el nivel de acceso; este servicio aplica además el alcance "su capítulo" del Director (resolveExpenseScope). |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `list()` | Promise<ExpenseListView> | — |
| `summary()` | — | — |
| `create()` | Promise<ExpenseView> | — |
| `remove()` | Promise<void> | — |


## Enlaces

- [[M7 - expense]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
