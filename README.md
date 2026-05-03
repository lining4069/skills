# Skills Repository

[English](README.md) | [简体中文](README.zh-CN.md)

This repository publishes portable AI-agent skills that can be installed with the Skills CLI.

## Available Skills

| Skill | Purpose |
|-------|---------|
| `second-brain` | Build and maintain a Karpathy-style LLM wiki / personal knowledge base. |
| `project-bootstrap` | Orchestrate a new project from raw idea to approved PRD, bootstrap docs, harness instantiation, and first action plan. |
| `brainstorm-to-prd` | Turn a raw project idea into a reviewable and approvable `PRD.md`. |
| `prd-to-bootstrap` | Derive `PRODUCT_SPEC.md` and `HARNESS_BOOTSTRAP.md` from an approved `PRD.md`. |
| `bootstrap-harness` | Instantiate a repo control plane and contract baseline from bootstrap docs. |
| `first-plan-seeder` | Create the first `.agent/active-plans/...` execution plan after harness bootstrap. |

## Tutorials

- [Claude Code example: build `lining'sWiki`](tutorial/second-brain/claude-example.md)
- [Claude Code example: run the `project-bootstrap` workflow](tutorial/project-bootstrap/claude-example.md)
- [Future plugin skeleton for `project-bootstrap`](tutorial/project-bootstrap/plugin-skeleton.md)

## Naming Notes

This repository follows two naming rules borrowed from public skill collections such as Anthropic's skills repository and Superpowers:

- each individual skill name should be short, lowercase, hyphenated, and describe one concrete job
- when multiple helper skills form a larger workflow, expose one public entry-point name for discovery and keep the helper names focused on their stage

For that reason:

- the public workflow entry point is `project-bootstrap`
- helper skills stay explicit: `brainstorm-to-prd`, `prd-to-bootstrap`, `bootstrap-harness`, and `first-plan-seeder`

If this workflow later becomes a plugin or bundle, `project-bootstrap` is the recommended public name.

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

Install the project-bootstrap workflow entry point for Claude Code:

```bash
npx skills add https://github.com/lining4069/skills --skill project-bootstrap -a claude-code --copy -g
```

Use it in Claude Code with prompts such as:

```text
Use $project-bootstrap to inspect this repo and move it to the next valid pre-coding artifact.
Use $project-bootstrap to take this new project from raw idea to an approved PRD.
Use $project-bootstrap to continue from an approved PRD into bootstrap docs and the first action plan.
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

Install the project-bootstrap workflow entry point for Codex:

```bash
npx skills add https://github.com/lining4069/skills --skill project-bootstrap -a codex --copy -g
```

Use it in Codex as:

```text
Use $project-bootstrap to inspect the repo stage and move it to the next artifact.
Use $project-bootstrap to turn this raw app idea into an approved PRD.
Use $project-bootstrap to continue from PRD to bootstrap docs and the first action plan.
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

You can also install the `project-bootstrap` workflow skill for OpenCode:

```bash
npx skills add https://github.com/lining4069/skills --skill project-bootstrap -a opencode --copy -g
```

Use the installed `project-bootstrap` skill from OpenCode with the same workflow intent: detect the current stage and move the project to the next valid pre-coding artifact.

### Project-Level Install

Omit `-g` when you want to install into the current project instead of the user-level agent directories:

```bash
npx skills add https://github.com/lining4069/skills --skill second-brain -a claude-code codex opencode --copy
```

For a project-local pre-coding workflow install:

```bash
npx skills add https://github.com/lining4069/skills --skill project-bootstrap -a claude-code codex opencode --copy
npx skills add https://github.com/lining4069/skills --skill brainstorm-to-prd -a claude-code codex opencode --copy
npx skills add https://github.com/lining4069/skills --skill prd-to-bootstrap -a claude-code codex opencode --copy
npx skills add https://github.com/lining4069/skills --skill bootstrap-harness -a claude-code codex opencode --copy
npx skills add https://github.com/lining4069/skills --skill first-plan-seeder -a claude-code codex opencode --copy
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
  project-bootstrap/
    SKILL.md
    references/
  brainstorm-to-prd/
    SKILL.md
    references/
  prd-to-bootstrap/
    SKILL.md
    references/
  bootstrap-harness/
    SKILL.md
    assets/
  first-plan-seeder/
    SKILL.md
```

Add future skills as `skills/<skill-name>/SKILL.md`, for example `skills/new-skill/SKILL.md`.

No npm package is required for the skill itself; `npx skills add` downloads the repository and copies or symlinks the selected skill into the target CLI's skill directory.

## Skills CLI Discovery

`npx skills add <repo> --skill <name>` scans the repository for `SKILL.md` files and matches the `name` field in frontmatter. In this repository, for example:

- `second-brain` resolves to `skills/second-brain/SKILL.md`
- `project-bootstrap` resolves to `skills/project-bootstrap/SKILL.md`
- `brainstorm-to-prd` resolves to `skills/brainstorm-to-prd/SKILL.md`

Use `--list` to verify discovery before installing:

```bash
npx skills add https://github.com/lining4069/skills --list
```
