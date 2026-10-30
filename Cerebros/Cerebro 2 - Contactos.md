---
aliases:
  - Módulo 2
  - Contactos
tags:
  - chaptercore
  - modulo-2
---

# Cerebro 2 — Contactos, empresas y exmiembros

Parte de [[ChapterCore - Cerebro central]] · cerebro especializado del Módulo 2

## Código

Documentación técnica: [[M2 - Código del módulo]] (endpoints, archivos, pantallas y pruebas).

## Subgrupos conectados

- [[M2 - Directorio]]
- [[M2 - Relaciones institucionales]]
- [[M2 - Seguimiento]]

> [!abstract] Propósito
> Mantener en un solo lugar las relaciones de la Rama con personas y organizaciones,
> junto con el contexto necesario para continuar una conversación o colaboración. El
> directorio permite consultar quién es el contacto, qué relación tiene con la Rama y
> qué seguimiento se ha registrado.

> [!info] Grupos de información del contacto
> - **Personas y organizaciones:** empresas, exmiembros/alumni, conferencistas y
>   autoridades.
> - **Relación:** patrocinador, en negociación, prospecto o exaliado.
> - **Contexto:** datos de contacto, sector, ciudad, convenio, vencimiento y capítulo
>   asociado.
> - **Historial:** llamadas, correos, reuniones, eventos y notas.
>
> El capítulo asociado sirve como dato y filtro; según la descripción recibida, no
> restringe el acceso al contacto.

> [!success] Funciones descritas
> - Filtrado del directorio.
> - Importación CSV con validación por filas y resultado de importación total o nulo.
> - Acciones y visibilidad según cargo. Los directores de capítulo pueden ver todo el
>   directorio.
> - «Enviar correo» abre el programa de correo del dispositivo; ChapterCore no envía
>   el mensaje.

> [!example] Flujo de uso ilustrativo
> 1. Registrar una organización o persona y clasificar la relación.
> 2. Asociarla al capítulo correspondiente si aplica.
> 3. Añadir una interacción cuando ocurre un seguimiento.
> 4. Consultar el historial antes de retomar el contacto.
>
> Es un flujo de trabajo sugerido a partir de las funciones descritas, no una secuencia
> obligatoria impuesta por la aplicación.

> [!tip] Calidad de los registros
> Para facilitar búsquedas e importaciones, conviene acordar formatos consistentes
> para nombres de organizaciones, correos, ciudades, sectores y fechas de vencimiento.
> Antes de importar, revisar encabezados y errores por fila. Estas son recomendaciones
> operativas; no se ha descrito un detector automático de duplicados.

> [!warning] Privacidad y uso responsable
> El directorio contiene datos personales y de relación institucional. Definir qué
> información se recoge, con qué propósito, quién la consulta y cuánto tiempo se
> conserva antes de ampliar su uso. El NIST Privacy Framework es una herramienta
> voluntaria para identificar y gestionar riesgos de privacidad; no sustituye asesoría
> legal ni demuestra cumplimiento normativo.

> [!todo] Límites y decisiones pendientes
> - Los grupos configurables de visibilidad siguen pendientes.
> - No se describe detección de duplicados ni exportación del directorio.
> - No hay almacenamiento persistente definido para logos de empresas.
> - Definir privacidad, conservación y eliminación de datos.
> - Mantener claro que la acción de correo abre un cliente local, no envía desde
>   ChapterCore.
> - **Hallazgo (2026-10-30):** el historial rechaza fechas futuras comparando con
>   «hoy» en **UTC** (`todayIso` en `contacts/domain/contact.ts`). En Bolivia (UTC−4),
>   después de las 20:00 se acepta la fecha del día siguiente. No rechaza fechas válidas.

> [!success] Verificado de punta a punta (2026-10-30)
> Contra PostgreSQL local con las cuentas de prueba, 49 comprobaciones sin fallas:
> permisos por nivel (Miembro sin acceso, Director solo lectura, Secretaría edita e
> importa, solo Mesa borra), alta con capítulo y validaciones, conteos y filtros (tipo,
> texto, estado, capítulo, sector, último contacto), historial (rechaza fechas futuras;
> una interacción antigua no retrocede el último contacto), edición que reemplaza
> campos y conserva el historial, importación CSV (`;`, capítulo por sigla, todo o
> nada con errores por fila) y borrado. Pruebas unitarias: backend 23/23 y frontend 7/7.
> Detalle en [[2026-10-30 - Cerebros M1 y M2 membresía IEEE]].

## Conexiones

Usa cargos/permisos y el catálogo compartido de
[[Cerebro 1 - Base institucional]]. No se describe integración directa de contactos con
el Dashboard del Módulo 6.

## Fuentes externas

- [IEEE Student Branch Resources](https://students.ieee.org/student-branch-resources-2/):
  recursos de apoyo de ramas y comités regionales.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework): marco voluntario
  para ayudar a identificar y gestionar riesgos de privacidad.
- [Callouts — ayuda oficial de Obsidian](https://obsidian.md/help/Editing+and+formatting/Callouts):
  formato de los grupos de colores.
