#!/bin/bash

# 入力ディレクトリ
INPUT_DIR="marker_out/random"
# 出力ディレクトリ
OUTPUT_DIR="textlint_out"

# ライブラリの読み込み
source "$(dirname "$0")/../lib/textlint_util.sh"

# npx textlintの確認
if ! npx --no-install textlint -v &>/dev/null; then
    echo "textlintがインストールされていません。プロジェクトにtextlintをインストールしてください。"
    echo "インストールコマンド: npm install textlint --save-dev"
    exit 1
fi

# メイン処理
if [ -d "$INPUT_DIR" ]; then
    echo "校閲を開始します..."
    process_markdown_files "$INPUT_DIR" "$OUTPUT_DIR"
    echo "校閲が完了しました。結果は'$OUTPUT_DIR'に保存されています。"
else
    echo "エラー: 入力ディレクトリ'$INPUT_DIR'が存在しません。"
    exit 1
fi
