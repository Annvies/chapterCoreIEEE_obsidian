---
type: componente
modulo: 5
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/responses/SubmissionDetail.tsx
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - componente
---

# M5 - SubmissionDetail

[[M5 - Interfaz]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Componente
> Componente del frontend (`frontendChapterCoreIEEE/src/features/responses/SubmissionDetail.tsx`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `SubmissionDetail` | function | — |

### Props

| Prop | Obligatoria | Tipo |
|---|---|---|
| `form` | sí | `FormDetail` |
| `submissionId` | sí | `string` |
| `onClose` | sí | `() => void` |
| `onReviewed` | sí | `(submission: SubmissionView) => void` |
| `field` | sí | `FormField` |
| `value` | sí | `unknown` |
| `uploads` | sí | `SubmissionUploadView[]` |
| `onDownload` | sí | `(upload: SubmissionUploadView) => void` |


## Enlaces

- [[M5 - lib api]]
- [[M5 - Tipos forms]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
