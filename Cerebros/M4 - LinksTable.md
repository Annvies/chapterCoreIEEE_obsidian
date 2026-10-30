---
type: componente
modulo: 4
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/difusion/LinksTable.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - componente
---

# M4 - LinksTable

[[M4 - Interfaz]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/difusion/LinksTable.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `LinksTableProps` | interface | — |
| `LinksTable` | function | «Mis QR y enlaces oficiales» del mockup 06. |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `items` | sí | `ShortLink[]` |
| `isLoading` | sí | `boolean` |
| `error` | sí | `string \| null` |
| `selectedId` | sí | `string \| null` |
| `onSelect` | sí | `(id: string) => void` |
| `onSaved` | sí | `(link: ShortLink) => void` |
| `onRetry` | sí | `() => void` |
| `canEdit` | no | `boolean` |


## Enlaces

- [[M4 - lib qr]]
- [[M4 - Tipos difusion]]
- [[M4 - EditLinkForm]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
