---
type: central
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/main.ts
  - backendChapterCoreIEEE/src/difusion/redirect.controller.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - Endurecimiento HTTP

[[CC - Seguridad transversal]] · [[ChapterCore - Cerebro central]]

> [!abstract] Defensas a nivel de protocolo HTTP.

- `helmet()` en todas las respuestas.
- CORS limitado a orígenes conocidos, con credenciales.
- `ValidationPipe`: descarta campos no declarados y **rechaza** peticiones con campos extra (`forbidNonWhitelisted`).
- La redirección pública `/r/:codigo` añade CSP cerrada, `nosniff`, `no-referrer` y `Cache-Control: no-store`.

## Enlaces

- [[CC - Seguridad transversal]]
- [[Cerebro 4 - Difusión y QR]]
