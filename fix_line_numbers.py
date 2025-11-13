#!/usr/bin/env python3
"""
翻訳ファイルから誤って混入した行番号を削除するスクリプト
"""
import os
import re

def fix_line_numbers(content):
    """
    行頭の行番号パターン（スペース+数字+タブまたはスペース）を削除
    """
    # パターン: 行頭のスペース + 数字 + タブまたはスペース
    pattern = r'^(\s*)(\d+)\t'
    lines = content.split('\n')
    fixed_lines = []

    for line in lines:
        # 行番号パターンにマッチする場合は削除
        match = re.match(pattern, line)
        if match:
            # 行番号とタブを削除
            fixed_line = line[len(match.group(0)):]
            fixed_lines.append(fixed_line)
        else:
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
            if re.search(r'^\s*\d+\t', content, re.MULTILINE):
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
