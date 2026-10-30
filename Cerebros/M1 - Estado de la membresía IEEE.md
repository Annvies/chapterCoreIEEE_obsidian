---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/auth/domain/ieee-membership.ts
  - backendChapterCoreIEEE/src/auth/services/users.service.ts
  - frontendChapterCoreIEEE/src/lib/ieee.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Estado de la membresía IEEE

[[M1 - Identidad y acceso]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué es
> Un valor calculado a partir del número, el vencimiento y la verificación, sin
> guardarlo en la base. Así nunca queda «vigente» una membresía con la fecha vencida.

> [!info] Regla de cálculo (`resolveIeeeStatus`)
> 1. Sin número de miembro → **Sin vincular** (`sin_vincular`).
> 2. Con vencimiento anterior a hoy → **Vencida** (`vencida`), aunque esté verificada.
> 3. Verificada por la Mesa Directiva → **Vigente** (`vigente`).
> 4. En otro caso → **Pendiente de verificación** (`pendiente_verificacion`).
>
> «Hoy» es la fecha local del servidor (`todayIsoDate`). El mismo día del vencimiento
> todavía cuenta como vigente.

> [!success] Cuándo se pierde la verificación
> - Cambiar el **número**, el **tipo** o el **vencimiento** borra `ieee_verified_at` y
>   `ieee_verified_by`, y el estado vuelve a «Pendiente».
> - Cambiar solo las **sociedades** conserva la verificación.
> - Perder la verificación **no bloquea** la cuenta: la persona sigue entrando
>   (el bloqueo es solo para invitaciones nuevas, ver [[M1 - Aprobación de invitaciones]]).

> [!example] Insignias en la interfaz (`lib/ieee.ts`)
> | Estado | Etiqueta | Insignia |
> |---|---|---|
> | `sin_vincular` | Sin vincular | `cc-badge--draft` |
> | `pendiente_verificacion` | Pendiente de verificación | `cc-badge--received` |
> | `vigente` | Vigente | `cc-badge--accepted` |
> | `vencida` | Vencida | `cc-badge--rejected` |

## Enlaces

- Concepto padre: [[M1 - Perfil de membresía IEEE]].
- Código: [[M1 - ieee-membership]], [[M1 - users.service]], [[M1 - lib ieee]],
  [[M1 - Prueba ieee-membership.spec]].

## Fuentes

- `backendChapterCoreIEEE/src/auth/domain/ieee-membership.ts`
- `backendChapterCoreIEEE/src/auth/services/users.service.ts` (`updateIeeeProfile`, `verifyIeee`)
- `frontendChapterCoreIEEE/src/lib/ieee.ts`
