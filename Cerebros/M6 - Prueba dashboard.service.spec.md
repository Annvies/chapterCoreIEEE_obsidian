---
type: prueba
modulo: 6
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/dashboard/dashboard.service.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-6
  - prueba
---

# M6 - Prueba dashboard.service.spec

[[M6 - Pruebas]] · [[Cerebro 6 - Feedback y KPIs]]

> [!abstract] Prueba
> 9 casos de prueba (Jest).

### Casos

- **DashboardService**
  - calcula métricas, NPS, ranking y feedback reciente
  - cuenta escaneos de QR dentro del periodo
  - management cuenta todos los escaneos de QR
  - Secretaría también ve el alcance de la Rama
  - el Director de capítulo solo ve miembros y ranking de su capítulo
  - un Director sin capítulo asignado no ve métricas de la Rama
  - sin datos devuelve KPIs nulos y mantiene las limitaciones
  - management no filtra respuestas por fecha
  - usa semester por defecto

## Enlaces

- [[M6 - dashboard.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
