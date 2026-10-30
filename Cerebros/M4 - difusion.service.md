---
type: servicio
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/difusion/difusion.service.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - servicio
---

# M4 - difusion.service

[[M4 - Lógica del backend]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Servicio
> Archivo de servicio del backend (`difusion/difusion.service.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DEFAULT_STATS_DAYS` | const | — |
| `ResolveResult` | type | — |
| `isValidTimeZone` | function | — |
| `resolveShortBaseUrl` | function | Base pública de las URLs cortas, sin barra final (configurable con SHORT_LINK_BASE_URL). |
| `DifusionService` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `list()` | Promise<ShortLinkView[]> | — |
| `create()` | Promise<ShortLinkView> | — |
| `update()` | Promise<ShortLinkView> | — |
| `stats()` | Promise<LinkStatsView> | — |
| `resolve()` | — | Resuelve una URL corta. Registra la visita solo si el enlace está activo y la petición no es HEAD (previsualizadores de enlaces). Un fallo al registrar no impide redirigir. |


## Enlaces

- [[Cerebro 4 - Difusión y QR]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
