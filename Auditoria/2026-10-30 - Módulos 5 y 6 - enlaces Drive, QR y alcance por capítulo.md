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

# 2026-10-30 — Módulos 5 y 6: enlaces Drive, QR y alcance por capítulo

## Pedido

Sincronizar y enriquecer la bóveda con la skill obsidian-cerebros, revisando solo el
Cerebro central y los cerebros de los módulos 5 y 6, con nodos nuevos que tengan callouts
`abstract`, `info` y `success` y apunten a los archivos reales de código creados.

## Qué se hizo

| Área | Cambio | Archivos |
|---|---|---|
| Cerebros · M5 (nuevo) | Concepto del campo `drive_link` que sustituye la carga de archivos | `Cerebros/M5 - Enlaces de Drive.md` |
| Cerebros · M6 (nuevo) | Concepto del KPI `escaneosQr` (visitas con origen QR del periodo) | `Cerebros/M6 - Escaneos de QR.md` |
| Cerebros · M6 (nuevo) | Concepto del `scope` branch/chapter y lo que ve el Director de capítulo | `Cerebros/M6 - Alcance por capítulo.md` |
| Cerebro central | Integraciones pendientes y flujo Módulo 4 → Módulo 6 marcados como propuestos en los PR #27 y #28 | 1 |
| Cerebros 5 y 6 | Campos, archivos, cobertura, pendientes y conexiones según los PR | 2 |
| Subgrupos y conceptos M5 | `Datos y privacidad`, `Archivos adjuntos`, `Tipos de campo` enlazan el nuevo concepto | 3 |
| Subgrupos y conceptos M6 | `Indicadores`, `Periodos y filtros`, `Limitaciones del dashboard`: pendientes resueltos por el PR #28 | 3 |

No se editaron notas generadas (`generado: true`), el canvas, la configuración ni los
cerebros de los módulos 1 a 4.

## Fuentes consultadas

Repositorio `marianZamorano/chapterCoreIEEE`, ramas de los PR sin fusionar en `main`:

- PR #27, `feat/modulo-5-drive-links` (`3169b49`):
  `backendChapterCoreIEEE/src/forms/schema/form-schema.types.ts`,
  `backendChapterCoreIEEE/src/forms/schema/form-schema.zod.ts`,
  `backendChapterCoreIEEE/src/forms/public-forms.controller.ts`,
  `backendChapterCoreIEEE/src/forms/form-submissions.service.ts`,
  `frontendChapterCoreIEEE/src/features/public/DynamicForm.tsx`,
  `frontendChapterCoreIEEE/src/features/responses/SubmissionDetail.tsx`,
  `frontendChapterCoreIEEE/src/lib/form-schema-helpers.ts`,
  `specs/007-modulo-5-drive-links/spec.md`.
- PR #28, `feat/modulo-6-dashboard-qr-chapter-scope` (`3034dfe`):
  `backendChapterCoreIEEE/src/auth/domain/permissions.ts`,
  `backendChapterCoreIEEE/src/dashboard/dashboard.controller.ts`,
  `backendChapterCoreIEEE/src/dashboard/dashboard.module.ts`,
  `backendChapterCoreIEEE/src/dashboard/dashboard.service.ts`,
  `backendChapterCoreIEEE/src/dashboard/dashboard.types.ts`,
  `backendChapterCoreIEEE/src/difusion/entities/link-visit.entity.ts`,
  `frontendChapterCoreIEEE/src/types/dashboard.ts`,
  `frontendChapterCoreIEEE/src/features/dashboard/DashboardPage.tsx`,
  `specs/008-modulo-6-dashboard-qr-chapter-scope/spec.md`.

## Verificación

- Lint: 0 errores, 0 avisos, 12 sugerencias (antes 14: se resolvieron los pendientes de
  `M6 - Limitaciones del dashboard` y `M6 - Periodos y filtros`).
- Enlaces `[[...]]` de las notas nuevas resueltos (el lint no reporta enlaces rotos).
- Canvas sin cambios: solo llega al nivel de subgrupo.

## Hallazgos y correcciones

- El Cerebro central, el Cerebro 6 y las notas M6 daban como pendientes los escaneos QR y
  el filtro por capítulo; el PR #28 los implementa (H-01 y H-02 de la spec 001).
- El Cerebro 5 describía la carga de archivos como camino vigente; el PR #27 la sustituye
  por enlaces de Google Drive para los envíos nuevos.
- Las notas nuevas llevan `estado: propuesto` porque el código aún no está en `main`.

## Pendiente o por decidir

- Al fusionar los PR #27 y #28 en `main`: pasar las tres notas nuevas a `estado:
  confirmado`, quitar las marcas «pendiente de fusión» y ejecutar
  `scripts/mapear_repositorio.py` para regenerar las notas técnicas (nuevas pruebas
  `public-forms.controller.spec.ts`, `SubmissionDetail.test.tsx`, `FieldPalette.test.tsx`,
  `api.test.ts` y los cambios del dashboard).
- `server.mjs where` no encuentra el repositorio del producto en esta máquina: configurar
  con `setup` (archivo personal, no versionado) cuando se quiera usar el MCP.
- Equipo: acordar cómo interpretar los escaneos QR junto con los demás indicadores.
