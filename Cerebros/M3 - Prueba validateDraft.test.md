---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/validateDraft.test.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba validateDraft.test

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 6 casos de prueba (Vitest + Testing Library).

### Casos

- **validateDraft**
  - acepta una ficha completa
  - señala cada campo con problemas
  - aplica los mismos límites que el backend
- **isIsoDate**
  - rechaza fechas que no existen en el calendario
- **toPublishable**
  - limpia los campos y descarta las advertencias del envío
  - devuelve null si la ficha no es publicable

## Enlaces

- [[M3 - validateDraft]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
