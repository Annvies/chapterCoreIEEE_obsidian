---
type: concepto
modulo: 6
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/dashboard/dashboard.service.ts
actualizado: 2026-10-29
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

> [!question] Texto desactualizado en el código
> El mensaje del servicio dice que el módulo de difusión/QR «no está implementado», pero el Módulo 4 ya registra visitas: lo pendiente es la integración.

## Enlaces

- Forma parte de [[M6 - Periodos y filtros]].

## Fuentes

- `backendChapterCoreIEEE/src/dashboard/dashboard.service.ts`
