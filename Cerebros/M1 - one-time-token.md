---
type: dominio
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/domain/one-time-token.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - dominio
---

# M1 - one-time-token

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dominio
> Archivo de dominio del backend (`auth/domain/one-time-token.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `TokenPurpose` | enum | — |
| `TOKEN_TTL_MS` | const | — |
| `generateRawToken` | function | Token aleatorio de un solo uso. Solo su hash se guarda en la base. |
| `hashToken` | function | — |


## Enlaces

- [[Cerebro 1 - Base institucional]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
