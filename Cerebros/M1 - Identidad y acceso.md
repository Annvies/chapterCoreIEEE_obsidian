---
tags:
  - chaptercore
  - modulo-1
  - subgrupo
---

# Identidad y acceso

[[Cerebro 1 - Base institucional]] · Base transversal

> [!abstract] Idea central
> ChapterCore gestiona sus propias cuentas: correo y contraseña, sin proveedor externo.
> Identificar a la persona (sesión) es un paso distinto de autorizar cada operación
> ([[M1 - Permisos compartidos]]).

> [!info] Inicio de sesión
> - Contraseña de **8+ caracteres con letras y números** (máx. 72 bytes, límite de
>   bcrypt).
> - Sesión JWT de **8 horas**, o **30 días** si se marca «recordarme».
> - **5 intentos fallidos** bloquean la cuenta **15 minutos**.
> - El mensaje de error es el mismo si el correo no existe o la contraseña es
>   incorrecta, para no revelar qué cuentas existen.

> [!success] Enlaces de un solo uso
> Invitación (7 días) y restablecimiento (24 h). Solo se guarda el hash del token;
> al usarse, se invalidan los demás enlaces pendientes de esa persona.

> [!tip] Cierre de sesiones
> Cada usuario tiene un `token_version`. Cambiar la contraseña o desactivar la cuenta
> lo incrementa, y todas las sesiones abiertas dejan de ser válidas.

> [!warning] Reglas de protección
> Nadie puede desactivarse a sí mismo ni quitarse su propio nivel de Mesa Directiva, y
> el sistema impide dejar la Rama sin al menos una persona activa de Mesa Directiva.

## Enlaces

- Comparte criterios con [[M1 - Permisos compartidos]].
- El cargo de capítulo se apoya en [[M1 - Capítulos y sociedades]].

## Notas del subgrupo

- [[M1 - Ciclo de vida de una cuenta]]
- [[M1 - Enlaces de un solo uso]]
- [[M1 - Contraseñas y bloqueo de sesión]]
- [[M1 - Modelo de datos users y auth_tokens]]
- [[M1 - Perfil de membresía IEEE]]
- [[M1 - Estado de la membresía IEEE]]
- [[M1 - Aprobación de invitaciones]]
- [[M1 - Verificación manual en vTools]]
- [[M1 - Pantallas de membresía y aprobación]]
- [[M1 - Migraciones del perfil IEEE]]
