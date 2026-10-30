---
type: central
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/main.ts
  - backendChapterCoreIEEE/src/app.module.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - Backend NestJS

[[CC - Arquitectura y stack]] · [[ChapterCore - Cerebro central]]

> [!abstract] API REST en NestJS 10 con TypeORM; un módulo de Nest por módulo del producto.

## Arranque (`main.ts`)

- `helmet()` para cabeceras de seguridad.
- CORS con credenciales: orígenes de `CORS_ORIGIN` (por defecto `http://localhost:5173`) más `https://frontend-chapter-core-ieee.vercel.app`.
- `ValidationPipe` global con `whitelist`, `transform` y `forbidNonWhitelisted`.
- Puerto `PORT` (por defecto 3000). Sin prefijo global de rutas.

## Composición (`app.module.ts`)

- `ConfigModule` global; lee `.env.local` (raíz) y `.env` del backend.
- TypeORM asíncrono: `autoLoadEntities`, `synchronize: false`, migraciones en `src/database/migrations`, logging solo en desarrollo.
- Módulos: `AuthModule`, `ContactsModule`, `DashboardModule`, `DifusionModule`, `FormsModule`, `OpportunitiesModule`.
- `AppController`: `GET /` público que responde `Hello World!` (comprobación de vida).

## Enlaces

- [[CC - Arquitectura y stack]]
- [[Cerebro 1 - Base institucional]]
- [[Cerebro 2 - Contactos]]
- [[Cerebro 3 - Oportunidades IEEE]]
- [[Cerebro 4 - Difusión y QR]]
- [[Cerebro 5 - Secretaría y formularios]]
- [[Cerebro 6 - Feedback y KPIs]]
