---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/discovery.service.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba discovery.service.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 29 casos de prueba (Jest).

### Casos

- **DiscoveryService**
  - (a) se detiene en la primera estrategia con resultados válidos
  - (b) sin resultados válidos pasa a la siguiente
  - (c) una estrategia desactivada se informa y se salta
  - (d) un error pasa a la siguiente y muestra solo mensajes controlados
  - (e) al agotarse el presupuesto, la estrategia en curso termina como tiempo_agotado y no se ejecutan más
  - (e) pasa a las estrategias un margen de cierre anterior al fin del presupuesto
  - (f) forzar %s ejecuta solo esa estrategia
  - (f) OPPORTUNITY_DISCOVERY_FORCE_STRATEGY fuerza en desarrollo
  - (f) un valor desconocido en OPPORTUNITY_DISCOVERY_FORCE_STRATEGY se ignora
  - (g) forzar en producción se rechaza; la variable se ignora
  - forzar una estrategia desactivada se rechaza
  - (h) una segunda búsqueda simultánea de la misma persona se rechaza (429)
  - (i) sin estrategias habilitadas responde 503
  - (j) descarta lo que ya está publicado (enlace o fuente)
  - (k) el contador de páginas es común a todas las estrategias
  - rechaza una consulta sin palabras significativas
  - getConfig informa umbral, estrategias con etiqueta y si se puede forzar
  - **historial**
    - guarda la búsqueda con resultados y devuelve su id
    - guarda también la búsqueda sin resultados y la que agotó el tiempo
    - no guarda las peticiones rechazadas antes de buscar
    - si el guardado falla, devuelve los resultados igual con id null
  - **privacidad y contenido no confiable**
    - no escribe el texto buscado en los registros (logs), tampoco cuando fallan las estrategias
    - devuelve títulos y fragmentos como texto plano, sin etiquetas
  - **catálogo de respaldo**
    - (b) con resultados en vivo no se consulta el catálogo
    - sin coincidencias, muestra las más recientes con el aviso (RF-353)
    - (c) en modo producción no se puede forzar el catálogo
    - (d) si falla el guardado del historial, responde igual con id null
    - (e) fuera de producción se puede forzar solo el catálogo
    - C5: si las estrategias en vivo nunca terminan, el catálogo responde dentro del presupuesto

## Enlaces

- [[M3 - discovery.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
