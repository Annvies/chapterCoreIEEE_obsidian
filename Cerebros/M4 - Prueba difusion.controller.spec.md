---
type: prueba
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/difusion/difusion.controller.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - prueba
---

# M4 - Prueba difusion.controller.spec

[[M4 - Pruebas]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Prueba
> 12 casos de prueba (Jest).

### Casos

- **Difusión (HTTP)**
  - **administración**
    - aplica la matriz de permisos de Difusión
    - crea con un cuerpo válido y normaliza el alias
    - edita el destino y valida el id
    - rechaza con 400 un PATCH con %s = null (no llega a la base)
    - normaliza el destino (esquema en mayúsculas) antes de guardarlo
    - valida los parámetros de estadísticas
  - **redirección pública /r/:codigo**
    - redirige con 302 sin caché y marca el origen QR
    - cuenta como enlace si no viene del QR y no registra HEAD
    - no cuenta previsualizadores de chats ni precargas
    - sirve las páginas de aviso con cabeceras de seguridad
    - responde 410 si está pausado y 404 si no existe o el código es inválido
    - limita las redirecciones a 120 por minuto por IP

## Enlaces

- [[Cerebro 4 - Difusión y QR]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
