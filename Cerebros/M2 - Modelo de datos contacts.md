---
type: concepto
modulo: 2
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792627200000-CreateContactsModule.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-2
  - concepto
---

# M2 - Modelo de datos contacts

[[M2 - Directorio]] · [[Cerebro 2 - Contactos]]

> [!abstract] Qué es
> Tabla `contacts`: una fila por persona u organización del directorio.

> [!info] Confirmado en el código
> - Obligatorios: `tipo` y `nombre` (1–200).
> - Opcionales: organización, persona de contacto, cargo, correo, teléfono, sector, ciudad, `estado`, convenio, `convenio_vence`, capítulo (`chapter_id`), notas (máx. 2000) y `last_interaction_at`.
> - Autoría: `created_by` y `updated_by` (usuarios).

## Enlaces

- Forma parte de [[M2 - Directorio]].
- Relacionada con [[M2 - Tipos de contacto]], [[M2 - Importación CSV]], [[M2 - Acciones por nivel de acceso]].

## Fuentes

- `backendChapterCoreIEEE/src/database/migrations/1792627200000-CreateContactsModule.ts`
