---
type: decorador
modulo: 1
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/auth/decorators/public.decorator.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-1
  - decorador
---

# M1 - public.decorator

[[M1 - Lógica del backend]] · [[Cerebro 1 - Base institucional]]

> [!abstract] Decorador
> Archivo de decorador del backend (`auth/decorators/public.decorator.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `IS_PUBLIC_KEY` | const | — |
| `Public` | const | Todas las rutas exigen sesión por defecto (JwtAuthGuard global). @Public() es la excepción explícita: login, enlaces de acceso y formularios públicos. |


## Enlaces

- [[Cerebro 1 - Base institucional]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
