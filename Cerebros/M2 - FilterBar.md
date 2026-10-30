---
type: componente
modulo: 2
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/contacts/FilterBar.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-2
  - componente
---

# M2 - FilterBar

[[M2 - Interfaz]] · [[Cerebro 2 - Contactos]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/contacts/FilterBar.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DirectoryFilters` | interface | — |
| `FilterBar` | function | "filtros:" del mockup: los activos se quitan con ✕; los demás se añaden con "+ …". |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `filters` | sí | `DirectoryFilters` |
| `sectors` | sí | `string[]` |
| `chapters` | sí | `Chapter[]` |
| `onChange` | sí | `filters: DirectoryFilters): void` |


## Enlaces

- [[M2 - Tipos contacts]]
- [[M2 - contact-labels]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
