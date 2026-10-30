---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/page-fetcher.service.spec.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba page-fetcher.service.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 11 casos de prueba (Jest).

### Casos

- **PageFetcherService**
  - convierte HTML en texto sin scripts, estilos ni comentarios
  - solo conserva enlaces oficiales absolutos
  - rechaza URLs fuera de la allowlist sin hacer peticiones
  - sigue redirecciones relativas y absolutas dentro de los sitios oficiales
  - corta tras 3 redirecciones
  - rechaza páginas de más de 1 MB
  - rechaza contenido que no es HTML
  - informa errores HTTP de la fuente
  - comprueba la IP de cada host antes de conectar
- **isPrivateAddress**
  - bloquea %s
  - permite %s

## Enlaces

- [[M3 - page-fetcher.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
