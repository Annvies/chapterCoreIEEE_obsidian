---
type: migración
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792713600000-AddIeeeMembershipToUsers.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - migración
---

# M1 - Migración AddIeeeMembershipToUsers

[[M1 - Base de datos]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Migración
> Módulo 1: perfil IEEE de cada persona (specs/002-m1-perfil-ieee). El estado de la membresía no se guarda: se calcula con el número, el vencimiento y la verificación. Depende de users (CreateAuthModule) y de ieee_societies (CreateOpportunities).

| Campo | Valor |
|---|---|
| Archivo | `1792713600000-AddIeeeMembershipToUsers.ts` |
| Marca de tiempo | `1792713600000` (orden de ejecución) |
| Reversible | sí, tiene `down()` |

### Qué hace

- Crea la tabla `user_ieee_societies`
- Modifica `users`: ADD column `ieee_membership_grade`
- Índice `user_ieee_societies_society_id_idx` en `user_ieee_societies`

## Enlaces

- [[M1 - Tabla user_ieee_societies]]
- [[M1 - Tabla users]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
