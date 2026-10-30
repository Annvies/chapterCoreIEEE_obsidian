---
type: dominio
modulo: 2
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/contacts/domain/csv.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-2
  - dominio
---

# M2 - csv

[[M2 - Lógica del backend]] · [[Cerebro 2 - Contactos]]

> [!abstract] Dominio
> Lector CSV mínimo (RFC 4180) sin dependencias: comillas dobles, comillas escapadas (""), saltos de línea dentro de comillas, CRLF/LF y separador "," o ";" (Excel en español exporta con ";").

### Exporta

| Nombre | Tipo | Descripción |
|---|---|---|
| `CsvDelimiter` | type | — |
| `ParsedCsv` | interface | — |
| `CsvFormatError` | class | — |
| `detectDelimiter` | function | — |
| `parseCsv` | function | — |
| `normalizeHeader` | function | "Correo electrónico " -> "correo electronico". |


## Enlaces

- [[Cerebro 2 - Contactos]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
