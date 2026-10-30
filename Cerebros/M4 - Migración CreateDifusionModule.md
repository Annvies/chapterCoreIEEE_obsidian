---
type: migración
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/database/migrations/1792540800000-CreateDifusionModule.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - migración
---

# M4 - Migración CreateDifusionModule

[[M4 - Base de datos]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Migración
> Módulo 4 · Difusión, webmaster y QR (CONTEXTO.md §4, mockup 06): acortador de URLs, QR dinámicos (el QR codifica la URL corta y el destino se puede cambiar) y registro append-only de escaneos/clics con datos mínimos (sin IP ni user-agent).

| Campo | Valor |
|---|---|
| Archivo | `1792540800000-CreateDifusionModule.ts` |
| Marca de tiempo | `1792540800000` (orden de ejecución) |
| Reversible | sí, tiene `down()` |

### Qué hace

- Tipo enumerado `short_link_type`
- Tipo enumerado `short_link_status`
- Tipo enumerado `qr_style`
- Crea la tabla `short_links`
- Crea la tabla `link_visits`
- Índice `link_visits_link_id_visited_at_idx` en `link_visits`

## Enlaces

- [[M4 - Tabla short_links]]
- [[M4 - Tabla link_visits]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
