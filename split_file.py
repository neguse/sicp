#!/usr/bin/env python3
"""
ファイルを指定行数ずつに分割するスクリプト
"""
import sys
import os

def split_file(input_file, output_dir, lines_per_file=100):
    """
    ファイルを指定行数ずつに分割する

    Args:
        input_file: 入力ファイルのパス
        output_dir: 出力ディレクトリ
        lines_per_file: 1ファイルあたりの行数（デフォルト: 100）
    """
    # 出力ディレクトリが存在しない場合は作成
    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    file_count = 0

    for i in range(0, total_lines, lines_per_file):
        chunk = lines[i:i+lines_per_file]
        output_file = os.path.join(output_dir, f'chunk_{file_count:04d}.texi')

        with open(output_file, 'w', encoding='utf-8') as out:
            out.writelines(chunk)

        file_count += 1
        print(f'Created: {output_file} ({len(chunk)} lines)')

    print(f'\nTotal: {file_count} files created')
    print(f'Total lines: {total_lines}')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 split_file.py <input_file> <output_dir> [lines_per_file]')
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    lines_per_file = int(sys.argv[3]) if len(sys.argv) > 3 else 100

    split_file(input_file, output_dir, lines_per_file)
