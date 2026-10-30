---
type: migración
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792800000000-AddPendingApprovalToUsers.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - migración
---

# M1 - Migración AddPendingApprovalToUsers

[[M1 - Base de datos]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Migración
> Módulo 1: las invitaciones nuevas quedan "pendientes de aprobación" hasta que la Mesa Directiva acepta a la persona tras verificar su número IEEE (specs/002-m1-perfil-ieee). DEFAULT false: todas las cuentas existentes siguen entrando como hasta ahora. En PostgreSQL 11+ agregar una columna con DEFAULT constante no reescribe la tabla.

| Campo | Valor |
|---|---|
| Archivo | `1792800000000-AddPendingApprovalToUsers.ts` |
| Marca de tiempo | `1792800000000` (orden de ejecución) |
| Reversible | sí, tiene `down()` |

### Qué hace

- Modifica `users`: ADD column `pending_approval`

## Enlaces

- [[M1 - Tabla users]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
