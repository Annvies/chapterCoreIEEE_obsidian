---
type: concepto
modulo: 3
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/opportunities/opportunities.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - concepto
---

# M3 - Búsqueda por palabras clave

[[M3 - Descubrimiento]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Qué es
> La búsqueda interpreta la consulta sin IA: separa palabras, tipos y siglas.

> [!info] Confirmado en el código
> - Las siglas del catálogo (p. ej. «WIE») se convierten en filtro de capítulo.
> - Palabras como «becas», «scholarships», «concursos», «challenges» o «voluntariado» se convierten en filtro de tipo.
> - Se ignoran palabras vacías y las de menos de 3 letras; se usan hasta **8 términos**.
> - Devuelve hasta 50 resultados por defecto.

## Enlaces

- Forma parte de [[M3 - Descubrimiento]].
- Relacionada con [[M3 - Tipos de oportunidad]].

## Fuentes

- `backendChapterCoreIEEE/src/opportunities/opportunities.service.ts`
