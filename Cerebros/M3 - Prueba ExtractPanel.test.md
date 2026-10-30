---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/opportunities/ExtractPanel.test.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba ExtractPanel.test

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 8 casos de prueba (Vitest + Testing Library).

### Casos

- **ExtractPanel**
  - valida la URL antes de llamar al backend
  - muestra advertencias, exige el tipo y publica solo los campos de la ficha
  - muestra el 409 del backend como error de publicación y lo limpia al editar
  - sin extracción muestra los pasos y un ejemplo de ficha, sin bloque JSON
  - muestra la ficha como tarjeta legible con cada aviso junto a su campo
  - rechaza en la interfaz una URL con usuario o con otro puerto (H-15)
  - «Extraer ficha» carga la URL y lleva el foco al campo sin extraer
  - muestra el mensaje del backend cuando falla la extracción

## Enlaces

- [[M3 - ExtractPanel]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
