# HARNESS_BOOTSTRAP

日期：`[YYYY-MM-DD]`

这是一份工程实例化输入文档。

它负责告诉 Codex：

- 要把哪一套 instantiator 用到哪个项目仓库
- 这次实例化哪些 harness 层
- 是否需要同时生成最小代码骨架
- bootstrap 阶段的操作边界是什么

它不替代 `PRODUCT_SPEC.md`。

## 1. 路径与对象

推荐优先写相对语义：

- target repo path：`current repo root`
- product spec path：`PRODUCT_SPEC.md`
- instantiator source path：`bundled skill asset`

只有在确实需要外部 instantiator 源目录时，才写机器相关路径。

## 2. 项目类型

- 项目类型：`backend` / `agent-runtime` / `web-app` / `worker-api` / `other`
- 当前阶段定位：

例如：

- control-plane-first bootstrap
- harness + minimal runtime skeleton
- harness + minimal service skeleton

## 3. 主技术栈

- 语言：
- 框架：
- 数据层：
- 测试框架：
- 其他关键依赖：

## 4. 本次实例化范围

请明确勾选或填写：

- control plane：`yes/no`
- contract plane：`yes/no`
- runtime plane：`yes/no`
- capability plane：`yes/no`
- memory plane：`yes/no`
- verification plane：`yes/no`
- authorization baseline now：`yes/no`
- code skeleton now：`yes/no`

如果 `code skeleton now=yes`，请补充：

- 需要的最小代码骨架类型：
- 本轮只需要到什么程度：

## 5. 架构规则候选

写出当前倾向采用的项目级规则。

例如：

- `async boundary + sync core`
- `only adapters may talk to third-party APIs`
- `workers own external effects`

如果尚未批准，请明确写：

`No project-specific architecture rule has been approved yet.`

## 6. 工具与环境目标

写出本项目预计会由哪些 agent / tooling 协同工作。

例如：

- Codex
- Claude Code
- Cursor
- GitHub Copilot

如果希望输出额外兼容文件，也在这里说明。

例如：

- `CLAUDE.md` compatibility layer needed: `yes/no`
- Copilot instructions needed now: `yes/no`
- Cursor rules needed now: `yes/no`

如果需要这些兼容层，可参考：

- `templates/CLAUDE.template.md`
- `templates/COPILOT_INSTRUCTIONS.template.md`
- `templates/CURSOR_RULES.template.md`

## 6.1 权限与边界预期

写出当前是否已经知道这些边界：

- MCP 是否会使用
- third-party API 是否会使用
- 哪些能力需要 approval
- 是否存在 deny-by-default 的高风险能力
- workspace boundary 是否需要显式记录

如果暂时未知，也请明确写出“当前未批准权限模型”。

## 7. 第一里程碑

写清楚 bootstrap 完成后，Codex 下一步要推进的第一条工作。

例如：

- 建立最小 FastAPI 服务与 `/healthz`
- 建立单 agent runtime 闭环
- 建立第一条数据写入路径

## 8. 非目标

写出本轮 bootstrap 明确不做什么。

例如：

- 不接真实 LLM
- 不加多 agent
- 不加 RAG / MCP
- 不做前端

## 9. Bootstrap 约束

这部分是对 Codex 的直接操作约束。

建议至少覆盖：

- 不要修改 instantiator source
- 只向 target repo 写入
- 先实例化 harness，再决定是否生成代码骨架
- 任何 `L2/L3` 级工作都要先有 active plan
- 行为语义变化要同步更新 contract 文档

## 10. 期望输出

至少列出 bootstrap 后目标仓库中应该出现哪些内容。

例如：

- 根 `AGENTS.md`
- `.agent/*`
- `docs/api/API_CONTRACT.md`
- `docs/data/DATA_CONTRACT.md`
- `docs/runtime/RUNTIME_BASELINE.md`
- `docs/ops/AUTHORIZATION_BASELINE.md`
- `docs/ops/VERIFICATION_BASELINE.md`
- 第一份 `.agent/active-plans/*.md`
- 可选：最小代码骨架
- 可选：`CLAUDE.md` / `.github/copilot-instructions.md` / Cursor rules

## 11. 完成定义

明确 bootstrap 何时算完成。

例如：

- control / contract / runtime / authorization / verification baseline 均已项目化
- 第一份 active plan 已建立
- 已说明当前缺什么、下一步是什么

## 12. 对 Codex 的启动提示

这里可以直接写一段希望交给 Codex 的启动说明。

例如：

```text
请读取 `PRODUCT_SPEC.md` 与 `HARNESS_BOOTSTRAP.md`，
参考 instantiator source 下的 `harness-base/`，
只向 target repo 实例化 harness。
不要修改 instantiator source。
如 bootstrap 范围要求包含 code skeleton，再在 harness 实例化后落最小骨架。
```
