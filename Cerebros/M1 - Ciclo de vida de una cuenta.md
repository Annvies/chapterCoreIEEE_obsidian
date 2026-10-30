---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/auth/services/users.service.ts
  - backendChapterCoreIEEE/src/auth/services/auth.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Ciclo de vida de una cuenta

[[M1 - Identidad y acceso]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué es
> Una cuenta pasa por tres estados: `invited` (invitada), `active` (activa) y `disabled` (desactivada). Solo la Mesa Directiva cambia el estado.

> [!info] Confirmado en el código
> - La Mesa Directiva invita con correo, nombre, cargo, ámbito y capítulo. El n.º IEEE no lo escribe la Mesa: si lo envía, se ignora.
> - Las invitaciones nuevas nacen con `pending_approval = true`.
> - Al activar el enlace de invitación, la persona escribe su n.º IEEE (obligatorio) y su contraseña; la cuenta pasa a `active`, pero no puede entrar hasta que la Mesa la acepte ([[M1 - Aprobación de invitaciones]]).
> - Desactivar incrementa `token_version` y borra los enlaces pendientes: cierra todas las sesiones.
> - Al reactivar, vuelve a `active` si ya tenía contraseña, o a `invited` si nunca la definió.

> [!tip] Primera cuenta
> La primera cuenta (Presidencia de la Rama) se crea con `npm run seed:admin`, que imprime su enlace de activación (`database/seeds/create-admin.ts`).

## Enlaces

- Forma parte de [[M1 - Identidad y acceso]].
- Relacionada con [[M1 - Enlaces de un solo uso]], [[M1 - Contraseñas y bloqueo de sesión]], [[M1 - Modelo de datos users y auth_tokens]].

## Fuentes

- `backendChapterCoreIEEE/src/auth/services/users.service.ts`
- `backendChapterCoreIEEE/src/auth/services/auth.service.ts`
