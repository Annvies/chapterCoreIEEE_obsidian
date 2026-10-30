---
type: prueba
modulo: 2
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/contacts/DirectoryPage.test.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-2
  - prueba
---

# M2 - Prueba DirectoryPage.test

[[M2 - Pruebas]] · [[Cerebro 2 - Contactos]]

> [!abstract] Prueba
> 7 casos de prueba (Vitest + Testing Library).

### Casos

- **Directorio de contactos**
  - muestra pestañas con conteos, la tabla y la ficha del primer contacto
  - un Director de capítulo solo puede ver: sin crear, importar, registrar ni eliminar
  - Secretaría puede editar pero no eliminar
  - envía los filtros y la búsqueda al backend
  - registra una llamada en el historial
- **helpers del directorio**
  - formatea fechas de calendario como dd/mm/aaaa
  - marca convenios vencidos o por vencer en 30 días

## Enlaces

- [[M2 - DirectoryPage]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
