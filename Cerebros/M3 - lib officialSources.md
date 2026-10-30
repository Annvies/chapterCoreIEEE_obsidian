---
type: utilidad
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/lib/officialSources.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - utilidad
---

# M3 - lib officialSources

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Utilidad
> Dominios oficiales aceptados como fuente (CONTEXTO.md §7, spec 002 RF-329). La lista vigente la da el backend (GET /opportunities/official-domains); esta es la de respaldo mientras carga.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DEFAULT_OFFICIAL_DOMAINS` | const | Dominios oficiales aceptados como fuente (CONTEXTO.md §7, spec 002 RF-329). La lista vigente la da el backend (GET /opportunities/official-domains); esta es la de respaldo mientras carga. |
| `isOfficialIeeeUrl` | function | Mismas reglas que el servidor (RF-301, RF-332; resuelve H-15): https, sin usuario ni contraseña, puerto por defecto y dominio de la lista verificada (o un subdominio suyo). |


## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
