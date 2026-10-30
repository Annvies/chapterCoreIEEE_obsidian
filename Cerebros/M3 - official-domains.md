---
type: dominio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/official-domains.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - dominio
---

# M3 - official-domains

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dominio
> Lista verificada de dominios oficiales de IEEE (spec 002, RF-329). Es la única fuente para resultados, extracción y publicación. Un dominio incluye todos sus subdominios. Un dominio nuevo solo entra con la fuente oficial que lo acredita y la fecha de verificación; uno que deja de ser oficial no se borra: se marca como retirado con su motivo. URL oficial que acredita el dominio. Fecha de verificación (AAAA-MM-DD).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `OfficialDomainEntry` | interface | Lista verificada de dominios oficiales de IEEE (spec 002, RF-329). Es la única fuente para resultados, extracción y publicación. Un dominio incluye todos sus subdominios. Un dominio nuevo solo entra con la fuente oficial que lo acredita y la fecha de verificación; uno que deja de ser oficial no se borra: se marca como retirado con su motivo. |
| `OFFICIAL_DOMAIN_ENTRIES` | const | Sitios verificados en CONTEXTO.md §7 el 2026-10-19; la fuente es el sitio oficial listado allí. |
| `activeDomains` | function | Dominios aceptados: los de la lista que no están retirados. |


## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
