---
aliases:
  - Módulo 1
  - Base institucional
tags:
  - chaptercore
  - modulo-1
---

# Cerebro 1 — Base institucional, usuarios y permisos

## Subgrupos conectados

- [[M1 - Identidad y acceso]]
- [[M1 - Capítulos y sociedades]]
- [[M1 - Permisos compartidos]]

> [!abstract] Identidad y estructura
> Este módulo representa la base transversal de ChapterCore: integrantes, cargos y
> permisos, además del catálogo compartido de capítulos y sociedades. Los demás módulos
> necesitan distinguir quién realiza una acción, qué está autorizado a hacer y, cuando
> corresponde, a qué unidad institucional se asocia el registro.
>
> **Estado del conocimiento:** la descripción recibida solo menciona estas capacidades
> como dependencias; no proporciona un inventario funcional completo del Módulo 1.

> [!info] Superficies que dependen de la base
> - **Contactos:** utiliza cargos/permisos y el catálogo de capítulos; la pertenencia
>   de un contacto a un capítulo es dato y filtro, no restricción de acceso.
> - **Oportunidades:** requiere sesión y permisos diferenciados para buscar, extraer y
>   publicar; las fichas también pueden asociarse a capítulo/sociedad.
> - **Difusión:** requiere permisos para administrar enlaces y consultar estadísticas;
>   las redirecciones públicas no son una acción de administración.
> - **Secretaría:** los formularios publicados admiten respuestas sin sesión, mientras
>   su gestión y revisión requieren permisos.
> - **KPIs:** el Dashboard informa integrantes activos y considera permisos del sistema.

> [!success] Relación con el sistema
> El módulo funciona como una dependencia compartida, no como una pantalla aislada:
> autenticar o identificar a una persona es distinto de autorizar cada operación.
> La lista anterior es el comportamiento indicado para los módulos que lo consumen,
> no una especificación de cómo se implementa el control de acceso.

> [!tip] Contexto institucional IEEE
> IEEE describe las ramas estudiantiles como comunidades que conectan estudiantes,
> profesorado y profesionales, y enumera actividades técnicas, sociales, de extensión y
> oportunidades regionales. IEEE Region 9 SAC sitúa su trabajo en el desarrollo
> académico, profesional y de liderazgo de estudiantes en Latinoamérica y el Caribe.
> Este contexto puede orientar el vocabulario del catálogo; no determina los cargos,
> permisos ni estructura que ChapterCore implementa.

> [!example] Ejemplo de relación entre datos
> Una oportunidad podría asociarse a una sociedad; un contacto, a un capítulo; y una
> respuesta de formulario, a quien la revisa. Son ejemplos de relaciones posibles en
> las superficies descritas, no afirmaciones sobre el esquema de base de datos.

> [!warning] No confundir sesión con autorización
> Que una página requiera iniciar sesión no implica que todos los usuarios puedan
> editarla. Mantener diferenciadas lectura, creación, edición, publicación,
> administración y consulta de métricas es una recomendación para documentar la matriz
> real; los permisos concretos del Módulo 1 aún no se proporcionaron.

> [!question] Detalles que faltan
> Confirmar el ciclo de autenticación, los cargos existentes, la matriz de permisos,
> alta/baja de integrantes, gestión de sesiones, catálogo de capítulos/sociedades,
> pertenencia a múltiples unidades y reglas para cambios históricos.

> [!todo] Pendiente para completar este cerebro
> Incorporar la documentación del Módulo 1 y reemplazar las preguntas abiertas por
> reglas confirmadas. No inventar nombres de cargos ni permisos para rellenar vacíos.

## Conexiones

Es una dependencia de [[Cerebro 2 - Contactos]], [[Cerebro 3 - Oportunidades IEEE]],
[[Cerebro 4 - Difusión y QR]], [[Cerebro 5 - Secretaría y formularios]] y
[[Cerebro 6 - Feedback y KPIs]]. El Dashboard informa integrantes activos.

## Fuentes externas de contexto

- [IEEE Student Branches](https://students.ieee.org/student-branches/): propósito y
  actividades generales de las ramas estudiantiles.
- [IEEE Region 9 SAC](https://r9.ieee.org/sac/): misión y acciones del comité de
  actividades estudiantiles regional.
- [Callouts — ayuda oficial de Obsidian](https://obsidian.md/help/Editing+and+formatting/Callouts):
  formato de los subgrupos visuales de esta nota.

Estas fuentes describen contexto institucional, no la implementación de ChapterCore.
