---
type: servicio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/discovery.service.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - servicio
---

# M3 - discovery.service

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Servicio
> Archivo de servicio del backend (`opportunities/discovery/discovery.service.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `DISCOVERY_STRATEGIES` | const | — |
| `DISCOVERY_SIGNAL_FACTORY` | const | Crea la señal del presupuesto total; inyectable para probar el límite sin esperar 15 s. |
| `SignalFactory` | type | — |
| `DiscoveryResponse` | interface | — |
| `DiscoveryConfig` | interface | Lo que necesita la interfaz (GET /opportunities/discover/config). |
| `DiscoveryService` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `getConfig()` | Promise<DiscoveryConfig> | — |
| `discover()` | — | — |


## Enlaces

- [[M3 - result-filter]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
