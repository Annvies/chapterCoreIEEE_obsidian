---
type: dto
modulo: 6
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/dashboard/dto/dashboard-query.dto.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-6
  - dto
---

# M6 - DTO DashboardQueryDto

[[M6 - DTO y validaciones]] · [[Cerebro 6 - Feedback y KPIs]]

> [!abstract] Dto
> Contrato de datos `DashboardQueryDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `period` | `DashboardPeriod` | sí | `@IsOptional()`, `@IsIn(DASHBOARD_PERIODS)` |

## Enlaces

- [[Cerebro 6 - Feedback y KPIs]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
