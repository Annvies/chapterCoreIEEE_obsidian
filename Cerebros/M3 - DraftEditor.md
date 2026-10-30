---
type: componente
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/DraftEditor.tsx
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - componente
---

# M3 - DraftEditor

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/opportunities/DraftEditor.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DraftEditorProps` | interface | — |
| `DraftEditor` | function | Formulario controlado para corregir la ficha extraída antes de publicarla. |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `draft` | sí | `OpportunityDraft` |
| `societies` | sí | `IeeeSociety[]` |
| `problems` | sí | `DraftProblems` |
| `onChange` | sí | `(draft: OpportunityDraft) => void` |


## Enlaces

- [[M3 - Tipos opportunity]]
- [[M3 - validateDraft]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
