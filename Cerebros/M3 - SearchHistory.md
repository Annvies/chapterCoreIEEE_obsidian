---
type: componente
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/SearchHistory.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - componente
---

# M3 - SearchHistory

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/opportunities/SearchHistory.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `SearchHistoryProps` | interface | — |
| `SearchHistory` | function | Historial propio de búsquedas en fuentes oficiales (spec 002, HU-11, RF-341). |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `items` | sí | `SearchHistoryEntry[]` |
| `isLoading` | sí | `boolean` |
| `error` | sí | `string \| null` |
| `canExtract` | sí | `boolean` |
| `onExtract` | sí | `(url: string) => void` |
| `onRemove` | sí | `(id: string) => void` |
| `onClear` | sí | `() => void` |
| `confirm` | no | `(message: string) => boolean` |


## Enlaces

- [[M3 - Tipos opportunity]]
- [[M3 - DiscoveryResultList]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
