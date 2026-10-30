---
type: repositorio
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/repositories/contacts.repository.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-2
  - repositorio
---

# M2 - contacts.repository

[[M2 - Lógica del backend]] · [[Cerebro 2 - Contactos]]

> [!abstract] Repositorio
> Archivo de repositorio del backend (`contacts/repositories/contacts.repository.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ContactSearchCriteria` | interface | — |
| `ContactsRepository` | class | Acceso a datos del directorio. Los servicios no usan TypeORM directamente. |

### Métodos públicos

| Método | Devuelve | Descripción |
|---|---|---|
| `findById()` | Promise<Contact \| null> | — |
| `search()` | — | — |
| `countByType()` | Promise<Record<ContactType, number>> | Conteo por pestaña (sin filtros), como en el mockup. |
| `distinctSectors()` | Promise<string[]> | Sectores ya usados (para el filtro "+ Sector"), sin distinguir mayúsculas. |
| `create()` | Contact | — |
| `save()` | Promise<Contact> | — |
| `insertMany()` | Promise<number> | — |
| `delete()` | Promise<boolean> | — |
| `touchLastInteraction()` | Promise<void> | Mantiene la fecha de la interacción más reciente (no retrocede si se registra una antigua). |


## Enlaces

- [[M2 - contact]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
