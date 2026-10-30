---
type: guard
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/user-throttler.guard.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - guard
---

# M3 - user-throttler.guard

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Guard
> Límite de búsquedas en fuentes oficiales POR PERSONA (spec 002, RF-315 y RF-316), no por IP: varias personas detrás de la misma red no se bloquean entre sí. En memoria y por instancia, como el resto del throttler del proyecto (research.md H-R5).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DISCOVERY_LIMIT_MESSAGE` | const | — |
| `discoveryRateLimit` | function | Búsquedas por minuto y persona (OPPORTUNITY_DISCOVERY_RATE_LIMIT, 3 por defecto). |
| `UserThrottlerGuard` | class | — |


## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
