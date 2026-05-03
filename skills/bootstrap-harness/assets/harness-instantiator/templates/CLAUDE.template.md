# CLAUDE.md

这个文件是面向 Claude Code 的兼容层。

建议把它写成“薄适配层”，而不是复制一整套仓库规则。

## 目的

- 告诉 Claude Code 先读哪些 repo-visible harness 文件
- 明确项目的 bootstrap 输入是否仍然 relevant
- 把共享规则导向 `AGENTS.md` 与 `.agent/*`

## 推荐结构

### Required Reading

建议首先读取：

1. `AGENTS.md`
2. `.agent/ARCHITECTURE.md`
3. `.agent/INVARIANTS.md`
4. `.agent/PLANS.md`
5. `.agent/RUNTIME.md`
6. `.agent/MEMORY.md`
7. `docs/api/API_CONTRACT.md` if touching API semantics
8. `docs/data/DATA_CONTRACT.md` if touching persistence semantics
9. `docs/runtime/RUNTIME_BASELINE.md` if touching runtime behavior
10. `docs/ops/AUTHORIZATION_BASELINE.md` if touching permissions or approvals
11. `docs/ops/VERIFICATION_BASELINE.md` if touching verification semantics

### Local Claude Notes

只在这里写：

- 仅 Claude Code 才需要知道的本地说明
- hooks / subagents / memory 相关的项目化约定

不要把共享 contract 全量复制到这里。
