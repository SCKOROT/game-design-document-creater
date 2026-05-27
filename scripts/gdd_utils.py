#!/usr/bin/env python3
"""Utility helpers for Game Design Document Creator skills.

This script keeps file naming, title extraction, version-history updates, and
basic structure checks deterministic so the agent does not need to rewrite that
logic during every GDD task.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


REQUIRED_SECTIONS = [
    "核心体验陈述",
    "基本信息",
    "市场竞品分析",
    "核心玩法",
    "系统详细设计",
    "数值设计框架",
    "核心指标定义",
    "MVP 与垂直切片",
    "开发里程碑",
    "风险评估",
    "版本历史",
]

EXCLUDED_DIRS = {".git", "references", "examples", "scripts", "agents"}
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", re.MULTILINE)


def docs_dir(root: Path) -> Path:
    return root / "Docs"


def ensure_docs_dir(root: Path) -> Path:
    path = docs_dir(root)
    path.mkdir(parents=True, exist_ok=True)
    return path


def next_gdd_path(root: Path) -> Path:
    folder = ensure_docs_dir(root)
    first = folder / "GDD.md"
    if not first.exists():
        return first
    index = 2
    while True:
        candidate = folder / f"GDD{index}.md"
        if not candidate.exists():
            return candidate
        index += 1


def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    match = re.search(r"《([^》]+)》", markdown)
    if match:
        return match.group(1)
    return "未命名 GDD"


def find_gdd_files(root: Path) -> list[Path]:
    patterns = [
        "Docs/**/*.md",
        "docs/**/*.md",
        "**/*GDD*.md",
        "**/*策划*.md",
    ]
    found: dict[Path, None] = {}
    for pattern in patterns:
        for path in root.glob(pattern):
            relative_parts = set(path.relative_to(root).parts)
            if path.is_file() and not (relative_parts & EXCLUDED_DIRS):
                found[path.resolve()] = None
    return sorted(found.keys(), key=lambda path: str(path).lower())


def list_gdds(root: Path) -> list[dict[str, str]]:
    entries = []
    for path in find_gdd_files(root):
        text = path.read_text(encoding="utf-8")
        entries.append(
            {
                "path": str(path),
                "relative_path": str(path.relative_to(root.resolve())),
                "title": extract_title(text),
            }
        )
    return entries


def heading_titles(markdown: str) -> list[str]:
    titles = []
    for match in HEADING_RE.finditer(markdown):
        title = match.group(1).strip()
        title = re.sub(r"^第?[一二三四五六七八九十0-9]+[、.]\s*", "", title)
        titles.append(title)
    return titles


def check_structure(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"GDD file not found: {path}")
    if not path.is_file():
        raise IsADirectoryError(f"Expected a Markdown file, got directory: {path}")
    text = path.read_text(encoding="utf-8")
    headings = heading_titles(text)
    present = [
        section
        for section in REQUIRED_SECTIONS
        if any(section == heading or section in heading for heading in headings)
    ]
    missing = [section for section in REQUIRED_SECTIONS if section not in present]
    score = round(len(present) / len(REQUIRED_SECTIONS) * 100)
    return {
        "path": str(path),
        "title": extract_title(text),
        "score": score,
        "present": present,
        "missing": missing,
        "headings": headings,
    }


def append_version_history(path: Path, change: str, version: str | None = None) -> None:
    if not path.exists():
        raise FileNotFoundError(f"GDD file not found: {path}")
    if not path.is_file():
        raise IsADirectoryError(f"Expected a Markdown file, got directory: {path}")
    text = path.read_text(encoding="utf-8")
    today = date.today().isoformat()
    row = f"| {version or 'vNext'} | {today} | {change} |"

    lines = text.splitlines()
    history_heading = next(
        (
            index
            for index, line in enumerate(lines)
            if re.match(r"^\s{0,3}#{1,6}\s+.*版本历史\s*$", line)
        ),
        None,
    )

    if history_heading is None:
        addition = (
            "\n\n---\n\n## 九、版本历史\n\n"
            "| 版本 | 日期 | 修改内容 |\n"
            "|------|------|----------|\n"
            f"{row}\n"
        )
        path.write_text(text.rstrip() + addition, encoding="utf-8")
        return

    table_header = next(
        (
            index
            for index in range(history_heading + 1, len(lines))
            if re.match(r"^\|\s*版本\s*\|\s*日期\s*\|\s*修改内容\s*\|", lines[index])
        ),
        None,
    )
    if table_header is None:
        insert_at = history_heading + 1
        lines[insert_at:insert_at] = [
            "",
            "| 版本 | 日期 | 修改内容 |",
            "|------|------|----------|",
            row,
        ]
    else:
        separator = table_header + 1
        if separator < len(lines) and re.match(r"^\|\s*-+", lines[separator]):
            insert_at = separator + 1
        else:
            insert_at = table_header + 1
        lines.insert(insert_at, row)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="GDD utility helpers")
    subparsers = parser.add_subparsers(dest="command", required=True)

    next_parser = subparsers.add_parser("next-path", help="Print next available GDD path")
    next_parser.add_argument("--root", default=".", help="Project root")

    list_parser = subparsers.add_parser("list", help="List detected GDD files as JSON")
    list_parser.add_argument("--root", default=".", help="Project root")

    check_parser = subparsers.add_parser("check", help="Check required GDD sections")
    check_parser.add_argument("path", help="GDD Markdown file")

    version_parser = subparsers.add_parser("append-version", help="Append a version-history row")
    version_parser.add_argument("path", help="GDD Markdown file")
    version_parser.add_argument("--change", required=True, help="Change summary")
    version_parser.add_argument("--version", help="Version label")

    args = parser.parse_args()

    if args.command == "next-path":
        print(next_gdd_path(Path(args.root).resolve()))
        return 0
    if args.command == "list":
        print(json.dumps(list_gdds(Path(args.root).resolve()), ensure_ascii=False, indent=2))
        return 0
    if args.command == "check":
        print(json.dumps(check_structure(Path(args.path).resolve()), ensure_ascii=False, indent=2))
        return 0
    if args.command == "append-version":
        append_version_history(Path(args.path).resolve(), args.change, args.version)
        return 0
    return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, IsADirectoryError, UnicodeDecodeError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), flush=True)
        raise SystemExit(2)
