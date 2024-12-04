#!/bin/bash

# Directories
MARKER_DIR="marker_out"
LLM_DIR="textlint_out"
DIFF_DIR="diff"

# Ensure the diff directory exists
mkdir -p "$DIFF_DIR"

# Function to clean embedded picture lines for comparison
clean_file() {
    input_file="$1"
    temp_file="$2"
    # Remove image references (Markdown syntax for images)
    sed '/!\[.*\](.*)/d' "$input_file" >"$temp_file"
}

# Iterate over all Markdown files in marker_out
find "$MARKER_DIR" -type f -name "*.md" | while read -r marker_file; do
    # Generate corresponding file path in llm_out
    relative_path="${marker_file#$MARKER_DIR/}"
    llm_file="$LLM_DIR/$relative_path"
    diff_file="$DIFF_DIR/$relative_path.diff"

    # Ensure the llm_out file exists
    if [ ! -f "$llm_file" ]; then
        echo "No corresponding file for $marker_file in $LLM_DIR. Skipping."
        continue
    fi

    # Ensure the diff output directory exists
    mkdir -p "$(dirname "$diff_file")"

    # Clean the files to ignore image references
    marker_temp=$(mktemp)
    llm_temp=$(mktemp)
    clean_file "$marker_file" "$marker_temp"
    clean_file "$llm_file" "$llm_temp"

    # Generate the diff and save it to the diff directory
    git diff --no-index "$marker_temp" "$llm_temp" >"$diff_file"

    # Clean up temporary files
    rm "$marker_temp" "$llm_temp"

    echo "Diff generated: $diff_file"
done
