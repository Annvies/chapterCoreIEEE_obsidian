---
type: prueba
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/guards/guards.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - prueba
---

# M1 - Prueba guards.spec

[[M1 - Pruebas]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Prueba
> 7 casos de prueba (Jest).

### Casos

- **JwtAuthGuard**
  - deja pasar rutas @Public() sin token
  - exige token en las demás rutas
  - ignora las cabeceras x-user-role del shim anterior
  - pone el usuario vigente en request.user
  - rechaza tokens de cuentas que ya no son válidas
- **PermissionsGuard**
  - permite rutas sin @RequirePermission
  - aplica la matriz de permisos

## Enlaces

- [[Cerebro 1 - Base institucional]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
