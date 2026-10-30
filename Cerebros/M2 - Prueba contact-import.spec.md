---
type: prueba
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/domain/contact-import.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-2
  - prueba
---

# M2 - Prueba contact-import.spec

[[M2 - Pruebas]] · [[Cerebro 2 - Contactos]]

> [!abstract] Prueba
> 8 casos de prueba (Jest).

### Casos

- **parseCsv**
  - lee comillas, comillas escapadas y saltos de línea dentro de un campo
  - detecta el separador ";" de Excel en español, quita el BOM y normaliza cabeceras
  - ignora filas vacías y rechaza comillas sin cerrar o archivos vacíos
- **buildImportDrafts**
  - convierte filas válidas con alias de tipo, estado, fecha y capítulo
  - reporta todos los errores por fila y no devuelve borradores de filas inválidas
  - exige las columnas tipo y nombre
  - limita la importación a ${MAX_IMPORT_ROWS} filas
- **parseImportDate**
  - %s -> %s

## Enlaces

- [[M2 - contact-import]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
