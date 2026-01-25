#!/usr/bin/env python3

from pathlib import Path
import dmenu

def run_main_menu():
    options = {
        "Run": "",
        "Explorer": "nemo",
        "Browser": "firefox",
        "VS Code": "code",
        "Resolution": ["python3", Path("~/.config/i3/resolution_menu.py").expanduser().resolve()],
        "Help": "",
        "Power": "",
    }
    dmenu.dmenu(options)

if __name__ == "__main__":
    run_main_menu()