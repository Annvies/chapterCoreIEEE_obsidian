---
type: cliente API
modulo: 2
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/api/contacts.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-2
  - cliente-API
---

# M2 - Cliente API contacts

[[M2 - Interfaz]] · [[Cerebro 2 - Contactos]]

> [!abstract] Cliente API
> Cliente api del frontend (`frontendChapterCoreIEEE/src/api/contacts.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `listContacts` | function | — |
| `fetchContact` | function | — |
| `fetchSectors` | function | — |
| `fetchContactChapters` | function | — |
| `createContact` | function | — |
| `updateContact` | function | — |
| `deleteContact` | function | — |
| `addInteraction` | function | — |
| `importContactsCsv` | function | — |

### Llamadas a la API

| Función | Método | Ruta |
|---|---|---|
| `listContacts()` | `GET` | `/contacts` |
| `fetchContact()` | `GET` | `/contacts/:p` |
| `fetchSectors()` | `GET` | `/contacts/sectors` |
| `fetchContactChapters()` | `GET` | `/contacts/chapters` |
| `createContact()` | `POST` | `/contacts` |
| `updateContact()` | `PUT` | `/contacts/:p` |
| `deleteContact()` | `DELETE` | `/contacts/:p` |
| `addInteraction()` | `POST` | `/contacts/:p/interactions` |
| `importContactsCsv()` | `POST` | `/contacts/import` |


## Enlaces

- [[M2 - Tipos contacts]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
