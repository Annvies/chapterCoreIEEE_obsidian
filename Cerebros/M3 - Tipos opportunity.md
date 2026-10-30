---
type: tipos
modulo: 3
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/types/opportunity.ts
actualizado: 2026-10-29
tags:
  - chaptercore
  - modulo-3
  - tipos
---

# M3 - Tipos opportunity

[[M3 - Interfaz]] · [[Cerebro 3 - Oportunidades IEEE]]

> [!abstract] Tipos
> Ficha de oportunidad según CONTEXTO.md §7 (mockup 05): titulo, tipo, fecha_limite, elegibilidad, beneficio y enlace. Contrato real de backendChapterCoreIEEE (snake_case).

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `OPPORTUNITY_TYPES` | const | Ficha de oportunidad según CONTEXTO.md §7 (mockup 05): titulo, tipo, fecha_limite, elegibilidad, beneficio y enlace. Contrato real de backendChapterCoreIEEE (snake_case). |
| `OpportunityType` | type | — |
| `OpportunityFields` | interface | Campos que se envían al publicar (POST /opportunities). |
| `OpportunityDraft` | interface | Ficha propuesta por la IA (POST /opportunities/extract); aún no se ha guardado. |
| `Opportunity` | interface | — |
| `IeeeSociety` | interface | — |
| `OPPORTUNITY_TYPE_LABEL` | const | — |


## Enlaces

- [[Cerebro 3 - Oportunidades IEEE]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
