---
type: componente
modulo: 5
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/public/DynamicForm.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-5
  - componente
---

# M5 - DynamicForm

[[M5 - Interfaz]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/public/DynamicForm.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DynamicForm` | function | — |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `schema` | sí | `FormSchema` |
| `submitting` | sí | `boolean` |
| `serverError` | sí | `string \| null` |
| `onSubmit` | sí | `(data: Record<string, unknown>) => Promise<void>` |
| `field` | sí | `FormField` |
| `value` | sí | `unknown` |
| `error` | no | `string` |
| `onChange` | sí | `(value: unknown) => void` |


## Enlaces

- [[M5 - lib form-schema]]
- [[M5 - Tipos forms]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
