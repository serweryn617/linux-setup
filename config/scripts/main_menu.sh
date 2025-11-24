#!/bin/bash

source ~/.config/scripts/dmenu.sh

declare -A shutdown_menu=(
    ["Run"]=""
    ["Explorer"]="nemo"
    ["Browser"]="firefox"
    ["VS Code"]="code"
    ["Help"]=""
    ["Power"]="i3-msg exit"
)

action=$(printf "%s\n" "${!shutdown_menu[@]}" | dmenu_custom)

if [[ -n "$action" ]]; then
    ${shutdown_menu[$action]}
fi