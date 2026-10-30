---
type: decision
modulo: 3
estado: confirmado
fecha: 2026-10-30
fuentes:
  - CONTEXTO.md
  - specs/002-oportunidades-fuentes-oficiales/spec.md
  - frontendChapterCoreIEEE/src/api/opportunities.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - decision
---

# M3 - Retiro de la extracción en la interfaz

[[M3 - Extracción y revisión]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!info] Contexto
> La extracción con IA no funciona en producción: el alojamiento no tiene la clave del
> proveedor (`specs/002-oportunidades-fuentes-oficiales/spec.md`, «Después de integrar»).

> [!success] Decisión (2026-10-30, PR #43)
> Se quitaron del frontend el panel «Extraer convocatoria», la acción «Extraer ficha» de los
> resultados y del historial, el editor de ficha, su validación, sus hooks y sus pruebas.
> Quedan retirados los requisitos RF-321, RF-330 y RF-331 y la historia HU-13. Cada resultado
> de la [[M3 - Búsqueda en fuentes oficiales]] conserva solo el enlace a la página oficial.

> [!warning] Consecuencias
> - **Ya no se pueden publicar oportunidades desde la interfaz.** Las publicadas antes
>   siguen apareciendo en la búsqueda.
> - El backend no cambió: `POST /opportunities/extract` y `POST /opportunities` siguen
>   existiendo y exigiendo Editar, sin uso desde la interfaz.
> - `api/opportunities.ts` ahora solo busca, lista sociedades, busca en fuentes oficiales y
>   gestiona el historial.
> - La prueba E2E comprueba que no aparecen el panel ni «Extraer ficha».

> [!question] Por decidir
> Cómo se publicarán oportunidades nuevas. Las fuentes no registran alternativas
> evaluadas.

## Enlaces

- Forma parte de [[M3 - Extracción y revisión]].
- Relacionada con [[M3 - Extracción con Gemini]], [[M3 - Publicación y búsqueda]], [[M3 - Búsqueda en fuentes oficiales]].

## Fuentes

- `CONTEXTO.md` §7 («Retirado de la interfaz el 2026-10-30»)
- `specs/002-oportunidades-fuentes-oficiales/spec.md`
- Commit `18b8aa8` del producto, integrado con el PR #43 (`54d8d14`)
