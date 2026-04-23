#!/usr/bin/env python3
"""Deterministic helpers for the second-brain skill."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import sys
from pathlib import Path


VERSION = "0.1.0"

REQUIRED_DIRS = [
    "raw/inbox",
    "raw/archive",
    "wiki/entities",
    "wiki/concepts",
    "wiki/projects",
    "wiki/questions",
    "wiki/sources",
    "schema",
    "logs",
]

REQUIRED_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "second-brain.yaml",
    "wiki/index.md",
    "logs/events.jsonl",
    "logs/backlog.md",
    "schema/wiki-page.md",
]

CORE_PAGE_STEMS = {"index", "readme"}
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def today() -> str:
    return dt.date.today().isoformat()


def slugify(value: str) -> str:
    slug = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "untitled"


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 2
    while True:
        candidate = parent / f"{stem}-{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def frontmatter(title: str, page_type: str, confidence: str = "medium") -> str:
    return (
        "---\n"
        f"title: {title}\n"
        f"type: {page_type}\n"
        f"updated: {today()}\n"
        f"confidence: {confidence}\n"
        "sources: []\n"
        "---\n\n"
    )


def helper_path() -> str:
    return Path(__file__).resolve().as_posix()


def agents_md() -> str:
    helper = helper_path()
    return f"""# Second Brain Agent Instructions

This workspace is an LLM wiki: raw sources are preserved, while the agent maintains a concise, cross-linked Markdown wiki.

## Commands

### /second-brain-init
Initialize the folder structure and starter files. Prefer:

```bash
python3 {helper} init --root .
```

### /second-brain-ingest SOURCE
Register the source, read the raw material, and update the compiled wiki.

1. Put immutable source material under `raw/inbox/` or register it with `register-source`.
2. Read the source and existing related wiki pages before writing.
3. Update `wiki/sources/`, relevant entity/concept/project/question pages, `wiki/index.md`, and `logs/events.jsonl`.
4. Preserve provenance with raw paths or source links. Mark uncertainty instead of guessing.

### /second-brain-query QUESTION
Answer from the compiled wiki first. Read `wiki/index.md`, then relevant linked pages, then raw sources only when provenance or detail is needed. If the answer produces reusable knowledge, add it to `wiki/questions/` or the relevant concept page and log the update in `logs/events.jsonl`.

### /second-brain-health
Run the static linter and then use agent judgment for semantic checks:

```bash
python3 {helper} health --root .
```

## Wiki Rules
- Keep `raw/` append-only unless the user explicitly asks to clean or archive material.
- Keep wiki pages short, factual, and source-linked.
- Prefer `[[relative/wiki-links]]` for durable cross-links.
- Use `logs/backlog.md` for unresolved contradictions, missing sources, and follow-up questions.
- Do not overwrite user-written notes without reading them first.
"""


def config_yaml() -> str:
    return f"""version: "{VERSION}"
paths:
  raw: "raw"
  wiki: "wiki"
  schema: "schema"
  logs: "logs"
quality:
  stale_days: 90
  require_frontmatter: true
  require_source_traceability: true
commands:
  init: "/second-brain-init"
  ingest: "/second-brain-ingest"
  query: "/second-brain-query"
  health: "/second-brain-health"
"""


def index_md() -> str:
    return frontmatter("Second Brain Index", "index") + """# Second Brain Index

Use this page as the table of contents for the compiled wiki.

## Start Here
- Event log: `logs/events.jsonl`
- Maintenance backlog: `logs/backlog.md`

## Source Pages
Add registered source summaries here, for example `sources/source-id`.

## Concepts
Add durable concepts here, for example `concepts/concept-slug`.

## Entities
Add people, organizations, places, and tools here, for example `entities/entity-slug`.

## Projects
Add project pages here, for example `projects/project-slug`.

## Questions
Add reusable answers here, for example `questions/question-slug`.

## Maintenance Notes
- Prefer synthesis over dumping raw excerpts.
- Keep claims source-linked.
- Move stale or low-confidence items to `logs/backlog.md`.
"""


def events_jsonl() -> str:
    return ""


def backlog_md() -> str:
    return """# Second Brain Backlog

Track unresolved contradictions, weak claims, missing links, and future ingest/query work.

| Date | Type | Item | Owner/Next Step |
|------|------|------|-----------------|
"""


def wiki_page_schema() -> str:
    return """# Wiki Page Schema

Each durable wiki page should start with YAML frontmatter:

```yaml
---
title: Human-readable title
type: source | concept | entity | project | question | index | log | backlog
updated: YYYY-MM-DD
confidence: low | medium | high
sources:
  - raw/inbox/source-file.md
---
```

## Body Sections
- `Summary`: compact synthesis in the agent's own words.
- `Key Facts`: durable claims with provenance.
- `Links`: relevant `[[wiki-links]]`.
- `Open Questions`: uncertainty to revisit later.

## Provenance
Reference raw files, URLs, or source pages close to the claims they support. If a claim is useful but weakly sourced, keep it and mark confidence as `low`.
"""


def raw_readme() -> str:
    return """# Raw Sources

Store immutable inputs here. Use `raw/inbox/` for new material and `raw/archive/` for reviewed material that should remain available for provenance.
"""


def init_wiki(root: Path) -> int:
    root.mkdir(parents=True, exist_ok=True)

    created: list[str] = []
    for directory in REQUIRED_DIRS:
        path = root / directory
        path.mkdir(parents=True, exist_ok=True)
        created.append(directory)

    files = {
        "AGENTS.md": agents_md(),
        "CLAUDE.md": agents_md(),
        "second-brain.yaml": config_yaml(),
        "raw/README.md": raw_readme(),
        "wiki/index.md": index_md(),
        "logs/events.jsonl": events_jsonl(),
        "logs/backlog.md": backlog_md(),
        "schema/wiki-page.md": wiki_page_schema(),
    }
    for relative, content in files.items():
        if write_if_missing(root / relative, content):
            created.append(relative)

    print(f"Initialized second-brain wiki at {root}")
    print(f"Created or verified {len(created)} directories/files.")
    return 0


def append_once(path: Path, marker: str, text: str) -> None:
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if marker in current:
        return
    if current and not current.endswith("\n"):
        current += "\n"
    path.write_text(current + text, encoding="utf-8")


def append_event(root: Path, event: dict[str, str]) -> None:
    path = root / "logs" / "events.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")


def register_source(root: Path, source: Path) -> int:
    if not source.exists() or not source.is_file():
        print(f"Source file not found: {source}", file=sys.stderr)
        return 2

    init_wiki(root)

    title = source.stem.strip() or "Untitled"
    slug = slugify(title)
    destination = unique_path(root / "raw" / "inbox" / f"{today()}-{slug}{source.suffix}")
    shutil.copy2(source, destination)

    source_id = destination.stem
    raw_ref = rel(destination, root)
    stub = root / "wiki" / "sources" / f"{source_id}.md"
    stub_content = (
        "---\n"
        f"title: {title}\n"
        "type: source\n"
        f"updated: {today()}\n"
        "confidence: low\n"
        "sources:\n"
        f"  - {raw_ref}\n"
        "---\n\n"
        f"# {title}\n\n"
        "## Summary\n"
        "Pending LLM synthesis.\n\n"
        "## Source\n"
        f"- `{raw_ref}`\n\n"
        "## Extracted Claims\n"
        "- Pending.\n\n"
        "## Links\n"
        "- [[index]]\n"
    )
    write_if_missing(stub, stub_content)

    index_entry = f"- [[sources/{source_id}]] - {title}\n"
    append_once(root / "wiki" / "index.md", f"[[sources/{source_id}]]", f"\n{index_entry}")

    append_event(
        root,
        {
            "date": today(),
            "event": "ingest-registered",
            "subject": title,
            "source": raw_ref,
            "wiki_page": f"wiki/sources/{source_id}.md",
            "notes": f"Created wiki/sources/{source_id}.md for synthesis.",
        },
    )

    print(f"Registered source: {raw_ref}")
    print(f"Created source page: {rel(stub, root)}")
    return 0


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    block = text[4:end].strip()
    values: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    return values


def issue(severity: str, code: str, path: str, message: str, **extra: str) -> dict[str, str]:
    data = {
        "severity": severity,
        "code": code,
        "path": path,
        "message": message,
    }
    data.update(extra)
    return data


def wiki_pages(root: Path) -> list[Path]:
    wiki = root / "wiki"
    if not wiki.exists():
        return []
    return sorted(path for path in wiki.rglob("*.md") if path.is_file())


def page_lookup(root: Path, pages: list[Path]) -> dict[str, Path]:
    lookup: dict[str, Path] = {}
    wiki = root / "wiki"
    for page in pages:
        relative = page.relative_to(wiki).with_suffix("").as_posix()
        lookup[relative.lower()] = page
        lookup[page.stem.lower()] = page
        lookup[slugify(page.stem)] = page
    return lookup


def resolve_wikilink(target: str, lookup: dict[str, Path]) -> Path | None:
    normalized = target.strip().strip("/")
    if normalized.endswith(".md"):
        normalized = normalized[:-3]
    candidates = [
        normalized.lower(),
        slugify(normalized),
        normalized.replace(" ", "-").lower(),
    ]
    for candidate in candidates:
        if candidate in lookup:
            return lookup[candidate]
    return None


def health_report(root: Path, stale_days: int) -> dict[str, object]:
    issues: list[dict[str, str]] = []

    for directory in REQUIRED_DIRS:
        path = root / directory
        if not path.is_dir():
            issues.append(
                issue(
                    "error",
                    "missing-required-directory",
                    directory,
                    f"Required directory `{directory}` is missing.",
                )
            )

    for required_file in REQUIRED_FILES:
        path = root / required_file
        if not path.is_file():
            issues.append(
                issue(
                    "error",
                    "missing-required-file",
                    required_file,
                    f"Required file `{required_file}` is missing.",
                )
            )

    pages = wiki_pages(root)
    lookup = page_lookup(root, pages)
    inbound: dict[Path, int] = {page: 0 for page in pages}
    all_wiki_text: list[str] = []
    today_date = dt.date.today()

    for page in pages:
        text = page.read_text(encoding="utf-8")
        all_wiki_text.append(text)
        page_rel = rel(page, root)
        meta = parse_frontmatter(text)

        if not meta:
            issues.append(
                issue(
                    "warning",
                    "missing-frontmatter",
                    page_rel,
                    "Wiki page has no YAML frontmatter.",
                )
            )
        else:
            updated = meta.get("updated")
            if updated:
                try:
                    updated_date = dt.date.fromisoformat(updated)
                except ValueError:
                    issues.append(
                        issue(
                            "warning",
                            "invalid-updated-date",
                            page_rel,
                            "`updated` should use YYYY-MM-DD.",
                        )
                    )
                else:
                    age = (today_date - updated_date).days
                    if age > stale_days:
                        issues.append(
                            issue(
                                "warning",
                                "stale-page",
                                page_rel,
                                f"Page has not been updated for {age} days.",
                            )
                        )

        for match in WIKILINK_RE.finditer(text):
            target = match.group(1).strip()
            resolved = resolve_wikilink(target, lookup)
            if resolved is None:
                issues.append(
                    issue(
                        "error",
                        "broken-wikilink",
                        page_rel,
                        f"Wiki link `[[{target}]]` does not resolve.",
                        target=target,
                    )
                )
            else:
                inbound[resolved] = inbound.get(resolved, 0) + 1

        if "TODO VERIFY" in text or "CONTRADICTION" in text:
            issues.append(
                issue(
                    "warning",
                    "explicit-uncertainty-marker",
                    page_rel,
                    "Page contains an explicit uncertainty marker; move it to backlog if unresolved.",
                )
            )

    for page, count in inbound.items():
        if page.stem.lower() in CORE_PAGE_STEMS:
            continue
        if page.parent.name == "sources":
            continue
        if count == 0:
            issues.append(
                issue(
                    "warning",
                    "orphan-page",
                    rel(page, root),
                    "Wiki page has no inbound wikilinks.",
                )
            )

    wiki_blob = "\n".join(all_wiki_text)
    raw_root = root / "raw"
    if raw_root.exists():
        for raw_file in sorted(path for path in raw_root.rglob("*") if path.is_file()):
            if raw_file.name == "README.md" or raw_file.name.startswith("."):
                continue
            raw_ref = rel(raw_file, root)
            if raw_ref not in wiki_blob:
                issues.append(
                    issue(
                        "warning",
                        "unreferenced-raw-source",
                        raw_ref,
                        "Raw source is not referenced by any wiki page.",
                    )
                )

    error_count = sum(1 for item in issues if item["severity"] == "error")
    warning_count = sum(1 for item in issues if item["severity"] == "warning")
    return {
        "ok": error_count == 0,
        "root": str(root),
        "summary": {
            "pages": len(pages),
            "errors": error_count,
            "warnings": warning_count,
        },
        "issues": issues,
    }


def print_human_report(report: dict[str, object]) -> None:
    summary = report["summary"]
    assert isinstance(summary, dict)
    print(f"Second-brain health for {report['root']}")
    print(
        f"Pages: {summary['pages']} | "
        f"Errors: {summary['errors']} | "
        f"Warnings: {summary['warnings']}"
    )
    for item in report["issues"]:
        assert isinstance(item, dict)
        print(f"- [{item['severity']}] {item['code']} {item['path']}: {item['message']}")


def run_health(root: Path, stale_days: int, json_output: bool) -> int:
    report = health_report(root, stale_days)
    if json_output:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print_human_report(report)
    return 0 if report["ok"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="second-brain helper CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="initialize a second-brain wiki")
    init_parser.add_argument("--root", default=".", type=Path, help="wiki root directory")

    register_parser = subparsers.add_parser("register-source", help="copy a raw source and create a source stub")
    register_parser.add_argument("source", type=Path, help="source file to register")
    register_parser.add_argument("--root", default=".", type=Path, help="wiki root directory")

    health_parser = subparsers.add_parser("health", help="run static health checks")
    health_parser.add_argument("--root", default=".", type=Path, help="wiki root directory")
    health_parser.add_argument("--stale-days", default=90, type=int, help="days before a page is considered stale")
    health_parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "init":
        return init_wiki(args.root.resolve())
    if args.command == "register-source":
        return register_source(args.root.resolve(), args.source.resolve())
    if args.command == "health":
        return run_health(args.root.resolve(), args.stale_days, args.json)

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
