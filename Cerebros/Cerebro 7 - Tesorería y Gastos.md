---
type: cerebro
modulo: 7
estado: confirmado
fuentes:
  - specs/009-modulo-7-gastos-tesoreria/spec.md
  - backendChapterCoreIEEE/src/expenses/
  - backendChapterCoreIEEE/src/auth/domain/permissions.ts
  - backendChapterCoreIEEE/src/database/migrations/1792886400000-CreateExpensesModule.ts
  - frontendChapterCoreIEEE/src/features/expenses/
  - CONTEXTO.md
actualizado: 2026-10-30
aliases:
  - Módulo 7
  - Tesorería
  - Gastos
tags:
  - chaptercore
  - modulo-7
---

# Cerebro 7 — Control de gastos y tesorería

Parte de [[ChapterCore - Cerebro central]] · cerebro especializado del Módulo 7

> [!warning] Estado: código en `main`, aprobación formal pendiente
> El código se integró en `dev` con el PR #30 (`01dc806`, 2026-10-30) y llegó a `main` con
> el PR #31 (`607d4b8`). Pero `CONTEXTO.md` §4 y §9 siguen describiendo el módulo como «propuesto…
> pendiente de aprobación e integración»: falta registrar la enmienda 2.1.0 de la
> constitución y la aprobación de al menos dos integrantes, y actualizar `CONTEXTO.md`.

## Código

Documentación técnica: [[M7 - Código del módulo]] (endpoints, archivos, pantallas y pruebas).
Pantalla `/tesoreria` · módulo backend `expenses/` · spec
`specs/009-modulo-7-gastos-tesoreria/`.

## Subgrupos conectados

- [[M7 - Registro de gastos]]
- [[M7 - Alcance y permisos]]
- [[M7 - Totales y filtros]]

> [!abstract] Propósito
> Registrar los gastos de la Rama y de cada capítulo y conocer cuánto se gastó en un
> periodo. Le da una función propia al cargo Tesorero, que existe en la Rama y en los
> capítulos (`auth/domain/position.ts`) pero no tenía módulo.

> [!info] Datos del gasto (tabla `expenses`)
> Concepto, categoría, monto, fecha, alcance (Rama o capítulo), enlace de comprobante
> opcional y notas. Detalle en [[M7 - Modelo de datos expenses]] y
> [[M7 - Categorías y validaciones]].

> [!success] Flujo y permisos
> 1. La Mesa Directiva o un Director de capítulo abre **Registrar gasto**; el formulario se
>    valida con Zod y luego con `ExpenseInputDto` en el servidor.
> 2. `POST /expenses` guarda el gasto; tabla y tarjeta **Total gastado** se recargan.
> 3. `GET /expenses` lista con filtros de periodo, categoría y alcance (20 por página).
> 4. `GET /expenses/summary` devuelve el total, la cantidad y el desglose por categoría.
> 5. `DELETE /expenses/:id` hace una [[M7 - Eliminación lógica]].
>
> | Nivel | Acceso | Qué puede hacer |
> |---|---|---|
> | Mesa Directiva | Total | Todo, incluida la eliminación |
> | Secretaría | Ver | Consultar tabla y total |
> | Director de capítulo | Editar (su capítulo) | Registrar y consultar solo su capítulo |
> | Miembro | — | Sin acceso |
>
> El alcance «su capítulo» lo aplica el servidor: [[M7 - Alcance por capítulo de gastos]].

> [!warning] Límites
> - No se pueden editar gastos: un error se corrige eliminando y registrando de nuevo.
> - Sin ingresos, presupuestos, saldos ni exportación.
> - Una sola moneda para toda la Rama ([[M7 - Moneda y montos]]).
> - Un Director que registró un gasto por error debe pedir su eliminación a la Mesa
>   Directiva.

> [!todo] Pendientes
> - Registrar en `CONTEXTO.md` la aprobación del módulo y la enmienda 2.1.0 (el código ya
>   está en `main`).
> - **A-1:** confirmar la moneda; el código asume `BOB` (`lib/format.ts`).
> - **A-2:** confirmar si la Secretaría puede ver los gastos.
> - **A-3:** confirmar si hace falta editar gastos.
> - Ejecutar la migración en una base local y recorrer el quickstart (tareas T011 y T030).

> [!example] Verificación registrada
> Antes de publicar la rama (2026-10-30): backend con 295 pruebas y frontend con 87 pruebas
> en verde, y typecheck, lint y build sin errores. Sin prueba contra una base de datos real
> todavía. Detalle en `specs/009-modulo-7-gastos-tesoreria/tasks.md`.

## Conexiones

- Usa la matriz de permisos, los cargos y el catálogo de capítulos de
  [[Cerebro 1 - Base institucional]].
- El selector de alcance usa el catálogo `GET /contacts/chapters` del
  [[Cerebro 2 - Contactos]].
- Guarda los comprobantes como enlaces, igual que los formularios del
  [[Cerebro 5 - Secretaría y formularios]] guardan enlaces de Drive en lugar de archivos.
- No alimenta el [[Cerebro 6 - Feedback y KPIs]]: los gastos no aparecen en el dashboard.

## Fuentes

- `specs/009-modulo-7-gastos-tesoreria/` (spec, plan, research, data-model, contratos y
  tareas) y `docs/spec-modulo-7-gastos.md`.
- `backendChapterCoreIEEE/src/expenses/` y
  `backendChapterCoreIEEE/src/database/migrations/1792886400000-CreateExpensesModule.ts`.
- `backendChapterCoreIEEE/src/auth/domain/permissions.ts` (fila `Feature.Expenses`).
- `frontendChapterCoreIEEE/src/features/expenses/`, `src/api/expenses.ts` y
  `src/types/expenses.ts`.
- `CONTEXTO.md` §4 y §9; `.specify/memory/constitution.md` (enmienda 2.1.0 propuesta).
