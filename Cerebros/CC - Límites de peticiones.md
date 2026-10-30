---
type: central
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/opportunities/opportunities.module.ts
  - backendChapterCoreIEEE/src/difusion/difusion.module.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - Límites de peticiones

[[CC - Seguridad transversal]] · [[ChapterCore - Cerebro central]]

> [!abstract] `@nestjs/throttler` limita peticiones por minuto en los módulos expuestos a abuso.

| Módulo | Límite general | Límites propios |
|---|---|---|
| Oportunidades | 30/min | extraer 5/min, publicar 10/min; búsqueda en fuentes oficiales 3/min **por persona** (`OPPORTUNITY_DISCOVERY_RATE_LIMIT`) |
| Difusión | 60/min | crear enlace 20/min, redirección pública 120/min |
| Autenticación | — | 5 intentos fallidos bloquean 15 min (por cuenta) |

> [!warning] Límite en memoria
> El almacenamiento del throttler es en memoria: no se comparte entre instancias.

## Enlaces

- [[CC - Seguridad transversal]]
- [[Cerebro 1 - Base institucional]]
- [[Cerebro 3 - Oportunidades IEEE]]
- [[Cerebro 4 - Difusión y QR]]
