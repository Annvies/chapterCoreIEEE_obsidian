---
type: componente
modulo: 5
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/forms/BuilderCanvas.tsx
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - componente
---

# M5 - BuilderCanvas

[[M5 - Interfaz]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/forms/BuilderCanvas.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `BuilderCanvas` | function | — |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `title` | sí | `string` |
| `description` | sí | `string` |
| `schema` | sí | `FormSchema` |
| `selectedId` | sí | `string \| null` |
| `onSelect` | sí | `(id: string) => void` |
| `onMove` | sí | `(id: string, direction: -1 \| 1) => void` |
| `onDuplicate` | sí | `(id: string) => void` |
| `onRemove` | sí | `(id: string) => void` |
| `onDropType` | sí | `(type: FieldType) => void` |


## Enlaces

- [[M5 - lib form-schema]]
- [[M5 - Tipos forms]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
