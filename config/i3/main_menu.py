#!/usr/bin/env python3

import dmenu

def run_main_menu():
    options = {
        "Run": "",
        "Explorer": "nemo",
        "Browser": "firefox",
        "VS Code": "code",
        "Help": "",
        "Power": "",
        "Resolution": "",
    }
    dmenu.dmenu(options)

if __name__ == "__main__":
    run_main_menu()