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
| `GEMINI_API_KEY`, `GEMINI_MODEL` | Backend | Extracción de oportunidades (sin uso desde la interfaz desde el PR #43) |
| `OPPORTUNITY_DISCOVERY_RATE_LIMIT`, `_TIMEOUT_MS`, `_PAGE_TIMEOUT_MS`, `_MAX_PAGES`, `_MIN_RESULTS` | Backend | Límites de la búsqueda en fuentes oficiales |
| `OPPORTUNITY_DISCOVERY_STATIC`, `_PLAYWRIGHT`, `_CATALOG`, `_CATALOG_MAX_AGE_DAYS`, `_FORCE_STRATEGY` | Backend | Qué estrategias de la cascada se usan (el navegador solo con `_PLAYWRIGHT=true`) |
| `MAX_UPLOAD_MB`, `UPLOAD_DIR` | Backend | Adjuntos de formularios |
| `TEST_USERS_PASSWORD` | Backend | Seed de usuarios de prueba |
| `RUN_DB_INTEGRATION` | Backend | Con `1` activa la prueba de integración del historial de búsquedas contra una base real |
| `VITE_API_URL` | Frontend | URL del backend |

> [!warning] Secretos
> Los valores reales viven solo en `.env` (no versionado) y en los secretos de GitHub/Vercel.

## Enlaces

- [[CC - Arquitectura y stack]]
- [[Cerebro 1 - Base institucional]]
- [[Cerebro 3 - Oportunidades IEEE]]
- [[Cerebro 5 - Secretaría y formularios]]
