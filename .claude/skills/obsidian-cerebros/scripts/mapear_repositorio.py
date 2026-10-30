"""Mapea el código del producto ChapterCore a notas atómicas de la bóveda.

Crea, por módulo, seis grupos técnicos (API, DTO y validaciones, Lógica del backend,
Base de datos, Interfaz, Pruebas) y una nota por cada endpoint, DTO, tabla, archivo de
backend, componente, hook, cliente de API, archivo de tipos y archivo de pruebas.

Seguridad:
- Solo LEE `backendChapterCoreIEEE/src` y `frontendChapterCoreIEEE/src` (nunca .env).
- Solo ESCRIBE en `Cerebros/` y solo BORRA notas con `generado: true` en su frontmatter.
- Sin red y sin ejecutar comandos.

Uso (desde la raíz de la bóveda):
    python -I .claude/skills/obsidian-cerebros/scripts/mapear_repositorio.py [ruta del repo]
Si no se indica la ruta, usa .chaptercore.local.json o ../../ChapterCoreIEEE/chapterCoreIEEE.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parents[4]
C = VAULT / "Cerebros"
HOY = date.today().isoformat()


def repo_path() -> Path:
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).resolve()
    local = VAULT / ".chaptercore.local.json"
    if local.exists():
        return Path(json.loads(local.read_text(encoding="utf-8"))["repo"])
    return (VAULT / ".." / ".." / "ChapterCoreIEEE" / "chapterCoreIEEE").resolve()


REPO = repo_path()
BE = REPO / "backendChapterCoreIEEE" / "src"
FE = REPO / "frontendChapterCoreIEEE" / "src"
if not BE.is_dir() or not FE.is_dir():
    sys.exit(f"No se encontró el código del producto en {REPO}. Indica la ruta del clon.")

CEREBROS = {
    1: "Cerebro 1 - Base institucional", 2: "Cerebro 2 - Contactos", 3: "Cerebro 3 - Oportunidades IEEE",
    4: "Cerebro 4 - Difusión y QR", 5: "Cerebro 5 - Secretaría y formularios", 6: "Cerebro 6 - Feedback y KPIs",
}
GRUPOS = {
    "api": ("API", "Endpoints HTTP del módulo: método, ruta, permiso, límites y lógica que invocan."),
    "dto": ("DTO y validaciones", "Contratos de entrada de la API y sus reglas de validación (class-validator)."),
    "backend": ("Lógica del backend", "Servicios, reglas de dominio, guards, repositorios y utilidades del backend."),
    "db": ("Base de datos", "Tablas PostgreSQL creadas por las migraciones TypeORM, con columnas, restricciones e índices."),
    "ui": ("Interfaz", "Páginas, componentes, hooks, clientes de API y tipos del frontend React."),
    "test": ("Pruebas", "Archivos de pruebas automatizadas y los casos que verifican."),
}
FEATURE = {"Users": "Usuarios", "Contacts": "Contactos", "Opportunities": "Oportunidades",
           "Dissemination": "Difusión", "Forms": "Formularios", "Dashboard": "Dashboard"}
ACCESS = {"None": "Ninguno", "Respond": "Responder", "View": "Ver", "Edit": "Editar", "Total": "Total"}

BE_MOD = {"auth": 1, "contacts": 2, "opportunities": 3, "difusion": 4, "forms": 5, "dashboard": 6}
FE_FEAT_MOD = {"access": 1, "auth": 1, "contacts": 2, "opportunities": 3, "difusion": 4,
               "forms": 5, "public": 5, "responses": 5, "dashboard": 6}
FE_NAME_MOD = {"auth": 1, "contacts": 2, "opportunities": 3, "opportunity": 3, "difusion": 4,
               "dashboard": 6, "forms": 5, "access": 1, "session": 1, "qr": 4, "form-schema": 5,
               "form-schema-helpers": 5, "officialSources": 3, "api": 5}
HOOK_MOD = {"useIeeeSocieties": 3, "useOpportunitySearch": 3, "useOpportunityExtraction": 3,
            "useSavedOpportunities": 3, "useShortLinks": 4, "useLinkStats": 4, "useQrSvg": 4,
            "usePublishedForms": 5, "useDashboardSummary": 6}
COMPONENT_MOD = {"OpportunityCard": 3, "DeadlineBadge": 3}
TABLE_MOD = {"users": 1, "auth_tokens": 1, "ieee_societies": 1, "contacts": 2, "contact_interactions": 2,
             "opportunities": 3, "short_links": 4, "link_visits": 4, "forms": 5, "form_versions": 5,
             "form_submissions": 5, "form_uploads": 5}
TABLE_CONCEPT = {"users": "M1 - Modelo de datos users y auth_tokens", "auth_tokens": "M1 - Modelo de datos users y auth_tokens",
                 "ieee_societies": "M1 - Catálogo ieee_societies", "contacts": "M2 - Modelo de datos contacts",
                 "contact_interactions": "M2 - Historial de interacciones", "opportunities": "M3 - Modelo de datos opportunities",
                 "short_links": "M4 - Modelo short_links y link_visits", "link_visits": "M4 - Modelo short_links y link_visits",
                 "forms": "M5 - Estados del formulario", "form_versions": "M5 - Versionado de formularios",
                 "form_submissions": "M5 - Estados de una respuesta", "form_uploads": "M5 - Archivos adjuntos"}


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def rel(p: Path) -> str:
    return p.relative_to(REPO).as_posix()


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def balanced(text: str, start: int, open_ch: str = "(", close_ch: str = ")") -> int:
    """Índice del cierre que corresponde a text[start] (que debe ser open_ch)."""
    depth, quote = 0, None
    i = start
    while i < len(text):
        ch = text[i]
        if quote:
            if ch == "\\":
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in "'\"`":
            quote = ch
        elif ch == open_ch:
            depth += 1
        elif ch == close_ch:
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return len(text) - 1


def leading_comment(lines: list[str], idx: int) -> str:
    """Comentario (// o /** */) inmediatamente anterior a la línea idx."""
    out = []
    j = idx - 1
    while j >= 0 and (lines[j].strip().startswith(("//", "*", "/**", "*/")) or lines[j].strip().startswith("@")):
        s = lines[j].strip()
        if not s.startswith("@"):
            s = re.sub(r"^(/\*\*|\*/|\*|//)\s?", "", s).strip().rstrip("*/").strip()
            if s:
                out.append(s)
        j -= 1
    return " ".join(reversed(out))


def file_comment(text: str) -> str:
    """Primer bloque de comentario del archivo, antes de la primera declaración."""
    lines = text.splitlines()
    out = []
    for line in lines:
        s = line.strip()
        if s.startswith(("import ", "}", "from ")) or (s and not s.startswith(("//", "/*", "*")) and out == [] and not s.startswith("import")):
            if s.startswith(("import ", "} from", "from ")):
                continue
            break
        if s.startswith(("//", "/*", "*")):
            c = re.sub(r"^(/\*\*|/\*|\*/|\*|//)\s?", "", s).strip().rstrip("*/").strip()
            if c:
                out.append(c)
        elif out and not s:
            break
    return " ".join(out)


# ---------------------------------------------------------------- registro de notas
NOTES: dict[str, dict] = {}       # nombre -> {modulo, grupo, tipo, cuerpo, enlaces, fuentes, alias}
BY_FILE: dict[str, str] = {}      # ruta del repo -> nombre de nota


def unique(name: str) -> str:
    base, n = name, 2
    while name in NOTES or (C / f"{name}.md").exists() and not is_generated(C / f"{name}.md"):
        name = f"{base} ({n})"
        n += 1
    return name


def is_generated(p: Path) -> bool:
    try:
        head = p.read_text(encoding="utf-8")[:600]
    except OSError:
        return False
    return "\ngenerado: true\n" in head.replace("\r\n", "\n")


def add_note(name: str, modulo: int, grupo: str, tipo: str, abstract: str, cuerpo: list[str],
             fuentes: list[str], alias: list[str] | None = None) -> str:
    name = unique(name)
    NOTES[name] = {"modulo": modulo, "grupo": grupo, "tipo": tipo, "abstract": abstract, "cuerpo": cuerpo,
                   "fuentes": fuentes, "alias": alias or [], "enlaces": []}
    if tipo != "endpoint":  # un controlador tiene varios endpoints: no representa al archivo
        for f in fuentes:
            BY_FILE.setdefault(f, name)
    return name


# ---------------------------------------------------------------- backend: DTO
DTO_CLASS: dict[str, str] = {}  # NombreClase -> nota


def parse_dtos() -> None:
    for p in sorted(BE.rglob("dto/*.ts")):
        mod = BE_MOD.get(p.relative_to(BE).parts[0])
        if not mod:
            continue
        text = read(p)
        lines = text.splitlines()
        for i, line in enumerate(lines):
            m = re.match(r"export class (\w+)(?: extends ([\w()<>, ]+))? \{", line)
            if not m:
                continue
            cls, parent = m.group(1), m.group(2)
            end = balanced(text, text.index("{", text.index(line)), "{", "}")
            body = text[text.index(line):end]
            rows, decos = [], []
            blines = body.splitlines()[1:]
            k = 0
            while k < len(blines):
                bl = blines[k]
                if re.match(r"^  @\w+", bl):
                    deco = bl.strip()
                    while deco.count("(") > deco.count(")") and k + 1 < len(blines):
                        k += 1
                        deco += " " + blines[k].strip()
                    decos.append(re.sub(r"\s+", " ", deco))
                else:
                    pm = re.match(r"^  (?:readonly )?(\w+)([?!])?: (.+?);", bl)
                    if pm:
                        reglas = ", ".join(f"`{cell(d[:90])}{'…' if len(d) > 90 else ''}`" for d in decos) or "—"
                        opcional = "sí" if pm.group(2) == "?" or any(d.startswith("@IsOptional") for d in decos) else "no"
                        rows.append(f"| `{pm.group(1)}` | `{cell(pm.group(3))}` | {opcional} | {reglas} |")
                        decos = []
                k += 1
            comment = leading_comment(lines, i)
            cuerpo = []
            if parent:
                cuerpo.append(f"Hereda de `{parent}`.")
                cuerpo.append("")
            if rows:
                cuerpo += ["| Campo | Tipo | Opcional | Validaciones |", "|---|---|---|---|", *rows]
            else:
                cuerpo.append("Sin campos propios.")
            note = add_note(f"M{mod} - DTO {cls}", mod, "dto", "dto",
                            comment or f"Contrato de datos `{cls}` validado por el `ValidationPipe` global (whitelist y forbidNonWhitelisted).",
                            cuerpo, [rel(p)])
            NOTES[note]["parent"] = parent
            DTO_CLASS[cls] = note
    for name, n in NOTES.items():
        par = n.get("parent")
        if par:
            target = next((DTO_CLASS[c] for c in re.findall(r"\w+", par) if c in DTO_CLASS), None)
            if target and NOTES[target]["modulo"] == n["modulo"]:
                n["enlaces"].append(target)


# ---------------------------------------------------------------- backend: archivos de lógica
SKIP_BACKEND = re.compile(r"(\.spec\.ts|/dto/|/entities/|controller\.ts|\.module\.ts|/migrations/)$|/dto/|/entities/|/migrations/")
SERVICE_TYPE: dict[str, str] = {}  # ClaseServicio -> nota


def parse_backend_files() -> None:
    for p in sorted(BE.rglob("*.ts")):
        r = p.relative_to(BE).as_posix()
        if SKIP_BACKEND.search("/" + r) or r.endswith((".spec.ts", "controller.ts", ".module.ts")):
            continue
        top = p.relative_to(BE).parts[0]
        mod = BE_MOD.get(top)
        if r.startswith("database/seeds/"):
            mod = 1
        if r == "config/jwt.config.ts":
            mod = 1
        if not mod:
            continue
        text = read(p)
        lines = text.splitlines()
        exports, metodos = [], []
        current_class = None
        for i, line in enumerate(lines):
            m = re.match(r"export (?:abstract )?(class|interface|type|enum|const|function|async function) (\w+)", line)
            if m:
                kind = {"async function": "function"}.get(m.group(1), m.group(1))
                desc = leading_comment(lines, i)
                exports.append(f"| `{m.group(2)}` | {kind} | {cell(desc) or '—'} |")
                current_class = m.group(2) if kind == "class" else current_class
                if kind == "class" and m.group(2).endswith(("Service", "Repository", "Guard")):
                    SERVICE_TYPE[m.group(2)] = None  # se rellena abajo
            mm = re.match(r"^  (?:async )?(\w+)\((.*)", line)
            if mm and current_class and mm.group(1) not in ("constructor", "if", "for", "while", "switch", "return"):
                desc = leading_comment(lines, i)
                firma = mm.group(2)
                ret = re.search(r"\):\s*([^{]+)\{?\s*$", line)
                metodos.append(f"| `{mm.group(1)}()` | {cell(ret.group(1).strip()) if ret else '—'} | {cell(desc) or '—'} |")
        cuerpo = []
        if exports:
            cuerpo += ["### Exporta", "", "| Nombre | Tipo | Descripción |", "|---|---|---|", *exports, ""]
        if metodos:
            cuerpo += ["### Métodos públicos", "", "| Método | Devuelve | Descripción |", "|---|---|---|", *metodos, ""]
        kind = ("servicio" if ".service" in p.name else "repositorio" if "repositor" in r else
                "guard" if "guard" in r else "decorador" if "decorator" in p.name else "mapper" if "mapper" in r else
                "seed" if "seeds" in r else "configuración" if r.startswith("config") else "dominio")
        name = add_note(f"M{mod} - {p.stem}", mod, "backend", kind,
                        file_comment(text) or f"Archivo de {kind} del backend (`{r}`).", cuerpo, [rel(p)])
        for cls in [e.split("`")[1] for e in exports if "| class |" in e]:
            SERVICE_TYPE[cls] = name


def link_backend_imports() -> None:
    for p in sorted(BE.rglob("*.ts")):
        src = BY_FILE.get(rel(p))
        if not src:
            continue
        for imp in re.findall(r"from '(\.[^']+)'", read(p)):
            target = (p.parent / imp).resolve()
            for cand in (target.with_suffix(".ts"), target / "index.ts"):
                note = BY_FILE.get(rel(cand)) if cand.exists() else None
                if note and note != src and NOTES[note]["modulo"] == NOTES[src]["modulo"]:
                    NOTES[src]["enlaces"].append(note)


# ---------------------------------------------------------------- backend: endpoints
ENDPOINTS: list[tuple[str, str, str]] = []  # (metodo, ruta, nota)


def route_name(method: str, route: str) -> str:
    parts = [("{" + s[1:] + "}") if s.startswith(":") else s for s in route.strip("/").split("/") if s]
    return f"{method} " + (" › ".join(parts) if parts else "raíz")


def parse_endpoints() -> None:
    for p in sorted(BE.rglob("*controller.ts")):
        if p.name.endswith(".spec.ts"):
            continue
        mod = BE_MOD.get(p.relative_to(BE).parts[0])
        if not mod:
            continue
        text = read(p)
        base_m = re.search(r"@Controller\((?:'([^']*)')?\)", text)
        base = (base_m.group(1) or "") if base_m else ""
        cls_idx = text.index("export class")
        head = text[:cls_idx]
        cls_perm = re.search(r"@RequirePermission\(Feature\.(\w+), Access\.(\w+)\)", head)
        cls_public = "@Public()" in head
        cls_comment = leading_comment(text[:cls_idx].splitlines() + [""], len(text[:cls_idx].splitlines()))
        fields = dict(re.findall(r"private readonly (\w+): (\w+)", text))
        lines = text[cls_idx:].splitlines()
        buf: list[str] = []
        k = 0
        while k < len(lines):
            line = lines[k]
            if re.match(r"^  @\w+", line):
                deco = line.strip()
                while deco.count("(") > deco.count(")") and k + 1 < len(lines):
                    k += 1
                    deco += " " + lines[k].strip()
                buf.append(deco)
                k += 1
                continue
            if re.match(r"^  //|^  /\*\*|^   \*", line):
                buf.append("#" + re.sub(r"^\s*(/\*\*|\*/|\*|//)\s?", "", line).strip().rstrip("*/").strip())
                k += 1
                continue
            mm = re.match(r"^  (?:async )?(\w+)\(", line)
            if mm and mm.group(1) != "constructor" and any(re.match(r"@(Get|Post|Put|Patch|Delete)\(", d) for d in buf):
                start = k
                while k < len(lines) and lines[k] != "  }":
                    k += 1
                block = "\n".join(lines[start:k + 1])
                decos = [d for d in buf if not d.startswith("#")]
                comment = " ".join(d[1:] for d in buf if d.startswith("#") and len(d) > 1)
                http = next(re.match(r"@(Get|Post|Put|Patch|Delete)\((?:'([^']*)')?\)", d) for d in decos if re.match(r"@(Get|Post|Put|Patch|Delete)\(", d))
                method, sub = http.group(1).upper(), http.group(2) or ""
                route = "/" + "/".join(x for x in (base, sub) if x)
                perm = next((re.search(r"Feature\.(\w+), Access\.(\w+)", d) for d in decos if d.startswith("@RequirePermission")), None) or cls_perm
                public = cls_public or "@Public()" in decos
                acceso = "Público (sin sesión)" if public else (
                    f"{FEATURE.get(perm.group(1), perm.group(1))} · {ACCESS.get(perm.group(2), perm.group(2))}" if perm else "Sesión iniciada")
                thr = next((re.search(r"limit: (\d+), ttl: ([\d_]+)", d) for d in decos if d.startswith("@Throttle")), None)
                code = next((re.search(r"HttpStatus\.(\w+)", d) for d in decos if d.startswith("@HttpCode")), None)
                sig = block[: block.find("{", block.find(")"))] if ")" in block else block
                params = []
                for pm in re.finditer(r"@Param\('(\w+)'", sig):
                    params.append(f"- Parámetro de ruta `{pm.group(1)}`" + (" (UUID)" if "ParseUUIDPipe" in sig[pm.start():pm.start() + 60] else ""))
                for pm in re.finditer(r"@Query\((?:'(\w+)')?\) (\w+)(?:\?)?: ([\w| ]+)", sig):
                    params.append(f"- Query {'`' + pm.group(1) + '`' if pm.group(1) else ''} → `{pm.group(3).strip()}`")
                for pm in re.finditer(r"@Body\(\) (\w+): (\w+)", sig):
                    params.append(f"- Cuerpo → `{pm.group(2)}`")
                if "@UploadedFile()" in sig:
                    params.append("- Archivo adjunto (multipart)")
                if "@CurrentUser()" in sig:
                    params.append("- Usa la persona autenticada (`@CurrentUser`)")
                ret = re.search(r"\):\s*(Promise<[^{]+>|[\w<>\[\]| ]+)\s*\{", sig + "{")
                calls = sorted(set(re.findall(r"this\.(\w+)\.(\w+)\(", block)))
                cuerpo = ["| Campo | Valor |", "|---|---|",
                          f"| Método | `{method}` |", f"| Ruta | `{route}` |", f"| Acceso | {acceso} |",
                          f"| Controlador | `{rel(p)}` → `{mm.group(1)}()` |"]
                if thr:
                    cuerpo.append(f"| Límite | {thr.group(1)} peticiones por {int(thr.group(2).replace('_', '')) // 1000} s |")
                if code:
                    cuerpo.append(f"| Respuesta | `{code.group(1)}` |")
                if ret:
                    cuerpo.append(f"| Devuelve | `{cell(ret.group(1).strip())}` |")
                if params:
                    cuerpo += ["", "### Entradas", "", *params]
                if calls:
                    cuerpo += ["", "### Lógica que invoca", ""]
                    cuerpo += [f"- `{fields.get(f, f)}.{m_}()`" for f, m_ in calls]
                if cls_comment:
                    cuerpo += ["", f"> [!note] Comentario del controlador\n> {cell(cls_comment)}"]
                name = add_note(f"M{mod} - {route_name(method, route)}", mod, "api", "endpoint",
                                comment or f"`{method} {route}` · acceso: {acceso}.", cuerpo, [rel(p)],
                                alias=[f"{method} {route}"])
                for f, _ in calls:
                    svc = SERVICE_TYPE.get(fields.get(f, ""))
                    if svc and NOTES[svc]["modulo"] == mod:
                        NOTES[name]["enlaces"].append(svc)
                for dto in re.findall(r"@(?:Body|Query)\((?:'\w+')?\) \w+\??: (\w+)", sig):
                    if dto in DTO_CLASS and NOTES[DTO_CLASS[dto]]["modulo"] == mod:
                        NOTES[name]["enlaces"].append(DTO_CLASS[dto])
                ENDPOINTS.append((method, route, name))
                buf = []
                k += 1
                continue
            if line.strip() and not line.startswith("  @"):
                buf = [] if not line.strip().startswith(("//", "/*", "*")) else buf
            k += 1


# ---------------------------------------------------------------- base de datos
def parse_tables() -> None:
    enums: dict[str, str] = {}
    tables: dict[str, dict] = {}
    entity_files = {}
    for p in BE.rglob("entities/*.ts"):
        m = re.search(r"@Entity\('(\w+)'\)", read(p))
        if m:
            entity_files[m.group(1)] = rel(p)
    for p in sorted((BE / "database" / "migrations").glob("*.ts")):
        text = read(p)
        up = text[text.find("async up"):text.find("async down")] if "async down" in text else text
        for m in re.finditer(r"CREATE TYPE (\w+) AS ENUM \(([^)]*)\)", up):
            enums[m.group(1)] = m.group(2)
        for m in re.finditer(r'CREATE TABLE "?(\w+)"? \(', up):
            t = m.group(1)
            start = up.index("(", m.end() - 1)
            end = balanced(up, start)
            inner = up[start + 1:end]
            items, depth, cur = [], 0, ""
            for ch in inner:
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                if ch == "," and depth == 0:
                    items.append(cur)
                    cur = ""
                else:
                    cur += ch
            items.append(cur)
            cols, cons = [], []
            for it in items:
                s = re.sub(r"\s+", " ", it).strip()
                if not s:
                    continue
                if s.upper().startswith("CONSTRAINT"):
                    cons.append(s)
                else:
                    cm = re.match(r'"?(\w+)"? (.*)', s)
                    if cm:
                        cols.append((cm.group(1), cm.group(2)))
            tables[t] = {"cols": cols, "cons": cons, "idx": [], "alter": [], "mig": [rel(p)]}
        for m in re.finditer(r'CREATE (UNIQUE )?INDEX "?(\w+)"?\s+ON "?(\w+)"?(.*?)[`\']\s*,?\s*\)?;?', up, re.S):
            t = m.group(3)
            if t in tables:
                tables[t]["idx"].append(f"{'único ' if m.group(1) else ''}`{m.group(2)}`: {cell(re.sub(chr(10) + r'|\s+', ' ', m.group(4)).strip())}")
        for m in re.finditer(r"ALTER TABLE \"?(\w+)\"?\s+([^`']+)", up):
            if m.group(1) in tables:
                tables[m.group(1)]["alter"].append(re.sub(r"\s+", " ", m.group(2)).strip())
                tables[m.group(1)]["mig"].append(rel(p))
        for m in re.finditer(r'CREATE (UNIQUE )?INDEX "?(\w+)"?\s+ON "?(\w+)"?', up):
            t = m.group(3)
            if t in tables and rel(p) not in tables[t]["mig"]:
                tables[t]["mig"].append(rel(p))
    for t, d in tables.items():
        mod = TABLE_MOD.get(t)
        if not mod:
            continue
        rows = []
        for col, spec in d["cols"]:
            enum = next((e for e in enums if re.search(rf"\b{e}\b", spec)), None)
            extra = f" — valores: {cell(enums[enum])}" if enum else ""
            rows.append(f"| `{col}` | `{cell(spec)}`{extra} |")
        cuerpo = ["### Columnas", "", "| Columna | Definición |", "|---|---|", *rows]
        if d["cons"]:
            cuerpo += ["", "### Restricciones", ""] + [f"- `{cell(c)}`" for c in d["cons"]]
        if d["idx"]:
            cuerpo += ["", "### Índices", ""] + [f"- {i}" for i in d["idx"]]
        if d["alter"]:
            cuerpo += ["", "### Cambios posteriores", ""] + [f"- `{cell(a)[:200]}`" for a in d["alter"]]
        fuentes = list(dict.fromkeys(d["mig"] + ([entity_files[t]] if t in entity_files else [])))
        cuerpo += ["", "### Origen", ""] + [f"- `{f}`" for f in fuentes]
        name = add_note(f"M{mod} - Tabla {t}", mod, "db", "tabla",
                        f"Tabla `{t}` de PostgreSQL ({len(d['cols'])} columnas).", cuerpo, fuentes)
        concept = TABLE_CONCEPT.get(t)
        if concept and (C / f"{concept}.md").exists():
            NOTES[name]["enlaces"].append(concept)


# ---------------------------------------------------------------- frontend
API_CALLS: list[tuple[str, str, str]] = []  # (metodo, ruta normalizada, nota del cliente)


def fe_module(p: Path) -> int | None:
    parts = p.relative_to(FE).parts
    stem = p.stem.replace(".module", "")
    if parts[0] == "features":
        return FE_FEAT_MOD.get(parts[1])
    if parts[0] == "hooks":
        return HOOK_MOD.get(stem)
    if parts[0] == "components":
        return COMPONENT_MOD.get(stem)
    if parts[0] == "auth":
        return 1
    if parts[0] in ("api", "types", "lib"):
        return FE_NAME_MOD.get(stem)
    return None


def fe_name(p: Path, mod: int) -> str:
    parts = p.relative_to(FE).parts
    stem = p.stem
    if parts[0] == "api":
        return f"M{mod} - Cliente API {stem}"
    if parts[0] == "types":
        return f"M{mod} - Tipos {stem}"
    if parts[0] == "lib":
        return f"M{mod} - lib {stem}"
    return f"M{mod} - {stem}"


def parse_frontend() -> None:
    for p in sorted(list(FE.rglob("*.ts")) + list(FE.rglob("*.tsx"))):
        if re.search(r"\.(test|spec)\.tsx?$", p.name) or p.name.endswith(".d.ts"):
            continue
        mod = fe_module(p)
        if not mod:
            continue
        text = read(p)
        lines = text.splitlines()
        exports = []
        for i, line in enumerate(lines):
            m = re.match(r"export (?:default )?(?:async )?(function|const|interface|type|class|enum) (\w+)", line)
            if m:
                exports.append(f"| `{m.group(2)}` | {m.group(1)} | {cell(leading_comment(lines, i)) or '—'} |")
        props = []
        for pm in re.finditer(r"interface (\w+Props) \{([^}]*)\}", text):
            for fld in re.finditer(r"^\s+(\w+)(\?)?[:(]\s*([^;\n]*)", pm.group(2), re.M):
                props.append(f"| `{fld.group(1)}` | {'no' if fld.group(2) else 'sí'} | `{cell(fld.group(3))[:80]}` |")
        calls = []
        if p.relative_to(FE).parts[0] in ("api", "lib"):
            for cm in re.finditer(r"(?:apiFetch|request|fetch)(?:<[^(]*?>)?\(\s*([`'])(?:\$\{API_URL\})?(/.*?)\1(?=(.{0,240}))", text, re.S):
                # Query string o sufijos pegados (`/users${suffix}`) no forman parte de la ruta.
                path = re.split(r"\?|(?<!/)\$\{", cm.group(2))[0]
                path = re.sub(r"\$\{[^}]+\}", ":p", path).rstrip("/") or "/"
                resto = re.split(r"(?:apiFetch|request|fetch)(?:<|\()", cm.group(3))[0]
                method = re.search(r"method: '(\w+)'", resto)
                method = method.group(1) if method else "GET"
                before = text[:cm.start()]
                fn = re.findall(r"(?:export (?:async )?function (\w+)|^  (?:async )?(\w+)\()", before, re.M)
                fname = next((a or b for a, b in reversed(fn) if (a or b)), "?")
                calls.append((method, path, fname))
        cuerpo = []
        rp = p.relative_to(FE).as_posix()
        if rp.startswith("features/") and p.stem.endswith("Page"):
            cuerpo.append(f"Página de la aplicación. Ruta y permiso en [[M{mod} - Interfaz]].")
            cuerpo.append("")
        if exports:
            cuerpo += ["### Exporta", "", "| Nombre | Tipo | Descripción |", "|---|---|---|", *exports, ""]
        if props:
            cuerpo += ["### Props", "", "| Prop | Obligatoria | Tipo |", "|---|---|---|", *props, ""]
        if calls:
            cuerpo += ["### Llamadas a la API", "", "| Función | Método | Ruta |", "|---|---|---|"]
            cuerpo += [f"| `{f}()` | `{m_}` | `{cell(pth)}` |" for m_, pth, f in calls]
            cuerpo.append("")
        kind = ("página" if p.stem.endswith("Page") else "hook" if p.stem.startswith("use") else
                "cliente API" if rp.startswith("api/") else "tipos" if rp.startswith("types/") else
                "utilidad" if rp.startswith("lib/") else "componente" if p.suffix == ".tsx" else "módulo")
        name = add_note(fe_name(p, mod), mod, "ui", kind,
                        file_comment(text) or f"{kind.capitalize()} del frontend (`frontendChapterCoreIEEE/src/{rp}`).",
                        cuerpo, [rel(p)])
        for m_, pth, _ in calls:
            API_CALLS.append((m_, pth, name))
    # enlaces por imports relativos dentro del mismo módulo
    for p in sorted(list(FE.rglob("*.ts")) + list(FE.rglob("*.tsx"))):
        src = BY_FILE.get(rel(p))
        if not src:
            continue
        for imp in re.findall(r"from '(\.[^']+)'", read(p)):
            target = (p.parent / imp).resolve()
            for cand in (target.with_suffix(".ts"), target.with_suffix(".tsx"), target / "index.ts"):
                if cand.exists():
                    note = BY_FILE.get(rel(cand))
                    if note and note != src and NOTES[note]["modulo"] == NOTES[src]["modulo"]:
                        NOTES[src]["enlaces"].append(note)
                    break


def match_route(pattern: str, path: str) -> bool:
    a = [s for s in pattern.strip("/").split("/") if s]
    b = [s for s in path.strip("/").split("/") if s]
    return len(a) == len(b) and all(x.startswith(":") or y == ":p" or x == y for x, y in zip(a, b))


def link_api_calls() -> None:
    for method, route, ep in ENDPOINTS:
        clientes = sorted({n for m_, pth, n in API_CALLS if m_ == method and match_route(route, pth)})
        for cl in clientes:
            if NOTES[cl]["modulo"] == NOTES[ep]["modulo"]:
                NOTES[ep]["enlaces"].append(cl)
                NOTES[ep].setdefault("consumido", []).append(cl)


# ---------------------------------------------------------------- pruebas
def parse_tests() -> None:
    files = [p for p in BE.rglob("*.spec.ts")] + [p for p in FE.rglob("*.test.ts")] + [p for p in FE.rglob("*.test.tsx")]
    for p in sorted(files):
        if p.is_relative_to(BE):
            mod = BE_MOD.get(p.relative_to(BE).parts[0])
        else:
            parts = p.relative_to(FE).parts
            mod = FE_FEAT_MOD.get(parts[1]) if parts[0] == "features" else FE_NAME_MOD.get(p.name.split(".")[0])
        if not mod:
            continue
        text = read(p)
        casos = []
        for m in re.finditer(r"^(\s*)(describe|it|test)(?:\.each\([^)]*\))?\(\s*([`'\"])(.+?)\3", text, re.M):
            indent = "  " * (len(m.group(1)) // 2)
            mark = "**" if m.group(2) == "describe" else ""
            casos.append(f"{indent}- {mark}{cell(m.group(4))}{mark}")
        n_it = sum(1 for c in casos if "**" not in c)
        stem = p.name.rsplit(".", 1)[0]
        name = add_note(f"M{mod} - Prueba {stem}", mod, "test", "prueba",
                        f"{n_it} casos de prueba ({'Jest' if p.is_relative_to(BE) else 'Vitest + Testing Library'}).",
                        ["### Casos", "", *casos] if casos else ["Sin casos detectados."], [rel(p)])
        target_rel = rel(p).replace(".spec.ts", ".ts").replace(".test.tsx", ".tsx").replace(".test.ts", ".ts")
        target = BY_FILE.get(target_rel)
        if target and NOTES[target]["modulo"] == mod:
            NOTES[name]["enlaces"].append(target)


# ---------------------------------------------------------------- escritura
def write_all() -> int:
    for old in C.glob("*.md"):
        if is_generated(old):
            old.unlink()
    for mod in range(1, 7):
        for key, (titulo, desc) in GRUPOS.items():
            miembros = sorted(n for n, d in NOTES.items() if d["modulo"] == mod and d["grupo"] == key)
            if not miembros:
                continue
            gname = f"M{mod} - {titulo}"
            lineas = []
            if key == "ui":
                lineas += frontend_routes(mod)
            por_tipo: dict[str, list[str]] = {}
            for n in miembros:
                por_tipo.setdefault(NOTES[n]["tipo"], []).append(n)
            for tipo, ns in sorted(por_tipo.items()):
                lineas += [f"### {tipo.capitalize()} ({len(ns)})", ""] + [f"- [[{n}]]" for n in ns] + [""]
            write_note(gname, {"type": "grupo", "modulo": mod}, ["chaptercore", f"modulo-{mod}", "grupo"],
                       f"[[M{mod} - Código del módulo]] · [[{CEREBROS[mod]}]]",
                       f"> [!abstract] {titulo}\n> {desc} {len(miembros)} notas generadas desde el código.",
                       lineas, [], [f"M{mod} - Código del módulo", CEREBROS[mod]])
            for n in miembros:
                NOTES[n]["enlaces"].insert(0, gname)
    for name, d in NOTES.items():
        mod = d["modulo"]
        cuerpo = list(d["cuerpo"])
        if d.get("consumido"):
            cuerpo += ["", "### Consumido por el frontend", ""] + [f"- [[{c}]]" for c in sorted(set(d["consumido"]))]
        elif d["tipo"] == "endpoint":
            cuerpo += ["", "> [!question] Sin llamada directa en el frontend",
                       "> No se encontró una llamada a esta ruta en `frontendChapterCoreIEEE/src`. Puede usarse con una",
                       "> URL que devuelve el servidor, desde fuera de la app (p. ej. un QR) o no usarse todavía."]
        enlaces = list(dict.fromkeys(d["enlaces"]))
        write_note(name, {"type": d["tipo"], "modulo": mod}, ["chaptercore", f"modulo-{mod}", d["tipo"].replace(" ", "-")],
                   f"[[{enlaces[0]}]] · [[{CEREBROS[mod]}]]" if enlaces else f"[[{CEREBROS[mod]}]]",
                   f"> [!abstract] {d['tipo'].capitalize()}\n> {cell(d['abstract'])}",
                   cuerpo, d["fuentes"], enlaces[1:], d["alias"])
    return len(NOTES)


def frontend_routes(mod: int) -> list[str]:
    app = read(FE / "App.tsx")
    rows, stack = [], []
    for line in app.splitlines():
        abre = "<Route" in line and not line.rstrip().endswith("/>")
        perm = re.search(r'RequirePermission feature="(\w+)" access="(\w+)"', line)
        pm = re.search(r'<Route path="([^"]+)">', line)
        if abre:
            stack.append(f"{perm.group(1)} · {perm.group(2)}" if perm else
                         "prefijo:" + pm.group(1) if pm else "-")
        m = re.search(r'path="([^"]+)" element=\{<(\w+)', line)
        if m:
            prefix = next((s.split(":", 1)[1] for s in reversed(stack) if s.startswith("prefijo:")), "")
            path = m.group(1) if m.group(1).startswith("/") else f"{prefix}/{m.group(1)}"
            page = m.group(2)
            note = next((n for n, d in NOTES.items() if n.endswith(f" - {page}") and d["modulo"] == mod), None)
            if note:
                guard = next((s for s in reversed(stack) if s != "-" and not s.startswith("prefijo:")), "sesión")
                if path in ("/login", "/activar", "/f/:slug"):
                    guard = "público"
                rows.append(f"| `{path}` | [[{note}]] | {guard} |")
        if "</Route>" in line and stack:
            stack.pop()
    return (["### Rutas", "", "| Ruta | Página | Permiso |", "|---|---|---|", *rows, ""] if rows else [])


def write_note(name, props, tags, migas, abstract, cuerpo, fuentes, enlaces, alias=None) -> None:
    fm = ["---", f"type: {props['type']}", f"modulo: {props['modulo']}", "estado: confirmado", "generado: true"]
    if fuentes:
        fm += ["fuentes:"] + [f"  - {f}" for f in fuentes]
    fm += [f"actualizado: {HOY}"]
    if alias:
        fm += ["aliases:"] + [f'  - "{a}"' for a in alias]
    fm += ["tags:"] + [f"  - {t}" for t in tags] + ["---"]
    body = [*fm, "", f"# {name}", "", migas, "", abstract, "", *cuerpo]
    if enlaces:
        body += ["", "## Enlaces", ""] + [f"- [[{e}]]" for e in enlaces]
    else:
        body += ["", "## Enlaces", "", f"- [[{CEREBROS[props['modulo']]}]]"]
    body += ["", "%% Nota generada por scripts/mapear_repositorio.py: no la edites a mano; se regenera. %%", ""]
    (C / f"{name}.md").write_text("\n".join(body), encoding="utf-8", newline="\n")


def link_code_hubs() -> None:
    for mod in range(1, 7):
        p = C / f"M{mod} - Código del módulo.md"
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8").replace("\r\n", "\n")
        t = re.sub(r"\n## Grupos técnicos\n.*?(?=\n## |\Z)", "\n", t, flags=re.S)
        grupos = [f"M{mod} - {titulo}" for titulo, _ in GRUPOS.values() if (C / f"M{mod} - {titulo}.md").exists()]
        sec = "\n## Grupos técnicos\n\nCada grupo tiene una nota por pieza del código:\n\n" + "\n".join(f"- [[{g}]]" for g in grupos) + "\n"
        t = t.replace("\n## Endpoints del backend", sec + "\n## Endpoints del backend", 1)
        p.write_text(t, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    parse_dtos()
    parse_backend_files()
    link_backend_imports()
    parse_endpoints()
    parse_tables()
    parse_frontend()
    link_api_calls()
    parse_tests()
    total = write_all()
    link_code_hubs()
    por_mod = {m: sum(1 for d in NOTES.values() if d["modulo"] == m) for m in range(1, 7)}
    print(f"Notas generadas: {total} (+ grupos). Por módulo: {por_mod}. Endpoints: {len(ENDPOINTS)}.")
