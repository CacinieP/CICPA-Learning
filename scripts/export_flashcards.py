#!/usr/bin/env python3
"""
CICPA-Learning 闪卡导出脚本

解析所有 basics.md 中的 #anki-flashcard 区块，
输出 Anki 可导入的 CSV/TSV 格式。
"""

import csv
import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = REPO_ROOT / "anki-decks"

def parse_flashcards() -> List[Tuple[str, str, str, str]]:
    """
    解析所有 Markdown 文件中的闪卡。
    返回：[(问题, 答案, Tags, 来源文件), ...]
    """
    flashcards = []
    pattern = re.compile(
        r'<!--\s*anki-flashcard\s*-->\s*Q:\s*(.+?)\s*A:\s*(.+?)\s*Tags:\s*(.+?)(?=\n<!--|\n#|\Z)',
        re.DOTALL | re.IGNORECASE
    )

    markdown_files = list(REPO_ROOT.rglob("*-basics.md"))
    for f in markdown_files:
        try:
            content = f.read_text(encoding="utf-8")
            subject = f.parent.parent.name  # e.g. CICPA-Accounting
            chapter = f.parent.name        # e.g. 01-总论
            for match in pattern.finditer(content):
                q, a, tags_raw = match.groups()
                q = q.strip()
                a = a.strip()
                # 标准化标签
                subject_tag = subject.replace("CICPA-", "")  # 去掉前缀
                chapter_tag = chapter.split("-", 1)[-1]         # 去掉编号
                tags = f"{subject_tag}-{chapter_tag},{tags_raw.strip()}"
                source = f"{subject}/{chapter}/basics"
                flashcards.append((q, a, tags, source))
        except Exception as e:
            print(f"Warning: Failed to parse {f}: {e}", file=sys.stderr)

    return flashcards

def export_csv(flashcards: List[Tuple[str, str, str, str]], output_path: Path):
    """导出为 Anki 兼容的 CSV（制表符分隔）"""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["Front", "Back", "Tags", "Source"])
        for q, a, tags, source in flashcards:
            writer.writerow([q, a, tags, source])

def export_by_subject(flashcards: List[Tuple[str, str, str, str]]):
    """按科目分别导出"""
    from collections import defaultdict
    by_subject = defaultdict(list)
    for card in flashcards:
        # 从source提取科目
        source = card[3]
        subject = source.split("/")[0]
        by_subject[subject].append(card)

    OUTPUT_DIR.mkdir(exist_ok=True)
    for subject, cards in by_subject.items():
        safe_name = subject.replace("CICPA-", "").replace(" ", "-")
        output_path = OUTPUT_DIR / f"{safe_name}.tsv"
        export_csv(cards, output_path)
        print(f"  Exported: {output_path.name} ({len(cards)} cards)")

def main():
    print("=" * 50)
    print("  CICPA-Learning 闪卡导出")
    print("=" * 50)

    flashcards = parse_flashcards()

    if not flashcards:
        print("No flashcards found.")
        return 1

    print(f"\nFound {len(flashcards)} flashcards across all subjects.\n")

    # 全部导出为一包
    all_path = OUTPUT_DIR / "all-subjects.tsv"
    OUTPUT_DIR.mkdir(exist_ok=True)
    export_csv(flashcards, all_path)
    print(f"All subjects: {all_path.name} ({len(flashcards)} cards)")

    # 按科目分别导出
    print("\nBy subject:")
    export_by_subject(flashcards)

    print(f"\nOutput directory: {OUTPUT_DIR}")
    print("Import into Anki: File → Import → Select .tsv file")
    print("Note type: Basic (Front/Back)")
    print("Field separator: Tab")

    return 0

if __name__ == "__main__":
    sys.exit(main())