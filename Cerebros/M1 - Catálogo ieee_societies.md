---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/opportunities/entities/ieee-society.entity.ts
  - backendChapterCoreIEEE/src/database/migrations/1792368000000-CreateOpportunities.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Catálogo ieee_societies

[[M1 - Capítulos y sociedades]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué es
> Tabla compartida con las sociedades IEEE y grupos de afinidad que se usan como capítulos en cargos, contactos y oportunidades.

> [!info] Confirmado en el código
> - Campos: `sigla` y `nombre_oficial` únicos, `tipo` (`sociedad` o `grupo_afinidad`), `sitio_oficial` (https).
> - Carga inicial: PES, CIS, ComSoc, CASS, EMBS, RAS, IAS, CS y **WIE** (grupo de afinidad).
> - Un capítulo con personas, contactos u oportunidades asociadas no se puede borrar (`ON DELETE RESTRICT`).

> [!warning] No es la lista de capítulos activos
> Solo se agregan entradas verificadas en fuentes oficiales IEEE (`CONTEXTO.md` §5 y §7). Estar en el catálogo no significa que la Rama tenga ese capítulo.

## Enlaces

- Forma parte de [[M1 - Capítulos y sociedades]].

## Fuentes

- `backendChapterCoreIEEE/src/opportunities/entities/ieee-society.entity.ts`
- `backendChapterCoreIEEE/src/database/migrations/1792368000000-CreateOpportunities.ts`
