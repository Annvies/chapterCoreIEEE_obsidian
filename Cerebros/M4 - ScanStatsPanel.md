---
type: componente
modulo: 4
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/difusion/ScanStatsPanel.tsx
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-4
  - componente
---

# M4 - ScanStatsPanel

[[M4 - Interfaz]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/difusion/ScanStatsPanel.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ScanStatsPanelProps` | interface | — |
| `ScanStatsPanel` | function | «Escaneos · últimos 14 días» del mockup 06 para el enlace seleccionado. |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `link` | sí | `ShortLink \| null` |
| `stats` | sí | `LinkStats \| null` |
| `isLoading` | sí | `boolean` |
| `error` | sí | `string \| null` |
| `onRetry` | sí | `() => void` |


## Enlaces

- [[M4 - Tipos difusion]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
