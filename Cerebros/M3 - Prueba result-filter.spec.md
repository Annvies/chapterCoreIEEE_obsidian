---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/discovery/result-filter.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba result-filter.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 17 casos de prueba (Jest).

### Casos

- **filterResults**
  - acepta un resultado oficial y relacionado con ruta, fragmento y estrategia
  - sustituye un PDF por la página que lo contiene (RF-319)
  - descarta un archivo cuya página se desconoce
  - trata como archivo un tipo de contenido que no es una página web
  - descarta duplicados con otra forma de URL (RF-320)
  - descarta lo que ya está publicado como enlace o fuente
  - descarta resultados sin relación con la búsqueda (RF-336)
  - cuenta la sigla y el tipo que nombra la búsqueda
  - compara sin distinguir tildes ni mayúsculas
  - muestra título y fragmento como texto plano y recorta el fragmento a 200 caracteres
  - ordena por coincidencias y devuelve como máximo 20
- **filterResults en modo «recientes»**
  - acepta entradas sin palabras de la búsqueda y conserva su orden
  - mantiene los descartes de dominio, archivos y duplicados (RF-318 a RF-320)
  - devuelve como máximo 20
- **isFileLink / toPlainText**
  - %s es un archivo
  - una página HTML no es un archivo
  - quita etiquetas y espacios sobrantes

## Enlaces

- [[M3 - result-filter]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
