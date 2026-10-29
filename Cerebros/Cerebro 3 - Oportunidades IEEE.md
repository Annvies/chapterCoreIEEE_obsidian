---
aliases:
  - Módulo 3
  - Oportunidades IEEE
tags:
  - chaptercore
  - modulo-3
---

# Cerebro 3 — Búsqueda inteligente de oportunidades IEEE

## Subgrupos conectados

- [[M3 - Descubrimiento]]
- [[M3 - Extracción y revisión]]
- [[M3 - Publicación y búsqueda]]

> [!abstract] Propósito
> Ayudar a miembros a localizar oportunidades relevantes —por ejemplo, becas,
> concursos, premios, grants y voluntariados— y asistir a las personas autorizadas al
> preparar una ficha para revisión. El sistema facilita descubrimiento y organización;
> la fuente oficial de cada convocatoria sigue siendo la referencia para postular.

> [!info] Datos de una oportunidad
> La extracción puede proponer título, tipo, fecha límite, elegibilidad, beneficio,
> enlace y capítulo/sociedad. Una ficha útil debería permitir distinguir:
> - **Qué es:** título y tipo.
> - **A quién aplica:** elegibilidad y capítulo/sociedad si corresponde.
> - **Cuándo:** fecha límite y vigencia que deben comprobarse en la fuente.
> - **Qué ofrece:** beneficio o premio, si la fuente lo informa.
> - **Dónde confirmar:** URL original de la convocatoria.
>
> Este listado reúne campos descritos; no añade campos de producto no confirmados.

> [!success] Flujo descrito
> 1. Una persona autorizada entrega una URL de una fuente admitida.
> 2. El backend obtiene el contenido y Gemini propone una ficha estructurada.
> 3. El sistema muestra advertencias si faltan datos o hace falta confirmación.
> 4. Una persona revisa la información y decide si publicarla.
> 5. Los miembros buscan por palabras clave y filtran por tipo y capítulo/sociedad.
>
> Buscar requiere sesión y permiso de lectura; extraer y publicar requieren permiso de
> edición. La extracción no publica por sí sola.

> [!example] Revisión editorial recomendada
> Antes de publicar, abrir la convocatoria original y confirmar que el plazo no venció,
> que los requisitos y beneficios coinciden con la fuente, y que el enlace lleva al
> destino correcto. Si la página es ambigua, registrar la incertidumbre o no publicar
> hasta resolverla. Esta lista es una recomendación de revisión humana, no una
> verificación automática de la aplicación.

> [!tip] Cómo usar las fuentes IEEE
> El portal oficial [IEEE Student Opportunities](https://students.ieee.org/student-opportunities/)
> reúne financiación, becas y otras oportunidades estudiantiles. IEEE tiene además un
> formulario para que organizaciones presenten oportunidades para estudiantes. Estos
> recursos sirven para descubrir y contrastar convocatorias; la existencia en el portal
> no garantiza que el plazo siga abierto ni que cada estudiante cumpla los requisitos.

> [!warning] Lo que la extracción no garantiza
> Una ficha generada puede omitir información, interpretar mal una fecha o resumir de
> manera incompleta los criterios. Conservar el enlace fuente y la revisión humana
> ayuda a evitar que una propuesta de IA se confunda con una convocatoria verificada.

> [!todo] Límites y pendientes
> - La búsqueda avanzada en lenguaje natural no usa IA actualmente.
> - No hay recorrido/crawling automático de fuentes.
> - El perfil IEEE propuesto no está implementado.
> - La extracción puede equivocarse; la revisión humana es necesaria.
> - Documentar y mantener coherente la política de dominios admitidos.

## Conexiones

Depende de autenticación, permisos y catálogo compartido de
[[Cerebro 1 - Base institucional]]. Las oportunidades publicadas alimentan un conteo en
[[Cerebro 6 - Feedback y KPIs]].

## Fuentes externas

- [IEEE Student Opportunities](https://students.ieee.org/student-opportunities/):
  portal oficial para buscar oportunidades estudiantiles.
- [Submit Student Opportunity — IEEE](https://students.ieee.org/student-branches/submit-student-opportunity/):
  canal oficial para presentar una oportunidad al portal.
- [IEEE Region 9 SAC](https://r9.ieee.org/sac/): contexto de actividades, formación y
  oportunidades para estudiantes de Latinoamérica y el Caribe.
- [Callouts — ayuda oficial de Obsidian](https://obsidian.md/help/Editing+and+formatting/Callouts):
  formato de los grupos visuales.
