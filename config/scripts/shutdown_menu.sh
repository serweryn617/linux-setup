#!/bin/bash

source ./dmenu.sh

declare -A shutdown_menu=(
    ["Power Off"]="systemctl poweroff"
    ["Suspend"]="systemctl suspend"
    ["Reboot"]="systemctl reboot"
    ["Log Out"]="i3-msg exit"
)

action=$(printf "%s\n" "${!shutdown_menu[@]}" | dmenu_custom)

if [[ -n "$action" ]]; then
    ${shutdown_menu[$action]}
fi