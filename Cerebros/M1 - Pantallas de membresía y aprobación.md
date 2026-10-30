---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - frontendChapterCoreIEEE/src/features/profile/ProfilePage.tsx
  - frontendChapterCoreIEEE/src/features/auth/ActivateAccountPage.tsx
  - frontendChapterCoreIEEE/src/features/access/PendingRequestsPanel.tsx
  - frontendChapterCoreIEEE/src/features/access/UserDialog.tsx
  - frontendChapterCoreIEEE/src/features/access/UsersPanel.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Pantallas de membresía y aprobación

[[M1 - Identidad y acceso]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué es
> Las piezas de la interfaz React que muestran y editan el perfil IEEE y permiten a la
> Mesa Directiva aceptar o rechazar solicitudes.

> [!info] Componentes
> | Componente | Ruta / ubicación | Quién lo ve | Qué hace |
> |---|---|---|---|
> | `ProfilePage` | `/perfil` (enlace «Mi perfil» en la barra) | Toda persona con sesión | Edita número, tipo, vencimiento y sociedades; muestra la insignia de estado |
> | `ActivateAccountPage` | `/activar` | Quien tiene el enlace | En invitaciones pide el **n.º de membresía IEEE**; si queda pendiente muestra «Solicitud enviada» |
> | `PendingRequestsPanel` | Arriba de «Roles y permisos» | Mesa Directiva | Lista solicitudes con su número, enlace a vTools, **Aceptar** y **Rechazar** (con confirmación); se oculta si no hay |
> | `UserDialog` | Diálogo «Editar acceso» | Mesa Directiva | Sección «Perfil IEEE», número en solo lectura y botón «Aceptar solicitud» / «Marcar como verificado» |
> | `UsersPanel` | Lista de usuarios | Mesa Directiva | Insignia «Por aprobar» en cuentas pendientes |
> | `lib/ieee.ts` | Utilidades | — | Etiquetas de grado y estado, y fechas `aaaa-mm-dd` sin corrimiento de zona |

> [!success] Probado
> - Pruebas automáticas: `ProfilePage.test.tsx`, `PendingRequestsPanel.test.tsx` y los
>   casos de activación en `auth-flow.test.tsx` (frontend 62/62 el 2026-10-30).
> - El diálogo de invitar **ya no pide** el número: lo registra solo la persona.

## Enlaces

- Notas técnicas: [[M1 - ProfilePage]], [[M1 - ActivateAccountPage]], [[M1 - PendingRequestsPanel]],
  [[M1 - UserDialog]], [[M1 - UsersPanel]], [[M1 - RolesPage]], [[M1 - lib ieee]].
- Pruebas: [[M1 - Prueba ProfilePage.test]], [[M1 - Prueba PendingRequestsPanel.test]],
  [[M1 - Prueba auth-flow.test]].
- Grupo técnico: [[M1 - Interfaz]] · Diseño: [[CC - Diseño e interfaz]].

## Fuentes

- `frontendChapterCoreIEEE/src/features/profile/ProfilePage.tsx`
- `frontendChapterCoreIEEE/src/features/auth/ActivateAccountPage.tsx`
- `frontendChapterCoreIEEE/src/features/access/PendingRequestsPanel.tsx`
- `frontendChapterCoreIEEE/src/features/access/UserDialog.tsx`, `UsersPanel.tsx`, `RolesPage.tsx`
- `frontendChapterCoreIEEE/src/components/AppShell.tsx`, `frontendChapterCoreIEEE/src/App.tsx`
