---
type: concepto
modulo: 4
estado: confirmado
fuentes:
  - backendChapterCoreIEEE/src/difusion/short-links.util.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-4
  - concepto
---

# M4 - Validación de destinos

[[M4 - Enlaces cortos]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Qué es
> Reglas para que un enlace corto no sirva de trampa.

> [!info] Confirmado en el código
> - Solo destinos `http` o `https` absolutos.
> - Se rechazan URLs con usuario o contraseña (técnica de phishing para disfrazar el destino).
> - Se rechaza un destino que apunte al propio acortador, para evitar bucles.

## Enlaces

- Forma parte de [[M4 - Enlaces cortos]].
- Relacionada con [[M4 - Modelo short_links y link_visits]], [[M4 - Códigos y alias]].

## Fuentes

- `backendChapterCoreIEEE/src/difusion/short-links.util.ts`
