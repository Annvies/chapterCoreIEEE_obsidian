---
type: endpoint
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/opportunities.controller.ts
actualizado: 2026-10-30
aliases:
  - "POST /opportunities"
tags:
  - chaptercore
  - modulo-3
  - endpoint
---

# M3 - POST opportunities

[[M3 - API]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Endpoint
> `POST /opportunities` · acceso: Oportunidades · Editar.

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/opportunities` |
| Acceso | Oportunidades · Editar |
| Controlador | `backendChapterCoreIEEE/src/opportunities/opportunities.controller.ts` → `publish()` |
| Límite | 10 peticiones por 60 s |
| Devuelve | `Promise<OpportunityView>` |

### Entradas

- Cuerpo → `CreateOpportunityDto`

### Lógica que invoca

- `OpportunitiesService.publish()`

> [!note] Comentario del controlador
> Los guards globales del Módulo 1 exigen sesión y permiso; ver es para todos los niveles y extraer/publicar exige Editar (CONTEXTO.md §7). El límite de peticiones se mantiene.

### Consumido por el frontend

- [[M3 - Cliente API opportunities]]

## Enlaces

- [[M3 - opportunities.service]]
- [[M3 - DTO CreateOpportunityDto]]
- [[M3 - Cliente API opportunities]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
