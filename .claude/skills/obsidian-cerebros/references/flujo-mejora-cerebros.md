# Flujo para mejorar un cerebro

## 0. Preparación
- Confirma rutas con `vault_overview` (bóveda y repo encontrados).
- Si el repo no existe localmente, pide la ruta (o `git clone` con permiso del usuario).
- Pregunta el alcance solo si es ambiguo: un módulo, todos, o solo estructura.

## 1. Diagnóstico
- `vault_lint` → clasifica errores (bloquean), avisos (corregir) y sugerencias.
- `vault_overview` → huérfanas, enlaces rotos, notas por módulo.

## 2. Contexto del módulo
- `module_context(n)` → notas, pendientes abiertos y archivos de producto.
- Lee el cerebro y sus 3 subgrupos completos.
- Lee los archivos de producto en este orden: migraciones (modelo de datos) →
  `domain/` y `services/` (reglas) → `controllers/` y `dto/` (contrato y permisos)
  → frontend `features/` (lo que ve la persona) → `CONTEXTO.md` y `docs/`.
- `repo_search` para confirmar detalles concretos (límites, mensajes, enums).

## 3. Contraste (obligatorio)
Construye una tabla interna:

| Afirmación de la nota | Evidencia (ruta:línea) | Estado |
|---|---|---|
| … | … | confirmado / desactualizado / sin evidencia / contradicho |

- **Desactualizado o contradicho:** corrige y cita la fuente.
- **Sin evidencia:** mueve a `[!question]` o elimina si era especulación.
- **Pendiente que el código ya resuelve:** conviértelo en hecho confirmado.

## 4. Enriquecimiento
- Añade properties estándar (`type`, `modulo`, `estado`, `fuentes`, `actualizado`).
- Completa el callout `success` con el flujo real; añade Mermaid si aclara.
- Crea notas de concepto/decisión solo con respaldo (ver ideas en
  `chaptercore-mapa-codigo.md`), con su plantilla, y enlázalas desde el subgrupo.
- Conexiones entre módulos con verbo: "usa permisos de", "alimenta KPI de".
- Mantén las fuentes externas (IEEE, NIST, Obsidian) como contexto, no evidencia.

## 5. Estructura visual
- Canvas: añade las notas nuevas dentro del grupo del módulo; conexiones con `label`.
- Grafo: no hace falta tocarlo si la nota lleva `#modulo-N`.
- Bases: `templates/pendientes.base` → `Cerebros/Seguimiento.base` si aún no existe.

## 6. Verificación
- `vault_lint` sin errores; revisa avisos nuevos.
- Lista de `seguridad.md`.
- `git status` / `git diff --stat` para mostrar al usuario qué cambió.

## 7. Informe al usuario
- Qué se corrigió, qué se añadió (con fuentes), qué sigue pendiente y qué
  decisiones necesita el equipo.
- Pregunta si quiere commit (no lo hagas sin permiso).

## 8. Registro de auditoría (obligatorio si cambiaste archivos)
- Crea `Auditoria/AAAA-MM-DD - <Título corto>.md` desde `templates/auditoria.md`.
- Añade la fila al índice `Auditoria/README.md`, la más reciente arriba.
- Registra cantidades y rutas principales, no el contenido completo de cada nota.
- Si luego se hace commit con autorización, añade los hashes en `commits`.

## Criterios de calidad de un cerebro "senior"

- Cada afirmación del producto tiene fuente y estado.
- ≥ 3 enlaces salientes con contexto; 0 enlaces rotos; ninguna huérfana.
- Pendientes explícitos y accionables (quién decide, qué falta).
- Legible en 2 minutos: propósito arriba, detalle en subgrupos.
- Consistente con `CONTEXTO.md` y con los demás cerebros (sin contradicciones).
