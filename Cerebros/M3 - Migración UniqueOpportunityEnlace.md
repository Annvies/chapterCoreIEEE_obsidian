---
type: migración
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792454400000-UniqueOpportunityEnlace.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - migración
---

# M3 - Migración UniqueOpportunityEnlace

[[M3 - Base de datos]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Migración
> Evita dos oportunidades publicadas con el mismo enlace aunque se publiquen a la vez (la comprobación previa del servicio no basta ante una carrera). El servicio guarda el enlace en forma canónica (normalizeOfficialUrl) antes de insertar.

| Campo | Valor |
|---|---|
| Archivo | `1792454400000-UniqueOpportunityEnlace.ts` |
| Marca de tiempo | `1792454400000` (orden de ejecución) |
| Reversible | sí, tiene `down()` |

### Qué hace

- Índice único `opportunities_enlace_publicada_uq` en `opportunities`

## Enlaces

- [[M3 - Tabla opportunities]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
