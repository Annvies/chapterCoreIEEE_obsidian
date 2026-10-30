---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - CONTEXTO.md
  - frontendChapterCoreIEEE/src/features/access/PendingRequestsPanel.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Verificación manual en vTools

[[M1 - Identidad y acceso]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué es
> La forma, sin costo, de comprobar que un número de miembro IEEE es real: un directivo
> lo revisa en el **Membership Validator de vTools** y luego lo marca en ChapterCore.

> [!info] Por qué es manual (hecho verificado el 2026-10-19, `CONTEXTO.md`)
> - IEEE **no ofrece** inicio de sesión OAuth/SSO para aplicaciones externas.
> - Su API de validación de membresía solo se concede a grandes conferencias aprobadas.
> - Por eso ChapterCore no consulta a IEEE: que dos números coincidan no prueba que la
>   membresía sea válida; solo la revisión en vTools lo confirma.

> [!success] Cómo se hace en la aplicación
> - El panel «Solicitudes pendientes» enlaza a `https://vtools.ieee.org/membership-validator/`
>   y muestra el número de cada persona.
> - Al aceptar se guardan la fecha (`ieee_verified_at`) y el autor (`ieee_verified_by`).
> - Desde «Editar acceso» la Mesa también puede volver a verificar un perfil que
>   quedó pendiente porque la persona cambió sus datos.

> [!warning] Límite conocido
> La verificación depende de que un directivo revise a tiempo. Una persona invitada
> no entra hasta entonces ([[M1 - Aprobación de invitaciones]]).

## Enlaces

- Lo usan [[M1 - Aprobación de invitaciones]] y [[M1 - Estado de la membresía IEEE]].
- Código: [[M1 - PendingRequestsPanel]], [[M1 - UserDialog]], [[M1 - POST users › {id} › ieee › verify]].

## Fuentes

- `CONTEXTO.md` (decisión sobre la cuenta IEEE del usuario).
- `frontendChapterCoreIEEE/src/features/access/PendingRequestsPanel.tsx`
- `backendChapterCoreIEEE/src/auth/services/users.service.ts` (`verifyIeee`)
