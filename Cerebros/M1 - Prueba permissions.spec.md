---
type: prueba
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/domain/permissions.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - prueba
---

# M1 - Prueba permissions.spec

[[M1 - Pruebas]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Prueba
> 11 casos de prueba (Jest).

### Casos

- **resolveAccessLevel**
  - %s de %s es %s
  - sin cargo es miembro
- **hasAccess (matriz del mockup 03)**
  - solo la Mesa Directiva administra usuarios
  - formularios: secretaría total, director edita sin borrar, miembro solo responde
  - todas las personas ven oportunidades; los miembros no editan
- **hasAccess (Módulo 7 · gastos y tesorería)**
  - solo la Mesa Directiva elimina gastos
  - Director de capítulo registra solo en su capítulo y Secretaría solo consulta
  - un Miembro no accede a la tesorería
- **normalizePosition**
  - limpia ámbito y capítulo cuando no hay cargo
  - descarta el capítulo en cargos de Rama
  - exige ámbito y capítulo cuando corresponde

## Enlaces

- [[M1 - permissions]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
