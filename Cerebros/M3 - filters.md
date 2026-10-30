---
type: módulo
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/filters.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - módulo
---

# M3 - filters

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Módulo
> Supuesto (pendiente de confirmar): «cierra pronto» = fecha límite en los próximos 14 días.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `CLOSING_SOON_DAYS` | const | Supuesto (pendiente de confirmar): «cierra pronto» = fecha límite en los próximos 14 días. |
| `QuickFilter` | type | — |
| `QUICK_FILTERS` | const | — |
| `FilterOptions` | interface | — |
| `countCurrent` | function | Vigente = sin fecha límite o con fecha límite igual o posterior a hoy (spec 002, RF-310). |
| `DiscoveryOfferInput` | interface | — |
| `shouldOfferDiscovery` | function | ¿Se ofrece «Buscar en fuentes oficiales IEEE»? (RF-310) |
| `applyFilters` | function | — |


## Enlaces

- [[M3 - Tipos opportunity]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
