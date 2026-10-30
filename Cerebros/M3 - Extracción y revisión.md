---
tags:
  - chaptercore
  - modulo-3
  - subgrupo
---

# Extracción y revisión de oportunidades

[[Cerebro 3 - Oportunidades IEEE]] · Preparación de fichas

> [!warning] Retirado de la interfaz (PR #43, 2026-10-30)
> El panel «Extraer convocatoria» y la acción «Extraer ficha» se quitaron del frontend porque
> la extracción con IA no funciona en producción (el alojamiento no tiene la clave del
> proveedor). Desde entonces **no se puede extraer ni publicar desde la interfaz**. El
> backend no cambió: `POST /opportunities/extract` y `POST /opportunities` siguen existiendo,
> sin uso desde la interfaz. Fuente: `CONTEXTO.md` §7 y `specs/002-oportunidades-fuentes-oficiales/spec.md`.

> [!abstract] Qué hace (backend)
> Desde una URL admitida, el backend obtiene contenido y Gemini propone una ficha con
> información de la convocatoria.

> [!info] Datos sugeridos
> Título, tipo, fecha límite, elegibilidad, beneficio, enlace y capítulo/sociedad.
> Pueden mostrarse advertencias si faltan datos o se necesita confirmación.

> [!success] Revisión humana
> La extracción es una propuesta. Una persona autorizada revisa los datos y decide si
> publica; el sistema no publica automáticamente la propuesta.

> [!warning] Verificar en la fuente
> La IA puede equivocarse u omitir detalles. Confirmar plazo, requisitos, beneficio y
> enlace en la página original.

## Enlaces

La URL admitida depende de la política de fuentes; tras la revisión, la ficha pasa a
[[M3 - Publicación y búsqueda]]. Los permisos se detallan en el cerebro principal del
Módulo 1.

## Notas del subgrupo

- [[M3 - Fuentes oficiales admitidas]]
- [[M3 - Descarga de la página]]
- [[M3 - Extracción con Gemini]]
- [[M3 - Retiro de la extracción en la interfaz]]
