---
type: central
estado: confirmado
fuentes:
  - frontendChapterCoreIEEE/src/App.tsx
  - frontendChapterCoreIEEE/package.json
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - Frontend React

[[CC - Arquitectura y stack]] · [[ChapterCore - Cerebro central]]

> [!abstract] SPA en React 18 con Vite, React Router 6 y formularios con react-hook-form + Zod.

- URL del backend: `VITE_API_URL`.
- Rutas públicas: `/login`, `/activar`, `/f/:slug`. El resto exige sesión y un permiso de la matriz por sección (ver [[CC - Rutas protegidas del frontend]]).
- Estructura: `features/` (una carpeta por pantalla), `api/` (clientes HTTP), `hooks/`, `lib/`, `types/`, `components/` compartidos y `auth/` (sesión y guards).
- QR generado en el navegador con la librería `qrcode`.
- Pruebas con Vitest + Testing Library (jsdom).

## Enlaces

- [[CC - Arquitectura y stack]]
