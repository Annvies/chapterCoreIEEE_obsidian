---
type: dominio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/strategies/static-pages.strategy.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - dominio
---

# M3 - static-pages.strategy

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dominio
> Archivo de dominio del backend (`opportunities/discovery/strategies/static-pages.strategy.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `StartPage` | interface | — |
| `START_PAGES` | const | Fuentes verificadas en CONTEXTO.md §7 el 2026-10-19. |
| `selectStartPages` | function | Orden de descarga: primero la sigla nombrada, luego las páginas del tipo nombrado (antes las dedicadas solo a ese tipo que las mixtas) y, a igualdad, las generales antes que las de sociedad. |
| `extractCandidates` | function | Enlaces de una página con su texto y el del bloque que los contiene. |
| `StaticPagesStrategy` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `habilitada()` | boolean | — |
| `buscar()` | Promise<StrategyOutput> | — |


## Enlaces

- [[M3 - robots]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
