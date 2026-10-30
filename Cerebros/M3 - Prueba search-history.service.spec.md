---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/search-history.service.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba search-history.service.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 6 casos de prueba (Jest).

### Casos

- **SearchHistoryService**
  - guarda la búsqueda de esa persona
  - poda a las 50 más recientes de esa persona en la misma transacción (RF-324)
  - lista solo el historial propio, de la más reciente a la más antigua
  - elimina una entrada solo si es de la persona
  - vacía solo el historial propio
  - devuelve las entradas con la forma del contrato

## Enlaces

- [[M3 - search-history.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
