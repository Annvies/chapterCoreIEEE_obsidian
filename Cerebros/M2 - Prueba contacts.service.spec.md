---
type: prueba
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/services/contacts.service.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-2
  - prueba
---

# M2 - Prueba contacts.service.spec

[[M2 - Pruebas]] · [[Cerebro 2 - Contactos]]

> [!abstract] Prueba
> 10 casos de prueba (Jest).

### Casos

- **ContactsService**
  - crea un contacto normalizando opcionales y registrando la autoría
  - rechaza capítulos inexistentes y fechas de vencimiento imposibles
  - al editar reemplaza los campos y limpia el capítulo cargado
  - responde 404 si el contacto no existe
  - registra una interacción y actualiza la última interacción en la misma transacción
  - no acepta interacciones con fecha futura
- **ContactsImportService**
  - importa todas las filas válidas con la autoría de quien importa
  - no guarda nada si alguna fila tiene errores
  - acepta archivos Latin-1 exportados por Excel
  - rechaza CSV mal formados

## Enlaces

- [[M2 - contacts.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
