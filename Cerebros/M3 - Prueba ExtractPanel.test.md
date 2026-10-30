---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/ExtractPanel.test.tsx
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba ExtractPanel.test

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 4 casos de prueba (Vitest + Testing Library).

### Casos

- **ExtractPanel**
  - valida la URL antes de llamar al backend
  - muestra advertencias, exige el tipo y publica solo los campos de la ficha
  - muestra el 409 del backend como error de publicación y lo limpia al editar
  - muestra el mensaje del backend cuando falla la extracción

## Enlaces

- [[M3 - ExtractPanel]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
