---
type: dominio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/official-sources.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - dominio
---

# M3 - official-sources

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dominio
> Fuentes oficiales aceptadas (CONTEXTO.md §7, spec 002 RF-329): se derivan de la lista verificada, sin los dominios retirados.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `OFFICIAL_DOMAINS` | const | Fuentes oficiales aceptadas (CONTEXTO.md §7, spec 002 RF-329): se derivan de la lista verificada, sin los dominios retirados. |
| `parseOfficialUrl` | function | — |
| `normalizeOfficialUrl` | function | Forma canónica de una URL oficial para comparar duplicados: host en minúsculas, sin puerto por defecto, sin fragmento y sin «/» final (salvo la raíz). Conserva la query. |
| `isOfficialIeeeUrl` | function | — |
| `inferSocietySigla` | function | — |


## Enlaces

- [[M3 - official-domains]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
