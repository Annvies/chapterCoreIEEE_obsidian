---
type: migración
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792454400000-CreateAuthModule.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - migración
---

# M1 - Migración CreateAuthModule

[[M1 - Base de datos]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Migración
> Módulo 1: usuarios con cargo/ámbito (CONTEXTO.md §5) y enlaces de un solo uso para invitación y restablecimiento de contraseña. Depende de ieee_societies (migración de oportunidades) para el capítulo de los cargos de capítulo.

| Campo | Valor |
|---|---|
| Archivo | `1792454400000-CreateAuthModule.ts` |
| Marca de tiempo | `1792454400000` (orden de ejecución) |
| Reversible | sí, tiene `down()` |

### Qué hace

- Extensión `pgcrypto`
- Extensión `citext`
- Crea la tabla `users`
- Crea la tabla `auth_tokens`
- Índice `users_chapter_id_idx` en `users`
- Índice `auth_tokens_user_id_idx` en `auth_tokens`

## Enlaces

- [[M1 - Tabla users]]
- [[M1 - Tabla auth_tokens]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
