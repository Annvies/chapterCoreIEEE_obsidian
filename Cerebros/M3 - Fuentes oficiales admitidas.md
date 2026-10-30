---
type: concepto
modulo: 3
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/opportunities/official-sources.ts
  - backendChapterCoreIEEE/src/opportunities/official-domains.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - concepto
---

# M3 - Fuentes oficiales admitidas

[[M3 - Extracción y revisión]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Qué es
> Solo se extraen y publican oportunidades de dominios oficiales verificados.

> [!info] Confirmado en el código
> - Dominios: `ieee.org` y subdominios, `ieee-pes.org`, `comsoc.org`, `ieee-cas.org`, `embs.org`, `ieee-ras.org` y `computer.org`.
> - Solo `https`, sin usuario ni contraseña en la URL y sin puertos distintos de 443.
> - La sociedad se infiere del dominio (p. ej. `wie.ieee.org` → WIE).
> - Desde la spec 002 la lista vive en `official-domains.ts` y es la **única fuente** para
>   resultados, extracción y publicación. Cada dominio guarda la URL oficial que lo
>   acredita y la fecha de verificación (2026-10-19); uno que deja de ser oficial no se
>   borra, se marca como retirado con su motivo.
> - No basta con que el dominio contenga «ieee». `GET /opportunities/official-domains` expone
>   la misma lista; desde el PR #43 la interfaz ya no la usa (se quitó `lib/officialSources.ts`).

## Enlaces

- Forma parte de [[M3 - Extracción y revisión]].
- Relacionada con [[M3 - Descarga de la página]], [[M3 - Extracción con Gemini]], [[M3 - Búsqueda en fuentes oficiales]].

## Fuentes

- `backendChapterCoreIEEE/src/opportunities/official-sources.ts`
- `backendChapterCoreIEEE/src/opportunities/official-domains.ts`
