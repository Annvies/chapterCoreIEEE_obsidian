---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/robots.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba robots.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 8 casos de prueba (Jest).

### Casos

- **parseRobots / isPathAllowed**
  - %s → permitido=%s
  - usa el grupo propio de ChapterCore si existe, en lugar del de *
  - una línea Disallow vacía no prohíbe nada
  - respeta * y $ en las rutas
- **RobotsService**
  - descarga /robots.txt del host una sola vez y aplica sus reglas
  - permite la descarga si robots.txt no se puede leer
  - pasa la señal del presupuesto a la descarga de robots.txt
  - no consulta robots.txt de URLs que no son oficiales

## Enlaces

- [[M3 - robots]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
