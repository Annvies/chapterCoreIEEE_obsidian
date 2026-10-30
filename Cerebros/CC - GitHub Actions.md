---
type: central
estado: confirmado
fuentes:
  - .github/workflows/backend-ci.yml
  - .github/workflows/frontend-ci.yml
  - .github/workflows/deploy-vercel-prod.yml
  - CONTEXTO.md
actualizado: 2026-10-29
tags:
  - chaptercore
  - cerebro-central
---

# CC - GitHub Actions

[[CC - Despliegue e integración continua]] · [[ChapterCore - Cerebro central]]

> [!abstract] Tres workflows validan y despliegan el producto.

| Workflow | Disparador | Qué hace |
|---|---|---|
| `backend-ci` | push a `dev`/`main`, PR a `main`/`dev` | Valida el backend |
| `frontend-ci` | push a `dev`/`main`, PR a `main`/`dev` | Valida el frontend |
| `deploy-vercel-prod` | push a `main` | Valida ambos → `migration:run` en Neon → despliega backend → despliega frontend (`vercel deploy --prebuilt --prod`) |

> [!warning] Validaciones duplicadas
> `CONTEXTO.md` §6 señala que los CI también corren en `main`, duplicando validaciones; conviene quitar ese trigger.

## Enlaces

- [[CC - Despliegue e integración continua]]
