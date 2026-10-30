---
type: componente
modulo: 1
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/access/UsersPanel.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - componente
---

# M1 - UsersPanel

[[M1 - Interfaz]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/access/UsersPanel.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `UsersPanel` | function | — |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `search` | sí | `string` |
| `onSearchChange` | sí | `value: string): void` |
| `data` | sí | `UserList \| null` |
| `isLoading` | sí | `boolean` |
| `error` | sí | `string \| null` |
| `onRetry` | sí | `): void` |
| `onSelect` | sí | `user: UserView): void` |


## Enlaces

- [[M1 - lib access]]
- [[M1 - Tipos auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
