# GDD Question Bank

Use this reference when running new GDD creation or when a quick-mode request needs missing details.

## Core Questions

Ask the team-size question first because it changes every later recommendation.

Interaction rule:
- If using a structured question UI with a 2-4 option limit, never pass the long lists below directly.
- For long lists, show a plain-text numbered list and ask the user to type numbers, or split into category groups of 2-4 options.
- Prefer short milestone labels such as "阶段 1/5：团队与范围" instead of fixed question counts, because follow-up questions are conditional.

1. Team size
   - Personal indie developer: recommend small scope, fast prototype, low asset burden, simple tech stack, minimal live-ops.
   - 2-5 person small team: recommend focused vertical slice, limited content breadth, reusable systems, modest commercial validation.
   - Professional team: allow larger production scope, specialized pipelines, deeper monetization and operations planning.
   - Unknown yet: default to personal indie constraints first, then revise scope when the team becomes clearer.

2. Game type
   - Action: hack and slash, platformer, fighting, action adventure, metroidvania.
   - RPG: ARPG, JRPG, MMORPG, idle RPG, roguelike RPG, turn-based RPG, sandbox RPG.
   - Strategy: SLG, RTS, tower defense, tactics, auto battler, management strategy.
   - Casual: match-3, mahjong/card/chess, runner, puzzle, idle, casual PvP, narrative text.
   - Simulation/management: city, farm, restaurant/store, sports management, life sim, business sim.
   - Card/turn-based: TCG/CCG, deckbuilder, turn-based RPG, tactical RPG, card battler.
   - Shooter: FPS, TPS, top-down shooter, side-scrolling shooter, bullet hell, hybrid shooter.
   - Sports/racing: football, basketball, racing, extreme sports, sports manager.
   - Music/rhythm: falling-note rhythm, rhythm action, dance, music creation, rhythm narrative.
   - Horror/puzzle: survival horror, psychological horror, escape room, pure puzzle, narrative puzzle.
   - Other: let the user describe the genre.

Structured UI grouping example for the agent, not user-facing copy:
- 第 1 轮：动作 / RPG / 策略 / 休闲
- 第 2 轮：模拟经营 / 卡牌回合 / 射击 / 体育竞速
- 第 3 轮：音乐节奏 / 恐怖解谜 / 其他 / 帮我推荐

3. Art style
   - 2D pixel, 2D hand-drawn, 2D cartoon, 3D realistic, 3D low-poly, 3D cartoon, dark gothic, Chinese ink, anime, retro sci-fi, minimalist, custom.
   - Optional tone: bright, warm, dark, high contrast, monochrome/two-tone.

Structured UI grouping example for the agent, not user-facing copy:
- 先问：2D / 3D / 风格化 / 还没确定
- 再按所选大类追问具体风格。

4. Target platform
   - WeChat mini game, mobile app, PC, web, console, multi-platform.
   - If mobile is included, ask screen orientation: portrait, landscape, both, or recommendation.

5. Engine
   - Unity, Unreal Engine, Godot, Cocos Creator, GameMaker, custom engine, other, recommendation.
   - Recommendation should account for team size, target platform, 2D/3D needs, content pipeline, and hiring difficulty.

6. Core loop
   - Combat and loot, level challenge, management growth, PvP ranking, exploration and collection, social cooperation, story progression, strategy decision loop, character/equipment growth, creation and sharing, custom.
   - Multi-select is allowed.
   - Optional depth: easy to learn hard to master, casual, hardcore, progressive.

For multi-select core loops, prefer plain-text numbered input if the list has more than 4 choices.

7. Target audience
   - Hardcore, casual, mid-core, all ages, anime audience, competitive players, social players, specific niche.
   - Optional age band: 12-18, 18-30, 25-40, all ages.

8. Business model
   - Premium, free-to-play with IAP, IAP + ads, ads, subscription, hybrid, premium + DLC, recommendation.
   - If IAP is included, ask IAP types: cosmetics, characters/cards, progression resources, battle pass, gacha, remove ads, other.

Structured UI grouping example for the agent, not user-facing copy:
- 先问：买断制 / 免费内购 / 广告变现 / 还没确定
- 再追问 DLC、内购、战令、抽卡、去广告等细节。

9. Scope and schedule
   - Personal prototype, small project, medium project, large project, large commercial project, unknown.
   - Reconcile this with team size; do not recommend a large content scope for a personal developer unless the user explicitly insists.

10. Reference games
    - Ask for titles or allow skip.

11. Core features
    - Ask for 1-2 sentences describing the unique selling point.

12. Game name
    - Allow skip and use "未命名游戏".

13. Extra notes
    - Worldbuilding, special mechanics, technical constraints, production constraints, publishing goals.

## Team-Size Recommendation Rules

Personal indie developer:
- Prefer Godot, Unity, GameMaker, Cocos Creator, or web stack depending on target platform.
- Prefer 2D, low-poly, minimalist, card/puzzle, small systemic games, or procedural reuse.
- Prefer premium, demo-to-wishlist, small paid DLC, or light ads for mini games.
- Keep milestones to prototype, vertical slice, content pass, release polish.

2-5 person small team:
- Prefer Unity, Godot, Cocos Creator, or Unreal only if the team already has 3D expertise.
- Allow moderate 3D, online features, handcrafted content, or light live-ops.
- Recommend clear MVP plus one differentiating system.
- Include validation targets for playtest retention and content production velocity.

Professional team:
- Allow Unreal/Unity, mature asset pipelines, backend services, analytics, live-ops, monetization design, and multi-platform strategy.
- Include market positioning, KPI targets, production risks, and content roadmap.

Unknown yet:
- Start with personal indie assumptions to avoid overscoping.
- Tell the user the plan can be recalibrated later if the team grows.

## Quick-Mode Override Parsing

When the user says "按照/参考/类似 [reference game] 但是 [changes]", parse the part after "但是/但/不过/并且/同时" as overrides before asking follow-up questions.

Examples:
- "按照《杀戮尖塔》，但改为国风武侠题材，弱化卡牌构筑，并加入装备养成系统"
  - Reference game: 杀戮尖塔
  - Overrides: art/theme = 国风武侠, system emphasis = less deckbuilding, more equipment growth
- "参考原神但做成买断制单机，不要抽卡"
  - Reference game: 原神
  - Overrides: business model = premium single-player, remove gacha

After parsing, show a table with:
- Reference-derived baseline
- User override
- Final applied direction

Only ask about items that remain ambiguous or high-impact.

If the reference game cannot be confidently identified:
- Ask the user for genre, target platform, art style, and the design element they want to borrow.
- Continue with those descriptors as the baseline.
- Mark any inferred details as assumptions in the preview table.
