---
type: componente
modulo: 2
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/contacts/ContactDetailPanel.tsx
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-2
  - componente
---

# M2 - ContactDetailPanel

[[M2 - Interfaz]] · [[Cerebro 2 - Contactos]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/contacts/ContactDetailPanel.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ContactDetailPanel` | function | Panel derecho del mockup 04: ficha, acciones e historial. |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `detail` | sí | `ContactDetail \| null` |
| `error` | sí | `string \| null` |
| `hasSelection` | sí | `boolean` |
| `canEdit` | sí | `boolean` |
| `canDelete` | sí | `boolean` |
| `onRegister` | sí | `tipo: InteractionType): void` |
| `onEdit` | sí | `): void` |
| `onDelete` | sí | `): Promise<void>` |


## Enlaces

- [[M2 - Tipos contacts]]
- [[M2 - contact-labels]]
- [[M2 - StatusPill]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
