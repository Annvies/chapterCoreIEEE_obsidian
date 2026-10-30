---
type: dominio
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/domain/contact.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-2
  - dominio
---

# M2 - contact

[[M2 - Lógica del backend]] · [[Cerebro 2 - Contactos]]

> [!abstract] Dominio
> Módulo 2 · Contactos, empresas y exmiembros (CONTEXTO.md §4, mockup 04). Decisiones del 2026-10-19: tabla única con tipo + historial de interacciones; visibilidad solo por la matriz de permisos (los grupos siguen pendientes).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `ContactType` | enum | Pestañas del mockup 04. |
| `CONTACT_TYPES` | const | — |
| `RelationshipStatus` | enum | Estado de la relación con la Rama (chips del mockup 04). |
| `RELATIONSHIP_STATUSES` | const | — |
| `InteractionType` | enum | Tipos de registro del historial ("Registrar llamada", "Enviar correo", etc.). |
| `INTERACTION_TYPES` | const | — |
| `LastContactFilter` | enum | Filtro "Último contacto" del mockup. |
| `LAST_CONTACT_FILTERS` | const | — |
| `CONTACT_LIMITS` | const | — |
| `isIsoDate` | function | Fecha de calendario "aaaa-mm-dd" válida (sin hora ni zona). |
| `todayIso` | function | Hoy como "aaaa-mm-dd" en UTC. |


## Enlaces

- [[Cerebro 2 - Contactos]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
