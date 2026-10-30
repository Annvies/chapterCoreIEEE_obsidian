---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/strategies/catalog.strategy.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba catalog.strategy.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 7 casos de prueba (Jest).

### Casos

- **CatalogStrategy (ciclo 2, RF-350 a RF-354)**
  - devuelve todas las entradas como candidatos con la página donde aparecieron
  - prepara las más recientes del tipo pedido, en orden de aparición (RF-353, R10)
  - sin tipo en la búsqueda, las más recientes son de todos los tipos
  - informa la fecha del catálogo
  - con %i días y límite %s → antiguo=%s (RF-354)
  - no sale a la red ni consume el contador de páginas
  - OPPORTUNITY_DISCOVERY_CATALOG=%s → habilitada=%s

## Enlaces

- [[M3 - catalog.strategy]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
