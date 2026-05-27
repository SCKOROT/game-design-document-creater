# Test Prompts

Use these prompts to smoke-test the skill after changes.

## New GDD

```text
帮我设计一个个人独立开发能完成的肉鸽卡牌游戏，偏暗黑童话风，目标是 Steam 买断制。
```

Expected behavior:
- Ask or infer team size as personal indie.
- Use card/turn-based genre guidance.
- Keep scope small.
- Include MVP and vertical slice.
- Use indie-friendly metrics.

## Quick Mode With Overrides

```text
参考《原神》，但改为买断制单机，不要抽卡，团队只有 2-5 人，战斗可以简化。
```

Expected behavior:
- Parse reference game and overrides.
- Apply premium single-player and no gacha before asking follow-up questions.
- Reduce scope for small team.

## Optimization

```text
帮我优化 Docs/GDD.md，先看看这份策划案有什么问题。
```

Expected behavior:
- Read the selected file first.
- Output health analysis and quality score.
- Ask for optimization direction.

## Mobile Casual

```text
帮我设计一个 2-5 人团队能做完的微信小游戏，偏休闲益智，适合竖屏。
```

Expected behavior:
- Recommend small-team scope.
- Use casual/puzzle guidance.
- Include screen orientation and short-session metrics.

## Simulation

```text
我想做一个个人开发的餐厅模拟经营游戏，像开罗游戏那样但更重视员工培养。
```

Expected behavior:
- Use simulation/management guidance.
- Focus on resource chain and employee progression.
- Keep art and content scope realistic.

## Unknown Reference Game

```text
参考《不存在的星尘旅团》，但是做成竖屏休闲游戏。
```

Expected behavior:
- Say the reference cannot be confidently identified.
- Ask for genre, platform, core loop, or art style descriptors.
- Mark inferred fields as assumptions.

## Batch Optimization

```text
帮我同时优化 Docs/GDD.md 和 Docs/GDD2.md，重点看团队规模和 MVP 是否合理。
```

Expected behavior:
- Read each selected GDD independently.
- Produce separate health analysis and quality score.
- Ask whether to apply the same optimization strategy.

## Revise Previous Answer

```text
刚才团队规模选错了，改成个人独立开发，然后重新推荐引擎和 MVP 范围。
```

Expected behavior:
- Update prior assumptions.
- Recalculate engine, scope, metrics, and milestones.

## Irrelevant Request

```text
帮我写一个 Python 爬虫。
```

Expected behavior:
- Do not trigger the GDD workflow.
- Answer normally or ask whether the user meant a game design document.

## English Input

```text
Create a GDD for a solo-developed cozy farming sim for PC, premium model.
```

Expected behavior:
- Support English input.
- Ask whether to continue in English or Chinese if unclear.
- Apply solo indie scope rules.
