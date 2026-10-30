---
type: guard
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/guards/permissions.guard.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - guard
---

# M1 - permissions.guard

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Guard
> Guard global que aplica @RequirePermission. Corre después del JwtAuthGuard.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `PermissionsGuard` | class | Guard global que aplica @RequirePermission. Corre después del JwtAuthGuard. |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `canActivate()` | boolean | — |


## Enlaces

- [[M1 - authenticated-user]]
- [[M1 - permissions]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
