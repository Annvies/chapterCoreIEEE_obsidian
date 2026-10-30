---
type: componente
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/ExtractPanel.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - componente
---

# M3 - ExtractPanel

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Componente
> URL que llega desde «Extraer ficha»; `nonce` permite repetir la misma URL.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ExtractPrefill` | interface | URL que llega desde «Extraer ficha»; `nonce` permite repetir la misma URL. |
| `ExtractPanelProps` | interface | — |
| `ExtractPanel` | function | «Extraer convocatoria» (HU-7) rediseñado (spec 002, HU-12): pasos y ficha legible en lugar del bloque JSON del mockup 05; mismo flujo, validaciones y accesibilidad (RF-333). |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `societies` | sí | `IeeeSociety[]` |
| `onPublished` | sí | `() => void` |
| `officialDomains` | no | `readonly string[]` |
| `prefill` | no | `ExtractPrefill \| null` |


## Enlaces

- [[M3 - useOpportunityExtraction]]
- [[M3 - lib officialSources]]
- [[M3 - Tipos opportunity]]
- [[M3 - DraftCard]]
- [[M3 - DraftEditor]]
- [[M3 - ExtractSteps]]
- [[M3 - validateDraft]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
