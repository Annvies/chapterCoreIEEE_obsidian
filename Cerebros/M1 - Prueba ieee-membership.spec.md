---
type: prueba
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/domain/ieee-membership.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - prueba
---

# M1 - Prueba ieee-membership.spec

[[M1 - Pruebas]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Prueba
> 5 casos de prueba (Jest).

### Casos

- **resolveIeeeStatus**
  - sin número de miembro el perfil está sin vincular
  - con número sin verificar queda pendiente
  - verificado y sin vencer está vigente, incluso el mismo día del vencimiento
  - con vencimiento pasado está vencida aunque esté verificada
- **todayIsoDate**
  - formatea la fecha local como aaaa-mm-dd

## Enlaces

- [[M1 - ieee-membership]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
