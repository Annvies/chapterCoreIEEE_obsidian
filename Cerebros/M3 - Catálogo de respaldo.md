---
type: concepto
modulo: 3
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/catalog/catalog.ts
  - backendChapterCoreIEEE/src/opportunities/discovery/strategies/catalog.strategy.ts
  - CONTEXTO.md
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - concepto
---

# M3 - Catálogo de respaldo

[[M3 - Descubrimiento]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Qué es
> El último paso de la [[M3 - Búsqueda en fuentes oficiales]]: un archivo versionado con
> páginas oficiales ya leídas, para que la búsqueda dé resultados en producción, donde no
> hay navegador y algunos sitios IEEE pueden rechazar las IP de nube.

> [!info] Confirmado en el código
> - Archivo `opportunities/discovery/catalog/catalogo-oficial.json`, de como máximo 400
>   entradas (`MAX_CATALOG_ENTRIES`).
> - Se valida al cargarlo; si no es válido o está vacío no se usa. Es **dato no
>   confiable**: sus entradas pasan por el mismo filtro que los resultados en vivo.
> - Sus resultados muestran la fecha del catálogo, siguen «sin verificar» y avisan si
>   tiene más días de los configurados (`OPPORTUNITY_DISCOVERY_CATALOG_MAX_AGE_DAYS`;
>   `CONTEXTO.md` §7 habla de 30 días).
> - **Se regenera a mano** con `npm run discovery:catalog`, en local y con aprobación,
>   antes de cada integración a `main`. No hay recorrido programado.

## Enlaces

- Forma parte de [[M3 - Descubrimiento]].
- Relacionada con [[M3 - Búsqueda en fuentes oficiales]], [[M3 - Fuentes oficiales admitidas]].

## Fuentes

- `backendChapterCoreIEEE/src/opportunities/discovery/catalog/catalog.ts`
- `backendChapterCoreIEEE/src/opportunities/discovery/catalog/build-catalog.ts`
- `backendChapterCoreIEEE/src/opportunities/discovery/strategies/catalog.strategy.ts`
- `CONTEXTO.md` §7
