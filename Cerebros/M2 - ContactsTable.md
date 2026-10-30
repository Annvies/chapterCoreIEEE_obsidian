---
type: componente
modulo: 2
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/contacts/ContactsTable.tsx
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-2
  - componente
---

# M2 - ContactsTable

[[M2 - Interfaz]] · [[Cerebro 2 - Contactos]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/contacts/ContactsTable.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ContactsTable` | function | — |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `tipo` | sí | `ContactType` |
| `data` | sí | `ContactList \| null` |
| `isLoading` | sí | `boolean` |
| `error` | sí | `string \| null` |
| `hasFilters` | sí | `boolean` |
| `selectedId` | sí | `string \| null` |
| `onSelect` | sí | `contact: ContactView): void` |
| `onRetry` | sí | `): void` |
| `onPageChange` | sí | `page: number): void` |


## Enlaces

- [[M2 - Tipos contacts]]
- [[M2 - StatusPill]]
- [[M2 - contact-labels]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
