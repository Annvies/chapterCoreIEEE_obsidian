---
type: endpoint
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/difusion/redirect.controller.ts
actualizado: 2026-10-30
aliases:
  - "GET /r/:codigo"
tags:
  - chaptercore
  - modulo-4
  - endpoint
---

# M4 - GET r › {codigo}

[[M4 - API]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Endpoint
> Límite holgado: en un evento muchas personas escanean desde la misma red (misma IP).

| Campo | Valor |
|---|---|
| Método | `GET` |
| Ruta | `/r/:codigo` |
| Acceso | Público (sin sesión) |
| Controlador | `backendChapterCoreIEEE/src/difusion/redirect.controller.ts` → `redirect()` |
| Límite | 120 peticiones por 60 s |
| Devuelve | `Promise<void>` |

### Entradas

- Parámetro de ruta `codigo`
- Query `o` → `string | undefined`

### Lógica que invoca

- `DifusionService.resolve()`

> [!note] Comentario del controlador
> Ruta pública que abre quien escanea el QR o pulsa la URL corta (como /:code en MichiCode).

> [!question] Sin llamada directa en el frontend
> No se encontró una llamada a esta ruta en `frontendChapterCoreIEEE/src`. Puede usarse con una
> URL que devuelve el servidor, desde fuera de la app (p. ej. un QR) o no usarse todavía.

## Enlaces

- [[M4 - difusion.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
