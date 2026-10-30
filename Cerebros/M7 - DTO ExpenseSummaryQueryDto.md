---
type: dto
modulo: 7
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/expenses/dto/expense-summary-query.dto.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - dto
---

# M7 - DTO ExpenseSummaryQueryDto

[[M7 - DTO y validaciones]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Dto
> Filtros comunes del listado y del resumen.

| Campo | Tipo | Opcional | Validaciones |
|---|---|---|---|
| `alcance` | `string` | sí | `@IsOptional()`, `@Matches(/^(rama\|[1-9]\d{0,4})$/, { message: "El alcance debe ser 'rama' o el id de un cap…` |
| `desde` | `string` | sí | `@IsOptional()`, `@Matches(ISO_DATE, { message: 'La fecha inicial debe tener formato aaaa-mm-dd.' })` |
| `hasta` | `string` | sí | `@IsOptional()`, `@Matches(ISO_DATE, { message: 'La fecha final debe tener formato aaaa-mm-dd.' })` |

## Enlaces

- [[Cerebro 7 - Tesorería y Gastos]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
