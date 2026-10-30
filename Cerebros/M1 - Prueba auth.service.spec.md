---
type: prueba
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/services/auth.service.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - prueba
---

# M1 - Prueba auth.service.spec

[[M1 - Pruebas]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Prueba
> 16 casos de prueba (Jest).

### Casos

- **AuthService.login**
  - abre sesión con credenciales válidas y reinicia los intentos fallidos
  - responde igual si el correo no existe y gasta el mismo tiempo de hash
  - rechaza cuentas %s
  - cuenta los intentos fallidos y bloquea al llegar al máximo
  - no verifica la contraseña mientras la cuenta está bloqueada
  - rechaza cuentas que esperan la aprobación de la Mesa Directiva
  - con contraseña incorrecta no revela que la cuenta está pendiente
- **AuthService.authenticate**
  - invalida tokens emitidos antes de un cambio de contraseña
  - invalida sesiones de cuentas desactivadas
  - invalida sesiones de cuentas pendientes de aprobación
- **AuthService.setPasswordWithLink**
  - activa la invitación, sube la versión del token y marca el enlace como usado
  - exige el número de membresía IEEE al activar una invitación
  - una invitación pendiente de aprobación se activa pero no abre sesión
  - restablecer la contraseña no pide el número IEEE
  - rechaza enlaces vencidos o ya usados
  - rechaza contraseñas débiles antes de tocar la base

## Enlaces

- [[M1 - auth.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
