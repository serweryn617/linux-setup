#!/usr/bin/env python3

import colors
import subprocess

DMENU_COMMAND = (
    "dmenu",
    "-c", "-h", "24", "-l", "10", "-bw", "2",
    "-fn", "GitLab Mono",
    "-nb", colors.bg_dark,
    "-nf", colors.text,
    "-sb", colors.darker_gray,
    "-sf", colors.white,
    "-nhf", colors.pink2,
    "-shf", colors.pink1,
    "-nhb", colors.bg_dark,
    "-shb", colors.darker_gray,
    "-bc", colors.green1,
    "-i",
)

def dmenu(options: dict[str, str]):
    proc = subprocess.Popen(
        DMENU_COMMAND,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
    )

    selection, _ = proc.communicate("\n".join(options.keys()))
    selection = selection.strip()
    if selection in options:
        subprocess.Popen(options[selection])