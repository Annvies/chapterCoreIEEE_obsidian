---
type: dominio
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/domain/ieee-membership.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - dominio
---

# M1 - ieee-membership

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dominio
> Perfil IEEE autodeclarado (specs/002-m1-perfil-ieee). IEEE no ofrece OAuth ni una API de validación pública: un directivo verifica el número a mano en vTools.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `IeeeGrade` | enum | Perfil IEEE autodeclarado (specs/002-m1-perfil-ieee). IEEE no ofrece OAuth ni una API de validación pública: un directivo verifica el número a mano en vTools. |
| `IEEE_GRADES` | const | — |
| `IeeeStatus` | enum | Se calcula a partir de los datos; nunca se guarda (RF-IEEE-05). |
| `IeeeStatusInput` | interface | — |
| `resolveIeeeStatus` | function | — |
| `todayIsoDate` | function | Fecha de calendario local del servidor como "aaaa-mm-dd". |


## Enlaces

- [[Cerebro 1 - Base institucional]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
