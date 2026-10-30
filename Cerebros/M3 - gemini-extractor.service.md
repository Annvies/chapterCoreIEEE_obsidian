---
type: servicio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/gemini-extractor.service.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - servicio
---

# M3 - gemini-extractor.service

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Servicio
> Archivo de servicio del backend (`opportunities/gemini-extractor.service.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `RawExtraction` | interface | Salida cruda del modelo; se normaliza y valida en OpportunitiesService. |
| `parseRawExtraction` | function | — |
| `GeminiExtractorService` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `assertConfigured()` | string | Falla pronto (503) si no hay clave, antes de descargar ninguna página. |
| `extract()` | Promise<RawExtraction> | — |


## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
