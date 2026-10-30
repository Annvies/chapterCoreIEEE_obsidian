---
aliases:
  - Módulo 1
  - Base institucional
tags:
  - chaptercore
  - modulo-1
---

# Cerebro 1 — Base institucional, usuarios y permisos

Parte de [[ChapterCore - Cerebro central]] · cerebro especializado del Módulo 1

## Código

Documentación técnica: [[M1 - Código del módulo]] (endpoints, archivos, pantallas y pruebas).

## Subgrupos conectados

- [[M1 - Identidad y acceso]]
- [[M1 - Capítulos y sociedades]]
- [[M1 - Permisos compartidos]]

> [!abstract] Identidad y estructura
> Este módulo es la base transversal de ChapterCore: cuentas de integrantes, su cargo
> y ámbito (Rama o capítulo), el nivel de acceso que resulta de ese cargo y la matriz
> de permisos que aplican los demás módulos. El catálogo de capítulos es la tabla
> `ieee_societies`, compartida con Oportunidades y Contactos.

> [!info] Decisiones confirmadas (2026-10-19)
> - **Autenticación propia** con correo y contraseña (bcrypt + JWT emitido por el
>   backend). No hay proveedor de identidad externo ni «Ingresar con IEEE Account».
> - **Cada persona tiene un solo cargo**: Presidente, Vicepresidente, Tesorero,
>   Secretario o Webmaster, con ámbito Rama o capítulo. Sin cargo es «miembro».
> - **Cuatro niveles de acceso** (mockup 03): Mesa Directiva, Secretaría, Director de
>   capítulo y Miembro. Ver [[M1 - Permisos compartidos]].
> - **Alta solo por invitación** de la Mesa Directiva, con enlace de un solo uso.
> - **No hay servicio de correo**: los enlaces se comparten manualmente.

> [!success] Ciclo de vida de una cuenta
> 1. La Mesa Directiva invita (correo, nombre, cargo, ámbito, capítulo y n.º IEEE
>    opcional). La cuenta queda en estado `invited`.
> 2. El sistema genera un enlace de invitación válido **7 días**.
> 3. La persona abre el enlace, define su contraseña y la cuenta pasa a `active`.
> 4. Si olvida la contraseña, la Mesa Directiva genera un enlace de restablecimiento
>    válido **24 horas**.
> 5. La Mesa Directiva puede desactivar (`disabled`) y reactivar la cuenta.
>
> La primera cuenta (Presidencia de la Rama) se crea con el script
> `npm run seed:admin`, que imprime su enlace de activación.

> [!example] Del cargo al nivel de acceso
> | Cargo | Ámbito | Nivel |
> |---|---|---|
> | Presidente, Vicepresidente, Tesorero, Webmaster | Rama | Mesa Directiva |
> | Secretario | Rama o capítulo | Secretaría |
> | Presidente, Vicepresidente, Tesorero, Webmaster | Capítulo | Director de capítulo |
> | Sin cargo | — | Miembro |

> [!warning] No confundir sesión con autorización
> Tener sesión no implica poder editar. Cada operación declara qué permiso necesita
> (`@RequirePermission`) y un guard global lo compara con el nivel del usuario. Las
> rutas públicas (login, enlaces, formularios publicados, redirecciones) se marcan
> explícitamente como `@Public`.

> [!todo] Pendientes del Módulo 1
> - Los permisos «su capítulo» aún **no filtran datos por capítulo**: hoy solo se
>   aplica el nivel, y los módulos todavía no guardan el capítulo en todos los
>   registros.
> - Fuera del MVP por ahora: **registro de actividad** y **transferencia del periodo
>   de gestión** (aparecen en el mockup 03).
> - Sin servicio de correo, invitaciones y restablecimientos dependen de que la Mesa
>   Directiva comparta el enlace por otro canal.

## Conexiones

Es una dependencia de [[Cerebro 2 - Contactos]], [[Cerebro 3 - Oportunidades IEEE]],
[[Cerebro 4 - Difusión y QR]], [[Cerebro 5 - Secretaría y formularios]] y
[[Cerebro 6 - Feedback y KPIs]]. El Dashboard informa integrantes activos y el ranking
de capítulos por miembros activos.

## Fuentes

- `CONTEXTO.md` §5 del repositorio del producto: cargos, capítulos y decisiones
  confirmadas del Módulo 1.
- `backendChapterCoreIEEE/src/auth/`: implementación (dominio, servicios, guards).
- `backendChapterCoreIEEE/src/database/migrations/…-CreateAuthModule.ts`: tablas
  `users` y `auth_tokens`.
- [IEEE Student Branches](https://students.ieee.org/student-branches/): contexto
  general de las ramas estudiantiles (no define la implementación).
