---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/auth/domain/password-policy.ts
  - backendChapterCoreIEEE/src/auth/services/access-token.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Contraseñas y bloqueo de sesión

[[M1 - Identidad y acceso]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué es
> Reglas de contraseña, duración de la sesión y protección contra intentos repetidos.

> [!info] Confirmado en el código
> - Contraseña de **8+ caracteres** con letras y números; máximo 72 bytes (límite de bcrypt).
> - Sesión JWT de **8 horas**, o **30 días** con «recordarme».
> - **5 intentos fallidos** bloquean el inicio de sesión **15 minutos**.
> - El error es el mismo si el correo no existe o la contraseña es incorrecta.

## Enlaces

- Forma parte de [[M1 - Identidad y acceso]].
- Relacionada con [[M1 - Ciclo de vida de una cuenta]], [[M1 - Enlaces de un solo uso]], [[M1 - Modelo de datos users y auth_tokens]].

## Fuentes

- `backendChapterCoreIEEE/src/auth/domain/password-policy.ts`
- `backendChapterCoreIEEE/src/auth/services/access-token.service.ts`
