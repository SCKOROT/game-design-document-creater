<div align="center">

# Game Design Document Creator

### AI-Powered Game Design Document Generator

**Chinese-first interactive skill for Claude Code / Codex**

[![Test](https://github.com/SCKOROT/game-design-document-creater/actions/workflows/test.yml/badge.svg)](https://github.com/SCKOROT/game-design-document-creater/actions/workflows/test.yml)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Skill](https://img.shields.io/badge/Claude%20Code-Skill-6B46C1?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMiAxNWwtNS01IDEuNDEtMS40MUwxMCAxNC4xN2w3LjU5LTcuNTlMMTkgOGwtOSA5eiIvPjwvc3ZnPg==)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<br>

*Through Chinese interactive Q&A, quickly generate, check, and optimize*
*complete Game Design Documents (GDD)*

<br>

[Quick Start](#-quick-start) · [Features](#-features) · [Usage](#-usage) · [Architecture](#-architecture) · [CLI Tools](#-cli-tools) · [Testing](#-testing)

</div>

<br>

## Overview

Game Design Document Creator is a Claude Code / Codex skill that generates professional-grade Game Design Documents through structured Chinese dialogue. It adapts recommendations based on your team size — from solo indie developers to professional studios — covering gameplay design, numerical frameworks, market analysis, MVP planning, and risk assessment.

<br>

## Features

<table>
<tr>
<td width="50%">

### Create New GDD
Start from scratch with guided Q&A covering team size, genre, platform, engine, core loop, target audience, and business model. Outputs a complete 10-chapter document.

</td>
<td width="50%">

### Quick Mode
Use a reference game as starting point:
```
"Build something like Slay the Spire,
 but with a wuxia theme and
 equipment progression"
```

</td>
</tr>
<tr>
<td width="50%">

### Optimize Existing GDD
Reads your existing document, outputs a health analysis with quality scores, then optimizes by category: systems, numerical design, monetization, or MVP scope.

</td>
<td width="50%">

### Team-Size Adaptive
Solo indie, small team (2-5), or professional studio — each gets tailored scope, engine recommendations, business model suggestions, and success metrics.

</td>
</tr>
</table>

<br>

## GDD Structure

Every generated document follows a standardized 10-chapter structure:

```
 Chapter 1   Game Overview — core experience statement, basic info, market analysis
 Chapter 2   Core Gameplay — core loop, depth, major systems, controls
 Chapter 3   Detailed System Design — per-system specs with dependencies
 Chapter 4   Numerical Framework — economy, growth curves, KPI definitions
 Chapter 5   Art Requirements — characters, scenes, UI, VFX/audio
 Chapter 6   Technical Architecture — engine choice, key technical challenges
 Chapter 7   MVP & Vertical Slice — minimum scope, core hypotheses
 Chapter 8   Development Milestones — phased delivery with validation criteria
 Chapter 9   Risk Assessment — technical, market, and production risks
 Chapter 10  Version History — changelog with newest entries first
```

<br>

## Quick Start

**1. Install the skill**

```bash
# Clone into Claude Code skills directory
git clone https://github.com/SCKOROT/game-design-document-creater.git \
  ~/.claude/skills/game-design-document-creator
```

**2. Use it in Claude Code**

```
> /gddcreator
```

Or just describe what you want:

```
> design me a roguelike card game for solo development,
  dark fairy tale art style, targeting Steam premium
```

<br>

## Usage

| Trigger | Example |
|---------|---------|
| Command | `/gddcreator` |
| New GDD | *"help me design a game"* |
| Quick Mode | *"design a game based on Genshin Impact"* |
| Quick + Overrides | *"reference Slay the Spire, but change to wuxia theme with equipment progression"* |
| Optimize | *"help me optimize my design document"* |

> Legacy commands `/gamecreater` and `/game-design-document-creater` are still recognized.

<br>

## Architecture

```
game-design-document-creater/
│
├── SKILL.md                          # Skill entry point — routing & orchestration
│
├── references/
│   ├── question-bank.md              # Structured Q&A definitions
│   ├── gdd-template.md               # 10-chapter output template
│   ├── genre-templates.md            # 9 genre archetypes (RPG, Card, Casual, ...)
│   ├── quality-rubric.md             # 100-point scoring rubric
│   ├── optimization-rules.md         # Health analysis & optimization directions
│   └── mvp-vertical-slice.md         # MVP scoping rules by team size
│
├── scripts/
│   └── gdd_utils.py                  # Deterministic CLI utilities
│
├── tests/
│   └── test_gdd_utils.py             # Cross-platform test suite
│
├── examples/
│   └── test-prompts.md               # Smoke-test prompts for all modes
│
└── agents/
    └── openai.yaml                   # OpenAI/Codex agent config
```

`SKILL.md` stays lean (~180 lines) — all detailed question definitions, templates, and diagnostic rules live in `references/`, keeping the main skill's context footprint small.

<br>

## CLI Tools

The `gdd_utils.py` script handles deterministic operations that don't need AI:

```bash
# Find next available GDD filename
python scripts/gdd_utils.py next-path --root /path/to/project

# List all detected GDD files
python scripts/gdd_utils.py list --root /path/to/project

# Check GDD structure completeness (JSON output)
python scripts/gdd_utils.py check Docs/GDD.md

# Human-readable structure report
python scripts/gdd_utils.py check Docs/GDD.md --format human

# Append version history entry
python scripts/gdd_utils.py append-version Docs/GDD.md --change "Optimized core loop" --version v1.1
```

Structure checks distinguish **required sections** (11) from **recommended sections** (5) — a GDD missing recommended sections is still usable, just less thorough.

<br>

## Testing

```bash
# Install dev dependencies
python -m pip install -e ".[test]"

# Run tests
python -m pytest
```

CI runs on every push and PR across **Ubuntu** and **Windows** to catch encoding and path issues early.

<br>

## Supported Genres

The skill includes specialized guidance for 9 genre archetypes:

| | | |
|:---:|:---:|:---:|
| RPG / ARPG | Card / Roguelike | Casual / Puzzle |
| Shooter / FPS | Music / Rhythm | Sports / Racing |
| Horror / Puzzle | Simulation / Management | Strategy / SLG |

Each genre template provides tailored recommendations for core loops, system design priorities, art direction, and scope calibration.

<br>

## Quality Scoring

Generated GDDs are evaluated on a **100-point rubric** across 9 dimensions:

| Dimension | What it measures |
|-----------|-----------------|
| Core Experience | Clarity and alignment of the core experience statement |
| Gameplay Design | Core loop completeness, depth, and system coherence |
| Numerical Framework | Economy balance, growth curves, KPI definitions |
| Content & Art | Asset scope vs. team capacity |
| Technical | Engine fit, key technical risks addressed |
| Market & Monetization | Competitor analysis, business model coherence |
| MVP & Validation | Scope discipline, testable hypotheses |
| Production | Milestone realism, risk coverage |
| Document Quality | Structure, consistency, actionability |

<br>

## License

[MIT](LICENSE) &copy; 2024 AKOROT
