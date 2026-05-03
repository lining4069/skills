# Skills 仓库

[English](README.md) | [简体中文](README.zh-CN.md)

这个仓库发布可移植的 AI Agent Skills，可通过 Skills CLI 安装到不同宿主环境中。

## 当前可用 Skills

| Skill | 作用 |
|-------|------|
| `second-brain` | 构建和维护 Karpathy 风格的 LLM Wiki / 个人第二大脑。 |
| `project-bootstrap` | 把一个新项目从原始想法推进到 PRD、bootstrap 文档、harness 实例化和第一份 action plan。 |
| `brainstorm-to-prd` | 将原始项目想法收敛成可评审、可批准的 `PRD.md`。 |
| `prd-to-bootstrap` | 从已批准的 `PRD.md` 派生 `PRODUCT_SPEC.md` 和 `HARNESS_BOOTSTRAP.md`。 |
| `bootstrap-harness` | 根据 bootstrap 文档实例化仓库的控制面与 contract baseline。 |
| `first-plan-seeder` | 在 harness 实例化后生成第一份 `.agent/active-plans/...` 执行计划。 |

## 教程

- [Claude Code 示例：构建个人 LLM Wiki](tutorial/second-brain/claude-example.md)
- [Claude Code 示例：运行 `project-bootstrap` 工作流](tutorial/project-bootstrap/claude-example.md)
- [`project-bootstrap` 未来 plugin 骨架](tutorial/project-bootstrap/plugin-skeleton.md)

## 命名约定

这个仓库参考了 Anthropic skills 仓库与 Superpowers 的常见实践：

- 每个单独的 skill 名称应简短、小写、连字符分隔，并直接表达它的职责。
- 当多个 helper skills 组成一条完整工作流时，对外暴露一个更容易发现的公共入口名称。

因此：

- 这条前开发阶段工作流的公共入口名是 `project-bootstrap`
- helper skills 保持显式命名：`brainstorm-to-prd`、`prd-to-bootstrap`、`bootstrap-harness`、`first-plan-seeder`

如果后续这套工作流演进为 plugin，推荐继续使用 `project-bootstrap` 作为公开名称。

## 安装

### Claude Code

安装 `second-brain`：

```bash
npx skills add https://github.com/lining4069/skills --skill second-brain -a claude-code --copy -g
```

安装 `project-bootstrap` 工作流入口：

```bash
npx skills add https://github.com/lining4069/skills --skill project-bootstrap -a claude-code --copy -g
```

在 Claude Code 中可以这样使用：

```text
Use $project-bootstrap to inspect this repo and move it to the next valid pre-coding artifact.
Use $project-bootstrap to take this new project from raw idea to an approved PRD.
Use $project-bootstrap to continue from an approved PRD into bootstrap docs and the first action plan.
```

### Codex

安装 `second-brain`：

```bash
npx skills add https://github.com/lining4069/skills --skill second-brain -a codex --copy -g
```

安装 `project-bootstrap`：

```bash
npx skills add https://github.com/lining4069/skills --skill project-bootstrap -a codex --copy -g
```

在 Codex 中可以这样使用：

```text
Use $project-bootstrap to inspect the repo stage and move it to the next artifact.
Use $project-bootstrap to turn this raw app idea into an approved PRD.
Use $project-bootstrap to continue from PRD to bootstrap docs and the first action plan.
```

### OpenCode

安装 `second-brain`：

```bash
npx skills add https://github.com/lining4069/skills --skill second-brain -a opencode --copy -g
```

安装 `project-bootstrap`：

```bash
npx skills add https://github.com/lining4069/skills --skill project-bootstrap -a opencode --copy -g
```

### 项目级安装

如果希望安装到当前项目而不是全局目录，请省略 `-g`。例如：

```bash
npx skills add https://github.com/lining4069/skills --skill project-bootstrap -a claude-code codex opencode --copy
```

如需显式安装 helper skills，也可以分别安装：

```bash
npx skills add https://github.com/lining4069/skills --skill brainstorm-to-prd -a claude-code codex opencode --copy
npx skills add https://github.com/lining4069/skills --skill prd-to-bootstrap -a claude-code codex opencode --copy
npx skills add https://github.com/lining4069/skills --skill bootstrap-harness -a claude-code codex opencode --copy
npx skills add https://github.com/lining4069/skills --skill first-plan-seeder -a claude-code codex opencode --copy
```

## 本地开发

运行测试：

```bash
python3 -B -m unittest discover -s tests
```

当前测试会检查：

- helper CLI 行为
- skill frontmatter
- 发布所需文件是否齐全
- 是否意外包含本地机器路径

## 仓库结构

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

未来新增 skill 时，继续使用 `skills/<skill-name>/SKILL.md` 这种布局。

## Skills CLI 发现方式

`npx skills add <repo> --skill <name>` 会扫描仓库中的 `SKILL.md`，并根据 frontmatter 里的 `name` 字段匹配 skill。

例如在这个仓库里：

- `second-brain` -> `skills/second-brain/SKILL.md`
- `project-bootstrap` -> `skills/project-bootstrap/SKILL.md`
- `brainstorm-to-prd` -> `skills/brainstorm-to-prd/SKILL.md`

在安装前也可以先查看可发现技能列表：

```bash
npx skills add https://github.com/lining4069/skills --list
```
