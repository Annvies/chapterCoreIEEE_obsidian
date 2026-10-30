---
type: dominio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/catalog/catalog.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - dominio
---

# M3 - catalog

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dominio
> Catálogo de respaldo (spec 002, RF-350 a RF-355, data-model.md). Lo genera una persona en su equipo con `npm run discovery:catalog`; en producción solo se lee. Es dato no confiable: se valida al cargarlo y sus entradas pasan por el mismo filtro que los resultados en vivo.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `MAX_CATALOG_ENTRIES` | const | — |
| `CatalogEntry` | interface | — |
| `OfficialCatalog` | interface | — |
| `parseCatalog` | function | Catálogo válido y con al menos una entrada, o null si no se puede usar. |


## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
