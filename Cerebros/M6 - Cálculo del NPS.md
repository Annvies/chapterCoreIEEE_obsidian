---
type: concepto
modulo: 6
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/dashboard/dashboard.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-6
  - concepto
---

# M6 - Cálculo del NPS

[[M6 - Lectura del feedback]] · [[Cerebro 6 - Feedback y KPIs]]

> [!abstract] Qué es
> Net Promoter Score de las respuestas de recomendación.

> [!info] Confirmado en el código
> - Usa campos `scale` con `useInKpis` cuyo máximo es **≥ 10**.
> - Promotores ≥ 9, detractores ≤ 6, el resto neutrales.
> - `NPS = % promotores − % detractores`, redondeado a 1 decimal.

## Enlaces

- Forma parte de [[M6 - Lectura del feedback]].
- Relacionada con [[M6 - Satisfacción promedio]], [[M6 - Feedback reciente]].

## Fuentes

- `backendChapterCoreIEEE/src/dashboard/dashboard.service.ts`
