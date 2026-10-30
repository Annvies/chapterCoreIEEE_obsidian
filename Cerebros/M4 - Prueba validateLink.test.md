---
type: prueba
modulo: 4
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/difusion/validateLink.test.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-4
  - prueba
---

# M4 - Prueba validateLink.test

[[M4 - Pruebas]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Prueba
> 4 casos de prueba (Vitest + Testing Library).

### Casos

- **validateLink**
  - acepta un enlace válido con alias
  - exige nombre y destino http(s)
  - valida el formato del alias
- **isRedirectableUrl**
  - rechaza credenciales embebidas y protocolos peligrosos

## Enlaces

- [[M4 - validateLink]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
