---
type: concepto
modulo: 4
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/difusion/short-links.util.ts
  - backendChapterCoreIEEE/src/difusion/redirect.controller.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-4
  - concepto
---

# M4 - Filtro de bots y precargas

[[M4 - Métricas de difusión]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Qué es
> Qué peticiones no cuentan como visita.

> [!info] Confirmado en el código
> - Previsualizadores de chats y rastreadores (WhatsApp, Telegram, Slack, Discord, LinkedIn, bots y crawlers).
> - Precargas del navegador (`prefetch`, `prerender`) y peticiones `HEAD`.
> - Móvil se detecta por el user-agent en el momento, sin guardarlo.

> [!warning] Señal, no certeza
> Un bot desconocido puede contarse, y `?o=qr` puede añadirse a mano: las cifras son orientativas.

## Enlaces

- Forma parte de [[M4 - Métricas de difusión]].

## Fuentes

- `backendChapterCoreIEEE/src/difusion/short-links.util.ts`
- `backendChapterCoreIEEE/src/difusion/redirect.controller.ts`
