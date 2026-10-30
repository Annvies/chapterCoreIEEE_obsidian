---
type: servicio
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/services/access-token.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - servicio
---

# M1 - access-token.service

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Servicio
> Archivo de servicio del backend (`auth/services/access-token.service.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `AccessTokenPayload` | interface | — |
| `IssuedAccessToken` | interface | — |
| `AccessTokenService` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `issue()` | Promise<IssuedAccessToken> | — |
| `verify()` | Promise<AccessTokenPayload \| null> | — |


## Enlaces

- [[Cerebro 1 - Base institucional]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
