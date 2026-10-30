---
type: concepto
modulo: 3
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/opportunities/gemini-extractor.service.ts
  - backendChapterCoreIEEE/src/opportunities/opportunities.service.ts
  - backendChapterCoreIEEE/src/opportunities/opportunities.controller.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - concepto
---

# M3 - Extracción con Gemini

[[M3 - Extracción y revisión]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Qué es
> Gemini propone una ficha estructurada a partir del texto de la página; nunca publica.

> [!info] Confirmado en el código
> - Modelo configurable (`GEMINI_MODEL`), `temperature: 0`, respuesta con esquema fijo, 60 s de espera.
> - Límite: **5 extracciones por minuto** (consume cuota del nivel gratuito).
> - Controles anti‑invención: avisa si el año de la fecha límite no aparece en la página, si la fecha ya pasó o si hay cifras que no están en la fuente.

> [!warning] Revisión humana obligatoria
> La ficha es una propuesta con advertencias; una persona con permiso de edición decide si la publica.

## Enlaces

- Forma parte de [[M3 - Extracción y revisión]].
- Relacionada con [[M3 - Fuentes oficiales admitidas]], [[M3 - Descarga de la página]].

## Fuentes

- `backendChapterCoreIEEE/src/opportunities/gemini-extractor.service.ts`
- `backendChapterCoreIEEE/src/opportunities/opportunities.service.ts`
- `backendChapterCoreIEEE/src/opportunities/opportunities.controller.ts`
