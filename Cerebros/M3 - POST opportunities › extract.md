---
type: endpoint
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/opportunities.controller.ts
actualizado: 2026-10-30
aliases:
  - "POST /opportunities/extract"
tags:
  - chaptercore
  - modulo-3
  - endpoint
---

# M3 - POST opportunities › extract

[[M3 - API]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Endpoint
> Cada extracción descarga una página y consume cuota del nivel gratuito de Gemini.

| Campo | Valor |
|---|---|
| Método | `POST` |
| Ruta | `/opportunities/extract` |
| Acceso | Oportunidades · Editar |
| Controlador | `backendChapterCoreIEEE/src/opportunities/opportunities.controller.ts` → `extract()` |
| Límite | 5 peticiones por 60 s |
| Respuesta | `OK` |
| Devuelve | `Promise<OpportunityDraftView>` |

### Entradas

- Cuerpo → `ExtractOpportunityDto`

### Lógica que invoca

- `OpportunitiesService.extract()`

> [!note] Comentario del controlador
> Los guards globales del Módulo 1 exigen sesión y permiso; ver es para todos los niveles y extraer/publicar exige Editar (CONTEXTO.md §7). El límite de peticiones se mantiene.

### Consumido por el frontend

- [[M3 - Cliente API opportunities]]

## Enlaces

- [[M3 - opportunities.service]]
- [[M3 - DTO ExtractOpportunityDto]]
- [[M3 - Cliente API opportunities]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
