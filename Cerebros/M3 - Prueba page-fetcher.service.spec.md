---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/page-fetcher.service.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba page-fetcher.service.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 15 casos de prueba (Jest).

### Casos

- **PageFetcherService**
  - convierte HTML en texto sin scripts, estilos ni comentarios
  - solo conserva enlaces oficiales absolutos
  - rechaza URLs fuera de la allowlist sin hacer peticiones
  - sigue redirecciones relativas y absolutas dentro de los sitios oficiales
  - se identifica con el agente de usuario propio de ChapterCore
  - devuelve el HTML y el tipo de contenido de la página final
  - corta la descarga cuando se aborta la señal externa, antes de su propio límite
  - no descarga nada si la señal externa ya está abortada
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
