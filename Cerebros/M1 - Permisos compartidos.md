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

> [!example] Cómo se lee
> En Oportunidades, «Ver» permite buscar, y «Editar» permite extraer con IA y
> publicar. En Contactos, «Total» añade eliminar. Solo la Mesa Directiva administra
> usuarios y cargos.

> [!warning] «Su capítulo» todavía no filtra
> El Director de capítulo tiene el Dashboard marcado como «Ver (su capítulo)», pero
> hoy ve las métricas globales de la Rama. Ver [[Cerebro 6 - Feedback y KPIs]].

> [!todo] Pendiente
> Decidir si «su capítulo» debe filtrar los datos en cada módulo, y definir los grupos
> de visibilidad de contactos.

## Enlaces

Depende de [[M1 - Identidad y acceso]]. Implementado en
`backendChapterCoreIEEE/src/auth/domain/permissions.ts`.

## Notas del subgrupo

- [[M1 - Niveles de acceso]]
- [[M1 - Protección de la Mesa Directiva]]
