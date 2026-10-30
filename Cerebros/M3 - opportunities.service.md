---
type: servicio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/opportunities.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - servicio
---

# M3 - opportunities.service

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Servicio
> Archivo de servicio del backend (`opportunities/opportunities.service.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DEFAULT_LIMIT` | const | — |
| `parseSearchTerms` | function | — |
| `isValidIsoDate` | function | — |
| `ungroundedNumbers` | function | Cifras (2+ dígitos) del texto de la IA que no aparecen en la página fuente. |
| `buildDraft` | function | Normaliza la salida de la IA a una ficha revisable; nunca rellena datos ausentes. |
| `OpportunitiesService` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `search()` | Promise<OpportunityView[]> | Listado público: solo publicadas (los borrados lógicos los excluye TypeORM). |
| `listSocieties()` | Promise<IeeeSocietyView[]> | — |
| `extract()` | Promise<OpportunityDraftView> | Descarga la página oficial y propone una ficha; no guarda nada hasta que se publique. |
| `publish()` | Promise<OpportunityView> | Publica una ficha ya revisada por una persona (botón «Publicar» del mockup 05). |


## Enlaces

- [[M3 - official-sources]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
