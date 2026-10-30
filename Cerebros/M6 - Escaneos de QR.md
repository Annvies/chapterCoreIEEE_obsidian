---
type: concepto
modulo: 6
estado: propuesto
fuentes:
  - backendChapterCoreIEEE/src/dashboard/dashboard.service.ts
  - backendChapterCoreIEEE/src/dashboard/dashboard.module.ts
  - backendChapterCoreIEEE/src/difusion/entities/link-visit.entity.ts
  - frontendChapterCoreIEEE/src/features/dashboard/DashboardPage.tsx
  - specs/008-modulo-6-dashboard-qr-chapter-scope/spec.md
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-6
  - concepto
---

# M6 - Escaneos de QR

[[M6 - Indicadores]] · [[Cerebro 6 - Feedback y KPIs]]

> [!abstract] Qué es
> El KPI `escaneosQr` del Dashboard: cuántas veces se abrió un enlace corto desde su
> código QR durante el periodo elegido.

> [!info] En el código (PR #28, en `main` con el PR #29)
> - Cuenta las filas de `link_visits` con `origen = 'qr'`; el QR codifica la URL corta
>   con `?o=qr` (`difusion/entities/link-visit.entity.ts`).
> - Filtra por `visited_at` desde el inicio del periodo; en `management` cuenta todo el
>   histórico (`countQrScans` en `dashboard/dashboard.service.ts`).
> - `DashboardModule` registra `LinkVisit` (`dashboard/dashboard.module.ts`).
> - La tarjeta «Escaneos de QR» muestra la cifra (`features/dashboard/DashboardPage.tsx`).
> - Solo se calcula con alcance de Rama; para el Director llega como `null` (ver
>   [[M6 - Alcance por capítulo]]).

> [!success] Qué resuelve
> El hallazgo H-01: el Dashboard mostraba los escaneos como «sin datos aún» aunque el
> Módulo 4 ya registraba cada visita.

## Enlaces

- Forma parte de [[M6 - Indicadores]].
- Relacionada con [[M6 - Alcance por capítulo]] y [[M6 - Limitaciones del dashboard]].

## Fuentes

- PR #28 de `marianZamorano/chapterCoreIEEE` (commit `3034dfe`), integrado en `dev` (`fc0c916`) y en `main` con el PR #29 (`cdc4abf`).
- `specs/008-modulo-6-dashboard-qr-chapter-scope/spec.md`
