---
type: central
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/
  - backendChapterCoreIEEE/src/config/database.config.ts
  - CONTEXTO.md
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - Base de datos PostgreSQL

[[CC - Arquitectura y stack]] · [[ChapterCore - Cerebro central]]

> [!abstract] Una sola base PostgreSQL compartida por los seis módulos, gestionada con migraciones TypeORM.

## Migraciones (en orden)

| Migración | Crea |
|---|---|
| `1730000000000-CreateFormsModule` | `forms`, `form_versions`, `form_submissions`, `form_uploads` |
| `1792368000000-CreateOpportunities` | `ieee_societies` (con carga inicial), `opportunities` y enums de tipo y estado |
| `1792454400000-CreateAuthModule` | `users`, `auth_tokens` |
| `1792454400000-UniqueOpportunityEnlace` | Unicidad del enlace de oportunidades |
| `1792540800000-CreateDifusionModule` | `short_links`, `link_visits` y enums de enlaces y QR |
| `1792627200000-CreateContactsModule` | `contacts`, `contact_interactions` |

- Extensiones: `pgcrypto` (UUID) y `citext` (correos sin distinguir mayúsculas).
- Conexión: `DATABASE_URL` (o `DATABASE_URL_UNPOOLED` para migraciones) o `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`; `DB_SSL` opcional.
- `synchronize` siempre desactivado: el esquema solo cambia por migraciones.

## Enlaces

- [[CC - Arquitectura y stack]]
- [[Cerebro 1 - Base institucional]]
- [[Cerebro 2 - Contactos]]
- [[Cerebro 3 - Oportunidades IEEE]]
- [[Cerebro 4 - Difusión y QR]]
- [[Cerebro 5 - Secretaría y formularios]]
- [[Cerebro 6 - Feedback y KPIs]]
