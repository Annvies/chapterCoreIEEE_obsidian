---
type: central
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/config/jwt.config.ts
  - backendChapterCoreIEEE/src/config/database.config.ts
  - backendChapterCoreIEEE/src/main.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - Variables de entorno

[[CC - Arquitectura y stack]] · [[ChapterCore - Cerebro central]]

> [!abstract] Nombres de las variables que lee el código. **Nunca** se documentan sus valores.

| Variable | Dónde | Para qué |
|---|---|---|
| `PORT`, `NODE_ENV` | Backend | Puerto y entorno |
| `CORS_ORIGIN` | Backend | Orígenes permitidos (separados por coma) |
| `JWT_SECRET` | Backend | Firma de sesiones; obligatoria en producción (≥ 32 caracteres); en desarrollo se genera una temporal |
| `DATABASE_URL`, `DATABASE_URL_UNPOOLED`, `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`, `DB_SSL` | Backend | Conexión a PostgreSQL |
| `GEMINI_API_KEY`, `GEMINI_MODEL` | Backend | Extracción de oportunidades |
| `MAX_UPLOAD_MB`, `UPLOAD_DIR` | Backend | Adjuntos de formularios |
| `TEST_USERS_PASSWORD` | Backend | Seed de usuarios de prueba |
| `VITE_API_URL` | Frontend | URL del backend |

> [!warning] Secretos
> Los valores reales viven solo en `.env` (no versionado) y en los secretos de GitHub/Vercel.

## Enlaces

- [[CC - Arquitectura y stack]]
- [[Cerebro 1 - Base institucional]]
- [[Cerebro 3 - Oportunidades IEEE]]
- [[Cerebro 5 - Secretaría y formularios]]
