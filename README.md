# Game Design Document Creator

> Claude Code / Codex Skill - 游戏策划案生成器

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Game Design Document Creator 通过中文交互式问答，帮助你生成或优化完整的游戏设计文档 (GDD)。

## 功能

- 新建 GDD：从团队规模、游戏类型、平台、引擎、核心循环、目标用户和商业模式开始生成完整文档。
- 快速模式：支持"按照/参考/类似某游戏"生成，并能解析"但是..."后的自定义变化。
- 优化模式：先读取已有 GDD，输出健康度分析，再针对性优化。
- 团队规模适配：个人独立开发、2-5 人小团队、专业团队会得到不同的规模、引擎、商业模式和指标建议。
- GDD 增强章节：核心体验陈述、市场竞品分析、核心指标定义、生产风险评估。
- MVP/垂直切片：自动定义最小可行版本、可试玩切片和核心假设。
- 质量评分：优化模式可按 100 分 Rubric 诊断 GDD。
- 类型专属指导：RPG、卡牌、休闲、射击、模拟经营、策略等类型有不同设计重点。
- 交互安全：超过 4 个选项的问题会拆分或改用纯文本编号输入，避免结构化问答工具超限。

## 触发方式

| 方式 | 示例 |
|------|------|
| 命令 | `/gddcreator` |
| 新建 | "帮我设计一个游戏" |
| 新建 | "生成游戏策划案" |
| 快速模式 | "按照原神给我设计一个游戏" |
| 复合快速模式 | "参考《杀戮尖塔》，但改为国风武侠题材，并加入装备养成系统" |
| 优化模式 | "帮我优化策划案" |

旧命令 `/gamecreater` 和 `/game-design-document-creater` 仍可理解，但建议统一使用 `/gddcreator`。

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
├── README.md
└── LICENSE
```

`SKILL.md` 只保留触发、路由和执行规则；详细问答、模板和优化诊断规则放在 `references/` 中，减少主 skill 的上下文负担。

## 生成的 GDD 包含

- 核心体验陈述："在这个游戏里，玩家感受到..."
- 基本信息：团队规模、类型、平台、屏幕方向、引擎、用户、商业模式、规模。
- 参考游戏与市场竞品分析。
- 核心玩法、核心循环、系统详细设计。
- 数值设计框架和核心指标定义。
- MVP、垂直切片和核心假设。
- 美术需求、技术架构、开发里程碑。
- 技术、市场、生产风险评估。
- 版本历史。

生成前会先展示摘要并让用户确认，避免回答有误时直接写入文件。

## 安装

将整个目录复制到 Claude Code / Codex 的 skills 目录中：

```bash
mkdir -p ~/.claude/skills/game-design-document-creator
cp -R . ~/.claude/skills/game-design-document-creator/
```

如果你的环境使用 Codex skills 目录，请复制到对应的 `$CODEX_HOME/skills` 或 `~/.codex/skills`。

## 工具脚本

```bash
python scripts/gdd_utils.py next-path --root .
python scripts/gdd_utils.py list --root .
python scripts/gdd_utils.py check Docs/GDD.md
python scripts/gdd_utils.py append-version Docs/GDD.md --change "优化核心循环"
```

## 测试用例

见 [examples/test-prompts.md](examples/test-prompts.md)。

## 许可证

[MIT License](LICENSE)
