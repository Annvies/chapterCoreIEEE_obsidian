---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/auth/domain/permissions.ts
  - backendChapterCoreIEEE/src/auth/domain/position.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Niveles de acceso

[[M1 - Permisos compartidos]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué es
> El nivel de acceso se calcula a partir del cargo y su ámbito; no se asigna a mano.

> [!info] Confirmado en el código
> | Cargo | Ámbito | Nivel |
> |---|---|---|
> | Presidente, Vicepresidente, Tesorero, Webmaster | Rama | Mesa Directiva |
> | Secretario | Rama o capítulo | Secretaría |
> | Presidente, Vicepresidente, Tesorero, Webmaster | Capítulo | Director de capítulo |
> | Sin cargo | — | Miembro |

> [!example] Escala de acceso
> `none < respond < view < edit < total`: cada acceso incluye a los anteriores. Un guard global compara el nivel con lo que pide cada operación (`@RequirePermission`).

## Enlaces

- Forma parte de [[M1 - Permisos compartidos]].
- Relacionada con [[M1 - Protección de la Mesa Directiva]].

## Fuentes

- `backendChapterCoreIEEE/src/auth/domain/permissions.ts`
- `backendChapterCoreIEEE/src/auth/domain/position.ts`
