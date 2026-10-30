---
type: servicio
modulo: 5
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/forms/forms.service.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-5
  - servicio
---

# M5 - forms.service

[[M5 - Lógica del backend]] · [[Cerebro 5 - Secretaría y formularios]]

> [!abstract] Servicio
> Archivo de servicio del backend (`forms/forms.service.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `FormsService` | class | — |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `create()` | Promise<FormDetail> | — |
| `findAll()` | Promise<PaginatedResult<FormListItem>> | — |
| `findOne()` | Promise<FormDetail> | — |
| `update()` | — | — |
| `publish()` | Promise<FormDetail> | — |
| `remove()` | — | — |
| `getPublishedBySlug()` | Promise<PublicFormView> | — |


## Enlaces

- [[Cerebro 5 - Secretaría y formularios]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
