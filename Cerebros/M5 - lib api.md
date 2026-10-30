---
type: utilidad
modulo: 5
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/lib/api.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-5
  - utilidad
---

# M5 - lib api

[[M5 - Interfaz]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Utilidad
> Utilidad del frontend (`frontendChapterCoreIEEE/src/lib/api.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ApiError` | class | — |
| `api` | const | — |

### Llamadas a la API

| Función | Método | Ruta |
|---|---|---|
| `listForms()` | `GET` | `/forms` |
| `getForm()` | `GET` | `/forms/:p` |
| `createForm()` | `POST` | `/forms` |
| `updateForm()` | `PATCH` | `/forms/:p` |
| `publishForm()` | `POST` | `/forms/:p/publish` |
| `deleteForm()` | `DELETE` | `/forms/:p` |
| `getPublicForm()` | `GET` | `/public/forms/:p` |
| `submitPublicForm()` | `POST` | `/public/forms/:p/submissions` |
| `listSubmissions()` | `GET` | `/forms/:p/submissions` |
| `getSubmission()` | `GET` | `/forms/:p/submissions/:p` |
| `reviewSubmission()` | `PATCH` | `/forms/:p/submissions/:p/review` |
| `getStats()` | `GET` | `/forms/:p/submissions/stats` |
| `exportSubmissions()` | `GET` | `/forms/:p/submissions/export` |


## Enlaces

- [[M5 - Tipos forms]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
