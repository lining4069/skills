# Skills Repository

This repository publishes portable AI-agent skills that can be installed with the Skills CLI.

## Available Skills

| Skill | Purpose |
|-------|---------|
| `second-brain` | Build and maintain a Karpathy-style LLM wiki / personal knowledge base. |

## Tutorials

- [Claude Code example: build `lining'sWiki`](tutorial/second-brain/claude-example.md)

## Install

### Claude Code

```bash
npx skills add https://github.com/lining4069/skills --skill second-brain -a claude-code --copy -g
```

The skill is installed to:

```text
~/.claude/skills/second-brain
```

Use it in Claude Code as:

```text
/second-brain init
/second-brain ingest ./notes/source.md
/second-brain query "What does my wiki say about LLM Wiki vs RAG?"
/second-brain health
```

### Codex

```bash
npx skills add https://github.com/lining4069/skills --skill second-brain -a codex --copy -g
```

The skill is installed to:

```text
~/.codex/skills/second-brain
```

Use it in Codex as:

```text
Use $second-brain to initialize a second brain in the current workspace.
Use $second-brain to ingest ./notes/source.md into this wiki.
Use $second-brain to query "What are the main unresolved questions?"
Use $second-brain to run a health check and fix safe issues.
```

### OpenCode

```bash
npx skills add https://github.com/lining4069/skills --skill second-brain -a opencode --copy -g
```

The skill is installed to:

```text
~/.config/opencode/skills/second-brain
```

Use the installed `second-brain` skill from OpenCode with the same intents: `init`, `ingest`, `query`, and `health`.

### Project-Level Install

Omit `-g` when you want to install into the current project instead of the user-level agent directories:

```bash
npx skills add https://github.com/lining4069/skills --skill second-brain -a claude-code codex opencode --copy
```

## Local Development

Validate the helper CLI with:

```bash
python3 -B -m unittest discover -s tests
```

The test suite checks helper behavior, basic skill frontmatter, required publish files, and accidental local-machine path leaks.

You can also validate the skill folder with a target host's validator when available. For Codex-style validation:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py second-brain
```

That optional validator requires `PyYAML` in the Python environment used to run it.

## Repository Shape

This repository follows the common multi-skill layout used by public skill collections:

```text
skills/
  second-brain/
    SKILL.md
    scripts/
    references/
    assets/
    agents/
```

Add future skills as `skills/<skill-name>/SKILL.md`, for example `skills/new-skill/SKILL.md`.

No npm package is required for the skill itself; `npx skills add` downloads the repository and copies or symlinks the selected skill into the target CLI's skill directory.

## Skills CLI Discovery

`npx skills add <repo> --skill <name>` scans the repository for `SKILL.md` files and matches the `name` field in frontmatter. In this repository, `second-brain` resolves to `skills/second-brain/SKILL.md`.

Use `--list` to verify discovery before installing:

```bash
npx skills add https://github.com/lining4069/skills --list
```
