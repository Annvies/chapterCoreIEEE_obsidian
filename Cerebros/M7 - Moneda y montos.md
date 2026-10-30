---
type: concepto
modulo: 7
estado: confirmado
fuentes:
  - frontendChapterCoreIEEE/src/lib/format.ts
  - backendChapterCoreIEEE/src/expenses/repositories/expenses.repository.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - concepto
---

# M7 - Moneda y montos

[[M7 - Totales y filtros]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Qué es
> Cómo viajan y se muestran los importes para no perder céntimos.

> [!info] Confirmado en el código
> - El backend envía los montos y totales como **texto** (`"1250.50"`), no como número
>   de coma flotante.
> - `formatMoney` los muestra con `Intl.NumberFormat('es', { style: 'currency' })` y la
>   moneda única `CURRENCY = 'BOB'` (`frontendChapterCoreIEEE/src/lib/format.ts`).

> [!question] Supuesto pendiente
> La moneda en bolivianos es un **supuesto** del código («porque la Rama es de la UPB»);
> la aclaración A-1 de la spec 009 sigue abierta. Hay una sola moneda para toda la Rama.

## Enlaces

- Forma parte de [[M7 - Totales y filtros]].
- Relacionada con [[M7 - Total gastado por periodo]], [[M7 - Modelo de datos expenses]].

## Fuentes

- `frontendChapterCoreIEEE/src/lib/format.ts`
- `backendChapterCoreIEEE/src/expenses/repositories/expenses.repository.ts`
