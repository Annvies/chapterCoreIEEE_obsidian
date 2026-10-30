---
type: utilidad
modulo: 4
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/lib/qr.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - utilidad
---

# M4 - lib qr

[[M4 - Interfaz]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Utilidad
> Estilo del mockup 06 → design token (tokens.css). Nunca colores escritos a mano.

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `QR_STYLE_TOKEN` | const | Estilo del mockup 06 → design token (tokens.css). Nunca colores escritos a mano. |
| `LOGO_MAX_BYTES` | const | — |
| `LOGO_TYPES` | const | — |
| `readColorToken` | function | Lee un token de color hexadecimal de :root (la librería de QR solo acepta hex). |
| `buildQrSvg` | function | SVG del QR. Con logo se usa corrección de errores alta (H, ~30 %) y el logo ocupa el centro sobre un recuadro claro, como en los QR con marca: el código sigue siendo legible. |
| `svgToDataUrl` | function | — |
| `svgToPngBlob` | function | Rasteriza el SVG a PNG de 1024 px para imprimir el afiche. |
| `downloadBlob` | function | — |
| `readLogoFile` | function | Valida y lee el logo como data URL. No se sube al servidor. |
| `displayUrl` | function | URL sin protocolo para mostrarla como en el mockup (`dominio/r/codigo`). |


## Enlaces

- [[M4 - Tipos difusion]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
