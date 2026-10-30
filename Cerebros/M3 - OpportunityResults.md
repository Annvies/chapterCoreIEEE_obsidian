---
type: componente
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/OpportunityResults.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - componente
---

# M3 - OpportunityResults

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/opportunities/OpportunityResults.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `OpportunityResultsProps` | interface | — |
| `OpportunityResults` | function | — |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `items` | sí | `Opportunity[]` |
| `isLoading` | sí | `boolean` |
| `error` | sí | `string \| null` |
| `emptyMessage` | sí | `string` |
| `savedIds` | sí | `ReadonlySet<string>` |
| `onToggleSave` | sí | `(id: string) => void` |
| `onRetry` | sí | `() => void` |


## Enlaces

- [[M3 - OpportunityCard]]
- [[M3 - Tipos opportunity]]
- [[M3 - filters]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
