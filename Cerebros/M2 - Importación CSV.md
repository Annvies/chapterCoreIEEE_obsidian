---
type: concepto
modulo: 2
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/contacts/domain/contact-import.ts
  - backendChapterCoreIEEE/src/contacts/controllers/contacts.controller.ts
  - CONTEXTO.md
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-2
  - concepto
---

# M2 - Importación CSV

[[M2 - Directorio]] · [[Cerebro 2 - Contactos]]

> [!abstract] Qué es
> Carga masiva de contactos desde una plantilla CSV, todo o nada.

> [!info] Confirmado en el código
> - Archivo `.csv` de máximo **1 MB** y **500 filas**.
> - Columnas: tipo, nombre, organizacion, contacto, cargo, correo, telefono, sector, ciudad, estado, convenio, vence, capitulo, notas. Obligatorias: **tipo** y **nombre**.
> - Fechas `dd/mm/aaaa`, `dd-mm-aaaa` o `aaaa-mm-dd`; el capítulo se indica por su sigla.
> - Si una fila tiene errores no se importa ninguna, y se listan los errores por fila.

> [!warning] Sin detección de duplicados
> La importación no detecta contactos repetidos (`CONTEXTO.md`, fuera del MVP).

## Enlaces

- Forma parte de [[M2 - Directorio]].
- Relacionada con [[M2 - Modelo de datos contacts]], [[M2 - Tipos de contacto]], [[M2 - Acciones por nivel de acceso]].

## Fuentes

- `backendChapterCoreIEEE/src/contacts/domain/contact-import.ts`
- `backendChapterCoreIEEE/src/contacts/controllers/contacts.controller.ts`
- `CONTEXTO.md`
