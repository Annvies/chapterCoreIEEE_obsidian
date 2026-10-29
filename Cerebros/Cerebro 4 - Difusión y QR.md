---
aliases:
  - Módulo 4
  - Difusión y QR
tags:
  - chaptercore
  - modulo-4
---

# Cerebro 4 — Difusión, webmaster y QR

## Subgrupos conectados

- [[M4 - Enlaces cortos]]
- [[M4 - Códigos QR]]
- [[M4 - Métricas de difusión]]

> [!abstract] Propósito
> Organizar los enlaces oficiales que comparte la Rama y facilitar su distribución con
> enlaces cortos y códigos QR dinámicos. Si el QR apunta a un enlace corto gestionado
> por ChapterCore, se puede cambiar el destino en el sistema sin reimprimir el QR.

> [!info] Piezas del módulo
> - **Enlace corto:** alias opcional o código generado.
> - **QR:** generado en el navegador, descargable como PNG o SVG.
> - **Destino:** se puede cambiar sin cambiar el código del enlace.
> - **Estado y nombre:** se pueden actualizar para administrar el enlace.
> - **Métricas:** visitas fechadas, origen aproximado (QR/enlace), clasificación de
>   dispositivo móvil, totales y serie diaria.
> - **Acceso:** la redirección es pública; administrar enlaces y consultar estadísticas
>   requiere permisos.

> [!success] Flujo de difusión
> 1. Crear un enlace corto y comprobar su destino.
> 2. Generar y descargar el QR asociado.
> 3. Publicarlo en el material de difusión.
> 4. Si cambia la página de destino, actualizar el enlace y probar nuevamente el QR.
> 5. Consultar las estadísticas del enlace para observar visitas registradas.
>
> Puede apuntar a formularios publicados en
> [[Cerebro 5 - Secretaría y formularios]].

> [!tip] Convención opcional de campañas
> Google Analytics recomienda identificar campañas con parámetros UTM y usar de forma
> consistente al menos `utm_source`, `utm_medium` y `utm_campaign` en las URL etiquetadas.
> Por ejemplo, definir valores consistentes para el canal de difusión y la campaña.
> Esto puede complementar análisis en plataformas que reciben esos parámetros; no es
> una función confirmada de ChapterCore ni reemplaza sus estadísticas internas.

> [!example] Qué puede significar una visita
> Las métricas del módulo describen solicitudes/visitas registradas por el sistema, no
> necesariamente personas únicas ni conversiones. El origen «QR» es aproximado y puede
> ser falsificado si se representa mediante un parámetro de URL; por ello debe leerse
> como una señal, no como atribución infalible.

> [!warning] Privacidad y confiabilidad de las métricas
> Antes de conservar datos de visitas, definir propósito, nivel de detalle, acceso y
> retención. Bots no reconocidos pueden contarse como visitas. El rate limit en memoria
> no se comparte entre instancias, así que su efecto depende de la arquitectura de
> despliegue.

> [!todo] Límites y pendientes
> - Definir política de privacidad y retención de visitas.
> - Considerar la atribución QR como orientativa.
> - El rate limit en memoria no se comparte entre instancias.
> - No se describen borrado de enlaces ni control de conflictos de edición simultánea.
> - Las métricas aún no se integran al Dashboard del Módulo 6.

## Conexiones

Usa permisos de [[Cerebro 1 - Base institucional]] y difunde formularios publicados del
[[Cerebro 5 - Secretaría y formularios]]. Sus métricas todavía no llegan al Dashboard
del Módulo 6.

## Fuentes externas

- [Google Analytics: URL builders y datos de campañas](https://support.google.com/analytics/answer/10917952?hl=en):
  uso de parámetros UTM para identificar campañas que dirigen tráfico.
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework): herramienta
  voluntaria para identificar y gestionar riesgos de privacidad.
- [Callouts — ayuda oficial de Obsidian](https://obsidian.md/help/Editing+and+formatting/Callouts):
  formato visual de los subgrupos.
