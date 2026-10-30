# Opciones MCP para los cerebros

| | Opción | Requiere Obsidian abierto | Escritura | Costo | Riesgo |
|---|---|---|---|---|---|
| **A** | `chaptercore-vault` (esta skill) | No | Opcional (desactivada) | Gratis, sin dependencias | Bajo: sin red, sin ejecución de comandos, bloquea secretos |
| **B** | Plugin **Local REST API with MCP** | Sí | Sí (con ETag) | Gratis (MIT) | Medio: API key; solo 127.0.0.1 |
| **C** | `@modelcontextprotocol/server-filesystem` | No | Sí | Gratis | Medio: genérico, no entiende enlaces |
| **D** | Obsidian CLI (no es MCP) | Sí | Sí | Gratis | Bajo/medio según el comando |
| **E** | Otros plugins MCP (MCP Connector, Vault as MCP…) | Sí | Sí | Gratis | Medio/alto: varios sin revisión manual |

Recomendación: **A** siempre (auditoría y lectura del producto) + **B** solo si se
quiere editar dentro de Obsidian con su índice.

## A. chaptercore-vault

`mcp/server.mjs` — Node ≥ 18, sin `npm install`. Herramientas: `vault_overview`,
`vault_lint`, `module_context`, `vault_list_notes`, `vault_read_note`,
`vault_search`, `vault_links`, `repo_overview`, `repo_read_file`, `repo_search`,
`vault_write_note`.

Ubicación del clon del producto (cada persona puede tenerlo en otra ruta), por
prioridad: `CHAPTERCORE_REPO` → `.chaptercore.local.json` (creado con
`server.mjs setup "<ruta>"`, ignorado por Git) → detección automática cerca de la
bóveda y en carpetas habituales del usuario (remoto `marianZamorano/chapterCoreIEEE`
o `CONTEXTO.md` + `backendChapterCoreIEEE/`). `server.mjs where` muestra cuál usó.

Otras variables: `CHAPTERCORE_VAULT`,
`CHAPTERCORE_VAULT_WRITE=1` (habilita escritura de `.md`/`.canvas`/`.base` fuera
de carpetas ocultas y sin sobrescribir salvo `overwrite=true`).

Configuración incluida en el repositorio (rutas relativas a la raíz de la bóveda):

| Agente | Archivo |
|---|---|
| Claude Code | `.mcp.json` |
| Codex CLI | `.codex/config.toml` (proyecto de confianza) |
| OpenCode | `opencode.json` |
| Gemini CLI | `.gemini/settings.json` |
| GitHub Copilot (VS Code) | `.vscode/mcp.json` |

Sin MCP: `node .claude/skills/obsidian-cerebros/mcp/server.mjs lint`.

## B. Local REST API with MCP

1. Instalar el plugin desde *Plugins de la comunidad*; copiar la API key en sus ajustes.
2. Endpoint MCP: `https://127.0.0.1:27124/mcp/` (Streamable HTTP; certificado
   propio en `https://127.0.0.1:27124/obsidian-local-rest-api.crt`).
3. Claude Code (**no** lo guardes en el repo; usa ámbito de usuario):
   ```bash
   claude mcp add --scope user --transport http obsidian https://127.0.0.1:27124/mcp/ \
     --header "Authorization: Bearer $OBSIDIAN_API_KEY"
   ```
4. Herramientas: `vault_read`, `vault_write`, `vault_patch` (encabezado, bloque o
   frontmatter), `vault_append`, `vault_move`, `search_query`, `tag_list`,
   `command_execute`, `open_file`…
5. No actives el puerto HTTP 27123 salvo que haga falta; nunca expongas el puerto
   fuera de localhost.

## C. Filesystem MCP oficial

```json
{ "mcpServers": { "vault-fs": { "command": "npx", "args": ["-y",
  "@modelcontextprotocol/server-filesystem@<versión fija>", "<ruta de la bóveda>"] } } }
```
Fija la versión (no uses `latest`) y limita la ruta a la bóveda.

## D. Obsidian CLI

Ver `obsidian-cli-uri.md`. Ideal para `unresolved`, `orphans`, `properties` y
`base:query` usando el índice real de Obsidian.
