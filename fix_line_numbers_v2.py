#!/usr/bin/env python3
"""
翻訳ファイルから誤って混入した行番号を削除するスクリプト（改良版）
"""
import os
import re

def fix_line_numbers(content):
    """
    様々な形式の行番号パターンを削除
    """
    lines = content.split('\n')
    fixed_lines = []

    for line in lines:
        # パターン1: 行頭のスペース + 数字 + タブ
        # 例: "     1\t内容"
        match1 = re.match(r'^(\s*)(\d+)\t(.*)$', line)
        if match1:
            # タブより前の部分を削除
            fixed_lines.append(match1.group(3))
            continue

        # パターン2: 行頭のスペース（5個程度）+ 数字 + スペース
        # 例: "     2 内容"
        match2 = re.match(r'^\s{4,6}(\d+)\s(.*)$', line)
        if match2:
            # 行番号部分を削除
            fixed_lines.append(match2.group(2))
            continue

        # パターン3: 数字 + 複数スペース + 内容
        # 例: "1  内容" や "10   内容"
        # ただし、Texinfoの章番号（@node 1.1 など）は除外
        if not re.match(r'^[@\\]', line):  # @ または \ で始まらない行のみ
            match3 = re.match(r'^(\d+)\s{2,}(.*)$', line)
            if match3:
                fixed_lines.append(match3.group(2))
                continue

        # マッチしない場合はそのまま
        fixed_lines.append(line)

    return '\n'.join(fixed_lines)

def main():
    translated_dir = 'translated'
    fixed_count = 0

    for fname in sorted(os.listdir(translated_dir)):
        if not fname.endswith('.texi'):
            continue

        filepath = os.path.join(translated_dir, fname)

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # 行番号パターンが含まれているかチェック
            patterns = [
                r'^\s*\d+\t',
                r'^\s{4,6}\d+\s',
                r'^\d+\s{2,}[^0-9]',
            ]

            has_problem = any(re.search(p, content, re.MULTILINE) for p in patterns)

            if has_problem:
                # 修正を適用
                fixed_content = fix_line_numbers(content)

                # ファイルに書き戻す
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)

                print(f'Fixed: {fname}')
                fixed_count += 1

        except Exception as e:
            print(f'Error processing {fname}: {e}')

    print(f'\nTotal fixed: {fixed_count} files')

if __name__ == '__main__':
    main()
