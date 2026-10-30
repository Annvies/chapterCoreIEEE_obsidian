---
type: auditoria
fecha: 2026-10-30
agente: Claude Code (claude-opus-5-5)
solicitado_por: valelop2606
rama: main
commits:
  - 3ac3a00
tags:
  - auditoria
---

# 2026-10-30 — Remapeo completo de `main` y navegabilidad

## Pedido

Volver a mapear todo el repositorio del producto en `main` tras los nuevos cambios,
respetando la estructura de los cerebros y el tipo de información de cada uno, con más
nodos por cerebro, y asegurar que cada cerebro sea navegable.

## Qué se hizo

| Área | Cambio | Archivos |
|---|---|---|
| Skill (mapeador) | Nuevos tipos de nota generada: **una por migración** (qué crea o cambia y sobre qué tablas, enlazada a sus tablas), **una por módulo Nest** (imports, controladores, proveedores, enlazada a sus servicios y endpoints) y archivos de `dto/` sin clases (`transforms.ts`). Las pruebas de hooks ya se asignan a su módulo. Se corrigió la línea en blanco que se acumulaba en las notas «Código del módulo» y la capitalización de tipos («Módulo Nest») | `scripts/mapear_repositorio.py` |
| Skill | Script `navegabilidad.mjs` para comprobar que cada cerebro llega a todas sus notas; `SKILL.md` y el mapa módulo → código actualizados | 3 |
| Notas generadas | Regeneradas desde `origin/main` (`54d8d14`): **+20** nuevas (10 migraciones, 8 módulos Nest, `M1 - transforms`, `M3 - Prueba useOpportunityDiscovery.test`) y **−11** de la interfaz de extracción retirada | 334 notas generadas |
| Cerebro 3 | PR #43: la extracción con IA se retiró de la interfaz. Se actualizaron el cerebro, 4 subgrupos o conceptos y la nota de código, y se creó la decisión [[M3 - Retiro de la extracción en la interfaz]] | 8 |
| Cerebro 1 | `M1 - Permisos compartidos`: fila de Gastos y «su capítulo» ya filtra en Dashboard y Gastos | 1 |
| Cerebro central (`CC - …`) | Tesorería en el menú, en las rutas, en la matriz y en la base de datos; migraciones nuevas; `ExpensesModule`; variables `OPPORTUNITY_DISCOVERY_*` (solo nombres); límite de la búsqueda por persona; decisiones y pendientes al día | 10 |

## Fuentes consultadas

- `git log fb852aa..54d8d14` del producto (PR #43, commit `18b8aa8`).
- `CONTEXTO.md` §7 y §9 y `specs/002-oportunidades-fuentes-oficiales/spec.md`.
- `frontendChapterCoreIEEE/src/api/opportunities.ts`, `App.tsx`, `components/AppShell.tsx`.
- `backendChapterCoreIEEE/src/app.module.ts`, `auth/domain/permissions.ts`, `database/migrations/`,
  `*.module.ts` y los `config.get(...)` del backend (solo los nombres de las variables).

## Verificación

- Lint: **0 errores, 0 avisos**, 20 sugerencias (pendientes `todo`/`question` en las notas).
- Navegabilidad (`scripts/navegabilidad.mjs`): desde el cerebro central se alcanzan
  506/506 notas en 4 clics como máximo; desde cada cerebro, el 100 % de las notas de su
  módulo en 3 clics como máximo (M1 108, M2 58, M3 98, M4 51, M5 79, M6 28, M7 44).
- Las notas generadas salen de una exportación limpia de `origin/main` (`git archive`); la
  exportación temporal se borró al terminar.

## Hallazgos y correcciones

- Varias notas del Módulo 3 describían el panel «Extraer convocatoria» y la acción «Extraer
  ficha», que ya no existen en la interfaz. Desde el PR #43 **no se puede publicar** desde la
  interfaz, aunque los endpoints siguen en el backend.
- `GET /opportunities/official-domains` ya no se consulta desde la interfaz (se quitó
  `lib/officialSources.ts`).
- `M1 - Permisos compartidos` y `CC - Autorización por permisos` no tenían la fila de Gastos y
  decían que «su capítulo» aún no filtraba.
- `CC - Base de datos PostgreSQL` listaba 6 de las 10 migraciones.

## Pendiente o por decidir

- **Equipo:** cómo se publicarán oportunidades nuevas ahora que la interfaz no lo permite.
- **Equipo:** registrar en `CONTEXTO.md` la aprobación del Módulo 7 (sigue «propuesto»).
- **Bóveda:** los archivos compartidos del frontend (`api/client.ts`, `components/` comunes,
  `lib/dates.ts`, `lib/format.ts`) y del backend (`main.ts`, `app.module.ts`,
  `database/data-source.ts`) no tienen nota generada propia; se describen en las notas `CC - …`.
