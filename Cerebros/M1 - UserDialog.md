---
type: componente
modulo: 1
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/access/UserDialog.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - componente
---

# M1 - UserDialog

[[M1 - Interfaz]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/access/UserDialog.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `UserDialog` | function | — |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `mode` | sí | `'invite' \| 'edit'` |
| `user` | no | `UserView` |
| `onClose` | sí | `): void` |
| `onSaved` | sí | `user: UserView, link?: AccessLink): void` |


## Enlaces

- [[M1 - Cliente API auth]]
- [[M1 - auth-context]]
- [[M1 - lib access]]
- [[M1 - lib ieee]]
- [[M1 - Tipos auth]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
