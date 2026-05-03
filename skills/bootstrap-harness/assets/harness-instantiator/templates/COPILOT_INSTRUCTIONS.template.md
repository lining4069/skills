# copilot-instructions.md

这个模板用于生成 `.github/copilot-instructions.md`。

目标是为 GitHub Copilot 提供一个薄的仓库入口，而不是复制整套 harness。

## Recommended Instructions

- Read `AGENTS.md` before making non-trivial changes.
- Treat `.agent/*` files as the repository control plane.
- Use `docs/api/API_CONTRACT.md` for API semantics.
- Use `docs/data/DATA_CONTRACT.md` for persistence semantics.
- Use `docs/runtime/RUNTIME_BASELINE.md` for runtime semantics.
- Use `docs/ops/AUTHORIZATION_BASELINE.md` for permission and approval boundaries.
- Use `docs/ops/VERIFICATION_BASELINE.md` for verification expectations.
- For `L2` and `L3` changes, require an active plan before implementation.
- Update contract docs in the same change when semantics change.
