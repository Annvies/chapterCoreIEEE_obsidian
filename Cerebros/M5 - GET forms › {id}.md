---
type: endpoint
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/forms.controller.ts
actualizado: 2026-10-29
aliases:
  - "GET /forms/:id"
tags:
  - chaptercore
  - modulo-5
  - endpoint
---

# M5 - GET forms › {id}

[[M5 - API]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Endpoint
> `GET /forms/:id` · acceso: Formularios · Editar.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/forms/:id` |
| Acceso | Formularios · Editar |
| Controlador | `backendChapterCoreIEEE/src/forms/forms.controller.ts` → `findOne()` |

### Entradas

- Parámetro de ruta `id` (UUID)

### Lógica que invoca

- `FormsService.findOne()`

### Consumido por el frontend

- [[M5 - lib api]]

## Enlaces

- [[M5 - forms.service]]
- [[M5 - lib api]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
