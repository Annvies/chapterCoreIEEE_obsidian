---
type: utilidad
modulo: 1
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/lib/session.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - utilidad
---

# M1 - lib session

[[M1 - Interfaz]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Utilidad
> Token de sesión (JWT Bearer). "Recordarme" lo guarda en localStorage; si no, en sessionStorage y se pierde al cerrar la pestaña. Backend y frontend viven en dominios distintos en Vercel, por eso se usa un encabezado y no una cookie.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `getAccessToken` | function | — |
| `storeAccessToken` | function | — |
| `clearAccessToken` | function | — |
| `authorizationHeader` | function | — |
| `notifyUnauthorized` | function | Los clientes HTTP avisan cuando el backend responde 401 con una sesión guardada. |
| `onUnauthorized` | function | — |


## Enlaces

- [[Cerebro 1 - Base institucional]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
