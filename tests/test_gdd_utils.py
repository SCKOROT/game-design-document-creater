import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "gdd_utils.py"


def run_cli(*args, cwd=None):
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=cwd or ROOT,
        env=env,
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=False,
    )


def test_check_requires_headings_not_body_mentions(tmp_path):
    gdd = tmp_path / "GDD.md"
    gdd.write_text(
        "# 《测试》GDD\n\n正文提到核心体验陈述、市场竞品分析、核心指标定义、MVP 与垂直切片。\n",
        encoding="utf-8",
    )

    result = run_cli("check", str(gdd))
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["score"] == 0
    assert payload["required_score"] == 0
    assert "核心体验陈述" in payload["missing_required"]


def test_check_accepts_numbered_subheadings(tmp_path):
    gdd = tmp_path / "GDD.md"
    gdd.write_text(
        "\n".join(
            [
                "# 《测试》GDD",
                "## 一、游戏概述",
                "### 1.1 核心体验陈述",
                "### 1.2 基本信息",
                "### 1.3 游戏简介",
                "### 1.4 参考游戏",
                "### 1.5 市场竞品分析",
                "## 二、核心玩法设计",
                "## 三、系统详细设计",
                "## 四、数值设计框架",
                "### 4.3 核心指标定义",
                "## 五、美术需求清单",
                "## 六、技术架构建议",
                "## 七、MVP 与垂直切片",
                "## 八、开发里程碑",
                "## 九、风险评估",
                "## 十、版本历史",
            ]
        ),
        encoding="utf-8",
    )

    result = run_cli("check", str(gdd))
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["score"] == 100
    assert payload["required_score"] == 100
    assert payload["recommended_score"] == 100
    assert payload["missing_required"] == []
    assert payload["missing_recommended"] == []
    assert "核心体验陈述" in payload["headings"]


def test_check_distinguishes_recommended_sections(tmp_path):
    gdd = tmp_path / "GDD.md"
    gdd.write_text(
        "\n".join(
            [
                "# 《测试》GDD",
                "## 一、游戏概述",
                "### 核心体验陈述",
                "### 基本信息",
                "## 二、核心玩法设计",
                "## 三、系统详细设计",
                "## 四、数值设计框架",
                "### 核心指标定义",
                "## 七、MVP 与垂直切片",
                "## 八、开发里程碑",
                "## 九、风险评估",
                "## 十、版本历史",
            ]
        ),
        encoding="utf-8",
    )

    result = run_cli("check", str(gdd))
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["required_score"] == 100
    assert payload["recommended_score"] == 0
    assert "游戏简介" in payload["missing_recommended"]


def test_check_does_not_match_section_in_middle_of_heading(tmp_path):
    gdd = tmp_path / "GDD.md"
    gdd.write_text(
        "\n".join(
            [
                "# 《测试》GDD",
                "## 一、游戏概述",
                "### 核心体验陈述",
                "### 基本信息",
                "## 二、非核心玩法讨论",
                "## 三、系统详细设计",
                "## 四、数值设计框架",
                "### 核心指标定义",
                "## 七、MVP 与垂直切片",
                "## 八、开发里程碑",
                "## 九、风险评估",
                "## 十、版本历史",
            ]
        ),
        encoding="utf-8",
    )

    result = run_cli("check", str(gdd))
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert "核心玩法" in payload["missing_required"]


def test_check_human_format(tmp_path):
    gdd = tmp_path / "GDD.md"
    gdd.write_text("# 《测试》GDD\n", encoding="utf-8")

    result = run_cli("check", str(gdd), "--format", "human")
    assert result.returncode == 0
    assert "Required score:" in result.stdout
    assert "Missing required sections:" in result.stdout


def test_next_path_creates_docs_and_increments(tmp_path):
    result = run_cli("next-path", "--root", str(tmp_path))
    assert result.returncode == 0
    assert result.stdout.strip().endswith(str(Path("Docs") / "GDD.md"))

    (tmp_path / "Docs" / "GDD.md").write_text("# Existing\n", encoding="utf-8")
    result = run_cli("next-path", "--root", str(tmp_path))
    assert result.returncode == 0
    assert result.stdout.strip().endswith(str(Path("Docs") / "GDD2.md"))


def test_append_version_creates_tenth_history_section(tmp_path):
    gdd = tmp_path / "GDD.md"
    gdd.write_text("# 《测试》GDD\n", encoding="utf-8")

    result = run_cli("append-version", str(gdd), "--change", "测试更新", "--version", "v1.1")
    assert result.returncode == 0
    text = gdd.read_text(encoding="utf-8")
    assert "## 十、版本历史" in text
    assert "| v1.1 |" in text


def test_missing_file_returns_json_error(tmp_path):
    result = run_cli("check", str(tmp_path / "missing.md"))
    assert result.returncode == 2
    payload = json.loads(result.stdout)
    assert "GDD file not found" in payload["error"]
