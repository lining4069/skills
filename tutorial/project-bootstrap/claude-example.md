# Claude Code Example: Run `project-bootstrap`

This walkthrough shows how to install the `project-bootstrap` workflow skill for Claude Code and use it to take a new repository from raw idea to first action plan.

## 1. Install the Workflow Entry Point

Install the public entry-point skill:

```bash
npx skills add https://github.com/lining4069/skills --skill project-bootstrap -a claude-code --copy -g
```

If you want the helper skills available explicitly as well, install them too:

```bash
npx skills add https://github.com/lining4069/skills --skill brainstorm-to-prd prd-to-bootstrap bootstrap-harness first-plan-seeder -a claude-code --copy -g
```

Restart Claude Code or open a new session after installation.

## 2. Open a New Repository

Create or open the repository where the idea will live:

```bash
mkdir my-new-app
cd my-new-app
claude
```

## 3. Start From a Raw Idea

Ask Claude Code:

```text
Use $project-bootstrap to inspect this repo and move it to the next valid pre-coding artifact.
The product idea is: ...
```

If no approved `PRD.md` exists yet, Claude Code should route into the `brainstorm-to-prd` stage.

## 4. Approve the PRD

During the first stage, Claude Code should:

- ask focused clarification questions
- help narrow the current phase
- write or revise `PRD.md`
- stop for approval before continuing

When the PRD looks right, tell Claude Code explicitly that you approve it.

## 5. Continue to Bootstrap Docs

Run the workflow again:

```text
Use $project-bootstrap to continue this repo to the next valid stage.
```

With an approved `PRD.md`, Claude Code should create:

- `PRODUCT_SPEC.md`
- `HARNESS_BOOTSTRAP.md`

In a normal public install, the generated bootstrap document should usually prefer semantic path values such as:

- `target repo path: current repo root`
- `product spec path: PRODUCT_SPEC.md`
- `instantiator source path: bundled skill asset`

rather than machine-specific absolute paths.

## 6. Instantiate the Harness

Run the same workflow again:

```text
Use $project-bootstrap to continue this repo to the next valid stage.
```

Claude Code should now:

- instantiate `AGENTS.md`
- create `.agent/*`
- create `docs/api/`, `docs/data/`, `docs/runtime/`, and `docs/ops/` contract baselines
- optionally create `CLAUDE.md`, Copilot instructions, and Cursor rules when the bootstrap document asks for them

## 7. Seed the First Action Plan

Run the workflow once more:

```text
Use $project-bootstrap to continue this repo to the next valid stage.
```

Claude Code should create the first `.agent/active-plans/YYYY-MM-DD-first-action-plan.md` and stop there.

That repository is now ready for normal harness-guided development.
