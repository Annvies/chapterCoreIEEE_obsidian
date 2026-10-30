---
type: auditoria
fecha: 2026-10-29
agente: Claude Code (Opus 5.5)
solicitado_por: Marian Zamorano
rama: feat/skill-obsidian-cerebros
commits:
  - 4d1f6c7
  - 895f7d8
  - 9a2508f
  - 2a53a79
  - 8ecdd57
  - db3aa23
  - adfb99b
  - 5c2b295
  - d54886d
  - 53cb8da
  - 5ca87d5
  - a6f7136
  - f9c2713
tags:
  - auditoria
---

# 2026-10-29 — Skill obsidian-cerebros y reestructuración de los cerebros

> [!note] Registro retroactivo
> Se redactó al crear el sistema de auditoría; resume el trabajo hecho ese mismo día
> sobre el commit `cb5375c`.

## Pedido

Completar lo que faltaba en la bóveda, crear una skill experta en Obsidian usable por
varios agentes (con MCP gratuito y seguro), y reestructurar los cerebros para que haya un
cerebro central con seis cerebros especializados, cada uno con más detalle del código.

## Qué se hizo

| Área | Cambio | Archivos |
|---|---|---|
| Cerebros | Módulo 1 completado con datos verificados (antes provisional) | 4 notas |
| Cerebros | "Mapa de cerebros" pasa a **ChapterCore - Cerebro central** (alias conservado); cada cerebro enlaza al central | 8 |
| Cerebros | 36 notas de concepto; subgrupos sin enlaces cruzados entre módulos | 54 |
| Cerebros | Nota "Código del módulo" por cerebro | 6 |
| Cerebro central | 5 grupos transversales y 34 notas propias (stack, seguridad, despliegue, diseño, proyecto) | 39 |
| Mapa técnico | 238 notas generadas desde el código (endpoints, DTO, tablas, backend, interfaz, pruebas) en 35 grupos | 273 |
| Skill | `obsidian-cerebros`: SKILL.md, 12 referencias, plantillas, mapeador del repositorio | ~20 |
| MCP | Servidor `chaptercore-vault` sin dependencias ni red, solo lectura por defecto; 11 herramientas | 1 |
| Seguridad | Redacción de secretos, detección de inyecciones, auditoría local de llamadas, permisos en `.claude/settings.json` | 3 |
| Agentes | Configuración para Claude Code, Codex, OpenCode, Gemini CLI y Copilot | 9 |
| Obsidian | Colores del grafo por módulo, filtro `path:"Cerebros/"`, canvas por grupos, archivos excluidos | 3 |

## Fuentes consultadas

- `CONTEXTO.md` (§2–§10) y `mockups/README.md` del repositorio del producto.
- `backendChapterCoreIEEE/src/` (controladores, servicios, dominio, DTO, migraciones).
- `frontendChapterCoreIEEE/src/` (`App.tsx`, features, hooks, api, lib, types, pruebas).
- `.github/workflows/` y `package.json` de ambos proyectos.
- Externas: docs.obsidian.md, roadmap de Obsidian, registro `obsidianmd/obsidian-releases`,
  artículos de Invariant Labs y ThaiCERT sobre seguridad MCP.

## Verificación

- Lint final: 0 errores, 0 avisos, 14 sugerencias (pendientes abiertos de las notas).
- 380 notas, 0 enlaces rotos; 93 % de los enlaces dentro de su propio racimo.
- 42 de 45 endpoints vinculados con su cliente del frontend.
- Pruebas del MCP: bloqueo de `.env`, `node_modules`, rutas fuera de la bóveda, carpetas
  ocultas y sobrescritura; redacción de secretos; detección de una nota trampa.

## Hallazgos y correcciones

- Las oportunidades solo tienen tipos `beca`, `concurso` y `voluntariado` (las notas decían
  "premios y grants"); corregido en Cerebro 3 y M3 - Descubrimiento.
- `GET /users/:id` existe en el backend pero el frontend no lo usa.
- El mensaje del Dashboard dice que el módulo de difusión "no está implementado", aunque
  ya existe; lo pendiente es la integración de visitas QR.
- `graph.json` no estaba versionado y no tenía colores, aunque el Mapa los describía.

## Pendiente o por decidir

- Revisión del pull request por el equipo antes de unir a `main`.
- Decisiones del producto listadas en `CC - Pendientes del proyecto` (filtro por capítulo,
  privacidad y retención de datos, módulo de eventos, entre otras).
