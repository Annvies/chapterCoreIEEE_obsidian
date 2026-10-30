---
type: endpoint
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/controllers/contacts.controller.ts
actualizado: 2026-10-30
aliases:
  - "POST /contacts/import"
tags:
  - chaptercore
  - modulo-2
  - endpoint
---

# M2 - POST contacts › import

[[M2 - API]] · [[Cerebro 2 - Contactos]]

> [!abstract] Endpoint
> `POST /contacts/import` · acceso: Contactos · Editar.

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/contacts/import` |
| Acceso | Contactos · Editar |
| Controlador | `backendChapterCoreIEEE/src/contacts/controllers/contacts.controller.ts` → `importCsv()` |
| Respuesta | `OK` |

### Entradas

- Archivo adjunto (multipart)
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `ContactsImportService.importCsv()`

> [!note] Comentario del controlador
> Matriz oficial (mockup 03): Mesa Directiva total, Secretaría edita, Directores de capítulo ven y Miembros no tienen acceso.

### Consumido por el frontend

- [[M2 - Cliente API contacts]]

## Enlaces

- [[M2 - contacts-import.service]]
- [[M2 - Cliente API contacts]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
