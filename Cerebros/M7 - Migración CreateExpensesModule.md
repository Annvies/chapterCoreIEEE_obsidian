---
type: migración
modulo: 7
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792886400000-CreateExpensesModule.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - migración
---

# M7 - Migración CreateExpensesModule

[[M7 - Base de datos]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Migración
> Módulo 7: gastos de la Rama y de sus capítulos (specs/009-modulo-7-gastos-tesoreria). Depende de ieee_societies (alcance opcional) y de users (autoría y eliminación), creadas en migraciones anteriores. La eliminación es lógica (deleted_at).

| Campo | Valor |
|---|---|
| Archivo | `1792886400000-CreateExpensesModule.ts` |
| Marca de tiempo | `1792886400000` (orden de ejecución) |
| Reversible | sí, tiene `down()` |

### Qué hace

- Extensión `pgcrypto`
- Crea la tabla `expenses`
- Índice `expenses_fecha_idx` en `expenses`
- Índice `expenses_chapter_fecha_idx` en `expenses`

## Enlaces

- [[M7 - Tabla expenses]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
