# ChapterCore IEEE — Bóveda de Obsidian

Bóveda de notas del proyecto académico **ChapterCore**, el Sistema de Organización de la Rama
Estudiantil IEEE (UPB).

- Repositorio del producto: [marianZamorano/chapterCoreIEEE](https://github.com/marianZamorano/chapterCoreIEEE)
- Equipo: Valeria Isabel Lopez Pinto · Marian Isabel Zamorano Alcazar · Angela de Jesus Valcarce Arumbary

## Cómo abrir la bóveda

1. Clona este repositorio.
2. En Obsidian, elige **Abrir carpeta como bóveda** y selecciona la carpeta clonada.

## Cerebros por módulo

El mapa de los seis módulos y sus conexiones está en [[Cerebros/Mapa de cerebros]].
La vista espacial con grupos de color está en [[ChapterCore - Cerebros.canvas]].
Cada módulo tiene su cerebro y tres subgrupos enlazados.

## Skill para agentes de IA: obsidian-cerebros

La skill [`.claude/skills/obsidian-cerebros/`](.claude/skills/obsidian-cerebros/SKILL.md)
convierte a cualquier agente en un experto en Obsidian que audita y mejora los cerebros
contrastándolos con el código del producto. Es gratuita, local y de solo lectura por defecto.

| Agente | Cómo la encuentra | MCP `chaptercore-vault` |
|---|---|---|
| Claude Code | `.claude/skills/` | `.mcp.json` |
| Codex CLI | `.agents/skills/` + `AGENTS.md` | `.codex/config.toml` |
| OpenCode | `.claude/skills/` + `AGENTS.md` | `opencode.json` |
| Gemini CLI | `GEMINI.md` → `AGENTS.md` | `.gemini/settings.json` |
| GitHub Copilot | `.github/copilot-instructions.md` + `AGENTS.md` | `.vscode/mcp.json` |

Requisitos: Node.js 18 o superior y el repositorio del producto clonado **en cualquier
carpeta**. Cada persona puede tenerlo en una ruta distinta; el servidor lo busca así:

1. Variable de entorno `CHAPTERCORE_REPO`, si existe.
2. Archivo personal `.chaptercore.local.json` (no se sube a Git).
3. Detección automática: carpetas cercanas a la bóveda y carpetas habituales del usuario
   (Documentos, Escritorio, `source/repos`, `GitHub`, `Projects`…). Reconoce el clon por su
   remoto `marianZamorano/chapterCoreIEEE` o por su contenido.

Para comprobarlo o fijar tu ruta, desde la raíz de la bóveda:

```bash
node .claude/skills/obsidian-cerebros/mcp/server.mjs where                         # ¿dónde lo encontró?
node .claude/skills/obsidian-cerebros/mcp/server.mjs setup "D:/mis-repos/chapterCoreIEEE"   # fijar tu ruta
```

Después de `setup`, reinicia el agente (en VS Code: `Developer: Reload Window`).

Otros comandos sin MCP:

```bash
node .claude/skills/obsidian-cerebros/mcp/server.mjs lint       # auditoría de la bóveda
node .claude/skills/obsidian-cerebros/mcp/server.mjs module 3   # contexto de un módulo
```

Ejemplo de pedido al agente: *"Usa obsidian-cerebros para mejorar el Cerebro 3 con el código actual"*.

## Qué se versiona

- Las notas (`.md`) y los adjuntos.
- La configuración compartida de `.obsidian/` (ajustes, plugins activos y apariencia).

El estado local de cada persona no se versiona (paneles abiertos, caché y papelera). Ver
`.gitignore`.
