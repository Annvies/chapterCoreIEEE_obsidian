---
type: central
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/package.json
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - Dependencias del backend

[[CC - Arquitectura y stack]] · [[ChapterCore - Cerebro central]]

> [!abstract] Librerías de producción del backend (todas de código abierto).

| Paquete | Uso |
|---|---|
| `@nestjs/common`, `core`, `platform-express` 10 | Framework |
| `@nestjs/config` | Variables de entorno |
| `@nestjs/jwt` | Sesiones JWT |
| `@nestjs/throttler` | Límites de peticiones |
| `@nestjs/typeorm`, `typeorm`, `pg` | Base de datos |
| `bcryptjs` | Hash de contraseñas |
| `class-validator`, `class-transformer` | Validación de DTO |
| `zod` | Validación de esquemas de formularios |
| `exceljs` | Exportación XLSX |
| `multer` | Subida de archivos |
| `helmet` | Cabeceras de seguridad |
| `dotenv`, `reflect-metadata`, `rxjs` | Soporte |

Desarrollo: Jest, Supertest, ts-jest, ESLint, Prettier, TypeScript.

## Enlaces

- [[CC - Arquitectura y stack]]
