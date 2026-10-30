# Plugins recomendados (no IA), gratis

**Primero los core plugins** (ya incluidos, sin riesgo de terceros): Bases,
Canvas, Grafo, Properties, Plantillas, Backlinks, Enlaces salientes, Esquema,
Marcadores, Búsqueda, Recuperación de archivos. Esta bóveda ya los tiene activos
(`.obsidian/core-plugins.json`).

Comunitarios, todos gratuitos y de código abierto (descargas a 2026-10-29):

| Plugin (id) | Descargas | Uso en los cerebros | Prioridad |
|---|---|---|---|
| **Obsidian Git** (`obsidian-git`) | 3,4 M | Ver cambios y hacer pull desde Obsidian. **Desactiva el auto-commit/auto-push**: los commits los decide el equipo | Alta |
| **Dataview** (`dataview`) | 5,2 M | Consultas sobre properties (p. ej. notas con `estado: pendiente`). Para tablas simples, preferir Bases (core) | Media |
| **Templater** (`templater-obsidian`) | 6,0 M | Plantillas con fecha y prompts. Puede ejecutar JavaScript: no aceptar plantillas de terceros | Media |
| **Linter** (`obsidian-linter`) | 1,3 M | Formato consistente de YAML, encabezados y espacios | Media |
| **Omnisearch** (`omnisearch`) | 2,1 M | Búsqueda difusa, también en PDFs | Media |
| **Excalidraw** (`obsidian-excalidraw-plugin`) | 8,8 M | Diagramas de arquitectura del producto | Opcional |
| **Extended Graph** (`extended-graph`) | 80 k | Grafo con estados guardados e imágenes | Opcional |
| **Breadcrumbs** (`breadcrumbs`) | 426 k | Jerarquía mapa → cerebro → subgrupo con properties `up`/`down` | Opcional |
| **Kanban** (`obsidian-kanban`) | 2,8 M | Tablero de pendientes (o la vista kanban de Bases, v1.14) | Opcional |
| **Iconize** (`obsidian-icon-folder`) | 2,3 M | Iconos por módulo en el explorador | Opcional |
| **Style Settings** (`obsidian-style-settings`) | 2,8 M | Ajustar el tema sin CSS | Opcional |
| **Advanced URI** (`obsidian-advanced-uri`) | 0,69 M | Automatización por URI | Opcional |
| **Plugin Update Tracker** (`obsidian-plugin-update-tracker`) | 170 k | Ver actualizaciones y evaluar su riesgo antes de actualizar | Alta si instalas varios |
| **Note Refactor** (`note-refactor-obsidian`) | 350 k | Dividir notas grandes en notas atómicas | Opcional |

## Cómo compartirlos con el equipo

- La lista de plugins activos vive en `.obsidian/community-plugins.json` y sus
  ajustes en `.obsidian/plugins/<id>/data.json`. Versiona solo los ajustes que no
  contengan claves ni rutas personales; el código (`main.js`) se instala desde la app.
- Antes de proponer un plugin al equipo, pasa la lista de
  `obsidian-desarrollo-plugins.md` → "Lista de evaluación".
