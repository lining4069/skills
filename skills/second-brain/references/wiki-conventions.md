# Wiki Conventions

## Directory Structure

```text
raw/
  inbox/
  archive/
wiki/
  index.md
  sources/
  concepts/
  entities/
  projects/
  questions/
schema/
  wiki-page.md
logs/
  events.jsonl
  backlog.md
second-brain.yaml
AGENTS.md
CLAUDE.md
```

## Page Types

| Type | Path | Purpose |
|------|------|---------|
| `source` | `wiki/sources/<source-id>.md` | One source's summary, provenance, extracted claims, and links |
| `concept` | `wiki/concepts/<slug>.md` | Durable ideas synthesized across sources |
| `entity` | `wiki/entities/<slug>.md` | People, organizations, products, places, standards |
| `project` | `wiki/projects/<slug>.md` | Active work streams, decisions, status, next actions |
| `question` | `wiki/questions/<slug>.md` | Reusable answers and reasoning trails |
| `index` | `wiki/index.md` | Navigation and entry points |

## Frontmatter

```yaml
---
title: Human-readable title
type: source | concept | entity | project | question | index
updated: YYYY-MM-DD
confidence: low | medium | high
sources:
  - raw/inbox/example.md
---
```

Use `confidence: low` for provisional claims, unresolved contradictions, or sources that have not been reviewed.

## Ingest Checklist

1. Register or place the source under `raw/inbox/`.
2. Read `wiki/index.md`, `logs/events.jsonl`, and any likely related pages before editing.
3. Create or update the source page in `wiki/sources/`.
4. Extract durable claims, entities, concepts, decisions, and questions.
5. Merge with existing pages instead of creating duplicates.
6. Add backlinks and update index sections.
7. Move unresolved issues to `logs/backlog.md`.
8. Append a row to `logs/events.jsonl`.

## Query Checklist

1. Start from `wiki/index.md`.
2. Follow links before searching raw files.
3. Distinguish "the wiki says" from "the raw source says."
4. Cite page names and raw paths when the answer depends on provenance.
5. Capture reusable answers only when valuable.

## Health Checklist

Run the static helper first:

```bash
python3 <resolved-second-brain-skill-dir>/scripts/second_brain.py health
```

Then inspect semantic quality:

- Contradictory claims without a backlog entry.
- Pages that are too long and should split into concepts/entities/questions.
- Duplicated pages with similar titles or slugs.
- Claims without nearby source references.
- Index sections that no longer represent the wiki.
- Source pages that never graduated into concept/entity/project pages.
- Low-confidence pages that have not been revisited.

## Link Rules

- Prefer `[[concepts/slug]]`, `[[entities/slug]]`, `[[projects/slug]]`, `[[questions/slug]]`, and `[[sources/source-id]]`.
- Use singular nouns for concepts when possible.
- Keep slugs lowercase, ASCII, and hyphenated.
- Do not rely on raw file names as the only navigation path.

## Logging Format

Append one JSON object per line to `logs/events.jsonl`:

```json
{"date":"YYYY-MM-DD","event":"ingest","subject":"Short subject","source":"raw/inbox/source.md","wiki_page":"wiki/sources/source-id.md","notes":"Updated concepts/example and sources/source-id."}
```

Use event values such as `init`, `ingest-registered`, `ingest`, `query-captured`, `health-fix`, and `archive`. Keep unresolved maintenance work in `logs/backlog.md`.
