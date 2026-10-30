---
type: prueba
modulo: 7
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/expenses/services/expenses.service.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-7
  - prueba
---

# M7 - Prueba expenses.service.spec

[[M7 - Pruebas]] · [[Cerebro 7 - Tesorería y Gastos]]

> [!abstract] Prueba
> 12 casos de prueba (Jest).

### Casos

- **ExpensesService.create**
  - registra un gasto de la Rama con la autoría y el monto con dos decimales
  - asocia el gasto al capítulo elegido por la Mesa Directiva
  - usa el capítulo del Director cuando no indica ninguno
  - impide que el Director registre gastos de otro capítulo
  - rechaza fechas futuras, imposibles y capítulos inexistentes
  - devuelve la vista con el capítulo y quién registró el gasto
- **ExpensesService.list**
  - pagina con 20 por defecto y aplica los filtros
  - limita al Director a su capítulo y rechaza la Rama
  - rechaza un periodo invertido
- **ExpensesService.summary**
  - devuelve el total del repositorio con el periodo consultado
- **ExpensesService.remove**
  - elimina de forma lógica registrando quién lo hizo
  - responde 404 si el gasto no existe o ya fue eliminado

## Enlaces

- [[M7 - expenses.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
