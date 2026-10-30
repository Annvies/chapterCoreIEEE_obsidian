---
type: central
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/auth/guards/jwt-auth.guard.ts
  - backendChapterCoreIEEE/src/auth/decorators/public.decorator.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - Autenticación JWT global

[[CC - Seguridad transversal]] · [[ChapterCore - Cerebro central]]

> [!abstract] Toda ruta del backend exige un token JWT válido, salvo las marcadas con `@Public()`.

- Rutas públicas: `POST /auth/login`, `POST /auth/links/inspect`, `POST /auth/links/password`, `GET /public/forms/:slug`, `POST /public/forms/:slug/submissions`, `GET /r/:codigo` y `GET /`.
- El token lleva `sub` (usuario) y `tv` (`token_version`): cambiar la contraseña o desactivar la cuenta invalida todas las sesiones.
- Detalle en [[Cerebro 1 - Base institucional]].

## Enlaces

- [[CC - Seguridad transversal]]
- [[Cerebro 1 - Base institucional]]
