# Desarrollo y evaluación de plugins (docs.obsidian.md)

Fuente: <https://docs.obsidian.md/Home> (repositorio
<https://github.com/obsidianmd/obsidian-developer-docs>). Secciones: **Plugins**
(Build a plugin, Submit your plugin, referencia de API), **Themes** (Build a
theme, Submit, CSS variables), **Community directory** (Set up and claim,
Developer policies, Organizations) y comunidad (Discord `#plugin-dev` y
`#theme-dev`, foro Developers & API).

Úsalo para dos cosas: **evaluar** si un plugin de terceros es seguro y bien hecho,
y **escribir** un plugin propio si algún día los cerebros lo necesitan (casi nunca:
primero core plugins, Bases, CLI o MCP).

## Anatomía

- Plugin = clase que extiende `Plugin` (de `obsidian`), escrita en TypeScript.
- `onload()`: registra comandos (`addCommand`), vistas (`registerView`), eventos
  (`registerEvent`), pestaña de ajustes (`addSettingTab`), extensiones de editor.
- `onunload()`: libera recursos. Lo registrado con `register*` se limpia solo.
- Archivos distribuidos: `main.js`, `manifest.json` (`id`, `name`, `version`,
  `minAppVersion`, `description`, `author`, `authorUrl`, `isDesktopOnly`,
  `fundingUrl`) y opcionalmente `styles.css`. Se instalan en
  `.obsidian/plugins/<id>/`; activos listados en `.obsidian/community-plugins.json`.
- API clave: `app.vault` (archivos), `app.metadataCache` (enlaces, etiquetas,
  frontmatter ya analizados), `app.workspace` (vistas y hojas),
  `app.fileManager` (renombrar actualizando enlaces, `processFrontMatter`).

## Guías oficiales (lo que distingue un plugin bien hecho)

**Seguridad**
- No usar `innerHTML`/`outerHTML`/`insertAdjacentHTML` con datos de usuario;
  construir DOM con `createEl()`, `createDiv()`, `createSpan()`; vaciar con `el.empty()`.

**Recursos y ciclo de vida**
- Usar `registerEvent()`/`addCommand()` para limpieza automática.
- No hacer `detach` de hojas en `onunload`.

**Vault**
- Editar la nota activa con la API `Editor`, no con `Vault.modify()`.
- Ediciones en segundo plano con `Vault.process()` (atómico).
- Frontmatter con `FileManager.processFrontMatter()`, nunca a mano.
- Preferir la API Vault sobre `vault.adapter` (caché y operaciones en serie).
- Buscar por ruta con `getFileByPath()` / `getFolderByPath()`, no recorriendo todo.
- `normalizePath()` para rutas construidas o del usuario.

**Workspace y editor**
- No usar `workspace.activeLeaf`; usar `getActiveViewOfType(MarkdownView)` o
  `workspace.activeEditor?.editor`.
- No guardar referencias a vistas propias; usar `getLeavesOfType()`.
- Cambios en extensiones del editor: mutar el mismo array y `workspace.updateOptions()`.

**Comandos y UI**
- Sin atajos de teclado por defecto. `callback` / `checkCallback` /
  `editorCallback` / `editorCheckCallback` según el caso.
- Texto en *sentence case*; ajustes sin encabezado superior ni la palabra
  "settings"; encabezados con `new Setting(el).setName(…).setHeading()`.

**Estilo y código**
- Sin estilos en línea: clases CSS y variables CSS de Obsidian.
- No usar el global `app`; usar `this.app`. Consola limpia (solo errores).
- `const`/`let`, `async/await` con `try/catch`.

## Lista de evaluación de un plugin de terceros

1. ¿Está en el directorio oficial? ¿Dice *"not manually reviewed by Obsidian
   staff"*? (El directorio de la comunidad, desde mayo de 2026, usa revisión
   automatizada; la revisión manual es una garantía adicional.)
2. Licencia (MIT/GPL/AGPL = abierto; "source available" = leer restricciones).
3. ¿Accede a la red? ¿A qué servicios? ¿Telemetría? ¿Requiere cuenta o pago?
4. ¿`isDesktopOnly`? ¿Ejecuta procesos locales (agentes, terminal)?
5. Mantenimiento: últimos lanzamientos, issues abiertos, descargas.
6. Dónde guarda claves: lo correcto es el **Keychain** de Obsidian (v1.11).
