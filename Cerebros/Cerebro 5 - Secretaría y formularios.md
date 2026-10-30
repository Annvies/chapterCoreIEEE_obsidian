---
aliases:
  - Módulo 5
  - Secretaría y formularios
tags:
  - chaptercore
  - modulo-5
---

# Cerebro 5 — Secretaría y formularios dinámicos

Parte de [[ChapterCore - Cerebro central]] · cerebro especializado del Módulo 5

## Código

Documentación técnica: [[M5 - Código del módulo]] (endpoints, archivos, pantallas y pruebas).

## Subgrupos conectados

- [[M5 - Diseño de formularios]]
- [[M5 - Respuestas y versiones]]
- [[M5 - Datos y privacidad]]

> [!abstract] Propósito
> Dar a Secretaría herramientas para crear registros, postulaciones y encuestas sin
> programar una pantalla nueva para cada formulario. La estructura se almacena como
> datos y luego se representa para quien responde.

> [!info] Componentes descritos
> - **Definición:** título, descripción, URL pública y esquema JSON.
> - **Versionado:** nuevas versiones permiten preservar la estructura asociada a
>   respuestas anteriores.
> - **Campos:** texto, correo, número, selección, escala, fecha, enlace de Drive y
>   número de membresía IEEE. El tipo archivo queda solo para versiones ya publicadas
>   *(en `main` desde el PR #29, que integró el PR #27)*.
> - **Reglas:** visibilidad condicional y validaciones.
> - **Respuestas:** formularios publicados se pueden responder sin sesión; las
>   respuestas se pueden revisar, medir por estado y exportar a XLSX.
> - **Archivos:** se usa una abstracción de almacenamiento; la configuración local no
>   equivale necesariamente a persistencia adecuada en todos los despliegues. Desde el PR #27
>   (en `main` con el PR #29) ya no se guardan archivos nuevos: se piden enlaces de Google
>   Drive; los adjuntos históricos se conservan.

> [!success] Ciclo de vida conceptual
> 1. Preparar definición, campos y reglas.
> 2. Publicar una versión para recibir respuestas.
> 3. Conservar la relación entre cada respuesta y la versión de formulario que se
>    respondió.
> 4. Revisar resultados, métricas por estado y exportación.
> 5. Si se modifica el formulario, crear una versión nueva sin reinterpretar respuestas
>    antiguas según la estructura actual.
>
> Este ciclo resume capacidades descritas; los nombres de estados y reglas exactas de
> edición no se especificaron.

> [!tip] Contexto técnico: esquemas
> JSON Schema es un vocabulario para describir y validar documentos JSON: puede declarar
> tipos, propiedades y restricciones. Es útil como referencia conceptual para pensar en
> contratos de formulario y datos de respuesta. **ChapterCore valida actualmente con
> Zod; no debe describirse como una implementación de JSON Schema.**

> [!example] Por qué importa el versionado
> Si una encuesta publicada cambia de «capítulo» opcional a obligatorio, una respuesta
> recibida bajo la versión anterior debe interpretarse con las reglas que tenía al
> responderse. El versionado descrito busca conservar esa separación; este ejemplo
> explica el propósito, no un detalle interno de persistencia.

> [!warning] Seguridad, datos y adjuntos
> Hay hallazgos documentados sobre `submittedBy` y respuestas que incluyen campos fuera
> del esquema o campos ocultos. Debe verificarse que el servidor valida los datos
> recibidos y no confía únicamente en el formulario del navegador. Los adjuntos pueden
> contener datos personales: revisar autorización de descarga, almacenamiento,
> conservación y eliminación antes del despliegue.

> [!todo] Privacidad y calidad pendientes
> - Definir aviso/propósito, consentimiento cuando corresponda, retención y eliminación.
> - Verificar equivalencia entre validaciones frontend y backend.
> - ~~Evaluar el almacenamiento de archivos para el entorno de despliegue.~~ Propuesta:
>   enlaces de Drive (PR #27, en `main` con el PR #29).
> - Verificar el acceso a respuestas y archivos según los permisos.

## Conexiones

Usa permisos de [[Cerebro 1 - Base institucional]] para gestionar formularios y revisar
respuestas. [[Cerebro 4 - Difusión y QR]] puede difundir formularios publicados; sus
respuestas y escalas marcadas para KPI pueden alimentar
[[Cerebro 6 - Feedback y KPIs]].

## Fuentes externas

- [JSON Schema: Creating your first schema](https://json-schema.org/learn/getting-started-step-by-step):
  documentación oficial del estándar sobre descripción y validación de JSON.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework): marco voluntario
  de gestión de riesgos de privacidad, no certificación ni asesoría legal.
- [Callouts — ayuda oficial de Obsidian](https://obsidian.md/help/Editing+and+formatting/Callouts):
  formato de los subgrupos en color.
