---
type: prueba
modulo: 6
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/dashboard/dashboard.service.spec.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-6
  - prueba
---

# M6 - Prueba dashboard.service.spec

[[M6 - Pruebas]] · [[Cerebro 6 - Feedback y KPIs]]

> [!abstract] Prueba
> 4 casos de prueba (Jest).

### Casos

- **DashboardService**
  - calcula métricas, NPS, ranking y feedback reciente
  - sin datos devuelve KPIs nulos y mantiene las limitaciones
  - management no filtra respuestas por fecha
  - usa semester por defecto

## Enlaces

- [[M6 - dashboard.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
