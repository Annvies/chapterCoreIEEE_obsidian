# Instrucciones para agentes (Codex, OpenCode, Gemini CLI, GitHub Copilot, Claude Code)

Este repositorio es la bóveda de Obsidian del proyecto ChapterCore. Para cualquier
tarea sobre la bóveda, Obsidian o los "cerebros" de los módulos, usa la skill
**obsidian-cerebros**:

1. Lee `.claude/skills/obsidian-cerebros/SKILL.md` y síguelo.
2. Carga los archivos de `.claude/skills/obsidian-cerebros/references/` solo cuando
   el paso lo requiera.
3. Herramientas: MCP `chaptercore-vault` si tu cliente lo cargó; si no,
   `node .claude/skills/obsidian-cerebros/mcp/server.mjs lint | overview | module <1-6> | repo`.

Reglas mínimas (detalle en la skill):

- Verifica todo contra el repositorio del producto
  (<https://github.com/marianZamorano/chapterCoreIEEE>) y cita la fuente. No inventes.
  Cada persona puede tenerlo clonado en otra ruta: comprueba con
  `node .claude/skills/obsidian-cerebros/mcp/server.mjs where` y, si no aparece,
  pide la ruta y usa `... server.mjs setup "<ruta>"`.
- No leas ni copies secretos (`.env`, claves) ni datos personales reales.
- Solo plugins y servicios gratuitos, preferentemente locales.
- No hagas commit ni push sin autorización explícita del usuario.
- Conserva los nombres de archivo y los enlaces `[[...]]`; termina con el lint sin errores.
