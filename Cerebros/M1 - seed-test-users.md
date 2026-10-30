---
type: seed
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/seeds/seed-test-users.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - seed
---

# M1 - seed-test-users

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Seed
> Crea (o actualiza) una cuenta de prueba por cada nivel de acceso, más una cuenta desactivada para comprobar el rechazo del login. Es idempotente. TEST_USERS_PASSWORD=<contraseña> npm run seed:test-users npm run seed:test-users -- --remove      # borra las cuentas de prueba La contraseña nunca se guarda en el repositorio: se lee de TEST_USERS_PASSWORD (en local, desde backendChapterCoreIEEE/.env; en CI, desde un secreto). Usa la misma conexión que las migraciones (DATABASE_URL_UNPOOLED / DATABASE_URL / DB_*).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `TEST_ACCOUNTS` | const | — |


## Enlaces

- [[M1 - password-policy]]
- [[M1 - position]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
