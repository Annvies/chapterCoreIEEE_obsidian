---
type: central
estado: confirmado
fuentes:
  - CONTEXTO.md
  - backendChapterCoreIEEE/src/
  - frontendChapterCoreIEEE/src/
actualizado: 2026-10-29
aliases:
  - Mapa de cerebros
  - Cerebro central
tags:
  - chaptercore
  - cerebro-central
---

# ChapterCore — Cerebro central

**ChapterCore** es el sistema de gestión integral de la Rama Estudiantil IEEE (UPB) y sus
capítulos. Este cerebro central conecta los **seis cerebros especializados**, uno por
módulo del sistema. Cada cerebro tiene tres subgrupos y, debajo, notas de concepto
verificadas en el código.

> [!abstract] Estructura del conocimiento
> **Cerebro central** → 6 **cerebros de módulo** → 3 **subgrupos** cada uno → **conceptos**.
> Cada cerebro tiene además una nota **«MN - Código del módulo»** con la documentación
> técnica: endpoints y permisos, archivos de backend y frontend, pruebas y diagrama de flujo.
> Las relaciones entre módulos se expresan entre cerebros; los subgrupos y conceptos
> solo enlazan dentro de su módulo, para que cada cerebro forme su propio racimo en el grafo.

## Conocimiento transversal

Nodos propios del cerebro central, agrupados por tema:

- [[CC - Arquitectura y stack]] — Cómo está construido ChapterCore: backend, frontend, base de datos, dependencias, variables y scripts.
- [[CC - Seguridad transversal]] — Controles de seguridad que aplican a todos los módulos.
- [[CC - Despliegue e integración continua]] — Entornos, CI/CD con GitHub Actions y producción en Neon y Vercel.
- [[CC - Diseño e interfaz]] — Mockups oficiales, paleta IEEE, navegación y componentes compartidos.
- [[CC - Proyecto y equipo]] — Equipo, alcance, fuentes de verdad, decisiones, pendientes y reglas del proyecto.

## Los seis cerebros especializados

| Módulo | Cerebro | De qué se ocupa |
|---|---|---|
| 1 | [[Cerebro 1 - Base institucional]] | Cuentas, cargos, niveles de acceso, matriz de permisos y catálogo de capítulos |
| 2 | [[Cerebro 2 - Contactos]] | Directorio de empresas, alumni, conferencistas y autoridades, con su historial |
| 3 | [[Cerebro 3 - Oportunidades IEEE]] | Becas, concursos y voluntariados IEEE con extracción asistida por Gemini |
| 4 | [[Cerebro 4 - Difusión y QR]] | Enlaces cortos, QR dinámicos y conteo de visitas |
| 5 | [[Cerebro 5 - Secretaría y formularios]] | Formularios dinámicos versionados, respuestas y adjuntos |
| 6 | [[Cerebro 6 - Feedback y KPIs]] | Dashboard: miembros, oportunidades, respuestas, satisfacción y NPS |

> [!info] Arquitectura del producto
> - Backend NestJS + PostgreSQL en `backendChapterCoreIEEE/`; frontend React en
>   `frontendChapterCoreIEEE/`.
> - Decisiones confirmadas del equipo en `CONTEXTO.md`; mockups en `mockups/png/`.
> - Las carpetas `backend/`, `frontend/`, `fullstack/`, `DevOps/`, `QA/` y `uiux/` son
>   herramientas de apoyo, no el producto.

## Cómo se relacionan los cerebros

> [!success] Flujos entre módulos
> - **Módulo 1 → todos:** aporta identidad, nivel de acceso y el catálogo de capítulos.
> - **Módulo 3 → Módulo 6:** las oportunidades publicadas se cuentan en el Dashboard.
> - **Módulo 5 → Módulo 6:** respuestas, escalas `useInKpis` y comentarios alimentan
>   satisfacción, NPS y feedback reciente.
> - **Módulo 4 → Módulo 5:** los enlaces cortos y QR difunden formularios publicados.
> - **Módulo 2:** usa permisos y capítulos del Módulo 1; no alimenta el Dashboard.

> [!warning] Integraciones pendientes
> - Las visitas QR del Módulo 4 aún no llegan al Dashboard.
> - El filtro por capítulo del Director de capítulo aún no se aplica.
> - No existe un módulo de eventos (el Dashboard lo informa como no disponible).

## Cómo leer el grafo

- El grafo muestra solo la carpeta `Cerebros/` (filtro `path:"Cerebros/"`). Colores: central (dorado), Módulo 1
  naranja, 2 coral, 3 amarillo, 4 verde, 5 azul, 6 violeta.
- Los nodos grandes son los cerebros (más conexiones); los pequeños, conceptos.
- Vista espacial: `ChapterCore - Cerebros.canvas`.

## Fuentes

- Repositorio del producto: <https://github.com/marianZamorano/chapterCoreIEEE> (rama `main`).
- Las fuentes externas de cada cerebro (IEEE, NIST, Obsidian) son contexto, no evidencia
  de implementación.
