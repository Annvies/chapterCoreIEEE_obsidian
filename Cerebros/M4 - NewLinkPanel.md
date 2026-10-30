---
type: componente
modulo: 4
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/difusion/NewLinkPanel.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - componente
---

# M4 - NewLinkPanel

[[M4 - Interfaz]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/difusion/NewLinkPanel.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `NewLinkPanelProps` | interface | — |
| `NewLinkPanel` | function | «Nuevo QR dinámico» (pestaña Códigos QR) o «Nuevo enlace corto» (Enlaces oficiales). |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `tipo` | sí | `ShortLinkType` |
| `forms` | sí | `FormListItem[]` |
| `formsError` | sí | `string \| null` |
| `logo` | sí | `string \| null` |
| `onLogoChange` | sí | `(logo: string \| null) => void` |
| `onCreated` | sí | `(link: ShortLink) => void` |


## Enlaces

- [[M4 - Cliente API difusion]]
- [[M4 - lib qr]]
- [[M4 - Tipos difusion]]
- [[M4 - validateLink]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
