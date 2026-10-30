---
type: repositorio
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/repositories/auth-tokens.repository.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - repositorio
---

# M1 - auth-tokens.repository

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Repositorio
> Archivo de repositorio del backend (`auth/repositories/auth-tokens.repository.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `AuthTokensRepository` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `findByHash()` | Promise<AuthToken \| null> | — |
| `findByHashForUpdate()` | Promise<AuthToken \| null> | Bloquea la fila hasta el fin de la transacción para que el enlace no se canjee dos veces. |
| `replacePending()` | — | Guarda un token nuevo y descarta los pendientes del mismo usuario y propósito. |
| `markUsed()` | Promise<void> | — |
| `deletePendingForUser()` | — | — |


## Enlaces

- [[M1 - one-time-token]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
