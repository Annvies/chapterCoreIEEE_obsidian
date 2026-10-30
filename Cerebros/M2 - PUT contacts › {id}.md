---
type: endpoint
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/controllers/contacts.controller.ts
actualizado: 2026-10-30
aliases:
  - "PUT /contacts/:id"
tags:
  - chaptercore
  - modulo-2
  - endpoint
---

# M2 - PUT contacts › {id}

[[M2 - API]] · [[Cerebro 2 - Contactos]]

> [!abstract] Endpoint
> `PUT /contacts/:id` · acceso: Contactos · Editar.

| Campo | Valor |
|---|---|
| Método | `PUT` |
| Ruta | `/contacts/:id` |
| Acceso | Contactos · Editar |
| Controlador | `backendChapterCoreIEEE/src/contacts/controllers/contacts.controller.ts` → `update()` |

### Entradas

- Parámetro de ruta `id` (UUID)
- Cuerpo → `ContactInputDto`
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `ContactsService.update()`

> [!note] Comentario del controlador
> Matriz oficial (mockup 03): Mesa Directiva total, Secretaría edita, Directores de capítulo ven y Miembros no tienen acceso.

### Consumido por el frontend

- [[M2 - Cliente API contacts]]

## Enlaces

- [[M2 - contacts.service]]
- [[M2 - DTO ContactInputDto]]
- [[M2 - Cliente API contacts]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
