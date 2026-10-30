---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/strategies/static-pages.strategy.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba static-pages.strategy.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 16 casos de prueba (Jest).

### Casos

- **StaticPagesStrategy**
  - extrae enlaces con su título y el texto del bloque que los contiene
  - usa el contador común: no descarga más páginas que las que quedan
  - no descarga páginas prohibidas por robots.txt
  - pasa la señal del presupuesto a robots.txt y a cada descarga
  - abandona una página que supera el tiempo por página y sigue con las demás
  - tras un rechazo no vuelve a pedir páginas a ese host y lo informa
  - avisa cuando una página leída no tiene enlaces (posible página dinámica)
  - trata como dato el texto que intenta dar instrucciones
  - una página que falla no detiene la estrategia
  - informa error si no pudo leer ninguna página
  - se detiene si se agotó el presupuesto de tiempo
  - con poco tiempo restante deja de descargar y devuelve lo ya encontrado
  - OPPORTUNITY_DISCOVERY_STATIC=%s → habilitada=%s
- **selectStartPages**
  - prioriza las páginas de la sigla y del tipo que nombra la búsqueda
  - con un tipo, empieza por las páginas de ese tipo
  - no repite páginas y todas son oficiales

## Enlaces

- [[M3 - static-pages.strategy]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
