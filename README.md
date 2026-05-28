# Game Design Document Creator

> Claude Code / Codex Skill - 中文游戏策划案生成与优化助手

[![Test](https://github.com/SCKOROT/game-design-document-creater/actions/workflows/test.yml/badge.svg)](https://github.com/SCKOROT/game-design-document-creater/actions/workflows/test.yml)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Skill](https://img.shields.io/badge/Claude%20%2F%20Codex-Skill-6B46C1)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Game Design Document Creator 通过中文交互式问答，帮助你快速生成、检查和优化完整的游戏设计文档 (GDD)。它适合个人独立开发、2-5 人小团队，也能为专业团队提供更结构化的市场、指标、MVP 和风险分析。

## 亮点

| 能力 | 说明 |
|------|------|
| 新建 GDD | 从团队规模、类型、平台、引擎、核心循环、目标玩家画像和商业模式开始生成完整文档。 |
| 快速模式 | 支持“参考某游戏，但是加入自定义变化”的复合指令，并保留差异化要求。 |
| 优化模式 | 先读取已有 GDD，输出健康度分析，再按系统、数值、商业、MVP 等方向优化。 |
| 团队规模适配 | 个人、小团队、专业团队会得到不同的范围、引擎、商业模式和指标建议。 |
| 市场与指标 | 输出核心体验陈述、竞品分析、核心指标定义、MVP/垂直切片和生产风险。 |
| 运行时安全 | 超过 4 个选项的问题会拆分或改用编号输入，避免结构化问答工具超限。 |

## 触发方式

| 方式 | 示例 |
|------|------|
| 命令 | `/gddcreator` |
| 新建 | “帮我设计一个游戏” |
| 新建 | “生成游戏策划案” |
| 快速模式 | “按照原神给我设计一个游戏” |
| 复合快速模式 | “参考《杀戮尖塔》，但改为国风武侠题材，并加入装备成长系统” |
| 优化模式 | “帮我优化策划案” |

旧命令 `/gamecreater` 和 `/game-design-document-creater` 仍可理解，但建议统一使用 `/gddcreator`。

## GDD 输出内容

- 核心体验陈述：“在这个游戏里，玩家感受到……”
- 基本信息：团队规模、类型、平台、屏幕方向、引擎、目标玩家画像、商业模式、规模。
- 参考游戏与市场竞品分析。
- 核心玩法、核心循环、系统详细设计。
- 数值设计框架和核心指标定义。
- MVP、垂直切片和核心假设。
- 美术需求、技术架构、开发里程碑。
- 技术、市场、生产风险评估。
- 版本历史。

生成前会先展示摘要并让用户确认，避免回答有误时直接写入文件。

## 目录结构

```text
.
├── SKILL.md
├── references/
│   ├── question-bank.md
│   ├── gdd-template.md
│   ├── optimization-rules.md
│   ├── quality-rubric.md
│   ├── mvp-vertical-slice.md
│   └── genre-templates.md
├── scripts/
│   └── gdd_utils.py
├── examples/
│   └── test-prompts.md
├── tests/
│   └── test_gdd_utils.py
├── pyproject.toml
├── README.md
└── LICENSE
```

`SKILL.md` 只保留触发、路由和执行规则；详细问答、模板和优化诊断规则放在 `references/` 中，减少主 skill 的上下文负担。

## 安装

将整个目录复制到 Claude Code / Codex 的 skills 目录中：

```bash
mkdir -p ~/.claude/skills/game-design-document-creator
cp -R . ~/.claude/skills/game-design-document-creator/
```

如果你的环境使用 Codex skills 目录，请复制到对应的 `$CODEX_HOME/skills` 或 `~/.codex/skills`。

## 工具脚本

这些命令需要从 skill 安装目录或仓库目录运行；在实际用户项目中使用时，把脚本路径替换为 skill 安装目录下的绝对路径。

```bash
python scripts/gdd_utils.py next-path --root /path/to/user-project
python scripts/gdd_utils.py list --root /path/to/user-project
python scripts/gdd_utils.py check /path/to/user-project/Docs/GDD.md
python scripts/gdd_utils.py check /path/to/user-project/Docs/GDD.md --format human
python scripts/gdd_utils.py append-version /path/to/user-project/Docs/GDD.md --change "优化核心循环"
```

`check` 默认输出 JSON，便于 AI/脚本消费；`--format human` 输出终端可读摘要。结构检查分为必要章节和推荐章节，缺少推荐章节不会代表 GDD 不可用。

## 测试

```bash
python -m pip install -e ".[test]"
python -m pytest
```

GitHub Actions 会在 push 和 pull request 时于 Linux 与 Windows 上自动运行测试，避免编码和路径类问题漏过。

更多交互样例见 [examples/test-prompts.md](examples/test-prompts.md)。

## 许可证

[MIT License](LICENSE)
