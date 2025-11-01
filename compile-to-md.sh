#!/bin/sh

yq '.' higgingbotham.yaml \
    | mustache - template.md > higgingbotham.md
