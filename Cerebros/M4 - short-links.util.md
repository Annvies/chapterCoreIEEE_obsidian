---
type: dominio
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/difusion/short-links.util.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - dominio
---

# M4 - short-links.util

[[M4 - Lógica del backend]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Dominio
> Mismo enfoque que el acortador de MichiCode (código aleatorio de 6 caracteres con reintento si colisiona), pero con un generador criptográfico y solo minúsculas y dígitos: las URLs cortas se dictan y se escriben a mano desde un afiche. 36^6 ≈ 2.100 millones.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `CODE_LENGTH` | const | — |
| `CODE_PATTERN` | const | Formato común de códigos generados y alias: minúsculas, dígitos y guiones internos. |
| `CODE_MIN_LENGTH` | const | — |
| `CODE_MAX_LENGTH` | const | — |
| `generateShortCode` | function | — |
| `isRedirectableUrl` | function | Destino aceptable para una redirección: http(s) absoluto y sin usuario ni contraseña en la URL (esa parte se usa para disfrazar el destino real en enlaces de phishing). |
| `normalizeUrl` | function | Forma canónica de una URL (esquema y host en minúsculas); si no es URL, la deja igual. |
| `pointsToShortener` | function | true si el destino apunta al propio acortador (evita bucles de redirección). La ruta se compara sin distinguir mayúsculas, igual que el enrutador de Express. Los alias de dominio del mismo backend (otro host que sirve la misma app) no se pueden detectar aquí. |
| `isMobileUserAgent` | function | Detección mínima de móvil por user-agent; el user-agent no se guarda. |
| `isAutomatedRequest` | function | true si la petición es de un bot o una precarga del navegador (no cuenta como visita). |


## Enlaces

- [[Cerebro 4 - Difusión y QR]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
