---
type: dto
modulo: 7
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/expenses/dto/expense-input.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - dto
---

# M7 - DTO ExpenseInputDto

[[M7 - DTO y validaciones]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Dto
> Cuerpo de POST /expenses. No hay edición en esta entrega (spec 009, A-3).

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `concepto` | `string` | no | `@Trim()`, `@IsString()`, `@Length(1, EXPENSE_LIMITS.concepto, { message: `El concepto debe tener entre 1 y ${EXPENSE…` |
| `categoria` | `ExpenseCategory` | no | `@IsIn(EXPENSE_CATEGORIES, { message: 'La categoría no es válida.' })` |
| `monto` | `number` | no | `@IsNumber( { maxDecimalPlaces: 2, allowNaN: false, allowInfinity: false }, { message: 'El…`, `@Min(0.01, { message: 'El monto debe ser mayor a 0.' })`, `@Max(MAX_MONTO, { message: 'El monto supera el máximo permitido.' })` |
| `fecha` | `string` | no | `@Matches(ISO_DATE, { message: 'La fecha debe tener formato aaaa-mm-dd.' })` |
| `chapterId` | `number \| null` | sí | `@IsOptional()`, `@IsInt()`, `@Min(1)` |
| `comprobanteUrl` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@IsUrl( { protocols: ['https'], require_protocol: true }, { message: 'El comprobante debe…`, `@MaxLength(EXPENSE_LIMITS.comprobanteUrl)` |
| `notas` | `string \| null` | sí | `@EmptyToNull()`, `@IsOptional()`, `@IsString()`, `@MaxLength(EXPENSE_LIMITS.notas)` |

## Enlaces

- [[M7 - expense]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
