---
type: guard
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/guards/jwt-auth.guard.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - guard
---

# M1 - jwt-auth.guard

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Guard
> Archivo de guard del backend (`auth/guards/jwt-auth.guard.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `JwtAuthGuard` | class | Guard global: exige un Bearer JWT válido salvo en rutas marcadas con @Public(). |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `canActivate()` | Promise<boolean> | — |


## Enlaces

- [[M1 - authenticated-user]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
