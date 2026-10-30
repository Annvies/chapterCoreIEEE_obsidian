---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/opportunities.service.spec.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba opportunities.service.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 17 casos de prueba (Jest).

### Casos

- **buildDraft**
  - conserva los datos válidos y deduce el capítulo del host
  - no inventa datos ausentes y lo advierte
  - descarta enlaces que no aparecen en la página
  - advierte de fechas límite pasadas
  - advierte si el año o las cifras no figuran en la página (anclaje en la fuente)
- **ungroundedNumbers**
  - compara cifras ignorando separadores de miles
- **parseSearchTerms**
  - interpreta tipos y siglas y descarta palabras vacías
  - reconoce términos en inglés y siglas cortas
- **isValidIsoDate**
  - valida fechas de calendario reales
- **OpportunitiesService**
  - publica con estado y fecha fijados por el servidor y el enlace normalizado
  - rechaza capítulos fuera del catálogo
  - responde 409 si el enlace ya está publicado
  - traduce la violación del índice único (carrera) a 409
  - sin clave de IA no descarga la página
  - no llama a la IA si la página no tiene texto suficiente
  - responde 422 si la IA indica que no es una oportunidad
  - devuelve la ficha normalizada sin guardarla

## Enlaces

- [[M3 - opportunities.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
