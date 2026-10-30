---
type: servicio
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/services/users.service.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - servicio
---

# M1 - users.service

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Servicio
> Archivo de servicio del backend (`auth/services/users.service.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `AccessLinkView` | interface | — |
| `UserListView` | interface | — |
| `UsersService` | class | Administración de usuarios (solo Mesa Directiva, según la matriz). |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `list()` | Promise<UserListView> | — |
| `findOne()` | Promise<UserView> | — |
| `invite()` | — | — |
| `update()` | Promise<UserView> | — |
| `setStatus()` | — | — |
| `issueAccessLink()` | Promise<AccessLinkView> | Genera un enlace de invitación (si no activó su cuenta) o de restablecimiento. |
| `updateIeeeProfile()` | Promise<UserView> | La propia persona edita su perfil IEEE (RF-IEEE-01). Los campos omitidos no cambian. |
| `verifyIeee()` | Promise<UserView> | Un directivo confirma el número tras revisarlo en el Membership Validator de vTools. Si la cuenta esperaba aprobación, también la acepta. |


## Enlaces

- [[M1 - authenticated-user]]
- [[M1 - one-time-token]]
- [[M1 - permissions]]
- [[M1 - position]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
