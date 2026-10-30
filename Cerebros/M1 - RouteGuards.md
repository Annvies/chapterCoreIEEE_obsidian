---
type: componente
modulo: 1
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/auth/RouteGuards.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - componente
---

# M1 - RouteGuards

[[M1 - Interfaz]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Componente
> Exige sesión; si no hay, manda al login recordando a dónde se quería ir.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `RequireAuth` | function | Exige sesión; si no hay, manda al login recordando a dónde se quería ir. |
| `RequirePermission` | function | Exige un permiso de la matriz; el backend vuelve a validarlo en cada petición. |
| `ForbiddenPage` | function | — |
| `HomeRedirect` | function | Inicio según permisos: formularios para quien los administra, si no oportunidades. |


## Enlaces

- [[M1 - Tipos auth]]
- [[M1 - auth-context]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
