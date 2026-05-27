# GDD Optimization Rules

Use this reference when improving an existing GDD.

## Required First Step

Before asking the user to choose optimization directions, read the selected GDD file contents.

Then produce a concise health analysis and a 100-point score using `quality-rubric.md`:

```markdown
## 当前策划案健康度分析

| 维度 | 状态 | 说明 | 建议 |
|------|------|------|------|
| 章节完整度 | 完整/部分/缺失 | [说明] | [建议] |
| 核心体验陈述 | 清晰/模糊/缺失 | [说明] | [建议] |
| 核心循环 | 清晰/模糊/缺失 | [说明] | [建议] |
| 系统自洽性 | 强/中/弱 | [说明] | [建议] |
| 数值框架 | 完整/粗略/缺失 | [说明] | [建议] |
| 市场差异化 | 清晰/普通/缺失 | [说明] | [建议] |
| 核心指标 | 合理/不匹配/缺失 | [说明] | [建议] |
| MVP 与垂直切片 | 清晰/过大/缺失 | [说明] | [建议] |
| 团队规模匹配 | 匹配/偏大/偏小/未知 | [说明] | [建议] |
| 风险评估 | 可执行/泛泛/缺失 | [说明] | [建议] |
```

Keep the health analysis diagnostic, not judgmental. Use it to guide the next question.

## Optimization Directions

Offer focused choices after the health analysis:

1. Core experience statement
2. Core loop and main systems
3. Team-size/scope realignment
4. Market competitor differentiation
5. Numerical framework and core metrics
6. MVP and vertical slice scope
7. Monetization and business model
8. Technical architecture and engine choice
9. Art scope and production cost
10. Milestones and production plan
11. Full document restructuring

If multiple GDD files are selected:
- Ask whether to apply the same optimization strategy to all files or diagnose each file separately.
- If applying the same strategy, still read each file before editing because missing sections may differ.

## Editing Rules

- Preserve useful existing ideas instead of replacing the document wholesale.
- Add a version-history row describing the optimization.
- Prefer `scripts/gdd_utils.py append-version` for version-history updates when scripts are available.
- If a section is missing, add it in the location defined by `gdd-template.md`.
- If a section exists but is vague, rewrite it with clearer design intent, tradeoffs, and validation criteria.
- Make risks concrete: include cause, impact, mitigation, and early warning signal.

## Health Signals

Strong GDD:
- Has a specific player fantasy or emotional target.
- Core loop can be summarized in 3-6 steps.
- Systems reinforce each other rather than existing as a feature list.
- Scope matches team size and schedule.
- Differentiation is visible against competitors.
- Metrics validate the intended experience and business model.
- MVP and vertical slice clearly reduce production risk.

Weak GDD:
- Describes genre but not player experience.
- Lists many systems without priorities.
- Has commercial goals but no metrics.
- Uses a large-team content plan for a personal developer.
- References popular games without explaining what changes.
