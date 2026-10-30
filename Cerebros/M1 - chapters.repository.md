---
type: repositorio
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/repositories/chapters.repository.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - repositorio
---

# M1 - chapters.repository

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Repositorio
> Lectura del catálogo de sociedades IEEE usado como capítulos de la Rama.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ChaptersRepository` | class | Lectura del catálogo de sociedades IEEE usado como capítulos de la Rama. |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `findAll()` | Promise<IeeeSociety[]> | — |
| `exists()` | Promise<boolean> | — |
| `findByIds()` | Promise<IeeeSociety[]> | — |


## Enlaces

- [[Cerebro 1 - Base institucional]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
