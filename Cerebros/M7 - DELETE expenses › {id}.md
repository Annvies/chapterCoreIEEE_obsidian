---
type: endpoint
modulo: 7
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/expenses/controllers/expenses.controller.ts
actualizado: 2026-10-30
aliases:
  - "DELETE /expenses/:id"
tags:
  - chaptercore
  - modulo-7
  - endpoint
---

# M7 - DELETE expenses › {id}

[[M7 - API]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Endpoint
> `DELETE /expenses/:id` · acceso: Gastos · Total.

| Campo | Valor |
|---|---|
| Método | `DELETE` |
| Ruta | `/expenses/:id` |
| Acceso | Gastos · Total |
| Controlador | `backendChapterCoreIEEE/src/expenses/controllers/expenses.controller.ts` → `remove()` |
| Respuesta | `NO_CONTENT` |

### Entradas

- Parámetro de ruta `id` (UUID)
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `ExpensesService.remove()`

> [!note] Comentario del controlador
> Matriz (spec 009): Mesa Directiva total, Secretaría ve, Director de capítulo registra solo en su capítulo y Miembros no tienen acceso.

### Consumido por el frontend

- [[M7 - Cliente API expenses]]

## Enlaces

- [[M7 - expenses.service]]
- [[M7 - Cliente API expenses]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
