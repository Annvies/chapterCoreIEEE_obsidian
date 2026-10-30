---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/OfficialSearchResults.test.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba OfficialSearchResults.test

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 18 casos de prueba (Vitest + Testing Library).

### Casos

- **OfficialSearchResults (RF-317, RF-321, RF-337, RF-340)**
  - muestra ruta, título enlazado en otra pestaña, fragmento, «Sin verificar» y estrategia
  - no interpreta el HTML del título
  - un Miembro no ve «Extraer ficha»; el nivel Editar sí y recibe el enlace
  - con nivel Editar, «Extraer ficha» entrega el enlace del resultado
  - resume los intentos con su estado y motivo
  - mientras busca anuncia solo las estrategias habilitadas, en orden
  - muestra el mensaje de error de la petición (RF-343)
- **OfficialSearchResults con el catálogo**
  - muestra la fecha del catálogo, su nombre y la marca «sin verificar»
  - avisa como texto si el catálogo es antiguo (RF-354)
  - avisa si no hubo coincidencias exactas (RF-353)
  - sin catálogo no muestra ningún aviso de catálogo
- **accesibilidad con teclado**
  - el enlace y «Extraer ficha» se alcanzan con Tab en orden
  - la región de resultados tiene un encabezado que la nombra
- **SearchHistory (RF-325, RF-341)**
  - muestra el estado vacío
  - lista la búsqueda con sus resultados enlazados; el enlace se abre con un clic (SC-005)
  - elimina una entrada y vacía todo tras confirmar
- **StrategySelector (RF-326, RF-327)**
  - no aparece fuera de desarrollo ni si el servidor no permite forzar
  - en desarrollo permite elegir una estrategia habilitada

## Enlaces

- [[M3 - OfficialSearchResults]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
