---
type: dominio
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/domain/password-policy.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - dominio
---

# M1 - password-policy

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dominio
> Archivo de dominio del backend (`auth/domain/password-policy.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `PASSWORD_MIN_LENGTH` | const | — |
| `PASSWORD_MAX_BYTES` | const | bcrypt ignora lo que pase de 72 bytes; se rechaza para no truncar en silencio. |
| `PASSWORD_PATTERN` | const | — |
| `PASSWORD_POLICY_MESSAGE` | const | — |
| `isPasswordWithinLimits` | function | — |
| `MAX_FAILED_LOGIN_ATTEMPTS` | const | — |
| `LOCKOUT_MS` | const | — |


## Enlaces

- [[Cerebro 1 - Base institucional]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
