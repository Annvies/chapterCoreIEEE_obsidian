---
type: prueba
modulo: 7
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/expenses/expense-schema.test.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - prueba
---

# M7 - Prueba expense-schema.test

[[M7 - Pruebas]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Prueba
> 6 casos de prueba (Vitest + Testing Library).

### Casos

- **validateExpense**
  - convierte el formulario en el cuerpo de POST /expenses
  - rechaza el monto %j
  - acepta hoy y rechaza fechas futuras
  - exige concepto y categoría
  - solo acepta comprobantes https
- **currentMonthRange**
  - va del primer al último día del mes

## Enlaces

- [[M7 - expense-schema]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
