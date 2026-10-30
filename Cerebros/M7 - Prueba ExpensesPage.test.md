---
type: prueba
modulo: 7
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/expenses/ExpensesPage.test.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - prueba
---

# M7 - Prueba ExpensesPage.test

[[M7 - Pruebas]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Prueba
> 5 casos de prueba (Vitest + Testing Library).

### Casos

- **Tesorería**
  - muestra el total gastado, el desglose y la tabla a la Mesa Directiva
  - la Secretaría solo consulta: sin registrar ni eliminar
  - el Director de capítulo no elige alcance y registra en su capítulo
  - valida con Zod antes de enviar y recarga tabla y total al guardar
  - elimina un gasto solo después de confirmar

## Enlaces

- [[M7 - ExpensesPage]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
