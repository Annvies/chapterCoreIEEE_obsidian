---
type: auditoria
fecha: 2026-10-29
agente: Claude Code (Opus 5.5)
solicitado_por: Marian Zamorano
rama: feat/skill-obsidian-cerebros
commits: []
tags:
  - auditoria
---

# 2026-10-29 — README y registro de auditoría

## Pedido

Que cada ejecución de la skill deje un archivo que explique los cambios, para auditoría,
y que el `README.md` explique primero la bóveda, los cerebros y su estructura, dejando la
skill al final.

## Qué se hizo

| Área | Cambio | Archivos |
|---|---|---|
| Documentación | `README.md` reescrito: qué es la bóveda, niveles de la estructura, cerebro central, cerebros de módulo, grupos, tipos de nota, convenciones y navegación; la skill al final | 1 |
| Auditoría | Carpeta `Auditoria/` con índice y dos registros (este y uno retroactivo) | 3 |
| Skill | Regla 9 y paso 8 del flujo: registro obligatorio cuando se cambian archivos; plantilla `auditoria.md` | 3 |
| Agentes | `AGENTS.md` incluye la regla de auditoría para Codex, OpenCode, Gemini y Copilot | 1 |

## Fuentes consultadas

- Estado actual de la bóveda (`vault_overview`, `vault_lint`) y notas del cerebro central.

## Verificación

- Lint: 0 errores, 0 avisos.
- `Auditoria/` queda fuera del grafo (filtro `path:"Cerebros/"`).

## Hallazgos y correcciones

- Ninguno.

## Pendiente o por decidir

- Hacer commit de estos cambios cuando se autorice.
