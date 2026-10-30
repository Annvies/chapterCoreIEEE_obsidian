---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/auth/domain/one-time-token.ts
  - backendChapterCoreIEEE/src/auth/services/auth.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Enlaces de un solo uso

[[M1 - Identidad y acceso]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué es
> Invitaciones y restablecimientos de contraseña usan enlaces de un solo uso. No hay servicio de correo: la Mesa Directiva los comparte manualmente.

> [!info] Confirmado en el código
> - Invitación: válida **7 días**. Restablecimiento: válido **24 horas**.
> - El token son 32 bytes aleatorios; en la base solo se guarda su hash SHA-256.
> - Al usarse, se marca como usado y se borran los demás enlaces pendientes de esa persona.
> - Un enlace vencido, usado o de una cuenta desactivada responde: «El enlace no es válido o ya expiró».

## Enlaces

- Forma parte de [[M1 - Identidad y acceso]].
- Relacionada con [[M1 - Ciclo de vida de una cuenta]], [[M1 - Contraseñas y bloqueo de sesión]], [[M1 - Modelo de datos users y auth_tokens]].

## Fuentes

- `backendChapterCoreIEEE/src/auth/domain/one-time-token.ts`
- `backendChapterCoreIEEE/src/auth/services/auth.service.ts`
