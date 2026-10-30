---
type: dominio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/discovery.types.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - dominio
---

# M3 - discovery.types

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Dominio
> Tipos de la búsqueda en fuentes oficiales IEEE (spec 002, data-model.md y contracts/api-rest.md).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `STRATEGY_NAMES` | const | Estrategias en el orden de la cascada (RF-311). La IA con búsqueda web se descartó el 2026-10-30 (spec 002, Clarifications). Ciclo 2: búsqueda propia del sitio primero y catálogo de respaldo al final (RF-350, RF-357). |
| `StrategyName` | type | — |
| `LIVE_STRATEGIES` | const | Estrategias que leen sitios en vivo; el catálogo responde sin red (RF-351). |
| `STRATEGY_LABELS` | const | Nombres que ve la persona usuaria (RF-317). |
| `CatalogMeta` | interface | Datos del catálogo que acompañan a sus resultados (RF-352 a RF-354). |
| `AttemptStatus` | type | — |
| `DiscoveryTerms` | interface | Consulta interpretada: texto original más palabras, tipos y siglas (RF-305, RF-336). |
| `PageBudget` | class | Máximo común de páginas que puede descargar una búsqueda entre todas las estrategias (RF-322). |
| `StrategyError` | class | Fallo de una estrategia con un mensaje apto para la persona usuaria (motivo del intento). Cualquier otro error se informa con un mensaje genérico: nunca se muestran detalles internos. |
| `DiscoveryContext` | interface | Lo que cada estrategia recibe de la cascada. |
| `timeLeft` | function | Milisegundos que quedan hasta el margen de cierre (Infinity si no hay). |
| `DiscoveryCandidate` | interface | Enlace encontrado por una estrategia, antes de filtrarlo (result-filter.ts). |
| `StrategyOutput` | interface | — |
| `DEFAULT_PAGE_TIMEOUT_MS` | const | Tiempo máximo por página dentro del presupuesto común (spec 002, RF-356). |
| `readPageTimeout` | function | — |
| `DiscoveryStrategy` | interface | — |
| `DiscoveryAttempt` | interface | — |
| `DiscoveryResult` | interface | Resultado ya validado que se muestra y se guarda en el historial. |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `take()` | boolean | Reserva una página; devuelve false si ya no quedan. |
| `habilitada()` | boolean \| Promise<boolean>; | — |
| `buscar()` | Promise<StrategyOutput>; | — |


## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
