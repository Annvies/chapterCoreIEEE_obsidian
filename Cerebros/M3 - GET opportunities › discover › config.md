---
type: endpoint
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/discovery.controller.ts
actualizado: 2026-10-30
aliases:
  - "GET /opportunities/discover/config"
tags:
  - chaptercore
  - modulo-3
  - endpoint
---

# M3 - GET opportunities › discover › config

[[M3 - API]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Endpoint
> `GET /opportunities/discover/config` · acceso: Oportunidades · Ver.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/opportunities/discover/config` |
| Acceso | Oportunidades · Ver |
| Controlador | `backendChapterCoreIEEE/src/opportunities/discovery/discovery.controller.ts` → `getConfig()` |
| Devuelve | `Promise<DiscoveryConfig>` |

### Lógica que invoca

- `DiscoveryService.getConfig()`

> [!note] Comentario del controlador
> Búsqueda en fuentes oficiales IEEE e historial (spec 002, contracts/api-rest.md). Cualquier persona con sesión (nivel Ver, RF-315); «Extraer ficha» y «Publicar» siguen exigiendo Editar.

### Consumido por el frontend

- [[M3 - Cliente API opportunities]]

## Enlaces

- [[M3 - discovery.service]]
- [[M3 - Cliente API opportunities]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
