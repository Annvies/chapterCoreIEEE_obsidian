---
type: dto
modulo: 7
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/expenses/dto/list-expenses-query.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - dto
---

# M7 - DTO ListExpensesQueryDto

[[M7 - DTO y validaciones]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Dto
> Contrato de datos `ListExpensesQueryDto` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).

Hereda de `ExpenseSummaryQueryDto`.

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `categoria` | `ExpenseCategory` | sí | `@IsOptional()`, `@IsIn(EXPENSE_CATEGORIES)` |
| `page` | `number` | sí | `@IsOptional()`, `@Type(() => Number)`, `@IsInt()`, `@Min(1)` |
| `limit` | `number` | sí | `@IsOptional()`, `@Type(() => Number)`, `@IsInt()`, `@Min(1)`, `@Max(MAX_PAGE_SIZE)` |

## Enlaces

- [[M7 - DTO ExpenseSummaryQueryDto]]
- [[M7 - expense]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
