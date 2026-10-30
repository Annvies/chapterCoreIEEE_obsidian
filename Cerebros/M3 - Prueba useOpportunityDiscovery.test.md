---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/hooks/useOpportunityDiscovery.test.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba useOpportunityDiscovery.test

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 5 casos de prueba (Vitest + Testing Library).

### Casos

- **useOpportunityDiscovery**
  - envía la consulta y la estrategia forzada, y guarda la respuesta
  - una búsqueda nueva cancela la anterior
  - expone el mensaje de error del servidor
- **useSearchHistory**
  - no carga nada hasta que se abre el historial
  - carga, elimina una entrada y vacía

## Enlaces

- [[M3 - useOpportunityDiscovery]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
