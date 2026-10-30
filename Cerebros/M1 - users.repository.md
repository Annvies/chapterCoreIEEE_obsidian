---
type: repositorio
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/repositories/users.repository.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - repositorio
---

# M1 - users.repository

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Repositorio
> Archivo de repositorio del backend (`auth/repositories/users.repository.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `UserSearchCriteria` | interface | — |
| `UsersRepository` | class | Acceso a datos de usuarios. Los servicios no usan TypeORM directamente. |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `findById()` | Promise<User \| null> | — |
| `findByEmail()` | Promise<User \| null> | — |
| `findByEmailWithSecret()` | Promise<User \| null> | Incluye password_hash (columna con select: false). |
| `findByIdWithSecret()` | Promise<User \| null> | — |
| `search()` | — | — |
| `countByLevel()` | Promise<Record<AccessLevel, number>> | Conteo de usuarios no desactivados por nivel de acceso. |
| `countActiveMesaDirectiva()` | Promise<number> | Personas activas con nivel Mesa Directiva, excluyendo opcionalmente a una. |
| `create()` | User | — |
| `save()` | Promise<User> | — |
| `recordFailedLogin()` | Promise<void> | — |
| `recordSuccessfulLogin()` | Promise<void> | — |


## Enlaces

- [[M1 - permissions]]
- [[M1 - position]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
