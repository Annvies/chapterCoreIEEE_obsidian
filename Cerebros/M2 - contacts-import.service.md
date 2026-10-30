---
type: servicio
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/services/contacts-import.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-2
  - servicio
---

# M2 - contacts-import.service

[[M2 - Lógica del backend]] · [[Cerebro 2 - Contactos]]

> [!abstract] Servicio
> Archivo de servicio del backend (`contacts/services/contacts-import.service.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ImportResultView` | interface | — |
| `ContactsImportService` | class | Importación CSV del mockup 04 ("Importar CSV"). Es todo o nada: si alguna fila tiene errores no se guarda ninguna, para no dejar el directorio a medias. |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `importCsv()` | Promise<ImportResultView> | — |


## Enlaces

- [[M2 - contact-import]]
- [[M2 - csv]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
