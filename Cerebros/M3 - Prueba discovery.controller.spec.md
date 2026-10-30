---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/discovery.controller.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba discovery.controller.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 11 casos de prueba (Jest).

### Casos

- **DiscoveryController (HTTP)**
  - todas las rutas exigen sesión y el nivel Ver de oportunidades (RF-315)
  - POST /opportunities/discover devuelve 200 con la forma del contrato
  - acepta forzar una estrategia válida
  - limita a 3 búsquedas por minuto por persona; otra persona no comparte el límite
  - GET /opportunities/discover/config devuelve la configuración
  - **historial (RF-325)**
    - lista solo el historial de quien pregunta
    - elimina una entrada propia con 204
    - responde 404 si la entrada no existe o es de otra persona
    - rechaza ids que no son UUID
    - vacía solo el historial propio
  - no escribe el texto buscado en los registros durante la petición HTTP (RF-345)

## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
