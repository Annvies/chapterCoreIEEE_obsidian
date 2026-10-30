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

# M5 - Versionado de formularios

[[M5 - Respuestas y versiones]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Qué es
> Tabla `form_versions`: cada cambio de estructura es una versión nueva.

> [!info] Confirmado en el código
> - El esquema se guarda como JSON (`jsonb`) con número de versión correlativo.
> - Como máximo **un borrador** y **una versión publicada** por formulario.
> - Cada respuesta apunta a la versión que respondió (`form_version_id`).

## Enlaces

- Forma parte de [[M5 - Respuestas y versiones]].
- Relacionada con [[M5 - Estados de una respuesta]].

## Fuentes

- `backendChapterCoreIEEE/src/database/migrations/1730000000000-CreateFormsModule.ts`
