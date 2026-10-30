---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/official-sources.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba official-sources.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 7 casos de prueba (Jest).

### Casos

- **official-sources**
  - acepta la fuente oficial %s
  - normaliza mayúsculas del host
  - normaliza enlaces para detectar duplicados
  - infiere la sociedad solo de hosts verificados
  - **lista verificada de dominios**
    - los dominios aceptados son los de la lista que no están retirados
    - rechaza un dominio retirado
    - no acepta un dominio solo porque contenga «ieee»

## Enlaces

- [[M3 - official-sources]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
