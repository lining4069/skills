# Harness Base

这个目录是 instantiator source 的核心骨架。

在 `harness-instantiator/` 中，它的角色是：

- 只读参考源
- 实例化模板源

在目标仓库中，它的内容会被复制、改写并项目化，成为真正参与开发的：

- `AGENTS.md`
- `.agent/*`
- `docs/api/*`
- `docs/data/*`
- `docs/runtime/*`
- `docs/ops/*`

不要把这个目录当成业务项目来开发。
