---
type: concepto
modulo: 5
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - concepto
---

# M5 - Estados del formulario

[[M5 - Diseño de formularios]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Qué es
> Tabla `forms`: el formulario y su URL pública.

> [!info] Confirmado en el código
> - Estados: `draft`, `published` y `archived`.
> - `slug` único entre formularios activos (minúsculas, dígitos y guiones): es la URL pública.
> - Borrado lógico con `deleted_at`.

## Enlaces

- Forma parte de [[M5 - Diseño de formularios]].
- Relacionada con [[M5 - Tipos de campo]], [[M5 - Visibilidad condicional]].

## Fuentes

- `backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts`
