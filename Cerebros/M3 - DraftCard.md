---
type: componente
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/DraftCard.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - componente
---

# M3 - DraftCard

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/opportunities/DraftCard.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DraftCardProps` | interface | — |
| `DraftCard` | function | Ficha legible (spec 002, HU-12): sustituye al bloque JSON del mockup 05. |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `draft` | sí | `OpportunityDraft \| null` |
| `societies` | sí | `IeeeSociety[]` |
| `id` | sí | `DraftField \| 'capitulo'` |
| `label` | sí | `string` |
| `notices` | sí | `string[]` |
| `children` | sí | `ReactNode` |


## Enlaces

- [[M3 - Tipos opportunity]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
