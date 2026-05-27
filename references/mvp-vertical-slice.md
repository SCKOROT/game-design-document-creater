# MVP And Vertical Slice Planning

Use this reference for every new GDD and for optimization requests involving scope, milestones, or production risk.

## Required Output Section

Add this section before development milestones:

```markdown
## 七、MVP 与垂直切片

### 7.1 MVP 范围
| 模块 | 必须包含 | 暂缓/不做 | 验证目的 |
|------|----------|-----------|----------|
| 核心玩法 | [最小可玩循环] | [暂缓内容] | [验证什么] |
| 内容 | [最小关卡/角色/卡牌/资源量] | [暂缓内容] | [验证什么] |
| 美术 | [最低可接受表现] | [暂缓内容] | [验证什么] |
| 技术 | [必须跑通的技术点] | [暂缓内容] | [验证什么] |

### 7.2 垂直切片
[描述一个 10-30 分钟可完整体验的高质量片段，展示最终游戏体验。]

### 7.3 核心假设
| 假设 | 验证方式 | 通过标准 |
|------|----------|----------|
| [假设1] | [测试方式] | [通过标准] |
| [假设2] | [测试方式] | [通过标准] |
```

## Scope Rules

Personal indie developer:
- MVP should validate one core loop with placeholder art.
- Vertical slice should be short and polished enough for playtest or store-page material.
- Cut online multiplayer, large content rosters, complex live-ops, and heavy 3D unless essential.

2-5 person small team:
- MVP should prove the core loop plus one differentiating system.
- Vertical slice should include near-final art direction, onboarding, one complete content unit, and basic telemetry goals.
- Defer broad content, advanced monetization, and secondary modes.

Professional team:
- MVP can include backend, analytics, monetization hooks, and content pipeline tests.
- Vertical slice should validate production quality, pipeline throughput, monetization assumptions, and live-ops readiness.

## Common Cut List

Use this list when scope is too large:
- Extra playable characters/classes
- Secondary game modes
- Large story arcs
- Cosmetic store
- Guild/social systems
- Procedural content editor
- PvP ranking
- Multi-platform launch
- Full voice acting
