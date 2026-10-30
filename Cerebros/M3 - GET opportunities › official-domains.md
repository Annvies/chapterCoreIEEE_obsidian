---
type: endpoint
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/opportunities.controller.ts
actualizado: 2026-10-30
aliases:
  - "GET /opportunities/official-domains"
tags:
  - chaptercore
  - modulo-3
  - endpoint
---

# M3 - GET opportunities › official-domains

[[M3 - API]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Endpoint
> Lista verificada (spec 002, RF-329): la interfaz valida las URLs igual que el servidor.

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/opportunities/official-domains` |
| Acceso | Oportunidades · Ver |
| Controlador | `backendChapterCoreIEEE/src/opportunities/opportunities.controller.ts` → `listOfficialDomains()` |
| Devuelve | `OfficialDomainView[]` |

> [!note] Comentario del controlador
> Los guards globales del Módulo 1 exigen sesión y permiso; ver es para todos los niveles y extraer/publicar exige Editar (CONTEXTO.md §7). El límite de peticiones se mantiene.

> [!question] Sin llamada directa en el frontend
> No se encontró una llamada a esta ruta en `frontendChapterCoreIEEE/src`. Puede usarse con una
> URL que devuelve el servidor, desde fuera de la app (p. ej. un QR) o no usarse todavía.

## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
