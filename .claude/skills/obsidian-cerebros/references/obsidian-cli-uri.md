# Obsidian CLI y URI

## Obsidian CLI (v1.12, instalador ≥ 1.12.7) — <https://obsidian.md/help/cli>

Gratis e incluida en la app. **Requiere Obsidian abierto** (el primer comando lo
lanza). Activar: *Ajustes → General → Command line interface*. En Windows añade
`Obsidian.com` al PATH (reiniciar la terminal).

Sintaxis: `obsidian <comando> clave=valor flag`. `vault=<nombre>` como primer
parámetro si no estás dentro de la carpeta de la bóveda. `file=<nombre>` resuelve
como un enlace wiki; `path=<ruta>` es exacto. `format=json` donde exista. `--copy`
copia la salida.

Comandos más útiles para los cerebros:

| Objetivo | Comando |
|---|---|
| Enlaces rotos | `obsidian unresolved` |
| Huérfanas / callejones sin salida | `obsidian orphans` · `obsidian deadends` |
| Backlinks y enlaces de una nota | `obsidian backlinks file="Cerebro 3 - Oportunidades IEEE"` · `obsidian links file=…` |
| Properties | `obsidian properties format=json counts` · `obsidian property:set name=estado value=confirmado file=…` |
| Etiquetas | `obsidian tags counts sort=count` |
| Buscar | `obsidian search query="filtro por capítulo" format=json` · `search:context` |
| Leer / crear / añadir | `obsidian read file=…` · `obsidian create name=… template=… ` · `obsidian append file=… content="…"` |
| Bases | `obsidian bases` · `obsidian base:query …` · `obsidian base:views` |
| Esquema | `obsidian outline file=…` |
| Historial y diff | `obsidian history file=…` · `obsidian diff file=… from=1 to=2` |
| Plugins | `obsidian plugins:enabled` · `obsidian plugin:enable id=…` |
| Depuración | `obsidian dev:errors` · `obsidian dev:screenshot path=grafo.png` |

Precaución: `eval code=…`, `delete`, `plugin:install` y `history:restore` cambian
estado o ejecutan código; pide confirmación antes de usarlos.

## URI `obsidian://` (core)

- `obsidian://open?vault=<bóveda>&file=<ruta>` — abrir nota.
- `obsidian://new?vault=…&file=…&content=…` — crear nota.
- `obsidian://search?vault=…&query=…` — buscar.
- Valores codificados con `encodeURIComponent`. El plugin **Advanced URI** (gratis)
  añade comandos, escritura en encabezados y frontmatter.
