---
type: concepto
modulo: 1
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/auth/services/users.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - concepto
---

# M1 - Protección de la Mesa Directiva

[[M1 - Permisos compartidos]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Qué es
> Reglas que impiden dejar la Rama sin nadie que pueda administrar usuarios.

> [!info] Confirmado en el código
> - Nadie puede desactivar su propia cuenta.
> - Nadie puede quitarse su propio nivel de Mesa Directiva.
> - No se puede desactivar ni cambiar el cargo de la última persona activa de Mesa Directiva.

## Enlaces

- Forma parte de [[M1 - Permisos compartidos]].
- Relacionada con [[M1 - Niveles de acceso]].

## Fuentes

- `backendChapterCoreIEEE/src/auth/services/users.service.ts`
