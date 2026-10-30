---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/auth/services/auth.service.ts
  - backendChapterCoreIEEE/src/auth/services/users.service.ts
  - backendChapterCoreIEEE/src/auth/repositories/users.repository.ts
  - frontendChapterCoreIEEE/src/features/access/PendingRequestsPanel.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Aprobación de invitaciones

[[M1 - Identidad y acceso]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué es
> Las invitaciones nuevas quedan **pendientes de aprobación** (`users.pending_approval`).
> La persona activa su cuenta con su número IEEE, pero no puede iniciar sesión hasta
> que la Mesa Directiva verifique el número y la acepte.

> [!info] Reglas (confirmado en el código)
> - Invitar crea la cuenta con `pending_approval = true` y **sin número IEEE**: la Mesa
>   no lo escribe; si lo envía, se ignora (`users.service.ts`, `invite`).
> - Activar una invitación **exige** el número (6 a 12 dígitos). Si la cuenta está
>   pendiente, responde `{ pendingApproval: true }` y no abre sesión (`auth.service.ts`).
> - Login, activación y cada petición rechazan las cuentas pendientes. El aviso de
>   «pendiente» (403) solo aparece si la contraseña es correcta, para no revelar el
>   estado de la cuenta.
> - Restablecer la contraseña no pide el número.
> - Las cuentas pendientes **no cuentan** como Mesa Directiva activa
>   ([[M1 - Protección de la Mesa Directiva]]).
> - Las cuentas existentes y las de prueba no se ven afectadas: la columna tiene
>   `DEFAULT false` y el seed fija `pendingApproval: false`.

> [!success] Flujo completo
> 1. La Mesa invita (Roles y permisos → Invitar usuario) y comparte el enlace.
> 2. La persona abre `/activar`, escribe su **n.º de membresía IEEE** y su contraseña,
>    y ve «Solicitud enviada».
> 3. La solicitud aparece en **«Solicitudes pendientes»** (`GET /users?pending=true`).
> 4. La Mesa comprueba el número en vTools y pulsa **Aceptar**
>    (`POST /users/:id/ieee/verify`: verifica y acepta) o **Rechazar** (desactiva la
>    cuenta, con confirmación).
> 5. Una vez aceptada, la persona inicia sesión con normalidad.

> [!example] Verificado de punta a punta (2026-10-30)
> Contra PostgreSQL local: invitar un Gmail, activar sin número (400), activar con
> número (pendiente, sin sesión), login pendiente (403), aceptar, login (200) y
> rechazar (401 al entrar). Detalle en [[2026-10-30 - Cerebros M1 y M2 membresía IEEE]].

## Enlaces

- Código: [[M1 - PendingRequestsPanel]], [[M1 - ActivateAccountPage]], [[M1 - UserDialog]],
  [[M1 - POST users › {id} › ieee › verify]], [[M1 - POST auth › links › password]],
  [[M1 - GET users]], [[M1 - auth.service]], [[M1 - users.repository]].
- Pruebas: [[M1 - Prueba auth.service.spec]], [[M1 - Prueba PendingRequestsPanel.test]],
  [[M1 - Prueba auth-flow.test]].
- Modifica [[M1 - Ciclo de vida de una cuenta]] y usa [[M1 - Verificación manual en vTools]].

## Fuentes

- `backendChapterCoreIEEE/src/auth/services/auth.service.ts`
- `backendChapterCoreIEEE/src/auth/services/users.service.ts`
- `backendChapterCoreIEEE/src/auth/repositories/users.repository.ts`
- `frontendChapterCoreIEEE/src/features/access/PendingRequestsPanel.tsx`
- `specs/002-m1-perfil-ieee/spec.md` (RF-IEEE-08, RF-IEEE-09)
