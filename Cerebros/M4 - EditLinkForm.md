---
type: componente
modulo: 4
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/difusion/EditLinkForm.tsx
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-4
  - componente
---

# M4 - EditLinkForm

[[M4 - Interfaz]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/difusion/EditLinkForm.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `EditLinkFormProps` | interface | — |
| `EditLinkForm` | function | «Editar destino» / «Editar»: el código impreso no cambia, solo nombre, destino y estado. |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `link` | sí | `ShortLink` |
| `onSaved` | sí | `(link: ShortLink) => void` |
| `onCancel` | sí | `() => void` |


## Enlaces

- [[M4 - Cliente API difusion]]
- [[M4 - Tipos difusion]]
- [[M4 - validateLink]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
