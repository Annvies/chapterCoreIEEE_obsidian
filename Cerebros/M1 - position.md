---
type: dominio
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/domain/position.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - dominio
---

# M1 - position

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dominio
> Cargos y ámbitos confirmados en CONTEXTO.md §5. Una persona sin cargo es "miembro".

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `Cargo` | enum | Cargos y ámbitos confirmados en CONTEXTO.md §5. Una persona sin cargo es "miembro". |
| `Ambito` | enum | — |
| `CARGOS` | const | — |
| `AMBITOS` | const | — |
| `Position` | interface | — |
| `normalizePosition` | function | Normaliza la combinación cargo/ámbito/capítulo y devuelve un mensaje de error si no es coherente. Misma regla que el CHECK users_position_coherente. |


## Enlaces

- [[Cerebro 1 - Base institucional]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
