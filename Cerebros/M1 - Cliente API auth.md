---
type: cliente API
modulo: 1
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/api/auth.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - cliente-API
---

# M1 - Cliente API auth

[[M1 - Interfaz]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Cliente API
> Cliente api del frontend (`frontendChapterCoreIEEE/src/api/auth.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `login` | function | — |
| `fetchProfile` | function | — |
| `updateMyIeeeProfile` | function | — |
| `inspectAccessLink` | function | — |
| `setPasswordWithLink` | function | El número IEEE solo se envía al activar una invitación (es obligatorio en ese caso). |
| `fetchPermissionMatrix` | function | — |
| `fetchChapters` | function | — |
| `fetchIeeeSocieties` | function | — |
| `listUsers` | function | — |
| `inviteUser` | function | — |
| `updateUser` | function | — |
| `setUserStatus` | function | — |
| `issueAccessLink` | function | — |
| `verifyUserIeee` | function | — |

### Llamadas a la API

| Función | Método | Ruta |
|---|---|---|
| `login()` | `POST` | `/auth/login` |
| `fetchProfile()` | `GET` | `/auth/me` |
| `updateMyIeeeProfile()` | `PATCH` | `/auth/me/ieee` |
| `inspectAccessLink()` | `POST` | `/auth/links/inspect` |
| `setPasswordWithLink()` | `POST` | `/auth/links/password` |
| `fetchPermissionMatrix()` | `GET` | `/access/matrix` |
| `fetchChapters()` | `GET` | `/access/chapters` |
| `fetchIeeeSocieties()` | `GET` | `/access/societies` |
| `listUsers()` | `GET` | `/users` |
| `inviteUser()` | `POST` | `/users/invitations` |
| `updateUser()` | `PATCH` | `/users/:p` |
| `setUserStatus()` | `PATCH` | `/users/:p/status` |
| `issueAccessLink()` | `POST` | `/users/:p/access-link` |
| `verifyUserIeee()` | `POST` | `/users/:p/ieee/verify` |


## Enlaces

- [[M1 - Tipos auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
