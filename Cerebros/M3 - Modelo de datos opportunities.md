---
type: concepto
modulo: 3
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792368000000-CreateOpportunities.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - concepto
---

# M3 - Modelo de datos opportunities

[[M3 - Publicación y búsqueda]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Qué es
> Tabla `opportunities`: fichas en borrador o publicadas.

> [!info] Confirmado en el código
> - Campos: título (1–300), tipo, fecha límite, elegibilidad (lista, máx. 50), beneficio, enlace, sociedad, `fuente_url` y fecha de consulta.
> - Estados: `borrador` y `publicada`; `published_at` existe solo si está publicada.
> - Borrado lógico con `deleted_at`.
> - No se puede publicar dos veces el mismo enlace.
> - Límite: 10 publicaciones por minuto.

## Enlaces

- Forma parte de [[M3 - Publicación y búsqueda]].

## Fuentes

- `backendChapterCoreIEEE/src/database/migrations/1792368000000-CreateOpportunities.ts`
