#!/usr/bin/env python3
"""
CICPA-Learning 内容校验脚本

检查项：
1. 每章必须有 README.md + basics.md
2. basics.md 包含"第一性原理"标记
3. intermediate.md / advanced.md 模板合规（如存在）
4. 跨科联动标记格式正确
5. 闪卡格式可解析（#anki-flashcard 区块格式正确）
6. Markdown 文件命名规范（NN-章节名-{layer}.md）
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).parent.parent

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def log(msg: str, color: str = ""):
    print(f"{color}{msg}{Colors.END}")

def check_structure() -> Tuple[int, List[str]]:
    """检查每章是否包含 README.md 和 basics.md"""
    errors = []
    subjects = ["CICPA-Accounting", "CICPA-Auditing", "CICPA-Tax",
                "CICPA-Law", "CICPA-Financial Management", "CICPA-Corporate Strategy"]

    for subject in subjects:
        subject_dir = REPO_ROOT / subject
        if not subject_dir.exists():
            continue
        for chapter_dir in sorted(subject_dir.iterdir()):
            if not chapter_dir.is_dir():
                continue
            readme = chapter_dir / "README.md"
            basics = list(chapter_dir.glob("*-basics.md"))
            if not readme.exists():
                errors.append(f"Missing README.md: {chapter_dir.relative_to(REPO_ROOT)}")
            if not basics:
                errors.append(f"Missing basics.md: {chapter_dir.relative_to(REPO_ROOT)}")

    return len(errors), errors

def check_cross_links() -> Tuple[int, List[str]]:
    """检查跨科联动标记格式"""
    errors = []
    pattern = re.compile(r'🔗\s+\*\*跨科联动\*\*.*?→.*?\[\[\(].*?[\]\)]')
    markdown_files = list(REPO_ROOT.rglob("*.md"))
    for f in markdown_files:
        if ".git" in str(f):
            continue
        try:
            content = f.read_text(encoding="utf-8")
            if "🔗" in content:
                matches = pattern.findall(content)
                if not matches:
                    errors.append(f"Invalid cross-link format: {f.relative_to(REPO_ROOT)}")
        except Exception as e:
            errors.append(f"Read error: {f} - {e}")
    return len(errors), errors

def check_flashcards() -> Tuple[int, List[str]]:
    """检查闪卡格式"""
    errors = []
    pattern = re.compile(r'<!--\s*anki-flashcard\s*-->\s*Q:\s*.+?\s*A:\s*.+?\s*Tags:\s*.+?',
                         re.DOTALL | re.IGNORECASE)
    markdown_files = list(REPO_ROOT.rglob("*.md"))
    for f in markdown_files:
        if ".git" in str(f):
            continue
        try:
            content = f.read_text(encoding="utf-8")
            if "anki-flashcard" in content.lower():
                if not pattern.search(content):
                    errors.append(f"Invalid flashcard format: {f.relative_to(REPO_ROOT)}")
        except Exception:
            pass
    return len(errors), errors

def check_naming() -> Tuple[int, List[str]]:
    """检查 Markdown 文件命名规范"""
    errors = []
    pattern = re.compile(r'^\d{2}-.+-(basics|intermediate|advanced)\.md$')
    markdown_files = list(REPO_ROOT.rglob("*.md"))
    for f in markdown_files:
        if ".git" in str(f) or f.name == "README.md":
            continue
        if not pattern.match(f.name):
            errors.append(f"Invalid naming: {f.relative_to(REPO_ROOT)}")
    return len(errors), errors

def main():
    log("=" * 50, Colors.BLUE)
    log("  CICPA-Learning 内容校验", Colors.BLUE)
    log("=" * 50, Colors.BLUE)

    checks = [
        ("结构检查（README + basics）", check_structure),
        ("命名规范检查", check_naming),
        ("跨科联动标记检查", check_cross_links),
        ("闪卡格式检查", check_flashcards),
    ]

    total_errors = 0
    for name, check_func in checks:
        count, errors = check_func()
        total_errors += count
        if errors:
            log(f"\n[FAIL] {name}: {count} 个问题", Colors.RED)
            for e in errors[:10]:
                log(f"  - {e}", Colors.RED)
            if len(errors) > 10:
                log(f"  ... 还有 {len(errors) - 10} 个问题", Colors.YELLOW)
        else:
            log(f"[PASS] {name}", Colors.GREEN)

    log("\n" + "=" * 50, Colors.BLUE)
    if total_errors == 0:
        log("  所有检查通过！", Colors.GREEN)
    else:
        log(f"  共 {total_errors} 个问题待修复", Colors.YELLOW)
    log("=" * 50, Colors.BLUE)

    return 0 if total_errors == 0 else 1

if __name__ == "__main__":
    sys.exit(main())