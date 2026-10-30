---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/strategies/browser.strategy.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba browser.strategy.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 9 casos de prueba (Jest).

### Casos

- **BrowserStrategy**
  - habilitada %s → %s
  - queda desactivada si Playwright no está instalado
  - renderiza las páginas y extrae sus enlaces como la estrategia estática
  - usa el tiempo por página configurado (%j → %i ms)
  - respeta robots.txt y el contador común de páginas
  - cierra el navegador aunque falle una página
  - carga las páginas en tandas y, con poco tiempo, devuelve lo ya encontrado
  - no abre el navegador si el presupuesto ya se agotó
- **shouldBlockRequest**
  - %s

## Enlaces

- [[M3 - browser.strategy]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
