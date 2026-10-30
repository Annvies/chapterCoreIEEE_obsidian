---
type: endpoint
modulo: 7
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/expenses/controllers/expenses.controller.ts
actualizado: 2026-10-30
aliases:
  - "GET /expenses/summary"
tags:
  - chaptercore
  - modulo-7
  - endpoint
---

# M7 - GET expenses › summary

[[M7 - API]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Endpoint
> Declarada antes de cualquier ruta con parámetro.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/expenses/summary` |
| Acceso | Gastos · Ver |
| Controlador | `backendChapterCoreIEEE/src/expenses/controllers/expenses.controller.ts` → `summary()` |

### Entradas

- Query  → `ExpenseSummaryQueryDto`
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `ExpensesService.summary()`

> [!note] Comentario del controlador
> Matriz (spec 009): Mesa Directiva total, Secretaría ve, Director de capítulo registra solo en su capítulo y Miembros no tienen acceso.

### Consumido por el frontend

- [[M7 - Cliente API expenses]]

## Enlaces

- [[M7 - expenses.service]]
- [[M7 - DTO ExpenseSummaryQueryDto]]
- [[M7 - Cliente API expenses]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
