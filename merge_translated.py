#!/usr/bin/env python3
"""
翻訳済みチャンクファイルを1つのファイルに統合するスクリプト
"""
import os

def merge_files(input_dir, output_file):
    """
    翻訳済みファイルを統合

    Args:
        input_dir: 翻訳済みファイルのディレクトリ
        output_file: 出力ファイルのパス
    """
    # チャンクファイルを番号順にソート
    chunk_files = sorted([
        f for f in os.listdir(input_dir)
        if f.startswith('chunk_') and f.endswith('.texi')
    ])

    print(f'統合するファイル数: {len(chunk_files)}')

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, chunk_file in enumerate(chunk_files):
            chunk_path = os.path.join(input_dir, chunk_file)

            with open(chunk_path, 'r', encoding='utf-8') as infile:
                content = infile.read()
                outfile.write(content)

                # 最後のファイル以外は改行を追加（必要に応じて）
                if i < len(chunk_files) - 1:
                    # ファイルが改行で終わっていない場合のみ追加
                    if not content.endswith('\n'):
                        outfile.write('\n')

            if (i + 1) % 50 == 0:
                print(f'  {i + 1}/{len(chunk_files)} ファイル処理完了')

    print(f'\n統合完了: {output_file}')

    # ファイルサイズを表示
    file_size = os.path.getsize(output_file)
    print(f'ファイルサイズ: {file_size:,} バイト ({file_size / 1024 / 1024:.2f} MB)')

if __name__ == '__main__':
    input_dir = 'translated'
    output_file = 'sicp-pocket-ja.texi'

    merge_files(input_dir, output_file)
