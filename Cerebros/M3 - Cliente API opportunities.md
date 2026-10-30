---
type: cliente API
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/api/opportunities.ts
actualizado: 2026-10-29
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
| `publishOpportunity` | function | — |

### Llamadas a la API

| Función | Método | Ruta |
|---|---|---|
| `searchOpportunities()` | `GET` | `/opportunities` |
| `listSocieties()` | `GET` | `/opportunities/societies` |
| `extractOpportunity()` | `POST` | `/opportunities/extract` |
| `publishOpportunity()` | `POST` | `/opportunities` |


## Enlaces

- [[M3 - Tipos opportunity]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
