---
type: dominio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/strategies/browser.strategy.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - dominio
---

# M3 - browser.strategy

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dominio
> Archivo de dominio del backend (`opportunities/discovery/strategies/browser.strategy.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `RenderedPage` | interface | — |
| `BrowserSession` | interface | — |
| `BrowserAdapter` | interface | Separa la estrategia de Playwright para poder probarla sin navegador. |
| `BROWSER_ADAPTER` | const | — |
| `shouldBlockRequest` | function | ¿Debe abortarse esta petición del navegador? La navegación principal solo puede ir a la lista verificada; cualquier petición (subrecursos, iframes) a localhost o IP privadas se aborta. Limitación conocida: un nombre público que resuelva a una IP privada (DNS rebinding) no se detecta aquí, porque Chromium resuelve los nombres por su cuenta (qa-architect H3). |
| `PlaywrightBrowserAdapter` | class | Adaptador real: carga Playwright solo cuando se usa (import dinámico). |
| `BrowserStrategy` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `available()` | boolean | — |
| `open()` | Promise<BrowserSession> | — |
| `habilitada()` | boolean | — |
| `buscar()` | Promise<StrategyOutput> | — |


## Enlaces

- [[M3 - official-sources]]
- [[M3 - robots]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
