---
type: endpoint
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/forms.controller.ts
actualizado: 2026-10-29
aliases:
  - "POST /forms"
tags:
  - chaptercore
  - modulo-5
  - endpoint
---

# M5 - POST forms

[[M5 - API]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Endpoint
> `POST /forms` · acceso: Formularios · Editar.

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/forms` |
| Acceso | Formularios · Editar |
| Controlador | `backendChapterCoreIEEE/src/forms/forms.controller.ts` → `create()` |

### Entradas

- Cuerpo → `CreateFormDto`
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `FormsService.create()`

### Consumido por el frontend

- [[M5 - lib api]]

## Enlaces

- [[M5 - forms.service]]
- [[M5 - DTO CreateFormDto]]
- [[M5 - lib api]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
