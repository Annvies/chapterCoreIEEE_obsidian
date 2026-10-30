---
type: prueba
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/schema/form-schema.zod.spec.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - prueba
---

# M5 - Prueba form-schema.zod.spec

[[M5 - Pruebas]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Prueba
> 7 casos de prueba (Jest).

### Casos

- **formSchemaSchema**
  - acepta un esquema valido con logica condicional
  - rechaza ids duplicados
  - rechaza dependencias circulares de visibilidad
- **buildSubmissionSchema**
  - no exige el campo condicional si no es visible
  - exige el campo condicional cuando la regla se cumple
  - valida el numero de membresia
  - valida que un archivo tenga referencia de carga en servidor

## Enlaces

- [[M5 - form-schema.zod]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
