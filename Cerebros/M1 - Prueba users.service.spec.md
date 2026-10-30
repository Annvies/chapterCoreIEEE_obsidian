---
type: prueba
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/services/users.service.spec.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - prueba
---

# M1 - Prueba users.service.spec

[[M1 - Pruebas]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Prueba
> 10 casos de prueba (Jest).

### Casos

- **UsersService.invite**
  - crea la cuenta invitada y devuelve un enlace de un solo uso
  - rechaza correos repetidos
  - exige capítulo para cargos de capítulo
- **UsersService: protección del acceso administrativo**
  - impide que alguien se quite su propio nivel de Mesa Directiva
  - impide degradar a la última persona activa de la Mesa Directiva
  - impide desactivar la propia cuenta
  - al desactivar invalida sesiones y enlaces pendientes
  - reactivar a quien nunca definió contraseña lo deja como invitado
- **UsersService.issueAccessLink**
  - genera invitación para cuentas invitadas y restablecimiento para activas
  - no genera enlaces para cuentas desactivadas

## Enlaces

- [[M1 - users.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
