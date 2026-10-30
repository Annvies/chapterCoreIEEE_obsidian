---
type: endpoint
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/discovery.controller.ts
actualizado: 2026-10-30
aliases:
  - "POST /opportunities/discover"
tags:
  - chaptercore
  - modulo-3
  - endpoint
---

# M3 - POST opportunities › discover

[[M3 - API]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Endpoint
> `POST /opportunities/discover` · acceso: Oportunidades · Ver.

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/opportunities/discover` |
| Acceso | Oportunidades · Ver |
| Controlador | `backendChapterCoreIEEE/src/opportunities/discovery/discovery.controller.ts` → `discover()` |
| Respuesta | `OK` |
| Devuelve | `Promise<DiscoveryResponse>` |

### Entradas

- Cuerpo → `DiscoverDto`
- Usa la persona autenticada (`@CurrentUser`)

### Lógica que invoca

- `DiscoveryService.discover()`

> [!note] Comentario del controlador
> Búsqueda en fuentes oficiales IEEE e historial (spec 002, contracts/api-rest.md). Cualquier persona con sesión (nivel Ver, RF-315); «Extraer ficha» y «Publicar» siguen exigiendo Editar.

### Consumido por el frontend

- [[M3 - Cliente API opportunities]]

## Enlaces

- [[M3 - discovery.service]]
- [[M3 - DTO DiscoverDto]]
- [[M3 - Cliente API opportunities]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
