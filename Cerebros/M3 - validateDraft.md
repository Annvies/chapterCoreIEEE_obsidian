---
type: módulo
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/validateDraft.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - módulo
---

# M3 - validateDraft

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Módulo
> Límites del DTO del backend (CreateOpportunityDto) para fallar antes de enviar.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DraftField` | type | — |
| `DraftProblems` | type | — |
| `isIsoDate` | function | Fecha de calendario real en formato `aaaa-mm-dd` (rechaza 2027-02-30). |
| `validateDraft` | function | Problemas que impiden publicar, por campo (vacío = publicable). |
| `toPublishable` | function | Ficha lista para publicar, o `null` si aún tiene problemas. |


## Enlaces

- [[M3 - lib officialSources]]
- [[M3 - Tipos opportunity]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
