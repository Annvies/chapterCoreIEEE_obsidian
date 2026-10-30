---
type: central
estado: confirmado
fuentes:
  - CONTEXTO.md
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - Producción en Neon y Vercel

[[CC - Despliegue e integración continua]] · [[ChapterCore - Cerebro central]]

> [!abstract] Producción: PostgreSQL administrado en Neon; backend y frontend como proyectos separados en Vercel.

- Las migraciones se aplican en Neon antes de desplegar.
- La integración Git de Vercel debe usar `main` como rama de producción (se configura fuera del repositorio).
- Frontend publicado en `https://frontend-chapter-core-ieee.vercel.app` (origen CORS fijo en `main.ts`).
- No hay promoción automática de `dev` a `main`.

## Enlaces

- [[CC - Despliegue e integración continua]]
