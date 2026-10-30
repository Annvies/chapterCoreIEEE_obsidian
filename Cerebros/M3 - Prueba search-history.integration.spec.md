---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/search-history.integration.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba search-history.integration.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 4 casos de prueba (Jest).

### Casos

  - 51 búsquedas dejan solo las 50 más recientes
  - el enum tiene las 4 estrategias y guarda una búsqueda resuelta por el catálogo
  - la base rechaza más de 20 resultados (CHECK)
  - al borrar a la persona se borra su historial (ON DELETE CASCADE)

## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
