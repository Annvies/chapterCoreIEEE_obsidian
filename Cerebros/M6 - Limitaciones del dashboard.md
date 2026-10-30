---
type: concepto
modulo: 6
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/dashboard/dashboard.service.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-6
  - concepto
---

# M6 - Limitaciones del dashboard

[[M6 - Periodos y filtros]] · [[Cerebro 6 - Feedback y KPIs]]

> [!abstract] Qué es
> Lo que el Dashboard informa como no disponible.

> [!info] Confirmado en el código
> - `eventosRealizados` y `escaneosQr` se devuelven vacíos (`null`).
> - Las métricas son globales de la Rama: el filtro por capítulo del Director está pendiente.
> - El periodo por defecto es **semestre**.

> [!success] Resuelto en el PR #28 (pendiente de fusión)
> - `escaneosQr` cuenta las visitas QR del periodo ([[M6 - Escaneos de QR]]).
> - El Director de capítulo recibe alcance `chapter` ([[M6 - Alcance por capítulo]]).
> - `limitaciones` conserva solo la de eventos; para el Director añade la de métricas
>   sin asociación de capítulo y, si no tiene capítulo, la que lo explica.
> - Con eso deja de existir el mensaje desactualizado que decía que el módulo de QR «no
>   está implementado».

## Enlaces

- Forma parte de [[M6 - Periodos y filtros]].

## Fuentes

- `backendChapterCoreIEEE/src/dashboard/dashboard.service.ts`
