---
aliases:
  - Módulo 6
  - Feedback y KPIs
tags:
  - chaptercore
  - modulo-6
---

# Cerebro 6 — Feedback, métricas y KPIs

Parte de [[ChapterCore - Cerebro central]] · cerebro especializado del Módulo 6

## Código

Documentación técnica: [[M6 - Código del módulo]] (endpoints, archivos, pantallas y pruebas).

## Subgrupos conectados

- [[M6 - Indicadores]]
- [[M6 - Periodos y filtros]]
- [[M6 - Lectura del feedback]]

> [!abstract] Propósito
> Resumir información operativa para apoyar decisiones de gestión. El Dashboard agrega
> datos originados por otros módulos: es una vista de lectura e interpretación, no el
> lugar donde se capturan contactos, oportunidades o respuestas.

> [!info] Indicadores y fuentes
> - **Actividad institucional:** integrantes activos desde
>   [[Cerebro 1 - Base institucional]].
> - **Oportunidades publicadas:** desde [[Cerebro 3 - Oportunidades IEEE]].
> - **Formularios, respuestas, satisfacción y feedback:** desde
>   [[Cerebro 5 - Secretaría y formularios]].
> - **Respuestas por estado, ranking de capítulos y feedback reciente:** resumen de
>   datos operativos.
> - **Visitas QR:** registradas en el Módulo 4. En `main` aún no llegan al Dashboard;
>   el PR #28 (pendiente de fusión) las cuenta como escaneos del periodo.
> - **Contactos:** el Módulo 2 conserva su operación de directorio; no se describe que
>   alimente indicadores aquí.

> [!success] Periodos y cálculos descritos
> Los periodos disponibles son mes (30 días), semestre (180 días) y gestión (histórico).
> El periodo filtra las respuestas y sus métricas derivadas; los conteos de integrantes,
> oportunidades, formularios y el ranking no se filtran por periodo.
>
> La satisfacción se calcula promediando muestras de campos `scale` marcados para KPI.
> El NPS es el porcentaje de promotores menos el porcentaje de detractores.

> [!example] Lectura del NPS
> La metodología Net Promoter clasifica las respuestas a una pregunta de recomendación
> de 0 a 10: detractores 0–6, pasivos 7–8 y promotores 9–10. La fórmula es:
>
> `NPS = % promotores - % detractores`
>
> El resultado se expresa como una puntuación entre -100 y +100. No es el promedio de
> las respuestas ni la misma métrica que el promedio de satisfacción de escalas.

> [!tip] Interpretar sin sobreafirmar
> Comparar periodos solo cuando se entiende qué datos entran en cada cálculo. Un cambio
> en el promedio de satisfacción y un cambio en NPS responden a métricas distintas.
> Para explicar una variación, revisar el feedback y los formularios de origen; no
> inferir una causa a partir del indicador aislado.

> [!warning] Cobertura y límites
> En `main` las métricas son globales para la Rama y las visitas QR no llegan a esta
> vista. El PR #28 (pendiente de fusión) aplica el alcance por capítulo al Director y
> cuenta los escaneos. La ventana temporal no afecta todos los conteos. Evitar presentar
> una métrica como completa si su fuente o periodo no está incluido.

> [!todo] Mejoras pendientes
> - ~~Aplicar el filtro por capítulo para el Director.~~ Resuelto en el PR #28
>   (pendiente de fusión).
> - ~~Definir si se integrarán visitas QR.~~ Integradas en el PR #28 (pendiente de
>   fusión); falta acordar cómo interpretarlas junto con otros indicadores.
> - Mantener visible el periodo y la cobertura real de cada KPI.
> - No añadir métricas de contactos sin una integración y definición explícitas.

## Conexiones

[[Cerebro 1 - Base institucional]] aporta integrantes y permisos;
[[Cerebro 3 - Oportunidades IEEE]] oportunidades; y
[[Cerebro 5 - Secretaría y formularios]] respuestas, escalas y feedback. Las
visitas QR de [[Cerebro 4 - Difusión y QR]] se integran en el PR #28, pendiente de
fusión.

## Fuentes externas

- [Measuring Your Net Promoter Score — Bain/Net Promoter System](https://www.netpromotersystem.com/about/measuring-your-net-promoter-score/):
  grupos 0–6, 7–8 y 9–10 y fórmula de cálculo NPS.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework): referencia
  voluntaria para identificar y gestionar riesgos de privacidad en el uso de datos.
- [Callouts — ayuda oficial de Obsidian](https://obsidian.md/help/Editing+and+formatting/Callouts):
  formato de los subgrupos visuales.
