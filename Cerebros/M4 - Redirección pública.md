---
type: concepto
modulo: 4
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/difusion/redirect.controller.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-4
  - concepto
---

# M4 - Redirección pública

[[M4 - Códigos QR]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Qué es
> Ruta pública `/r/<código>` que abre quien escanea el QR o pulsa el enlace.

> [!info] Confirmado en el código
> - Responde con redirección **302** (no 301) y sin caché, para que cada escaneo cuente y siga los cambios de destino.
> - Enlace pausado → **410** «Enlace pausado»; inexistente → **404**.
> - Límite de 120 peticiones por minuto, holgado para eventos con muchas personas en la misma red.
> - Cabeceras de seguridad: CSP cerrada, `nosniff`, `no-referrer`.
> - El origen «QR» se marca con el parámetro `?o=qr`.

## Enlaces

- Forma parte de [[M4 - Códigos QR]].
- Relacionada con [[M4 - Tipos y estilos de QR]].

## Fuentes

- `backendChapterCoreIEEE/src/difusion/redirect.controller.ts`
