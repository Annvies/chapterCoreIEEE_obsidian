---
type: servicio
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/services/password-hasher.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - servicio
---

# M1 - password-hasher.service

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Servicio
> bcryptjs (JS puro) en lugar de bcrypt nativo: funciona en Vercel sin binarios.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `PasswordHasherService` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `hash()` | Promise<string> | — |
| `verify()` | Promise<boolean> | — |
| `verifyAgainstDummy()` | Promise<void> | Compara contra un hash ficticio para que el tiempo de respuesta no revele si el correo existe. |


## Enlaces

- [[Cerebro 1 - Base institucional]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
