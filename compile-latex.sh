#!/usr/bin/env bash

tex_dir="$HOME/texmf/tex/latex/DND-5e-LaTeX-Character-Sheet-Template"

if [ "$(pwd)" != "$tex_dir" ]; then
    echo "Error: Use the script defined in:"
    echo "$tex_dir"
