---
type: servicio
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/search-history.service.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - servicio
---

# M3 - search-history.service

[[M3 - Lógica del backend]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Servicio
> Historial de búsquedas en fuentes oficiales (spec 002, RF-323 a RF-325). El texto buscado es dato personal: solo lo ve y lo borra su dueño.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `MAX_HISTORY` | const | Búsquedas que se conservan por persona (D2). |
| `SearchHistoryEntry` | interface | — |
| `SearchHistoryService` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `save()` | Promise<string> | Guarda la búsqueda y poda a las 50 más recientes de esa persona en una sola transacción. |
| `list()` | Promise<SearchHistoryEntry[]> | — |
| `remove()` | Promise<boolean> | Elimina una entrada propia; false si no existe o es de otra persona. |
| `clear()` | Promise<void> | — |


## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
