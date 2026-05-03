# Project Bootstrap Checklist

这份清单用于验收一个新项目是否已经从 instantiator source 正确实例化为受 Harness Engineering 约束的目标仓库。

推荐配合：

- `PRODUCT_SPEC.md`
- `HARNESS_BOOTSTRAP.md`
- `harness-instantiator/harness-base/`

一起使用。

## 一、工作区准备

1. 是否已经存在真正的目标仓库目录
2. 是否保留 `harness-instantiator/` 作为只读参考源
3. 是否使用父工作区打开，保证 Codex 同时能读到目标仓库与 instantiator

## 二、输入文件准备

1. 目标仓库根目录下是否存在 `PRODUCT_SPEC.md`
2. 目标仓库根目录下是否存在 `HARNESS_BOOTSTRAP.md`
3. `PRODUCT_SPEC.md` 是否已经写清楚项目目标、当前阶段范围、非目标和成功标准
4. `HARNESS_BOOTSTRAP.md` 是否已经写清楚：
   - target repo path
   - instantiator source path
   - project type
   - stack
   - instantiate scope
   - first milestone
   - non-goals
   - bootstrap constraints

## 三、实例化边界

1. Codex 是否被明确告知只能写目标仓库
2. Codex 是否被明确告知不要修改 instantiator 源目录
3. 是否已经明确这次只落 harness，还是同时落最小代码骨架

## 四、控制面实例化检查

1. 根 `AGENTS.md` 是否已经项目化
2. `.agent/ARCHITECTURE.md` 是否写了真实架构边界
3. `.agent/PLANS.md` 是否与项目 change level 规则兼容
4. `.agent/INVARIANTS.md` 是否已有真实 invariant ID
5. `.agent/IMPLEMENTATION_STATUS.md` 是否反映当前项目状态
6. `.agent/RUNTIME.md` 是否写了当前 runtime baseline
7. `.agent/MEMORY.md` 是否写了当前 memory strategy
8. `.agent/TOOLS.md` 是否与当前 capability 边界一致

## 五、Contract Plane 检查

1. `docs/api/API_CONTRACT.md` 是否已有 baseline
2. `docs/data/DATA_CONTRACT.md` 是否已有 baseline
3. 是否明确哪些 contract 当前未启用，而不是留成模糊模板占位

## 六、Capability / Authorization Plane 检查

1. `docs/ops/AUTHORIZATION_BASELINE.md` 是否已说明：
   - auth boundary
   - permission model
   - approval requirement 或当前未启用
   - workspace / MCP / external API scope
2. `.agent/TOOLS.md` 是否与上述授权边界一致

## 七、Runtime / Verification Plane 检查

1. `docs/runtime/RUNTIME_BASELINE.md` 是否已说明：
   - execution model
   - retries / budgets
   - pause / resume 或当前未启用
   - approval / HITL 或当前未启用
   - scheduling / background work 或当前未启用
2. `docs/ops/VERIFICATION_BASELINE.md` 是否已说明：
   - regression expectations
   - trace / log / metrics / audit baseline
   - release gates

## 八、第一份 active plan

1. `.agent/active-plans/` 下是否已有第一份 active plan
2. 该 plan 是否说明了：
   - goal
   - scope / non-goals
   - change metadata
   - contract impact
   - test plan
   - implementation sequence
3. 如果是 `L2` 或 `L3` 级任务，是否已经明确 approval / rollback 需求

## 九、模板污染检查

1. 是否仍残留明显模板占位
2. 是否把 instantiator 示例误当成项目事实
3. 是否误把未批准的架构规则写进目标仓库

## 十、最小启动判定

满足以下条件即可进入正式开发：

1. 根 `AGENTS.md` 已项目化
2. 至少 3 条真实 invariants 已存在
3. API / data / runtime / authorization / verification baseline 已写
4. 第一份 active plan 已建立
5. 团队或 agent 已知道哪些改动必须走 `L2` / `L3`

## 十一、bootstrap 完成后的建议动作

1. 关闭父工作区
2. 只打开目标仓库
3. 让 Codex 从目标仓库的 `AGENTS.md` 开始工作
4. 用第一份 active plan 启动真正的里程碑开发
