---
type: componente
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/StrategySelector.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - componente
---

# M3 - StrategySelector

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/opportunities/StrategySelector.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `StrategySelectorProps` | interface | — |
| `StrategySelector` | function | Modo de desarrollo: forzar una sola estrategia. Nunca visible en producción (RF-327). |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `config` | sí | `DiscoveryConfig \| null` |
| `value` | sí | `StrategyName \| ''` |
| `onChange` | sí | `(value: StrategyName \| '') => void` |
| `devMode` | no | `boolean` |


## Enlaces

- [[M3 - Tipos opportunity]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
