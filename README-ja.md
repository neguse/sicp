# SICP 日本語版

計算機プログラムの構造と解釈（Structure and Interpretation of Computer Programs）の日本語翻訳版です。

## 翻訳について

- **翻訳バージョン**: 2.andresraba6.6-ja1
- **翻訳日**: 2025年11月13日
- **元バージョン**: 2.andresraba6.6 (September 16, 2015)
- **翻訳方法**: AI翻訳（Claude）を使用
- **翻訳範囲**: 全コンテンツ（100%完了）

## ファイル構成

- `sicp-pocket-ja.texi` - 日本語版統合ファイル（1.8MB、約32,000行）
- `split/` - 元ファイルを100行ずつに分割したファイル（380ファイル）
- `translated/` - 翻訳済みファイル（380ファイル）
- `split_file.py` - ファイル分割スクリプト
- `merge_translated.py` - ファイル統合スクリプト
- `fix_line_numbers_v2.py` - 行番号修正スクリプト

## ビルド方法

### 必要なツール

- Texinfo 7.1以上
- Perl 5.12以上
- Ruby 1.9.3以上
- Nokogiri gem
- PhantomJS
- インターネット接続

### ビルド手順

1. Makefileを編集:
```bash
# SRC変数を日本語版ファイルに変更
sed -i 's/sicp-pocket\.texi/sicp-pocket-ja.texi/' Makefile
sed -i 's/\.\.\/sicp\.epub/\.\.\/sicp-ja.epub/' Makefile
```

2. ビルド実行:
```bash
make
```

### 既知の問題

現在、以下の構文エラーがあり、ビルドが完全に成功しません：

- 重複した`@node`定義
- 存在しないノードへの参照
- マッチしない`@end`タグ

これらは翻訳とファイル統合プロセスで発生したもので、修正作業が必要です。

## ライセンス

元のSICPと同じく、Creative Commons Attribution-ShareAlike 4.0 International License ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)) の下でライセンスされています。

## 元プロジェクト

- [sicp-epub](https://github.com/sarabander/sicp-epub) - HTML5/EPUB3版のSICPプロジェクト
- [MIT Press SICP](https://mitpress.mit.edu/sicp) - MIT Pressの公式ページ

## 翻訳品質について

本翻訳はAIによる自動翻訳です。技術用語は適切な日本語訳を使用していますが、一部不自然な表現や誤訳が含まれている可能性があります。ご了承ください。

### 翻訳方針

- Texinfoコマンドは変更せず、そのまま保持
- Schemeコードは一切変更せず、コメント含め元のまま保持
- URL、ファイル名、技術的識別子は保持
- 本文のみを日本語に翻訳
- 既存のSICP日本語訳の用語に準拠（procedure→手続き、data→データなど）

## 貢献

翻訳の改善提案やバグ報告は、Issueまたはプルリクエストでお願いします。
