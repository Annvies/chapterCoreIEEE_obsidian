---
type: central
estado: confirmado
fuentes:
  - frontendChapterCoreIEEE/src/App.tsx
  - frontendChapterCoreIEEE/src/auth/RouteGuards.tsx
  - frontendChapterCoreIEEE/src/components/AppShell.tsx
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - Rutas protegidas del frontend

[[CC - Seguridad transversal]] · [[ChapterCore - Cerebro central]]

> [!abstract] El frontend repite la matriz: cada sección exige sesión y su permiso; el menú solo muestra lo permitido.

| Ruta | Permiso |
|---|---|
| `/login`, `/activar`, `/f/:slug` | Público |
| `/secretaria/formularios…` | Formularios · Editar |
| `/dashboard` | Dashboard · Ver |
| `/contactos` | Contactos · Ver |
| `/oportunidades` | Oportunidades · Ver |
| `/difusion` | Difusión · Ver |
| `/tesoreria` | Gastos · Ver |
| `/accesos` | Usuarios · Total |
| `/perfil` | Sesión iniciada (perfil IEEE propio) |

La protección real está en el backend; el frontend solo evita mostrar lo que no corresponde.

## Enlaces

- [[CC - Seguridad transversal]]
- [[Cerebro 1 - Base institucional]]
- [[Cerebro 7 - Tesorería y Gastos]]
