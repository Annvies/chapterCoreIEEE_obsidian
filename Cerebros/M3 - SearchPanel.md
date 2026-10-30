---
type: componente
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/SearchPanel.tsx
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - componente
---

# M3 - SearchPanel

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/opportunities/SearchPanel.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `SearchPanelProps` | interface | — |
| `SearchPanel` | function | — |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `filter` | sí | `QuickFilter` |
| `chapter` | sí | `string` |
| `societies` | sí | `IeeeSociety[]` |
| `onSearch` | sí | `(query: string) => void` |
| `onFilterChange` | sí | `(filter: QuickFilter) => void` |
| `onChapterChange` | sí | `(chapter: string) => void` |


## Enlaces

- [[M3 - Tipos opportunity]]
- [[M3 - filters]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
