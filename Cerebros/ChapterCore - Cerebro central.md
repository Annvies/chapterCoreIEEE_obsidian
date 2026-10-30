---
type: central
estado: confirmado
fuentes:
  - CONTEXTO.md
  - backendChapterCoreIEEE/src/
  - frontendChapterCoreIEEE/src/
actualizado: 2026-10-30
aliases:
  - Mapa de cerebros
  - Cerebro central
tags:
  - chaptercore
  - cerebro-central
---

# ChapterCore — Cerebro central

**ChapterCore** es el sistema de gestión integral de la Rama Estudiantil IEEE (UPB) y sus
capítulos. Este cerebro central conecta los **siete cerebros especializados**, uno por
módulo del sistema: los seis del MVP y el del Módulo 7, ya en `main`. Cada cerebro tiene tres subgrupos y, debajo, notas de concepto
verificadas en el código.

> [!abstract] Estructura del conocimiento
> **Cerebro central** → 7 **cerebros de módulo** → 3 **subgrupos** cada uno → **conceptos**.
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

## Los siete cerebros especializados

| Módulo | Cerebro | De qué se ocupa |
|---|---|---|
| 1 | [[Cerebro 1 - Base institucional]] | Cuentas, cargos, niveles de acceso, matriz de permisos, catálogo de capítulos, perfil de membresía IEEE y aprobación de invitaciones |
| 2 | [[Cerebro 2 - Contactos]] | Directorio de empresas, alumni, conferencistas y autoridades, con su historial |
| 3 | [[Cerebro 3 - Oportunidades IEEE]] | Becas, concursos y voluntariados IEEE: búsqueda y búsqueda a petición en fuentes oficiales; la extracción con Gemini queda solo en el backend |
| 4 | [[Cerebro 4 - Difusión y QR]] | Enlaces cortos, QR dinámicos y conteo de visitas |
| 5 | [[Cerebro 5 - Secretaría y formularios]] | Formularios dinámicos versionados, respuestas y enlaces de Drive |
| 6 | [[Cerebro 6 - Feedback y KPIs]] | Dashboard: miembros, oportunidades, respuestas, satisfacción, NPS y escaneos QR, con alcance por capítulo |
| 7 | [[Cerebro 7 - Tesorería y Gastos]] | Gastos de la Rama y de cada capítulo y total gastado por periodo; código en `main`, aprobación formal pendiente en `CONTEXTO.md` |

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
> - **Módulo 4 → Módulo 6:** las visitas con origen QR se cuentan como escaneos en el
>   Dashboard.
> - **Módulo 2:** usa permisos y capítulos del Módulo 1; no alimenta el Dashboard.
> - **Módulo 1 y 2 → Módulo 7:** tesorería usa la matriz de permisos y el
>   catálogo de capítulos; no alimenta el Dashboard.

> [!warning] Integraciones pendientes
> - Escaneos QR en el Dashboard, alcance por capítulo del Director (PR #28) y enlaces de
>   Google Drive en formularios públicos (PR #27): **ya están en `main`** (PR #29).
> - Módulo 7, tesorería: **en `main`** desde el PR #31 (`607d4b8`), pero `CONTEXTO.md` aún
>   lo describe como propuesto; falta registrar la aprobación y la enmienda 2.1.0.
> - No existe un módulo de eventos (el Dashboard lo informa como no disponible).

## Cómo leer el grafo

- El grafo muestra solo la carpeta `Cerebros/` (filtro `path:"Cerebros/"`). Colores: central (dorado), Módulo 1
  naranja, 2 coral, 3 amarillo, 4 verde, 5 azul, 6 violeta, 7 turquesa.
- Los nodos grandes son los cerebros (más conexiones); los pequeños, conceptos.
- Vista espacial: `ChapterCore - Cerebros.canvas`.

## Fuentes

- Repositorio del producto: <https://github.com/marianZamorano/chapterCoreIEEE> (rama `main`).
- Las fuentes externas de cada cerebro (IEEE, NIST, Obsidian) son contexto, no evidencia
  de implementación.
