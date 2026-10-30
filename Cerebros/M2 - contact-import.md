---
type: dominio
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/domain/contact-import.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-2
  - dominio
---

# M2 - contact-import

[[M2 - Lógica del backend]] · [[Cerebro 2 - Contactos]]

> [!abstract] Dominio
> Datos editables de un contacto (alta manual o fila de CSV).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ContactDraft` | interface | Datos editables de un contacto (alta manual o fila de CSV). |
| `ImportRowError` | interface | — |
| `MAX_IMPORT_ROWS` | const | — |
| `IMPORT_COLUMNS` | const | Columnas de la plantilla, en orden. |
| `buildImportDrafts` | function | Convierte un CSV ya leído en borradores de contacto. Devuelve todos los errores por fila para que la persona corrija el archivo de una sola vez. @param chapterIdsBySigla siglas del catálogo ieee_societies en minúsculas. |
| `parseImportDate` | function | Acepta "dd/mm/aaaa", "dd-mm-aaaa" o "aaaa-mm-dd"; devuelve "aaaa-mm-dd". |


## Enlaces

- [[M2 - contact]]
- [[M2 - csv]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
