---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/OpportunitiesPage.test.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba OpportunitiesPage.test

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 8 casos de prueba (Vitest + Testing Library).

### Casos

- **OpportunitiesPage — búsqueda en fuentes oficiales (HU-10)**
  - con 2 vigentes ofrece la acción
  - con 3 vencidas también la ofrece
  - con 3 vigentes no la ofrece
  - sin texto de búsqueda no la ofrece
  - con todas las estrategias desactivadas no la ofrece
  - una nueva búsqueda reemplaza los resultados de fuentes oficiales (RF-339)
  - la región viva existe antes de buscar y anuncia el resultado (RF-337)
  - sin extracción con IA: ni el nivel Editar ve el panel ni «Extraer ficha»

## Enlaces

- [[M3 - OpportunitiesPage]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
