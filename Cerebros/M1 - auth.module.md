---
type: módulo Nest
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/auth.module.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - módulo-Nest
---

# M1 - auth.module

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Módulo Nest
> Módulo 1 · Autenticación y control de acceso. Capas: controllers -> services -> repositories -> entities; reglas puras en domain/.

### Importa

- `TypeOrmModule`
- `User`
- `AuthToken`
- `IeeeSociety`
- `JwtModule`
- `ConfigService`
- `HS256`

### Controladores

- `AuthController`
- `UsersController`
- `AccessController`

### Proveedores

- `UsersRepository`
- `AuthTokensRepository`
- `ChaptersRepository`
- `PasswordHasherService`
- `AccessTokenService`
- `AuthService`
- `UsersService`
- `AccessService`
- `El`
- `APP_GUARD`
- `JwtAuthGuard`
- `PermissionsGuard`

### Exporta

- `ChaptersRepository`


## Enlaces

- [[M1 - users.repository]]
- [[M1 - auth-tokens.repository]]
- [[M1 - chapters.repository]]
- [[M1 - password-hasher.service]]
- [[M1 - access-token.service]]
- [[M1 - auth.service]]
- [[M1 - users.service]]
- [[M1 - access.service]]
- [[M1 - jwt-auth.guard]]
- [[M1 - permissions.guard]]
- [[M1 - POST auth › login]]
- [[M1 - GET auth › me]]
- [[M1 - PATCH auth › me › ieee]]
- [[M1 - POST auth › links › inspect]]
- [[M1 - POST auth › links › password]]
- [[M1 - GET users]]
- [[M1 - POST users › invitations]]
- [[M1 - GET users › {id}]]
- [[M1 - PATCH users › {id}]]
- [[M1 - PATCH users › {id} › status]]
- [[M1 - POST users › {id} › ieee › verify]]
- [[M1 - POST users › {id} › access-link]]
- [[M1 - GET access › matrix]]
- [[M1 - GET access › chapters]]
- [[M1 - GET access › societies]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
