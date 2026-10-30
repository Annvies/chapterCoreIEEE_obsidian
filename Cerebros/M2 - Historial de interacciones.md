---
type: concepto
modulo: 2
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792627200000-CreateContactsModule.ts
  - CONTEXTO.md
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-2
  - concepto
---

# M2 - Historial de interacciones

[[M2 - Seguimiento]] · [[Cerebro 2 - Contactos]]

> [!abstract] Qué es
> Tabla `contact_interactions`: registro fechado de cada contacto con la persona u organización.

> [!info] Confirmado en el código
> - Tipos: `llamada`, `correo`, `reunion`, `evento` y `nota`.
> - Descripción obligatoria (1–1000) y fecha.
> - Si se elimina el contacto, se elimina su historial (`ON DELETE CASCADE`).
> - «Enviar correo» abre `mailto:` y ofrece registrarlo en el historial.

## Enlaces

- Forma parte de [[M2 - Seguimiento]].

## Fuentes

- `backendChapterCoreIEEE/src/database/migrations/1792627200000-CreateContactsModule.ts`
- `CONTEXTO.md`
