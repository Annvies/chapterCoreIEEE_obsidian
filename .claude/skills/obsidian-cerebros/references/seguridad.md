# Seguridad

Ningún sistema con agentes es "totalmente seguro". El objetivo es que un error o
un contenido malicioso **no pueda causar daño sin que una persona lo apruebe**.

## Lecciones de incidentes reales con MCP

### 1. Inyección vía contenido no confiable — "toxic agent flow" (Invariant Labs, 2025)
<https://invariantlabs.ai/blog/mcp-github-vulnerability>

Un issue público con instrucciones ocultas hizo que un agente con el MCP de
GitHub leyera repositorios privados y publicara su contenido en un PR público. No
era un bug del servidor: el agente combinaba **tres cosas** a la vez:

1. **Contenido no confiable** (texto escrito por terceros),
2. **acceso a datos privados**,
3. **un canal de salida** (publicar, enviar, subir).

La alineación del modelo no bastó; hace falta control a nivel de sistema.

**Cómo aplica aquí:** notas de colaboradoras, comentarios de código, `docs/` o
páginas IEEE podrían contener instrucciones. `chaptercore-vault` no tiene canal de
salida, pero el agente puede tener otros (web, Drive, Trello, navegador, `git push`).

**Mitigaciones aplicadas**
- El MCP no tiene red, no ejecuta comandos y es de solo lectura por defecto.
- Las herramientas que devuelven contenido lo marcan como **datos no confiables**.
- `vault_lint` detecta frases típicas de inyección y secretos en todas las notas.
- `vault_write_note` rechaza contenido con forma de secreto o de inyección.
- La skill prohíbe usar canales de salida sin pedido explícito del usuario.
- `.claude/settings.json`: herramientas de lectura permitidas; escritura,
  `git commit`, `git push` y `WebFetch` **piden confirmación**; `.env` y claves denegados.
- **Registro de auditoría** local `.chaptercore-audit.log` (no versionado) con cada
  llamada al MCP.

**Lo que depende de ti**
- No uses "Permitir siempre" en herramientas que publican o envían (git push,
  Drive, Trello, navegador, correo).
- En sesiones de trabajo con los cerebros, desconecta los MCP externos que no
  necesites (`/mcp` en Claude Code).
- Revisa `git diff` antes de cada commit.

### 2. Servidor MCP malicioso en npm — `postmark-mcp` (Koi Security, sep 2025)
<https://www.thaicert.or.th/en/2025/10/01/researchers-discover-first-malicious-mcp-server-in-rogue-postmark-mcp-package-used-to-steal-user-emails/>

Un paquete npm que imitaba a uno legítimo añadió en la versión 1.0.16 **una sola
línea** que copiaba en BCC cada correo a un servidor del atacante (1.643
descargas). Lección: un MCP corre con tus privilegios; una actualización puede
volverlo malicioso.

**Cómo aplica aquí:** `chaptercore-vault` **no usa npm ni dependencias**; el
código está versionado en este repositorio y no se actualiza solo. El riesgo
equivalente es que alguien modifique `mcp/server.mjs`, `.mcp.json` u otras
configuraciones de agentes en el repositorio.

**Mitigaciones**
- Revisar en cada pull request cualquier cambio en `.claude/`, `.agents/`,
  `.mcp.json`, `.codex/`, `.gemini/`, `.vscode/`, `opencode.json`, `AGENTS.md`,
  `GEMINI.md` y `.github/`. Señales de alarma: `fetch`, `http`, `net`,
  `child_process`, `exec`, `spawn`, URLs nuevas o `eval`.
- Claude Code pide aprobar los servidores de `.mcp.json` del proyecto: no los
  apruebes si cambiaron y no sabes por qué.
- MCP de terceros: solo de fuentes oficiales, con versión fija (nunca `latest`),
  revisando el repositorio antes de actualizar.
- Lo mismo vale para **plugins de Obsidian**: no están aislados y pueden leer toda
  la bóveda y usar la red.

## Modelo de amenazas

| Riesgo | Mitigación |
|---|---|
| Filtrar secretos del producto (`.env`, `JWT_SECRET`, `GEMINI_API_KEY`, `DATABASE_URL`) | El MCP bloquea `.env*`, claves y certificados por nombre **y** redacta valores con forma de secreto dentro de cualquier archivo. Nombra la variable, nunca su valor |
| Datos personales en la bóveda | Datos ficticios o agregados; nada real de contactos o respuestas |
| Inyección de prompt en notas, código o web | Contenido marcado como no confiable; detección en `vault_lint`; la skill no obedece instrucciones leídas |
| Exfiltración por otros canales del agente | Sin canales de salida sin pedido explícito; confirmación para `git push` y `WebFetch` |
| Servidor MCP o plugin comprometido | Sin dependencias; revisión de cambios; versiones fijas en terceros |
| Agente que sobrescribe notas | Solo lectura por defecto; sin sobrescritura implícita; `git diff` antes de commit |
| Servidor local expuesto | Solo `127.0.0.1`; API keys en variables de entorno de usuario |
| Commits no autorizados | La skill nunca hace commit ni push sin permiso explícito |

## Riesgo residual (honesto)

- La detección de inyecciones usa patrones: una inyección bien disfrazada puede
  pasar. Por eso la defensa principal es **no tener canal de salida sin aprobación**.
- La redacción de secretos reconoce formatos comunes, no todos.
- Si alguien con permiso de escritura en el repositorio cambia el servidor y
  nadie lo revisa, las demás lo ejecutarán. La revisión humana es necesaria.

## Lista de comprobación antes de terminar

- [ ] `vault_lint` sin errores (incluye inyecciones y secretos).
- [ ] Ninguna nota contiene claves, tokens, contraseñas, URLs con credenciales ni
      datos personales reales.
- [ ] Toda afirmación nueva del producto tiene fuente.
- [ ] No se usó ningún canal de salida (web, Drive, push…) sin pedido explícito.
- [ ] Ningún cambio en `.obsidian/` desactiva core plugins o añade plugins sin acuerdo.
- [ ] No se hizo commit ni push sin autorización.
