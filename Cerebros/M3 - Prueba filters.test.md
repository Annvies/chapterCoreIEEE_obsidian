---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/filters.test.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba filters.test

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 5 casos de prueba (Vitest + Testing Library).

### Casos

- **countCurrent (RF-310)**
  - cuenta las que no tienen fecha y las que cierran hoy o después
- **shouldOfferDiscovery (RF-310)**
  - con 2 vigentes ofrece la acción
  - con 3 vencidas también la ofrece
  - con 3 vigentes no la ofrece
  - sin texto, mientras carga o sin estrategias habilitadas no la ofrece

## Enlaces

- [[M3 - filters]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
