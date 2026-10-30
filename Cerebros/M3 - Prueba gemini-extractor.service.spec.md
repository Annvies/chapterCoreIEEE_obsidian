---
type: prueba
modulo: 3
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/opportunities/gemini-extractor.service.spec.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - prueba
---

# M3 - Prueba gemini-extractor.service.spec

[[M3 - Pruebas]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Prueba
> 5 casos de prueba (Jest).

### Casos

- **GeminiExtractorService**
  - responde 503 si falta la clave, sin llamar al proveedor
  - envía la clave en cabecera (no en la URL) y usa salida JSON estructurada
  - traduce el 429 del nivel gratuito a un error explícito
  - envía la página como JSON para que su texto no rompa los delimitadores
  - normaliza la salida cruda descartando tipos incorrectos

## Enlaces

- [[M3 - gemini-extractor.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
