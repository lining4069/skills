# Future Plugin Skeleton: `project-bootstrap`

This document describes the recommended directory skeleton if the `project-bootstrap` workflow evolves from a public skills bundle into a publishable plugin.

## Goal

Keep the plugin thin and compositional:

- the **public product name** stays `project-bootstrap`
- the **workflow logic** remains split across reusable helper skills
- the plugin mainly provides packaging, versioning, optional commands, and workflow convenience

## Recommended Shape

```text
project-bootstrap-plugin/
  .codex-plugin/
    plugin.json
  README.md
  CHANGELOG.md
  skills/
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
        harness-instantiator/
    first-plan-seeder/
      SKILL.md
  templates/
    PRODUCT_SPEC.template.md
    HARNESS_BOOTSTRAP.template.md
  docs/
    workflow.md
    compatibility.md
  examples/
    raw-idea-example.md
    approved-prd-example.md
    bootstrap-output-example.md
  tests/
    test_plugin_package.py
    test_workflow_docs.py
```

## Role Of Each Layer

### `.codex-plugin/`

Defines plugin metadata, packaging, marketplace-facing identity, and any plugin-specific configuration.

### `skills/`

Contains the actual reusable workflow units.

This should remain the functional core of the plugin so the logic is still reusable outside the plugin host when needed.

### `templates/`

Contains top-level publish templates that should be easy to reference from docs and examples without digging through skill internals.

### `docs/`

Holds host-agnostic documentation:

- workflow overview
- stage model
- compatibility and expectations

### `examples/`

Shows concrete artifact evolution:

- idea
- PRD
- bootstrap docs
- instantiated harness

### `tests/`

Checks packaging quality, publishability, and absence of machine-local leakage.

## Naming Recommendation

If this becomes a plugin, keep:

- plugin name: `project-bootstrap`
- top-level user-facing command or intent: `project-bootstrap`

Keep helper names unchanged:

- `brainstorm-to-prd`
- `prd-to-bootstrap`
- `bootstrap-harness`
- `first-plan-seeder`

This preserves discoverability while keeping the workflow internals explicit.

## Migration Strategy From The Current Skills Repo

If you later build the plugin:

1. treat the current `project-bootstrap` skill as the source of truth for the public workflow entry point
2. vendor the helper skills into the plugin under `skills/`
3. vendor the bundled `harness-instantiator` snapshot from `bootstrap-harness/assets/`
4. move host-specific install instructions from the skills repo into plugin docs
5. keep the skills repo and plugin repo versioned separately

## Why Not Collapse Everything Into One Huge Skill

Because the current decomposition gives you:

- clearer stage boundaries
- easier testing
- easier reuse
- better future host compatibility

The plugin should package the workflow, not erase its internal architecture.
