---
type: servicio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/page-fetcher.service.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - servicio
---

# M3 - page-fetcher.service

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Servicio
> Archivo de servicio del backend (`opportunities/page-fetcher.service.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `FetchedPage` | interface | — |
| `FetchPageOptions` | interface | — |
| `USER_AGENT` | const | Agente propio: los sitios de IEEE pueden identificarlo y aplicarle sus reglas de robots.txt. |
| `isPrivateAddress` | function | — |
| `htmlToText` | function | Convierte HTML en texto legible; descarta scripts, estilos y comentarios. Tiempo lineal. |
| `extractTitle` | function | — |
| `extractOfficialLinks` | function | — |
| `HostRejectedException` | class | Descarga una página oficial IEEE con protección SSRF: solo https, solo dominios de la allowlist (también en cada redirección), sin IPs privadas, tamaño y tiempo acotados. El sitio rechazó la descarga automática: 403, 429 o desafío del cortafuegos de AWS (spec 002, RF-358). Lleva el host para no volver a pedirle páginas; nunca se evade. |
| `PageFetcherService` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `assertPublicHost()` | Promise<void> | Rechaza hosts que resuelven a direcciones no públicas. |
| `fetchPage()` | Promise<FetchedPage> | — |


## Enlaces

- [[M3 - official-sources]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
