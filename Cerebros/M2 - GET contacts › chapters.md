---
type: endpoint
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/controllers/contacts.controller.ts
actualizado: 2026-10-30
aliases:
  - "GET /contacts/chapters"
tags:
  - chaptercore
  - modulo-2
  - endpoint
---

# M2 - GET contacts › chapters

[[M2 - API]] · [[Cerebro 2 - Contactos]]

> [!abstract] Endpoint
> Capítulos para el filtro y el formulario (el de /access exige administrar usuarios).

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/contacts/chapters` |
| Acceso | Contactos · Ver |
| Controlador | `backendChapterCoreIEEE/src/contacts/controllers/contacts.controller.ts` → `chapters()` |

### Lógica que invoca

- `ContactsService.listChapters()`

> [!note] Comentario del controlador
> Matriz oficial (mockup 03): Mesa Directiva total, Secretaría edita, Directores de capítulo ven y Miembros no tienen acceso.

### Consumido por el frontend

- [[M2 - Cliente API contacts]]

## Enlaces

- [[M2 - contacts.service]]
- [[M2 - Cliente API contacts]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
