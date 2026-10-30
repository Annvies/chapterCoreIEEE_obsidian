---
type: prueba
modulo: 4
estado: confirmado
generado: true
fuentes:
  - backendChapterCoreIEEE/src/difusion/difusion.service.spec.ts
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - prueba
---

# M4 - Prueba difusion.service.spec

[[M4 - Pruebas]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Prueba
> 22 casos de prueba (Jest).

### Casos

- **DifusionService**
  - **create**
    - genera un código y devuelve la URL corta y la del QR
    - reintenta con otro código si el generado ya existe
    - se rinde tras varios choques seguidos
    - usa el alias y responde 409 si está ocupado
    - no reintenta ante otros errores
    - rechaza destinos que son otra URL corta (bucle)
  - **list**
    - cuenta visitas, filtra por tipo y estado y limita a 200
  - **update**
    - rechaza un destino en bucle también al editar
    - convierte una violación de CHECK de la base en 400, no en 500
    - cambia el destino sin cambiar el código
    - responde 404 si no existe
  - **resolve**
    - redirige y registra la visita sin datos personales
    - no registra peticiones HEAD
    - redirige aunque falle el registro de la visita
    - no redirige ni cuenta enlaces pausados o inexistentes
  - **stats**
    - suma la serie diaria y conserva los días sin visitas
    - usa 14 días y UTC por defecto y rechaza zonas desconocidas
    - responde 400 si PostgreSQL no reconoce una zona que Intl sí acepta
- **resolveShortBaseUrl**
  - quita la barra final y usa el puerto por defecto si no está configurada
  - falla al arrancar si la base no es una URL
  - en producción exige SHORT_LINK_BASE_URL (sin caer en localhost)
- **isValidTimeZone**
  - valida zonas IANA

## Enlaces

- [[M4 - difusion.service]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
