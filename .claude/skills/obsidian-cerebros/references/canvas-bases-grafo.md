# Canvas, Bases y grafo

## JSON Canvas 1.0 (`.canvas`) — <https://jsoncanvas.org/spec/1.0/>

Raíz: `{ "nodes": [...], "edges": [...] }` (ambos opcionales). Los nodos se
dibujan en orden: el primero queda debajo (z‑index ascendente), así que **los
grupos van antes que sus hijos**.

**Nodo (común):** `id` (único), `type` (`text` | `file` | `link` | `group`),
`x`, `y`, `width`, `height` (enteros, px), `color` opcional.

| type | Campos propios |
|---|---|
| `text` | `text` (Markdown) |
| `file` | `file` (ruta desde la raíz de la bóveda), `subpath` opcional (`#Encabezado`) |
| `link` | `url` |
| `group` | `label`, `background`, `backgroundStyle` (`cover` \| `ratio` \| `repeat`) |

**Edge:** `id`, `fromNode`, `toNode`, `fromSide`/`toSide`
(`top`|`right`|`bottom`|`left`), `fromEnd` (def. `none`), `toEnd` (def. `arrow`),
`color`, `label`.

**Color:** hex `"#RRGGBB"` o preset `"1"` rojo, `"2"` naranja, `"3"` amarillo,
`"4"` verde, `"5"` cian, `"6"` morado.

**Reglas para este canvas:** un grupo por módulo (cerebro + 3 subgrupos dentro de
los límites del grupo), conexiones con `label` que expliquen la dependencia
("permisos", "alimenta KPI"), ids estables y legibles (`m3-extraccion`). Valida
siempre con `JSON.parse` y comprueba que cada `file` existe (`vault_lint` lo hace).

## Bases (`.base`, core plugin desde v1.9)

YAML con `filters`, `formulas`, `properties`, `summaries`, `views`.

```yaml
filters:
  and:
    - file.inFolder("Cerebros")
    - file.hasTag("chaptercore")
formulas:
  dias_sin_verificar: '(now() - date(actualizado)).days'
properties:
  estado:
    displayName: Estado
views:
  - type: table
    name: Por módulo
    groupBy: { property: note.modulo, direction: ASC }
    order: [file.name, estado, actualizado, formula.dias_sin_verificar]
  - type: kanban            # vista kanban (v1.14)
    name: Madurez
    groupBy: { property: note.estado, direction: ASC }
```

- Prefijos: `note.` (o nada) = frontmatter, `file.` = archivo
  (`file.name`, `file.folder`, `file.links`, `file.backlinks`, `file.tags`,
  `file.mtime`), `formula.` = fórmulas.
- Filtros: cadena o `and`/`or`/`not` anidados; funciones `file.hasTag()`,
  `file.inFolder()`, `file.hasLink()`; operadores `== != > < >= <= && || !`.
- Fechas: `now() + "1 day"`, `date("2026-01-01")`; unidades `y M w d h m s`.
- Vistas: `table`, `list`, `cards`, `map`, `kanban`, y las que añadan plugins
  (API de Bases desde v1.10). Resúmenes: `Average`, `Sum`, `Empty`, `Filled`,
  `Unique`… `groupBy` y `groupOrder` para agrupar.
- `file.backlinks` no se refresca automáticamente: no lo uses como métrica en vivo.

## Grafo (`.obsidian/graph.json`)

- `colorGroups`: lista de `{ "query": "tag:#modulo-1", "color": { "a": 1, "rgb": <entero> } }`.
  `rgb` es el hex en decimal (`0xF28C28` = 15895592). Gana el primer grupo que coincide.
- Filtros útiles: `search` (en esta bóveda `path:"Cerebros/"`; sin la barra también
  coincide con `ChapterCore - Cerebros.canvas`, que enlaza todo y se vuelve el centro), `showOrphans`, `showTags`,
  `showAttachments`, `hideUnresolved`. Fuerzas: `centerStrength`, `repelStrength`,
  `linkStrength`, `linkDistance`.
- Colores de módulos usados en esta bóveda: 1 naranja `#F28C28`, 2 coral `#FF7F50`,
  3 amarillo `#E8C547`, 4 verde `#4CAF50`, 5 azul `#3B82F6`, 6 violeta `#8B5CF6`.
- Obsidian reescribe `graph.json` al cerrar el panel del grafo: edítalo con la app
  cerrada o desde la interfaz (Grafo → Grupos).
- **Más nodos = más notas.** El grafo dibuja un nodo por archivo (y opcionalmente
  por etiqueta o adjunto). Para enriquecerlo crea notas de concepto/decisión reales,
  no notas vacías.
- Excluir del grafo/búsqueda: *Ajustes → Archivos y enlaces → Archivos excluidos*
  (`userIgnoreFilters` en `app.json`). Las carpetas que empiezan por `.` ya se ignoran.
