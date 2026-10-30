---
type: concepto
modulo: 3
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/discovery.controller.ts
  - backendChapterCoreIEEE/src/opportunities/discovery/discovery.service.ts
  - backendChapterCoreIEEE/src/opportunities/discovery/discovery.types.ts
  - backendChapterCoreIEEE/src/opportunities/discovery/user-throttler.guard.ts
  - backendChapterCoreIEEE/src/opportunities/opportunities.module.ts
  - CONTEXTO.md
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - concepto
---

# M3 - Búsqueda en fuentes oficiales

[[M3 - Descubrimiento]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Qué es
> Cuando una búsqueda normal devuelve menos de 3 oportunidades vigentes publicadas, la
> interfaz ofrece **«Buscar en fuentes oficiales IEEE»**. El servidor recorre sitios
> oficiales **solo a petición de una persona**, nunca de forma programada, y devuelve
> enlaces **«sin verificar»** que nunca se publican solos (spec 002, `CONTEXTO.md` §7).

> [!info] Confirmado en el código
> - `POST /opportunities/discover` (acceso **Ver**: cualquier persona con sesión).
>   Cada resultado ofrece solo el enlace a la página oficial: la acción «Extraer ficha» se
>   retiró de la interfaz en el PR #43.
> - **Cascada** registrada en `opportunities.module.ts`: páginas oficiales estáticas →
>   navegador automatizado (solo en local) → [[M3 - Catálogo de respaldo]].
> - Presupuesto común: 15 s y 10 páginas por búsqueda (configurables con
>   `OPPORTUNITY_DISCOVERY_MAX_PAGES`), 5 s por página y 1 s reservado al catálogo.
> - Límite **por persona**, no por IP: 3 búsquedas por minuto
>   (`OPPORTUNITY_DISCOVERY_RATE_LIMIT`), en memoria y por instancia.
> - Los resultados pasan por `result-filter.ts` y la lista de
>   [[M3 - Fuentes oficiales admitidas]]; enlazan a la página, nunca a un archivo.
> - `GET /opportunities/discover/config` da a la interfaz la configuración, y
>   `GET /opportunities/official-domains` la lista verificada de dominios (desde el PR #43 la
>   interfaz ya no la consulta).

> [!warning] Estrategia declarada sin implementar
> El tipo `discovery_strategy` y `STRATEGY_NAMES` incluyen `busqueda_sitio` («Búsqueda del
> sitio»), pero el módulo solo registra las estrategias `estaticas`, `navegador` y
> `catalogo`. La IA con búsqueda web se descartó el 2026-10-30.

## Enlaces

- Forma parte de [[M3 - Descubrimiento]].
- Relacionada con [[M3 - Historial de búsquedas]], [[M3 - Búsqueda por palabras clave]], [[M3 - Descarga de la página]].

## Fuentes

- `backendChapterCoreIEEE/src/opportunities/discovery/` (controlador, servicio, tipos, estrategias y `user-throttler.guard.ts`)
- `backendChapterCoreIEEE/src/opportunities/opportunities.module.ts`
- `CONTEXTO.md` §7 · `specs/002-oportunidades-fuentes-oficiales/`
