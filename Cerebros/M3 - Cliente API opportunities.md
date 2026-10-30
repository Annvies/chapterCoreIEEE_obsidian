---
type: cliente API
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/api/opportunities.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - cliente-API
---

# M3 - Cliente API opportunities

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Cliente api
> Cliente api del frontend (`frontendChapterCoreIEEE/src/api/opportunities.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `searchOpportunities` | function | — |
| `listSocieties` | function | — |
| `extractOpportunity` | function | — |
| `getDiscoveryConfig` | function | — |
| `discoverOpportunities` | function | — |
| `listSearchHistory` | function | — |
| `deleteSearchHistoryEntry` | function | — |
| `clearSearchHistory` | function | — |
| `listOfficialDomains` | function | — |
| `publishOpportunity` | function | — |

### Llamadas a la API

| Función | Método | Ruta |
|---|---|---|
| `searchOpportunities()` | `GET` | `/opportunities` |
| `listSocieties()` | `GET` | `/opportunities/societies` |
| `extractOpportunity()` | `POST` | `/opportunities/extract` |
| `getDiscoveryConfig()` | `GET` | `/opportunities/discover/config` |
| `discoverOpportunities()` | `POST` | `/opportunities/discover` |
| `listSearchHistory()` | `GET` | `/opportunities/search-history` |
| `deleteSearchHistoryEntry()` | `DELETE` | `/opportunities/search-history/:p` |
| `clearSearchHistory()` | `DELETE` | `/opportunities/search-history` |
| `listOfficialDomains()` | `GET` | `/opportunities/official-domains` |
| `publishOpportunity()` | `POST` | `/opportunities` |


## Enlaces

- [[M3 - Tipos opportunity]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
