---
type: cliente API
modulo: 4
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/api/difusion.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - cliente-API
---

# M4 - Cliente API difusion

[[M4 - Interfaz]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Cliente api
> Único sitio que conoce las rutas de backendChapterCoreIEEE/src/difusion.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `listShortLinks` | function | — |
| `createShortLink` | function | — |
| `updateShortLink` | function | — |
| `getLinkStats` | function | — |

### Llamadas a la API

| Función | Método | Ruta |
|---|---|---|
| `listShortLinks()` | `GET` | `/difusion/enlaces` |
| `createShortLink()` | `POST` | `/difusion/enlaces` |
| `updateShortLink()` | `PATCH` | `/difusion/enlaces/:p` |
| `getLinkStats()` | `GET` | `/difusion/enlaces/:p/estadisticas` |


## Enlaces

- [[M4 - Tipos difusion]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
