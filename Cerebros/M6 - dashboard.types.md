---
type: dominio
modulo: 6
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/dashboard/dashboard.types.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-6
  - dominio
---

# M6 - dashboard.types

[[M6 - Lógica del backend]] · [[Cerebro 6 - Feedback y KPIs]]

> [!abstract] Dominio
> Periodos del mockup 02: último mes, semestre y gestión completa.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DASHBOARD_PERIODS` | const | Periodos del mockup 02: último mes, semestre y gestión completa. |
| `DashboardPeriod` | type | — |
| `DashboardRange` | interface | — |
| `DashboardSatisfaction` | interface | — |
| `DashboardNps` | interface | — |
| `DashboardChapterRank` | interface | — |
| `DashboardFeedbackItem` | interface | — |
| `DashboardScope` | type | Alcance del resumen según la matriz de permisos: `branch` para quien ve toda la Rama y `chapter` para el Director de capítulo ("Ver (su capítulo)"). |
| `DashboardResponses` | interface | — |
| `DashboardSummary` | interface | Los campos que admiten null lo hacen en alcance `chapter`: oportunidades, formularios, respuestas y QR no tienen asociación de capítulo y no se muestran para no exponer métricas globales de la Rama. |


## Enlaces

- [[Cerebro 6 - Feedback y KPIs]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
