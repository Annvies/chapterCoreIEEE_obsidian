---
type: componente
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/DiscoveryResultList.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - componente
---

# M3 - DiscoveryResultList

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/opportunities/DiscoveryResultList.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DiscoveryResultListProps` | interface | — |
| `DiscoveryResultList` | function | Resultados «sin verificar» con formato de buscador (spec 002, RF-317 y RF-340). Títulos y fragmentos llegan como texto plano y React los escapa: nunca se interpreta su HTML. |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `results` | sí | `DiscoveryResult[]` |
| `headingLevel` | no | `3 \| 4` |


## Enlaces

- [[M3 - Tipos opportunity]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
