---
type: migración
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792627200000-CreateContactsModule.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-2
  - migración
---

# M2 - Migración CreateContactsModule

[[M2 - Base de datos]] · [[Cerebro 2 - Contactos]]

> [!abstract] Migración
> Módulo 2: directorio de empresas, alumni, conferencistas y autoridades (mockup 04) con su historial de interacciones. Depende de ieee_societies (capítulo opcional) y de users (autoría), creadas en migraciones anteriores.

| Campo | Valor |
|---|---|
| Archivo | `1792627200000-CreateContactsModule.ts` |
| Marca de tiempo | `1792627200000` (orden de ejecución) |
| Reversible | sí, tiene `down()` |

### Qué hace

- Extensión `pgcrypto`
- Extensión `citext`
- Crea la tabla `contacts`
- Crea la tabla `contact_interactions`
- Índice `contacts_tipo_nombre_idx` en `contacts`
- Índice `contacts_chapter_id_idx` en `contacts`
- Índice `contact_interactions_contact_fecha_idx` en `contact_interactions`

## Enlaces

- [[M2 - Tabla contacts]]
- [[M2 - Tabla contact_interactions]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
