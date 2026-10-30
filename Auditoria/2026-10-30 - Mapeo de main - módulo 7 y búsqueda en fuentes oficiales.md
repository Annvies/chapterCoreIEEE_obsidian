---
type: auditoria
fecha: 2026-10-30
agente: Claude Code (claude-opus-5-5)
solicitado_por: valelop2606
rama: main
commits: []
tags:
  - auditoria
---

# 2026-10-30 — Mapeo de `main`: módulo 7 y búsqueda en fuentes oficiales

## Pedido

Mapear la información nueva de la rama `main` del producto (commit `fb852aa`), actualizar
los cerebros y, si corresponde, añadir un cerebro nuevo respetando la estructura base.

## Qué se hizo

| Área | Cambio | Archivos |
|---|---|---|
| Skill | El mapeador y el servidor MCP reconocen el **Módulo 7** (`expenses/`, `features/expenses/`, tabla `expenses`), la tabla `opportunity_searches` y los hooks `useOpportunityDiscovery`, `useSearchHistory` y `useOfficialDomains`; `module_context` acepta 1–7 | `scripts/mapear_repositorio.py`, `mcp/server.mjs` |
| Skill (documentación) | Siete cerebros en `SKILL.md`; fila del Módulo 7 y archivos de la spec 002 en el mapa módulo → código | `SKILL.md`, `references/chaptercore-mapa-codigo.md`, `references/arquitectura-conocimiento.md` |
| Cerebro 7 | Reescrito con la estructura base: 3 subgrupos (Registro de gastos, Alcance y permisos, Totales y filtros), 6 conceptos y `M7 - Código del módulo`. Estado corregido: el código ya está en `main` | 11 notas curadas |
| Cerebro 3 | 3 conceptos nuevos (Búsqueda en fuentes oficiales, Catálogo de respaldo, Historial de búsquedas); se actualizaron el subgrupo Descubrimiento, el cerebro, las fuentes oficiales admitidas y la nota de código | 7 notas curadas |
| Cerebros 5 y 6 | «PR #27/#28 pendiente de fusión» corregido a «en `main` con el PR #29» | 10 notas curadas |
| Cerebro central y README | Siete cerebros; módulos 3, 5, 6 y 7 descritos según `main` | 2 |
| Notas generadas | Regeneradas desde `origin/main`: 94 nuevas (M3 búsqueda en fuentes oficiales, M5 pruebas nuevas y 41 técnicas del M7). De las 273 que ya existían, 48 cambiaron su contenido y 225 solo la fecha `actualizado` | 367 |
| Canvas | Subgrupos, código y 6 grupos técnicos del M7; se quitó «(propuesto)» del grupo | `ChapterCore - Cerebros.canvas` |

## Fuentes consultadas

- `git log` y `git diff a2749db..fb852aa` del producto (PR #24 a #42).
- `CONTEXTO.md` §4, §7 y §9 (versión de `main`).
- `backendChapterCoreIEEE/src/expenses/`, `auth/domain/permissions.ts`, migración `1792886400000-CreateExpensesModule.ts`.
- `backendChapterCoreIEEE/src/opportunities/discovery/`, `official-domains.ts`, `opportunities.module.ts`, migración `1792972800000-CreateOpportunitySearchHistory.ts`.
- `frontendChapterCoreIEEE/src/features/expenses/`, `lib/format.ts`, `App.tsx`, `components/AppShell.tsx`.
- `dashboard/` y `forms/schema/` para confirmar que los PR #27 y #28 están en `main`.

## Verificación

- Lint: **0 errores, 0 avisos**, 16 sugerencias (pendientes `todo`/`question` en las notas).
- Enlaces rotos: 0. Canvas: JSON válido y sin notas de estructura fuera de él.
- Las notas generadas salen de una exportación limpia de `origin/main` (`git archive`)
  y no de la copia de trabajo del clon del producto, que tiene cambios sin commitear.
  La exportación temporal se borró al terminar.

## Hallazgos y correcciones

- El Cerebro 7 decía que el código estaba «en rama, no integrado en `main`»: llegó a `main`
  con el PR #31 (`607d4b8`).
- `CONTEXTO.md` sigue describiendo el Módulo 7 como «propuesto… pendiente de aprobación e
  integración», lo que contradice el código de `main`.
- Varias notas de los módulos 5 y 6 decían que los PR #27 y #28 estaban «pendientes de
  fusión»: ya están en `main` desde el PR #29.
- El Cerebro 3 decía que no había recorrido de fuentes: desde el PR #42 se recorren a
  petición de una persona.
- La estrategia `busqueda_sitio` está en el enum `discovery_strategy`, pero no hay
  ninguna implementación registrada (solo estáticas, navegador y catálogo).
- El clon local del producto tiene cambios sin commitear que eliminan el panel de extracción
  (`ExtractPanel`, `DraftCard`, `useOpportunityExtraction`…) y modifican `CONTEXTO.md` y la
  spec 002. No se tocaron. Cuando lleguen a `main`, habrá que volver a ejecutar el mapeador.

## Pendiente o por decidir

- **Equipo:** registrar en `CONTEXTO.md` la aprobación del Módulo 7 y la enmienda 2.1.0, y
  resolver las aclaraciones A-1 (moneda `BOB`), A-2 (si la Secretaría ve los gastos) y A-3
  (si se pueden editar gastos).
- **Equipo:** implementar o quitar la estrategia `busqueda_sitio`; ampliar los dominios
  oficiales desde el sitemap de IEEE (pendiente de la spec 002).
- **Bóveda:** las notas `CC - …` (mockups, navegación, matriz de permisos) aún no
  mencionan la pantalla `/tesoreria` ni `Feature.Expenses`.
