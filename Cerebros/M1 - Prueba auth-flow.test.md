---
type: prueba
modulo: 1
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/auth/auth-flow.test.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - prueba
---

# M1 - Prueba auth-flow.test

[[M1 - Pruebas]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Prueba
> 11 casos de prueba (Vitest + Testing Library).

### Casos

- **Login**
  - manda al login a quien no tiene sesión
  - no muestra el botón de IEEE Account
  - inicia sesión, guarda el token y vuelve a la página pedida
  - muestra el mensaje del backend si las credenciales son incorrectas
- **Guards de rutas**
  - recupera la sesión guardada y bloquea secciones sin permiso
  - descarta un token vencido y vuelve al login
- **Activación de cuenta**
  - avisa si el enlace no trae token
  - valida el enlace y define la contraseña
  - exige el número IEEE y, si la cuenta espera aprobación, no abre sesión
  - restablecer la contraseña no pide el número IEEE
- **can()**
  - aplica el orden de permisos de la matriz

## Enlaces

- [[Cerebro 1 - Base institucional]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
