---
type: concepto
modulo: 6
estado: propuesto
fuentes:
  - backendChapterCoreIEEE/src/auth/domain/permissions.ts
  - backendChapterCoreIEEE/src/dashboard/dashboard.controller.ts
  - backendChapterCoreIEEE/src/dashboard/dashboard.service.ts
  - backendChapterCoreIEEE/src/dashboard/dashboard.types.ts
  - frontendChapterCoreIEEE/src/types/dashboard.ts
  - frontendChapterCoreIEEE/src/features/dashboard/DashboardPage.tsx
  - specs/008-modulo-6-dashboard-qr-chapter-scope/spec.md
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-6
  - concepto
---

# M6 - Alcance por capítulo

[[M6 - Periodos y filtros]] · [[Cerebro 6 - Feedback y KPIs]]

> [!abstract] Qué es
> El campo `scope` del resumen del Dashboard: `branch` (toda la Rama) o `chapter` (solo
> el capítulo de quien consulta, «Ver (su capítulo)» en la matriz de permisos).

> [!info] En el código (PR #28, rama `feat/modulo-6-dashboard-qr-chapter-scope`, sin fusionar en `main`)
> - El alcance sale de `chapterOnly` en `PERMISSION_MATRIX[Feature.Dashboard]`
>   (`auth/domain/permissions.ts`); el controlador pasa el usuario autenticado al
>   servicio (`dashboard/dashboard.controller.ts`).
> - **Mesa Directiva y Secretaría:** `scope: 'branch'` con todas las métricas.
> - **Director de capítulo:** solo `miembrosActivos` y `rankingCapitulos` filtrados por
>   su `chapterId`. Oportunidades, formularios, respuestas, satisfacción, NPS, feedback
>   y escaneos QR llegan como `null` porque no tienen asociación de capítulo
>   (`chapterSummary` en `dashboard/dashboard.service.ts`).
> - **Director sin capítulo asignado:** 0 miembros, ranking vacío y una limitación que
>   lo explica.
> - En la interfaz, los tipos son una unión discriminada por `scope`
>   (`types/dashboard.ts`); la vista de capítulo muestra «Pulso de tu capítulo», el
>   panel «Tu capítulo» y el aviso «No disponible para este alcance»
>   (`features/dashboard/DashboardPage.tsx`).

> [!success] Qué resuelve
> El hallazgo H-02: la matriz asignaba «Ver (su capítulo)» al Director, pero el
> Dashboard le devolvía las métricas de toda la Rama.

> [!warning] Decisión tomada
> Las oportunidades no tienen capítulo; se decidió no mostrarle al Director el total de
> la Rama en lugar de aproximarlo. Asociar oportunidades, formularios o enlaces a un
> capítulo requeriría migración y decisión del equipo.

## Enlaces

- Forma parte de [[M6 - Periodos y filtros]].
- Relacionada con [[M6 - Miembros activos y ranking]], [[M6 - Escaneos de QR]] y
  [[M6 - Limitaciones del dashboard]].

## Fuentes

- PR #28 de `marianZamorano/chapterCoreIEEE` (commit `3034dfe`), pendiente de fusión.
- `specs/008-modulo-6-dashboard-qr-chapter-scope/spec.md`
