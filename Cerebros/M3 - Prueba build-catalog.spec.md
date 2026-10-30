---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/catalog/build-catalog.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba build-catalog.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 8 casos de prueba (Jest).

### Casos

- **buildCatalog (ciclo 2, RF-355, C8)**
  - produce un catálogo válido con su fecha
  - solo guarda páginas oficiales https que no son archivos
  - no repite enlaces aunque aparezcan en dos páginas de partida
  - registra tipo, página, orden de aparición y sigla de la página
  - con una página de varios tipos, infiere el tipo del texto
  - guarda como máximo ${MAX_ENTRIES_PER_PAGE} por página y ${MAX_CATALOG_ENTRIES} en total
  - descarta enlaces de menú y pie de página que no nombran una convocatoria (T046)
  - reconoce palabras de convocatoria sin distinguir mayúsculas

## Enlaces

- [[M3 - build-catalog]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
