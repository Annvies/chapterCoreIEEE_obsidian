---
type: prueba
modulo: 5
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/lib/form-schema.test.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - prueba
---

# M5 - Prueba form-schema.test

[[M5 - Pruebas]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Prueba
> 6 casos de prueba (Vitest + Testing Library).

### Casos

- **form-schema**
  - genera slugs sin acentos ni símbolos
  - crea campos de escala con rango por defecto
  - valida campos obligatorios visibles
  - oculta y no exige campos condicionales
  - separa archivos y descarta respuestas ocultas
  - rechaza valores fuera de la escala

## Enlaces

- [[M5 - lib form-schema]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
