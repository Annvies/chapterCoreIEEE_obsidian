---
type: servicio
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/services/auth.service.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - servicio
---

# M1 - auth.service

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Servicio
> Archivo de servicio del backend (`auth/services/auth.service.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `SessionView` | interface | — |
| `PendingApprovalView` | interface | Respuesta al activar una invitación que todavía debe aceptar la Mesa Directiva. |
| `TokenInfoView` | interface | — |
| `AuthService` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `login()` | Promise<SessionView> | — |
| `authenticate()` | Promise<AuthenticatedUser \| null> | Valida un JWT y devuelve el usuario vigente, o null si la sesión ya no es válida. |
| `profile()` | Promise<ProfileView> | — |
| `inspectLink()` | Promise<TokenInfoView> | — |
| `setPasswordWithLink()` | — | Activa una invitación (exige el número IEEE) o restablece la contraseña y abre sesión. Si la cuenta espera la aprobación de la Mesa Directiva, no abre sesión. |


## Enlaces

- [[M1 - authenticated-user]]
- [[M1 - one-time-token]]
- [[M1 - password-policy]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
