process_markdown_files() {
    local input_dir="$1"
    local output_dir="$2"

    find "$input_dir" -type f -name "*.md" | while read -r md_file; do
        # 入力ファイルの親親ディレクトリを取得
        parent_parent_dir=$(basename "$(dirname "$(dirname "$md_file")")")
        parent_dir=$(basename "$(dirname "$md_file")")

        # 出力先パスを決定
        relative_path="$parent_parent_dir/$parent_dir/$(basename "$md_file")"
        output_file="$output_dir/$relative_path"
        output_dirname=$(dirname "$output_file")

        # 出力ディレクトリを作成
        mkdir -p "$output_dirname"

        # 元ファイルをコピーして修正先ファイルを準備
        cp "$md_file" "$output_file"

        echo "Processing (fixing): $output_file"

        # コピーしたファイルに修正を適用
        npx textlint --fix "$output_file" >/dev/null 2>&1
        npx textlint --fix "$output_file" >/dev/null 2>&1
        echo "Output saved to: $output_file"
    done
}
