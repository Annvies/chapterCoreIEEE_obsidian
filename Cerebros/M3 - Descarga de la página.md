---
type: concepto
modulo: 3
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/opportunities/page-fetcher.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - concepto
---

# M3 - Descarga de la página

[[M3 - Extracción y revisión]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Qué es
> El backend descarga la página de la convocatoria antes de enviarla a la IA, con límites estrictos.

> [!info] Confirmado en el código
> - Máximo 3 redirecciones, 1 MB, 20 s de espera.
> - Se convierte a texto (máx. 40.000 caracteres) y se conservan hasta 150 enlaces.

## Enlaces

- Forma parte de [[M3 - Extracción y revisión]].
- Relacionada con [[M3 - Fuentes oficiales admitidas]], [[M3 - Extracción con Gemini]].

## Fuentes

- `backendChapterCoreIEEE/src/opportunities/page-fetcher.service.ts`
