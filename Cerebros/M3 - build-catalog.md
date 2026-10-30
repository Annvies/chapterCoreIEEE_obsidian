---
type: dominio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/catalog/build-catalog.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - dominio
---

# M3 - build-catalog

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dominio
> Construcción del catálogo de respaldo a partir de páginas ya leídas (spec 002, RF-355, C8). Función pura: la descarga la hace `scripts/build-discovery-catalog.ts`, con las mismas protecciones que la búsqueda. Aplica el mismo filtro que los resultados en vivo.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `CrawledPage` | interface | — |
| `MAX_ENTRIES_PER_PAGE` | const | Máximo por página de partida: todas quedan representadas dentro de las 400 (T046). |
| `looksLikeOpportunity` | function | — |
| `buildCatalog` | function | — |


## Enlaces

- [[M3 - official-sources]]
- [[M3 - result-filter]]
- [[M3 - catalog]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
