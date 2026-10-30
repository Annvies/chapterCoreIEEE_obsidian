---
type: endpoint
modulo: 7
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/expenses/controllers/expenses.controller.ts
actualizado: 2026-10-30
aliases:
  - "POST /expenses"
tags:
  - chaptercore
  - modulo-7
  - endpoint
---

# M7 - POST expenses

[[M7 - API]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Endpoint
> `POST /expenses` · acceso: Gastos · Editar.

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/expenses` |
| Acceso | Gastos · Editar |
| Controlador | `backendChapterCoreIEEE/src/expenses/controllers/expenses.controller.ts` → `create()` |

### Entradas

- Cuerpo → `ExpenseInputDto`
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `ExpensesService.create()`

> [!note] Comentario del controlador
> Matriz (spec 009): Mesa Directiva total, Secretaría ve, Director de capítulo registra solo en su capítulo y Miembros no tienen acceso.

### Consumido por el frontend

- [[M7 - Cliente API expenses]]

## Enlaces

- [[M7 - expenses.service]]
- [[M7 - DTO ExpenseInputDto]]
- [[M7 - Cliente API expenses]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
