---
type: dominio
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/domain/permissions.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-1
  - dominio
---

# M1 - permissions

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Dominio
> Niveles del mockup 03. Mapeo de cargos confirmado por el equipo el 2026-10-19: Mesa Directiva      -> Presidente, Vicepresidente, Tesorero y Webmaster de la Rama Secretaría          -> Secretario (de la Rama o de un capítulo) Director de capítulo-> Presidente, Vicepresidente, Tesorero y Webmaster de un capítulo Miembro             -> sin cargo directivo

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `AccessLevel` | enum | Niveles del mockup 03. Mapeo de cargos confirmado por el equipo el 2026-10-19: Mesa Directiva      -> Presidente, Vicepresidente, Tesorero y Webmaster de la Rama Secretaría          -> Secretario (de la Rama o de un capítulo) Director de capítulo-> Presidente, Vicepresidente, Tesorero y Webmaster de un capítulo Miembro             -> sin cargo directivo |
| `ACCESS_LEVELS` | const | — |
| `Feature` | enum | — |
| `FEATURES` | const | — |
| `Access` | enum | Ordenados de menor a mayor: un permiso incluye a los anteriores. |
| `PermissionCell` | interface | — |
| `PERMISSION_MATRIX` | const | Matriz del mockup 03 adoptada como oficial el 2026-10-19. |
| `resolveAccessLevel` | function | — |
| `MESA_DIRECTIVA_BRANCH_CARGOS` | const | Cargos que, con ámbito Rama, otorgan el nivel Mesa Directiva. |
| `hasAccess` | function | — |
| `permissionsFor` | function | — |


## Enlaces

- [[M1 - position]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
