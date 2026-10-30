# Plugins de IA para Obsidian (categoría AI)

Fuentes: directorio <https://community.obsidian.md/search?type=plugin&categories=ai>
(se renderiza con JavaScript; datos tomados del registro oficial
`obsidianmd/obsidian-releases` → `community-plugins.json` y
`community-plugin-stats.json`, 2026-10-29) y los README de cada repositorio.
Unos 1.000 plugins mencionan IA/LLM/MCP; aquí están los relevantes.

**Leyenda.** Costo: 🟢 gratis · 🟡 gratis + parte de pago · 🔴 de pago.
Privacidad: **Local** = no sale del equipo · **BYOK** = usa tu clave y envía el
contexto a ese proveedor · **Agente** = ejecuta procesos locales (Claude Code,
Codex…). ⚠️ = el directorio indica *"not manually reviewed by Obsidian staff"*.

## Recomendados para los cerebros (gratis, seguros, pocas limitaciones)

| Plugin (id) | Descargas | Costo | Privacidad | Para qué sirve aquí |
|---|---|---|---|---|
| **Smart Connections** (`smart-connections`) | 1,25 M | 🟡 núcleo gratis | **Local** (embeddings locales por defecto, sin API key, offline) | Descubrir notas relacionadas entre módulos y proponer enlaces que faltan |
| **Local REST API with MCP** (`obsidian-local-rest-api`) | 0,82 M | 🟢 MIT | Local (HTTPS 127.0.0.1:27124, API key) | Servidor MCP dentro de Obsidian para que cualquier agente edite notas (ver `mcp-opciones.md`) |
| **Copilot** (`copilot`) | 3,0 M | 🟡 gratis con BYOK; "Plus" de pago | BYOK / local con endpoints compatibles OpenAI; claves en Keychain | Chat con la bóveda y modo agente con Claude Code / Codex / OpenCode (escritorio). AGPL‑3.0 |
| **Local GPT** (`local-gpt`) + **AI Providers** (`ai-providers`) | 0,11 M / 66 k | 🟢 | **Local** con Ollama o LM Studio | Acciones de texto (resumir, reescribir) sin enviar nada fuera |
| **Smart Composer** (`smart-composer`) | 178 k | 🟢 | BYOK u Ollama | Chat con contexto de notas y ediciones en un clic |

## Otros útiles con matices

| Plugin | Costo | Nota |
|---|---|---|
| **Agent Client** (`agent-client`) ⚠️ | 🟢 | Chat con Claude Code, Codex, Gemini CLI… vía Agent Client Protocol. Muy útil para usar esta misma skill desde Obsidian; sin revisión manual |
| **Claudian** (`realclaudian`) ⚠️ | 🟢 | Embebe Claude Code/Codex en la bóveda. Sin revisión manual |
| **Text Generator** (`obsidian-textgenerator-plugin`) | 🟢 BYOK | Plantillas de generación; envía contexto al proveedor |
| **ChatGPT MD** (`chatgpt-md`) | 🟢 BYOK / Ollama | Chat dentro de una nota |
| **Gemini Scribe** (`gemini-scribe`) | 🟢 BYOK | Gemini con notas como contexto; la capa gratuita de la API de Google puede usar los datos para mejorar productos: no usar con datos personales |
| **Smart Lookup** (`smart-lookup`) | 🟢 | Búsqueda semántica (mismo autor que Smart Connections) |
| **Khoj** (`khoj`) | 🟡 | Autohospedado gratis; nube con planes |
| **InfraNodus AI Graph View** | 🔴/🟡 | Análisis de huecos en el grafo; servicio externo |
| **Note Companion** (`fileorganizer2000`) | 🔴 o autohospedado | Requiere suscripción o tu propia infraestructura |

Plugins MCP basados en Obsidian (alternativas a Local REST API):
**MCP Connector** (`mcp-tools-istefox`), **Semantic Notes Vault MCP**
(`semantic-vault-mcp`) ⚠️, **Vault as MCP** (`vault-as-mcp`) ⚠️,
**MCP Server** (`mcp-server`) ⚠️.

## Configuración recomendada (100 % gratis y local)

1. **Smart Connections** con el modelo local por defecto → panel de conexiones.
2. **Ollama** (gratis, local) + **Local GPT** para resumir o reescribir.
3. Agentes externos (Claude Code, Codex, OpenCode, Gemini CLI, Copilot) con esta
   skill y el MCP `chaptercore-vault`, que no necesita ningún plugin.
4. Si se quiere editar desde Obsidian: **Local REST API with MCP** solo en
   127.0.0.1, con la API key guardada fuera del repositorio.

## Reglas al recomendar plugins de IA

- Indica siempre: costo real, adónde van los datos y si está revisado manualmente.
- **Los plugins de Obsidian no están aislados**: tienen acceso a todos los archivos
  y, en escritorio, a la red y al sistema. Instala pocos y de autores conocidos.
- Nunca guardes API keys en notas ni en `.obsidian/plugins/*/data.json` versionado
  (añádelo a `.gitignore`); usa el Keychain de Obsidian.
- Las cifras de descargas cambian: vuelve a consultar el registro si importan.
