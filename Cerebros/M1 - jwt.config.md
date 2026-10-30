---
type: configuración
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/config/jwt.config.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - configuración
---

# M1 - jwt.config

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Configuración
> Archivo de configuración del backend (`config/jwt.config.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `resolveJwtSecret` | function | JWT_SECRET es obligatorio en producción (mínimo 32 caracteres). En desarrollo, si falta, se usa un secreto aleatorio por proceso: las sesiones se pierden al reiniciar el backend, pero no hay que tocar el .env para arrancar. |


## Enlaces

- [[Cerebro 1 - Base institucional]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
