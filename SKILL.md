---
name: game-design-document-creator
description: Create or improve game design documents (GDD) through interactive Chinese Q&A. Use when the user asks to design a game, generate a game planning document, create a GDD, optimize an existing game plan, or design by referencing another game such as "按照原神设计一个游戏", "帮我设计一个游戏", "生成游戏策划案", "优化策划案", or "/gddcreator".
---

# Game Design Document Creator

通过交互式问答生成或优化游戏设计文档 (GDD)。优先输出可落地的设计方案，而不是泛泛的创意清单。

## Resources

Load these references only when needed:

- `references/question-bank.md`: new-document questions, team-size recommendation rules, quick-mode override parsing.
- `references/gdd-template.md`: required GDD structure, including core experience statement, competitor analysis, and core metrics.
- `references/optimization-rules.md`: health analysis and editing rules for existing GDD files.
- `references/quality-rubric.md`: 100-point GDD quality scoring rubric.
- `references/mvp-vertical-slice.md`: MVP, vertical slice, and core hypothesis planning.
- `references/genre-templates.md`: genre-specific questions and required design details.

Resource paths are relative to this skill's installation directory, not the user's project directory. Resolve the skill directory from the loaded `SKILL.md` location before reading references or running scripts.

Common installation path hints:
- Claude Code: `~/.claude/skills/game-design-document-creator/` or `~/.claude/skills/game-design-document-creater/`
- Codex: `$CODEX_HOME/skills/game-design-document-creator/` or `~/.codex/skills/game-design-document-creator/`
- Project-local installs: `.superpowers/skills/game-design-document-creator/`

If the runtime does not expose the skill directory, locate this skill by finding a `SKILL.md` whose frontmatter name is `game-design-document-creator`, then use that folder as `<skill_dir>`. If `<skill_dir>` still cannot be found, continue without scripts: read available references from the loaded skill context and use normal file tools in the user project.

Use `scripts/gdd_utils.py` for deterministic file operations:

- `python <skill_dir>/scripts/gdd_utils.py next-path --root <project_dir>`
- `python <skill_dir>/scripts/gdd_utils.py list --root <project_dir>`
- `python <skill_dir>/scripts/gdd_utils.py check <project_dir>/Docs/GDD.md`
- `python <skill_dir>/scripts/gdd_utils.py check <project_dir>/Docs/GDD.md --format human`
- `python <skill_dir>/scripts/gdd_utils.py append-version <project_dir>/Docs/GDD.md --change "优化核心循环"`

## Commands And Triggers

Treat these as equivalent triggers:

- `/gddcreator`
- "帮我设计一个游戏"
- "生成游戏策划案"
- "我想做一个 XX 类型的游戏"
- "按照/参考/类似 XX 游戏设计"
- "帮我优化策划案"
- "修改/完善/升级已有 GDD"

If the user uses old names such as `/gamecreater` or `/game-design-document-creater`, continue normally and prefer `/gddcreator` in future prompts.

## Startup

1. Inspect the user request.
2. Search for existing GDD files with `<skill_dir>/scripts/gdd_utils.py list --root <project_dir>` when scripts are available; otherwise use patterns such as `Docs/**/*.md`, `docs/**/*.md`, `**/*GDD*.md`, and `**/*策划*.md`.
3. Choose the mode:
   - Quick mode: request contains "按照", "参考", or "类似" plus a reference game.
   - Optimization mode: request asks to optimize, modify, improve, complete, diagnose, or upgrade an existing GDD.
   - New mode: request asks to create or design a game, or no existing GDD is relevant.
   - Ambiguous command mode: `/gddcreator` with existing GDD files. Ask whether to create a new GDD or optimize an existing one.

## Interaction Rules

- Ask concise questions one at a time unless the environment provides a structured multi-question UI.
- If a structured question tool is available, use it only when the question has 2-4 options. For more than 4 options, either split the choices into several rounds or present a plain-text numbered list and let the user type numbers.
- Never call a structured question tool with more options than the current tool schema allows.
- Let users answer with numbers, labels, free text, "跳过", or "帮我推荐".
- When the user says "帮我推荐", recommend based on team size, platform, genre, and production constraints.
- Do not force every optional question. Ask only high-impact follow-ups when the user's intent is already clear.
- Always ask team size before other new-mode questions unless the user already provided it.
- Preserve user constraints over defaults.
- Use milestone-style progress labels instead of fixed counts when branch questions are possible, such as "阶段 2/5：玩法方向", not "问题 1/10".

## Quick Mode

Use when the user asks to design by referencing another game.

1. Load `references/question-bank.md`.
2. Parse the reference game and any override clause after words such as "但是", "但", "不过", "并且", or "同时".
3. Build a baseline analysis of the reference game's type, art style, core loop, platform, audience, business model, and key features.
   - If web search is available and the game is recent, obscure, or uncertain, search reliable sources to verify its genre, platform, core loop, and monetization before analyzing.
   - If the reference game is obscure or cannot be confidently identified, say so and ask the user for 2-3 short descriptors such as genre, platform, core loop, art style, or monetization.
   - If partial information is available, label uncertain fields as assumptions instead of inventing specifics.
4. Apply explicit user overrides before showing the result.
5. Show a compact table:

```markdown
| 项目 | 参考游戏基线 | 用户覆盖项 | 最终方向 |
|------|--------------|------------|----------|
| 游戏类型 | ... | ... | ... |
| 美术风格 | ... | ... | ... |
| 核心循环 | ... | ... | ... |
| 商业模式 | ... | ... | ... |
```

6. Ask whether to generate directly or adjust selected elements.
7. Before writing, show a short generation summary and ask the user to confirm or revise.
8. Generate the GDD using `references/gdd-template.md` after confirmation.

Do not copy protected IP, characters, story, names, levels, or art assets from the reference game. Borrow only design patterns and clearly state the differentiation.

## New GDD Mode

1. Load `references/question-bank.md`.
2. Load `references/genre-templates.md` after the genre is known.
3. Load `references/mvp-vertical-slice.md` before writing milestones.
4. Ask the team-size question first:
   - 个人独立开发
   - 2-5 人小团队
   - 专业团队
   - 还没确定：先按个人独立开发约束推荐，后续可调整
5. Continue through the question bank, adapting depth to the user's answers.
6. Use team size to adjust recommendations:
   - Personal indie: reduce scope, recommend low-cost art and validation milestones.
   - Small team: focus on vertical slice, content reuse, and one clear differentiator.
   - Professional team: include analytics, live-ops, production pipeline, and market positioning where appropriate.
7. Before writing the document, summarize the captured direction and ask the user to confirm or revise.
8. Load `references/gdd-template.md` and create the Markdown GDD after confirmation.
9. Save new GDD files under `Docs/`. Prefer `<skill_dir>/scripts/gdd_utils.py next-path --root <project_dir>` to create the directory and pick the path.

The generated GDD must include:

- Core experience statement: "在这个游戏里，玩家感受到..."
- Market competitor analysis table.
- Core metrics appropriate to team size and business model.
- MVP scope, vertical slice, and core hypotheses.
- Development milestones with validation goals.
- Risks covering technology, market, and production.

## Optimization Mode

1. Find existing GDD files.
2. If multiple files match, ask the user to choose one or more.
3. Load `references/optimization-rules.md`.
4. Load `references/quality-rubric.md`.
5. Read the selected GDD file before asking for optimization direction.
6. Output a current-document health analysis and 100-point quality score covering:
   - Section completeness
   - Core experience statement
   - Core loop clarity
   - System coherence
   - Numerical framework
   - Market differentiation
   - Core metrics
   - MVP and vertical slice quality
   - Team-size/scope fit
   - Risk quality
7. Ask the user which dimensions to optimize.
8. Edit the chosen GDD in place unless the user asks for a copy.
9. Add or update the version-history section with a concise description of the change. Prefer `<skill_dir>/scripts/gdd_utils.py append-version` when scripts are available.
10. After editing, provide a concise change summary listing changed sections, added sections, removed sections, and any remaining risks. Use `git diff` when the project is a git repository.

When adding missing sections, follow `references/gdd-template.md`. When optimizing several GDDs, diagnose each file independently even if the same optimization direction is applied.

## Session Resume

If the user asks to continue a previously interrupted GDD session, inspect the conversation history and any draft files in the project. Summarize the collected answers, identify missing high-impact fields, and continue from the next incomplete stage instead of restarting.

## Output Standards

- Use clear Chinese by default.
- Keep design claims concrete and testable.
- Tie every major system back to the core experience statement.
- Make scope realistic for the team size.
- In competitor analysis, explain difference and risk instead of simply listing reference games.
- In core metrics, choose indicators that fit the project:
  - Indie: prototype completion, playtest completion, average session length, wishlist/demo conversion, feedback quality.
  - Small team: D1/D7 retention, session length, content consumption, conversion, production velocity.
  - Professional team: D1/D7/D30 retention, ARPU, LTV, payer conversion, ROAS, live-ops cadence.
- Always define MVP scope and a vertical slice. Use them to cut features when the plan is too large.
- Apply genre-specific guidance from `references/genre-templates.md` after the user selects a genre.

## Validation

Before finalizing, check:

- The generated or edited file exists at the intended path.
- Run `<skill_dir>/scripts/gdd_utils.py check <path>` when scripts are available.
- Treat missing required sections as blockers. Treat missing recommended sections as improvement suggestions unless the user asked for a full production GDD.
- The GDD contains the upgraded sections: 开发团队/团队规模, 核心体验陈述, 市场竞品分析, 核心指标定义, and MVP 与垂直切片.
- Quick-mode overrides from "但是..." style instructions were applied.
- Existing user content was preserved unless it conflicted with the requested optimization.
