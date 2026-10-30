---
type: prueba
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/difusion/short-links.util.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - prueba
---

# M4 - Prueba short-links.util.spec

[[M4 - Pruebas]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Prueba
> 10 casos de prueba (Jest).

### Casos

- **generateShortCode**
  - genera códigos de 6 caracteres en minúsculas y dígitos
  - no repite códigos en una muestra pequeña
- **isRedirectableUrl**
  - acepta %s
- **normalizeUrl**
  - pone esquema y host en minúsculas y deja igual lo que no es URL
- **isAutomatedRequest**
  - reconoce previsualizadores de chats y precargas
  - no descarta navegadores normales
- **pointsToShortener**
  - detecta destinos que son otra URL corta
  - no se deja engañar por mayúsculas ni por el punto final del host
  - permite otras rutas del mismo host y otros hosts
- **isMobileUserAgent**
  - reconoce móviles comunes y no confunde escritorio

## Enlaces

- [[M4 - short-links.util]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
