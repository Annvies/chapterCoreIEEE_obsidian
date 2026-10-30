---
type: prueba
modulo: 4
estado: confirmado
generado: true
fuentes:
  - frontendChapterCoreIEEE/src/features/difusion/DifusionPage.test.tsx
actualizado: 2026-10-30
tags:
  - chaptercore
  - modulo-4
  - prueba
---

# M4 - Prueba DifusionPage.test

[[M4 - Pruebas]] · [[Cerebro 4 - Difusión y QR]]

> [!abstract] Prueba
> 10 casos de prueba (Vitest + Testing Library).

### Casos

- **DifusionPage**
  - muestra la lista, la vista previa del más reciente y sus escaneos
  - valida antes de crear y envía solo los campos del contrato
  - acorta un enlace oficial con alias desde la otra pestaña
  - muestra el error del servidor (p. ej. alias ocupado)
  - edita el destino sin cambiar el código
  - sigue funcionando si el rol no puede ver los formularios
  - sin permiso Editar muestra la lista en solo lectura
  - cambia de pestaña con las flechas del teclado
  - lleva el foco al primer campo con error y conserva lo escrito al cambiar de pestaña
  - muestra en pantalla la confirmación al copiar el enlace

## Enlaces

- [[M4 - DifusionPage]]

%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%
