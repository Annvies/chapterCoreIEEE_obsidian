---
type: concepto
modulo: 4
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792540800000-CreateDifusionModule.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-4
  - concepto
---

# M4 - Modelo short_links y link_visits

[[M4 - Enlaces cortos]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Qué es
> Dos tablas: los enlaces cortos y el registro de visitas.

> [!info] Confirmado en el código
> - `short_links`: código único, nombre (1–120), `destino_url` (http/https, máx. 2048), tipo, estado y estilo.
> - `link_visits`: registro solo de inserción con fecha, origen (`qr` o `enlace`) y si fue desde móvil.
> - **No se guarda IP ni user-agent** de quien visita.

## Enlaces

- Forma parte de [[M4 - Enlaces cortos]].
- Relacionada con [[M4 - Códigos y alias]], [[M4 - Validación de destinos]].

## Fuentes

- `backendChapterCoreIEEE/src/database/migrations/1792540800000-CreateDifusionModule.ts`
