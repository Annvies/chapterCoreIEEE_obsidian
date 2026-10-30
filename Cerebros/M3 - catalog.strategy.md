---
type: dominio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/strategies/catalog.strategy.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - dominio
---

# M3 - catalog.strategy

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dominio
> Archivo de dominio del backend (`opportunities/discovery/strategies/catalog.strategy.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DISCOVERY_CATALOG` | const | Contenido crudo del catálogo (el JSON versionado en producción, un fixture en pruebas). |
| `CatalogStrategy` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `habilitada()` | boolean | — |
| `buscar()` | Promise<StrategyOutput> | Firma común de las estrategias; el catálogo no usa el contexto. |


## Enlaces

- [[M3 - catalog]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
