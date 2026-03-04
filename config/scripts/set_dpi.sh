#!/bin/bash

WIDTH=$(xdpyinfo | grep -oP "dimensions:\s+\K\d+")

if [[ "$WIDTH" -ge 3840 ]]; then
    DPI=144
else
    DPI=96
fi

xrdb -merge <(echo "Xft.dpi: $DPI")
