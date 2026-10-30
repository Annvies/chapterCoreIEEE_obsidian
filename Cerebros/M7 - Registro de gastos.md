---
tags:
  - chaptercore
  - modulo-7
  - subgrupo
---

# Registro de gastos

[[Cerebro 7 - Tesorería y Gastos]] · Qué se guarda de cada gasto

> [!abstract] Propósito
> Dejar constancia de cada gasto de la Rama o de un capítulo con los datos mínimos para
> sumarlo y justificarlo: concepto, categoría, monto, fecha y, si existe, un enlace al
> comprobante.

> [!info] Cómo se registra
> En `/tesoreria`, **Registrar gasto** abre un diálogo que valida con Zod
> (`features/expenses/expense-schema.ts`); el servidor repite la validación con
> `ExpenseInputDto` y la base de datos con restricciones `CHECK`. Las tres capas aplican
> los mismos límites.

> [!warning] Sin edición
> No existe ruta para modificar un gasto: un error se corrige eliminándolo y registrándolo
> de nuevo (ver [[M7 - Eliminación lógica]]). Si debe poder editarse sigue abierto
> (aclaración A-3 de la spec 009).

## Enlaces

Quién puede registrar y en qué alcance: [[M7 - Alcance y permisos]]. Cómo se suman los
gastos registrados: [[M7 - Totales y filtros]].

## Notas del subgrupo

- [[M7 - Modelo de datos expenses]]
- [[M7 - Categorías y validaciones]]
