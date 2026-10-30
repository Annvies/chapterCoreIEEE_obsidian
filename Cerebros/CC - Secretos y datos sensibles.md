---
type: central
estado: confirmado
fuentes:
  - CONTEXTO.md
  - backendChapterCoreIEEE/src/config/jwt.config.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - Secretos y datos sensibles

[[CC - Seguridad transversal]] · [[ChapterCore - Cerebro central]]

> [!abstract] Reglas para claves y datos personales.

- `.env` nunca se versiona; `.env.example` solo trae valores de desarrollo.
- Secretos de producción en el entorno `production` de GitHub: `NEON_DATABASE_URL_UNPOOLED`, `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID_BACKEND`, `VERCEL_PROJECT_ID_FRONTEND` (solo nombres).
- Los enlaces de un solo uso se guardan como hash; las contraseñas con bcrypt.
- Las visitas de enlaces no guardan IP ni user-agent.
- Pendiente: política de privacidad, retención y eliminación de datos (contactos, respuestas, adjuntos).

## Enlaces

- [[CC - Seguridad transversal]]
