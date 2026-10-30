---
aliases:
  - Mapa de cerebros
tags:
  - chaptercore
  - modulos
---

# ChapterCore — mapa de los seis cerebros

Este mapa conecta una nota de conocimiento por cada módulo de ChapterCore. Cada nota
distingue el alcance descrito de los límites y pendientes; no reemplaza la documentación
del producto ni convierte una función pendiente en una función disponible.

## Los seis módulos

1. **Módulo 1 — Base institucional, usuarios y permisos**. Subgrupos: Identidad y acceso; capítulos y sociedades; permisos compartidos.
2. **Módulo 2 — Contactos, empresas y exmiembros**. Subgrupos: Directorio; relaciones institucionales; seguimiento.
3. **Módulo 3 — Oportunidades IEEE**. Subgrupos: Descubrimiento; extracción y revisión; publicación y búsqueda.
4. **Módulo 4 — Difusión, webmaster y QR**. Subgrupos: Enlaces cortos; códigos QR; métricas de difusión.
5. **Módulo 5 — Secretaría y formularios**. Subgrupos: Diseño de formularios; respuestas y versiones; datos y privacidad.
6. **Módulo 6 — Feedback, métricas y KPIs**. Subgrupos: Indicadores; periodos y filtros; lectura del feedback.

> **Vista espacial:** abre [[ChapterCore - Cerebros.canvas]] para ver cada módulo en su propio grupo de color, con sus subgrupos colocados juntos y las dependencias importantes conectadas.

## Cómo leer los colores

El **Graph view** pinta las notas por módulo usando sus etiquetas `#modulo-1` a
`#modulo-6`: naranja, coral, amarillo, verde, azul y violeta. Cada módulo enlaza con
tres subgrupos y estos se conectan con notas relacionadas de otros módulos.

Para explorarlo, abre el panel **Grafo** de Obsidian. Si los colores no aparecen, abre
los ajustes del grafo → **Grupos**, añade o restablece los grupos por etiqueta, y
asegúrate de estar viendo el grafo de la bóveda y no el grafo local de una nota.
Los colores de los callouts dentro de las notas dependen del tema; el grafo usa los
grupos de color configurados en `.obsidian/graph.json`.

Consulta la [guía oficial del Graph view de Obsidian](https://obsidian.md/help/Plugins/Graph+view)
y la [guía oficial de callouts](https://obsidian.md/help/Editing+and+formatting/Callouts).

## Conexiones entre módulos

- **Módulo 1** proporciona la base transversal de integrantes, cargos, permisos y el
  catálogo de capítulos/sociedades que utilizan los demás módulos.
- **Módulo 2** usa los permisos y el catálogo del Módulo 1 para organizar contactos e
  interacciones. No se describe una integración directa con el Dashboard.
- **Módulo 3** usa autenticación y permisos del Módulo 1; las oportunidades publicadas
  alimentan un conteo del Módulo 6.
- **Módulo 4** usa permisos del Módulo 1 y puede difundir formularios publicados en el
  Módulo 5 mediante enlaces cortos y QR. Sus visitas aún no se integran en el Dashboard.
- **Módulo 5** usa permisos del Módulo 1, recopila respuestas y produce datos para el
  Módulo 6. El Módulo 4 puede enlazar sus formularios publicados.
- **Módulo 6** agrega datos de integrantes, oportunidades y formularios/feedback. Es una
  vista de indicadores, no sustituye las funciones operativas de los otros módulos.

## Nota sobre la fuente

Los seis cerebros se basan en la descripción funcional de los módulos. El Módulo 1 se
completó a partir de `CONTEXTO.md` §5 y del código de `backendChapterCoreIEEE/src/auth/`
del repositorio del producto (rama `main`): autenticación propia, cargos y ámbitos,
niveles de acceso, matriz oficial de permisos y catálogo `ieee_societies`.

Las referencias externas de cada nota son fuentes de contexto, no evidencia de que una
integración o función esté implementada en ChapterCore. Para las funciones del producto,
priorizar la documentación y el código del propio proyecto.
