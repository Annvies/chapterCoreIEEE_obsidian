# Arquitectura de conocimiento (nivel senior)

## Principios

- **Una idea por nota (atómica)** y un título que la enuncie. Una nota que necesita
  más de ~3 callouts sobre temas distintos probablemente son dos notas.
- **Los enlaces son la estructura**; las carpetas solo agrupan por tipo. No crees
  jerarquías de carpetas profundas: Obsidian navega por enlaces, backlinks y grafo.
- **MOC (Map of Content):** nota índice que enlaza y explica un conjunto. En esta
  bóveda: `Mapa de cerebros` (MOC raíz) → cada `Cerebro N` (MOC de módulo) →
  subgrupos `MN - …` → notas de concepto/decisión.
- **Conectar con intención:** cada enlace debe explicar *por qué* se relaciona
  ("depende de", "alimenta a", "contradice"). Un enlace sin contexto vale poco.
- **Progresión de madurez:** pendiente → propuesto → confirmado. Nunca eliminar la
  marca de incertidumbre sin evidencia.

## Tipos de nota de esta bóveda

| Tipo (`type`) | Nombre de archivo | Propósito |
|---|---|---|
| `mapa` | `Mapa de cerebros` | MOC raíz |
| `cerebro` | `Cerebro N - <Módulo>` | MOC del módulo: propósito, funciones, límites, conexiones |
| `subgrupo` | `MN - <Tema>` | Un aspecto del módulo (3 por módulo) |
| `concepto` | `MN - <Concepto>` | Entidad o regla concreta (p. ej. "M1 - Matriz de permisos") |
| `decision` | `ADR-NNN - <Decisión>` | Decisión de arquitectura/producto con fecha, contexto y consecuencias |

Para crear más nodos útiles (no relleno), buenas candidatas son: entidades de base
de datos (`users`, `opportunities`, `short_links`, `form_versions`), flujos (alta por
invitación, extracción con Gemini, versionado de formularios), decisiones fechadas
de `CONTEXTO.md` y pendientes transversales (privacidad, filtro por capítulo).

## Properties (frontmatter) estándar

```yaml
---
type: subgrupo            # mapa | cerebro | subgrupo | concepto | decision
modulo: 3                 # 1-6 (omitir en notas transversales)
estado: confirmado        # confirmado | propuesto | pendiente | desactualizado
fuentes:                  # rutas del repo del producto o URLs oficiales
  - backendChapterCoreIEEE/src/opportunities/opportunities.service.ts
actualizado: 2026-10-29   # fecha de la última verificación contra el código
aliases:
  - Extracción con IA
tags:
  - chaptercore
  - modulo-3
  - subgrupo
---
```

- Las etiquetas `modulo-N` dan color en el grafo; **no las cambies**.
- `estado` y `actualizado` permiten Bases de seguimiento (ver `templates/pendientes.base`).
- Las properties de tipo lista usan YAML de lista, no texto separado por comas.

## Estructura de un cerebro

1. Título `# Cerebro N — <nombre completo>`
2. `## Subgrupos conectados` (3 enlaces)
3. Callouts en orden: `abstract` (propósito) → `info` (datos/componentes) →
   `success` (flujo) → `example` → `tip` → `warning` → `todo`/`question`
4. `## Conexiones` (relación con otros módulos, con verbo)
5. `## Fuentes` (código y documentos; luego fuentes externas)

## Nombres y estilo

- Español, mayúscula inicial solo en la primera palabra y nombres propios.
- Sin caracteres prohibidos en nombres de archivo: `* " \ / < > : | ?` ni `#^[]`.
- No renombres archivos existentes sin actualizar todos los enlaces (Obsidian lo
  hace solo si se renombra **desde Obsidian** con "actualizar enlaces" activo).
- Fechas ISO (`AAAA-MM-DD`).

## Anti‑patrones

- Copiar código largo en notas (enlaza la ruta y resume la regla).
- Etiquetas que duplican enlaces (`#contactos` cuando ya enlaza al cerebro).
- Notas huérfanas o callejones sin salida (sin enlaces salientes).
- Afirmaciones del producto sin fuente o con fuente de las carpetas de tooling.
