---
type: cerebro
modulo: 7
estado: propuesto
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

> [!warning] Estado: propuesto, en rama
> El código está en la rama `feat/modulo-7-gastos-tesoreria` del producto, **todavía no
> integrado en `main`**. El módulo amplía el MVP de seis módulos y espera la aprobación de
> la enmienda 2.1.0 de la constitución y de la spec 009 por al menos dos integrantes.
> Fuente: `specs/009-modulo-7-gastos-tesoreria/spec.md`, `CONTEXTO.md` §4.

## Código

Pantalla `/tesoreria` · módulo backend `expenses/` · spec
[`specs/009-modulo-7-gastos-tesoreria`](https://github.com/marianZamorano/chapterCoreIEEE/tree/feat/modulo-7-gastos-tesoreria/specs/009-modulo-7-gastos-tesoreria).
Los enlaces apuntan a la rama; cuando se integre, cambiarán a `main`.

| Capa | Archivo |
|---|---|
| Migración | [`1792886400000-CreateExpensesModule.ts`](https://github.com/marianZamorano/chapterCoreIEEE/blob/feat/modulo-7-gastos-tesoreria/backendChapterCoreIEEE/src/database/migrations/1792886400000-CreateExpensesModule.ts) |
| Entidad | [`entities/expense.entity.ts`](https://github.com/marianZamorano/chapterCoreIEEE/blob/feat/modulo-7-gastos-tesoreria/backendChapterCoreIEEE/src/expenses/entities/expense.entity.ts) |
| Reglas de dominio | [`domain/expense.ts`](https://github.com/marianZamorano/chapterCoreIEEE/blob/feat/modulo-7-gastos-tesoreria/backendChapterCoreIEEE/src/expenses/domain/expense.ts) |
| DTOs | [`dto/`](https://github.com/marianZamorano/chapterCoreIEEE/tree/feat/modulo-7-gastos-tesoreria/backendChapterCoreIEEE/src/expenses/dto) |
| Repositorio | [`repositories/expenses.repository.ts`](https://github.com/marianZamorano/chapterCoreIEEE/blob/feat/modulo-7-gastos-tesoreria/backendChapterCoreIEEE/src/expenses/repositories/expenses.repository.ts) |
| Servicio | [`services/expenses.service.ts`](https://github.com/marianZamorano/chapterCoreIEEE/blob/feat/modulo-7-gastos-tesoreria/backendChapterCoreIEEE/src/expenses/services/expenses.service.ts) |
| Controlador | [`controllers/expenses.controller.ts`](https://github.com/marianZamorano/chapterCoreIEEE/blob/feat/modulo-7-gastos-tesoreria/backendChapterCoreIEEE/src/expenses/controllers/expenses.controller.ts) |
| Permisos | [`auth/domain/permissions.ts`](https://github.com/marianZamorano/chapterCoreIEEE/blob/feat/modulo-7-gastos-tesoreria/backendChapterCoreIEEE/src/auth/domain/permissions.ts) (`Feature.Expenses`) |
| Pantalla | [`features/expenses/ExpensesPage.tsx`](https://github.com/marianZamorano/chapterCoreIEEE/blob/feat/modulo-7-gastos-tesoreria/frontendChapterCoreIEEE/src/features/expenses/ExpensesPage.tsx) |
| Registro | [`features/expenses/ExpenseDialog.tsx`](https://github.com/marianZamorano/chapterCoreIEEE/blob/feat/modulo-7-gastos-tesoreria/frontendChapterCoreIEEE/src/features/expenses/ExpenseDialog.tsx) + [`expense-schema.ts`](https://github.com/marianZamorano/chapterCoreIEEE/blob/feat/modulo-7-gastos-tesoreria/frontendChapterCoreIEEE/src/features/expenses/expense-schema.ts) (Zod) |
| Cliente y tipos | [`api/expenses.ts`](https://github.com/marianZamorano/chapterCoreIEEE/blob/feat/modulo-7-gastos-tesoreria/frontendChapterCoreIEEE/src/api/expenses.ts) · [`types/expenses.ts`](https://github.com/marianZamorano/chapterCoreIEEE/blob/feat/modulo-7-gastos-tesoreria/frontendChapterCoreIEEE/src/types/expenses.ts) |

> [!abstract] Propósito
> Registrar los gastos de la Rama y de cada capítulo y conocer cuánto se gastó en un
> periodo. Le da una función propia al cargo Tesorero, que existe en la Rama y en los
> capítulos (`auth/domain/position.ts`) pero no tenía módulo.

> [!info] Datos del gasto (tabla `expenses`)
> - **Concepto** (1–200), **categoría** (`evento`, `material`, `transporte`,
>   `alimentacion`, `servicios`, `otro`), **monto** `numeric(12,2)` mayor que 0 y **fecha**
>   de calendario, que no puede ser futura.
> - **Alcance:** `chapter_id` hacia `ieee_societies`; vacío significa gasto de la Rama.
> - **Comprobante:** solo un enlace `https` opcional; ChapterCore no lo abre ni lo verifica.
> - **Autoría:** `created_by`; al eliminar se guardan `deleted_at` y `deleted_by`.
> - El monto viaja como texto (`"1250.50"`) y los totales se suman en SQL, para no perder
>   céntimos.

> [!success] Flujo y permisos
> 1. La Mesa Directiva o un Director de capítulo abre **Registrar gasto**; el formulario se
>    valida con Zod y luego con `ExpenseInputDto` en el servidor.
> 2. `POST /expenses` guarda el gasto; tabla y tarjeta **Total gastado** se recargan.
> 3. `GET /expenses` lista con filtros de periodo, categoría y alcance (20 por página).
> 4. `GET /expenses/summary` devuelve el total, la cantidad y el desglose por categoría.
> 5. `DELETE /expenses/:id` hace una eliminación lógica: el gasto deja de listarse y de
>    sumar.
>
> | Nivel | Acceso | Qué puede hacer |
> |---|---|---|
> | Mesa Directiva | Total | Todo, incluida la eliminación |
> | Secretaría | Ver | Consultar tabla y total |
> | Director de capítulo | Editar (su capítulo) | Registrar y consultar solo su capítulo |
> | Miembro | — | Sin acceso |
>
> El alcance «su capítulo» lo aplica el servidor con `resolveExpenseScope`, leyendo
> `chapterOnly` de la matriz: el mismo patrón que usa el dashboard del
> [[Cerebro 6 - Feedback y KPIs]].

> [!warning] Límites
> - No se pueden editar gastos: un error se corrige eliminando y registrando de nuevo.
> - Sin ingresos, presupuestos, saldos ni exportación.
> - Una sola moneda para toda la Rama.
> - Un Director que registró un gasto por error debe pedir su eliminación a la Mesa
>   Directiva.

> [!todo] Pendientes
> - Aprobar la enmienda 2.1.0 y la spec 009 (al menos dos integrantes).
> - **A-1:** confirmar la moneda; el código asume `BOB` (`lib/format.ts`).
> - **A-2:** confirmar si la Secretaría puede ver los gastos.
> - **A-3:** confirmar si hace falta editar gastos.
> - Ejecutar la migración en una base local y recorrer el quickstart (tareas T011 y T030).
> - Ampliar la skill (`MODULES` en `mcp/server.mjs` y `range(1, 7)` en
>   `scripts/mapear_repositorio.py`) para generar los subgrupos y las notas técnicas
>   `M7 - …`, como en los otros cerebros.

> [!example] Verificación registrada
> Antes de publicar la rama (2026-10-30): backend con 295 pruebas y frontend con 87 pruebas
> en verde, y typecheck, lint y build sin errores, sobre el código actual de `dev`. Sin
> prueba contra una base de datos real todavía. Detalle en
> `specs/009-modulo-7-gastos-tesoreria/tasks.md`.

## Conexiones

- Usa la matriz de permisos, los cargos y el catálogo de capítulos de
  [[Cerebro 1 - Base institucional]].
- El selector de alcance usa el catálogo `GET /contacts/chapters` del
  [[Cerebro 2 - Contactos]], porque el de oportunidades no expone el `id` del capítulo.
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
