---
type: servicio
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/services/contacts.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-2
  - servicio
---

# M2 - contacts.service

[[M2 - Lógica del backend]] · [[Cerebro 2 - Contactos]]

> [!abstract] Servicio
> Archivo de servicio del backend (`contacts/services/contacts.service.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ContactListView` | interface | — |
| `ContactsService` | class | Directorio de contactos (Módulo 2). Los permisos los aplica el PermissionsGuard. |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `list()` | Promise<ContactListView> | — |
| `listSectors()` | Promise<string[]> | — |
| `listChapters()` | Promise<ChapterView[]> | — |
| `findOne()` | Promise<ContactDetailView> | — |
| `create()` | Promise<ContactDetailView> | — |
| `update()` | — | — |
| `remove()` | Promise<void> | — |
| `addInteraction()` | — | — |
| `validateDraft()` | Promise<ContactDraft> | Normaliza y valida reglas que el DTO no cubre (fecha real, capítulo existente). |


## Enlaces

- [[M2 - contact]]
- [[M2 - contact-import]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
