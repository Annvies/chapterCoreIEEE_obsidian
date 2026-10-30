---
tags:
  - chaptercore
  - modulo-1
  - subgrupo
---

# Permisos compartidos

[[Cerebro 1 - Base institucional]] · Autorización transversal

> [!abstract] Idea central
> La matriz de permisos del mockup 03 es la oficial desde el 2026-10-19. Cada nivel
> tiene un acceso por función, y cada acceso incluye a los anteriores:
> `Ninguno < Responder < Ver < Editar < Total`.

> [!info] Matriz oficial
> | Función | Mesa Directiva | Secretaría | Director de capítulo | Miembro |
> |---|---|---|---|---|
> | Contactos | Total | Editar | Ver | Ninguno |
> | Oportunidades | Total | Editar | Editar | Ver |
> | Difusión | Total | Ver | Editar | Ninguno |
> | Formularios | Total | Total | Editar | Responder |
> | Dashboard | Total | Ver | Ver (su capítulo) | Ninguno |
> | Usuarios | Total | Ninguno | Ninguno | Ninguno |
> | Gastos | Total | Ver | Editar (su capítulo) | Ninguno |
>
> La fila de Gastos llegó con el Módulo 7 ([[Cerebro 7 - Tesorería y Gastos]]).

> [!example] Cómo se lee
> En Oportunidades, «Ver» permite buscar y usar la búsqueda en fuentes oficiales, y
> «Editar» permite extraer con IA y publicar (solo en el backend desde el PR #43). En Contactos, «Total» añade eliminar.
> Solo la Mesa Directiva administra usuarios y cargos.

> [!success] «Su capítulo» ya filtra en Dashboard y Gastos
> La marca `chapterOnly` de la matriz limita al Director a su capítulo en el Dashboard
> (PR #28, en `main` con el PR #29) y en Gastos (`resolveExpenseScope`). Ver
> [[Cerebro 6 - Feedback y KPIs]] y [[Cerebro 7 - Tesorería y Gastos]].

> [!todo] Pendiente
> Decidir si «su capítulo» debe filtrar los datos en los demás módulos (hoy solo lo hacen
> Dashboard y Gastos), y definir los grupos de visibilidad de contactos.

## Enlaces

Depende de [[M1 - Identidad y acceso]]. Implementado en
`backendChapterCoreIEEE/src/auth/domain/permissions.ts`.

## Notas del subgrupo

- [[M1 - Niveles de acceso]]
- [[M1 - Protección de la Mesa Directiva]]
