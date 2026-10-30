---
type: central
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/auth/guards/permissions.guard.ts
  - backendChapterCoreIEEE/src/auth/domain/permissions.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - Autorización por permisos

[[CC - Seguridad transversal]] · [[ChapterCore - Cerebro central]]

> [!abstract] Un guard global compara el nivel de la persona con el permiso que exige cada endpoint.

| Función | Mesa Directiva | Secretaría | Director de capítulo | Miembro |
|---|---|---|---|---|
| Contactos | Total | Editar | Ver | Ninguno |
| Oportunidades | Total | Editar | Editar | Ver |
| Difusión | Total | Ver | Editar | Ninguno |
| Formularios | Total | Total | Editar | Responder |
| Dashboard | Total | Ver | Ver (su capítulo) | Ninguno |
| Usuarios | Total | Ninguno | Ninguno | Ninguno |

Sin permiso: `403 Tu cargo no tiene permiso para realizar esta acción.`

## Enlaces

- [[CC - Seguridad transversal]]
- [[Cerebro 1 - Base institucional]]
- [[Cerebro 2 - Contactos]]
- [[Cerebro 3 - Oportunidades IEEE]]
- [[Cerebro 4 - Difusión y QR]]
- [[Cerebro 5 - Secretaría y formularios]]
- [[Cerebro 6 - Feedback y KPIs]]
