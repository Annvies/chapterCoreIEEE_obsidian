---
type: módulo Nest
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/contacts.module.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-2
  - módulo-Nest
---

# M2 - contacts.module

[[M2 - Lógica del backend]] · [[Cerebro 2 - Contactos]]

> [!abstract] Módulo Nest
> Módulo 2 · Contactos, empresas y exmiembros. Capas: controllers -> services -> repositories -> entities; reglas puras en domain/.

### Importa

- `TypeOrmModule`
- `Contact`
- `ContactInteraction`
- `AuthModule`

### Controladores

- `ContactsController`

### Proveedores

- `ContactsRepository`
- `ContactInteractionsRepository`
- `ContactsService`
- `ContactsImportService`


## Enlaces

- [[M2 - contacts.repository]]
- [[M2 - contact-interactions.repository]]
- [[M2 - contacts.service]]
- [[M2 - contacts-import.service]]
- [[M2 - GET contacts]]
- [[M2 - GET contacts › sectors]]
- [[M2 - GET contacts › chapters]]
- [[M2 - GET contacts › {id}]]
- [[M2 - POST contacts]]
- [[M2 - POST contacts › import]]
- [[M2 - PUT contacts › {id}]]
- [[M2 - DELETE contacts › {id}]]
- [[M2 - POST contacts › {id} › interactions]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
