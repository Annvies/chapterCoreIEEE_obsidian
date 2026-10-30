---
type: endpoint
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/forms.controller.ts
actualizado: 2026-10-30
aliases:
  - "POST /forms/:id/publish"
tags:
  - chaptercore
  - modulo-5
  - endpoint
---

# M5 - POST forms › {id} › publish

[[M5 - API]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Endpoint
> `POST /forms/:id/publish` · acceso: Formularios · Editar.

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/forms/:id/publish` |
| Acceso | Formularios · Editar |
| Controlador | `backendChapterCoreIEEE/src/forms/forms.controller.ts` → `publish()` |
| Respuesta | `OK` |

### Entradas

- Parámetro de ruta `id` (UUID)
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `FormsService.publish()`

### Consumido por el frontend

- [[M5 - lib api]]

## Enlaces

- [[M5 - forms.service]]
- [[M5 - lib api]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
