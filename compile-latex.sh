#!/usr/bin/env bash
set -euxo pipefail

curr_dir="$PWD"
compile_dir='/home/leon/texmf/tex/latex/DND-5e-LaTeX-Character-Sheet-Template'

yq '.' higgingbotham.yaml | mustache - template.tex > "$compile_dir/higgingbotham.tex"
