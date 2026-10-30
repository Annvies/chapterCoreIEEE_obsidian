# ChapterCore: mapa módulo → código

Repositorio: <https://github.com/marianZamorano/chapterCoreIEEE> (`main`).
Verificado el 2026-10-30 (commit `54d8d14`). Para la lista actualizada de archivos usa
`module_context(n)`, que la descubre por palabras clave.

## Reglas de lectura del repositorio

- **Producto:** `backendChapterCoreIEEE/` (NestJS + TypeORM + PostgreSQL) y
  `frontendChapterCoreIEEE/` (React). Infraestructura Neon/Vercel (`CONTEXTO.md` §6).
- **Fuente de decisiones:** `CONTEXTO.md` (§4 alcance, §5 cargos, capítulos y
  permisos, §7 IA y oportunidades, §9 pendientes).
- **Mockups:** `mockups/png/01…08` (referencia visual obligatoria; los valores
  entre corchetes son de ejemplo).
- **Tooling, no producto:** `backend/`, `frontend/`, `fullstack/`, `DevOps/`,
  `QA/`, `uiux/`, `.opencode/`, `.playwright-mcp/`.
- **Prohibido leer:** `backendChapterCoreIEEE/.env`, `frontendChapterCoreIEEE/.env`.

## Módulos

| # | Cerebro | Backend (`backendChapterCoreIEEE/src/`) | Frontend (`frontendChapterCoreIEEE/src/`) | Docs / mockups |
|---|---|---|---|---|
| 1 | Base institucional | `auth/` (domain/`permissions.ts`, `position.ts`, `password-policy.ts`, `one-time-token.ts`; services; guards; controllers `auth`, `users`, `access`), migración `…-CreateAuthModule.ts`, `database/seeds/create-admin.ts` | `features/auth/` (LoginPage, ActivateAccountPage), `features/access/RolesPage.tsx`, `auth/` (AuthProvider, RouteGuards), `lib/access.ts`, `lib/session.ts`, `api/auth.ts`, `types/auth.ts`, `hooks/useIeeeSocieties.ts` | `CONTEXTO.md` §5 · mockups 01, 03 |
| 2 | Contactos | `contacts/` (domain `contact-import.ts`, `csv.ts`; entities `contact`, `contact-interaction`), migración `…-CreateContactsModule.ts` | `features/contacts/DirectoryPage.tsx`, `api/contacts.ts`, `types/contacts.ts` | `CONTEXTO.md` §5 (decisiones Módulo 2) · mockup 04 |
| 3 | Oportunidades | `opportunities/` (`gemini-extractor.service.ts`, `page-fetcher.service.ts`, `official-sources.ts`, `is-official-ieee-url.decorator.ts`), entidad `ieee-society`, `official-domains.ts`, `discovery/` (cascada estáticas → navegador → catálogo, historial), migraciones `…-CreateOpportunities.ts`, `…-UniqueOpportunityEnlace.ts`, `…-CreateOpportunitySearchHistory.ts` | `features/opportunities/OpportunitiesPage.tsx`, `api/opportunities.ts`, `hooks/useOpportunitySearch.ts`, `useSavedOpportunities.ts`, `useOpportunityDiscovery.ts`, `useSearchHistory.ts`, `components/OpportunityCard.tsx`, `DeadlineBadge.tsx` (la interfaz de extracción se retiró en el PR #43) | `CONTEXTO.md` §7 · `specs/002-oportunidades-fuentes-oficiales/` · `docs/qa/estrategia-pruebas-oportunidades.md` · mockup 05 |
| 4 | Difusión y QR | `difusion/` (`short-links.util.ts`, `redirect.controller.ts`, entidades `short-link`, `link-visit`), migración `…-CreateDifusionModule.ts` | `features/difusion/` (DifusionPage, LinksTable, NewLinkPanel, QrPreviewPanel, ScanStatsPanel), `hooks/useShortLinks.ts`, `useLinkStats.ts`, `useQrSvg.ts`, `lib/qr.ts` | `docs/modulo-4-difusion-qr.md` · mockup 06 |
| 5 | Secretaría y formularios | `forms/` (`schema/form-schema.zod.ts`, entities `form`, `form-version`, `form-submission`, `form-upload`, `storage/`), migración `…-CreateFormsModule.ts` | `features/forms/` (FormsListPage, FormBuilderPage), `features/public/PublicFormPage.tsx`, `features/responses/FormResponsesPage.tsx`, `lib/form-schema.ts`, `form-schema-helpers.ts`, `types/forms.ts`, `hooks/usePublishedForms.ts` | `CONTEXTO.md` §4 · mockups 07, 08 |
| 6 | Feedback y KPIs | `dashboard/` (`dashboard.service.ts`, `dashboard.types.ts`, `dto/dashboard-query.dto.ts`) | `features/dashboard/DashboardPage.tsx`, `api/dashboard.ts`, `hooks/useDashboardSummary.ts`, `types/dashboard.ts` | `CONTEXTO.md` §4 (fórmulas KPI) · mockup 02 |
| 7 | Tesorería y gastos | `expenses/` (`domain/expense.ts`, `services/expenses.service.ts`, `repositories/expenses.repository.ts`, entidad `expense`), migración `…-CreateExpensesModule.ts`, fila `Feature.Expenses` en `auth/domain/permissions.ts` | `features/expenses/` (ExpensesPage, ExpenseDialog, ExpensesTable, expense-schema, useExpenses), `api/expenses.ts`, `types/expenses.ts`, `lib/format.ts` (moneda) | `specs/009-modulo-7-gastos-tesoreria/` · `docs/spec-modulo-7-gastos.md` · sin mockup |

## Hechos verificados útiles (Módulo 1)

- Niveles: `mesa_directiva`, `secretaria`, `director_capitulo`, `miembro`.
- Accesos ordenados: `none < respond < view < edit < total`.
- Funciones de la matriz: `contacts`, `opportunities`, `dissemination`, `forms`,
  `dashboard`, `users`, `expenses`.
- Catálogo `ieee_societies`: PES, CIS, ComSoc, WIE (grupo de afinidad), CASS,
  EMBS, RAS, IAS, CS.

## Ideas de notas nuevas con respaldo en el código

- M1: "M1 - Matriz de permisos" (concepto) · "ADR-001 - Autenticación propia sin IdP".
- M2: "M2 - Importación CSV todo o nada" (límite 1 MB / 500 filas).
- M3: "M3 - Fuentes oficiales admitidas" (`official-sources.ts`) · flujo Mermaid de extracción.
- M4: "M4 - Modelo short_links y link_visits".
- M5: "M5 - Esquema Zod de formularios" · "M5 - Versionado de formularios".
- M6: "M6 - Fórmulas de KPI" (satisfacción `scale` 1–5 `useInKpis`, NPS 0–10).

Antes de crear cualquiera, lee el archivo citado y confirma el detalle.
