#!/usr/bin/env python3
"""Structural validator for pre-talk cards. No LLM, no network."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_HEADERS = [
    "# 备谈卡",
    "## 核心句",
    "## 重要性排序",
    "## 对方预设三问",
    "## 红线",
    "## 开场第一句",
]

FILLED_HEADERS = ["## 核心句", "## 开场第一句"]


def section(text: str, header: str) -> str:
    m = re.search(rf"^{re.escape(header)}[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else ""


def check(path: Path, headers_only: bool = False) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for h in REQUIRED_HEADERS:
        if not re.search(rf"^{re.escape(h)}\b", text, re.M):
            errors.append(f"missing header: {h}")
    if errors or headers_only:
        return errors

    core = section(text, "## 核心句")
    core_line = next((ln for ln in core.splitlines() if ln.strip()), "")
    if not core_line:
        errors.append("核心句为空")
    elif len(core_line) > 60:
        errors.append(f"核心句超过 60 字（{len(core_line)}）")

    ranking = section(text, "## 重要性排序")
    if not re.search(r"^\s*1\.", ranking, re.M):
        errors.append("排序缺「1. 第一重要」")
    if not re.search(r"^\s*2\.", ranking, re.M):
        errors.append("排序缺「2. 第二重要」（试金石：答不出第二重要，第一句是口号）")

    qa = section(text, "## 对方预设三问")
    rows = [ln for ln in qa.splitlines() if ln.strip().startswith("|")]
    data_rows = [ln for ln in rows if not re.match(r"^\|[\s:-]+\|", ln) and "---" not in ln]
    if len(data_rows) < 2:
        errors.append("对方预设三问表格数据行不足（表头 + 至少 1 个问题行）")

    opener = section(text, "## 开场第一句")
    if not next((ln for ln in opener.splitlines() if ln.strip()), ""):
        errors.append("开场第一句为空")

    glasses = section(text, "## 眼镜开场白")
    if glasses:
        g_line = next((ln for ln in glasses.splitlines() if ln.strip()), "")
        if g_line and len(g_line) > 60:
            errors.append(f"眼镜开场白超过 60 字（{len(g_line)}）")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate pre-talk card structure")
    parser.add_argument("cards", nargs="+", type=Path)
    parser.add_argument("--headers-only", action="store_true", help="only check headers (for the empty template)")
    args = parser.parse_args()

    failed = False
    for path in args.cards:
        if not path.is_file():
            print(f"FAIL {path.name}: file not found")
            failed = True
            continue
        errors = check(path, headers_only=args.headers_only)
        if errors:
            failed = True
            for e in errors:
                print(f"FAIL {path.name}: {e}")
        else:
            print(f"PASS {path.name}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
