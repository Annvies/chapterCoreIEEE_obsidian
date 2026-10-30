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

# M6 - Satisfacción promedio

[[M6 - Lectura del feedback]] · [[Cerebro 6 - Feedback y KPIs]]

> [!abstract] Qué es
> Promedio de las calificaciones de satisfacción.

> [!info] Confirmado en el código
> - Usa campos `scale` con `useInKpis` cuyo máximo es **≤ 5**.
> - Media aritmética redondeada a 2 decimales, con el tamaño de la muestra.

## Enlaces

- Forma parte de [[M6 - Lectura del feedback]].
- Relacionada con [[M6 - Cálculo del NPS]], [[M6 - Feedback reciente]].

## Fuentes

- `backendChapterCoreIEEE/src/dashboard/dashboard.service.ts`
