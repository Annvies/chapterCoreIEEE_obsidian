---
type: dominio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/robots.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - dominio
---

# M3 - robots

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dominio
> Reglas de robots.txt (RFC 9309) para la búsqueda en fuentes oficiales (spec 002, RF-322). Se aplica el grupo del agente ChapterCore si existe; si no, el grupo «*».

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `RobotsRules` | interface | — |
| `parseRobots` | function | Agrupa las reglas por agente y devuelve las que aplican a ChapterCore. |
| `isPathAllowed` | function | Gana la regla más larga que coincide; a igual longitud, gana Allow (RFC 9309 §2.2.2). |
| `RobotsService` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `isAllowed()` | Promise<boolean> | ¿Puede ChapterCore descargar esta URL oficial? Si robots.txt no se lee, se permite. |


## Enlaces

- [[M3 - official-sources]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
