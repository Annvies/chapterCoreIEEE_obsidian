---
type: módulo
modulo: 2
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/contacts/contact-labels.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-2
  - módulo
---

# M2 - contact-labels

[[M2 - Interfaz]] · [[Cerebro 2 - Contactos]]

> [!abstract] Módulo
> Módulo del frontend (`frontendChapterCoreIEEE/src/features/contacts/contact-labels.ts`).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `CONTACT_TYPE_ORDER` | const | — |
| `TYPE_INFO` | const | — |
| `STATUS_LABELS` | const | — |
| `STATUS_OPTIONS` | const | — |
| `INTERACTION_LABELS` | const | — |
| `INTERACTION_OPTIONS` | const | — |
| `LAST_CONTACT_LABELS` | const | — |
| `LAST_CONTACT_OPTIONS` | const | — |
| `formatCalendarDate` | function | `aaaa-mm-dd` → `dd/mm/aaaa`, como en el mockup. |
| `todayLocalIso` | function | Hoy en la zona horaria del navegador, como `aaaa-mm-dd`. |
| `ExpiryState` | type | — |
| `expiryState` | function | Convenio vencido o por vencer en 30 días (se resalta en el panel). |
| `contactPersonLine` | function | "Nombre · Cargo" de la persona de contacto (empresas) o el cargo (personas). |
| `initials` | function | — |
| `CSV_TEMPLATE_COLUMNS` | const | Cabeceras de la plantilla CSV (mismas que acepta el backend). |


## Enlaces

- [[M2 - Tipos contacts]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
