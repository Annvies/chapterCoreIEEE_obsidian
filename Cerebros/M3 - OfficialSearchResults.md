---
type: componente
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/OfficialSearchResults.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - componente
---

# M3 - OfficialSearchResults

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/opportunities/OfficialSearchResults.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `OfficialSearchResultsProps` | interface | — |
| `OfficialSearchResults` | function | Resultados de «Buscar en fuentes oficiales IEEE» (spec 002, HU-10). |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `status` | sí | `DiscoveryStatus` |
| `response` | sí | `DiscoveryResponse \| null` |
| `error` | sí | `string \| null` |
| `config` | sí | `DiscoveryConfig \| null` |


## Enlaces

- [[M3 - useOpportunityDiscovery]]
- [[M3 - Tipos opportunity]]
- [[M3 - discoveryAnnouncement]]
- [[M3 - DiscoveryResultList]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
