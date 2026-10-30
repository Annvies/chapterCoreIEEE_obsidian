---
tags:
  - chaptercore
  - modulo-7
  - subgrupo
---

# Alcance y permisos de la tesorería

[[Cerebro 7 - Tesorería y Gastos]] · Quién ve, registra y elimina

> [!abstract] Propósito
> Dar al cargo Tesorero y a la Mesa Directiva una vista de todos los gastos, y a cada
> Director de capítulo una vista limitada a su capítulo.

> [!info] Fila `Feature.Expenses` de la matriz
> | Nivel | Acceso | Qué puede hacer |
> |---|---|---|
> | Mesa Directiva | Total | Consultar, registrar y eliminar en cualquier alcance |
> | Secretaría | Ver | Consultar tabla y total |
> | Director de capítulo | Editar (solo su capítulo) | Registrar y consultar su capítulo |
> | Miembro | Ninguno | Sin acceso; no ve la entrada **Tesorería** del menú |
>
> Fuente: `backendChapterCoreIEEE/src/auth/domain/permissions.ts`. El Tesorero pertenece a
> la Mesa Directiva (`MESA_DIRECTIVA_CARGOS`).

> [!question] Por confirmar
> Si la Secretaría debe ver los gastos sigue abierto (aclaración A-2 de la spec 009); el
> código ya le da acceso Ver.

## Enlaces

Los permisos salen de la matriz del [[Cerebro 1 - Base institucional]]. Lo que se
registra: [[M7 - Registro de gastos]]. Lo que se suma: [[M7 - Totales y filtros]].

## Notas del subgrupo

- [[M7 - Alcance por capítulo de gastos]]
- [[M7 - Eliminación lógica]]
