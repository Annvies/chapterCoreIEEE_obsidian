---
type: central
estado: confirmado
fuentes:
  - CONTEXTO.md
  - backendChapterCoreIEEE/package.json
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - Entorno de desarrollo local

[[CC - Despliegue e integración continua]] · [[ChapterCore - Cerebro central]]

> [!abstract] Cómo levantar ChapterCore en una computadora.

1. PostgreSQL 18 en Docker: `docker compose --env-file .env.example up -d` desde `backendChapterCoreIEEE/` (contenedor `chaptercore-postgres`, puerto `5434`, base `chaptercore_dev`).
2. `npm run db:setup`: migraciones + usuarios de prueba.
3. `npm run seed:admin -- --email … --name "…"`: crea la Presidencia de la Rama e imprime su enlace de activación.
4. Backend con `npm run start:dev`; frontend con `npm run dev` (puerto 5173).

## Enlaces

- [[CC - Despliegue e integración continua]]
