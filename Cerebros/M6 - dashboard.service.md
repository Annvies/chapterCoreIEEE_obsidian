---
type: servicio
modulo: 6
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/dashboard/dashboard.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-6
  - servicio
---

# M6 - dashboard.service

[[M6 - Lógica del backend]] · [[Cerebro 6 - Feedback y KPIs]]

> [!abstract] Servicio
> Archivo de servicio del backend (`dashboard/dashboard.service.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DashboardService` | class | Módulo 6 · Feedback, métricas y KPIs (mockup 02). Fórmulas confirmadas el 2026-10-19: - Satisfacción: media aritmética de campos `scale` con `useInKpis` (1–5). - NPS: %promotores (>= 9) - %detractores (<= 6) sobre campos `scale` 0–10. - Periodos: month = 30 días, semester = 180 días, management = histórico. - Miembros activos: usuarios con status `active`. Eventos, asistencia y escaneos de QR no tienen fuente de datos todavía. |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `summary()` | Promise<DashboardSummary> | — |


## Enlaces

- [[Cerebro 6 - Feedback y KPIs]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
