---
type: concepto
modulo: 5
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/forms/schema/form-schema.types.ts
  - backendChapterCoreIEEE/src/forms/schema/form-schema.zod.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - concepto
---

# M5 - Tipos de campo

[[M5 - Diseño de formularios]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Qué es
> Once tipos de campo validados con Zod.

> [!info] Confirmado en el código
> - `text`, `textarea`, `email`, `number`, `select`, `radio`, `checkbox`, `scale`, `date`, `file` y `membership_number`.
> - Validaciones posibles: longitud, mínimo/máximo, patrón, fechas, tamaño y tipos de archivo.

> [!info] Cambio propuesto (PR #27, pendiente de fusión)
> Se añade `drive_link`; `file` deja de ofrecerse en el constructor y solo se conserva
> para leer versiones publicadas antiguas. Ver [[M5 - Enlaces de Drive]].
> - `scale` va de 1 a 5 por defecto; con `useInKpis` alimenta el Dashboard.

## Enlaces

- Forma parte de [[M5 - Diseño de formularios]].
- Relacionada con [[M5 - Visibilidad condicional]], [[M5 - Estados del formulario]].

## Fuentes

- `backendChapterCoreIEEE/src/forms/schema/form-schema.types.ts`
- `backendChapterCoreIEEE/src/forms/schema/form-schema.zod.ts`
