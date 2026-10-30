---
type: endpoint
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/forms.controller.ts
actualizado: 2026-10-29
aliases:
  - "PATCH /forms/:id"
tags:
  - chaptercore
  - modulo-5
  - endpoint
---

# M5 - PATCH forms › {id}

[[M5 - API]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Endpoint
> `PATCH /forms/:id` · acceso: Formularios · Editar.

| Campo | Valor |
|---|---|
| Método | `PATCH` |
| Ruta | `/forms/:id` |
| Acceso | Formularios · Editar |
| Controlador | `backendChapterCoreIEEE/src/forms/forms.controller.ts` → `update()` |

### Entradas

- Parámetro de ruta `id` (UUID)
- Cuerpo → `UpdateFormDto`
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `FormsService.update()`

### Consumido por el frontend

- [[M5 - lib api]]

## Enlaces

- [[M5 - forms.service]]
- [[M5 - DTO UpdateFormDto]]
- [[M5 - lib api]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
