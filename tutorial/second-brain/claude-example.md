# Claude Code Example: Build `lining'sWiki`

This walkthrough installs the `second-brain` skill for Claude Code, creates a personal LLM Wiki named `lining'sWiki`, and opens it with Obsidian.

## 1. Install the Skill

Install `second-brain` globally for Claude Code:

```bash
npx skills add https://github.com/lining4069/skills --skill second-brain -a claude-code --copy -g
```

Restart Claude Code or open a new Claude Code session after installation.

## 2. Create the Wiki Folder

This example creates the wiki at:

```text
/Users/lining/Documents/llm-wiki/lining'sWiki
```

Because the folder name contains an apostrophe, wrap the path in double quotes:

```bash
mkdir -p "/Users/lining/Documents/llm-wiki/lining'sWiki"
cd "/Users/lining/Documents/llm-wiki/lining'sWiki"
```

## 3. Start Claude Code in the Wiki Folder

From inside the wiki folder, start Claude Code:

```bash
claude
```

Then ask Claude Code:

```text
/second-brain init
```

By default, `second-brain` uses the current directory as the wiki root. Since you already ran `cd "/Users/lining/Documents/llm-wiki/lining'sWiki"`, you do not need to pass `--root .`.

Equivalent absolute-path form:

```text
/second-brain init --root "/Users/lining/Documents/llm-wiki/lining'sWiki"
```

Expected structure:

```text
lining'sWiki/
  AGENTS.md
  CLAUDE.md
  second-brain.yaml
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
  logs/
    events.jsonl
    backlog.md
```

## 4. Add Raw Sources

Put raw notes, article exports, meeting notes, or markdown files under `raw/inbox/`.

Example from a shell:

```bash
cp "/path/to/source.md" "/Users/lining/Documents/llm-wiki/lining'sWiki/raw/inbox/"
```

Example from inside the wiki folder:

```bash
cp "/path/to/source.md" raw/inbox/
```

## 5. Ingest Sources

In Claude Code, ask:

```text
/second-brain ingest raw/inbox/source.md
```

During ingest, Claude Code should:

- Preserve the raw file under `raw/`.
- Update or create a source page under `wiki/sources/`.
- Update durable concept/entity/project/question pages.
- Add wikilinks and source references.
- Update `wiki/index.md` and `logs/events.jsonl`.
- Put unresolved contradictions or weak claims in `logs/backlog.md`.

## 6. Query the Wiki

Ask questions against the compiled wiki:

```text
/second-brain query "LLM Wiki 和 RAG 的核心区别是什么？"
```

If an answer is worth keeping, ask Claude Code to persist it:

```text
把这个答案沉淀到 wiki/questions/，并更新相关概念页和 log。
```

## 7. Run Health Checks

Run a structural and semantic health check:

```text
/second-brain health
```

To let Claude Code fix safe issues:

```text
/second-brain health 并修复安全的断链、孤页和索引问题，不要删除 raw 文件。
```

The deterministic helper checks required folders/files, broken wikilinks, stale pages, orphan pages, and unreferenced raw sources. Claude Code should then inspect semantic issues such as duplicate concepts, vague provenance, contradictions, and low-confidence claims.

## 8. Open With Obsidian

Open Obsidian and choose:

```text
Open folder as vault
```

Select:

```text
/Users/lining/Documents/llm-wiki/lining'sWiki
```

Start from:

```text
wiki/index.md
```

Obsidian will understand wikilinks such as `[[log]]`, `[[backlog]]`, `[[concepts/example]]`, and `[[sources/source-id]]`.

## Daily Workflow

Use this loop:

1. Save new material into `raw/inbox/`.
2. Run `/second-brain ingest <source>`.
3. Read and edit the compiled wiki in Obsidian.
4. Ask `/second-brain query ...` when you need synthesized answers.
5. Run `/second-brain health` regularly.

## Common Path Patterns

When already inside the wiki folder, rely on the default current-directory root:

```text
/second-brain health
```

From any other directory:

```text
/second-brain health --root "/Users/lining/Documents/llm-wiki/lining'sWiki"
```

Both forms target the same wiki. The `.` form is shorter; the absolute-path form is clearer when you are not currently inside the wiki folder.
