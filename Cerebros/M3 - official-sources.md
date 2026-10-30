---
type: dominio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/official-sources.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - dominio
---

# M3 - official-sources

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dominio
> Fuentes oficiales aceptadas (CONTEXTO.md §7): ieee.org y sus subdominios, más los sitios oficiales verificados de sociedades que no cuelgan de ieee.org.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `OFFICIAL_DOMAINS` | const | Fuentes oficiales aceptadas (CONTEXTO.md §7): ieee.org y sus subdominios, más los sitios oficiales verificados de sociedades que no cuelgan de ieee.org. |
| `parseOfficialUrl` | function | — |
| `normalizeOfficialUrl` | function | Forma canónica de una URL oficial para comparar duplicados: host en minúsculas, sin puerto por defecto, sin fragmento y sin «/» final (salvo la raíz). Conserva la query. |
| `isOfficialIeeeUrl` | function | — |
| `inferSocietySigla` | function | — |


## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
