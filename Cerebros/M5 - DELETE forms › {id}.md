---
type: endpoint
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/forms.controller.ts
actualizado: 2026-10-30
aliases:
  - "DELETE /forms/:id"
tags:
  - chaptercore
  - modulo-5
  - endpoint
---

# M5 - DELETE forms › {id}

[[M5 - API]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Endpoint
> `DELETE /forms/:id` · acceso: Formularios · Total.

| Campo | Valor |
|---|---|
| Método | `DELETE` |
| Ruta | `/forms/:id` |
| Acceso | Formularios · Total |
| Controlador | `backendChapterCoreIEEE/src/forms/forms.controller.ts` → `remove()` |

### Entradas

- Parámetro de ruta `id` (UUID)

### Lógica que invoca

- `FormsService.remove()`

### Consumido por el frontend

- [[M5 - lib api]]

## Enlaces

- [[M5 - forms.service]]
- [[M5 - lib api]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
