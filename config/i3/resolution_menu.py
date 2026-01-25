#!/usr/bin/env python3

from pathlib import Path
import dmenu

def run_resolution_menu():
    options = {
        "FullHD": ["bash", "-c", Path("~/.config/scripts/res_1080p.sh").expanduser().resolve()],
        "WUXGA": ["bash", "-c", Path("~/.config/scripts/res_1200p.sh").expanduser().resolve()],
        "2K": ["bash", "-c", Path("~/.config/scripts/res_1440p.sh").expanduser().resolve()],
        "4K": ["bash", "-c", Path("~/.config/scripts/res_2160p.sh").expanduser().resolve()],
    }
    dmenu.dmenu(options)

if __name__ == "__main__":
    run_resolution_menu()