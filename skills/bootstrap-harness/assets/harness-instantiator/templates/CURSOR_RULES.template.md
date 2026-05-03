# Cursor Rules Template

这个模板用于生成 Cursor 项目的规则文件内容。

请根据你实际采用的 Cursor 规则载体，将下面内容写入对应位置。

## Recommended Rules

- Start with `AGENTS.md`.
- Treat `.agent/*` as the project control plane.
- If `PRODUCT_SPEC.md` and `HARNESS_BOOTSTRAP.md` still exist and are still relevant, read them before bootstrap-adjacent work.
- For API work, read `docs/api/API_CONTRACT.md`.
- For data work, read `docs/data/DATA_CONTRACT.md`.
- For runtime work, read `docs/runtime/RUNTIME_BASELINE.md`.
- For permission or approval changes, read `docs/ops/AUTHORIZATION_BASELINE.md`.
- For verification changes, read `docs/ops/VERIFICATION_BASELINE.md`.
- Do not treat template text as project fact after bootstrap; rely on instantiated repo files.
